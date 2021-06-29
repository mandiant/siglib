"""
create a .sig file from .pat files stored in tarballs
optionally excludes tarball paths and includes pat file names

example runs:
  $ python3 create_sig.py -d -e libraries test -i libc msvc --tarballs-root data/ -- outdir/
    -d - output debugging messages
    -e - exclude paths containing string `libraries` or `test`
    -ip - include pat files containing `libc` and `msvc`
    --tarballs-root - root path storing tarballs containing .pat files
    --
    data/ - root path of tarballs
    outdir/ - path to output files

  $ python3 create_sig.py --patfiles data/VS6/vc98/lib/libc*.pat -- outdir/
    --patfiles - paths to .pat files
    --
    outdir/ - path to output files
"""

import os
import shutil
import sys
import logging
import tarfile
import argparse
import subprocess


logger = logging.getLogger(__name__)


# the patched sigmake doesn't complain about number of leaves
PATH_SIGMAKE = os.path.abspath("../sigmake_patched.exe")
PATH_ZIPSIG = os.path.abspath("../zipsig.exe")

SIGNAME_DEFAULT = "(sigfile)"


def collect_tarball_paths(path, exclude=None):
    """
    return all tarballs recursively collected starting from path
    exclude specifies a list of strings used to filter out paths
    """
    tarball_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(".tar.gz"):
                continue

            tarball_path = os.path.join(root, file)

            if exclude:
                skip = False
                for exc in exclude:
                    if exc in tarball_path:
                        skip = True
                        break
                if skip:
                    logger.debug(f" [-] skipping {tarball_path}")
                    continue

            tarball_paths.append(tarball_path)
    return tarball_paths


def extract_pat_files(outdir, tarball_path, exclude=None, include=None, write_files=True):
    """
    extract all .pat files from a tarball to output directory
    """
    tar = tarfile.open(tarball_path, "r:gz")
    for m in tar.getmembers():
        if not m.name.endswith(".pat"):
            continue

        if exclude:
            skip = False
            for exc in exclude:
                if exc in m.name:
                    skip = True
                    break
            if skip:
                logger.debug(f" [-] skipping {m.name}")
                continue

        if include:
            for inc in include:
                if inc in m.name:
                    if write_files:
                        write_tar_member(outdir, tar, m)
                    else:
                        logger.debug(f" [+] {m.name}")
        else:
            if write_files:
                write_tar_member(outdir, tar, m)
            else:
                logger.debug(f" [+] {m.name}")
    return 0


def write_tar_member(outdir, tar, m):
    """
    write file from tarball to output directory
    """
    outpath = os.path.join(outdir, flatten_path(m.name))
    logger.debug(" writing %s", outpath)
    with open(outpath, "wb") as f:
        f.write(tar.extractfile(m).read())


def flatten_path(name):
    # tarballs may store directory structure, e.g. VS6.tar.gz/VS6.tar/VS6/vc98/lib/libc.lib.pat
    name = name.replace("/", "-")
    return name


def create_sig_file_from_pats(outdir, outsigfile, patfiles, signame, reject_functions, ignore_functions):
    """
    convenience functionality around IDA's sigmake
    """
    outsigfile = os.path.join(outdir, outsigfile)

    reject_functions = [f"-lr{rf}" for rf in reject_functions] if reject_functions else []
    ignore_functions = [f"-li{igf}" for igf in ignore_functions] if ignore_functions else []

    # use multiple -v for more verbosity, two appears to be max
    args = (
        [PATH_SIGMAKE, "-v", "-v"] + [f'-n"{signame}"'] + reject_functions + ignore_functions + patfiles + [outsigfile]
    )
    logfile = open(os.path.join(outdir, "run1.log"), "wb")
    r = run(args, stdout=logfile, stderr=logfile)
    logfile.close()

    exc_file = os.path.splitext(outsigfile)[0] + ".exc"
    if not os.path.exists(exc_file):
        raise ValueError(f"sigmake failed, check {logfile.name} - did not create exclusion file {exc_file}")

    process_exc_file(exc_file)

    logfile = open(os.path.join(outdir, "run2.log"), "wb")
    run(args, stdout=logfile, stderr=logfile)
    logfile.close()

    if not os.path.exists(outsigfile):
        raise ValueError(f"did not create {outsigfile}")

    return outsigfile


def create_temp_pat_files(outdir, files):
    temp_pat_files = []
    for i, f in enumerate(files):
        new = os.path.join(outdir, f"{i}.pat")
        shutil.copy(f, new)
        temp_pat_files.append(new)
    return temp_pat_files


