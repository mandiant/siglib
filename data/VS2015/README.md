# VS14.0 / Visual Studio 2015 / v140

## download

Visual Studio 2019 installer and release channel (used to install Visual Studio 2015 tools):
  - https://aka.ms/vs/16/release/vs_buildtools.exe
  - https://aka.ms/vs/16/release/channel

Install [components](https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019):
  - `Microsoft.VisualStudio.Component.VC.140`: MSVC v140 - VS 2015 C++ build tools (v14.00)

(See [Dockerfile](../../Dockerfile))

This results in:
  - `C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\`: Visual Studio 2015 tools
  - `C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\atlmfc`: C++ MFC for v140 build tools
  - `C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\`: Windows Standalone SDK for Windows 10 from VS2015

We'll ignore the following targets, if present:
  - `arm`
  - `arm64`
  - `store`
  - `onecore`
  - `ucrt_enclave`
  - `uwp`


## .lib/.obj

### compiler: 14.0

```
39c8a778f65656ef8839b56881362137  UnitTest/lib/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
4a8e30837b5a44a7fc70632b8344de7f  UnitTest/lib/amd64/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
193dfc6a2bdfdb2a315f705f7f55b5f3  lib/wsetargv.obj
50fc529c19794acda9859c06649949f4  lib/VsGraphicsHelper.lib
c86daf84c55ac8a893b80c1acf6ef366  lib/vcruntimed.lib
ede62b117642fc600935037deb669630  lib/vcruntime.lib
946cba7ff52b721b6e9c2503566c641b  lib/vcompd.lib
164708bd914a3f921aa7f5957ff701bc  lib/vcomp.lib
2b697e958757bd7a07377f6211780574  lib/vccorlibd.lib
3141f3d164d044d6e9d61f36a0efb1d1  lib/vccorlib.lib
4dfff659dedf0b92b100abad031b99f2  lib/vcampd.lib
e6ffbfb505c915cacaf5a8c9950d40cd  lib/vcamp.lib
d5306869601c80ce38beadf4544dcc96  lib/threadlocale.obj
3d2e39994ae8091b0f753d1d354befc9  lib/setargv.obj
ff8dca22ae76214f19df15a8593ce2f6  lib/pwsetargv.obj
19607538cd3d5613e2441775810b6ac7  lib/ptrustud.lib
8308e76e66b5fb45aeb695899138739e  lib/ptrustu.lib
c141ec328ec38e8ee874e547e236ee57  lib/ptrustmd.lib
7edb13c62e0f2ce0b8726caea195c8a9  lib/ptrustm.lib
e6b677890c7547f48cfa3ea40e512091  lib/pthreadlocale.obj
9a8c7a52bf7d4d7ee39fb1a58e74ee60  lib/psetargv.obj
1b637641ee73847066c781a903a7aafa  lib/pnothrownew.obj
8468e8d23274244deafd8bf40540c850  lib/pnoenv.obj
6c639caa7e3f4ddb6aaf93599585f85f  lib/pnoarg.obj
714fdf0f1205dea5f7026b4ae6148a8f  lib/pnewmode.obj
4c552b0ee799b0f244e3ca777457c811  lib/pinvalidcontinue.obj
68b2ed4fa9dc64988ee79a3475abb030  lib/pgort.lib
b23623400c00fb973350e9a8b1d8ab50  lib/pgobootrun.lib
78cddb68b485a7d4ab38230ef23f1b82  lib/pcommode.obj
9c7c9d697cd1b320a106c214996344fd  lib/pbinmode.obj
23bba27f156b0ad6e5c2676ab514ef7c  lib/oldnames.lib
468f13e3d481066965d1b80b031e5cba  lib/nothrownew.obj
c6ee6b5edafe8671c1bd6bc7f933b894  lib/notelemetry.obj
bdad8ce23c081db7b1a6161d79615bbc  lib/noenv.obj
cc4d642d66466bc088b9df2b572fa369  lib/noarg.obj
abed2feef3fc5742de3b08b5c3d9ddd4  lib/newmode.obj
cbf35ab927f7908ebe24e43e8ef51750  lib/msvcurtd.lib
8109d5a995b18a4dcd011cd49dd3b067  lib/msvcurt.lib
52ac4fe1bf5736ec58bf32d029b359e6  lib/msvcrtd.lib
27f10db674f10bc34633424300d7a785  lib/msvcrt.lib
71596c97f8d6c9ac8b03f30fef5d3a50  lib/msvcprtd.lib
48ae6bd51072d760890fdc49c5581312  lib/msvcprt.lib
8bf525baeac5dfe4e618ed899d5fe8e0  lib/msvcmrtd.lib
b79806de7591fdd6db8d005541a81025  lib/msvcmrt.lib
fd3673204830825ba019fdf46c68a317  lib/loosefpmath.obj
4091c506300368d01bb470e4814a86a9  lib/libvcruntimed.lib
480eba2bc3925e66773c0ebcedef14db  lib/libvcruntime.lib
7f2841a413c4b4faf2aad27097eb6cbb  lib/libcpmtd1.lib
1201d6d0bbf782ac331246e5340af759  lib/libcpmtd0.lib
a60e3b7c00f7b04f54d917c59294fccd  lib/libcpmtd.lib
0d16910cc450458a3164364146e2577e  lib/libcpmt1.lib
cc50f9b05b0808102f1eddf00642d455  lib/libcpmt.lib
3feb27f0314a7973e72752447f7b414e  lib/libconcrtd1.lib
8fef56d66cba05af6444d2340ebbc00d  lib/libconcrtd0.lib
ff8ba12c396977c075907bfe0fd75332  lib/libconcrtd.lib
767cd813669fec97f994c30767ba5039  lib/libconcrt1.lib
ec20bd2d039bbc0cad6f783ab1514e9c  lib/libconcrt.lib
c834109599bd0af776763b649bce4f92  lib/libcmtd.lib
d1cfab7eaf7a198e10bbd44b498eef3c  lib/libcmt.lib
75581a0566edd31a8d8429f7379c3222  lib/legacy_stdio_wide_specifiers.lib
5c3cc56011286c4d83a134ee46e6499d  lib/legacy_stdio_definitions.lib
40dfdf6239dbf99f6404f63692f106d7  atlmfc/lib/uafxcwd.lib
2f23b3e4a8ef16df0772127f97ca5492  atlmfc/lib/uafxcw.lib
4889289d9ded591ca6b4b5c5b4bdebf8  atlmfc/lib/nafxcwd.lib
e9b353e215ff21fbe3cef7fd217e3c87  atlmfc/lib/nafxcw.lib
14b7e6634d3c1ddd97d589e4784039ce  atlmfc/lib/mfcs140ud.lib
7041980d333a87ea0f0fe6b87339ba85  atlmfc/lib/mfcs140u.lib
430577cbb788fa66e57f01a020f69100  atlmfc/lib/mfcs140d.lib
0ab1d4a56500d218042ad3b115ccaa8b  atlmfc/lib/mfcs140.lib
554c2716b2b00a64963f1d63ec74c3b6  atlmfc/lib/MFCM140ud.lib
d8a4b29bf47eb2f953700819f6809912  atlmfc/lib/MFCM140u.lib
5702acc78f04d43105d9cffff05d5ceb  atlmfc/lib/MFCM140d.lib
a24179208af45b5c6fc6d80517ce5187  atlmfc/lib/MFCM140.lib
34ce85da5542c88ad85b26a40a652b96  atlmfc/lib/mfc140ud.lib
284ba744bb193b628390980070d6f3b7  atlmfc/lib/mfc140u.lib
3d9ce777b91846b3aadd32ceb5bbf98b  atlmfc/lib/mfc140d.lib
7840590735a95d9938895f6eec2cba43  atlmfc/lib/mfc140.lib
0b2dca207c032bb743410e1823e3cdc1  atlmfc/lib/atls.lib
ff41b7266c43deb8d55ec33b2970212d  atlmfc/lib/afxnmcdd.lib
2d8c00a6a151744a201fcdbb9e326d14  atlmfc/lib/afxnmcd.lib
7a4f19e43d1e78f4c388a9f66e776edd  lib/iso_stdio_wide_specifiers.lib
748d246e339612c496d1d066ca489af3  lib/invalidcontinue.obj
52468a5517926353b46507bdff64f0ab  atlmfc/lib/amd64/uafxcwd.lib
c36c26ded4dd7a08da5be2642a280a8f  atlmfc/lib/amd64/uafxcw.lib
11f9ac8a02535e7d13360170abf9403b  atlmfc/lib/amd64/nafxcwd.lib
8e0a0767880db9e375e6ae90d2914d20  atlmfc/lib/amd64/nafxcw.lib
1083d76ac0a7f755dd997c17360db69b  atlmfc/lib/amd64/mfcs140ud.lib
267b1eef46ba3a2c2b7d691050dec81d  atlmfc/lib/amd64/mfcs140u.lib
c6831eaf51d6aaf83503b812b59461d7  atlmfc/lib/amd64/mfcs140d.lib
603fc0c949f4913813c2cd67acac1b78  atlmfc/lib/amd64/mfcs140.lib
7e652ef2bd7e3e381d311bf56ccbe0e1  atlmfc/lib/amd64/MFCM140Ud.lib
516b039b0a51b168949204d726541b06  atlmfc/lib/amd64/MFCM140U.lib
9325debf5afb02942a4c1ca2fc143d0b  atlmfc/lib/amd64/MFCM140d.lib
71b15eaadde6a49eb1d812866073e517  atlmfc/lib/amd64/MFCM140.lib
544504a124f4f798570c67c9a61f5d63  atlmfc/lib/amd64/mfc140ud.lib
10c8398dd881e279dc84beaa1178c39a  atlmfc/lib/amd64/mfc140u.lib
10e9f38bf5f1c19d9b07352651f6a676  atlmfc/lib/amd64/mfc140d.lib
edd5fc9c5760b2c6556167ed09e15a48  atlmfc/lib/amd64/mfc140.lib
3957862dc9ed08b62f156f2307fe5b30  atlmfc/lib/amd64/atls.lib
666ba1c7599da750f8bb75c16ec148f9  atlmfc/lib/amd64/afxnmcdd.lib
f0f9220a71fe643756ba512f101f3645  atlmfc/lib/amd64/afxnmcd.lib
8cee88d35e60a8550fce0669c250e279  lib/fp10.obj
6794ea4ee67e7eacbf87c1c6c55b5dee  lib/delayimp.lib
6b78333157cee8c881a99d0f4154ff0c  lib/concrtd.lib
6de0a1111e59d89ec1b11cb9a732474e  lib/concrt.lib
f2bd1a3edff7796c23c2b64410d06c0b  lib/comsuppwd.lib
eba82cdad1523a366c06552443a1a17a  lib/comsuppw.lib
822bf79ee64d7be8a775db984346496b  lib/comsuppd.lib
c05d1edc1f7bd8ac0e59f806a1c40fb8  lib/comsupp.lib
5b635d6ebb2fe3e6aa20815095be403c  lib/commode.obj
117ca1bbc325b7ac3566073ff26ad9e0  lib/chkstk.obj
55e465634ea4b601e22eaad18c23146d  lib/binmode.obj
19d076be9951be3cdd2100f82c479400  lib/amd64/libconcrt.lib
ee5378bc6362e0f084da75b3d89a02f9  lib/amd64/msvcurt.lib
ae5ec7624235773add0cb662873aed7b  lib/amd64/msvcurtd.lib
9bed56b79d15e7395c1e7962d830b9ac  lib/amd64/newmode.obj
a83ca5c69c3000654a8f7a28db883afb  lib/amd64/pnewmode.obj
4ddc7dd9339a08dea239e8fb943b698f  lib/amd64/pnoenv.obj
d71452a703dfac3ff9f4b5cce636b95c  lib/amd64/psetargv.obj
86530a7ffbe68e497dd409bee24234b7  lib/amd64/ptrustm.lib
485ff473275a80be2d8d45eaba6b1be3  lib/amd64/ptrustmd.lib
4ea37bc63a54f5c23732b723af9de717  lib/amd64/ptrustu.lib
96ccc132f21beb56ff5bd17b838889b8  lib/amd64/ptrustud.lib
56d81b394518729a86aeaf27439e4429  lib/amd64/pwsetargv.obj
e2338e38c61c3a8dddf96ab456968aa3  lib/amd64/setargv.obj
58d7a3fcd7bb9dcff3b28ac5a915d529  lib/amd64/vcamp.lib
f60dad8ddfa3f95cffa2dea8b573a057  lib/amd64/vccorlib.lib
fc6296758d82e65b17f37f9b16d7822a  lib/amd64/vccorlibd.lib
eb3ba6cd5d839dfdad7c0c9be8310a5b  lib/amd64/vcomp.lib
7ce90d7ad43f7a8ce0caf08edabc9e25  lib/amd64/wsetargv.obj
50d10ab7e9f8b3d539c6c21386a9c1e4  lib/amd64/VsGraphicsHelper.lib
8f363c186461449a672f6a2eddb23561  lib/amd64/vcruntimed.lib
38e3a198e166b851e862f5b7f2bad2da  lib/amd64/vcruntime.lib
87fd14c969640a16ee51a61c9a9843b5  lib/amd64/vcompd.lib
98291585e789c6657de5616b51119cc4  lib/amd64/vcampd.lib
9c213db901274d6a13ab4800d1275bda  lib/amd64/threadlocale.obj
185229853a80b079318b027a7843bcbd  lib/amd64/pthreadlocale.obj
a5a85c621374d5d28221bc075fb1aed2  lib/amd64/pnothrownew.obj
b0054a777021663a813d73b99098e35e  lib/amd64/pnoarg.obj
a01359b77088df96bce021e6888c2eac  lib/amd64/pinvalidcontinue.obj
0f27024c2a8f5f680677f524283a2324  lib/amd64/pgort.lib
dabfbfd1cda1ebe4b68dc64fe3da0f0a  lib/amd64/pgobootrun.lib
9e04a8e3a2a66a59d43145041b06690d  lib/amd64/pcommode.obj
dd25b768b48eb4ccdbbeaf4577de56cf  lib/amd64/pbinmode.obj
3f187383c95aebe83125dbbe56df77e2  lib/amd64/oldnames.lib
16d5f8a17420cfe3ccdcece9df807264  lib/amd64/nothrownew.obj
848d2aeb74337fb42527147328c3e256  lib/amd64/notelemetry.obj
d0654db5897708a397b76e5a9d8c4a9f  lib/amd64/noenv.obj
0dd92112cddf33ec21f1bdde76271814  lib/amd64/noarg.obj
30dd8ae54368a3087cfdc610144114aa  lib/amd64/msvcrtd.lib
aa964bcd49976fab89e59b8413a1b4a1  lib/amd64/msvcrt.lib
9858649bfab4738c9740e3cc188a4e6f  lib/amd64/msvcprtd.lib
7ce0da12b5af15a3610a462fe1662f7a  lib/amd64/msvcprt.lib
35fb58b91a909bfb494313b5b5191a30  lib/amd64/msvcmrtd.lib
d30fd183f0055eee68b2ae6df5f0a6ec  lib/amd64/msvcmrt.lib
f0221b9624eac12839b113f7958907df  lib/amd64/loosefpmath.obj
90b8774038dffafb3e388586ef3af400  lib/amd64/libvcruntimed.lib
d725fe6e9a05ca90dc0fc56b5ae43a93  lib/amd64/libvcruntime.lib
39739f94c01b55ab0829068bef425d52  lib/amd64/libcpmtd1.lib
84f49a11afa01cdb84ee2a5a415db2cf  lib/amd64/libcpmtd0.lib
a217f9dfac9afacdaf356a5c2cfa13b5  lib/amd64/libcpmtd.lib
136599c73ab696748dfb3c0f2ac83ae2  lib/amd64/libcpmt1.lib
f2f41e3be2fba4bcdff9b9182ea45552  lib/amd64/libcpmt.lib
7be07f6e01442a56ab1d4995f1eb890b  lib/amd64/libconcrtd1.lib
35cfc4f7d9c6984ff4a0bddfdee20e0e  lib/amd64/libconcrtd0.lib
152a1db0fd330946293596a3fad89b99  lib/amd64/libconcrtd.lib
9ac70c4a284a39bb77612dfc4fde81f9  lib/amd64/libconcrt1.lib
f6d3e3400e5304228cec09d63b9209e3  lib/amd64/libcmtd.lib
eab319e6f38fba7c93aab06bb9e1b046  lib/amd64/libcmt.lib
748b0f8040822083b30006028002bafd  lib/amd64/legacy_stdio_wide_specifiers.lib
dc6921b0e5d2f1b52f3caef082cd2c19  lib/amd64/legacy_stdio_definitions.lib
54f716cf45d6428311940a9b1319d961  lib/amd64/iso_stdio_wide_specifiers.lib
b525bc329562eeba32bfbec45a7aa26c  lib/amd64/invalidcontinue.obj
715287ae88ad448d8e3ca3b9d5c94479  lib/amd64/delayimp.lib
b5ecad3b3aea79882ab3fa9358b7e008  lib/amd64/concrtd.lib
2d464a4b0854eeeeca99a28ff9d2e5f7  lib/amd64/concrt.lib
3e2be9b52d8a2d5a3ff23c3a68dfcacc  lib/amd64/comsuppwd.lib
7b13fe0222be9d4379b0ed888372e6ab  lib/amd64/comsuppw.lib
627b3ad031f1bb6fde0e7c9cd52af17f  lib/amd64/comsuppd.lib
5d739cc055826fa38f08fd3b70b54bb5  lib/amd64/comsupp.lib
593d0c8dbe614850b77289cdc14e7e53  lib/amd64/commode.obj
f512fbf93b152886d18e188e5daca530  lib/amd64/chkstk.obj
65874f04cee23c628eb062bd8d8efcda  lib/amd64/binmode.obj
```

### ucrt: 10.0.10240.0

```
16f93b7e2c612ae84b96ce46a5bdd637  10.0.10240.0/ucrt/x64/libucrt.lib
92dcd14f9d99f4ce36619b201ea0b7d0  10.0.10240.0/ucrt/x64/libucrtd.lib
f83e39d7cbe39437fb0202c7a8c36c83  10.0.10240.0/ucrt/x64/ucrt.lib
91675612f322b415e42f0b89e229fa4a  10.0.10240.0/ucrt/x64/ucrtd.lib
0fb2c1d5ade60005456b447a285368d7  10.0.10240.0/ucrt/x86/libucrt.lib
2065fcdf73bc47dd90d3c8834ac5486d  10.0.10240.0/ucrt/x86/libucrtd.lib
7910ea07c7110572c1427c587ea501b6  10.0.10240.0/ucrt/x86/ucrt.lib
93468959d04c958338ff99f5331757ff  10.0.10240.0/ucrt/x86/ucrtd.lib
```

## .pat

pcf version:
```
COFF parser. Copyright (c) 1997-2019 Hex-Rays SA. Version 1.23
Usage: pcf [-switch or @file or $env_var] file [pattern-file]
        (wildcards are allowed)
