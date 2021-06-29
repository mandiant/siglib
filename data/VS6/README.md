# VS 6.0 / Visual Studio 6

## download
Service Pack 6 for Visual Basic 6.0, Visual C++ 6.0 with Visual Source Safe 6.0d http://www.microsoft.com/en-us/download/details.aspx?id=9183

## prepare
```
$ 7z x Vs6sp6.exe -oVs6sp6
$ cd Vs6sp6
$ 7z x VS6sp61.cab -oVS6sp61
```

## .lib/.obj
```
$ find Vs6sp61/ -iname "*.lib"
Vs6sp61/vc98/lib/atl.lib
Vs6sp61/vc98/lib/atldload.lib
Vs6sp61/vc98/lib/comsupp.lib
Vs6sp61/vc98/lib/libc.lib
Vs6sp61/vc98/lib/libcd.lib
Vs6sp61/vc98/lib/libcimt.lib
Vs6sp61/vc98/lib/libcimtd.lib
Vs6sp61/vc98/lib/libcmt.lib
Vs6sp61/vc98/lib/libcmtd.lib
Vs6sp61/vc98/lib/libcp.lib
Vs6sp61/vc98/lib/libcpd.lib
Vs6sp61/vc98/lib/libcpmt.lib
Vs6sp61/vc98/lib/libcpmtd.lib
Vs6sp61/vc98/lib/mfcdload.lib
Vs6sp61/vc98/lib/msvcprt.lib
Vs6sp61/vc98/lib/msvcprtd.lib
Vs6sp61/vc98/lib/msvcrt.lib
Vs6sp61/vc98/lib/msvcrtd.lib
Vs6sp61/vc98/lib/oleaut32.lib
Vs6sp61/vc98/lib/uuid.Lib
Vs6sp61/vc98/mfc/lib/eafxis.lib
Vs6sp61/vc98/mfc/lib/eafxisd.lib
Vs6sp61/vc98/mfc/lib/mfc42.lib
Vs6sp61/vc98/mfc/lib/mfc42d.lib
Vs6sp61/vc98/mfc/lib/mfc42u.lib
Vs6sp61/vc98/mfc/lib/mfc42ud.lib
Vs6sp61/vc98/mfc/lib/mfcd42d.lib
Vs6sp61/vc98/mfc/lib/mfcd42ud.lib
Vs6sp61/vc98/mfc/lib/mfcn42d.lib
Vs6sp61/vc98/mfc/lib/mfcn42ud.lib
Vs6sp61/vc98/mfc/lib/mfco42d.lib
Vs6sp61/vc98/mfc/lib/mfco42ud.lib
Vs6sp61/vc98/mfc/lib/mfcs42.lib
Vs6sp61/vc98/mfc/lib/mfcs42d.lib
Vs6sp61/vc98/mfc/lib/mfcs42u.lib
Vs6sp61/vc98/mfc/lib/mfcs42ud.lib
Vs6sp61/vc98/mfc/lib/nafxcw.lib
Vs6sp61/vc98/mfc/lib/nafxcwd.lib
Vs6sp61/vc98/mfc/lib/nafxis.lib
Vs6sp61/vc98/mfc/lib/nafxisd.lib
Vs6sp61/vc98/mfc/lib/uafxcw.lib
Vs6sp61/vc98/mfc/lib/uafxcwd.lib
```