def run(args, cwd=os.curdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    logger.debug("running %s", " ".join(args))
    p = subprocess.Popen(args, cwd=cwd, stdout=stdout, stderr=stderr)
    # wait
    p.communicate()


def process_exc_file(exc_file):
    """
    process exclusion file
    """
    with open(exc_file, "rb") as f:
        lines = f.read().splitlines(keepends=True)

    include_functions = (
        "__CxxFrameHandler3",
        "__strdup",
        "mainCRTStartup",
        "_mainCRTStartup",
    )
    new_lines = []
    for line in lines:
        line = line.decode("utf-8")
        if line.startswith(include_functions):
            line = "+" + line
            new_lines.append(line.encode("utf-8"))
        else:
            # TODO
            # __iswblank_l                                            00 0000 8BFF558BEC66837D08096A407503585DC3FF7508E8........59595DC3......
            # _iswblank                                               00 0000 8BFF558BEC66837D08096A407503585DC3FF7508E8........59595DC3......

            # TODO
            # __Toupper                                         	30 7B17 558BEC518B450C5385C056750D8B35........A1........EB058B308B400485
            # __Toupper_lk                                      	30 7B17 558BEC518B450C5385C056750D8B35........A1........EB058B308B400485

            new_lines.append(line.encode("utf-8"))

    # remove header
    with open(exc_file, "wb") as f:
        f.writelines(new_lines[5:])


def zipsig(outsigfile, save_unzipped_file=True):
    if save_unzipped_file:
        unzipped_file = f"{outsigfile}.bu"
        logger.info(f"saving unzipped file as {unzipped_file}")
        shutil.copy(outsigfile, unzipped_file)

    args = [PATH_ZIPSIG, outsigfile]
    run(args)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        "outdir",
        type=str,
        help="path to output directory",
    )
    parser.add_argument("-e", "--exclude", nargs="*", help="exclude paths that contain exclusion string")
    parser.add_argument("-ep", "--exclude_pats", nargs="*", help="exclude pat files that contain exclusion string")
    parser.add_argument("-ip", "--include_pats", nargs="*", help="include pat files that contain inclusion string")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--tarballs-root", help="data path to root of tarballs, use with -e and -i")
    group.add_argument("--patfiles", nargs="+", help="paths to input .pat files")
    parser.add_argument(
        "-s", "--sigfile", required=True, help="name of output .sig file, e.g. flare_msvc_rtf_32_64.sig"
    )
    parser.add_argument(
        "-N",
        "--no-act",
        action="store_true",
        help="don't make any changes, use with --debug to view selected .pat files",
    )
    parser.add_argument("-n", "--signame", default=SIGNAME_DEFAULT, help="signature file title (used by IDA)")
    parser.add_argument("-lr", "--reject_functions", action="append", help="reject functions matching the pattern")
    parser.add_argument("-li", "--ignore_functions", action="append", help="ignore functions when comparing leaves")
    # logging modes
    parser.add_argument("-d", "--debug", action="store_true", help="enable debugging output on STDERR")
    parser.add_argument("-q", "--quiet", action="store_true", help="disable all output but errors")
    args = parser.parse_args(args=argv)

    if args.quiet:
        logging.basicConfig(level=logging.WARNING)
        logging.getLogger().setLevel(logging.WARNING)
    elif args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().setLevel(logging.INFO)

    if args.patfiles and (args.exclude or args.exclude_pats or args.include_pats or args.no_act):
        logger.error("-e, -ep, -ip, -N arguments can only be used with --tarballs-root")
        return -1

    if args.no_act:
        for tarball_path in collect_tarball_paths(args.tarballs_root, exclude=args.exclude):
            logger.debug("extracting from %s", tarball_path)
            extract_pat_files(
                args.outdir, tarball_path, exclude=args.exclude_pats, include=args.include_pats, write_files=False
            )
        return 0

    if os.path.exists(args.outdir):
        logger.error("%s already exists", args.outdir)
        return -1
    else:
        logger.info("creating output directory %s", args.outdir)
        os.mkdir(args.outdir)

    if args.signame == SIGNAME_DEFAULT:
        args.signame = args.sigfile.replace("-", " ").replace("_", " ").replace(".sig", "").upper()

    if args.tarballs_root:
        logger.info("collecting tarball paths")
        for tarball_path in collect_tarball_paths(args.tarballs_root, exclude=args.exclude):
            logger.debug("extracting from %s", tarball_path)
            extract_pat_files(args.outdir, tarball_path, exclude=args.exclude_pats, include=args.include_pats)
        # rely on wildcard extension after copying files to outdir
        patfiles = [os.path.join(args.outdir, "*.pat")]
    else:
        logger.info("using provided .pat files")
        patfiles = args.patfiles

    logger.info("creating sig file %s", args.sigfile)
    try:
        sigpath = create_sig_file_from_pats(
            args.outdir, args.sigfile, patfiles, args.signame, args.reject_functions, args.ignore_functions
        )
    except ValueError as e:
        logger.error(str(e))
        return -1

    logger.info("zipping sig file %s", sigpath)
    zipsig(sigpath, save_unzipped_file=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