```

### compiler: 14.0

```
atlmfc/lib/afxnmcd.lib: skipped 18, total 152
atlmfc/lib/afxnmcdd.lib: skipped 0, total 269
atlmfc/lib/amd64/afxnmcd.lib: skipped 40, total 148
atlmfc/lib/amd64/afxnmcdd.lib: skipped 6, total 264
atlmfc/lib/amd64/atls.lib: skipped 27, total 79
atlmfc/lib/amd64/mfc140.lib: skipped 14638, total 14638
atlmfc/lib/amd64/mfc140d.lib: skipped 17149, total 17149
atlmfc/lib/amd64/mfc140u.lib: skipped 17345, total 17345
atlmfc/lib/amd64/mfc140ud.lib: skipped 20273, total 20273
atlmfc/lib/amd64/MFCM140.lib: skipped 25, total 41
atlmfc/lib/amd64/MFCM140d.lib: skipped 31, total 47
atlmfc/lib/amd64/MFCM140U.lib: skipped 27, total 43
atlmfc/lib/amd64/MFCM140Ud.lib: skipped 33, total 49
atlmfc/lib/amd64/mfcs140.lib: skipped 243, total 844
atlmfc/lib/amd64/mfcs140d.lib: skipped 28, total 1364
atlmfc/lib/amd64/mfcs140u.lib: skipped 266, total 867
atlmfc/lib/amd64/mfcs140ud.lib: skipped 57, total 1329
atlmfc/lib/amd64/nafxcw.lib: skipped 6025, total 58774
atlmfc/lib/amd64/nafxcwd.lib: skipped 1036, total 67066
atlmfc/lib/amd64/uafxcw.lib: skipped 7944, total 59874
atlmfc/lib/amd64/uafxcwd.lib: skipped 2953, total 66305
atlmfc/lib/atls.lib: skipped 4, total 1102
atlmfc/lib/mfc140.lib: skipped 14998, total 14998
atlmfc/lib/mfc140d.lib: skipped 17545, total 17545
atlmfc/lib/mfc140u.lib: skipped 17936, total 17936
atlmfc/lib/mfc140ud.lib: skipped 20900, total 20900
atlmfc/lib/MFCM140.lib: skipped 25, total 41
atlmfc/lib/MFCM140d.lib: skipped 32, total 48
atlmfc/lib/MFCM140u.lib: skipped 27, total 43
atlmfc/lib/MFCM140ud.lib: skipped 34, total 50
atlmfc/lib/mfcs140.lib: skipped 60, total 881
atlmfc/lib/mfcs140d.lib: skipped 11, total 1410
atlmfc/lib/mfcs140u.lib: skipped 83, total 904
atlmfc/lib/mfcs140ud.lib: skipped 38, total 1375
atlmfc/lib/nafxcw.lib: skipped 6944, total 60050
atlmfc/lib/nafxcwd.lib: skipped 344, total 68379
atlmfc/lib/uafxcw.lib: skipped 8677, total 61278
atlmfc/lib/uafxcwd.lib: skipped 2376, total 67738
lib/amd64/binmode.obj: skipped 0, total 1
lib/amd64/chkstk.obj: skipped 0, total 1
lib/amd64/commode.obj: skipped 0, total 1
lib/amd64/comsupp.lib: skipped 4, total 30
lib/amd64/comsuppd.lib: skipped 4, total 32
lib/amd64/comsuppw.lib: skipped 4, total 30
lib/amd64/comsuppwd.lib: skipped 4, total 32
lib/amd64/concrt.lib: skipped 291, total 291
lib/amd64/concrtd.lib: skipped 291, total 291
lib/amd64/delayimp.lib: skipped 5, total 33
lib/amd64/invalidcontinue.obj: skipped 1, total 2
lib/amd64/iso_stdio_wide_specifiers.lib: skipped 0, total 3
lib/amd64/legacy_stdio_definitions.lib: skipped 8, total 231
lib/amd64/legacy_stdio_wide_specifiers.lib: skipped 0, total 3
lib/amd64/libcmt.lib: skipped 155, total 554
lib/amd64/libcmtd.lib: skipped 146, total 555
lib/amd64/libconcrt.lib: skipped 555, total 5519
lib/amd64/libconcrt1.lib: skipped 553, total 5519
lib/amd64/libconcrtd.lib: skipped 17, total 5734
lib/amd64/libconcrtd0.lib: skipped 17, total 5734
lib/amd64/libconcrtd1.lib: skipped 17, total 5734
lib/amd64/libcpmt.lib: skipped 1292, total 7596
lib/amd64/libcpmt1.lib: skipped 1605, total 8399
lib/amd64/libcpmtd.lib: skipped 6, total 9069
lib/amd64/libcpmtd0.lib: skipped 6, total 7926
lib/amd64/libcpmtd1.lib: skipped 6, total 8766
lib/amd64/libvcruntime.lib: skipped 18, total 428
lib/amd64/libvcruntimed.lib: skipped 4, total 431
lib/amd64/loosefpmath.obj: skipped 0, total 1
lib/amd64/msvcmrt.lib: skipped 274, total 574
lib/amd64/msvcmrtd.lib: skipped 274, total 579
lib/amd64/msvcprt.lib: skipped 1515, total 1528
lib/amd64/msvcprtd.lib: skipped 1524, total 1542
lib/amd64/msvcrt.lib: skipped 299, total 698
lib/amd64/msvcrtd.lib: skipped 290, total 699
lib/amd64/msvcurt.lib: skipped 1860, total 26712
lib/amd64/msvcurtd.lib: skipped 1868, total 28499
lib/amd64/newmode.obj: skipped 0, total 1
lib/amd64/noarg.obj: skipped 3, total 3
lib/amd64/noenv.obj: skipped 3, total 3
lib/amd64/notelemetry.obj: skipped 4, total 4
lib/amd64/nothrownew.obj: skipped 0, total 4
lib/amd64/oldnames.lib: skipped 228, total 228
lib/amd64/pbinmode.obj: skipped 0, total 1
lib/amd64/pcommode.obj: skipped 0, total 1
lib/amd64/pgobootrun.lib: skipped 2, total 2
lib/amd64/pgort.lib: skipped 9, total 18
lib/amd64/pinvalidcontinue.obj: skipped 0, total 4
lib/amd64/pnewmode.obj: skipped 0, total 1
lib/amd64/pnoarg.obj: skipped 0, total 3
lib/amd64/pnoenv.obj: skipped 0, total 3
lib/amd64/pnothrownew.obj: skipped 0, total 8
lib/amd64/psetargv.obj: skipped 0, total 1
lib/amd64/pthreadlocale.obj: skipped 0, total 1
lib/amd64/ptrustm.lib: skipped 0, total 185
lib/amd64/ptrustmd.lib: skipped 0, total 186
lib/amd64/ptrustu.lib: skipped 0, total 111
lib/amd64/ptrustud.lib: skipped 0, total 111
lib/amd64/pwsetargv.obj: skipped 0, total 1
lib/amd64/setargv.obj: skipped 0, total 1
lib/amd64/threadlocale.obj: skipped 1, total 1
lib/amd64/vcamp.lib: skipped 165, total 165
lib/amd64/vcampd.lib: skipped 166, total 166
lib/amd64/vccorlib.lib: skipped 287, total 559
lib/amd64/vccorlibd.lib: skipped 280, total 566
lib/amd64/vcomp.lib: skipped 113, total 113
lib/amd64/vcompd.lib: skipped 113, total 113
lib/amd64/vcruntime.lib: skipped 71, total 71
lib/amd64/vcruntimed.lib: skipped 71, total 71
lib/amd64/VsGraphicsHelper.lib: skipped 10, total 10
lib/amd64/wsetargv.obj: skipped 0, total 1
lib/binmode.obj: skipped 0, total 1
lib/chkstk.obj: skipped 0, total 1
lib/commode.obj: skipped 0, total 1
lib/comsupp.lib: skipped 4, total 30
lib/comsuppd.lib: skipped 0, total 30
lib/comsuppw.lib: skipped 4, total 30
lib/comsuppwd.lib: skipped 0, total 30
lib/concrt.lib: skipped 291, total 291
lib/concrtd.lib: skipped 291, total 291
lib/delayimp.lib: skipped 0, total 34
lib/fp10.obj: skipped 0, total 1
lib/invalidcontinue.obj: skipped 1, total 2
lib/iso_stdio_wide_specifiers.lib: skipped 0, total 3
lib/legacy_stdio_definitions.lib: skipped 8, total 231
lib/legacy_stdio_wide_specifiers.lib: skipped 0, total 3
lib/libcmt.lib: skipped 161, total 562
lib/libcmtd.lib: skipped 132, total 563
lib/libconcrt.lib: skipped 622, total 5675
lib/libconcrt1.lib: skipped 620, total 5675
lib/libconcrtd.lib: skipped 0, total 5930
lib/libconcrtd0.lib: skipped 0, total 5930
lib/libconcrtd1.lib: skipped 0, total 5930
lib/libcpmt.lib: skipped 1065, total 7770
lib/libcpmt1.lib: skipped 1204, total 8611
lib/libcpmtd.lib: skipped 0, total 9420
lib/libcpmtd0.lib: skipped 0, total 8215
lib/libcpmtd1.lib: skipped 0, total 9101
lib/libvcruntime.lib: skipped 23, total 425
lib/libvcruntimed.lib: skipped 0, total 426
lib/loosefpmath.obj: skipped 0, total 1
lib/msvcmrt.lib: skipped 276, total 576
lib/msvcmrtd.lib: skipped 276, total 581
lib/msvcprt.lib: skipped 1515, total 1529
lib/msvcprtd.lib: skipped 1523, total 1543
lib/msvcrt.lib: skipped 306, total 708
lib/msvcrtd.lib: skipped 277, total 709
lib/msvcurt.lib: skipped 1871, total 26677
lib/msvcurtd.lib: skipped 1879, total 28464
lib/newmode.obj: skipped 1, total 1
lib/noarg.obj: skipped 3, total 3
lib/noenv.obj: skipped 3, total 3
lib/notelemetry.obj: skipped 4, total 4
lib/nothrownew.obj: skipped 0, total 4
lib/oldnames.lib: skipped 228, total 228
lib/pbinmode.obj: skipped 0, total 1
lib/pcommode.obj: skipped 0, total 1
lib/pgobootrun.lib: skipped 2, total 2
lib/pgort.lib: skipped 13, total 29
lib/pinvalidcontinue.obj: skipped 0, total 4
lib/pnewmode.obj: skipped 0, total 1
lib/pnoarg.obj: skipped 0, total 3
lib/pnoenv.obj: skipped 0, total 3
lib/pnothrownew.obj: skipped 0, total 8
lib/psetargv.obj: skipped 0, total 1
lib/pthreadlocale.obj: skipped 0, total 1
lib/ptrustm.lib: skipped 0, total 185
lib/ptrustmd.lib: skipped 0, total 186
lib/ptrustu.lib: skipped 0, total 111
lib/ptrustud.lib: skipped 0, total 111
lib/pwsetargv.obj: skipped 0, total 1
lib/setargv.obj: skipped 1, total 1
lib/threadlocale.obj: skipped 1, total 1
lib/vcamp.lib: skipped 165, total 165
lib/vcampd.lib: skipped 166, total 166
lib/vccorlib.lib: skipped 283, total 558
lib/vccorlibd.lib: skipped 280, total 567
lib/vcomp.lib: skipped 113, total 113
lib/vcompd.lib: skipped 113, total 113
lib/vcruntime.lib: skipped 80, total 80
lib/vcruntimed.lib: skipped 80, total 80
lib/VsGraphicsHelper.lib: skipped 10, total 10
lib/wsetargv.obj: skipped 1, total 1
UnitTest/lib/amd64/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib: skipped 20, total 20
UnitTest/lib/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib: skipped 20, total 20
```

### ucrt: 10.0.10240.0

```
ucrt/x64/libucrt.lib: skipped 756, total 8005
ucrt/x64/libucrtd.lib: skipped 280, total 8194
ucrt/x64/ucrt.lib: skipped 1351, total 1351
ucrt/x64/ucrtd.lib: skipped 1414, total 1414
ucrt/x86/libucrt.lib: skipped 566, total 7841
ucrt/x86/libucrtd.lib: skipped 194, total 8010
ucrt/x86/ucrt.lib: skipped 1378, total 1378
ucrt/x86/ucrtd.lib: skipped 1441, total 1441
```