```
$ find VS6/ -type f \( -iname "*.lib" -o -iname "*.obj" \) -exec md5sum {} \;
9b05ab7aaa93e32ff5d5d449956da75c *VS6/vc98/lib/atl.lib
cc1107eb2cfc0381ea2eb649528b2714 *VS6/vc98/lib/atldload.lib
79787ea71e1a922533f11966a851da6c *VS6/vc98/lib/comsupp.lib
d7b98b1a1acb7830c0492a5a6c067aae *VS6/vc98/lib/libc.lib
9afe7b97ba936b5e0c48b912b2b42b87 *VS6/vc98/lib/libcd.lib
3137d04020f1caa342db588e9c0cdacb *VS6/vc98/lib/libcimt.lib
bae8a55e608457ceb8f4254080df0c92 *VS6/vc98/lib/libcimtd.lib
2cfcb0ef30f936e434d7d3be11bef2c7 *VS6/vc98/lib/libcmt.lib
b9e55116a92eb94a449ca041c185b4a3 *VS6/vc98/lib/libcmtd.lib
8dbda62901721e2569853189d1b5d967 *VS6/vc98/lib/libcp.lib
84f9ff2267dc6d42514c369c0d7aed00 *VS6/vc98/lib/libcpd.lib
ef2f398fb9522fb133070ffb5741ae90 *VS6/vc98/lib/libcpmt.lib
b437028fd12ce3db5baf857c21ac0718 *VS6/vc98/lib/libcpmtd.lib
c14017070b936450624b68ab9105ce18 *VS6/vc98/lib/mfcdload.lib
07dfa8c351b6481c92ac8a9aaab1f125 *VS6/vc98/lib/msvcprt.lib
571aee70ce8d993094157957398b5f04 *VS6/vc98/lib/msvcprtd.lib
380dd6cd28ab53a7e22ad9bf902135fd *VS6/vc98/lib/msvcrt.lib
336549a15d5b8d389a29c573ccba6846 *VS6/vc98/lib/msvcrtd.lib
135f80bfd86282a3f4839f5068a644d0 *VS6/vc98/lib/oleaut32.lib
04a5b553bab6262f23ea48bba019165e *VS6/vc98/lib/uuid.Lib
c684515f45bf38f04d34aad7eae8403e *VS6/vc98/mfc/lib/eafxis.lib
f766a94ba675888422bdbeaf0482ded4 *VS6/vc98/mfc/lib/eafxisd.lib
8fd4f98083966eddf8967c0a341460d8 *VS6/vc98/mfc/lib/mfc42.lib
86d23d9f9912c2b537e7b1eff2668c0d *VS6/vc98/mfc/lib/mfc42d.lib
5e5207805a1b32c9df95401809318303 *VS6/vc98/mfc/lib/mfc42u.lib
420ed41422127281b66c7756b5ad76f1 *VS6/vc98/mfc/lib/mfc42ud.lib
f82d2928c22175976411bd2a194d6da6 *VS6/vc98/mfc/lib/mfcd42d.lib
5367557a95a892059f96c6473f2cce38 *VS6/vc98/mfc/lib/mfcd42ud.lib
e78a6d21bd075a193e4ba3c358a149ca *VS6/vc98/mfc/lib/mfcn42d.lib
ce0e2a7dafb92c0ef9822109f6a54f59 *VS6/vc98/mfc/lib/mfcn42ud.lib
59cf2660a869210957c1a43b0a80c2fe *VS6/vc98/mfc/lib/mfco42d.lib
77f4a0a1974ed5049d847af01ade3302 *VS6/vc98/mfc/lib/mfco42ud.lib
f369292b1f687ae0e3a8c31379acf713 *VS6/vc98/mfc/lib/mfcs42.lib
d5f11da7d83fd31b18540dccb819dba3 *VS6/vc98/mfc/lib/mfcs42d.lib
fa61c83bb0eceace2df667ff3ccf212a *VS6/vc98/mfc/lib/mfcs42u.lib
2d15e5d2212a964c6a3a3fca13f4f0bf *VS6/vc98/mfc/lib/mfcs42ud.lib
01b1725dc1a28b944b6beb8023975e5a *VS6/vc98/mfc/lib/nafxcw.lib
c005978222c697e650fd670c78c0c501 *VS6/vc98/mfc/lib/nafxcwd.lib
e2bed60308ebe9394f6b700f02454aae *VS6/vc98/mfc/lib/nafxis.lib
0c4d7f0fb00fe86b3cca5f2df6b4bf1e *VS6/vc98/mfc/lib/nafxisd.lib
b4a775c9c3bf7988532e69a7017c37a6 *VS6/vc98/mfc/lib/uafxcw.lib
5fbf663fabe9b8080044936fcd654602 *VS6/vc98/mfc/lib/uafxcwd.lib
```


## .pat

```
COFF parser. Copyright (c) 1997-2020 Hex-Rays SA. Version 1.23
```

```
$ find VS6/ -type f -exec ../../pcf.exe {} {}.pat \;
.\VS6\vc98\lib\atl.lib: skipped 48, total 48
.\VS6\vc98\lib\atldload.lib: skipped 0, total 9
.\VS6\vc98\lib\comsupp.lib: skipped 1, total 21
.\VS6\vc98\lib\libc.lib: skipped 50, total 1203
.\VS6\vc98\lib\libcd.lib: skipped 40, total 1281
.\VS6\vc98\lib\libcimt.lib: skipped 12, total 315
.\VS6\vc98\lib\libcimtd.lib: skipped 0, total 571
.\VS6\vc98\lib\libcmt.lib: skipped 50, total 1271
.\VS6\vc98\lib\libcmtd.lib: skipped 40, total 1351
.\VS6\vc98\lib\libcp.lib: skipped 70, total 1122
.\VS6\vc98\lib\libcpd.lib: skipped 0, total 1829
.\VS6\vc98\lib\libcpmt.lib: skipped 66, total 1168
.\VS6\vc98\lib\libcpmtd.lib: skipped 0, total 1820
.\VS6\vc98\lib\mfcdload.lib: skipped 0, total 16
.\VS6\vc98\lib\msvcprt.lib: skipped 2104, total 2106
.\VS6\vc98\lib\msvcprtd.lib: skipped 2104, total 2107
.\VS6\vc98\lib\msvcrt.lib: skipped 854, total 944
.\VS6\vc98\lib\msvcrtd.lib: skipped 883, total 977
.\VS6\vc98\lib\oleaut32.lib: skipped 0, total 354
.\VS6\vc98\lib\uuid.Lib: skipped 0, total 0
.\VS6\vc98\mfc\lib\eafxis.lib: skipped 7, total 94
.\VS6\vc98\mfc\lib\eafxisd.lib: skipped 0, total 11
.\VS6\vc98\mfc\lib\mfc42.lib: skipped 6385, total 6385
.\VS6\vc98\mfc\lib\mfc42d.lib: skipped 4850, total 4850
.\VS6\vc98\mfc\lib\mfc42u.lib: skipped 6376, total 6376
.\VS6\vc98\mfc\lib\mfc42ud.lib: skipped 4856, total 4856
.\VS6\vc98\mfc\lib\mfcd42d.lib: skipped 705, total 705
.\VS6\vc98\mfc\lib\mfcd42ud.lib: skipped 705, total 705
.\VS6\vc98\mfc\lib\mfcn42d.lib: skipped 110, total 110
.\VS6\vc98\mfc\lib\mfcn42ud.lib: skipped 111, total 111
.\VS6\vc98\mfc\lib\mfco42d.lib: skipped 2914, total 2914
.\VS6\vc98\mfc\lib\mfco42ud.lib: skipped 2910, total 2910
.\VS6\vc98\mfc\lib\mfcs42.lib: skipped 2, total 27
.\VS6\vc98\mfc\lib\mfcs42d.lib: skipped 0, total 26
.\VS6\vc98\mfc\lib\mfcs42u.lib: skipped 2, total 27
.\VS6\vc98\mfc\lib\mfcs42ud.lib: skipped 0, total 26
.\VS6\vc98\mfc\lib\nafxcw.lib: skipped 481, total 8548
.\VS6\vc98\mfc\lib\nafxcwd.lib: skipped 0, total 2057
.\VS6\vc98\mfc\lib\nafxis.lib: skipped 7, total 92
.\VS6\vc98\mfc\lib\nafxisd.lib: skipped 0, total 11
.\VS6\vc98\mfc\lib\uafxcw.lib: skipped 481, total 8547
.\VS6\vc98\mfc\lib\uafxcwd.lib: skipped 0, total 2006
```

```
$ find VS6 -name '*.pat' -print0 | tar -czvf VS6/VS6.tar.gz --null -T -
VS6/vc98/lib/atl.lib.pat
VS6/vc98/lib/atldload.lib.pat
VS6/vc98/lib/comsupp.lib.pat
VS6/vc98/lib/libc.lib.pat
VS6/vc98/lib/libcd.lib.pat
VS6/vc98/lib/libcimt.lib.pat
VS6/vc98/lib/libcimtd.lib.pat
VS6/vc98/lib/libcmt.lib.pat
VS6/vc98/lib/libcmtd.lib.pat
VS6/vc98/lib/libcp.lib.pat
VS6/vc98/lib/libcpd.lib.pat
VS6/vc98/lib/libcpmt.lib.pat
VS6/vc98/lib/libcpmtd.lib.pat
VS6/vc98/lib/mfcdload.lib.pat
VS6/vc98/lib/msvcprt.lib.pat
VS6/vc98/lib/msvcprtd.lib.pat
VS6/vc98/lib/msvcrt.lib.pat
VS6/vc98/lib/msvcrtd.lib.pat
VS6/vc98/lib/oleaut32.lib.pat
VS6/vc98/lib/uuid.Lib.pat
VS6/vc98/mfc/lib/eafxis.lib.pat
VS6/vc98/mfc/lib/eafxisd.lib.pat
VS6/vc98/mfc/lib/mfc42.lib.pat
VS6/vc98/mfc/lib/mfc42d.lib.pat
VS6/vc98/mfc/lib/mfc42u.lib.pat
VS6/vc98/mfc/lib/mfc42ud.lib.pat
VS6/vc98/mfc/lib/mfcd42d.lib.pat
VS6/vc98/mfc/lib/mfcd42ud.lib.pat
VS6/vc98/mfc/lib/mfcn42d.lib.pat
VS6/vc98/mfc/lib/mfcn42ud.lib.pat
VS6/vc98/mfc/lib/mfco42d.lib.pat
VS6/vc98/mfc/lib/mfco42ud.lib.pat
VS6/vc98/mfc/lib/mfcs42.lib.pat
VS6/vc98/mfc/lib/mfcs42d.lib.pat
VS6/vc98/mfc/lib/mfcs42u.lib.pat
VS6/vc98/mfc/lib/mfcs42ud.lib.pat
VS6/vc98/mfc/lib/nafxcw.lib.pat
VS6/vc98/mfc/lib/nafxcwd.lib.pat
VS6/vc98/mfc/lib/nafxis.lib.pat
VS6/vc98/mfc/lib/nafxisd.lib.pat
VS6/vc98/mfc/lib/uafxcw.lib.pat
VS6/vc98/mfc/lib/uafxcwd.lib.pat
```
