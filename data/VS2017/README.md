# VS14.16 / Visual Studio 2017 / v141

## download

Visual Studio 2019 installer and release channel (used to install Visual Studio 2015 tools):
  - https://aka.ms/vs/16/release/vs_buildtools.exe
  - https://aka.ms/vs/16/release/channel

Install [components](https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019):
  - `Microsoft.VisualStudio.Component.VC.v141.x86.x64`: MSVC v141 - VS 2017 C++ x64/x86 build tools (v14.16)
  - `Microsoft.VisualStudio.Component.VC.v141.CLI.Support`: C++/CLI support for v141 build tools (14.16)
  - `Microsoft.VisualStudio.Component.VC.v141.ATL`: C++ ATL for v141 build tools (x86 & x64), version 16.0.28625.61
  - `Microsoft.VisualStudio.Component.VC.v141.MFC`: C++ MFC for v141 build tools (x86 & x64), version 16.0.28625.61
  - `Microsoft.VisualStudio.Component.Windows10SDK.16299`: Windows 10 SDK (10.0.16299.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.4 
  - `Microsoft.VisualStudio.Component.Windows10SDK.17134`: Windows 10 SDK (10.0.17134.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.7 
  - `Microsoft.VisualStudio.Component.Windows10SDK.17763`: Windows 10 SDK (10.0.17763.0), version 16.0.28517.75, usually bundled with Visual Studio 2017 ver.15.8 

(See [Dockerfile](../../Dockerfile))

This results in:
  - `C:\BuildTools\VC\Tools\MSVC\14.16.27023\`: MSVC v141 - VS 2017 C++ x64/x86 build tools (v14.16)
  - `C:\BuildTools\VC\Tools\MSVC\14.16.27023\atlmfc`: C++ MFC for v141 build tools (x86 & x64)
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.16299.0`: Windows 10 SDK (10.0.16299.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.4 
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.17134.0`: Windows 10 SDK (10.0.17134.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.7 
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.17763.0`: Windows 10 SDK (10.0.17763.0), version 16.0.28517.75, usually bundled with Visual Studio 2017 ver.15.8 

We'll ignore the following targets, if present:
  - `arm`
  - `arm64`
  - `store`
  - `onecore`
  - `ucrt_enclave`
  - `uwp`

## .lib/.obj

### compiler: 14.16.27023

```
acb3bedf0030b83b50c48a13e1117e78  14.16.27023/atlmfc/lib/x86/mfcs140.lib
02fa96eea20990f9aeff04c2daddbacc  14.16.27023/atlmfc/lib/x86/uafxcwd.lib
1ee9a66033c9913295f73fc329d9680e  14.16.27023/atlmfc/lib/x86/uafxcw.lib
59a1b4d7464620eb5eeeb98658fefdb6  14.16.27023/atlmfc/lib/x86/nafxcwd.lib
128fdb32831f922cc764318d9922618a  14.16.27023/atlmfc/lib/x86/nafxcw.lib
c83ff4d89533b772cabbd95cc1f7b522  14.16.27023/atlmfc/lib/x86/mfcs140ud.lib
b501f4ef255b37641e32a45d21094ec8  14.16.27023/atlmfc/lib/x86/mfcs140u.lib
5d0b977192bc9db40864b658d6071a12  14.16.27023/atlmfc/lib/x86/MFCM140ud.lib
8a6bc2f5388f5dc476ad1b06e4b9f07c  14.16.27023/atlmfc/lib/x86/MFCM140u.lib
96420723c45994a00ea29b078d25e141  14.16.27023/atlmfc/lib/x86/mfcs140d.lib
564164cf6a88d1fda3b47c71b4a4089d  14.16.27023/atlmfc/lib/x86/MFCM140d.lib
dde4a43e28d16ed8c55d65d960cc46a4  14.16.27023/atlmfc/lib/x86/MFCM140.lib
73d3713c5704338d453baecb8978a6a1  14.16.27023/atlmfc/lib/x86/mfc140ud.lib
5b7e9fdd1696d1b271e84cdd3694f873  14.16.27023/atlmfc/lib/x86/mfc140u.lib
88f045d40c6724b05d783318a3cd1c5c  14.16.27023/atlmfc/lib/x86/mfc140d.lib
f2172505a5f83c09e4b6716ae9a73bce  14.16.27023/atlmfc/lib/x86/mfc140.lib
bcf8818057b1c7c4c826c648df417dbc  14.16.27023/atlmfc/lib/x86/atls.lib
5ff47ef487919707467ad25877ba7b19  14.16.27023/atlmfc/lib/x86/afxnmcdd.lib
474e91e5b62ba6ae47f7d28d37575b35  14.16.27023/atlmfc/lib/x86/afxnmcd.lib
8de757e31de0c74a30182d42f90d04f0  14.16.27023/atlmfc/lib/x64/uafxcwd.lib
cbe649858df61d17436fea07ef15d056  14.16.27023/atlmfc/lib/x64/uafxcw.lib
a2fb5fbc2b0a12c809576db9700fb7c5  14.16.27023/atlmfc/lib/x64/nafxcwd.lib
25292873095fb5eb9c0b9bf22b19dd1d  14.16.27023/atlmfc/lib/x64/nafxcw.lib
7f62e8c3662cf0e5f63ae779deef855e  14.16.27023/atlmfc/lib/x64/mfcs140ud.lib
00f130991bd20b2fd6fd4fe890be8bf9  14.16.27023/atlmfc/lib/x64/mfcs140u.lib
26ec54740b30491f09fc634612a2e5f5  14.16.27023/atlmfc/lib/x64/mfcs140d.lib
a4a19a86974b4354b94a507bfa0ef85d  14.16.27023/atlmfc/lib/x64/mfcs140.lib
d146ecc62588a7044c6ee59a2a956f64  14.16.27023/atlmfc/lib/x64/MFCM140Ud.lib
7b7b064209cb08fb732273f3c96dedb5  14.16.27023/atlmfc/lib/x64/MFCM140U.lib
db5568d589b76ca40188570818d33266  14.16.27023/atlmfc/lib/x64/MFCM140d.lib
66594593807c3019b6987d7c994b5dc7  14.16.27023/atlmfc/lib/x64/MFCM140.lib
3207103168fef993220bfcfa3f35a593  14.16.27023/atlmfc/lib/x64/mfc140ud.lib
42ab162ae1051c3ef169148f16aa1e26  14.16.27023/atlmfc/lib/x64/mfc140u.lib
8de81ae2475c60104aee731f3d1fcedc  14.16.27023/atlmfc/lib/x64/mfc140d.lib
4506bc2ea4f01f06b1764dd1d9e7c41f  14.16.27023/atlmfc/lib/x64/mfc140.lib
0d2d8ff6e7a1056471242007b382c891  14.16.27023/atlmfc/lib/x64/atls.lib
03f3bbe3ce597d17858b0da9f3770574  14.16.27023/atlmfc/lib/x64/afxnmcdd.lib
7f080b3cf850a22d8a04f39a4e87d4d8  14.16.27023/atlmfc/lib/x64/afxnmcd.lib
99f1fc9f3e6a47c43554d8d937a02319  14.16.27023/lib/x64/concrtd.lib
1ec09aa828a03e70898ff2aed5853c3b  14.16.27023/lib/x64/msvcrt.lib
787c58455f03aa7c69f45e19fb4de32c  14.16.27023/lib/x64/msvcrtd.lib
55cf59a14ac0f7e8182dcf7ac1264a27  14.16.27023/lib/x64/newmode.obj
b4587c72a71b8fa205703ab66ca11c39  14.16.27023/lib/x64/noenv.obj
cabe0bb364594ec9cedf46fb34d83a66  14.16.27023/lib/x64/oldnames.lib
775c0b91c8531a412dfbbaba62a17e68  14.16.27023/lib/x64/pnothrownew.obj
a3cb3c3fcc3a3b9f826e353745f83e87  14.16.27023/lib/x64/pthreadlocale.obj
28375859dccc64e843a8d24c596a3238  14.16.27023/lib/x64/ptrustu.lib
8bdfe6272f6aca8595dba964ec568268  14.16.27023/lib/x64/pwsetargv.obj
4ee21533b5a903ef8bef67c37731ec7f  14.16.27023/lib/x86/vcruntimed.lib
d73125e2da5d7f21e683076245a132ae  14.16.27023/lib/x86/wsetargv.obj
8c647448c264f23d90b520afe0cdbe23  14.16.27023/lib/x86/vcruntime.lib
89049e09a9ce87d34a6926e390a5c18d  14.16.27023/lib/x86/vcompd.lib
59bc2d41fc4b002cc17f415b4d7f16a4  14.16.27023/lib/x86/vccorlibd.lib
8a19e27dd3efaed28ca868b09080612b  14.16.27023/lib/x86/vcomp.lib
d180ab95765bbe694d52fa8d9cc70253  14.16.27023/lib/x86/vccorlib.lib
1ba00f0760f0b7655090c0d676d00ae0  14.16.27023/lib/x86/vcampd.lib
9430afbedc809a9d32315bdc8701d183  14.16.27023/lib/x86/vcamp.lib
47cd872210a7a155b05c7ddce7353dba  14.16.27023/lib/x86/threadlocale.obj
1715939e0fabe56ce0b281e56a38f249  14.16.27023/lib/x86/setargv.obj
92705c20723d3e26cfd5204461d10bc5  14.16.27023/lib/x86/pwsetargv.obj
0c5e13ea35d4e4a84ec69f8d16afd400  14.16.27023/lib/x86/ptrustud.lib
fa3e0ee888eaa2624ac56cc859007dab  14.16.27023/lib/x86/ptrustu.lib
273b42303523a0f27dc453510edd3d16  14.16.27023/lib/x86/ptrustmd.lib
fb7837dfe52e6c1d7c33df4f144c4f8e  14.16.27023/lib/x86/ptrustm.lib
2895230962870ee88bfa07adb5ffb038  14.16.27023/lib/x86/pthreadlocale.obj
32a41276ec233d374ee008588a356c4f  14.16.27023/lib/x86/psetargv.obj
e5e0bc6c44a047e5693d0f3bb05e4ab8  14.16.27023/lib/x86/pnothrownew.obj
c25f0d3d79b5b95cc33d98f960e41b31  14.16.27023/lib/x86/pnoenv.obj
90776fc65addc6c86e76f86d31baa80e  14.16.27023/lib/x86/pnoarg.obj
b6aecedf4e1f89f76c1ed34633b64963  14.16.27023/lib/x86/pnewmode.obj
cc387c06ae73c366110b0ac7beb6a6c2  14.16.27023/lib/x86/pinvalidcontinue.obj
b3e80a3a0a6be7d5860bc47b831da4ea  14.16.27023/lib/x86/pgort.lib
031c2416dfb00bd776ab96c9a972be0e  14.16.27023/lib/x86/pgobootrun.lib
6039decc4ef165ff5fa8a17297b2254e  14.16.27023/lib/x86/pcommode.obj
d7118c522cbc1c16cf481effbf3a48db  14.16.27023/lib/x86/pbinmode.obj
8ef4bdd5e7ee2efd094d0d100ef6f997  14.16.27023/lib/x86/oldnames.lib
1973fcdb57c1dd902f993cc3d3d7c747  14.16.27023/lib/x86/nothrownew.obj
448f88cd8d66f53982fc3b7bec654a2b  14.16.27023/lib/x86/notelemetry.obj
6ba1b0fd7840d584f620ee4e523118ef  14.16.27023/lib/x86/noenv.obj
763bba3086598849e121a34da1088347  14.16.27023/lib/x86/noarg.obj
5d79513260420acb2c879a02275afae0  14.16.27023/lib/x86/newmode.obj
8327f47cb8dc738ab67a8dec0de93281  14.16.27023/lib/x86/msvcurtd.lib
96ac59050dc99b23034107eb9d0529c2  14.16.27023/lib/x86/msvcurt.lib
a517a93fad6306ce214d4ea4cb3c751d  14.16.27023/lib/x86/msvcrtd.lib
fab5e82dd09b102d33962ef5744effd4  14.16.27023/lib/x86/msvcrt.lib
ee2628cc3b1f19d1fa4c3f5f5029932e  14.16.27023/lib/x86/msvcprtd.lib
0aeaa2f186b9b88ae3d03ea17233fd6c  14.16.27023/lib/x86/msvcprt.lib
3283cf5f43c7fcafaf860c446c4d07d8  14.16.27023/lib/x86/msvcmrtd.lib
729615cc86dfd838b96540d708dd45dd  14.16.27023/lib/x86/msvcmrt.lib
383c16bef0e2068b8943786611b84f9e  14.16.27023/lib/x86/loosefpmath.obj
dda7884c0524a6029259e991db209a9e  14.16.27023/lib/x86/libvcruntimed.lib
9189ea4ca9ba9a18386d3279d156f449  14.16.27023/lib/x86/libvcruntime.lib
8a492eca0122aa6a7579e915a508568c  14.16.27023/lib/x86/libcpmtd1.lib
1d793c95431afcb01d794ea260cef1bd  14.16.27023/lib/x86/libcpmtd0.lib
a8dd2fb4dfa99c4c0c356df057351b0c  14.16.27023/lib/x86/libcpmtd.lib
ecfe6f5b48d5ef3dc6362455762e0629  14.16.27023/lib/x86/libcpmt1.lib
bd925e5b3f0408b842ca35915f7e1573  14.16.27023/lib/x86/libcpmt.lib
bb1586625013b58d9f492cf77a22e3ef  14.16.27023/lib/x86/libconcrtd1.lib
8f698ea33dfd79061c6c041ed623a959  14.16.27023/lib/x86/libconcrtd0.lib
65f6f22389cd4f7c1c1a309d361af592  14.16.27023/lib/x86/libconcrtd.lib
15afebf62ff5084099a3b6231550caf2  14.16.27023/lib/x86/libconcrt1.lib
67d406f7696482c2c55ad5da89059000  14.16.27023/lib/x86/libconcrt.lib
ccd6bfc4c9f5d112416d5a7747c9efa1  14.16.27023/lib/x86/libcmtd.lib
df36ce7b754e00f6589002e1fac11265  14.16.27023/lib/x86/libcmt.lib
e333004ee85ae430ef049e592c18a1cc  14.16.27023/lib/x86/legacy_stdio_wide_specifiers.lib
e90a32adfcee272a3e370931e53dfd31  14.16.27023/lib/x86/legacy_stdio_definitions.lib
9328ede9924bdf8657d4c0ab66c9dd0c  14.16.27023/lib/x86/iso_stdio_wide_specifiers.lib
eb0e0b65c33912623cfe54c6d7b4e75c  14.16.27023/lib/x86/invalidcontinue.obj
65fe42b9facbdabeeba3b8394bb42c9c  14.16.27023/lib/x86/fp10.obj
c58d72d3fff6fae5350178dccfef95bd  14.16.27023/lib/x86/exe_initialize_mta.lib
efa55a23298d17157d26858a66ce169e  14.16.27023/lib/x86/delayimp.lib
12961961cf71bb51d205faa9325e62a8  14.16.27023/lib/x86/concrtd.lib
2429038c966d3906d3c3cf5f2c8b7085  14.16.27023/lib/x86/concrt.lib
81f56ba913d79b3c943cee90b972945d  14.16.27023/lib/x86/comsuppwd.lib
c9f8377873eee6b70e6ba8926f3ebf53  14.16.27023/lib/x86/comsuppw.lib
8b3f2ad27edf4fab74f5af33f1072e4f  14.16.27023/lib/x86/comsuppd.lib
adb60bd6e98f1f6c02b4bcb4a819deb8  14.16.27023/lib/x86/comsupp.lib
bbc25a1cbe52b8c1aa35a75ea0038589  14.16.27023/lib/x86/commode.obj
722f9c5f167272e00952e7a373fa64b7  14.16.27023/lib/x86/chkstk.obj
85bef0c2174074cdb824bfd6ed19412a  14.16.27023/lib/x86/binmode.obj
44c25b122f42da6e4cd50a2e90fd57ef  14.16.27023/lib/x86/aligned_new.lib
e01034fb3b12f15ac4847e050c37a26b  14.16.27023/lib/x64/wsetargv.obj
93d15d6f26f7f8cff1d8b8aad0e82fe6  14.16.27023/lib/x64/vcruntimed.lib
8cb1435a8801a75aac1e3379f33ace15  14.16.27023/lib/x64/vcruntime.lib
54560f8b5c9494e4644129bcfe563af1  14.16.27023/lib/x64/vcompd.lib
a76be324cca8ebc3fb2c280b39259adc  14.16.27023/lib/x64/vcomp.lib
f394c37addbde5e28af021f14ed788aa  14.16.27023/lib/x64/vccorlibd.lib
f67bdabeff62a330827f9192832921e4  14.16.27023/lib/x64/vccorlib.lib
a71ceb1a32474d22f49af58e834e09b1  14.16.27023/lib/x64/vcampd.lib
abd4d27879180994fc4a5d0655a428b4  14.16.27023/lib/x64/vcamp.lib
ae160cc765358261661705563e0f0a88  14.16.27023/lib/x64/threadlocale.obj
8221df5c32fdfc9c99d560a744095e1e  14.16.27023/lib/x64/setargv.obj
b818b20847e9aad8227b2ed511093340  14.16.27023/lib/x64/ptrustud.lib
0d7fc7b691bb59fba1aec3111523f07a  14.16.27023/lib/x64/ptrustmd.lib
f0f75688bb1829db418fb5955db95da6  14.16.27023/lib/x64/psetargv.obj
4b5bd407d809ed81624ddfe2a3395363  14.16.27023/lib/x64/pnoenv.obj
00435939c5700ec5dcb098efa2da1381  14.16.27023/lib/x64/pnoarg.obj
e38ae94f63d9001852a13b53ba82dab7  14.16.27023/lib/x64/ptrustm.lib
e2beebadd79c5918119f2c2ec6ccfa8b  14.16.27023/lib/x64/pnewmode.obj
400d5218df9e809351c502266fadc142  14.16.27023/lib/x64/pgort.lib
df96489004f83964c58a5f55712516ef  14.16.27023/lib/x64/pgobootrun.lib
d9cd404c9fcda360871cb9dac7dd3550  14.16.27023/lib/x64/pcommode.obj
a91029106090df77e90dc58bc79be362  14.16.27023/lib/x64/pbinmode.obj
5aa8fcbf14ae8adc8a36384f12af143c  14.16.27023/lib/x64/nothrownew.obj
87fef0cccefa9621ea820a7de8df98d4  14.16.27023/lib/x64/notelemetry.obj
c7106c555370dfb79c482864fd8dd24d  14.16.27023/lib/x64/noarg.obj
359fddc6783d23910857d659e080ec77  14.16.27023/lib/x64/msvcurtd.lib
5edb2aaf2b6a995c8d40ac1dd355cff4  14.16.27023/lib/x64/msvcurt.lib
e8db41de74c43c975ec94856ab877176  14.16.27023/lib/x64/msvcprtd.lib
554ed4b4b92b84235abf3060c04a6b74  14.16.27023/lib/x64/pinvalidcontinue.obj
e50acc4ce5f178c3f1caf3e48506d3d0  14.16.27023/lib/x64/msvcprt.lib
89844e650af3e605b4931627c65b6938  14.16.27023/lib/x64/msvcmrtd.lib
74a6bf0c1ad1e5d4c4fc3a7c6c19b3d3  14.16.27023/lib/x64/msvcmrt.lib
43326b72522824a1ae9e59c8ec7beab3  14.16.27023/lib/x64/loosefpmath.obj
fbb0a6bd155f1f98964fc5e6ba6dfb70  14.16.27023/lib/x64/libvcruntimed.lib
2f5b562de5c5360fc942f146f676cdc3  14.16.27023/lib/x64/libvcruntime.lib
914c7a1f9cd4fb6272c674f6ba603bdf  14.16.27023/lib/x64/libcpmtd1.lib
b6944303106f7fb930cf3dbeebeaf053  14.16.27023/lib/x64/libcpmtd0.lib
a9c76cf79d936d5524618685b616df72  14.16.27023/lib/x64/libcpmtd.lib
4bc543a082b823937210ee859d8ae9c7  14.16.27023/lib/x64/libcpmt1.lib
d87fa4976937d8acbd680116b7065b3a  14.16.27023/lib/x64/libcpmt.lib
a8236c9d296586d4df74301d32bc357b  14.16.27023/lib/x64/libconcrtd1.lib
74dd2fd834c5b8f064e5ee966e5c8876  14.16.27023/lib/x64/libconcrtd0.lib
1a41095d2a70ea47f1d569b1bb55d11b  14.16.27023/lib/x64/libconcrtd.lib
39d2b96a4e57501126d2c36948bf6956  14.16.27023/lib/x64/libconcrt1.lib
a4df8a71e81da4cbd649a11d69280a78  14.16.27023/lib/x64/libconcrt.lib
c87d453dd59b14b8bb51f0c844084d0e  14.16.27023/lib/x64/libcmtd.lib
e44fb4853781c992da82e48d5c29934b  14.16.27023/lib/x64/libcmt.lib
e5c33da4a3e90b4752aeb754a1b1c797  14.16.27023/lib/x64/legacy_stdio_wide_specifiers.lib
ff9f35bba0bd72285d9db49d4e3a4153  14.16.27023/lib/x64/iso_stdio_wide_specifiers.lib
3a262f36dd5c3e0bea0ab2b50f80f227  14.16.27023/lib/x64/legacy_stdio_definitions.lib
7e1a595748c393ae95a4e8b83458a53a  14.16.27023/lib/x64/invalidcontinue.obj
be90cfe3bc12ca6dcde509a311ddcdd3  14.16.27023/lib/x64/exe_initialize_mta.lib
339817c33ea40857fd8a9117e807ace7  14.16.27023/lib/x64/delayimp.lib
e3b946218b6da8d8c01612ccbe21349b  14.16.27023/lib/x64/concrt.lib
46c1d7b6d6d59c3d4cee16b17db3a1c2  14.16.27023/lib/x64/comsuppwd.lib
aba2674a5f233e29a952c3dbf30abdd6  14.16.27023/lib/x64/comsuppw.lib
bb6ea4a71390d3e76872ad513eea480f  14.16.27023/lib/x64/comsuppd.lib
5e3edd861267dd5cad174d3727b539ea  14.16.27023/lib/x64/comsupp.lib
59537757d6e602c843a76b79ebe83ce4  14.16.27023/lib/x64/commode.obj
fe32293d6d8e68c77defb472990dec72  14.16.27023/lib/x64/chkstk.obj
abca28b8ef9b04c4acc7ea346a8b9495  14.16.27023/lib/x64/binmode.obj
bf8297bf71481e75f916c5ad6468b7af  14.16.27023/lib/x64/aligned_new.lib
```

### ucrt: 10.0.16299.0

```
c61b6ad00e33acc99d21775c6b37b6a8  10.0.16299.0/ucrt/x86/ucrtd.lib
51171c76b1c50e38049067d0d7d27d36  10.0.16299.0/ucrt/x86/ucrt.lib
a3c6f3d10e845f1764078d241d07d952  10.0.16299.0/ucrt/x86/libucrtd.lib
81eea8cdb6bc9977755d3bf0e2dbb79b  10.0.16299.0/ucrt/x86/libucrt.lib
6838985c39ef63e814f0186b7eebd616  10.0.16299.0/um/x86/AclUI.Lib
3dc3adf700b86484bae496250a5782ac  10.0.16299.0/um/x86/ActiveDS.Lib
3a43d0033d7bbd648bcd1ea553954d56  10.0.16299.0/um/x86/ADSIid.Lib
58aaf33675e5c2f4557aa61029326445  10.0.16299.0/um/x86/advpack.Lib
3727e3013dae8f977e1be440f8c2b75a  10.0.16299.0/um/x86/ahadmin.lib
a2c89140ad4e628b9dc4b362f2a82ec7  10.0.16299.0/um/x86/amsi.lib
37cf6aa6ed8748e563c007f28bcbe731  10.0.16299.0/um/x86/AdvAPI32.Lib
13ae4ae80d9d35989e65cf22cb7f3885  10.0.16299.0/um/x86/amstrmid.lib
5e5fb9ef93f4483f88eb37f75d31b828  10.0.16299.0/um/x86/api-ms-win-net-isolation-l1-1-0.lib
28518c07023a0905b7466280ca74f95d  10.0.16299.0/um/x86/appnotify.lib
cc986a5d2fcb641a481ef8102abb4b54  10.0.16299.0/um/x86/ASycFilt.Lib
0dfb7a875e57f2d201b18468e056adf7  10.0.16299.0/um/x86/appmgr.lib
d17ec005f7e8654b60d9fb56bee0f1b3  10.0.16299.0/um/x86/audiobaseprocessingobject.lib
2d38e56563956a37cf33b07dd10c9ef3  10.0.16299.0/um/x86/appmgmts.lib
6c14f4a3ca8550cda11765d3d4b2590b  10.0.16299.0/um/x86/apidll.lib
c35cbb49284138ecb45bff77672a40f0  10.0.16299.0/um/x86/AudioBaseProcessingObjectV140.lib
6d3b89952cf51cb021182bceffaf2f86  10.0.16299.0/um/x86/audioeng.lib
43daa5fee21922dcd656dff24e80134a  10.0.16299.0/um/x86/AuthZ.Lib
e057f62ed5b05def5134485ad141f108  10.0.16299.0/um/x86/avifil32.Lib
408ee1b51943c445899aae639b039afe  10.0.16299.0/um/x86/avrt.lib
f93efac731eeb7d665d50783f197a4eb  10.0.16299.0/um/x86/basesrv.lib
96d0105f5ac3574cd88364eaa9390d5b  10.0.16299.0/um/x86/bcrypt.lib
650486d5dc2d0dc1a5a753ab4c14c0ba  10.0.16299.0/um/x86/Bits.Lib
85078ae8a550816e27dfc346221869e2  10.0.16299.0/um/x86/BufferOverflow.lib
e9980083485f9bf8cba652112c722706  10.0.16299.0/um/x86/aux_ulib.lib
d88caf8c122294c9f92bb56360a2ad2e  10.0.16299.0/um/x86/BufferOverflowU.lib
dc274745fc2e502e9c8b7a354d9be4e6  10.0.16299.0/um/x86/Cabinet.Lib
374a80c793366c129a38f4dbdd8f2cc5  10.0.16299.0/um/x86/certadm.lib
391d42b30887d3acf75e9d121e957d3b  10.0.16299.0/um/x86/certca.lib
402a8d72127ea9702a13362fc4573f6d  10.0.16299.0/um/x86/certcli.lib
ecd314e7d4c096214824989e3461816e  10.0.16299.0/um/x86/bthprops.lib
7f4e67e7a8802a5b5cf4268f701b7684  10.0.16299.0/um/x86/CertIdl.Lib
cb962ece314ac4dc6919641914370597  10.0.16299.0/um/x86/CertPolEng.Lib
9b8a3fef8166a4c6d02a68ef16f5d4a0  10.0.16299.0/um/x86/cfgmgr32.lib
54657cc871949c03825595768dced8df  10.0.16299.0/um/x86/Chakrart.lib
630918cdee2c3ca6d54a9de2007976cb  10.0.16299.0/um/x86/cldapi.lib
9a5dd1ff6ae50f8ea7a3786024e788dd  10.0.16299.0/um/x86/clfsmgmt.lib
db9cbf0995541be9172ca538c0ad814a  10.0.16299.0/um/x86/ClusApi.Lib
c887f7557bb294b8729c1a0989a8a682  10.0.16299.0/um/x86/ComCtl32.Lib
04be09c9853ef310ddff97cccd8fba54  10.0.16299.0/um/x86/ComDlg32.Lib
a6c8880b4cc5666d201d692e10d0314a  10.0.16299.0/um/x86/clfsw32.lib
d893364c4c8b9948bda64e5ab030547d  10.0.16299.0/um/x86/CompPkgSup.lib
954723ed1581a9a07983b1612400f36e  10.0.16299.0/um/x86/compstui.lib
7be68a216f4705f6fdabdcb4f01deb3e  10.0.16299.0/um/x86/BluetoothApis.lib
49844b94cfd82e362d96ef577a326e57  10.0.16299.0/um/x86/CoreMessaging.lib
2b619ed9ef22bd735760da7032ceebac  10.0.16299.0/um/x86/ComSvcs.Lib
938978e28e710b0684582fc6774cf33c  10.0.16299.0/um/x86/corrEngine.lib
3b5523cf742cde855ec4cf0382d5c502  10.0.16299.0/um/x86/audiomediatypecrt.lib
b23161017b3e7451e79b26f13b44cb03  10.0.16299.0/um/x86/Credui.lib
5fbd9d614a74135f3e2420643155ade6  10.0.16299.0/um/x86/Crypt32.Lib
03d6ad52d7a984ad2408e8ce4979773e  10.0.16299.0/um/x86/cryptdll.lib
f07c6d5f39af941dfe2b55e5759d8a2c  10.0.16299.0/um/x86/CryptNet.Lib
9ccaf6625f634a133775b2056df72931  10.0.16299.0/um/x86/cryptui.lib
de078a4ea692b90e8cdb0995d4bb475c  10.0.16299.0/um/x86/cryptxml.lib
c495b7ae8da1ecadbab6c7116f6a0f9d  10.0.16299.0/um/x86/cscapi.lib
ff27e43a34eb5a2be03411cf2998e587  10.0.16299.0/um/x86/cscdll.lib
7c870cb7015d71e526cdb538a043af98  10.0.16299.0/um/x86/d2d1.lib
ee3af3ca343a5b396254c10d17c99f59  10.0.16299.0/um/x86/d3d10.lib
34543b95aa55bcb3d89b6ed2961b2438  10.0.16299.0/um/x86/d3d10_1.lib
a6e732c3c3fce4a0ba57505e06b01ba0  10.0.16299.0/um/x86/d3d11.lib
69ede790c07193a163d67fe49bbb5a2d  10.0.16299.0/um/x86/d3d12.lib
28f6695f06569dcfbc33c7e0736181ba  10.0.16299.0/um/x86/d3d9.lib
b026c6aa49d52c4c19b124c121e61d5a  10.0.16299.0/um/x86/d3dcompiler.lib
65dd7158941d6fd68cbf2f633d140dad  10.0.16299.0/um/x86/d3dcsx.lib
5bd856591b402c58465bf46f59e8807a  10.0.16299.0/um/x86/d3dcsxd.lib
a7dc9716dad68829d674cd02da40b5dd  10.0.16299.0/um/x86/davclnt.lib
65ac8547791a4852882278d3e4ef433a  10.0.16299.0/um/x86/DbgEng.Lib
20cbe9d1f55f64b02aa53e3f9385b833  10.0.16299.0/um/x86/DbgHelp.Lib
2d9b6ffe3aff134b9f626a523c51ae17  10.0.16299.0/um/x86/dciman32.lib
f7191bcdccb196b8ec927625536a72d4  10.0.16299.0/um/x86/dcomp.lib
77cb4808926e5ad65b711674cac5b303  10.0.16299.0/um/x86/ddraw.lib
9cc0149ee37217588917c6ba839ea8db  10.0.16299.0/um/x86/devenum.lib
d37bde7902e0b0ec4115d77550c5fcf9  10.0.16299.0/um/x86/deviceaccess.lib
5d28e29788ef57f4e52c62e1b9b59318  10.0.16299.0/um/x86/dflayout.lib
5c63ec79c640059809a51b34453cc544  10.0.16299.0/um/x86/DhcpCSvc.Lib
58f98b73ce91589f61cdcb663eddd3a6  10.0.16299.0/um/x86/devmgr.lib
cf06292c6a19e118b115a99168738f98  10.0.16299.0/um/x86/DhcpCSvc6.Lib
8715b8cf1b4a08ac5bbb3f33f81ad9d6  10.0.16299.0/um/x86/dhcpsapi.lib
a582ea6f657c372e7c94dc81a61e5150  10.0.16299.0/um/x86/difxapi.lib
745c32c4e7bd232a3573510b4c678fa8  10.0.16299.0/um/x86/dinput8.lib
d9a3f2586160f512f39982f78d54f5cd  10.0.16299.0/um/x86/dloadhelper.lib
98271cf17a37a9fafb94fa9fe28cec03  10.0.16299.0/um/x86/dmoguids.lib
a1bdb220541a9408e45968bce5964ac0  10.0.16299.0/um/x86/dmprocessxmlfiltered.lib
1372db11330004a07ba5422fc0a2274c  10.0.16299.0/um/x86/dnscrcli.lib
f9ecca1aa44ca5743b3dcd17e57eda09  10.0.16299.0/um/x86/dnslib.lib
e4e838679acec66b17423f78dd65f765  10.0.16299.0/um/x86/dnsperf.lib
ed5c8aafb0534b1aa70f20fd2670b60a  10.0.16299.0/um/x86/DnsAPI.Lib
5f308c76eabb37431adc872a5a9cc6e5  10.0.16299.0/um/x86/dnsrpc.lib
f3f76401dd06f06f816958e660472933  10.0.16299.0/um/x86/dnsrslvr.lib
1ecddc1c25b0598c3b5bce926fdb1119  10.0.16299.0/um/x86/dpx.lib
71025f0bea7eeb88c066b1d4db9cc049  10.0.16299.0/um/x86/drt.lib
5d2d4d86c0d164232ccfce3cb06c9869  10.0.16299.0/um/x86/drtprov.lib
da096044af2964c9ba0c93fe602d2728  10.0.16299.0/um/x86/drttransport.lib
5dad909121d044f1072b7abe645b3483  10.0.16299.0/um/x86/dsound.lib
2b66310cff4a68203fd32cb70e9fd9dc  10.0.16299.0/um/x86/DSProp.Lib
8ba9c6852c28e161b6bb27010785fa0f  10.0.16299.0/um/x86/dssec.lib
38ab13ab20d6f30c8a890aabdf55406b  10.0.16299.0/um/x86/dststlog.lib
7bd94ea947bab441fb4e17f08f7a90f7  10.0.16299.0/um/x86/DSUIExt.Lib
dbe08be41a74faf1540d237995a0cdc1  10.0.16299.0/um/x86/dwmapi.lib
91a75521c9519c6bba3686869e94f7c6  10.0.16299.0/um/x86/DtcHelp.Lib
37804ae738d63ab261e0abcbcd66347c  10.0.16299.0/um/x86/dwrite.lib
91bef6cc63326c9ea1690127db9a8755  10.0.16299.0/um/x86/dxguid.lib
c01d7c3fc0a35235ce9b0c03fc972751  10.0.16299.0/um/x86/dxgi.lib
f3b06171b3f6a45b85b66c1aebfc8fa0  10.0.16299.0/um/x86/dxtmsft.lib
f694a6ae16955c7d4d40551c3fa4d01a  10.0.16299.0/um/x86/dxtrans.lib
bbc1de5e830d6499248a70f931d29b8d  10.0.16299.0/um/x86/dxva2.lib
c0c522fbd2cae4b132875021790daa01  10.0.16299.0/um/x86/eappcfg.lib
2d3b901e79afeba8ce823bbd00f2373f  10.0.16299.0/um/x86/eappprxy.lib
8a65a5e2114c27f846a6f118a974f69b  10.0.16299.0/um/x86/easregprov.lib
68d06f4aa002893b94871a91cfb2df44  10.0.16299.0/um/x86/efswrt.lib
fb13b8f8153ea0374868c137d8d555ed  10.0.16299.0/um/x86/elfapi.lib
a60a1e74924dd183a2b9a81d127b5e54  10.0.16299.0/um/x86/ehstorguids.lib
1e666c826fb5a25c79844c732febd538  10.0.16299.0/um/x86/els.lib
12b56c25f5e57d09a8c2acfbc905c2d1  10.0.16299.0/um/x86/ElsCore.lib
3bf76948f90b1b3e5515ae82d0fb5634  10.0.16299.0/um/x86/esent.lib
933c3e80612e02fd83559015f5f4b726  10.0.16299.0/um/x86/evr.lib
80e20d48dc815332ab4488efc7dd78fa  10.0.16299.0/um/x86/FaultRep.Lib
fca39a29592c44a78c72111b62b9fde2  10.0.16299.0/um/x86/feclient.lib
4e28e2559caf601c8ddd561113ff47e2  10.0.16299.0/um/x86/FhSvcCtl.lib
b64af8c0a7e3f748a0b08cd16e5cc246  10.0.16299.0/um/x86/fileextd.lib
f05b8cc3aba298385cc877cc6f9dfcc5  10.0.16299.0/um/x86/fltLib.lib
4032925ceca4de47538f9d80948cfb94  10.0.16299.0/um/x86/fontsub.lib
63475c78279bfb5c4404e7c3ad185515  10.0.16299.0/um/x86/FrameDyd.Lib
6c733bacf38569e65ffd8b8602eb0dce  10.0.16299.0/um/x86/fwpuclnt.lib
7f15a0c7e00690c9565ce0984aba27ca  10.0.16299.0/um/x86/fxsutility.lib
6e3ac90548a1ce672d4fc1009e332775  10.0.16299.0/um/x86/FrameDyn.Lib
51af78175e4b3288097b9e373040d5a4  10.0.16299.0/um/x86/Gdi32.Lib
0a43cb583953d24500741857f3ae4d27  10.0.16299.0/um/x86/gdiplus.lib
bbc902c47c13e6ace782a62d5a8d5ed3  10.0.16299.0/um/x86/GlU32.Lib
23d3de020251f1250a5edcf0dd091b81  10.0.16299.0/um/x86/GPEdit.lib
a107a7630c19c2c1ed764a7a8df1f52e  10.0.16299.0/um/x86/gpmuuid.lib
7dd3b8d9df29d425914db07004f68c9d  10.0.16299.0/um/x86/hbaapi.lib
2537fa8f1686477044909104f3a505a0  10.0.16299.0/um/x86/hhsetup.lib
8cb5f1afab12eef2901c9435d11b8d18  10.0.16299.0/um/x86/hid.lib
eb52f8afd61279a17aaaa325aece5b55  10.0.16299.0/um/x86/glmf32.lib
8814af5caf416636518f13dd3db733ee  10.0.16299.0/um/x86/HLink.Lib
1cd11642cd335cc55188c0bebc7abb36  10.0.16299.0/um/x86/hrtfapo.lib
8c10d67acf1eda65c67dcbb88d4bd971  10.0.16299.0/um/x86/Htmlhelp.Lib
059960b724162a66fd7d04ef2f7d4f00  10.0.16299.0/um/x86/httpapi.lib
c8d40de0e8033b2c913561a79136a468  10.0.16299.0/um/x86/iashlpr.lib
f25382830e7e0c7cd5f557d6cd796e38  10.0.16299.0/um/x86/Icm32.Lib
8170d2ea4037cd7809220e174ee157ad  10.0.16299.0/um/x86/Icmui.Lib
8f5f3f54312a422e311e84fa0ab37576  10.0.16299.0/um/x86/icuin.Lib
29435d9ab3c82ad377c6140408c2fb64  10.0.16299.0/um/x86/icuuc.lib
06523fd3fbb72b2c8c39154d4dd5fecf  10.0.16299.0/um/x86/IEPMAPI.Lib
4ce5515eb3cca6f8f13049181513df4c  10.0.16299.0/um/x86/iesetup.lib
f2392615e12f6ea6dcb3abf2a519cf81  10.0.16299.0/um/x86/ImageHlp.Lib
fd490827bbd577301c1536b1d1e46b4e  10.0.16299.0/um/x86/imgutil.Lib
e2411611d1825c4e0ccdf34d5f7ccf23  10.0.16299.0/um/x86/Imm32.Lib
d66360b034534bca06fc4159472ae2fa  10.0.16299.0/um/x86/infocardapi.Lib
752d5c678d82e62d9155b38025c1582b  10.0.16299.0/um/x86/inkobjcore.lib
8a2e852e8d49a936647b882060d595ec  10.0.16299.0/um/x86/inseng.lib
be734ccd8dbfcf931accaa6df7784eab  10.0.16299.0/um/x86/int64.lib
2698862d56b5c93f12cbc21562db94fe  10.0.16299.0/um/x86/iphlpapi.lib
8ad9e68473fcde10617b5e7feb495c53  10.0.16299.0/um/x86/Iprop.Lib
86e07fa2d07f9c987291dd584681a44d  10.0.16299.0/um/x86/irprops.lib
d49612aa79085abfc37e05be1c411929  10.0.16299.0/um/x86/iscsidsc.lib
fd00b65c990cf441b13ea4f7fe7450db  10.0.16299.0/um/x86/jetoledb.lib
7e380b94088af47c54da103081dcfa93  10.0.16299.0/um/x86/jsrt.lib
1c747c570c1983150299baa7d7244f32  10.0.16299.0/um/x86/kerbcli.lib
b52a8f79125bffab2a3d788657ea8486  10.0.16299.0/um/x86/kernel32.Lib
f29b577c80f71d97e1ba597699cefc61  10.0.16299.0/um/x86/kernel32legacylib.lib
1240a055df1edf6f44a2844eeed204f7  10.0.16299.0/um/x86/KSProxy.Lib
d18dc51d3d6d21e5482ccc51fe91bbac  10.0.16299.0/um/x86/ksuser.lib
ebe016abd4d05d95b57f4a6de0952c49  10.0.16299.0/um/x86/ktmw32.lib
8c2b397295309edefc7e60bae57053af  10.0.16299.0/um/x86/LoadPerf.Lib
2667667e3d847f2acaf899a3cc09b97b  10.0.16299.0/um/x86/locationapi.lib
40b11d933065b71581caaf65a954fd86  10.0.16299.0/um/x86/Lz32.Lib
5fab5efdb3e74edea33d918d902286fd  10.0.16299.0/um/x86/magnification.lib
c5cce321c7a6b9dafc1394779e7cf17f  10.0.16299.0/um/x86/MAPI32.Lib
60d9e8d8329e36343061e5ea0a386963  10.0.16299.0/um/x86/mbnapi_uuid.lib
8b40f31ee4c891c3ae64a08e2976aee4  10.0.16299.0/um/x86/mciole32.lib
53b221e725ee419da10ae015113afe65  10.0.16299.0/um/x86/mdmlocalmanagement.lib
804fc364b790ccfdee6d1199c48fa655  10.0.16299.0/um/x86/MDMRegistration.lib
d5361fe793dbf9c5a45dde63b50107bc  10.0.16299.0/um/x86/Mf.lib
d477633b1d8d785257ea47fba4f240b3  10.0.16299.0/um/x86/Mfcore.lib
5040791b920430839fbdd4a94a1074be  10.0.16299.0/um/x86/mfreadwrite.lib
85b3bf68d16f7735cb944ad8b252e4fe  10.0.16299.0/um/x86/mfplay.lib
627adc7941b89e984bc5645f8207bfdc  10.0.16299.0/um/x86/Mfplat.lib
2fd880f1e8ae99bac07aa43b6c781922  10.0.16299.0/um/x86/mfsensorgroup.lib
d637963bd623791ce65827186b430d9c  10.0.16299.0/um/x86/Mfsrcsnk.lib
7492c0710605493abf630ab1d333d857  10.0.16299.0/um/x86/mfuuid.lib
51b5125ef1c80bb11176ccc6c1fc4e0e  10.0.16299.0/um/x86/MgmtAPI.Lib
18cc82c3678376ebc471f8ad8b40faae  10.0.16299.0/um/x86/mi.lib
119ba0e3acbce9fe86cb6c36c6354fa0  10.0.16299.0/um/x86/mincore_downlevel.lib
fa7e33c8b7cb0c5d5144121d7fee204b  10.0.16299.0/um/x86/mmdevapi.lib
1aa1fa6e19fe540967e7770e117d7b0f  10.0.16299.0/um/x86/Mprapi.Lib
cc6b896312846e73238b4f7ec067d1ab  10.0.16299.0/um/x86/Mpr.Lib
d67d7d5c374d77b1262bfbb2fcf41adb  10.0.16299.0/um/x86/MqOA.Lib
f36685bbe177b70a6c368dbe2c0b9ff3  10.0.16299.0/um/x86/mprsnap.lib
90744efa111f7053b18646e626eaeb8f  10.0.16299.0/um/x86/MqRt.Lib
169e2d5228f2ddcff8b50e53ff4c93ee  10.0.16299.0/um/x86/MMC.Lib
e191a0de112a57eac6a695e69eaae5da  10.0.16299.0/um/x86/msaatext.lib
6d22ef6bb0337ccd81a816fddb57fe7f  10.0.16299.0/um/x86/MrmSupport.lib
25cc3a69f8c2acc5d557bc0db7301856  10.0.16299.0/um/x86/mincore.lib
3e9083822309ae506fc3b2822eadfb77  10.0.16299.0/um/x86/MSAcm32.Lib
265debeceae0192af531386a6574ac50  10.0.16299.0/um/x86/MSAJApi.lib
aec4846be798f6a446de4d9e8980e858  10.0.16299.0/um/x86/Mscms.Lib
778a8ab9f767ea494d1ae6cdcb2bf63e  10.0.16299.0/um/x86/MsCtfMonitor.lib
26cc38b2bbca508cd4f4ebf2b226ff82  10.0.16299.0/um/x86/msdasc.lib
2f22d61ae2a34f1148b0a9841255e5f9  10.0.16299.0/um/x86/msdelta.lib
3fa5e01a16718629330ca2974429a410  10.0.16299.0/um/x86/msdmo.lib
f82e47d0db18f2e22da3560d9d330e0e  10.0.16299.0/um/x86/msdrm.lib
66c2925d816f08bc82da0e880f352ce5  10.0.16299.0/um/x86/Msi.Lib
791e0bed40dcc14d236e2e8841ae2d48  10.0.16299.0/um/x86/MSImg32.Lib
9d9a461cff590d97eb52f1a7f4f77f54  10.0.16299.0/um/x86/mspatcha.lib
9f3b41712fd3321fdff88be370cae763  10.0.16299.0/um/x86/mspatchc.lib
09b79acf8d202b305594cdec507ce320  10.0.16299.0/um/x86/mspbase.lib
258d3c10e5e6be04e8ba5ca0014e4e22  10.0.16299.0/um/x86/msports.lib
2769091765d15fbc00bbdd949e597422  10.0.16299.0/um/x86/MSRating.Lib
784f6ccd565e51357a3c72d94fff9b38  10.0.16299.0/um/x86/msv1_0.lib
03208f0b4ef3b64be946ae47f2dea1d8  10.0.16299.0/um/x86/MSTask.Lib
735ec777e89f6472c3bb43ae9ebad84e  10.0.16299.0/um/x86/msvfw32.Lib
cb2ecf792ba5b0d2baf0f7869296bc47  10.0.16299.0/um/x86/MsWSock.Lib
187359bea8e2ac8b59cfd18f2d5f3c17  10.0.16299.0/um/x86/MsXml2.Lib
645294e13e89af6c4b85b15ec2c92bce  10.0.16299.0/um/x86/msxml6.lib
3ffd4a0e409d3b7acca35404ffd6e27a  10.0.16299.0/um/x86/Mtx.Lib
ab4909aae6da67905a617ff060710834  10.0.16299.0/um/x86/mtxdm.lib
9e293c8746307a7cc464fd97edf71357  10.0.16299.0/um/x86/muiload.lib
573255327fc064e968a119920f16f334  10.0.16299.0/um/x86/ncrypt.lib
f554891d3aa1c2df3f8a7f5d508e401b  10.0.16299.0/um/x86/nddeapi.lib
6702144a9869d6d04286a9bf7483cce4  10.0.16299.0/um/x86/ndfapi.lib
7916f3a75fa02935927013912f9d2b9c  10.0.16299.0/um/x86/ndproxystub.lib
4b93ef2cb2efb7cae72458be3da81228  10.0.16299.0/um/x86/NetAPI32.Lib
500ec2667291c0556d98203a3f2b0d69  10.0.16299.0/um/x86/netlib.lib
0e3c25385bf392b5c29f1e9f93dc2d85  10.0.16299.0/um/x86/NetSh.Lib
ee410d2a3f7c69f9c4ccfe043086692e  10.0.16299.0/um/x86/newdev.lib
a89f13814d186f18a693b77e0ef2beef  10.0.16299.0/um/x86/ninput.lib
5216aebb39ed670cf2064c773cae4f80  10.0.16299.0/um/x86/normaliz.lib
fdb9158a3c6db983a96354fe41694dca  10.0.16299.0/um/x86/ntdll.lib
52ac8f6c363dc8258618df3a3e2e641f  10.0.16299.0/um/x86/ntdsa.lib
2961866fbcd4393ba1b4de8400f634c5  10.0.16299.0/um/x86/ntdsatq.lib
5289850435d0ce5fc3b423db86ad4233  10.0.16299.0/um/x86/NtDsAPI.Lib
bcc0e30c464d19679e5fbd2ca77516d7  10.0.16299.0/um/x86/ntdsetup.lib
b11758d0617d22881a1fef82060c84eb  10.0.16299.0/um/x86/ntfrsapi.lib
8b40c345ea174f1568fe9da885b9908f  10.0.16299.0/um/x86/nt.lib
1072a4771a7c3049fff4ce00ca53d3d9  10.0.16299.0/um/x86/ntlanman.lib
758797b3bbd72e1056fe085052a2c0a3  10.0.16299.0/um/x86/ntmarta.lib
c89471c0d4e10ec947e785ee39cbf867  10.0.16299.0/um/x86/NtQuery.Lib
fc49f3a5640325914683a0874325fa95  10.0.16299.0/um/x86/ntstc_libcmt.lib
fcad07cffd716ee4f57b0c9948aedb3a  10.0.16299.0/um/x86/ntstc_msvcrt.lib
e65b82c985af3afcc3a9a42c14406b31  10.0.16299.0/um/x86/ntvdm.lib
5cff0ef3ee16cec11099619d5966dad4  10.0.16299.0/um/x86/objsel.lib
251f560f245bd5416dae9f79ea5acd14  10.0.16299.0/um/x86/odbc32.lib
cdf20cd816e75dccaec4862cb77479ab  10.0.16299.0/um/x86/odbcbcp.lib
f5e6f1078c9fb6421e5d180f02a2933b  10.0.16299.0/um/x86/odbccp32.lib
23afc0091fc3e344732d439210b975e1  10.0.16299.0/um/x86/OemLicense.lib
c7df5fe514fbfa5686d8a9422fcbf115  10.0.16299.0/um/x86/Ole32.Lib
50b7e169681d10e245c2d6d508dc624a  10.0.16299.0/um/x86/OleAcc.Lib
02425e98846ec3f07c63eb02773384b6  10.0.16299.0/um/x86/OleAut32.Lib
9230476aa34fd74c625b3e288a9f51ff  10.0.16299.0/um/x86/olecli32.lib
41faa8da0b0477c71fc728ecb76c41bf  10.0.16299.0/um/x86/oledb.lib
3b140dcb05d677a307f4b60e7a10b78a  10.0.16299.0/um/x86/OleDlg.Lib
284fe477af22692ce57ed7cbdbf4e6be  10.0.16299.0/um/x86/OlePro32.Lib
78cf9eaa26eb8d82ffed3800cefeef65  10.0.16299.0/um/x86/olesvr32.lib
dfece4386a15a76e83f7caf506be76fb  10.0.16299.0/um/x86/ondemandconnroutehelper.lib
b2fea557668011f4f2cd3d4460cce053  10.0.16299.0/um/x86/OneCore.Lib
a2965afa8e413434a2b0763db826addb  10.0.16299.0/um/x86/OneCoreUAP.Lib
054ccc83b0ecfdfafa299b3a07586ad0  10.0.16299.0/um/x86/OneCoreUAP_downlevel.Lib
054ccc83b0ecfdfafa299b3a07586ad0  10.0.16299.0/um/x86/OneCore_downlevel.Lib
d6932944975b666fa892c084b3a0d6fb  10.0.16299.0/um/x86/OpenGL32.Lib
12446b748f93635a65e29122b34e2b94  10.0.16299.0/um/x86/osptk.lib
3fe88338c6904524c295bab95ad89ab3  10.0.16299.0/um/x86/p2p.lib
2f185ca0d51463d07ec133f8f1223138  10.0.16299.0/um/x86/p2pgraph.lib
6c7530914f5d566fce8f1cd2db2adc62  10.0.16299.0/ucrt/x64/ucrtd.lib
b7cd4e115e865ad89e5884982c7c1826  10.0.16299.0/ucrt/x64/ucrt.lib
31af0200b675d1b772b3fc2fab0eb6c3  10.0.16299.0/ucrt/x64/libucrtd.lib
50ebd7018baa052f25fca4f13d1d93f0  10.0.16299.0/ucrt/x64/libucrt.lib
0bc058247be8cc42b1348e52da9ddf4a  10.0.16299.0/um/x86/patchwiz.lib
a82c03ff1578e129ca0af7df524274e9  10.0.16299.0/um/x86/pathcch.lib
02769470d624add60d05ac287ae9856b  10.0.16299.0/um/x86/Pdh.Lib
52c82eebc2b79faccdcc2ef856a6199d  10.0.16299.0/um/x86/PhotoAcquireUID.lib
31865503618e982fbda56b93cd5420b8  10.0.16299.0/um/x86/PortableDeviceGuids.lib
f397f973faef1875710968be12e9c6d2  10.0.16299.0/um/x86/powrprof.lib
7c361732aea0badf5d7c1e3e5bafd5b4  10.0.16299.0/um/x86/prntvpt.lib
7f2a6853e3ffe60c1453de0f71cc1f0d  10.0.16299.0/um/x86/propsys.lib
31fe454103ecdd21ef4540dbb2057afd  10.0.16299.0/um/x86/Psapi.Lib
ac40d11785604a294f51af516a6c6d47  10.0.16299.0/um/x86/quartz.lib
c89471c0d4e10ec947e785ee39cbf867  10.0.16299.0/um/x86/query.lib
24ed1f6e3986037dc924fabe5f5a3630  10.0.16299.0/um/x86/RASAPI32.Lib
2ed52e2d9f48852a25c825fb00fc1032  10.0.16299.0/um/x86/RASDlg.Lib
13154df134cf9166792b59eb6cee6899  10.0.16299.0/um/x86/rasuser.lib
8aa629f354339d03aadc5a827cff9afa  10.0.16299.0/um/x86/resutils.lib
040bdee12ab2d6e297d63e61f15a2193  10.0.16299.0/um/x86/rometadata.lib
be556f1d588c65ba6dcd35f0ee8905ea  10.0.16299.0/um/x86/rpcexts.lib
2ea69f469f9e5975d2acb98de85c4618  10.0.16299.0/um/x86/rpcproxy.lib
25edc711ebeaa62c43ebcc7009179011  10.0.16299.0/um/x86/RpcRT4.Lib
204f0f19e6b9bf3218c9f14e14a0a005  10.0.16299.0/um/x86/rpcutil.lib
44e196cc716a3359d7537502d9e5d2dc  10.0.16299.0/um/x86/rstrtmgr.lib
b5ce3eb669355434e85bb261c9069522  10.0.16299.0/um/x86/Rtm.Lib
17db3703dd268789fa8fff09ed77f947  10.0.16299.0/um/x86/rtutils.lib
1746405136f4dff9c466fae111fb18a6  10.0.16299.0/um/x86/schannel.lib
df116e1325d68c2c6fb88f54a9c49b60  10.0.16299.0/um/x86/ScrnSave.Lib
d151b7f049ec1f12190ff567f9b297a5  10.0.16299.0/um/x86/SearchSDK.lib
525d61ecf358498e3fcf86213e0406c1  10.0.16299.0/um/x86/ShFolder.Lib
5468cd25cb9306bda1f03faf10128ad0  10.0.16299.0/um/x86/ShLwApi.Lib
96f8664ef4e9b6c37a0de7fcb42b870a  10.0.16299.0/um/x86/slc.lib
c0a01b74425154c04499d916ddbcf910  10.0.16299.0/um/x86/slcext.lib
a9c94f4d206b7b4b05ca5ce96643b717  10.0.16299.0/um/x86/slwga.lib
9caad1052bd19800c07fc203c4e9745a  10.0.16299.0/um/x86/SnmpAPI.Lib
61d09e3eca2f7d4a6cc0e01057a692aa  10.0.16299.0/um/x86/spoolss.lib
32a6f73e73ecd560246a982c8d8bbe9d  10.0.16299.0/um/x86/SpOrder.Lib
975809863a122cba40909b3773795a8f  10.0.16299.0/um/x86/srpapi.lib
e3d63c1ce68ce24f1ce957ee5beb5b79  10.0.16299.0/um/x86/ssdpapi.lib
2fcf12bb3986936d20bdba4a3ecf0932  10.0.16299.0/um/x86/Sti.Lib
70efc0c0552d8d67a359b9dade374f14  10.0.16299.0/um/x86/strmbase.lib
3fdd13b7d97a8d650fba4ae84d2d06df  10.0.16299.0/um/x86/strmiids.lib
511148a1cbb75d7c914ad0d6e962b1ca  10.0.16299.0/um/x86/strsafe.lib
c7aef8d7896a4a2eef71022150ac37d0  10.0.16299.0/um/x86/Svcguid.Lib
3ea2dcb11d83c0864481f9884de116c5  10.0.16299.0/um/x86/swdevice.lib
7c302cd09570e4e45d101ffed2af5466  10.0.16299.0/um/x86/synchronization.lib
3e5297dfd39e3f59ec92ed15c29e156f  10.0.16299.0/um/x86/Tapi32.Lib
54ca121d4837c0970fc035d8b05589c9  10.0.16299.0/um/x86/tapi32l.lib
9671753563a61782c4eb0aebabbf625e  10.0.16299.0/um/x86/taskschd.lib
286f8ba201a52c9b204914a49a4b6a04  10.0.16299.0/um/x86/tbs.lib
4b40f09d2f88499a36b845332a2da635  10.0.16299.0/um/x86/Thunk32.Lib
67c1655d677df21abfbbf9f461345373  10.0.16299.0/um/x86/tsec.lib
c33dd521becccce3b1597729b3a23826  10.0.16299.0/um/x86/tspubplugincom.lib
00b6c7f7b285c1450ad0049790e2c83c  10.0.16299.0/um/x86/twain_32.lib
60b9550ac1009b4937fadbf605afe4ba  10.0.16299.0/um/x86/TranscodeImageUID.lib
2e9e0ece3130525637e772c8b8ea4832  10.0.16299.0/um/x86/Traffic.Lib
84a81f0c52dd43926be11618750fc49c  10.0.16299.0/um/x86/UIAutomationCore.lib
9f2742a13092c273674e0e0646a224f5  10.0.16299.0/um/x86/umpdddi.lib
09fb30d92d0070e1d1b69772ff896c54  10.0.16299.0/um/x86/unicows.lib
3c900be0a4f8a3f4452636a3e39d01e0  10.0.16299.0/um/x86/Urlmon.Lib
76c9fb7c8f2a1525c2cc602452e7634f  10.0.16299.0/um/x86/User32.Lib
2e32e09dce664345a25f918bff92f259  10.0.16299.0/um/x86/UserEnv.Lib
bcdf2560d6a6d130dbb7dd00e1eef347  10.0.16299.0/um/x86/USP10.Lib
71bc7bb071428ef1fad49bdaa61b8dbd  10.0.16299.0/um/x86/Uuid.Lib
b4f5a4434bdc81cbf6b26637cd1ea310  10.0.16299.0/um/x86/Uxtheme.lib
099d7646481d141302cceacf5deabb48  10.0.16299.0/um/x86/vccomsup.lib
e1a0bce5d2ae62e63ad130beb8062471  10.0.16299.0/um/x86/Vfw32.Lib
b99dae9d4f01ed23d2505b8efaf99377  10.0.16299.0/um/x86/Virtdisk.Lib
bd13913e05a2cc2914553266cb1b36c7  10.0.16299.0/um/x86/vscmgr.lib
705e14a5f9d14b07397d56dc5994f3af  10.0.16299.0/um/x86/vssapi.lib
60340be78d74a53dc00b58f32e6f936c  10.0.16299.0/um/x86/vss_uuid.lib
403562f827ebdf6506255980db9efba1  10.0.16299.0/um/x86/vstorinterface.lib
10c49bcfb6e45beb38b572168b89928a  10.0.16299.0/um/x86/wcmapi.lib
fd6d801974395bd8759281c9ffc13e86  10.0.16299.0/um/x86/wcmguid.lib
188d3f77c892ffe19d487e9286d97f03  10.0.16299.0/um/x86/wdsbp.lib
23e59189264c33bd88d89b13f390fd2b  10.0.16299.0/um/x86/wdsClientAPI.LIB
53c43122538ff676ae27246b2e70346a  10.0.16299.0/um/x86/wdspxe.lib
74c3fb8629dad401326aebbbc60134e7  10.0.16299.0/um/x86/wdstptc.lib
76a0a5a99c34249ab780255e1e6a1033  10.0.16299.0/um/x86/WebServices.lib
215757c5e53ace58d9b494bce138daf9  10.0.16299.0/um/x86/websocket.lib
2923759cd41fa32dfaf7cfe649521363  10.0.16299.0/um/x86/wecapi.lib
c598a5319ab1fe4852e7b3c8123c177e  10.0.16299.0/um/x86/Wer.lib
31c878a4690dc6c336ede4f87cd9bccc  10.0.16299.0/um/x86/wevtapi.lib
a795248df010000065841d943a34eb69  10.0.16299.0/um/x86/wiaservc.lib
6cdd86fb7553f65e555f246ad751033b  10.0.16299.0/um/x86/wiautil.lib
7ba0b626eb7ca4db6a680cd71a805bdc  10.0.16299.0/um/x86/WinBio.lib
9b3f692dfaf568015b75697a82742f1e  10.0.16299.0/um/x86/windows.data.pdf.lib
1cd74e7328a556d0f6e763d4631c0556  10.0.16299.0/um/x86/windows.networking.lib
fb333825d507c8905c8a2dc463e1fcf3  10.0.16299.0/um/x86/WindowsApp.lib
c19c73550de70f43a7b20a905fd799a3  10.0.16299.0/um/x86/WindowsApp_downlevel.lib
e4126419d3c08a8d20243fe2519a5bbf  10.0.16299.0/um/x86/windowssideshowguids.lib
757857a03d1ed5e2dc300ff7aa478342  10.0.16299.0/um/x86/winfax.lib
2d98fa1e56494d6a4be1d20f7496a432  10.0.16299.0/um/x86/WinInet.Lib
317c50d6ff4aa471500947376d13e485  10.0.16299.0/um/x86/WinMM.Lib
f2a278016aac945e368cba6bc29bfe7b  10.0.16299.0/um/x86/winsatapi.lib
87d0b7d9c1ea613f03020c1ea796e8c8  10.0.16299.0/um/x86/winscard.lib
a8ef98ea1bf95cc27d1a4744848c9437  10.0.16299.0/um/x86/winsqlite3.lib
f2148d0d32dda0af0cdb1f5931182d18  10.0.16299.0/um/x86/WinSpool.Lib
d9a240cb2b9cabe53bdf6425126db23e  10.0.16299.0/um/x86/WinStrm.Lib
5ab4a3ed15d89098c2742612c87bfc50  10.0.16299.0/um/x86/WinTrust.Lib
5ce57931baeb40c7391cada0411dcf67  10.0.16299.0/um/x86/winusb.lib
5f1f65009ef88e9b1839fc760281b4d9  10.0.16299.0/um/x86/wlanapi.lib
d38154a9e70d4ae8f01f7b12975cccc5  10.0.16299.0/um/x86/wlanui.lib
113827c037e31735e64c1eb8b55f256f  10.0.16299.0/um/x86/Wldap32.Lib
827d8c0d4fbdfe4e7649a79e5c7d2c79  10.0.16299.0/um/x86/wmip.lib
0ef463670b32803b2af22bf81c4c0b08  10.0.16299.0/um/x86/wmiutils.lib
dbe184530f8deda8a2dc741df02dc425  10.0.16299.0/um/x86/wmvcore.lib
4cb9f72996d35984cea57d93da0ee590  10.0.16299.0/um/x86/wofutil.lib
015ddee0b165c58c082de490a95b437f  10.0.16299.0/um/x86/workspaceax.lib
bd06f19f2ac2fa7f94d564fff4b0aab4  10.0.16299.0/um/x86/Wow32.Lib
0964496a5111bfa3ea61bd29d80ef585  10.0.16299.0/um/x86/xapobase2_8.lib
49f09c122078a7914bab77e4e943e182  10.0.16299.0/um/x86/xaudio2.lib
ac9613820bd7ab6aea0c691f5f7c2adf  10.0.16299.0/um/x86/xaswitch.lib
ae63a688df4bfa4901fae5d301ef96d2  10.0.16299.0/um/x86/xapobase.lib
7707aac54ea0c82aaec3fab6efb17120  10.0.16299.0/um/x86/wuguid.lib
3dd3ded8c992ac4b5aee9391b0e954f5  10.0.16299.0/um/x86/WtsApi32.Lib
85f872ce38c88b00e1f17c9a4c392475  10.0.16299.0/um/x86/WSock32.Lib
ff0170022cc6a893cfbb52113b1192d9  10.0.16299.0/um/x86/WSnmp32.Lib
7888bb227ed7abaef543c62869f37ee4  10.0.16299.0/um/x86/wsmsvc.lib
a53bce1b984d9b0cd438ad5d097ba94e  10.0.16299.0/um/x86/wsdapi.lib
2a183086c55c8a9f0fc5a57cd1ea7e37  10.0.16299.0/um/x86/wsclient.lib
251d196ef35f1b543d901c6d1f7c544c  10.0.16299.0/um/x86/wscapi.lib
7650343cc6f03de96a29012f435d39a6  10.0.16299.0/um/x86/wsbonline.lib
d803553169728e1b63bd2f8a8c693e0d  10.0.16299.0/um/x86/wsbapp_uuid.Lib
cb5249b9faf66e12231fba06ba571c8c  10.0.16299.0/um/x86/WS2_32.Lib
cf0bab1501439e3b1f7b22a0ee142f6d  10.0.16299.0/um/x86/wmcodecdspuuid.lib
3e648de8171911c3d72a92464b483a45  10.0.16299.0/um/x86/winsta.lib
60163bc9214fd92bbe512ad1c2c74d36  10.0.16299.0/um/x86/winhttp.lib
dbf8ac3f887768ddb046b40a575de391  10.0.16299.0/um/x86/windowscodecs.lib
a79ae7122dc98c0858ebc9d5d479392d  10.0.16299.0/um/x86/windows.ui.lib
84c67e5288acfc7e62ea46f0ae5c5d8f  10.0.16299.0/um/x86/WiaGuid.Lib
c041e2847b96cdcbfa8cad9c0d08f405  10.0.16299.0/um/x86/wdsmc.lib
b20828d171d98bf19cb7dd1dc740a3a6  10.0.16299.0/um/x86/wbemuuid.lib
d84d234069837aa661f042a32afe4dd9  10.0.16299.0/um/x86/Version.Lib
f9f5fe9c14ace13b23523c05a494dedf  10.0.16299.0/um/x86/vds_uuid.lib
1e6f6093d3355b59b1b0e1815c10971a  10.0.16299.0/um/x86/VdmDbg.Lib
8ad81c285c4194088a2d4d66725a64c1  10.0.16299.0/um/x86/ualapi.lib
01adcf30689c32ffeafaa1a351487cc4  10.0.16299.0/um/x86/txfw32.lib
416ecda474dc5b5baee43721ee7ec090  10.0.16299.0/um/x86/twinapi.lib
c10e593306a10ce11b2bf0dc795de4ad  10.0.16299.0/um/x86/tokenbinding.lib
5ca174dfc6b6e31c6863fd871bcf3fc2  10.0.16299.0/um/x86/tdh.lib
8772f13b794b5be38810e1327f564963  10.0.16299.0/um/x86/t2embed.lib
35fa50025601e656e493a2566919c496  10.0.16299.0/um/x86/structuredquery.lib
7a8c98d7dddf90adb587de885fcf31b4  10.0.16299.0/um/x86/SrClient.lib
95255cc23723c903cba4f1bc6373c8cb  10.0.16299.0/um/x86/shell32.lib
46ad1bff05ca70805ca5ef8e22014790  10.0.16299.0/um/x86/shdocvw.lib
8acf41ac1feac1c0ec786c11ca1f736f  10.0.16299.0/um/x86/shcore.lib
44f53e1972a998474bbbc2e5ed567bd7  10.0.16299.0/um/x86/Sfc.Lib
737d1770c96ddc72c234fc2e3c77335d  10.0.16299.0/um/x86/SetupAPI.Lib
01e4200d1db9b6528cfc868f06b74f92  10.0.16299.0/um/x86/SensorsUtils.lib
6e12adc0163015607a9ce01d91b564a9  10.0.16299.0/um/x86/sensorsapi.lib
cbdbc448a6b48600772551293b52eeec  10.0.16299.0/um/x86/SensAPI.Lib
61dc1d43e372a67e784737ed44870bef  10.0.16299.0/um/x86/sens.lib
d0f9d049c6387458c8e990bc0e0e013f  10.0.16299.0/um/x86/security.lib
c1a0c68a69ef5f9602a6146176e08ef1  10.0.16299.0/um/x86/Secur32.Lib
0ed7c7c9fdf7771a135618ff614e154d  10.0.16299.0/um/x86/ScrnSavW.Lib
54c9f83cb424d9363c0faa9aae8f3c2f  10.0.16299.0/um/x86/scesrv.lib
43150c301d1284a6a8d6917a11bb8490  10.0.16299.0/um/x86/scecli.lib
e18d942ff53bf8b49de1e8c6e145f3c6  10.0.16299.0/um/x86/SCardDlg.Lib
bde6010c1d857376770e3729aa738fa4  10.0.16299.0/um/x86/sbtsv.lib
55ad0201f4beab3b0a2b88da5a127a6a  10.0.16299.0/um/x86/sas.lib
1988eea33cc8d3e678c2690d2cc0ec9d  10.0.16299.0/um/x86/SAPI.Lib
29a37cb8622db324c70cf5a0d3ea7568  10.0.16299.0/um/x86/samsrv.lib
71bfb3362e4865e8e19d27d2116fadc3  10.0.16299.0/um/x86/samlib.lib
f376658aaa4559833f5a5ac7840153f4  10.0.16299.0/um/x86/runtimeobject.lib
47babc25fb8c585eae56c507f881d095  10.0.16299.0/um/x86/RTWorkQ.lib
bc4aeaa1ec453425fad37e983b8d55fe  10.0.16299.0/um/x86/Rpcns4.Lib
0ec36f75b510a91fc2760e2e7911781e  10.0.16299.0/um/x86/qwave.lib
2dd20ccd100576de3d35075e13c55f28  10.0.16299.0/um/x86/PeerDist.lib
8b18486dd7b8e175866fe8612fb21ecc  10.0.16299.0/um/x86/xpsprint.lib
cb2303279a15b45e2c5bdc960da706d2  10.0.16299.0/um/x86/xpsdocumenttargetprint.lib
bc972cea04d26db88c7f59b2ed58c873  10.0.16299.0/um/x86/xolehlp.lib
fa04ef0bcf0b6533c44f125b2980b1f0  10.0.16299.0/um/x86/xmllite.lib
471aba8f6b54f0dba4b63903a05f5f87  10.0.16299.0/um/x86/xinputuap.lib
6328d7d0f5079c3781f333417b59a997  10.0.16299.0/um/x86/Xinput9_1_0.lib
8e28a0276510e0f3dcdde577e936fdf4  10.0.16299.0/um/x86/xinput.lib
459398b37912ce52fff2e1edacbeb925  10.0.16299.0/um/x86/xaudio2_8.lib
13d2d3f7c48b146db1510dcadc4c63ef  10.0.16299.0/um/x64/Uxtheme.lib
cb8a12e0a7fb76c95d296ca8b351ddcd  10.0.16299.0/um/x64/wdsmc.lib
214777bd86071760630c1010436f5cb9  10.0.16299.0/um/x64/wdstptc.lib
0b048a5a23e75717e3136986f41ef284  10.0.16299.0/um/x64/windows.data.pdf.lib
153e78c2e004779c0990088b7a5adebb  10.0.16299.0/um/x64/winfax.lib
a11db85509c04dac8c222a571e23ea24  10.0.16299.0/um/x64/wmip.lib
50e89140e46dc203b618c59199d4ad41  10.0.16299.0/um/x64/wmiutils.lib
d09ebcc6d3a16dd0bbac8ab839d6ba98  10.0.16299.0/um/x64/wmvcore.lib
5a06819aaa98896c7972d52ee8ba1157  10.0.16299.0/um/x64/wsdapi.lib
2866a2896bef6841c91c14e177bac75d  10.0.16299.0/um/x64/wuguid.lib
ef6142a1af3a3dc19534466d1202b364  10.0.16299.0/um/x64/xpsprint.lib
766668b3c236da691dbadcf350a73af8  10.0.16299.0/um/x64/xpsdocumenttargetprint.lib
b52400b45b710a5108383019524d8a22  10.0.16299.0/um/x64/xolehlp.lib
ebbcbcd4a82db88c5a665363ea6c80a7  10.0.16299.0/um/x64/xmllite.lib
7e4fe9f8a432dd5129f35a89f4df4d65  10.0.16299.0/um/x64/xinputuap.lib
14198a246d969dac73c0b959011fd2c4  10.0.16299.0/um/x64/Xinput9_1_0.lib
55fd6113b3a8b9f18ab61e7e76c54315  10.0.16299.0/um/x64/xinput.lib
d9a8da35d9f4dfc1692ba666157d114b  10.0.16299.0/um/x64/xaudio2_8.lib
0235b004470cdefbe3116bd014416339  10.0.16299.0/um/x64/xaudio2.lib
c177412f0c87d0ea7c2a47956916a04d  10.0.16299.0/um/x64/xaswitch.lib
c0c5d7fc7d71b09cafc5af7d75cbe3f0  10.0.16299.0/um/x64/xapobase2_8.lib
ed65761c685394e7130a0c4787587d8d  10.0.16299.0/um/x64/xapobase.lib
1494b56758eb89db2edb0647cb077b95  10.0.16299.0/um/x64/WtsApi32.Lib
d4575569780011360fef97fedf5d05a7  10.0.16299.0/um/x64/WSock32.Lib
3385747d078e06f2a302a8e00556a3c8  10.0.16299.0/um/x64/WSnmp32.Lib
20ad7bfd2c0ccdda5219ed0eba03cf13  10.0.16299.0/um/x64/wsmsvc.lib
e5070bba1716d9f916588aad535486bb  10.0.16299.0/um/x64/wsclient.lib
1a2666324d5c759e54553ebb0371fb57  10.0.16299.0/um/x64/wscapi.lib
db4de54681dce3b51399c57364927ff0  10.0.16299.0/um/x64/wsbonline.lib
691a82a12c6e957a8b7370dae8a6cfe5  10.0.16299.0/um/x64/wsbapp_uuid.Lib
c675d980ef799ddfb85bd8b00b23149b  10.0.16299.0/um/x64/WS2_32.Lib
793c5dd19758c550273f9437e7ca3b93  10.0.16299.0/um/x64/workspaceax.lib
dc83a99ca1bb420fcae9837560e0fad2  10.0.16299.0/um/x64/wofutil.lib
369e12d04cbfe419a69349514f60ddee  10.0.16299.0/um/x64/wnvapi.lib
2c5f4b1329cd9c780b2fda61304de402  10.0.16299.0/um/x64/wmcodecdspuuid.lib
782b701404ced64a55eedafb7bbbf36f  10.0.16299.0/um/x64/Wldap32.Lib
9d7e74d4f6a90ff89b6b1485c495009a  10.0.16299.0/um/x64/wlanui.lib
f2738bcb61c217f6b110b832c22e70ff  10.0.16299.0/um/x64/wlanapi.lib
478de4228cbee0d49a804fd171b433f9  10.0.16299.0/um/x64/winusb.lib
86900c10c71924d5c19093230122d897  10.0.16299.0/um/x64/WinTrust.Lib
a8d9b2363e5ccd67eb382cd101b61e73  10.0.16299.0/um/x64/WinStrm.Lib
1a49552bee8518fe6a395019f7a21ca5  10.0.16299.0/um/x64/winsta.lib
b2829478c9b7596d2d76694aef855152  10.0.16299.0/um/x64/winsqlite3.lib
db591d619e26e67b383a511b14b3bce6  10.0.16299.0/um/x64/WinSpool.Lib
7ffb60a93aba11777178fb59cf722ba3  10.0.16299.0/um/x64/winscard.lib
4812a6aff658c2588ec6a6931cffa0ad  10.0.16299.0/um/x64/winsatapi.lib
b6aab5d03ee4dd28816430c0cca46708  10.0.16299.0/um/x64/WinMM.Lib
18453d53d9d7a9bd60d3865c44383327  10.0.16299.0/um/x64/WinInet.Lib
1245af700fbf8553610f3c89ca11e2ba  10.0.16299.0/um/x64/winhttp.lib
99bb4a0393bff4170c79aab21fe606ba  10.0.16299.0/um/x64/windowssideshowguids.lib
73d8cfcc9a7f04f2765327877e70c05d  10.0.16299.0/um/x64/windowscodecs.lib
bdb18b71d40e22244a21007195b9f615  10.0.16299.0/um/x64/WindowsApp_downlevel.lib
f47f6f94bf74f7e9d1f85a420604c7e1  10.0.16299.0/um/x64/WindowsApp.lib
ee75fe9a72548f1ad115afbadad9aa47  10.0.16299.0/um/x64/windows.ui.lib
e8063b683c0bcf42888983ee2369d2c4  10.0.16299.0/um/x64/windows.networking.lib
e3deb38d05554815646df189d78f53b6  10.0.16299.0/um/x64/WinBio.lib
2ec6c9461fe510822d92b074d9b51819  10.0.16299.0/um/x64/wiautil.lib
93f1c41e70b82e3dbf8a6bcd01e1d23c  10.0.16299.0/um/x64/wiaservc.lib
987ab316eec4b6504ec205b65545bf42  10.0.16299.0/um/x64/WiaGuid.Lib
88536df3986a59f5b0f22f751bf10b26  10.0.16299.0/um/x64/wevtapi.lib
60d5857b7189cc24f86d18a6f7f0b1b3  10.0.16299.0/um/x64/Wer.lib
67660f2308fa48a658aef2110398babb  10.0.16299.0/um/x64/wecapi.lib
29566c163cee164c4887f21d1e532121  10.0.16299.0/um/x64/websocket.lib
99a1e3d3b1fb5fb3935a8515289fba2a  10.0.16299.0/um/x64/WebServices.lib
3ada4f7259663543d5632e05bcb5e06e  10.0.16299.0/um/x64/wdspxe.lib
46a7ebfbafc7d097880bbeab293f9f0d  10.0.16299.0/um/x64/wdsClientAPI.LIB
c29d101998409b937edbf4b7b0e9ab6c  10.0.16299.0/um/x64/wdsbp.lib
d99ee469ee1ae7e09642e5ba35ce1b49  10.0.16299.0/um/x64/wcmguid.lib
2f2a34533d062cd7c642dd9e75567aab  10.0.16299.0/um/x64/wcmapi.lib
745b04de1dff59772f842f5f253d27c4  10.0.16299.0/um/x64/wbemuuid.lib
68ec23a8718bcb4e6d6e87b11564ddea  10.0.16299.0/um/x64/vstorinterface.lib
033a5ce1ff5f59c3161e4759fe659b00  10.0.16299.0/um/x64/vss_uuid.lib
d000d6c34ff059f45c6f652257322423  10.0.16299.0/um/x64/vssapi.lib
3c69b21aaf022781bd61c58d60e1f8b8  10.0.16299.0/um/x64/vscmgr.lib
7dc9b0eeb452aec22464d30aa1ff094e  10.0.16299.0/um/x64/Virtdisk.Lib
4c5e5753f801f2bb47c4d3d7639463ad  10.0.16299.0/um/x64/Vfw32.Lib
e57f3ebe3ff8a2555aa19ddb490dccc0  10.0.16299.0/um/x64/vertdll.lib
8576f55ed3878e577dd851ca1c55649e  10.0.16299.0/um/x64/Version.Lib
1855359d983d8361d00815c6e7475d95  10.0.16299.0/um/x64/vds_uuid.lib
5418ae02954af0935eca12ba609ce78e  10.0.16299.0/um/x64/vccomsup.lib
e5daa28be2d263d7b1126398dcbcd472  10.0.16299.0/um/x64/Uuid.Lib
b8aff191649d85cf733568b925e07caf  10.0.16299.0/um/x64/USP10.Lib
6c232c3b89478ad2ad4ceba29369b456  10.0.16299.0/um/x64/UserEnv.Lib
6a8f5addfa30d937ed22dd251f4e35e3  10.0.16299.0/um/x64/User32.Lib
19ffdb33c1aa181484bb1557ffc1da91  10.0.16299.0/um/x64/Urlmon.Lib
d44fd1ae6d4b45b43ad45fd0455a0ec1  10.0.16299.0/um/x64/umpdddi.lib
e1d609e5c8740fc0f818eb705fba965a  10.0.16299.0/um/x64/UIAutomationCore.lib
2c7c92de6880a93d6fb1d1d177b6060e  10.0.16299.0/um/x64/ualapi.lib
7099bf38876007c3ae8b2b58023ea1b3  10.0.16299.0/um/x64/txfw32.lib
be9c7b0d756124dcfcfa4f95d0e56046  10.0.16299.0/um/x64/twinapi.lib
b4fd9577f3cd934f1b24173a6964533c  10.0.16299.0/um/x64/tspubplugincom.lib
fd90469b61a1e9648c91d11afc1e6569  10.0.16299.0/um/x64/tsec.lib
74a7419f326c076e4a800e67a8b0cfca  10.0.16299.0/um/x64/TranscodeImageUID.lib
5feca23b70bcfedeb0ebd07dc62f9e38  10.0.16299.0/um/x64/Traffic.Lib
0ff72bb74b405078ac5bcb25d0179ea9  10.0.16299.0/um/x64/tokenbinding.lib
93f2d98c2b2856e0b28732c99fa4e83c  10.0.16299.0/um/x64/tdh.lib
6f2b03f122ebe609bfce9c2975a19b65  10.0.16299.0/um/x64/tbs.lib
af2616b5d095d8c5706c8351c034cbde  10.0.16299.0/um/x64/taskschd.lib
2a1e9bb487d9a1daba885c98bdb651d6  10.0.16299.0/um/x64/tapi32l.lib
299b77c19eda4596fa971794394bd2e2  10.0.16299.0/um/x64/Tapi32.Lib
1e9c61ae3d2acf31b7807a65602982c2  10.0.16299.0/um/x64/t2embed.lib
eb20d70ef5f4cde42bdda9d9d19646ce  10.0.16299.0/um/x64/synchronization.lib
cee8b204939f7120ac7a7d08bff4f639  10.0.16299.0/um/x64/swdevice.lib
21b14ac07fb92ea13e9ea2ecf209566e  10.0.16299.0/um/x64/Svcguid.Lib
9cb0820af59699e14ffa4ffb1342ac62  10.0.16299.0/um/x64/structuredquery.lib
5c89b55993441dccfc3fb58fdd106a8d  10.0.16299.0/um/x64/strsafe.lib
28e571070ed8dbb09b174f3694ca1c9e  10.0.16299.0/um/x64/strmiids.lib
39f2e430a60f20f76bd0fe45eeea9ae3  10.0.16299.0/um/x64/strmbase.lib
a053a1ad69e96fa875b9ffe8049c1663  10.0.16299.0/um/x64/Sti.Lib
cabd4cff4b69262a7ed99659e3a1887c  10.0.16299.0/um/x64/ssdpapi.lib
541f18fe0c5bc035ba4ff56e0550f28f  10.0.16299.0/um/x64/srpapi.lib
eb4f4006798309400c64d6ce1b608a25  10.0.16299.0/um/x64/SrClient.lib
b0c360a8e5840c09e75e6575f05b7cd4  10.0.16299.0/um/x64/SpOrder.Lib
a2bcf4df1146929e5ebf4afa89764b72  10.0.16299.0/um/x64/spoolss.lib
4ac250fa5df87cffb74182e0d53cb4f6  10.0.16299.0/um/x64/SnmpAPI.Lib
179724952a1ab1399aa06c9bce15c78e  10.0.16299.0/um/x64/slwga.lib
99403852756b8764e7ce21289dafa170  10.0.16299.0/um/x64/slcext.lib
6cc3c880014c85e479c05b269709ec25  10.0.16299.0/um/x64/slc.lib
86ba8bc72c56b106d44423d74d21baf9  10.0.16299.0/um/x64/ShLwApi.Lib
46979eaa45d9ebe3317dba1d110dc0e0  10.0.16299.0/um/x64/ShFolder.Lib
ed0057891c3f6509cac9b5a08c49f52e  10.0.16299.0/um/x64/shell32.lib
afb2f99594cbc32d35338930cc90d077  10.0.16299.0/um/x64/shdocvw.lib
0c98bfeda4caf1882606bb1084107ff1  10.0.16299.0/um/x64/shcore.lib
848d67dba1839bbedab1e32e4af77758  10.0.16299.0/um/x64/Sfc.Lib
4c541efa04a51c7326f0df9b0fa7e5fe  10.0.16299.0/um/x64/SetupAPI.Lib
c55d36846f89d02d1fd656326b48bfbb  10.0.16299.0/um/x64/SensorsUtils.lib
bc6014d56af64ddb29472a983a917164  10.0.16299.0/um/x64/sensorsapi.lib
5e55f70e052db9c0ce4b3725de7c3e61  10.0.16299.0/um/x64/SensAPI.Lib
ca0ce2717164636f96b404854a0d5ecd  10.0.16299.0/um/x64/sens.lib
d64566dde2b727015c57afeb8fccd384  10.0.16299.0/um/x64/security.lib
0b579b742251f71e33e5b65e330683cd  10.0.16299.0/um/x64/Secur32.Lib
76a4c0dfbb2e32949290d9ea3a931de0  10.0.16299.0/um/x64/SearchSDK.lib
f173f689095727f4f7062696df68064e  10.0.16299.0/um/x64/ScrnSavW.Lib
203eb833dc3f2ecdd70e94b1aead2eef  10.0.16299.0/um/x64/ScrnSave.Lib
56bc45b14bfd637a79a9e19f3bfb3d2d  10.0.16299.0/um/x64/schannel.lib
3f0bbcf294271d94ff2700cce4adcf3b  10.0.16299.0/um/x64/scesrv.lib
e055569ac8386d8691b8f62df614dc9c  10.0.16299.0/um/x64/scecli.lib
4afbd5c6b1a11c1f0f8c8ff05fa0252b  10.0.16299.0/um/x64/SCardDlg.Lib
60fc5908c7880280cbe01e03463004e8  10.0.16299.0/um/x64/sbtsv.lib
c5022a666eee252e2119ba66f474d48e  10.0.16299.0/um/x64/sas.lib
3f9a948048554135fbbf17eb14cfe22e  10.0.16299.0/um/x64/SAPI.Lib
001e0c846a65fc8742264a56cb351c86  10.0.16299.0/um/x64/samsrv.lib
9f8073871017bb6906d934f0a4b6f896  10.0.16299.0/um/x64/samlib.lib
a78836b05fd2c119b9525339bf4e465e  10.0.16299.0/um/x64/runtimeobject.lib
64a1e976a79c173a372400a8a8c19ad8  10.0.16299.0/um/x64/RTWorkQ.lib
ffeb2b5a28381531a0fc06c4b7d04f86  10.0.16299.0/um/x64/rtutils.lib
0d782d0d2aa18539edfad772678dfbe8  10.0.16299.0/um/x64/Rtm.Lib
ad7e46f51e4e7fd21b4535823faa96a1  10.0.16299.0/um/x64/rstrtmgr.lib
ae72b868aa7b813f3e91d45aa9b3540e  10.0.16299.0/um/x64/rpcutil.lib
cdaff2ca4cb5fc8a1117935cf2c06ae3  10.0.16299.0/um/x64/RpcRT4.Lib
f2ee9ef1b229984c233f536fe88e8ca3  10.0.16299.0/um/x64/rpcproxy.lib
93ce71871ae0aef189249db6690d43cb  10.0.16299.0/um/x64/Rpcns4.Lib
e8a9057b2dc81fda7a43554b30bab082  10.0.16299.0/um/x64/rpcexts.lib
2960b17ab678cafef9d6f3b01d1a9dcb  10.0.16299.0/um/x64/rometadata.lib
8a2716bb891d48113e44226458487e6d  10.0.16299.0/um/x64/resutils.lib
3a8752c13dfd410937fb809a0ed18ae3  10.0.16299.0/um/x64/rasuser.lib
c3290258ab1f7fd6fbaa9366f4371c07  10.0.16299.0/um/x64/RASDlg.Lib
ff02638ed7c4cc8791948fa1ac3284c4  10.0.16299.0/um/x64/RASAPI32.Lib
e6fbd3f27847a5c3c9bd30fdaac45c1e  10.0.16299.0/um/x64/qwave.lib
c26e2f270edb25a4b0da7e2007ca3327  10.0.16299.0/um/x64/query.lib
731965841f71681dd7d7aaa0ee89246f  10.0.16299.0/um/x64/quartz.lib
3e7b22887ac088cd09fd96993f253d11  10.0.16299.0/um/x64/Psapi.Lib
404a30e20e12bd29b6a1051a66f40cda  10.0.16299.0/um/x64/propsys.lib
2205054d3d1b7edc79ec47acec661031  10.0.16299.0/um/x64/prntvpt.lib
f336d913db78e7c7b674633dd19e8ba3  10.0.16299.0/um/x64/powrprof.lib
04d84da2164c7ccb8edb31bf7ba4090d  10.0.16299.0/um/x64/PortableDeviceGuids.lib
544087c43e39af6618d79976dd2334be  10.0.16299.0/um/x64/PhotoAcquireUID.lib
152da476ea5985e05cb0e081db03a234  10.0.16299.0/um/x64/PeerDist.lib
342c2d9d040636e517ff38f27061c358  10.0.16299.0/um/x64/Pdh.Lib
774f231327a1f08b993beb4831158f7d  10.0.16299.0/um/x64/pathcch.lib
6828500319b90d3ac6917eb8f29b3e34  10.0.16299.0/um/x64/p2pgraph.lib
e06f2bb3d707e407b8507d106a833c0e  10.0.16299.0/um/x64/p2p.lib
5eabed3044227f944651e7e60b5e71da  10.0.16299.0/um/x64/osptk.lib
da68291e083a6f820de791439457ec6e  10.0.16299.0/um/x64/opmxbox.Lib
3ca1fbf3378463770850549dcb56807b  10.0.16299.0/um/x64/OpenGL32.Lib
efdaff652c725d7382a3c16592f87bc0  10.0.16299.0/um/x64/OneCore_downlevel.Lib
efdaff652c725d7382a3c16592f87bc0  10.0.16299.0/um/x64/OneCoreUAP_downlevel.Lib
bbdb246d7ee5289e5a589e4b94da76dc  10.0.16299.0/um/x64/OneCoreUAP.Lib
05093ff05153b06c5c07fb7caf7dcf76  10.0.16299.0/um/x64/OneCore.Lib
c2910dab45b37ca4a0744188e2379b27  10.0.16299.0/um/x64/ondemandconnroutehelper.lib
c3bab31692f60a22b41eb38350eecab6  10.0.16299.0/um/x64/olesvr32.lib
f79907262588786b5ee9d86b37df4375  10.0.16299.0/um/x64/OleDlg.Lib
9746705e4b3ae2072ddcf97ea36e9522  10.0.16299.0/um/x64/oledb.lib
ffafdfea9dba62b440a89dacac2c759a  10.0.16299.0/um/x64/olecli32.lib
9e5e9a561f3fb61697e5922a817a1d09  10.0.16299.0/um/x64/OleAut32.Lib
9f2d200ff42466d3b3c6b792658fa9d4  10.0.16299.0/um/x64/OleAcc.Lib
ee5295a04237c682c9b9ef1c655fb3a6  10.0.16299.0/um/x64/Ole32.Lib
9d999dd9283afc70d65e5ecef05fe803  10.0.16299.0/um/x64/OemLicense.lib
133ef96e4a365b235646f857ca5e8826  10.0.16299.0/um/x64/odbccp32.lib
b2587e74ac5c5940551f729821c87731  10.0.16299.0/um/x64/odbcbcp.lib
f62297283a04c5971ac133b271608239  10.0.16299.0/um/x64/odbc32.lib
1c7fa902547fd7fa6f1e332c1bad2922  10.0.16299.0/um/x64/objsel.lib
9b91ed7ca4cc3780e0bf2f4ea3d89914  10.0.16299.0/um/x64/ntstc_msvcrt.lib
3316e656c8af57a611b66493ea53ee6d  10.0.16299.0/um/x64/ntstc_libcmt.lib
c26e2f270edb25a4b0da7e2007ca3327  10.0.16299.0/um/x64/NtQuery.Lib
e56a168807750d60d0b75b1ef0e8d61f  10.0.16299.0/um/x64/ntmarta.lib
89a2b679586b2bc9a7c29032b3268706  10.0.16299.0/um/x64/ntlanman.lib
d34bbcb46fb3833eceb34b4e32d1b7fa  10.0.16299.0/um/x64/ntfrsapi.lib
c022b6ca2ee9db0d34bbf34186c91233  10.0.16299.0/um/x64/ntdsetup.lib
7f408e4693f8a0da530b5f00deaeee03  10.0.16299.0/um/x64/ntdsatq.lib
c07564e1118aaa75019777c519df2dd6  10.0.16299.0/um/x64/NtDsAPI.Lib
c9d8bd1e460886ada0e5501488af7a76  10.0.16299.0/um/x64/ntdsa.lib
adbe864f312bf4580c25662a493c8bab  10.0.16299.0/um/x64/nt.lib
7474c4602d10e271615637e6c8cb6b61  10.0.16299.0/um/x64/ntdll.lib
6408608ca89cd010397357bddc669053  10.0.16299.0/um/x64/normaliz.lib
d01130339a63aa3a03966444893a60aa  10.0.16299.0/um/x64/ninput.lib
5e500db48870fb1a6cc2b9fbd5be6140  10.0.16299.0/um/x64/NetSh.Lib
26307c41e8d4cbf15eca776f717ef746  10.0.16299.0/um/x64/newdev.lib
3bd70008b93404b6aff243714f02d324  10.0.16299.0/um/x64/netlib.lib
06eb9441e359e73193c94ba0caec17bd  10.0.16299.0/um/x64/NetAPI32.Lib
31f02873bb72744997478957ce670036  10.0.16299.0/um/x64/ndproxystub.lib
091b27d87ef0623102b58ba7eed4b99d  10.0.16299.0/um/x64/ndfapi.lib
cc7025c9132192fff0ee0f95ec88316d  10.0.16299.0/um/x64/nddeapi.lib
05878c7e17d2746d036d622efac88b69  10.0.16299.0/um/x64/ncrypt.lib
c5b003b5fd016cb47e9e6ab1ca12f3e5  10.0.16299.0/um/x64/nanosrv.lib
56ceed60c38a0e254f3e543e76d175b0  10.0.16299.0/um/x64/muiload.lib
67b094b7136ed8b2546fd089ce666624  10.0.16299.0/um/x64/mtxdm.lib
29b699b82498fbaf97036b7325906bd6  10.0.16299.0/um/x64/Mtx.Lib
e765008bd4ec94ca92c71ca08fa20009  10.0.16299.0/um/x64/msxml6.lib
6d55f6edbec5b4c491aa841ed1ff1d86  10.0.16299.0/um/x64/MsXml2.Lib
7f79e78aadfc2828f6ddeaf6705144c2  10.0.16299.0/um/x64/MsWSock.Lib
ef411432013b8eba85606875627a8903  10.0.16299.0/um/x64/msvfw32.Lib
7f3baf950cb0ba258ae6d908f9c7c6d7  10.0.16299.0/um/x64/msv1_0.lib
2f1645a9b721f2654ab40a196dcb0262  10.0.16299.0/um/x64/MSTask.Lib
ec6cf6a9c48c8750ef9eb28f4020fe0a  10.0.16299.0/um/x64/MSRating.Lib
9a0541d2de112a5d5a55170b47786b58  10.0.16299.0/um/x64/msports.lib
de285c07257ac396d8f201164cf0ce44  10.0.16299.0/um/x64/mspbase.lib
987b83e4c93767a27b3d81508da9f686  10.0.16299.0/um/x64/mspatchc.lib
a9790a6e09eb970781335b6956fa3818  10.0.16299.0/um/x64/mspatcha.lib
b636e4fd7e9d393a643715537dcf8834  10.0.16299.0/um/x64/MSImg32.Lib
cf4bba62bc0cd4d7cb0852b7e95d1114  10.0.16299.0/um/x64/Msi.Lib
06ddefe703cc517d87a25e677ebbc408  10.0.16299.0/um/x64/msdrm.lib
885afbd213bf79265924ca435daaa20a  10.0.16299.0/um/x64/msdmo.lib
b85f5df6262f300cfe7a8aca228cdd29  10.0.16299.0/um/x64/msdelta.lib
3b2d029dd5f6075c6e84a0c8fba319ab  10.0.16299.0/um/x64/msdasc.lib
f80062b3d7cbd40b609d454f049f2769  10.0.16299.0/um/x64/MsCtfMonitor.lib
f1346c7917a2aa163ee1e1585070e31d  10.0.16299.0/um/x64/Mscms.Lib
a4d0cd1a6c6600f89999ed8f7d6e149c  10.0.16299.0/um/x64/MSAJApi.lib
9101e220d76ffbfb0f93c3e03ae6e4f4  10.0.16299.0/um/x64/MSAcm32.Lib
3390a0e839b59722c1e66dd9b4bd23c0  10.0.16299.0/um/x64/msaatext.lib
726aa4e21f8646de68d35c910767a8b8  10.0.16299.0/um/x64/MrmSupport.lib
f13add503a91e0e626ed1d4946e7d8c2  10.0.16299.0/um/x64/MqRt.Lib
451218bd227fb68da076040a1a7a7dc7  10.0.16299.0/um/x64/MqOA.Lib
02aded30404566e56846b30ac29b3386  10.0.16299.0/um/x64/mprsnap.lib
6b663bc8fc74d9616bc2c1c2cd1b8c5e  10.0.16299.0/um/x64/Mprapi.Lib
b8bf4c0d67286ad95f6d060169014a28  10.0.16299.0/um/x64/Mpr.Lib
66705b03a0514b50d525f33a6da672e0  10.0.16299.0/um/x64/mmdevapi.lib
c2df5bc7cb4786a42ce7c9bee28fc682  10.0.16299.0/um/x64/MMC.Lib
8b32c77cf9b5f8ef7d97a34ffb3b5797  10.0.16299.0/um/x64/mincore_downlevel.lib
cad3eb723eba8f4674045f31859b4372  10.0.16299.0/um/x64/mincore.lib
037a7cfc9fab08cb8fb0e9fa5130bf3e  10.0.16299.0/um/x64/mi.lib
8df7fca7657780335686bbec74e2dd38  10.0.16299.0/um/x64/MgmtAPI.Lib
3d2d8a58e40e81841cbfd3846256ab6a  10.0.16299.0/um/x64/mfuuid.lib
9c6a3b762cec03482fb9ef4bc8a911c5  10.0.16299.0/um/x64/Mfsrcsnk.lib
6fdab848adfbaf7312bd44cde60799a3  10.0.16299.0/um/x64/mfsensorgroup.lib
e4f5b2a6fe604335015381c5bade73dd  10.0.16299.0/um/x64/mfreadwrite.lib
b874f7afa3ff2772cd0a4e0bc0e25f0b  10.0.16299.0/um/x64/mfplay.lib
7eae5d2601f49a1ffe50dd9f6bcd7e09  10.0.16299.0/um/x64/Mfcore.lib
1e5a63788cafd779662b9c2807957a3c  10.0.16299.0/um/x64/Mfplat.lib
146ec536595b31d70c1bec5f2d4ffd9d  10.0.16299.0/um/x64/Mf.lib
3eecde58a34611aff14a4511b8faa917  10.0.16299.0/um/x64/MDMRegistration.lib
8a8b16286ac913c45048cef51715e9b3  10.0.16299.0/um/x64/mdmlocalmanagement.lib
16006c0b1bbe16987e04e27ff91cdec4  10.0.16299.0/um/x64/mciole32.lib
fe80d5e4c5179616cbfc510ce7d3f4bb  10.0.16299.0/um/x64/mbnapi_uuid.lib
9db3496cc1fb4020d235e1d342373ed5  10.0.16299.0/um/x64/MAPI32.Lib
6264bef649f4592637867e5e25bb9d5f  10.0.16299.0/um/x64/magnification.lib
a98d736dc16f722df9c2f0ef16ff4772  10.0.16299.0/um/x64/Lz32.Lib
b71e31bc2e494e12714dc6ce6e04e025  10.0.16299.0/um/x64/locationapi.lib
2460df3063fdf81858fc59abd08a3380  10.0.16299.0/um/x64/LoadPerf.Lib
b7ba6efb92e8d165c6034696cd7493f7  10.0.16299.0/um/x64/ktmw32.lib
8b1f670b0cd6ed7550ae3380f02d2536  10.0.16299.0/um/x64/ksuser.lib
f7aa84d8b0ac73f55642f6e08a2488e5  10.0.16299.0/um/x64/KSProxy.Lib
d411062bcd2e7250a10104214920f368  10.0.16299.0/um/x64/kernel32legacylib.lib
92cfb793b739f6c5e92541e119f3bcdf  10.0.16299.0/um/x64/kernel32.Lib
ade052086973c27735b733ad97f2ea84  10.0.16299.0/um/x64/kerbcli.lib
a831f385a0eae32eb3bfc8be69790f39  10.0.16299.0/um/x64/jsrt.lib
fb04a7ae6cae84d85655f4969de56aa9  10.0.16299.0/um/x64/iscsidsc.lib
41458b9310e41116600f10f1832aaa4c  10.0.16299.0/um/x64/irprops.lib
0a1b1703e15af5112e8d3b46b790e2bb  10.0.16299.0/um/x64/Iprop.Lib
65df3e0b00d5866b3b8db983dc793c76  10.0.16299.0/um/x64/iphlpapi.lib
9fde1bd6933ad15a963d7c613d2f64fd  10.0.16299.0/um/x64/inseng.lib
3a07cee16e3f95c34b4fb84f5cf133d6  10.0.16299.0/um/x64/inkobjcore.lib
c4de4cc8a517beef960bc15461f50e39  10.0.16299.0/um/x64/infocardapi.Lib
1445b222b043fc177058a41490edb454  10.0.16299.0/um/x64/Imm32.Lib
576f632e9b4fccb24da2f1103cd663dd  10.0.16299.0/um/x64/imgutil.Lib
cc8631314e1588fbca65f11edcbaec7a  10.0.16299.0/um/x64/ImageHlp.Lib
de82b633ed7f6ca60c829ffccbccf031  10.0.16299.0/um/x64/iesetup.lib
d5a72fd006a92c6d7746c8d90b8de6bb  10.0.16299.0/um/x64/IEPMAPI.Lib
b23d035444ed887f10ab24994849d209  10.0.16299.0/um/x64/icuuc.lib
1d05450dc50b64e1718f371d1af00113  10.0.16299.0/um/x64/icuin.Lib
ca36bd5b3a3bc5eb7a0ffc52243f58ad  10.0.16299.0/um/x64/Icmui.Lib
2fc4d0af1c25ed7a26554a441a5d9ba5  10.0.16299.0/um/x64/Icm32.Lib
d236dbd6ec4e5b84e3d2750953991510  10.0.16299.0/um/x64/iashlpr.lib
985d26699f2a161b3310fa5189a7ac04  10.0.16299.0/um/x64/httpapi.lib
a2bf2286643e69215c1186680f2b993f  10.0.16299.0/um/x64/Htmlhelp.Lib
abc175a8937d55f525d8539b4e477e28  10.0.16299.0/um/x64/hrtfapo.lib
cfa90e93bb9845687cea7424cad6b5bd  10.0.16299.0/um/x64/HLink.Lib
56bbfe02d74932fba32a3149e976855a  10.0.16299.0/um/x64/hid.lib
67c091165cbb7cb8d218f8bb00c5b36d  10.0.16299.0/um/x64/hhsetup.lib
4178a65b8ec880d571bbd6c973f3c713  10.0.16299.0/um/x64/hbaapi.lib
035315d008964ce3acaf037fc5649f6f  10.0.16299.0/um/x64/gpmuuid.lib
f951c064e885b98f56c1e03a7d1468c0  10.0.16299.0/um/x64/GPEdit.lib
c338a1c2f7871996dadc4f89d7fa1da8  10.0.16299.0/um/x64/GlU32.Lib
2bcd4a2c9c5474c5aea4b41364117668  10.0.16299.0/um/x64/glmf32.lib
6944dad1bb26dd8a6ef86df0939bdf13  10.0.16299.0/um/x64/gdiplus.lib
2e9bf2a907fe294a866c7ded7f33424d  10.0.16299.0/um/x64/Gdi32.Lib
cec4ffe65c93e55595ed5f5a5d82bd70  10.0.16299.0/um/x64/fxsutility.lib
2c0c2bce0499ba4eadd124bc6c81dd5f  10.0.16299.0/um/x64/fwpuclnt.lib
49aacf991f91b4f48af88420a51e2df7  10.0.16299.0/um/x64/FrameDyn.Lib
76f9166f36c727f236c25303b81acbe2  10.0.16299.0/um/x64/FrameDyd.Lib
1ff134c1eb3e45ec95e4ed7ed6724ef1  10.0.16299.0/um/x64/fontsub.lib
fd01914573d434f5ac60b89d2297f361  10.0.16299.0/um/x64/fltLib.lib
819232c366f25c5069b59e727b9b9024  10.0.16299.0/um/x64/FhSvcCtl.lib
8b7f6672d37f1434c4d2d362dcf23a35  10.0.16299.0/um/x64/fileextd.lib
98b842b0b5e01d854d3ad6c64168a640  10.0.16299.0/um/x64/feclient.lib
6ac1ed44e394a794fb4a45bc08364a68  10.0.16299.0/um/x64/FaultRep.Lib
5479371f0f92bad92ec02cbe852e54e5  10.0.16299.0/um/x64/evr.lib
c40cebd31774c0f129db19fc8fb99395  10.0.16299.0/um/x64/esent.lib
659fb1320efa569f7adced769a4d0b2f  10.0.16299.0/um/x64/ElsCore.lib
81dc73ced6fbf91cc8d9db6c2d4f4555  10.0.16299.0/um/x64/els.lib
c9d6cd00085d2ec78d9c8817e77820b5  10.0.16299.0/um/x64/elfapi.lib
971c73449d2d9e4fc1e273fbb49541be  10.0.16299.0/um/x64/ehstorguids.lib
6991623e58ea4cf0f98fdaf874eeca9d  10.0.16299.0/um/x64/efswrt.lib
21617f637ae17e75dd2b27c755001b2f  10.0.16299.0/um/x64/easregprov.lib
79c4e44a92dc2ad215ced2e970302580  10.0.16299.0/um/x64/eappprxy.lib
9b456ef7265317888437a9b9bf79745b  10.0.16299.0/um/x64/eappcfg.lib
b64cbb68322b5f8ec911813efd012be1  10.0.16299.0/um/x64/dxva2.lib
7f7ca0ee957a67aa075ea99a0fe63e72  10.0.16299.0/um/x64/dxtrans.lib
4c193de22209e915a415937971c661fe  10.0.16299.0/um/x64/dxtmsft.lib
2ad872959347ebc63ecc6548f92a4df9  10.0.16299.0/um/x64/dxguid.lib
ab9a98aeeb59c742a45942cda80e1349  10.0.16299.0/um/x64/dxgi.lib
6a6ca000c875ce0498d8c21da4c18442  10.0.16299.0/um/x64/dwrite.lib
df444d9527bf9b496bf42e279e61c4d0  10.0.16299.0/um/x64/dwmapi.lib
9ece2b5a5ecaffab380f3e09bd7e6704  10.0.16299.0/um/x64/DtcHelp.Lib
b7e491e10b61531812c8be6763890cb5  10.0.16299.0/um/x64/dststlog.lib
1f8552845755ead810997319f9f160aa  10.0.16299.0/um/x64/dssec.lib
3de38bf140cf0e8969266b0cac029977  10.0.16299.0/um/x64/DSProp.Lib
b3239b8d132be0a50d1ed372fda3c19c  10.0.16299.0/um/x64/dsound.lib
890994825fddcdb0cbe5e0ca2321280b  10.0.16299.0/um/x64/drttransport.lib
e0da4f0bc6d277b3e0c7aaf2b50bd747  10.0.16299.0/um/x64/drtprov.lib
5cec2edc9e7d1c96de8b76822a1692e4  10.0.16299.0/um/x64/DSUIExt.Lib
ea91aacd8f1f8aa64480772b930d790d  10.0.16299.0/um/x64/drt.lib
ed0a9a55b9538966c7b10cb0031d89f4  10.0.16299.0/um/x64/dpx.lib
8dc5286c1097d86a21cbe6d4afc40072  10.0.16299.0/um/x64/dnsrslvr.lib
f882e271d2e366b507258e67a81820eb  10.0.16299.0/um/x64/dnsperf.lib
a2c4338ef6c0f64aaef3e913fac1ede4  10.0.16299.0/um/x64/dnslib.lib
2dd65a1985b9660c8c45f48c422f5a30  10.0.16299.0/um/x64/dnsrpc.lib
1c501b92fe8d1a095e3005253e40234c  10.0.16299.0/um/x64/dnscrcli.lib
dcde7c13138f2f900428868401cf0694  10.0.16299.0/um/x64/DnsAPI.Lib
c80afdae777124bee2abce1845916f3f  10.0.16299.0/um/x64/dmprocessxmlfiltered.lib
579dfd01384511f5aa4ef029ed4cbb7d  10.0.16299.0/um/x64/dmoguids.lib
3250f81d39c34fd846eae30ce28974a5  10.0.16299.0/um/x64/dloadhelper.lib
36392dd03626542a37aa5cf2f6c95551  10.0.16299.0/um/x64/dinput8.lib
b5a1af5800a23bb43cd50ba8946ea737  10.0.16299.0/um/x64/difxapi.lib
6e4fba4df2e42fda67432c0ab8dee443  10.0.16299.0/um/x64/dhcpsapi.lib
529233c1364c77148db521a506369f43  10.0.16299.0/um/x64/DhcpCSvc6.Lib
167201306db632cdd67ae62c58c26041  10.0.16299.0/um/x64/DhcpCSvc.Lib
c7b146382c77e22e155661e1e1c47930  10.0.16299.0/um/x64/dflayout.lib
5a51166d08f295abd334357694388e2f  10.0.16299.0/um/x64/devmgr.lib
0fa981d36359a720251bff285165dfc3  10.0.16299.0/um/x64/deviceaccess.lib
c0f6f29b8fbaa8ae7f1dc1e09b74da5b  10.0.16299.0/um/x64/devenum.lib
c553b24de5be8893d2c39c720e952e40  10.0.16299.0/um/x64/ddraw.lib
e9af6cf2c8307417de13567634bf5918  10.0.16299.0/um/x64/dcomp.lib
d9862260268e09152c77bd93b4e007bf  10.0.16299.0/um/x64/dciman32.lib
1671f82ce96c75a4454e1b8f212938f0  10.0.16299.0/um/x64/DbgHelp.Lib
afcd91912e30697d589066d20b9db73f  10.0.16299.0/um/x64/DbgEng.Lib
046f60ed890d03f7de8277893801f168  10.0.16299.0/um/x64/davclnt.lib
55df014c9f0504a732221d9ab889583e  10.0.16299.0/um/x64/d3dcsxd.lib
393be1ddfe66b81309cee99f45c0fa74  10.0.16299.0/um/x64/d3dcompiler.lib
048125fd7083ff71c264532d4e8a7af8  10.0.16299.0/um/x64/d3dcsx.lib
a6acbf7bf6111cb3054fcf0d07061ff8  10.0.16299.0/um/x64/d3d9.lib
8b48214c9948e67af12384701660ac18  10.0.16299.0/um/x64/d3d11.lib
0765388740dd3e96999388a8952e78a3  10.0.16299.0/um/x64/d3d12.lib
abaca0da5be9d307673d1da1ad026dd4  10.0.16299.0/um/x64/d3d10_1.lib
12db165647f81b0a521ecc79ef4e3913  10.0.16299.0/um/x64/d3d10.lib
2910f29b402d797bdc4ba1110ea318cd  10.0.16299.0/um/x64/d2d1.lib
78d13931ff6d1b4c7952269c222674da  10.0.16299.0/um/x64/cscdll.lib
0307b961315428c291ea89175a68e02d  10.0.16299.0/um/x64/cscapi.lib
c88116d6acf28265a7f4d2f33e59c190  10.0.16299.0/um/x64/cryptui.lib
58c8e6f7ef8108729e45a06a800602c4  10.0.16299.0/um/x64/cryptxml.lib
94b277f0a89d13d65991ff0810638496  10.0.16299.0/um/x64/CryptNet.Lib
d76ede5201dca9d2b0e951f60d6fc0d9  10.0.16299.0/um/x64/cryptdll.lib
7134e328fbafb5609f6c894e10eacfa6  10.0.16299.0/um/x64/Crypt32.Lib
435485c885193e47b78c8e6358a31578  10.0.16299.0/um/x64/Credui.lib
0e56f8e540ed3f8e4b0191cf92741e99  10.0.16299.0/um/x64/corrEngine.lib
a171b199d5e91c5b3328987715d28c22  10.0.16299.0/um/x64/CoreMessaging.lib
66f52365ba86c75d669913fea2954f59  10.0.16299.0/um/x64/ComSvcs.Lib
33460098b1510f44b1baab8e5c5cd240  10.0.16299.0/um/x64/compstui.lib
a08757ae0537713a06f17671c87840a4  10.0.16299.0/um/x64/CompPkgSup.lib
44b6ba41d7f679c2e0f212af28b0e876  10.0.16299.0/um/x64/ComDlg32.Lib
998980de11b7f232cc3c74057c629774  10.0.16299.0/um/x64/ComCtl32.Lib
a266d18821d65046a2019b1c130df999  10.0.16299.0/um/x64/ClusApi.Lib
c0afad84a882810bad2c750a9a996a45  10.0.16299.0/um/x64/clfsmgmt.lib
5c2b7189a0fd69778ab207492372fafe  10.0.16299.0/um/x64/clfsw32.lib
a34c101616aa041d7f12f1cb3d620258  10.0.16299.0/um/x64/Chakrart.lib
a5629ae8556d74d5d544720d6c0f6f6b  10.0.16299.0/um/x64/cldapi.lib
b768a448eff8c8ad536ccbbfc60ef757  10.0.16299.0/um/x64/cfgmgr32.lib
ecfe8105232d3db49aa5dc35b6d105b4  10.0.16299.0/um/x64/CertPolEng.Lib
b9488f562128d543e6356c827f1cbc3a  10.0.16299.0/um/x64/CertIdl.Lib
a54b4e1a3b853fb770da88350531fa89  10.0.16299.0/um/x64/certcli.lib
e6bfa1188ff6cdd3cee807461bc58102  10.0.16299.0/um/x64/certca.lib
4a1c8d97821d3370ec7d9e782afc5ce3  10.0.16299.0/um/x64/certadm.lib
1ee71775a41d153b71def8c1152eaf4b  10.0.16299.0/um/x64/Cabinet.Lib
0e92192722954b267e033c24eaec6f5f  10.0.16299.0/um/x64/BufferOverflowU.lib
753fa0b02d27b74e023b3acfc88f178b  10.0.16299.0/um/x64/BufferOverflow.lib
305307e57d6f879d21fbe8418f829df2  10.0.16299.0/um/x64/bthprops.lib
9a26f808f323c2c628f8c6be84fa6cd9  10.0.16299.0/um/x64/BluetoothApis.lib
daeb887e148a28a1c544f352671714d5  10.0.16299.0/um/x64/Bits.Lib
fced579837960fb4f1d8455193f6ae66  10.0.16299.0/um/x64/bcrypt.lib
7014467e0609f0d3a7fb3a237b0f48b7  10.0.16299.0/um/x64/basesrv.lib
b994057e545398fa1723f7598a707ab7  10.0.16299.0/um/x64/avrt.lib
6848318f8a32cd7f399be0bd5375dcc6  10.0.16299.0/um/x64/avifil32.Lib
7acfadd4a008e7b561ecabd78dbbd690  10.0.16299.0/um/x64/aux_ulib.lib
516d543298e33197f036cca9bcf56f7e  10.0.16299.0/um/x64/AuthZ.Lib
0bae2c2b8376e68ce985858f9e463bb6  10.0.16299.0/um/x64/audioeng.lib
d8c57658cb03731a2a528bdafe45fe9a  10.0.16299.0/um/x64/audiomediatypecrt.lib
25b09df96fc23a123430323e1c66c8e1  10.0.16299.0/um/x64/AudioBaseProcessingObjectV140.lib
7c661581a4acfba99cc4f82e795b4b73  10.0.16299.0/um/x64/audiobaseprocessingobject.lib
bbd6131d31da91c56ea518c3734b6409  10.0.16299.0/um/x64/appnotify.lib
21a38718eb28440874f3bc9cb94ddf55  10.0.16299.0/um/x64/appmgr.lib
d29ebf3c339c6887eff358c0e03751fb  10.0.16299.0/um/x64/appmgmts.lib
6c4bbfc2cac16ed89d2912d1b9a72681  10.0.16299.0/um/x64/amstrmid.lib
2eae76af1d12b6a7c8d475f589dddb38  10.0.16299.0/um/x64/api-ms-win-net-isolation-l1-1-0.lib
ad9832c51ce8e1577c447e05a5bd734d  10.0.16299.0/um/x64/amsi.lib
59b26f38e7048ed3737d50649d19483f  10.0.16299.0/um/x64/ahadmin.lib
a0d9fd51c791130a17dba6ebfcfd48e5  10.0.16299.0/um/x64/advpack.Lib
c29220fc8e18d0fa250cead81e820c56  10.0.16299.0/um/x64/AdvAPI32.Lib
8bb72dc3716840be788a64631a6e1056  10.0.16299.0/um/x64/ADSIid.Lib
ba8bc026f0e09f29081c3c3649254cf7  10.0.16299.0/um/x64/ActiveDS.Lib
6a94ea66aa37715a11eeffb43120a358  10.0.16299.0/um/x64/AclUI.Lib
```

### ucrt: 10.0.17134.0

```
3c25a0289161fa4dbb3bd55178f65f14  10.0.17134.0/ucrt/x86/ucrtd.lib
51171c76b1c50e38049067d0d7d27d36  10.0.17134.0/ucrt/x86/ucrt.lib
592179e1b96a842998888caf311e6781  10.0.17134.0/ucrt/x86/libucrtd.lib
93025a15a90c2d952092dd27b36ddce5  10.0.17134.0/ucrt/x86/libucrt.lib
100bb4e5d65075ba737922abeb39f9dd  10.0.17134.0/ucrt/x64/ucrtd.lib
b7cd4e115e865ad89e5884982c7c1826  10.0.17134.0/ucrt/x64/ucrt.lib
6e4bc1c87a8ce6f8667400330f700287  10.0.17134.0/ucrt/x64/libucrtd.lib
870e0c062997bb9bb2a9b8036155a081  10.0.17134.0/ucrt/x64/libucrt.lib
b21350335dda88d1a94a4a4300a32345  10.0.17134.0/um/x64/AclUI.Lib
fad646a1ef8db433b2907fe401e5fc9a  10.0.17134.0/um/x64/ActiveDS.Lib
64074df6a13aef36d328309c2f3a1ef5  10.0.17134.0/um/x64/ADSIid.Lib
7f915a7ba7bc7e0561ecd2d21872332b  10.0.17134.0/um/x64/AdvAPI32.Lib
44d6f0dc2a62b0f4e038b2e40fa0da48  10.0.17134.0/um/x64/advpack.Lib
e1bc7983d54d8b99a655d22292d00ad3  10.0.17134.0/um/x64/ahadmin.lib
7e9346f2c76f4c6fb626d4dca2b06a2b  10.0.17134.0/um/x64/amsi.lib
02b7c245ee8447c1dad6faf3d941ded7  10.0.17134.0/um/x64/amstrmid.lib
2eae76af1d12b6a7c8d475f589dddb38  10.0.17134.0/um/x64/api-ms-win-net-isolation-l1-1-0.lib
c9be6ba8a78268654556274c2cf68043  10.0.17134.0/um/x64/appmgmts.lib
0a865bce6c259ebe6fe2a534ff38b1a3  10.0.17134.0/um/x64/appmgr.lib
bbd6131d31da91c56ea518c3734b6409  10.0.17134.0/um/x64/appnotify.lib
46cdd6460877c7f3963922a8a8940e15  10.0.17134.0/um/x64/audiobaseprocessingobject.lib
c164c8ea4004ac461faf46e30f327d20  10.0.17134.0/um/x64/AudioBaseProcessingObjectV140.lib
e5008bc2a9719f00026112e13d5dfa31  10.0.17134.0/um/x64/audioeng.lib
ca802f50cdfb642d945b3591373c42da  10.0.17134.0/um/x64/audiomediatypecrt.lib
43e520c5a143f329eaaa76f1779ed450  10.0.17134.0/um/x64/AuthZ.Lib
1ffad90e6fbc69e81d210c4aed178d9a  10.0.17134.0/um/x64/aux_ulib.lib
90cf7a67a4fbe7b9448d26ea00e9554f  10.0.17134.0/um/x64/avifil32.Lib
40e9b3014c8a85b394bf758b7116bfb3  10.0.17134.0/um/x64/avrt.lib
c81c09c94d1684c979407e72d618af97  10.0.17134.0/um/x64/basesrv.lib
157bc6645e8f7b1c640d28e7e1a8fdcb  10.0.17134.0/um/x64/bcrypt.lib
cc5bfa9550396e28903db712e376d420  10.0.17134.0/um/x64/Bits.Lib
ea2d0ad1f9f0a6dbb30cb637507cc652  10.0.17134.0/um/x64/BluetoothApis.lib
099ee7cd414ef9403bcec06a28462850  10.0.17134.0/um/x64/bthprops.lib
7fded511af0da520c7132416c0a261b2  10.0.17134.0/um/x64/BufferOverflow.lib
5d6625a7a7f8b0734ef9a4270e0cf390  10.0.17134.0/um/x64/BufferOverflowU.lib
56ce30aae9b135e6ee06d27ecc07ee1e  10.0.17134.0/um/x64/Cabinet.Lib
6b43540a09ab0a80543301f8074ce3d0  10.0.17134.0/um/x64/certadm.lib
11511ec602d4091e84469ac6de4f0bd4  10.0.17134.0/um/x64/certcli.lib
0e964faa2ab14cc972078c6a1e540472  10.0.17134.0/um/x64/CertIdl.Lib
65b8d727e618bdeb66a9e9d1be044708  10.0.17134.0/um/x64/CertPolEng.Lib
e45aefccebb828f5e3e7cf24a09214ba  10.0.17134.0/um/x64/cfgmgr32.lib
8fd4d03742352cbb8fca7306fe0dd64c  10.0.17134.0/um/x64/Chakrart.lib
f4f9a2c5d1c231d0e99eeef18f9b4787  10.0.17134.0/um/x64/cldapi.lib
78c7774dc87350ee3097ba1d19b2f972  10.0.17134.0/um/x64/certca.lib
19d8b0f04e3538d76248a981c799311e  10.0.17134.0/um/x64/clfsmgmt.lib
8b8491ce3ed5a848907d8dfe106f42d0  10.0.17134.0/um/x64/clfsw32.lib
c8aca1319745eca9a3ad908cfa943e5a  10.0.17134.0/um/x64/ClusApi.Lib
fbd685f37a4f8ad5636540f9255a0965  10.0.17134.0/um/x64/ComCtl32.Lib
6fadc790c91babf072a8bff70ef626ff  10.0.17134.0/um/x64/ComDlg32.Lib
cd38131c70a1622bb5db38795472f356  10.0.17134.0/um/x64/CompPkgSup.lib
a7240abf2c9af1ccaf4eb5758459abe8  10.0.17134.0/um/x64/compstui.lib
ce23413eae6810908a4ecf577e0b058d  10.0.17134.0/um/x64/ComSvcs.Lib
5faec999204d4d78f26e9922e5f55f68  10.0.17134.0/um/x64/CoreMessaging.lib
dfb3d9960e6cfabf8a8a1aa5d6085cd5  10.0.17134.0/um/x86/AclUI.Lib
48162713b62dfef063842128ad875243  10.0.17134.0/um/x64/Crypt32.Lib
710b0a7f3d5c6655ed5e8107bb90d198  10.0.17134.0/um/x64/cryptdll.lib
b67724e22727696f8079c3d46caede22  10.0.17134.0/um/x64/d3d10.lib
85b81ffff5625013fbb20947555db8d8  10.0.17134.0/um/x64/d3dcompiler.lib
56f22e1ca146907100a97ab062d76fac  10.0.17134.0/um/x64/d3dcsxd.lib
0af3ea69373bc36b383187ae1d2b61d2  10.0.17134.0/um/x64/davclnt.lib
412e8ee1e741ca69ae5093216a42594b  10.0.17134.0/um/x64/DbgEng.Lib
cb55b7daee67358ff0f3fdd8d94426c2  10.0.17134.0/um/x64/DbgHelp.Lib
ffba8dbd4bbd4e8635f6c509da3446e3  10.0.17134.0/um/x64/dciman32.lib
51d65b4462a2eb98f9c0ee75cdf5cfe7  10.0.17134.0/um/x64/DbgModel.Lib
6e5c042e23c0aa292064c538d3d48dbc  10.0.17134.0/um/x64/d3dcsx.lib
7a821f4714deca7764cef2476f21e4a1  10.0.17134.0/um/x64/d3d9.lib
e213a0a4769d3cf6bb4993fa8f7f9092  10.0.17134.0/um/x64/d3d12.lib
f07e02c07bf2dca21e30e3154350d128  10.0.17134.0/um/x64/d3d11.lib
e08b9758d300c848861e2d774b0ede36  10.0.17134.0/um/x64/d3d10_1.lib
3e7d5315b2f11176f5a17b3179c15f80  10.0.17134.0/um/x86/advpack.Lib
aa4f5df0d64da929a4cc47f985681b0d  10.0.17134.0/um/x64/ddraw.lib
5e5fb9ef93f4483f88eb37f75d31b828  10.0.17134.0/um/x86/api-ms-win-net-isolation-l1-1-0.lib
7dc4721e4f57f37067b184be69e6afd7  10.0.17134.0/um/x64/deviceaccess.lib
ad481afb7f84cb291b544ad84d18defb  10.0.17134.0/um/x64/dhcpsapi.lib
30b693aaf7db0a28642317f3c8f86a62  10.0.17134.0/um/x64/dinput8.lib
9c0e8215235dd1c3a646c28a2bc77fc6  10.0.17134.0/um/x64/dloadhelper.lib
1ab520a9084fbe7589b7198db41f0cf4  10.0.17134.0/um/x86/AdvAPI32.Lib
d53d3fd536329e6a02648dee8476e3c8  10.0.17134.0/um/x86/AudioBaseProcessingObjectV140.lib
2314e929688ca5bc1313cb0d8804bc7f  10.0.17134.0/um/x64/DnsAPI.Lib
408b535c416805a9cff166f5eb2b6a72  10.0.17134.0/um/x86/audiomediatypecrt.lib
ebecad0234f5c00467e402cf7bab4213  10.0.17134.0/um/x64/dnslib.lib
771c1ef3ce29877af705069d8c04d674  10.0.17134.0/um/x64/dnsperf.lib
0d0d783eb2028c6cc0d50a02b0f1a3cc  10.0.17134.0/um/x64/dnsrpc.lib
80a4f6302cc3d3a6e151dcb7dbcae65b  10.0.17134.0/um/x64/dnsrslvr.lib
c84911063a57c9dcd09c5436fcb7aead  10.0.17134.0/um/x86/basesrv.lib
1bfe4a504ac0fd86b10ed208b7f4dd79  10.0.17134.0/um/x64/drtprov.lib
2d846f150e4741399ef44beb578ca7c4  10.0.17134.0/um/x86/bcrypt.lib
8c35837618c4ee1d8454a22d48b03537  10.0.17134.0/um/x64/drttransport.lib
cb1dce5c69b5f4c14e2c69324770fe7a  10.0.17134.0/um/x86/Bits.Lib
5b6ea31174e6e764404a726836b2cbdc  10.0.17134.0/um/x64/DSProp.Lib
50452fcc2285d3abbb587bf41debaf6a  10.0.17134.0/um/x86/BufferOverflow.lib
931aa8df305178171e2ff5e3930fef08  10.0.17134.0/um/x64/dststlog.lib
5ae172c9c037d0dd92cc472289f46261  10.0.17134.0/um/x86/Cabinet.Lib
da84db1235bd988a01fd10f9855a9303  10.0.17134.0/um/x64/dwmapi.lib
0abe0731386db59aa6bfefa80269f68f  10.0.17134.0/um/x64/dwrite.lib
586d1366d272bd805baad9a2d2ee11b6  10.0.17134.0/um/x86/certcli.lib
9b51599f4c326449d5305ed265b7514c  10.0.17134.0/um/x86/certca.lib
3cebe1201e8c11e91acdaf54cf62c6c8  10.0.17134.0/um/x86/certadm.lib
3c07ecfabfd68b902c117fa68ff46664  10.0.17134.0/um/x64/DtcHelp.Lib
8791a39b6f776385c2e3cecda9eb3d35  10.0.17134.0/um/x64/DSUIExt.Lib
b5c60c6bb25bdd4d814fd650c5b01c5d  10.0.17134.0/um/x86/BufferOverflowU.lib
9fe2a8e8ef90ef5cb50d5acc9ad549e6  10.0.17134.0/um/x86/CertIdl.Lib
f19c2bf167c69da902dcc04349b4cef7  10.0.17134.0/um/x86/CertPolEng.Lib
5429d0a7215e67a68fd476c036067a4f  10.0.17134.0/um/x64/eappcfg.lib
0006ebee6691ee31ebf231864e7a55a5  10.0.17134.0/um/x64/easregprov.lib
31789fa9a94b3ac8b04a0e9f1ad6dc41  10.0.17134.0/um/x64/efswrt.lib
d58e8397c378e697c054fab41f1af647  10.0.17134.0/um/x64/elfapi.lib
0d55259fd6aa7d081593727a3cc8a0f0  10.0.17134.0/um/x64/evr.lib
df5181053542ee865952362e80f18bb2  10.0.17134.0/um/x86/clfsmgmt.lib
f10b8212f806b138072889c37e7df13e  10.0.17134.0/um/x86/clfsw32.lib
5945f98764b2a7afca3ed2b773dfb8a1  10.0.17134.0/um/x64/FhSvcCtl.lib
5e8c47dff8752e7f09de713224fd99b7  10.0.17134.0/um/x64/fileextd.lib
08de8516373e30b96760535bc3868c6c  10.0.17134.0/um/x64/fltLib.lib
a8d30bdb95b8df851d7ecf1193fc3ab2  10.0.17134.0/um/x64/fontsub.lib
93aec17a6fc3887efe26f6398baec913  10.0.17134.0/um/x64/FrameDyn.Lib
bcb5181d9127b9b1f0ab67c4b631600a  10.0.17134.0/um/x64/FrameDyd.Lib
642a68486891cce462a246c9b9cdc6ac  10.0.17134.0/um/x64/fwpuclnt.lib
5fd4988d96ef2cd5f5ebc5e4bff9f4a8  10.0.17134.0/um/x64/fxsutility.lib
b1dcc994fe93da8a6420324f7072173f  10.0.17134.0/um/x64/Gdi32.Lib
fd9788089bdf9f3ddb9e9bf97379ebf5  10.0.17134.0/um/x64/gdiplus.lib
03041f50c5d254d23e8008a3a151d285  10.0.17134.0/um/x64/GlU32.Lib
5cd9e623cb4ec851701a40de7d5cb704  10.0.17134.0/um/x64/GPEdit.lib
4fc5e714e601f4f16c8d88934242452c  10.0.17134.0/um/x64/gpmuuid.lib
6784a5e35009152b0a61ad04a6f974c2  10.0.17134.0/um/x64/hbaapi.lib
296d336999c2893ca9842f1ba0208844  10.0.17134.0/um/x64/hhsetup.lib
65ca5740c42ff01911d7074b626f5793  10.0.17134.0/um/x64/HLink.Lib
8e94ae2378af0a7d0747a2898756519e  10.0.17134.0/um/x64/glmf32.lib
da0d1039be2bc048ee9173894cf67d76  10.0.17134.0/um/x64/Htmlhelp.Lib
2a34a3110d15a816782100931bcc382e  10.0.17134.0/um/x86/ClusApi.Lib
f8171c16ed82350d7fa5c8001a58e211  10.0.17134.0/um/x64/hrtfapo.lib
6e1ebe2b26528bc44877f5977aced5b0  10.0.17134.0/um/x64/httpapi.lib
d25bac2e0bb4af2eb87b08278f644322  10.0.17134.0/um/x86/ComCtl32.Lib
140acf2362aa3058cc3a7c6353079413  10.0.17134.0/um/x64/icuuc.lib
ded8a9d65b8128669b48d2cf8b6b8fd0  10.0.17134.0/um/x86/CoreMessaging.lib
724c3817f88ed0ed4a433a7561055a1c  10.0.17134.0/um/x86/corrEngine.lib
0a0b372a65f3ea2803a7be648822878e  10.0.17134.0/um/x64/Imm32.Lib
c4de4cc8a517beef960bc15461f50e39  10.0.17134.0/um/x64/infocardapi.Lib
e2b4c95f26b3da0a5ee10ad8cb774dcd  10.0.17134.0/um/x86/cryptdll.lib
1f9812ff8e4999341f67277bfd21dc85  10.0.17134.0/um/x86/CryptNet.Lib
757791d2847513ec81263c7ec64ac4a4  10.0.17134.0/um/x64/iphlpapi.lib
26246fdbd267689bc21efaf37e3d8228  10.0.17134.0/um/x86/cryptui.lib
4d61f253736cf5091f2bf8f35d2d39e1  10.0.17134.0/um/x64/Iprop.Lib
1a2f93f99f8dc2a1fab8c928c06606da  10.0.17134.0/um/x86/cryptxml.lib
535e4dc6fb5c105d35fb2018e2c70559  10.0.17134.0/um/x86/cscapi.lib
26e9ec1a048bf835060abf3ed0d6e1cf  10.0.17134.0/um/x86/d2d1.lib
c1cc67347159e661b163dc7f7f5ec7d3  10.0.17134.0/um/x86/d3d10.lib
9a475ea0a7903e8f23098ba6c559e8fa  10.0.17134.0/um/x64/iscsidsc.lib
c66c3ecf572ebb7c62fd647489420162  10.0.17134.0/um/x86/d3d9.lib
b81f621e9ff3ea96e2f4b972b720adce  10.0.17134.0/um/x86/d3dcompiler.lib
6aa46b1587c730a46bb8ea2cd82a4fa0  10.0.17134.0/um/x64/kernel32legacylib.lib
c29e8897e856c948da609cb148134fea  10.0.17134.0/um/x64/keycredmgr.lib
d2489f8b25254bd4a47cc77caa55944c  10.0.17134.0/um/x86/davclnt.lib
50bca36a786f444d6f02602db74e8f52  10.0.17134.0/um/x86/DbgEng.Lib
40a4969d02e21bb0213e1b0ff2fbc5f2  10.0.17134.0/um/x86/DbgHelp.Lib
71aca46ebc0c26b63df715232820ef8f  10.0.17134.0/um/x64/ksuser.lib
d095b092b0447f2daa07fa3ee6ea61af  10.0.17134.0/um/x64/ktmw32.lib
8f272d625675705a23f063b16db8b711  10.0.17134.0/um/x86/dcomp.lib
dcf2005d6b08db4ebc8cb8f5fb369d38  10.0.17134.0/um/x86/devenum.lib
eb13891d40f95ea30981e35d21bf2543  10.0.17134.0/um/x86/devmgr.lib
59721f66fcd94ee23d9ca140df788f30  10.0.17134.0/um/x86/DhcpCSvc.Lib
8359df0fd87d335318c845296666f38f  10.0.17134.0/um/x86/difxapi.lib
1482fefcbbfcb82d3320dec795cab0da  10.0.17134.0/um/x64/Lz32.Lib
37f2e1c75af8778b4d70e05294f9b90a  10.0.17134.0/um/x86/dmoguids.lib
2fdfc432860aca8a3196a558efbd794d  10.0.17134.0/um/x64/locationapi.lib
b09c0705b53c3274a4e4cb0992868551  10.0.17134.0/um/x86/dloadhelper.lib
bca416fe45f0659286cefeb4a198b369  10.0.17134.0/um/x64/MAPI32.Lib
d0738f6bbe3459a7113cc5f8024f5ec4  10.0.17134.0/um/x86/DnsAPI.Lib
e6f01bb444275d3909483579509703e4  10.0.17134.0/um/x64/MDMRegistration.lib
43fd79347fee0e188dcb1ad389732751  10.0.17134.0/um/x64/Mf.lib
0c9f16202acdd3126dcb9a53d1a452c7  10.0.17134.0/um/x64/Mfcore.lib
df0497874fffb1622e9f66dae4ce5dcd  10.0.17134.0/um/x64/Mfplat.lib
87e1fc1c2c02eac5edf550bbf3a1f779  10.0.17134.0/um/x86/drtprov.lib
ce72b4f4fb41891f3a67a138291af485  10.0.17134.0/um/x86/DSProp.Lib
acd81bba940b3b491587bacf6ebc1b2a  10.0.17134.0/um/x64/mfuuid.lib
8b32c77cf9b5f8ef7d97a34ffb3b5797  10.0.17134.0/um/x64/mincore_downlevel.lib
6e404ec880b4c3da43a2014aa2b8a042  10.0.17134.0/um/x86/DtcHelp.Lib
eb18784270891ce70b2cbf95232af970  10.0.17134.0/um/x86/dwmapi.lib
c66ef7b5dda94a6df83bb8e7f59c7ecf  10.0.17134.0/um/x64/Mpr.Lib
4c6df65948249e3111624ceff2b0daea  10.0.17134.0/um/x86/dwrite.lib
850c303d4285b6322d14c95e87e62cfc  10.0.17134.0/um/x86/dxgi.lib
858fc3d0b850146b039c387285b96e46  10.0.17134.0/um/x64/MqOA.Lib
25fa8f1c080df3b1744a469656fe001c  10.0.17134.0/um/x64/mprsnap.lib
9d173e2330731d9b153ac7cb07381da8  10.0.17134.0/um/x64/Mprapi.Lib
810c276c47a7f07901cf717e973760fd  10.0.17134.0/um/x64/mmdevapi.lib
6f237da8cd47e08fbe81fa10eb5baded  10.0.17134.0/um/x64/MMC.Lib
baf88791968e5233e073eea2a1bad7f6  10.0.17134.0/um/x86/DSUIExt.Lib
4c44022908cc20a6eba5eb62cf16a56c  10.0.17134.0/um/x86/dxguid.lib
9e59469d938bb87c2a53b3602d70b7b9  10.0.17134.0/um/x86/dxtmsft.lib
c042ac9f94430a58f8dd8e26f600ca07  10.0.17134.0/um/x86/dxtrans.lib
07a0231ddc8934c774be4118378f01b1  10.0.17134.0/um/x86/dxva2.lib
2bb9fa93af5a866cd01ad69a3f35e1d9  10.0.17134.0/um/x86/eappprxy.lib
f9f92c1a5563aaeed77b961e2e98ec79  10.0.17134.0/um/x86/efswrt.lib
90b3986b8517d92125b919203de445aa  10.0.17134.0/um/x86/easregprov.lib
12c42a8907c5d851088405a508f0b1d9  10.0.17134.0/um/x86/eappcfg.lib
08520e4c8b72ecfc97129bf9a34350a6  10.0.17134.0/um/x64/MqRt.Lib
21890bcb7485f8af4db0664de7dcb8d2  10.0.17134.0/um/x64/MrmSupport.lib
8e05f213e3272e69f0a7423532e2017c  10.0.17134.0/um/x64/MSRating.Lib
9a6c87b29301e105808379409754b8d5  10.0.17134.0/um/x64/MSTask.Lib
0fe6237e3505f2ee0ba7cf182030ab5e  10.0.17134.0/um/x64/msv1_0.lib
177d1bfd91b1b88a5cd92165c943aef8  10.0.17134.0/um/x64/MsXml2.Lib
aec4f1f6b7ebd7cf604d68f50e1071ea  10.0.17134.0/um/x64/msxml6.lib
5d3e47160d0ec4633112349bdf7b0a09  10.0.17134.0/um/x64/Mtx.Lib
cbba3e381dfb6a9cb4b9206457cd2c59  10.0.17134.0/um/x64/mtxdm.lib
e5c0f56141e9b258ab62bcf042bfdeda  10.0.17134.0/um/x64/msvfw32.Lib
ce06621c9d2f9c77976602fec4232512  10.0.17134.0/um/x64/MsWSock.Lib
9ba985b4c56564c0fa8c9cb90b9accca  10.0.17134.0/um/x64/msports.lib
bdedfc9c5ab0b7d11da83238f3bff5a9  10.0.17134.0/um/x64/mspbase.lib
c54b31a9a387de88b0227cda1262abfa  10.0.17134.0/um/x64/mspatchc.lib
b3304c08e944ab9cde95acaeecb04f7f  10.0.17134.0/um/x64/mspatcha.lib
1cbb172ff9d0caf436e200e2e2994cec  10.0.17134.0/um/x64/MSImg32.Lib
b0c9149cc95e4142db6ca3e4fd9178f1  10.0.17134.0/um/x64/Msi.Lib
fa00de1340986c03f44c4acc6c1ef6be  10.0.17134.0/um/x64/nanosrv.lib
1bd451cf927074bed65df9bfb71cf5b1  10.0.17134.0/um/x64/ncrypt.lib
28a422c2d30205b1c2e56e70140172ee  10.0.17134.0/um/x64/nddeapi.lib
28d01cb7d77d12f5d259fd78a23b265e  10.0.17134.0/um/x64/ndfapi.lib
b78859291cca98bec481b5bb403d0964  10.0.17134.0/um/x64/ndproxystub.lib
fa87bdfa338083ffae4bc15bf9ade4f5  10.0.17134.0/um/x64/NetAPI32.Lib
da213eaebf00370b6599a7d508162d45  10.0.17134.0/um/x64/netlib.lib
3977ef3dabf19574bbf2e3406dda2e42  10.0.17134.0/um/x64/NetSh.Lib
7fcde23e6aad24e78b83e15e4623d661  10.0.17134.0/um/x64/newdev.lib
13ff18b65257b5b34eab6b1365a2f341  10.0.17134.0/um/x64/ninput.lib
1ef76bd8cb6c9e0941742abfa34c792f  10.0.17134.0/um/x64/normaliz.lib
c0f8a112115ebd2ab161d3ad268839b7  10.0.17134.0/um/x64/nt.lib
a55b65b592f41316e89eeba650672155  10.0.17134.0/um/x64/ntdll.lib
940d3e75ae56651681e5f2cd940157a4  10.0.17134.0/um/x64/ntdsa.lib
8d38c38940233a75ef51b2e6edbb8f26  10.0.17134.0/um/x86/feclient.lib
1145d5521f06745efef099225dcf74ea  10.0.17134.0/um/x86/FhSvcCtl.lib
bc2fdf2d9a21957c669dab0ba5af6043  10.0.17134.0/um/x64/NtDsAPI.Lib
ae27696279db87e621da15adec436bc8  10.0.17134.0/um/x86/fileextd.lib
4a5c378222fce1ec929b17e730571a7f  10.0.17134.0/um/x64/ntdsatq.lib
47d01a65cec82c0c80a0ad242b77cf9f  10.0.17134.0/um/x86/fltLib.lib
12ba7a5efdf1bf20482be20f6df1b927  10.0.17134.0/um/x86/fontsub.lib
60968cae3af03ad283161c29d0c1c7e6  10.0.17134.0/um/x64/ntdsetup.lib
d3d22fd39c3ada3f660594c11420d39d  10.0.17134.0/um/x86/FrameDyd.Lib
87541e4adcfb6a65a72eb6b1ee946f69  10.0.17134.0/um/x64/ntfrsapi.lib
c0b4e33cd13ed4cac9fb80afd17b83a3  10.0.17134.0/um/x86/FrameDyn.Lib
94843636eff932aaed2f477966df3c86  10.0.17134.0/um/x64/ntlanman.lib
7e58ed8716fc3e09ec1b119c5dddea3d  10.0.17134.0/um/x64/ntmarta.lib
4f9cd8ad322f0020aa6c2fa775f4b334  10.0.17134.0/um/x86/fwpuclnt.lib
d61b077b76afac37263829fe5bd3d931  10.0.17134.0/um/x64/NtQuery.Lib
1fb0cabf0a4b1a555cd0f3dc44581caa  10.0.17134.0/um/x64/ntstc_libcmt.lib
89e275951d6da91363e76c644e8755f7  10.0.17134.0/um/x86/gdiplus.lib
807f1f462729605d72058379d421c8bb  10.0.17134.0/um/x64/objsel.lib
fea729bd25aa2d2d4ccfcf866e7c701d  10.0.17134.0/um/x86/glmf32.lib
882d32a5ace043d1ca9b06c7aabedd3a  10.0.17134.0/um/x64/odbc32.lib
30f40be8d3170f42017468bd433b8c07  10.0.17134.0/um/x86/GlU32.Lib
bd7407a452bf5956d064fa5c509c4024  10.0.17134.0/um/x86/GPEdit.lib
2228c62693a412a75308e25a3cbb7ca8  10.0.17134.0/um/x64/odbcbcp.lib
f002ed852396ff4223e345a73ac496cf  10.0.17134.0/um/x64/odbccp32.lib
8ffddc9f1912f42e6dd1df10c14394e7  10.0.17134.0/um/x86/hbaapi.lib
b136faac06b2ca16a8bce767ecd429db  10.0.17134.0/um/x86/gpmuuid.lib
610e2bdc72e843a20d321e9ddaf68f72  10.0.17134.0/um/x86/hhsetup.lib
2b407ce18b6505eac111f18659310f1f  10.0.17134.0/um/x86/hid.lib
83f3e8ff62133028a4c4b47b3ec1c274  10.0.17134.0/um/x64/OemLicense.lib
f54f93d4e781ea36cec04ab4442adc22  10.0.17134.0/um/x64/Ole32.Lib
7ee3ee0a38aebf357879c9af258ffad8  10.0.17134.0/um/x86/HLink.Lib
2f36795ba2f6be84d70ab71a34b35d62  10.0.17134.0/um/x64/ntstc_msvcrt.lib
2a04f285d0edda152a1eecf36cc363ef  10.0.17134.0/um/x86/hrtfapo.lib
51be71344c449bae106d38740ce4ecd4  10.0.17134.0/um/x64/OleAcc.Lib
27fc86c382bf9b912da887e325e345fb  10.0.17134.0/um/x86/Htmlhelp.Lib
98a8cf45389b67007e8ef16c74335207  10.0.17134.0/um/x86/Gdi32.Lib
e8cdd3c18fe9f5e1577354e71db71e45  10.0.17134.0/um/x64/OleAut32.Lib
c8ce3babaa2036852a4be008a7911bfe  10.0.17134.0/um/x86/httpapi.lib
17bb5dab76b1968f1bf49e67c63a6c11  10.0.17134.0/um/x64/olecli32.lib
be5122b4f4b3fe8c854eb389deb6eeb8  10.0.17134.0/um/x86/fxsutility.lib
cd9014d27f84dd954d099043c2326a09  10.0.17134.0/um/x64/oledb.lib
10bec7b5c331a35d6d2e0f8591f645aa  10.0.17134.0/um/x64/OleDlg.Lib
33e1a217c983ca39179bfc5fd9443618  10.0.17134.0/um/x64/olesvr32.lib
7573637d97fdc10d09574d2da3383185  10.0.17134.0/um/x64/ondemandconnroutehelper.lib
1539cf889de38f42c67d9a0543234bc3  10.0.17134.0/um/x64/OneCore.Lib
77e1047f92a5af7d44152a4413e0e3f9  10.0.17134.0/um/x64/OneCoreUAP.Lib
edd35ccc56f468c1bd7c15bf1c050c35  10.0.17134.0/um/x64/OneCoreUAP_downlevel.Lib
edd35ccc56f468c1bd7c15bf1c050c35  10.0.17134.0/um/x64/OneCore_downlevel.Lib
af060510054b739e207e141e84a2b8d6  10.0.17134.0/um/x64/OpenGL32.Lib
00864cd2f252b66302450ba847695f30  10.0.17134.0/um/x64/muiload.lib
337001a0e6ed81324340c651e568de32  10.0.17134.0/um/x64/opmxbox.Lib
5b865add78ea1bc68ab3668f93f52ea7  10.0.17134.0/um/x64/osptk.lib
fd9b0e887f84c6dfe9247bb365913749  10.0.17134.0/um/x64/p2p.lib
821c9179099b423e223c3a317cfa7aa2  10.0.17134.0/um/x64/p2pgraph.lib
774f231327a1f08b993beb4831158f7d  10.0.17134.0/um/x64/pathcch.lib
1cbe216679eb7e1291e124c7d352d1aa  10.0.17134.0/um/x64/PeerDist.lib
9c6b1e1cd704852e376ecd4d731ddbd6  10.0.17134.0/um/x64/PhotoAcquireUID.lib
f738fe4f401b36dd75d81367797e1d24  10.0.17134.0/um/x64/PortableDeviceGuids.lib
897ff2e3af5740fbe84cd6f698bcf475  10.0.17134.0/um/x64/powrprof.lib
dd1c5df6cf9287dc897f8a896ff63b19  10.0.17134.0/um/x64/prntvpt.lib
1a5516fe5c84b57cea648c34147d312e  10.0.17134.0/um/x64/propsys.lib
4440389bab6167dd6762bfb2dbcaf805  10.0.17134.0/um/x64/Psapi.Lib
22ca98c23f408da4e4b56316c5322b23  10.0.17134.0/um/x64/quartz.lib
d61b077b76afac37263829fe5bd3d931  10.0.17134.0/um/x64/query.lib
2c13982c432518bb621d67b1511da98e  10.0.17134.0/um/x64/Pdh.Lib
0c36341024775a93be866d961c894510  10.0.17134.0/um/x64/RASAPI32.Lib
aabe84e7931ad8e3c129125566785717  10.0.17134.0/um/x64/RASDlg.Lib
0baa697042a57a2b94491ea5e69a91ce  10.0.17134.0/um/x64/qwave.lib
b9f2088e4e76e053d15868eebe4bf604  10.0.17134.0/um/x64/rasuser.lib
9250c982e7e8b8f4ead0035bb2da70ef  10.0.17134.0/um/x64/Rpcns4.Lib
37c3e48f3497e16b1433be7436f76542  10.0.17134.0/um/x64/rpcproxy.lib
56145338b6b07431e8b446b636e08796  10.0.17134.0/um/x64/RpcRT4.Lib
55cfcabf3ad15446b30cebd4608c7945  10.0.17134.0/um/x64/rstrtmgr.lib
debcafa9cf9bd0d5d4b6ac5f7acee089  10.0.17134.0/um/x64/Rtm.Lib
c06c2972a29caad48307f4f749efcb8b  10.0.17134.0/um/x64/rpcutil.lib
2f4316c3e972da3a95bfac8823efd000  10.0.17134.0/um/x64/rtutils.lib
fed2a692607a3283aa1ac61ee3fe2f0a  10.0.17134.0/um/x64/rpcexts.lib
51b970cdad9323231a2e705187657a2e  10.0.17134.0/um/x64/rometadata.lib
89b02af90650b9238023f50c62d8b735  10.0.17134.0/um/x64/resutils.lib
a8060e01f1b3f6678596a5b5dce38e11  10.0.17134.0/um/x86/iashlpr.lib
22ece4a246ad94a646cdfa06016c3bb8  10.0.17134.0/um/x86/FaultRep.Lib
cc82d3c53468fe6abc2aa1409370bae0  10.0.17134.0/um/x64/msdrm.lib
aaf4f5a36260eea63affa2d29eba7456  10.0.17134.0/um/x64/msdmo.lib
13886fa3a7682970cb34b21e046318b8  10.0.17134.0/um/x86/evr.lib
2da48b809bd279d2bbee186f26c8d9fd  10.0.17134.0/um/x86/esent.lib
801dafeca8b4af965432efec20309cd6  10.0.17134.0/um/x64/msdelta.lib
31015651f68ed080f0ee0f150460be10  10.0.17134.0/um/x86/ElsCore.lib
ddd660da251677bc396b24e4ae293abf  10.0.17134.0/um/x86/els.lib
bed3c8e3f0e4e2486c1b931f5e3ab620  10.0.17134.0/um/x86/elfapi.lib
d8ffc408b0aa5e8d52cdaead5341c565  10.0.17134.0/um/x64/msdasc.lib
839df525749778bcbc6a914558aadc70  10.0.17134.0/um/x64/MsCtfMonitor.lib
7063dca25253b6a997b3f5af6ef1b937  10.0.17134.0/um/x86/ehstorguids.lib
690dae3a69330109ff2f2c3421d54f11  10.0.17134.0/um/x64/Mscms.Lib
2f06be4c522bee52fd1422780e20dc01  10.0.17134.0/um/x64/RTWorkQ.lib
84eafe7e0c93ab92b1980aa4fc47955d  10.0.17134.0/um/x86/Icm32.Lib
a78836b05fd2c119b9525339bf4e465e  10.0.17134.0/um/x64/runtimeobject.lib
306a654689fefb02655eb062979f8d2d  10.0.17134.0/um/x86/icuin.Lib
ecbb2e7838ddcce64562a2379f6f1abc  10.0.17134.0/um/x86/icuuc.lib
9fde019ff55514664a9ff15b8df990fc  10.0.17134.0/um/x64/samlib.lib
974f92257e120e4c377bd6ba4028d44e  10.0.17134.0/um/x86/iesetup.lib
7ead52958212cdc36d92ffaacef00cac  10.0.17134.0/um/x64/SAPI.Lib
2f4c39f9ea95f80e1ba7079fc54ed4d5  10.0.17134.0/um/x64/SCardDlg.Lib
0b83f555748cac7ef5253ec6127a7da2  10.0.17134.0/um/x64/scesrv.lib
293a61d863d33416fa452f5af09b27e7  10.0.17134.0/um/x86/imgutil.Lib
583ecf6b7226e9153168163304221986  10.0.17134.0/um/x64/ScrnSave.Lib
e8d2f728f16a1af4142ef4934847c6c9  10.0.17134.0/um/x64/ScrnSavW.Lib
f890f12e322a21c1e1a4c4d575231ab3  10.0.17134.0/um/x86/jsrt.lib
ccc9cf649324d7cece6acf41ab265750  10.0.17134.0/um/x86/kerbcli.lib
7adf74b01bb66c2e81eab9ac4b495e78  10.0.17134.0/um/x86/kernel32.Lib
5bbad49ae0219a865c39d9621a20c548  10.0.17134.0/um/x64/Secur32.Lib
07f6edc2a8362462f7e7139c9451da7d  10.0.17134.0/um/x64/SearchSDK.lib
f75467a49a1a98b47c1651c2a05297ad  10.0.17134.0/um/x64/security.lib
39ee925b2ed906aeeabedc0125f33321  10.0.17134.0/um/x86/keycredmgr.lib
397e93a8da57538a194618b506257775  10.0.17134.0/um/x64/sens.lib
189a07f668bb5a0587f858548d2da555  10.0.17134.0/um/x86/KSProxy.Lib
9b51b6d8ef0b82a2dde69f739223742f  10.0.17134.0/um/x86/kernel32legacylib.lib
ca368d161e1ad76a551d8af91e54e350  10.0.17134.0/um/x86/ksuser.lib
fd00b65c990cf441b13ea4f7fe7450db  10.0.17134.0/um/x86/jetoledb.lib
13d6289fe5725251c377216440df56e1  10.0.17134.0/um/x86/ktmw32.lib
18ad5ac1cf616810165165d472a13568  10.0.17134.0/um/x86/LoadPerf.Lib
0c6005d6003cab589724433d6ec3776f  10.0.17134.0/um/x64/sensorsapi.lib
c13e7767ce673f373e559b92b08fe600  10.0.17134.0/um/x64/SensAPI.Lib
9cf58a12e34f8864fb044e82a8e84184  10.0.17134.0/um/x64/SensorsUtils.lib
8885ebf3b07dcda133e44d1613bed899  10.0.17134.0/um/x64/SetupAPI.Lib
0c1b961d6d6a3a647b9f4939978f0635  10.0.17134.0/um/x86/locationapi.lib
7a6fade0a67c0bea05ac0c17a80997d6  10.0.17134.0/um/x64/Sfc.Lib
0ad5607fcf233d94cec18edc4909bbef  10.0.17134.0/um/x86/magnification.lib
749f8e4b3f653bb3372cafdebde59588  10.0.17134.0/um/x86/mbnapi_uuid.lib
831fe0eb3d3c4483d69c99c6dd2996fa  10.0.17134.0/um/x86/mciole32.lib
f20f01f945ae4d3973aaa3684647b062  10.0.17134.0/um/x64/ShFolder.Lib
34bbb9cc435deabe52fa46f1993be0c2  10.0.17134.0/um/x86/mdmlocalmanagement.lib
e984b85c3d1e567e1e42674da3fcf365  10.0.17134.0/um/x64/slc.lib
5b99c427cfb646c34c85dfcfe22c8dba  10.0.17134.0/um/x64/slcext.lib
5ed0e6d882375e7ccad0e207569af789  10.0.17134.0/um/x86/Mf.lib
b305ec27be685e03cd07a0eb534d410c  10.0.17134.0/um/x64/slwga.lib
995884c522528b9bce55c1acf560b995  10.0.17134.0/um/x64/SnmpAPI.Lib
a12c536c460f60f86f8e8dc853034b20  10.0.17134.0/um/x86/Mfplat.lib
2f9381bd5d04480e9c95306f687b4327  10.0.17134.0/um/x86/mfsensorgroup.lib
1997bdaae3a6565ab59f3f4b26101ae1  10.0.17134.0/um/x64/SrClient.lib
799c1fbbcc3ee3585e9ff37d1488f478  10.0.17134.0/um/x86/Mfsrcsnk.lib
0d1af51a4e6bfc03c819f2a32e7e788b  10.0.17134.0/um/x64/srpapi.lib
50fc337cb6e181be279244d37a5d0d04  10.0.17134.0/um/x86/mfuuid.lib
4337fdfd605a5829df67445cd3ea6778  10.0.17134.0/um/x64/ssdpapi.lib
a18ab68eda8d6ddf6fa3c0604607ca47  10.0.17134.0/um/x86/MgmtAPI.Lib
77b394952381b8dc9c442b87e52fe2f5  10.0.17134.0/um/x86/mi.lib
61fad682ebb1a99a993b5010ed278833  10.0.17134.0/um/x86/mincore.lib
948259d0c7723566eb21e878166627f8  10.0.17134.0/um/x64/Svcguid.Lib
09c60a1a25384428ee9acbd1b3212805  10.0.17134.0/um/x86/MsXml2.Lib
1f886ae9be4045df7593f315e4438229  10.0.17134.0/um/x86/Mtx.Lib
3ff8847b966c7580aaa6494d9063c4ca  10.0.17134.0/um/x86/mtxdm.lib
df6e092760f7c5c1f3f53720a1636ac7  10.0.17134.0/um/x86/muiload.lib
7e95483791c44c755ed31d3b75166bdd  10.0.17134.0/um/x86/nddeapi.lib
a39e2c5a4217ef9447342ab1ff70fd80  10.0.17134.0/um/x86/ndproxystub.lib
82a454587dae6610d0a7ed7aac39e747  10.0.17134.0/um/x86/ndfapi.lib
4caf03398d6448ab1a56dbc35b5f86e3  10.0.17134.0/um/x86/ncrypt.lib
c98efb947ff372a0118f839a2600adaf  10.0.17134.0/um/x86/msxml6.lib
8305782d76ed536d6a75e47c1f3c2a4c  10.0.17134.0/um/x86/MsWSock.Lib
8465f0c8b6c618f7c9b2851f6f4c7144  10.0.17134.0/um/x86/msv1_0.lib
8306f743604d3c4777f0a7f15dffc674  10.0.17134.0/um/x86/msvfw32.Lib
751d327242401bd364b1e65a615161b5  10.0.17134.0/um/x86/MSTask.Lib
90b12a1f0d35cee3ae254f2395b428df  10.0.17134.0/um/x86/MSRating.Lib
c4bb7fec982000800e476db2b640f8e8  10.0.17134.0/um/x86/msports.lib
61c41e5bfdd002efce1f2c347a5d645b  10.0.17134.0/um/x86/NetAPI32.Lib
8e426910e18afcd270872efb24233172  10.0.17134.0/um/x86/mspbase.lib
12b398c2538afe2d5ba1ade66b217473  10.0.17134.0/um/x86/netlib.lib
3c6ce8a2bc2e0dfd7a01a9e009a78c79  10.0.17134.0/um/x86/NetSh.Lib
02dbdd2db38ec47ab4169c184d9334ec  10.0.17134.0/um/x86/mspatchc.lib
bbe3ffe3b71a7c1325dfe9369d64c92b  10.0.17134.0/um/x86/mspatcha.lib
f65a000549bd50c35709bdca127106b0  10.0.17134.0/um/x86/MSImg32.Lib
e5c57bdc243fe4ef3e094fc16ded658d  10.0.17134.0/um/x86/Msi.Lib
10c5d0c09d559f5c53d4c080a4a6a056  10.0.17134.0/um/x86/msdrm.lib
a9ddeadab0562324f327edc4f34353a2  10.0.17134.0/um/x64/swdevice.lib
eb20d70ef5f4cde42bdda9d9d19646ce  10.0.17134.0/um/x64/synchronization.lib
5b99e1b2ce30965a12e3e8d13096790a  10.0.17134.0/um/x86/ninput.lib
9d4ed8aac9fbce09370e64c3342e6e6f  10.0.17134.0/um/x64/t2embed.lib
c22e273eb3699309d4e649fa3bedd5c1  10.0.17134.0/um/x64/Tapi32.Lib
0dd30c751519fe9776cb831def1f71a0  10.0.17134.0/um/x64/tapi32l.lib
97f7713181d371a3e73af24945dfe5d0  10.0.17134.0/um/x86/newdev.lib
b5219965ab43d4f8f4a8034ebc61f8bc  10.0.17134.0/um/x86/msdmo.lib
13e62c0b3ca9d361c1bc6ef46355d281  10.0.17134.0/um/x86/msdelta.lib
a0a7f7e87a80c7ec2e6b5f958c6c4b65  10.0.17134.0/um/x86/msdasc.lib
e8c360a2062ca28fea8d57be819f6c64  10.0.17134.0/um/x86/MsCtfMonitor.lib
0df328c5008f8485b69cda0a6015ffeb  10.0.17134.0/um/x64/structuredquery.lib
fcb44b0ac12680f6d1a66e5e44f4d6df  10.0.17134.0/um/x64/strsafe.lib
1d4229fb7048d66e147e26eea2dc35f3  10.0.17134.0/um/x86/normaliz.lib
ea6bd177d5d3fe9831c61bd921a34a6c  10.0.17134.0/um/x86/Mscms.Lib
cdacc5acc90ebfeb7401f59394f9ce34  10.0.17134.0/um/x64/taskschd.lib
6ad5e596e4a86898b05ff4e800d51349  10.0.17134.0/um/x64/tbs.lib
b15951511fa2a6131ee969542c18a35b  10.0.17134.0/um/x86/nt.lib
9788c535dec9b5cb2bb37032a4b981d7  10.0.17134.0/um/x64/tokenbinding.lib
0b264dc029f1e3127b2b287de36f2695  10.0.17134.0/um/x86/ntdsa.lib
9290fecf037164c0e99da88cdcbc911c  10.0.17134.0/um/x86/ntdsatq.lib
01a861fbe1f431567e18b60d1ff26e83  10.0.17134.0/um/x86/ntdsetup.lib
b2992dc1e6e25da72bdd04d30f2530aa  10.0.17134.0/um/x86/ntfrsapi.lib
093ab1a3db0426ba21d866fc95d989cc  10.0.17134.0/um/x86/ntmarta.lib
04e32c498c0b582fdecc78269560b452  10.0.17134.0/um/x86/ntstc_libcmt.lib
7e4f65b44febcf58efcff99347860197  10.0.17134.0/um/x64/ualapi.lib
175434e43d4749d554b071fcfa937dd2  10.0.17134.0/um/x86/ntstc_msvcrt.lib
34b5bca9d804062d21ed61ce5cece1f6  10.0.17134.0/um/x86/ntvdm.lib
1a4c2a9c4f44e0dc1d0570f83879d0c4  10.0.17134.0/um/x64/umpdddi.lib
44e29d39b5ea29404f4a9fa49723124e  10.0.17134.0/um/x86/objsel.lib
bb97ebe389a1b8a370c8a08e626826d3  10.0.17134.0/um/x86/odbc32.lib
7ad1fbb0d55a84072a0c1098c00e7af3  10.0.17134.0/um/x86/odbcbcp.lib
3fd165904449260671987e1cb4dfe01c  10.0.17134.0/um/x64/UserEnv.Lib
acf2862c81367a3320ba87c33c5cf8a9  10.0.17134.0/um/x64/USP10.Lib
d539fb0fc1f3c5a6742ca2b551c01521  10.0.17134.0/um/x64/Uuid.Lib
d4e2552233be2dacb08f3d6b7e82e107  10.0.17134.0/um/x86/odbccp32.lib
72912a0ffd825998ef78933d47aa5c7b  10.0.17134.0/um/x86/OemLicense.lib
9c3f0208831583e984e3e938a65146a4  10.0.17134.0/um/x64/Uxtheme.lib
da14767a80469e94d76d0020c50a6389  10.0.17134.0/um/x64/vccomsup.lib
e4ec4b077f4ef13b0ffd92ed42046286  10.0.17134.0/um/x86/OleAcc.Lib
c6a75740fc4c3eb898e833a85bdef39c  10.0.17134.0/um/x86/OleAut32.Lib
e3b29b2d82b7ebf142d5eedea1f02de5  10.0.17134.0/um/x86/olecli32.lib
31e625b3e9d5edf4ce654b210865d77b  10.0.17134.0/um/x86/oledb.lib
1740882d16c88d1b9d5bd9f69b14dc0c  10.0.17134.0/um/x86/OleDlg.Lib
b248b1929537260cd4dd504db1ea96c2  10.0.17134.0/um/x86/OlePro32.Lib
1c455c9164ab2b68b5e67f3f36ec05ea  10.0.17134.0/um/x64/vds_uuid.lib
608ae1c459a6e12c000df222bbafc7a6  10.0.17134.0/um/x64/Virtdisk.Lib
b84846e81ddb9df5093b9dbf9c62b7e8  10.0.17134.0/um/x64/vmsavedstatedumpprovider.lib
e1cc17124f2e037a75994d1a8443d38a  10.0.17134.0/um/x86/ondemandconnroutehelper.lib
2967e8c8be62a0182471e268d6ae3a39  10.0.17134.0/um/x86/olesvr32.lib
bf57d60dd9f1d42c0050666a5cd46c87  10.0.17134.0/um/x86/OneCore.Lib
793586003b7be1e6fdfb2d005eb76787  10.0.17134.0/um/x64/Vfw32.Lib
e2cfacccf60b55aceaeeea6381bafb78  10.0.17134.0/um/x86/OneCoreUAP.Lib
00774f02d8d2aabcd6373e8e009d340c  10.0.17134.0/um/x64/vertdll.lib
0dfd400c00c9b3b2eb6060d479a7ad58  10.0.17134.0/um/x86/OneCoreUAP_downlevel.Lib
38ce2a4d29046150efbbafb3b61d7b99  10.0.17134.0/um/x64/Version.Lib
0dfd400c00c9b3b2eb6060d479a7ad58  10.0.17134.0/um/x86/OneCore_downlevel.Lib
c50b692c70b156aaa5c4e06d485d2d81  10.0.17134.0/um/x86/OpenGL32.Lib
fca902a11a9e28322313d90232d8a944  10.0.17134.0/um/x86/Ole32.Lib
7f7c35df36b544118cf53c90b9a2d5d2  10.0.17134.0/um/x86/osptk.lib
80d5db9e03481b290bec06e20eb2456b  10.0.17134.0/um/x64/User32.Lib
f27a2ac923a3706ee7aec4af06c09bc0  10.0.17134.0/um/x64/Urlmon.Lib
24ed68e369985e624a8f98d7410e60d7  10.0.17134.0/um/x86/p2p.lib
3ed624564e715f45e901ad41aae53702  10.0.17134.0/um/x86/patchwiz.lib
890c36c352e7c2669ca161fe5899d98a  10.0.17134.0/um/x86/p2pgraph.lib
a82c03ff1578e129ca0af7df524274e9  10.0.17134.0/um/x86/pathcch.lib
fbae1501ed5fb18ebf622429f4b445a8  10.0.17134.0/um/x86/Pdh.Lib
c852aa443162e9a07e1e5137e5889a78  10.0.17134.0/um/x64/UIAutomationCore.lib
49fe003476f5ed592bb7ea3ca1fc26fe  10.0.17134.0/um/x86/PeerDist.lib
b9eb69a7c9d9459720fc9492fec53199  10.0.17134.0/um/x86/PhotoAcquireUID.lib
b220016b16fbddc68ed337872e8fe703  10.0.17134.0/um/x64/txfw32.lib
b1258503f31340c3e90ddc2e98274201  10.0.17134.0/um/x64/twinapi.lib
c34d0680cd02f9afcd6365c4b9c3b6d7  10.0.17134.0/um/x86/PortableDeviceGuids.lib
1d06d476fdcc8ba62d631c098ae4338a  10.0.17134.0/um/x86/powrprof.lib
895e0f4e3e1e184c053d94b8c9548c40  10.0.17134.0/um/x86/NtQuery.Lib
2064d7f18e75448a617da1736e562ddc  10.0.17134.0/um/x86/prntvpt.lib
1902269fa6a413d552622ec0384e9984  10.0.17134.0/um/x86/ntlanman.lib
f78ab6a9fda853c0e550e502fe4f6ae7  10.0.17134.0/um/x86/propsys.lib
197ad269875ee287affd9fc28cc6945f  10.0.17134.0/um/x64/tspubplugincom.lib
ee0ad1f8fbd44f6ca112291ae4bd4f44  10.0.17134.0/um/x86/Psapi.Lib
f91e9888de1dc0caa1fbf9025d4ff289  10.0.17134.0/um/x64/tsec.lib
d158aea6806a149a6f30fc9e841a7b02  10.0.17134.0/um/x86/quartz.lib
1a2861b936745a2f5e1c27f413bc3abf  10.0.17134.0/um/x64/TranscodeImageUID.lib
895e0f4e3e1e184c053d94b8c9548c40  10.0.17134.0/um/x86/query.lib
4a8172d4aef271f205a253c14691d893  10.0.17134.0/um/x86/qwave.lib
f8fc0367d620b7fd9fdec0451d863042  10.0.17134.0/um/x86/NtDsAPI.Lib
13777a6a4b33a5a71f3396624c972ec7  10.0.17134.0/um/x86/RASAPI32.Lib
0028593b065eef2faed6019ff46da2e3  10.0.17134.0/um/x86/ntdll.lib
6eb33aa2689dede6c7b291c642e0392e  10.0.17134.0/um/x64/Traffic.Lib
278bb91a2ea47da777601ceaed209993  10.0.17134.0/um/x86/RASDlg.Lib
bf335485bbad1c310f4419f3b42550e1  10.0.17134.0/um/x86/rasuser.lib
69c3f2712f74e01d64e7b5d28ed56416  10.0.17134.0/um/x64/tdh.lib
6d6af1875d7fd9d3db872e4aeede0da2  10.0.17134.0/um/x86/MSAJApi.lib
6eed44fd7acad40e9da6ae332aceb2cf  10.0.17134.0/um/x86/MSAcm32.Lib
1cbe1315933778c19dc9fb57973a5f63  10.0.17134.0/um/x86/resutils.lib
fa3e100fd175da0586beaeda18664095  10.0.17134.0/um/x86/rometadata.lib
700d89c80ac68813142beb1146a4964f  10.0.17134.0/um/x86/rpcexts.lib
65b0ec03765a8e056fcfea2e74e32f6a  10.0.17134.0/um/x86/msaatext.lib
56e053e82b86ef17ed7cc2009098b603  10.0.17134.0/um/x86/RpcRT4.Lib
20f81794080196bec5ec7e4d00cd2d51  10.0.17134.0/um/x86/rpcutil.lib
767ca46fa28200bf3fd49a7410df48d6  10.0.17134.0/um/x86/rstrtmgr.lib
3b94896b309d0c23af71d052a946cd64  10.0.17134.0/um/x86/Rtm.Lib
f376658aaa4559833f5a5ac7840153f4  10.0.17134.0/um/x86/runtimeobject.lib
d1ee7721a6fad14e09c931f60e7d6d07  10.0.17134.0/um/x86/samlib.lib
4c66eab7099a8acfbc2464dd599edc65  10.0.17134.0/um/x86/samsrv.lib
8f4e081f05c33d0c73bd328139a4e6e8  10.0.17134.0/um/x86/sbtsv.lib
07b0cc843d9f80c713b9d34d547163fd  10.0.17134.0/um/x86/SCardDlg.Lib
62a61cb34bc06de5aee54ee1d2c2d57b  10.0.17134.0/um/x86/scecli.lib
0de633733833801f30d42469e0260f1e  10.0.17134.0/um/x86/scesrv.lib
0739efcec2d8199e1103f85d5456a037  10.0.17134.0/um/x86/sas.lib
313bf3942745ca6c41f02eceaded133c  10.0.17134.0/um/x86/schannel.lib
fc62c1e09ecbe929db18c7924d5e7c0f  10.0.17134.0/um/x86/SAPI.Lib
7a7df1a6826f0210a65b677e6e368699  10.0.17134.0/um/x86/ScrnSave.Lib
12bdf247ca44b526219ce85d3f44b799  10.0.17134.0/um/x86/ScrnSavW.Lib
4989e98646f3b5a15a396801dc037b8e  10.0.17134.0/um/x86/RTWorkQ.lib
de41df527e850a6f76dc0816e3a1426b  10.0.17134.0/um/x86/SearchSDK.lib
bb31ba3225fd0a0caede35d424590a96  10.0.17134.0/um/x86/rtutils.lib
45805050729772e23a3d36c88d1086f9  10.0.17134.0/um/x86/Secur32.Lib
595466861957b62ff57653f31e7a7978  10.0.17134.0/um/x86/rpcproxy.lib
7d3d4cd585314e538ae2dbdb480c2152  10.0.17134.0/um/x86/Rpcns4.Lib
99d4b217b82444937e858e765d9d81a0  10.0.17134.0/um/x86/security.lib
989665cb53fd517d982014f40e029fce  10.0.17134.0/um/x86/MrmSupport.lib
f9231733d081b908431f5ad002171834  10.0.17134.0/um/x86/sens.lib
ddd326323dda1c8ad2ea7a9b302a111b  10.0.17134.0/um/x86/MqRt.Lib
b9abe7e94a316ad393d596edd6bc8025  10.0.17134.0/um/x86/SensAPI.Lib
8cede4e8da4e4fa9ce851821fa4b3c26  10.0.17134.0/um/x86/sensorsapi.lib
32a3ba8d9e676e289b7b64b828827147  10.0.17134.0/um/x86/SensorsUtils.lib
d73a6e7d2ba1e5c27238b6cbb3b1f8af  10.0.17134.0/um/x86/MqOA.Lib
84d588678a9df3f994001a334ffc2fb3  10.0.17134.0/um/x86/mprsnap.lib
a944acc5498c739bbac63a6a4b1fcf8f  10.0.17134.0/um/x86/Mprapi.Lib
5b7651f2199379208b5f3390513f353d  10.0.17134.0/um/x86/Mpr.Lib
d33fd8886e2af49cadddffd4efe8bc6e  10.0.17134.0/um/x86/mmdevapi.lib
4647d0f5d4f4dec2279e46854b1be3c0  10.0.17134.0/um/x86/SetupAPI.Lib
f49f6e00741fc928cd1c7fd8cc2f8416  10.0.17134.0/um/x86/MMC.Lib
209c3bfced9b901cc1fdd9ed4b1880fe  10.0.17134.0/um/x86/Sfc.Lib
8acf41ac1feac1c0ec786c11ca1f736f  10.0.17134.0/um/x86/shcore.lib
3d100714bb6411a0e790938389f252c5  10.0.17134.0/um/x86/shdocvw.lib
9285f80941fad71aa0eb0ffdb8e32683  10.0.17134.0/um/x86/shell32.lib
0da43b9e0bfdcdadd4cdbe45de7473e1  10.0.17134.0/um/x86/ShFolder.Lib
71da2197da322b10b7228b70ba63b2f3  10.0.17134.0/um/x86/ShLwApi.Lib
bf50db67758538ebbb843f613b5e5b0d  10.0.17134.0/um/x86/slc.lib
119ba0e3acbce9fe86cb6c36c6354fa0  10.0.17134.0/um/x86/mincore_downlevel.lib
1a7c5f3cd871cd02b19d1c45b76b814d  10.0.17134.0/um/x86/slcext.lib
06a9da3ef9485526d8f29714a955cc0c  10.0.17134.0/um/x86/slwga.lib
02b7c245ee8447c1dad6faf3d941ded7  10.0.17134.0/um/x64/strmiids.lib
80dab64ff8243b9d036b73687fa5f16a  10.0.17134.0/um/x86/SnmpAPI.Lib
312c39d6ecf8747adb0c85da51ac6561  10.0.17134.0/um/x86/spoolss.lib
4fded930fd60c8f3df66b4bd74df3271  10.0.17134.0/um/x86/SpOrder.Lib
49aa0c6d071394c9248f2dd533fcd6a2  10.0.17134.0/um/x64/strmbase.lib
ceedcaed051172c5021cbd41cca4042f  10.0.17134.0/um/x86/SrClient.lib
69773a34493e90d5eb04dae440b1b478  10.0.17134.0/um/x86/srpapi.lib
754d3f55137caf2d8339e88c7e620b39  10.0.17134.0/um/x86/ssdpapi.lib
5e4c3ec9ea3792f7625c2c8e12bb2d2d  10.0.17134.0/um/x64/Sti.Lib
f819df2e01d4ed4b0214b679c7739efc  10.0.17134.0/um/x86/Sti.Lib
e71dcd81e0fe24857a39e6ab8952042b  10.0.17134.0/um/x86/strmbase.lib
76ae8e26b37d403a5e1ce7afa5592cf4  10.0.17134.0/um/x86/strmiids.lib
1a0fbecd6aef98678f1c4804aba39b15  10.0.17134.0/um/x86/strsafe.lib
e777e887b24219266e321d27800e2273  10.0.17134.0/um/x86/structuredquery.lib
15838644f763a3ae075270378539d4fd  10.0.17134.0/um/x86/Svcguid.Lib
60eb2e92f650cee9eddb4b3372b50cbd  10.0.17134.0/um/x86/swdevice.lib
7c302cd09570e4e45d101ffed2af5466  10.0.17134.0/um/x86/synchronization.lib
a67b820a0d9d81bf1428a3117318f638  10.0.17134.0/um/x64/SpOrder.Lib
a697d2e8e6260d1a5e29ba9a63486e87  10.0.17134.0/um/x86/t2embed.lib
306a29b9f48a373bb928bba531e4657b  10.0.17134.0/um/x86/Tapi32.Lib
26523440be53e73cca47e1922ab448c2  10.0.17134.0/um/x86/tapi32l.lib
1efe122faa1aedddfdc929a5ec19105b  10.0.17134.0/um/x86/mfreadwrite.lib
27a1a4c054d256de984dd2eb6ec8437d  10.0.17134.0/um/x86/taskschd.lib
17a839d5e0502693f194fac41dfd626f  10.0.17134.0/um/x64/spoolss.lib
8d6cda09b608d771c53238bf5e07afd4  10.0.17134.0/um/x86/mfplay.lib
55dca3db6e06031426c81ea2d7e1f547  10.0.17134.0/um/x86/tbs.lib
e92185a5b2c67802ec2533091ddb69e6  10.0.17134.0/um/x86/tdh.lib
40e78e0be8ac2004fbada77281c2f5f3  10.0.17134.0/um/x86/Thunk32.Lib
4660fb30f1a6b0549e6a81c0acba6550  10.0.17134.0/um/x86/tokenbinding.lib
b5b33cc9846a613f25bb4dbf704d206d  10.0.17134.0/um/x86/Mfcore.lib
dff6115b6358819f535a17fa993c80fb  10.0.17134.0/um/x86/Traffic.Lib
dbe3ee7c876e0b47eda901e2d0bf9e4f  10.0.17134.0/um/x86/tsec.lib
f3ae8f60a658d025e7feeeaf08938a32  10.0.17134.0/um/x86/TranscodeImageUID.lib
9c5d1d99791b40427c15e723a38dfc6f  10.0.17134.0/um/x86/tspubplugincom.lib
630952bb6037132c5546ceb96631c4d0  10.0.17134.0/um/x86/MDMRegistration.lib
fee0a890961c0a5283fe57ca57dd482e  10.0.17134.0/um/x86/twain_32.lib
518532669e8ca82750d427df6048ece0  10.0.17134.0/um/x64/ShLwApi.Lib
d04573333979316ca5cfcf0449140289  10.0.17134.0/um/x86/twinapi.lib
6aafa021fb2a814b6b68c2c1230783f7  10.0.17134.0/um/x86/txfw32.lib
386bce20a9006dd32620f472b010610e  10.0.17134.0/um/x64/shell32.lib
ba44f4c739a7ea5068a6fbd8aaf65ef9  10.0.17134.0/um/x64/shdocvw.lib
e29e40a6c8211c011cd82ec25bdd971c  10.0.17134.0/um/x86/ualapi.lib
0c98bfeda4caf1882606bb1084107ff1  10.0.17134.0/um/x64/shcore.lib
320d604d0879dea0bbfc15360839f91d  10.0.17134.0/um/x86/MAPI32.Lib
28bcef8068ecefba4886bba8f5d9e758  10.0.17134.0/um/x86/umpdddi.lib
f585a6fc5ced728bad5181d0afca851a  10.0.17134.0/um/x86/UIAutomationCore.lib
386b497e656098b5ae3194ce2070a329  10.0.17134.0/um/x86/unicows.lib
0e27c9f6dba631b9b23752108fcc00dd  10.0.17134.0/um/x86/Urlmon.Lib
ec7e5a6e9ccdb3625041b580bb50aee3  10.0.17134.0/um/x86/Lz32.Lib
702c592c789cae30177b34af80599eb7  10.0.17134.0/um/x86/User32.Lib
7252d4694939e7e9a9f4fc7baaa3f430  10.0.17134.0/um/x86/UserEnv.Lib
ca3b12fa9fc99eeddcccfb4aaa775de5  10.0.17134.0/um/x64/schannel.lib
14e6717b56f948f11795896c6b6bb914  10.0.17134.0/um/x86/USP10.Lib
0b6485b1f1efae258254d4b50316ebe8  10.0.17134.0/um/x86/iscsidsc.lib
7913c0c81359c4b43341b9a2e4a5de2f  10.0.17134.0/um/x86/irprops.lib
5dd9b4fb8a0d645b19f9ae1191369262  10.0.17134.0/um/x86/Uuid.Lib
951436429272d5823b32b552f980873e  10.0.17134.0/um/x86/Uxtheme.lib
68f85a70832ee5b05d98499c31793f7c  10.0.17134.0/um/x86/vccomsup.lib
73fb2016ee065ec98bb3e0b36b81e8d9  10.0.17134.0/um/x86/Iprop.Lib
9bff6ecd16be501b690079f1523064b3  10.0.17134.0/um/x64/scecli.lib
567ce91536675f8447bc28bd0dbc32e9  10.0.17134.0/um/x86/VdmDbg.Lib
cb826f33fc7552dff983c12cad01e68c  10.0.17134.0/um/x86/int64.lib
29cbf7789a48cf2c519953da9cd1e99c  10.0.17134.0/um/x86/vds_uuid.lib
7ac7c5513ffd82dba46997ea23c137b4  10.0.17134.0/um/x86/Version.Lib
2e4f61c225cfbf32435ed85732686ca8  10.0.17134.0/um/x86/inseng.lib
c2e3f9fe479cc5982833efaab2748090  10.0.17134.0/um/x86/iphlpapi.lib
a377bd4270e2b9d010f0fecdff4e1fa7  10.0.17134.0/um/x86/Virtdisk.Lib
35e28667ee20f678e20d4c8da9dc5bf7  10.0.17134.0/um/x86/Vfw32.Lib
4960eaba80ec49322dc01ee9fd2f72f8  10.0.17134.0/um/x86/vscmgr.lib
ad81c5845534285d9e60b0fc96ab5133  10.0.17134.0/um/x86/vssapi.lib
3ecb829d10df88d1a26d9900004c1277  10.0.17134.0/um/x86/inkobjcore.lib
940e925bc003c94e9680e599997a1163  10.0.17134.0/um/x86/vss_uuid.lib
d66360b034534bca06fc4159472ae2fa  10.0.17134.0/um/x86/infocardapi.Lib
f3427ee9cc19ea9436a84d40982cef05  10.0.17134.0/um/x86/vstorinterface.lib
9133799242a08f092aa4aade20501e44  10.0.17134.0/um/x86/Imm32.Lib
358fc21dfd4d4488010360c63f38ec0a  10.0.17134.0/um/x86/wbemuuid.lib
71d01671563dd0b65ceed82af858d39e  10.0.17134.0/um/x86/wcmapi.lib
4f3989f0391ba9874b3c249d21f2669f  10.0.17134.0/um/x64/sbtsv.lib
ae343ecb3e5a307b6dc8617607a4c244  10.0.17134.0/um/x86/wcmguid.lib
0a00a418519d0d36937174a3d09d156b  10.0.17134.0/um/x86/wdsbp.lib
068071842f02f2a2cb0915979534a43f  10.0.17134.0/um/x64/sas.lib
a26f2d837a8bbcc5068cb95f000c2497  10.0.17134.0/um/x86/wdsClientAPI.LIB
617869bd775c5dc383b5939f4f03c932  10.0.17134.0/um/x86/ImageHlp.Lib
859a7f3441fe909d0730a2d6a59265eb  10.0.17134.0/um/x86/wdsmc.lib
1a03ccb588c1f58f3e17fe1fb7b8d71e  10.0.17134.0/um/x86/wdspxe.lib
0f474633222dac09ac05de1483ea7967  10.0.17134.0/um/x64/samsrv.lib
af504a5abefb37c5d32c73942f1cf578  10.0.17134.0/um/x86/wdstptc.lib
3385ff257f208527e5feacae8bec8ca3  10.0.17134.0/um/x86/WebServices.lib
1fe25eb90ddd310d1c3bdfc21d45b3d7  10.0.17134.0/um/x86/IEPMAPI.Lib
dfbd1784145d6a072b51ca8a7ac0fa52  10.0.17134.0/um/x86/websocket.lib
06ff9a920e893d78d2b9609f077d34c1  10.0.17134.0/um/x86/wecapi.lib
aa717d040a911e06bd809737f40e6773  10.0.17134.0/um/x86/Wer.lib
af9702075d39487fda66eb03e67477d3  10.0.17134.0/um/x86/Icmui.Lib
3ec761d7a3b62ccb069639b8cf756ca6  10.0.17134.0/um/x86/wevtapi.lib
8ff2f9f0eda01adead5cbbec1fd26358  10.0.17134.0/um/x86/WiaGuid.Lib
77e30a215d031d760f653a76f38c4b19  10.0.17134.0/um/x86/wiaservc.lib
67ef2e2828946fbde9e1bd218b60ac41  10.0.17134.0/um/x64/MSAJApi.lib
77d9dd3919c6504deed0dd94884e4210  10.0.17134.0/um/x86/wiautil.lib
7f17881c1e056702c9f9ff3532b2124b  10.0.17134.0/um/x64/MSAcm32.Lib
d4504d9772d769967128bba7118ad9f5  10.0.17134.0/um/x64/msaatext.lib
537b801cebdc8979b51630405f8497bf  10.0.17134.0/um/x86/WinBio.lib
0ce0e527140100b8b31c79c028c87b8d  10.0.17134.0/um/x86/windows.data.pdf.lib
7fa4bc6de6d5c5321fca8876ae6e32c0  10.0.17134.0/um/x86/windows.networking.lib
1a9a42387b823d33d43c3c58eed4a11b  10.0.17134.0/um/x86/windows.ui.lib
eab1d2a02b27b6a32b045493fb1ca35b  10.0.17134.0/um/x86/WindowsApp.lib
c89a9b6916641462fda7f879a36ca392  10.0.17134.0/um/x86/WindowsApp_downlevel.lib
d30da7e21bf1ce8ba9b257a2493be63c  10.0.17134.0/um/x86/dststlog.lib
1b07ab23c4d6ab61875207cb8030905c  10.0.17134.0/um/x86/windowscodecs.lib
a99d8c82fbabfc595bbae1aa84e863c6  10.0.17134.0/um/x64/mincore.lib
9c3bb81fd6cec0ada95d0c664a8b1635  10.0.17134.0/um/x86/windowssideshowguids.lib
596f83d646bf65f92d952923d22d012d  10.0.17134.0/um/x64/mi.lib
2bbcab930c443ac47d544c4f707e53ad  10.0.17134.0/um/x86/dssec.lib
6830b3af7c58c272ac22882b34b9f1ed  10.0.17134.0/um/x86/winfax.lib
4e5dc7b4c6f0a741cac14208ea70bb49  10.0.17134.0/um/x86/winhttp.lib
087f160b1e7eead20b9830c5837f86e6  10.0.17134.0/um/x64/MgmtAPI.Lib
db88c81835e08837b083b954c061f389  10.0.17134.0/um/x86/WinInet.Lib
3d4d9f56fb444eb2772038f21bb4fe14  10.0.17134.0/um/x86/winml.lib
0bb3b605d07ee103354679d98a8cb82b  10.0.17134.0/um/x86/WinMM.Lib
668148741aaf4d08634e7f62e243fbb5  10.0.17134.0/um/x86/winsatapi.lib
8c7a1fd08f8a576a7222eb59a0e6b850  10.0.17134.0/um/x86/winscard.lib
9ca4c01f471a156be83af03ee3634aba  10.0.17134.0/um/x64/Mfsrcsnk.lib
c1596deabd53a7c6ebac60b2526b1c0f  10.0.17134.0/um/x86/WinSpool.Lib
2a0bbce7dd38ab0967ae5af1e1597f67  10.0.17134.0/um/x86/winsqlite3.lib
2b962bbe343c73e4e6e684c362daee67  10.0.17134.0/um/x86/dsound.lib
cf4b7ecbeaa4764f8f19846c55db1f01  10.0.17134.0/um/x64/mfsensorgroup.lib
326df6ed7836eb90e3afbb402bcc825e  10.0.17134.0/um/x86/drttransport.lib
633f05c9240da5be37071262872ef895  10.0.17134.0/um/x86/winsta.lib
4f652e6e74c4e21d2e7161c2243bf4d6  10.0.17134.0/um/x86/WinStrm.Lib
e2662f1638d40d09c298cfce47b85f7c  10.0.17134.0/um/x86/drt.lib
4f147ade4f52f659ad0fcdcd369c8598  10.0.17134.0/um/x86/WinTrust.Lib
c8422d6c44ca20a35924241b6799d558  10.0.17134.0/um/x64/mfreadwrite.lib
d01de3cfcff11b777e080de5ef6c366a  10.0.17134.0/um/x64/mfplay.lib
8b3a0038064e57f73df29f88b886ebf6  10.0.17134.0/um/x86/dpx.lib
bb49a27b59366e244cbf049c32f3f2be  10.0.17134.0/um/x86/dnsrslvr.lib
df78cf0c20c1ae01c6ebbda94c6c9778  10.0.17134.0/um/x86/winusb.lib
1860f1b3781e4dec92268489d1226c8d  10.0.17134.0/um/x86/dnsrpc.lib
e40ecc82984d49349688dddd2d0fc29e  10.0.17134.0/um/x86/wlanapi.lib
9b8d15ceb297a52c13c0c9033a0c55b7  10.0.17134.0/um/x86/dnsperf.lib
10ca4da96bbb97042627d286680b8fd9  10.0.17134.0/um/x86/wlanui.lib
b58f5f1e294a2e4fd06a0724055ee6b5  10.0.17134.0/um/x86/Wldap32.Lib
aec491d1c8f6992e854573cd3c0a69c8  10.0.17134.0/um/x86/Wldp.Lib
0536758695c9df3fc022d17f169c9593  10.0.17134.0/um/x86/dnslib.lib
cfe27e6addfc0da6b11cb28e5b60e155  10.0.17134.0/um/x86/wmcodecdspuuid.lib
ddb00824c016f6027a29e3655b5bb158  10.0.17134.0/um/x86/wmip.lib
8f262e7974a132db44357a40c2ad13ad  10.0.17134.0/um/x86/wmiutils.lib
63fb10acd7bd86e0a597fbc569634588  10.0.17134.0/um/x64/mdmlocalmanagement.lib
4a39d666774facd03a16c1749612c37e  10.0.17134.0/um/x86/dnscrcli.lib
19c43b296cd1638d1cd32523173fdaad  10.0.17134.0/um/x86/wmvcore.lib
b6019faad899ad3e626e2fa303b60bf1  10.0.17134.0/um/x64/mciole32.lib
8b267b02d48fd22acf312b46c740a9af  10.0.17134.0/um/x86/wofutil.lib
7165019b26daf2e756edf69c4c3901e6  10.0.17134.0/um/x86/workspaceax.lib
6523f96afc6c256e695fccc0ac0c2a4c  10.0.17134.0/um/x64/mbnapi_uuid.lib
1917e9baf82eef5d82d5848c3ea472e2  10.0.17134.0/um/x86/dmprocessxmlfiltered.lib
201474bd9cf99eda639c6336f6dd5da3  10.0.17134.0/um/x86/Wow32.Lib
f2b3175cfbab048929c9ac1eeef43871  10.0.17134.0/um/x86/WS2_32.Lib
1230914754b824d04983b2294b4ae8f6  10.0.17134.0/um/x86/wsbapp_uuid.Lib
25019dfbfe962bbbdfefe20a6bd8e995  10.0.17134.0/um/x86/wsbonline.lib
3d03bb4ced36b63dc258baaa3e0ba6b7  10.0.17134.0/um/x64/magnification.lib
35cdd12b5498e0ffc75d454f33864aab  10.0.17134.0/um/x86/wscapi.lib
fda7b05d2b18f138a342d39566597b51  10.0.17134.0/um/x86/wsclient.lib
c4bc319857eb3c4b5021153fa2549c97  10.0.17134.0/um/x86/wsdapi.lib
834e08e9e0e2be2bdbf588efcdf4789b  10.0.17134.0/um/x86/dinput8.lib
cc0ea2747a5b0a7c3ee7443971fa7947  10.0.17134.0/um/x86/dhcpsapi.lib
43eb7d367b7cc8bef29a0c0062c00586  10.0.17134.0/um/x86/DhcpCSvc6.Lib
8c483832cb8d4e0296ebd85a3aab7150  10.0.17134.0/um/x86/dflayout.lib
a44b37c073685c058f004be6e2cd0067  10.0.17134.0/um/x86/wsmsvc.lib
f8780c80cfa70659728927db70641f9d  10.0.17134.0/um/x86/WSnmp32.Lib
9153d1467b4cd4e57c2c978396ee5aef  10.0.17134.0/um/x86/deviceaccess.lib
ab245b4491a60d335a272a30091b990a  10.0.17134.0/um/x86/WSock32.Lib
1288f935d0ec95b4b73a243d026361ab  10.0.17134.0/um/x86/wuguid.lib
e1af235172b112fa32e69b70aeb3abb7  10.0.17134.0/um/x86/ddraw.lib
95c2d419bbd6ddd2503f0c56f60d5d26  10.0.17134.0/um/x86/WtsApi32.Lib
4b3ce86c04e385e59613661a248e544c  10.0.17134.0/um/x86/xapobase.lib
ba1c10bec6a65dfd1a29f14a75acd8c7  10.0.17134.0/um/x64/LoadPerf.Lib
9e727945a430603e3d92fc5edd446c09  10.0.17134.0/um/x86/dciman32.lib
b6a89438c749c2d5034e2a65fee7ebaa  10.0.17134.0/um/x86/DbgModel.Lib
617f900c6ecbcfe024deee156b6fc66b  10.0.17134.0/um/x64/KSProxy.Lib
cd641add51de56ccfdb75a032aa471ac  10.0.17134.0/um/x86/d3dcsxd.lib
a35deba900c44eb12b933e1d726e6f4c  10.0.17134.0/um/x64/kernel32.Lib
fc62f93cc519a478f8acd8d73b983c86  10.0.17134.0/um/x86/d3dcsx.lib
d36f85060a1edc25b0dbafa6a464cc28  10.0.17134.0/um/x64/kerbcli.lib
83210a3715f1b90aeb5fdea80fd5f220  10.0.17134.0/um/x86/d3d12.lib
086c98032b4a88ddeba7e0d35fa882c4  10.0.17134.0/um/x86/d3d11.lib
b8c62a3544a1fc67cb22f62b5865c2c3  10.0.17134.0/um/x86/d3d10_1.lib
b68612775381c9200dc2d38067a10d60  10.0.17134.0/um/x86/cscdll.lib
e5dbe4508ddc1505f8707bde2ad0ac98  10.0.17134.0/um/x64/irprops.lib
a5cf3fa22de1a2e28ab786dcd7e62348  10.0.17134.0/um/x64/jsrt.lib
384292926d32f47502a0d0b6a3623753  10.0.17134.0/um/x64/inseng.lib
43a9ca84895fd9476d3d3230b843b25e  10.0.17134.0/um/x64/inkobjcore.lib
fbf01f40dd5f7d8cfe2616d379e4a3ae  10.0.17134.0/um/x64/imgutil.Lib
c56b93d702cef7aa93fd7bb58c50bf1c  10.0.17134.0/um/x86/Crypt32.Lib
56831edb4afb0ca049bbf018d796e49c  10.0.17134.0/um/x64/ImageHlp.Lib
c1981a82de82f27c0c92a1864b763c98  10.0.17134.0/um/x86/Credui.lib
05d7a864a371fc966e394b2dd0a969d9  10.0.17134.0/um/x64/iesetup.lib
f4c835d8f581ab0603eae73ccd9e3a00  10.0.17134.0/um/x64/IEPMAPI.Lib
d0fb0b477b2194fbd82f0954ca7336a9  10.0.17134.0/um/x86/ComSvcs.Lib
f11d5a2f0ea4df6a7ace5957971d1aa7  10.0.17134.0/um/x64/icuin.Lib
09a315110b2fd4ee74954b40b3288126  10.0.17134.0/um/x86/compstui.lib
ab0b976b3ebab551d964058a7953e786  10.0.17134.0/um/x86/CompPkgSup.lib
179ce683a2a85a840ae4c26019bc43b0  10.0.17134.0/um/x64/Icmui.Lib
e4063058f35f4dd6a7cf14ed82d15761  10.0.17134.0/um/x86/ComDlg32.Lib
7a794e1011d170adc3fc7409580e5e2e  10.0.17134.0/um/x64/Icm32.Lib
1b8075c0bf6d0f0367a1ccbd35df3e78  10.0.17134.0/um/x64/iashlpr.lib
c866f6b6d25c83e14cc08568c735d6ae  10.0.17134.0/um/x64/hid.lib
921593beda1ed336eb00a5c482f73bfd  10.0.17134.0/um/x64/feclient.lib
9c713368dc560743f1340e906e537c21  10.0.17134.0/um/x86/cldapi.lib
5cbf44f960b945f62a7dbc2a7f5b2ca4  10.0.17134.0/um/x64/FaultRep.Lib
8ff5374e9fe64e3a1d74ecb086d4f96d  10.0.17134.0/um/x86/Chakrart.lib
048af3955f8faae323fa74bdecfdce26  10.0.17134.0/um/x64/esent.lib
ff7cc63d5a29dd88b80a7f13f5e1c4d5  10.0.17134.0/um/x64/ElsCore.lib
3f0610ed57641fd556313c8764cc2928  10.0.17134.0/um/x64/els.lib
e0a56257b3e0d4b4f9b415fcffe74843  10.0.17134.0/um/x64/ehstorguids.lib
d2702a46154aca1bd0fa48a39e9e8aa9  10.0.17134.0/um/x64/eappprxy.lib
1bd4d225c134b0cfd523e9901424d4a2  10.0.17134.0/um/x64/dxva2.lib
dfb9151f3489ebb6deeb3aa310e8553d  10.0.17134.0/um/x64/dxtrans.lib
b44f8225d5a5c912604e469df7992093  10.0.17134.0/um/x86/cfgmgr32.lib
5710132a0ad8c3dee0370ba0a84e3d21  10.0.17134.0/um/x64/dxtmsft.lib
1f5e2051cb91f82f8daf64e72be405cc  10.0.17134.0/um/x64/dxguid.lib
fe148df7501c6ed870f601377880fd84  10.0.17134.0/um/x64/vscmgr.lib
f188bef25369c41865353cf632c84f55  10.0.17134.0/um/x64/vssapi.lib
d8c6603559d64b7240196607ac4fc54a  10.0.17134.0/um/x64/vss_uuid.lib
8738f90c6290a2d858e7e80f63b76465  10.0.17134.0/um/x64/vstorinterface.lib
366b6d42750c346817634e1954dbe5f2  10.0.17134.0/um/x64/dxgi.lib
521202013536674b9176ad8cf218d0f7  10.0.17134.0/um/x64/wbemuuid.lib
59200f221af9f06c6f25d61fa8c08569  10.0.17134.0/um/x64/wcmapi.lib
3c7b45bffdb1864fa7ab237d069f82c3  10.0.17134.0/um/x64/dssec.lib
b790663cfeab3fccd922b8850f77d802  10.0.17134.0/um/x86/bthprops.lib
9047bb452e91a1da6b8aa5081b4bb79e  10.0.17134.0/um/x64/wcmguid.lib
7b8053adde557b6fcb663d93e3e73468  10.0.17134.0/um/x86/BluetoothApis.lib
0760db56939ce573c5ea7ad15da121d4  10.0.17134.0/um/x64/wdsbp.lib
61bc28b107bbac35ce9b06df4d725c48  10.0.17134.0/um/x64/wdsClientAPI.LIB
6210d7b1b8e5b4064cc81ef0efc2a7dc  10.0.17134.0/um/x64/wdsmc.lib
4ce53e4a8a5ec10025f58e3304c0ac88  10.0.17134.0/um/x64/wdspxe.lib
ed9808c4d19f475f811c5c60f3bad5f7  10.0.17134.0/um/x64/wdstptc.lib
26ab3e81179515c501d2fc2fb9a3a6dc  10.0.17134.0/um/x64/WebServices.lib
cbbc93047afe5a3c83257904248f5cb2  10.0.17134.0/um/x64/websocket.lib
15c9ac175d92e4a4d4a3ba2ecbac4911  10.0.17134.0/um/x64/dsound.lib
86aed25625f81088dcb1872e3e4ea2e0  10.0.17134.0/um/x64/wecapi.lib
c6de3bc29703cb589b3417ff32c4332e  10.0.17134.0/um/x64/wevtapi.lib
56349b9c2e8c1b4883e188d42567ecd0  10.0.17134.0/um/x64/Wer.lib
4951309a020fa56c7fbb02a67ba6dfef  10.0.17134.0/um/x64/WiaGuid.Lib
53ef6d3070310c6719e8b1234663c403  10.0.17134.0/um/x64/wiaservc.lib
8084d0fb1b4e74880f11a60e4d07915b  10.0.17134.0/um/x64/wiautil.lib
99d93eb4ed6a2232750e0a039d46450f  10.0.17134.0/um/x86/xapobase2_8.lib
add243d66900ffd53b1a7d955394b447  10.0.17134.0/um/x64/WinBio.lib
a8a03674e2504944a1b154534333f615  10.0.17134.0/um/x86/xaswitch.lib
77789c58f7bbad70901afa07c4f67390  10.0.17134.0/um/x64/windows.data.pdf.lib
a9e293f996400f85165ddf6e4e207a47  10.0.17134.0/um/x86/xaudio2.lib
b9f4f982e140df139c34beb13be43386  10.0.17134.0/um/x64/windows.networking.lib
9db69179d910f28aa27574e93ed1fb11  10.0.17134.0/um/x86/xaudio2_8.lib
09b81ba7ffd8cfbc94dfca813abb6699  10.0.17134.0/um/x86/xinput.lib
57380861b1951537c547cf33a63126e6  10.0.17134.0/um/x64/windows.ui.lib
74dc55e3a86a8f78ee0256baa5a46a48  10.0.17134.0/um/x86/Xinput9_1_0.lib
3add92067c204062cc5f23e687f40c40  10.0.17134.0/um/x86/xinputuap.lib
b8f053b560ba36806ebe2e70ad26af4a  10.0.17134.0/um/x86/xmllite.lib
d8105cd4bfeed0e54c0124022bacd8c5  10.0.17134.0/um/x86/xolehlp.lib
327a70babe97743e934bc00b6699c7fc  10.0.17134.0/um/x64/WindowsApp.lib
682c062b1bf9298f8f73885e2f7070fc  10.0.17134.0/um/x64/drt.lib
bc72bed777a3e07f2a7c6b4e17c6ef4a  10.0.17134.0/um/x86/avrt.lib
0b300366d427c628419e5bcd8aeaf47e  10.0.17134.0/um/x64/dpx.lib
f578e2747d0d50aa37fde4c41503cec4  10.0.17134.0/um/x86/avifil32.Lib
1aacf6cb94542b8ac77880a5b508d5ac  10.0.17134.0/um/x86/aux_ulib.lib
ba25ddf0220adb9e41dd178875714eaa  10.0.17134.0/um/x86/AuthZ.Lib
dc469a18851de29001d2546014637809  10.0.17134.0/um/x64/dnscrcli.lib
85bc6e0b5bc98709f6e7b5e06358d2a1  10.0.17134.0/um/x86/audioeng.lib
38fd9e797444e2575f922c588228622d  10.0.17134.0/um/x64/dmprocessxmlfiltered.lib
f68d639620531185d8c8981316e75006  10.0.17134.0/um/x64/dmoguids.lib
ee6bf44a5d37421750bcc570c4345cd2  10.0.17134.0/um/x86/audiobaseprocessingobject.lib
09019e239123ecfcace9ececf76e8df4  10.0.17134.0/um/x64/difxapi.lib
4f1ac3ca1412022327ff0e2b291893d5  10.0.17134.0/um/x86/ASycFilt.Lib
28518c07023a0905b7466280ca74f95d  10.0.17134.0/um/x86/appnotify.lib
c81613cc66704377eadd273f81ff9302  10.0.17134.0/um/x64/DhcpCSvc6.Lib
2dea0c0960cf6d9c5b4ca0b2d25e2564  10.0.17134.0/um/x86/appmgr.lib
8268daa77732e165e0732daa31c0d909  10.0.17134.0/um/x64/DhcpCSvc.Lib
7e2351f68b78e8459b930f588a3b4d2d  10.0.17134.0/um/x64/dflayout.lib
ff2825debe600ba3690556d8cf2da104  10.0.17134.0/um/x86/appmgmts.lib
46a2c20d729e1ad4b84ffa3d176facea  10.0.17134.0/um/x64/devmgr.lib
2ad4dfdf25baca11b5f3c7252db41c56  10.0.17134.0/um/x86/apidll.lib
b11fa81993db36e17de3fc5fa26a756e  10.0.17134.0/um/x86/xpsdocumenttargetprint.lib
4e294d590deaec522910ec114efd2e13  10.0.17134.0/um/x86/xpsprint.lib
76ae8e26b37d403a5e1ce7afa5592cf4  10.0.17134.0/um/x86/amstrmid.lib
8013b6f84e9c6783e316a69c7413f63b  10.0.17134.0/um/x64/devenum.lib
b597dc18543149a3295b9f674113d378  10.0.17134.0/um/x86/amsi.lib
5008d5c8d427ce51e4b3c220d9d62710  10.0.17134.0/um/x86/ahadmin.lib
6311611dfef3741dbd244c99c09c43d0  10.0.17134.0/um/x64/dcomp.lib
3d8e94695d6d92cc4dd93ff34b31a755  10.0.17134.0/um/x64/d2d1.lib
e287de13c875a00aa6f6dece9101cb61  10.0.17134.0/um/x64/cscdll.lib
cd3fe142b88b28880130735018b71540  10.0.17134.0/um/x64/cscapi.lib
c13fbfb3abe27a8134031c1d5eb9afa1  10.0.17134.0/um/x64/cryptxml.lib
6068d06726e0d3c3a83d564fe8247726  10.0.17134.0/um/x64/cryptui.lib
6d798bc7d0897431d6cb366a032e3778  10.0.17134.0/um/x64/CryptNet.Lib
5f5d82c7480fce9979a91d4c27b37f33  10.0.17134.0/um/x86/ADSIid.Lib
97ebc837c87f24eeeb5cb82263cf7f84  10.0.17134.0/um/x86/ActiveDS.Lib
c888d1200334ef4c9c7d9ffa2f7f3ac1  10.0.17134.0/um/x64/Credui.lib
a405273fb3be0fcbfd9b1e7710cefc55  10.0.17134.0/um/x64/WindowsApp_downlevel.lib
16417acc7a1b7072afc31fe494be58db  10.0.17134.0/um/x64/corrEngine.lib
e3881aa2470f2278678fdba3e9db368b  10.0.17134.0/um/x64/windowscodecs.lib
096c52b3ca5a9815573152a71909ff99  10.0.17134.0/um/x64/windowssideshowguids.lib
25e718344fce88b3b14d13616a22bba2  10.0.17134.0/um/x64/winfax.lib
8da76971d03a292f28a242f86793f2a0  10.0.17134.0/um/x64/winhttp.lib
115d28bc1bb3f5ef9af56697e5ff8f23  10.0.17134.0/um/x64/WinHvEmulation.lib
1b781705b02d0ee938a8ad1471e8abb8  10.0.17134.0/um/x64/WinHvPlatform.lib
ba3b62df2dadcd8acb9a4e801beb188d  10.0.17134.0/um/x64/WinInet.Lib
18c9b53552a58668ee48ea2eeacd93d8  10.0.17134.0/um/x64/winml.lib
4a85bd5b8bf559aaf8c63162b4363fcb  10.0.17134.0/um/x64/WinMM.Lib
f18cd3e21f99d7e9b0cc55cf77169995  10.0.17134.0/um/x64/winsatapi.lib
40a3c7e7aebec63f55949df305e2ee99  10.0.17134.0/um/x64/winscard.lib
6a4669064aaa4c082e0f4632a9518bec  10.0.17134.0/um/x64/winsqlite3.lib
f3f8fcd635e849456ab0aaaaa0918d24  10.0.17134.0/um/x64/winsta.lib
68662957c46c668da0173b465573bafb  10.0.17134.0/um/x64/WinTrust.Lib
59519b8b7b666c84d2d2112e1359462a  10.0.17134.0/um/x64/WinStrm.Lib
ba3b7ce34ff0666c1d2ecac288279256  10.0.17134.0/um/x64/winusb.lib
de56501037407bd3c5c417adbb44390a  10.0.17134.0/um/x64/WinSpool.Lib
6d4224ff055c2778fa8b2957f3ed8153  10.0.17134.0/um/x64/wlanui.lib
7799edc78000dd42f9f8127a46597e23  10.0.17134.0/um/x64/Wldp.Lib
71746c4973c1318dcdda7e3165e89c9d  10.0.17134.0/um/x64/wmcodecdspuuid.lib
a50a769f5824877ec33dccf576cae1ac  10.0.17134.0/um/x64/wmiutils.lib
1944371212af12a2a980b27f35973f9a  10.0.17134.0/um/x64/wmip.lib
d8a6916bfe752acd3e63483e83210028  10.0.17134.0/um/x64/wmvcore.lib
62b706fc7084e7e80af18be69f4b5bb3  10.0.17134.0/um/x64/wnvapi.lib
aa5fe68e70f775b4474ff75ef95f1161  10.0.17134.0/um/x64/wofutil.lib
a13aa87b15e122db8d18fe85a220f71b  10.0.17134.0/um/x64/workspaceax.lib
107caf645f63fd1a613bc4d0ac400517  10.0.17134.0/um/x64/Wldap32.Lib
254acd8b582c3be5b8c9e2214a238102  10.0.17134.0/um/x64/wlanapi.lib
d6237b64832b1a9a1d7526161fbfe3ff  10.0.17134.0/um/x64/WS2_32.Lib
44a6d20757970f661a778c4453119b55  10.0.17134.0/um/x64/wsbapp_uuid.Lib
2250b540962d8fa74caba0e598d7b8c6  10.0.17134.0/um/x64/wsbonline.lib
57aec18e1612448aeb13760a9f5a1ea8  10.0.17134.0/um/x64/wscapi.lib
339c67ce1308e8285d3f50de8b316c6d  10.0.17134.0/um/x64/wsclient.lib
9399706be8d1423675cda550828d4487  10.0.17134.0/um/x64/wsdapi.lib
aac97d95dfc538dd0d95a37ded1e5f53  10.0.17134.0/um/x64/wsmsvc.lib
ebb587bcf9aaaff9d18ab334fcff432d  10.0.17134.0/um/x64/WSnmp32.Lib
e34035249896f41060659166d88b2aa5  10.0.17134.0/um/x64/WSock32.Lib
5335c3a071187bd3725c027550b1edde  10.0.17134.0/um/x64/WtsApi32.Lib
ef897f0e3aa26a7bb6df0caca438b6c1  10.0.17134.0/um/x64/wuguid.lib
c3761918dcf45caafaeb5668384b66b4  10.0.17134.0/um/x64/xapobase.lib
5de9bf5f5a6caea5c77b78f1cb6dda2d  10.0.17134.0/um/x64/xapobase2_8.lib
df1c0fdf0212fbec7c14d2145e4474f5  10.0.17134.0/um/x64/xaswitch.lib
c744b1bcd1c6099d9921ae4aa5464c49  10.0.17134.0/um/x64/xaudio2.lib
8af386a12a08f0ddee291eda0beb2698  10.0.17134.0/um/x64/xaudio2_8.lib
e936f18758a715ee3734f2030de10c83  10.0.17134.0/um/x64/xmllite.lib
6f2fcd4e4b8bac50ebb22c184a27e8a1  10.0.17134.0/um/x64/xolehlp.lib
faa90e9163e0dc8d6a63564bb7938b24  10.0.17134.0/um/x64/xpsdocumenttargetprint.lib
23df65074c1ee78b86917e9e47d91f28  10.0.17134.0/um/x64/xpsprint.lib
b2be2ee07d989041f7350fe217c4df61  10.0.17134.0/um/x64/xinputuap.lib
a2580849ec470cb7f33c2e91f5eac567  10.0.17134.0/um/x64/Xinput9_1_0.lib
00960dc55757c03f9c85a74029bcc568  10.0.17134.0/um/x64/xinput.lib
```

### ucrt: 10.0.17763.0

```
8e3d12cfc36f53ac5cbc713b6a0bac2c  10.0.17763.0/ucrt/x86/ucrtd.lib
51171c76b1c50e38049067d0d7d27d36  10.0.17763.0/ucrt/x86/ucrt.lib
b3b38cb22c107ca63226d1e1477c64a0  10.0.17763.0/ucrt/x86/libucrtd.lib
05ba0189753fa35d76e8f0349e4ba994  10.0.17763.0/ucrt/x86/libucrt.lib
2ab205783b0a9b34df46446fd76e2030  10.0.17763.0/um/x86/Mfsrcsnk.lib
be65ab19590b9b03cfd5aceba1804a41  10.0.17763.0/um/x86/MSAJApi.lib
5de90f77b29bb9d173f82b8ef9f35ac4  10.0.17763.0/um/x86/msports.lib
d385710fe44c0487241c44604d4ccb0e  10.0.17763.0/um/x86/MSRating.Lib
84afdf7928b4fdc3d002929debae5bdb  10.0.17763.0/um/x86/msxml6.lib
aeba4bc9146abac1adb62bb629c1a390  10.0.17763.0/um/x86/Mtx.Lib
89d3614dc608fcdaa28fb3eb7a81ccc7  10.0.17763.0/um/x86/muiload.lib
95a80ed4908ea471ab0c65c03ed70c9d  10.0.17763.0/um/x86/nddeapi.lib
a4e52557294d84798ef9e8b5bdad333d  10.0.17763.0/um/x86/ndfapi.lib
87c4f5a39f71b8c1000c354e6ff923b7  10.0.17763.0/um/x86/ncrypt.lib
017bbfb70b7460298bac574d172a94e0  10.0.17763.0/um/x86/ndproxystub.lib
11e246143ef0392d39a7c0d5a9962150  10.0.17763.0/um/x86/NetAPI32.Lib
3af88499e735c0a2ad3abb95b6e2a39d  10.0.17763.0/um/x86/NetSh.Lib
c09b47fefd95faf9a3e2b24151f366f5  10.0.17763.0/um/x86/normaliz.lib
e5c548fc4753d0d057439b6829a4976e  10.0.17763.0/um/x86/newdev.lib
9ec3423e9553c5f0faac6984ae26fb38  10.0.17763.0/um/x86/nt.lib
69883bc6a067c6eb24bb76eaca5a0c72  10.0.17763.0/um/x86/ntdll.lib
a944da8a438a9343499f35daa7819ce4  10.0.17763.0/um/x86/ntdsa.lib
3269821fbaa671ee6bab3d146d3c9db3  10.0.17763.0/um/x86/NtDsAPI.Lib
b64e2ebcf2696c4de085e580b9d0df7d  10.0.17763.0/um/x86/ntdsatq.lib
7126fcbc212a5faee773cbff96bbc663  10.0.17763.0/um/x86/ntdsetup.lib
7c3eba4e68251a56a7dbc51f644427ad  10.0.17763.0/um/x86/ntfrsapi.lib
4d7992ca74824626b4aaa57e0011dc99  10.0.17763.0/um/x86/ntlanman.lib
08f5b6cb6cf37dc4a7ee4a96b0296855  10.0.17763.0/um/x86/ntmarta.lib
785ca3523030042fdac1ec144f9eb447  10.0.17763.0/um/x86/NtQuery.Lib
543c79b394740f3f558ff5854ade5a1b  10.0.17763.0/um/x86/ntstc_libcmt.lib
afb523316ed6ea64a00e04c96909c5d0  10.0.17763.0/um/x86/ninput.lib
18122c987780f11174eed13153f8226a  10.0.17763.0/um/x86/netlib.lib
a7f3c9c529cad86e05559d1b754c061d  10.0.17763.0/um/x86/mtxdm.lib
b3ccf45a42a2f9705a37610e71490ea3  10.0.17763.0/um/x86/MsXml2.Lib
778ec34d3f5ce7d16f25b3b6825639d7  10.0.17763.0/um/x86/msvfw32.Lib
69441af6b3c80a7c053e690c5e4928f5  10.0.17763.0/um/x86/MsWSock.Lib
91f63076c844b4f585ba6564af509704  10.0.17763.0/um/x86/msv1_0.lib
2e394fc3c2b5c19bd9d1423f1ad887b1  10.0.17763.0/um/x86/MSTask.Lib
7b011010f13d47671d95624ab0a9a00b  10.0.17763.0/um/x86/mspbase.lib
e7f8196bd18c2b627ac294da59fd4dc6  10.0.17763.0/um/x86/mspatchc.lib
59af155f0424b5fab5a9188db65872d2  10.0.17763.0/um/x86/mspatcha.lib
e27455b00231b6e5026f899f12100467  10.0.17763.0/um/x86/MSImg32.Lib
ebd6e0eeab3fbb65c44915e9837a765a  10.0.17763.0/um/x86/Msi.Lib
b4452c44e64fbe2e054f0b874cec8a91  10.0.17763.0/um/x86/msdrm.lib
0ae566d844b6da6e2f9b71b43036eea7  10.0.17763.0/um/x86/msdmo.lib
32faa7521945910b4eb6544f344f26eb  10.0.17763.0/um/x86/msdelta.lib
1055954f48da435ca00ffbc25b76c5fe  10.0.17763.0/um/x86/msdasc.lib
0d1348d8ad8f3d88aaa240be09857ff7  10.0.17763.0/um/x86/MsCtfMonitor.lib
8b77ddf233796858c2d3104d0eb182cb  10.0.17763.0/um/x86/ntstc_msvcrt.lib
28d37f137a308eb36607d0af0f2b31dc  10.0.17763.0/um/x86/ntvdm.lib
282feda6e279d82584026415e6ea6c86  10.0.17763.0/um/x86/objsel.lib
3d100a3a888d5f38b1ab1c2eb33717fe  10.0.17763.0/um/x86/odbcbcp.lib
c6fde9fcf6782371ebb681dce69ed5d7  10.0.17763.0/um/x86/odbccp32.lib
c1f26a69fdf6fd7d8101e9231d182bae  10.0.17763.0/um/x86/OemLicense.lib
2651d8ce2ff21504dd78e8836d82e360  10.0.17763.0/um/x86/OleAut32.Lib
34c70d7c6ed3d1ef53addca8c1f19464  10.0.17763.0/um/x86/OleAcc.Lib
2d56b4962a7498e8917e0cb85de4668e  10.0.17763.0/um/x86/Ole32.Lib
c786005237c00d28a912f37e379e35de  10.0.17763.0/um/x86/olecli32.lib
a3cd207083c425d58bf064262c504256  10.0.17763.0/um/x86/oledb.lib
6624b55fd9492546a5c1ac2a2262aea3  10.0.17763.0/um/x86/OlePro32.Lib
1086008ddbe24b82d2b731bab8fdaed6  10.0.17763.0/um/x86/OleDlg.Lib
5c97ed29b445db5a6c61d1a7b9f64317  10.0.17763.0/um/x86/ondemandconnroutehelper.lib
49f85c6913541696bc10facc7bfd6129  10.0.17763.0/um/x86/olesvr32.lib
f18252feac2a7280ac773f8ec5253907  10.0.17763.0/um/x86/OneCore.Lib
325480d44ec9a5a7bca3a1471b490af6  10.0.17763.0/um/x86/OneCoreUAP_apiset.Lib
ea494824637714961655bd5ac5ed3bc0  10.0.17763.0/um/x86/OneCoreUAP.Lib
e80c3aa1a16cb8150bac7eaec3233bd3  10.0.17763.0/um/x86/OneCoreUAP_downlevel.Lib
91aa80708774618c95a83cddec7e9fa9  10.0.17763.0/um/x86/odbc32.lib
978003a8937ce93ded21b3d1d6b0ad92  10.0.17763.0/um/x86/Mscms.Lib
a6261ad3e99470d1c01818be6aa8dd93  10.0.17763.0/um/x86/OneCore_apiset.Lib
91695474928f97470329c5f5212fe84d  10.0.17763.0/um/x86/OpenGL32.Lib
7a7fab8718df7115e78ca7595f1e590a  10.0.17763.0/um/x86/osptk.lib
d07307769e8f84c8a8ffad6c927db75e  10.0.17763.0/um/x86/p2p.lib
043e3d2bca5a81b8bd797c9b6a497f6a  10.0.17763.0/um/x86/p2pgraph.lib
4948914d37ec98f9303c3a5feff78120  10.0.17763.0/um/x86/patchwiz.lib
a82c03ff1578e129ca0af7df524274e9  10.0.17763.0/um/x86/pathcch.lib
cf03fc4d80117d39d2dbf5d94303ffbe  10.0.17763.0/um/x86/OneCore_downlevel.Lib
4dab4c37a0b17088e838ca68034320fb  10.0.17763.0/um/x86/Pdh.Lib
c3d61916f175378242528ae502d1f3ba  10.0.17763.0/um/x86/PhotoAcquireUID.lib
f36a91335331f4e6eb8dad7ea42b7f4a  10.0.17763.0/um/x86/PeerDist.lib
fba6d64fbab798bc8a0f2d8e739ac636  10.0.17763.0/um/x86/PortableDeviceGuids.lib
41f79a7054cedf5f9b4b454a7003bcc1  10.0.17763.0/um/x86/powrprof.lib
85573aee14d71bf130fc8df731eb515b  10.0.17763.0/um/x86/prntvpt.lib
113767ce8c3d7a3396dff3651308fb59  10.0.17763.0/um/x86/propsys.lib
230f33faf79d5381c627add3c3e8adce  10.0.17763.0/um/x86/ProjectedFSLib.lib
2714ee61785f272f7dbc2c9e0fad7fda  10.0.17763.0/um/x86/Psapi.Lib
90ab8b4391a64b9a76ae3a1b267ac24f  10.0.17763.0/um/x86/quartz.lib
785ca3523030042fdac1ec144f9eb447  10.0.17763.0/um/x86/query.lib
999a16b85e0158bf6d7dbfbb1e023f92  10.0.17763.0/um/x86/qwave.lib
378faf22210a94c6b912f1dfac9073cd  10.0.17763.0/um/x86/MSAcm32.Lib
44207132ba2d2314db7f78c8ddb4616c  10.0.17763.0/um/x86/msaatext.lib
37242ec6d4875471ce194caecb020142  10.0.17763.0/um/x86/MqRt.Lib
c6d0fb1bd0d5f22b02971c3a54432445  10.0.17763.0/um/x86/MrmSupport.lib
ff96fe1d81b46171c5924a0a4e2a94dc  10.0.17763.0/um/x86/mprsnap.lib
593cc7f75fa20e528fd25b7f29b15027  10.0.17763.0/um/x86/MqOA.Lib
0e777cd3fbe34532ee86b99ff2fbc5c3  10.0.17763.0/um/x86/Mprapi.Lib
c4ab61a8ac0503bd61ae92156054235b  10.0.17763.0/um/x86/Mpr.Lib
ebd2fd57ea4bfe7f7bc51d4108274557  10.0.17763.0/um/x86/mmdevapi.lib
b7b7e671a6f1df75c27ba2da5db11c9a  10.0.17763.0/um/x86/MMC.Lib
119ba0e3acbce9fe86cb6c36c6354fa0  10.0.17763.0/um/x86/mincore_downlevel.lib
856d7ad2d0381884ee2956c1cc22e20c  10.0.17763.0/um/x86/mincore.lib
333bedd481d2bab90275a87c103d71ae  10.0.17763.0/um/x86/mi.lib
7c524872c9ef895f5151e392054b0d22  10.0.17763.0/um/x86/RASAPI32.Lib
2c1ba6567dc6ef53417b3e407d1fbfed  10.0.17763.0/um/x86/RASDlg.Lib
5e6b85dd26c3dea830559d4150485cbe  10.0.17763.0/um/x86/rasuser.lib
2167ac378e172b091a53381dde7c0fe3  10.0.17763.0/um/x86/MgmtAPI.Lib
34e5a41100c67003333c85a8b1ce115d  10.0.17763.0/um/x86/mfuuid.lib
188d00e6960484a0bc5a401184b1b50f  10.0.17763.0/um/x86/resutils.lib
abb6109f6929d13aa77251082cb624c4  10.0.17763.0/um/x86/rometadata.lib
44041e111c073ce143f741598f4b5596  10.0.17763.0/um/x86/mfsensorgroup.lib
b11593ebb99b836f674834e9a3b712da  10.0.17763.0/um/x86/rpcexts.lib
1d0d41c380d63163596448d7c9c502f3  10.0.17763.0/um/x86/Rpcns4.Lib
53da03864a1ade900ca36923c0702856  10.0.17763.0/um/x86/rpcproxy.lib
f5bfef02c5fe32727795496667afcaf8  10.0.17763.0/um/x86/RpcRT4.Lib
c15bcfb6e9b5d309b801d40e252eea8c  10.0.17763.0/um/x86/mfreadwrite.lib
a17eeee6f65d33af022f19273d0dbdb2  10.0.17763.0/um/x86/mfplay.lib
3f5fb464f40c1e70614c726fb095e040  10.0.17763.0/um/x86/Mfplat.lib
2648f528d561ac26a842d52d920c2f80  10.0.17763.0/um/x86/Mfcore.lib
682546a6cbda96e0d6922617260c2094  10.0.17763.0/um/x86/rpcutil.lib
562de71c6a2f68a4e8d70d35d9c8341f  10.0.17763.0/um/x86/Mf.lib
3770348ee7a07f3e0e45d6870544cb40  10.0.17763.0/um/x86/rstrtmgr.lib
9603e799016952ee2b596eaa94b129f9  10.0.17763.0/um/x86/Rtm.Lib
4f4cf5e15df1e183b7864eb01edd0d1e  10.0.17763.0/um/x86/rtutils.lib
692b87bc9159ae49ca4b21faa13a1989  10.0.17763.0/um/x86/MDMRegistration.lib
2857535b231edff7f7ffb1e5eb66f40c  10.0.17763.0/um/x86/RTWorkQ.lib
cd35fa699825f741a1afd4fd4d49c954  10.0.17763.0/um/x86/mdmlocalmanagement.lib
f376658aaa4559833f5a5ac7840153f4  10.0.17763.0/um/x86/runtimeobject.lib
e8354d98978e98826c155d008bf18989  10.0.17763.0/um/x86/samlib.lib
446994cd0517422e2013bec45fe8c32f  10.0.17763.0/um/x86/mciole32.lib
10f80209aee8ebfce93abffffe72b7d9  10.0.17763.0/um/x86/mbnapi_uuid.lib
546028c79818c408ee45226e1de5367b  10.0.17763.0/um/x86/samsrv.lib
07067fd3af65bd8476e91ea8d5582318  10.0.17763.0/um/x86/MAPI32.Lib
8b85db0b60af3cee2dd1b93cf4af8594  10.0.17763.0/um/x86/SAPI.Lib
9b4e79575f8f88f1861e25474586c714  10.0.17763.0/um/x86/magnification.lib
82ff80bb128f56eaf4fb04337370a651  10.0.17763.0/um/x86/locationapi.lib
0b287fd9c756e7c1db5055cbb278bb8a  10.0.17763.0/um/x86/Lz32.Lib
4340ddf1a3fcfe2e79cfd8a832bfac9f  10.0.17763.0/um/x86/sas.lib
4eb479d3f6e40e96cd570efb115dd116  10.0.17763.0/um/x86/LoadPerf.Lib
179ed6588d4a1ae67a5dffe53dc8debd  10.0.17763.0/um/x86/sbtsv.lib
bd7e1eb0e50229ca9365072f3b23159c  10.0.17763.0/um/x86/ktmw32.lib
6a2bacec517ef9c6c585ab9cdc33e5a2  10.0.17763.0/um/x86/ksuser.lib
262d11dc496a5a659a4e015ec4bc8048  10.0.17763.0/um/x86/SCardDlg.Lib
4bb3b313935c4a74b77cfbf239b93aa9  10.0.17763.0/um/x86/KSProxy.Lib
127b1c348d48d3e0e3291179a9eb7ae2  10.0.17763.0/um/x86/keycredmgr.lib
57bf5f2268d1ada386e9d378bca32385  10.0.17763.0/um/x86/scecli.lib
ffd466d1d6ecf5040001b0aa20655ded  10.0.17763.0/um/x86/kernel32legacylib.lib
a1267de08074201e2e0506bb5e184b47  10.0.17763.0/um/x86/scesrv.lib
ed2c5c139bec6f4981702efbd3a9b50d  10.0.17763.0/um/x86/kernel32.Lib
c6e22e4c0095bb0ab94e1b8025f8d1ca  10.0.17763.0/um/x86/kerbcli.lib
d76a8f01625b4d3d70c35f7872aca401  10.0.17763.0/um/x86/schannel.lib
c7de9139435476f869a02043f29a4634  10.0.17763.0/um/x86/ScrnSave.Lib
b9e5500d545f996adf939d1d1c4dda29  10.0.17763.0/um/x86/jsrt.lib
fd00b65c990cf441b13ea4f7fe7450db  10.0.17763.0/um/x86/jetoledb.lib
cc2a7a12d4989db4e087d3ff006d0b00  10.0.17763.0/um/x86/ScrnSavW.Lib
9e84635955dfa96b3f432b5476efa2b9  10.0.17763.0/um/x86/SearchSDK.lib
5a3e375d79176cf448e626a07a2ebcd8  10.0.17763.0/um/x86/iscsidsc.lib
ce6b8e975e8777cf9c1f5d8d3c7af1bc  10.0.17763.0/um/x86/Secur32.Lib
f806720f00d86351a78e1dd1440b536e  10.0.17763.0/um/x86/security.lib
33616986519cc6b888a9c7ff251c124e  10.0.17763.0/um/x86/irprops.lib
e6eac33bbc9371adf376351ab2d6a9e7  10.0.17763.0/um/x86/sens.lib
aff5d1cf7d0ed225e1f69762fdba7ec9  10.0.17763.0/um/x86/Iprop.Lib
12bbc07792ee1add470558770e4ba9df  10.0.17763.0/um/x86/SensAPI.Lib
aa8baa90fc4504905bd4a89b64777f9c  10.0.17763.0/um/x86/iphlpapi.lib
13a1bc04f0fcb8e3f1ceb742a63388a4  10.0.17763.0/um/x86/int64.lib
dd02fe855a2881d7d75e433cdd0fbf1b  10.0.17763.0/um/x86/sensorsapi.lib
9185ebd8372909727553e350bf3032c8  10.0.17763.0/um/x86/SensorsUtils.lib
ba24f73a0a20ab79754f38cbce3f807a  10.0.17763.0/um/x86/inseng.lib
8abda2c58d5156aa5378e97052919267  10.0.17763.0/um/x86/inkobjcore.lib
b105c6a17f36d8c38c87c3f10c8a34c1  10.0.17763.0/um/x86/SetupAPI.Lib
a88e25dec95d5f318097e496e7b16c1a  10.0.17763.0/um/x86/Sfc.Lib
fb7d9eee6f4d1f4e3655ea89660310c2  10.0.17763.0/um/x86/shcore.lib
d66360b034534bca06fc4159472ae2fa  10.0.17763.0/um/x86/infocardapi.Lib
d2c2aaf03582a332a8c282293bde7099  10.0.17763.0/um/x86/shdocvw.lib
53f547a7370db08233249e1a5540b4ca  10.0.17763.0/um/x86/shell32.lib
6b36c3bee018967648085e6e37bee5a0  10.0.17763.0/um/x86/ShFolder.Lib
c83df8fd7a6c5a5450a431fbc19c5af4  10.0.17763.0/um/x86/ShLwApi.Lib
f82c607ea3e32e8a7d4044f66dfef3a6  10.0.17763.0/um/x86/Imm32.Lib
80dd712165b9ae7e2adc6440a56ae9f2  10.0.17763.0/um/x86/slc.lib
f7808ac7f3f8bf28c29119ddaf5b5488  10.0.17763.0/um/x86/imgutil.Lib
21cf705d302f2cf6419f1f4d49afd381  10.0.17763.0/um/x86/slcext.lib
a56530b407f8da9544c466a8a0fb9000  10.0.17763.0/um/x86/ImageHlp.Lib
c1426f0ccecab91c5e73d1d982974dd3  10.0.17763.0/um/x86/slwga.lib
1965c75f7ea13052f3bf9cbf7f76fac5  10.0.17763.0/um/x86/iesetup.lib
3598315b0ec9069fa871b2679258b8c3  10.0.17763.0/um/x86/SnmpAPI.Lib
37db4051d8193e81c0f9cbd5ec261df6  10.0.17763.0/um/x86/IEPMAPI.Lib
7ddd236f222f0a44eb7d5c5b56d93825  10.0.17763.0/um/x86/icuuc.lib
0c5d07b3371d18b38728f658fb0dc5bc  10.0.17763.0/um/x86/spoolss.lib
48475b4e0f86bbb161b2e93955794731  10.0.17763.0/um/x86/SpOrder.Lib
b457e7ae5d247012870e5346b29e29b2  10.0.17763.0/um/x86/icuin.Lib
a256ef8b3dcfbfff415e00847ffad23c  10.0.17763.0/um/x86/SrClient.lib
c0d21358695df53e0fbd3c7de4044a0b  10.0.17763.0/um/x86/srpapi.lib
0bc863a7eb9768308a1e1eb51393d727  10.0.17763.0/um/x86/Icmui.Lib
b890d2d004b76474054fe276d782d002  10.0.17763.0/um/x86/ssdpapi.lib
d6e9651b7498f722b003a7908dcb76c0  10.0.17763.0/um/x86/Icm32.Lib
3fa84b55535bc2f823375654f1af74ca  10.0.17763.0/um/x86/Sti.Lib
1f9f3c15855ccd8dacf1c8c98cbcb02f  10.0.17763.0/um/x86/iashlpr.lib
7b466830746de36dd6857caa53e5460f  10.0.17763.0/um/x86/strmbase.lib
c2df2c0c5a854abdaf9e30d43e681d20  10.0.17763.0/um/x86/httpapi.lib
ec6375700e62622a76ec33cbe9314088  10.0.17763.0/um/x86/strmiids.lib
8e694e73f212604c304835631ff24c4a  10.0.17763.0/um/x86/strsafe.lib
a6d889bf96874d42d3b13d5ab9bc9dd9  10.0.17763.0/um/x86/Htmlhelp.Lib
65fd792672e99f38a5f7e5ee4c8ae757  10.0.17763.0/um/x86/hrtfapo.lib
c0abe80fad3195c7cb159f5cc85c8c4b  10.0.17763.0/um/x86/HLink.Lib
8f7015df726dad6651b4ffc985c8c04d  10.0.17763.0/um/x86/hid.lib
7b2fd1ad3257a1a039a2ea27be797fc8  10.0.17763.0/um/x86/hhsetup.lib
f8ddb90990ce6665b00f9365098c569f  10.0.17763.0/um/x86/hbaapi.lib
83a05309a73dd35c48f897497fbbdec2  10.0.17763.0/um/x86/gpmuuid.lib
7f8bbc5d621b01bccf73b7b154d5cd2d  10.0.17763.0/um/x86/GPEdit.lib
1769b9d765660c20fb196d05c8493160  10.0.17763.0/um/x86/GlU32.Lib
1693dab5bed76a02b199684c9cbbacab  10.0.17763.0/um/x86/structuredquery.lib
7a0d2d51af60c32091ffdee8b4cda2a8  10.0.17763.0/um/x86/Svcguid.Lib
7c302cd09570e4e45d101ffed2af5466  10.0.17763.0/um/x86/synchronization.lib
e4647e6409b2cc56d69ce4c5cb31a820  10.0.17763.0/um/x86/t2embed.lib
34d681dec589e9e9884231ccc0d85434  10.0.17763.0/um/x86/Tapi32.Lib
d6b36944e80eee2d4d9287503618ed10  10.0.17763.0/um/x86/taskschd.lib
0a480aa61db933d69cba1b3876c78d48  10.0.17763.0/um/x86/Thunk32.Lib
ce9842a389e0ad9020508887ddcc7dcf  10.0.17763.0/um/x86/tokenbinding.lib
56c34b5b76caaebae77533838304f4c9  10.0.17763.0/um/x86/Traffic.Lib
edb01442a415ae283c06c23d74887e0f  10.0.17763.0/um/x86/TranscodeImageUID.lib
a60a12abde8caf36fe3bef6ec187f7b3  10.0.17763.0/um/x86/tsec.lib
31acc6e9efa1fef9f06bffee3d4e51e9  10.0.17763.0/um/x86/glmf32.lib
ecf52e90d021607124315fbe01f2f37f  10.0.17763.0/um/x86/tbs.lib
ccbc15b5c8769ac6243f8ee6e11ee2f1  10.0.17763.0/um/x86/tspubplugincom.lib
5f4ccc2e3f663d12fd588a9cec9bb8b4  10.0.17763.0/um/x86/tdh.lib
ebd95f5b55aa7d9ff683378d9092fc66  10.0.17763.0/um/x86/tapi32l.lib
92dd29161f3dd0c0794f00ecf0a21a40  10.0.17763.0/um/x86/twain_32.lib
45f23229c11e31345fd9ebfaf29a581c  10.0.17763.0/um/x86/swdevice.lib
618091db2f47e7fb9c84b3dae7963325  10.0.17763.0/um/x86/twinapi.lib
f968e9d0afef895705026a10c0a49484  10.0.17763.0/um/x86/gdiplus.lib
2bd21aa242cec3a95c94454e69090dfa  10.0.17763.0/um/x86/txfw32.lib
0cb1317e9dcd1370831fe9ddac5b0670  10.0.17763.0/um/x86/Gdi32.Lib
7164016f0c0de762070e96d58dc616b5  10.0.17763.0/um/x86/fxsutility.lib
ca0b0a4114f9b67dff710f4bd232166e  10.0.17763.0/um/x86/fwpuclnt.lib
10a5fed35b8c6a9c304deb1f0c4d83e8  10.0.17763.0/um/x86/ualapi.lib
659b738e57967ea27bfa0bbc8673ba7c  10.0.17763.0/um/x86/FrameDyd.Lib
9338d0717ef858aee7f947521e28fc63  10.0.17763.0/um/x86/UIAutomationCore.lib
8b20eb949789d897e8fee14d9839fd93  10.0.17763.0/um/x86/FrameDyn.Lib
633a5c6ad7d3e80a55193414708f3438  10.0.17763.0/um/x86/fontsub.lib
8951680a6247dbfe32ae77688a09714e  10.0.17763.0/um/x86/fileextd.lib
59f3f9b56465335cb74001a8d02f77fd  10.0.17763.0/um/x86/fltLib.lib
29e529027e33eee147948c7901435fc9  10.0.17763.0/um/x86/FhSvcCtl.lib
19e04716bae64cd82a65a95aa164f1f1  10.0.17763.0/um/x86/feclient.lib
37cf6e1e80606e28ea00564d08c9b53d  10.0.17763.0/um/x86/umpdddi.lib
c14ca24da59b90edf5457cb6a534d8f9  10.0.17763.0/um/x86/unicows.lib
713746ec42275c1fd43adf6bdac52ed4  10.0.17763.0/um/x86/Urlmon.Lib
af6af6300d255b5a2e7e65aa8c4c7acc  10.0.17763.0/um/x86/Uuid.Lib
53facf610365e968f988cc8efd1b65aa  10.0.17763.0/um/x86/USP10.Lib
ba5a0c97d23a3699369f32f02f0c87d8  10.0.17763.0/um/x86/Uxtheme.lib
bf218e2aad76ec39c5f451e5d9aa33e6  10.0.17763.0/um/x86/vccomsup.lib
ec329cc490257a077607eeb97ea2d281  10.0.17763.0/um/x86/UserEnv.Lib
357519c52eb73f9b5c2fe207a43327da  10.0.17763.0/um/x86/User32.Lib
395e8114a5112e544710dc207c7f9ee2  10.0.17763.0/um/x86/FaultRep.Lib
4fe25a3534319e8759b8a80ea48f0acb  10.0.17763.0/um/x86/evr.lib
d13e116f8cf8ba851e2e040f820776e4  10.0.17763.0/um/x86/esent.lib
b93d3f2ab2655587ab65c067b330d5cf  10.0.17763.0/um/x86/ElsCore.lib
592fb1addd3730724c3abe84a3a0e4f2  10.0.17763.0/um/x86/els.lib
2fb7cfef813e225243afdb2bd5afecec  10.0.17763.0/um/x86/elfapi.lib
dd375b5d6d8e5ebfe2b647d49963fb6d  10.0.17763.0/um/x86/ehstorguids.lib
1a2e55edd4fedb12e9f1cbb8eaa14ed1  10.0.17763.0/um/x86/VdmDbg.Lib
8af49057f023462043208eacb518ab22  10.0.17763.0/um/x86/vds_uuid.lib
af797c08f2f224f3a489659aab28a642  10.0.17763.0/um/x86/Version.Lib
ba278f8e61dfd49e1b469b17fc76e33d  10.0.17763.0/um/x86/vssapi.lib
2b35449763aaa1f8921ce3cacbf01fc8  10.0.17763.0/um/x86/vscmgr.lib
052d6f348a770235de502620d7ccb7ec  10.0.17763.0/um/x86/Virtdisk.Lib
afae5bb375e89f654006c6907fa31c74  10.0.17763.0/um/x86/Vfw32.Lib
54cf6998c54c6f642ed7fae989d87237  10.0.17763.0/um/x86/efswrt.lib
b32efecd740f80071dddc7cdff65956e  10.0.17763.0/um/x86/easregprov.lib
89c108552c961e38d24a765aaa41f088  10.0.17763.0/um/x86/eappprxy.lib
ecdb0a9cda26522779c7fcb9be887fd0  10.0.17763.0/um/x86/dxva2.lib
266ac521760a59d15e42e007b9e4303e  10.0.17763.0/um/x86/eappcfg.lib
4b47878696337bfd5150d70e05ab943d  10.0.17763.0/um/x86/dxtrans.lib
9286d76c2629d4da4320f7e5affd9d06  10.0.17763.0/um/x86/dxtmsft.lib
8e6c97175c44d44bc68ebb433bbc335d  10.0.17763.0/um/x86/dxguid.lib
1367d0e62f3b59e2f2f0359b9b1d26df  10.0.17763.0/um/x86/dxgi.lib
b62f4cd94e0e420c81ec9bc26dd62c7a  10.0.17763.0/um/x86/dxcompiler.lib
fd956736dcbbc134c20c17a439533e43  10.0.17763.0/um/x86/dwrite.lib
97a98a322cba2a5e5ea955799e44e8a2  10.0.17763.0/um/x86/vss_uuid.lib
f9e46aa8ed70608a77f4322deab8b53a  10.0.17763.0/um/x86/vstorinterface.lib
832f2007b1df48f6b52a91d52ffb4ef2  10.0.17763.0/um/x86/wcmapi.lib
cf93c60157106bc6f07ac39fed08e500  10.0.17763.0/um/x86/wbemuuid.lib
0539657df308f8ea2a005957b218bb0c  10.0.17763.0/um/x86/wcmguid.lib
c6e369e0da678287a761b3fad0636840  10.0.17763.0/um/x86/wdsbp.lib
5cbcf2adff178a2fc3c17c39727ba61e  10.0.17763.0/um/x86/dwmapi.lib
d31d29a242abf89ec83e9a3a6b316990  10.0.17763.0/um/x86/DtcHelp.Lib
4ac192dca373028f61b85f287723191b  10.0.17763.0/um/x86/wdsClientAPI.LIB
290039954df24f8dfb91a1cb056f88cd  10.0.17763.0/um/x86/wdstptc.lib
c3e0072cbad8b3ea9b4053d7a5d7954c  10.0.17763.0/um/x86/wdspxe.lib
fb826943fdd14b8d924a02be475bffe4  10.0.17763.0/um/x86/WebServices.lib
bae0d07ac9e22eda8e82b5b3c604f58b  10.0.17763.0/um/x86/websocket.lib
a2af920f3a03ac325b4a3324d7f204ae  10.0.17763.0/um/x86/wecapi.lib
47d9a6c627df40aa0bb5e078cd636945  10.0.17763.0/um/x86/wdsmc.lib
1a9240ceb11c064136b8a13252383976  10.0.17763.0/um/x86/DSUIExt.Lib
7954720bdeec7a1b324914c98f565559  10.0.17763.0/um/x86/dststlog.lib
b5f3404532fb29208e933912c8d5411b  10.0.17763.0/um/x86/Wer.lib
21de97b04dc481a441d505a14d46617a  10.0.17763.0/um/x86/dssec.lib
68ba7f389bb15df2d99f1ee744ecc0e2  10.0.17763.0/um/x86/wevtapi.lib
ad771746ead3ed2296ad8cf32eb68180  10.0.17763.0/um/x86/DSProp.Lib
e379d5b3880a686fdb6dc1f1053e9de5  10.0.17763.0/um/x86/WiaGuid.Lib
bf3f4b5da322cee23aee3f39b4c97c61  10.0.17763.0/um/x86/dsound.lib
f94495d53a37fa54fe0f29770da02ae9  10.0.17763.0/um/x86/wiaservc.lib
274872d2ce2ec9d3fee4edf430a7ed07  10.0.17763.0/um/x86/drttransport.lib
122dd97bcc06ae76ff033ccbfa05e791  10.0.17763.0/um/x86/wiautil.lib
f6fac0d232ccad4ccc46935e619b91ea  10.0.17763.0/um/x86/drtprov.lib
c8d9cf2904bbcbd6c85a39e98d3dce9a  10.0.17763.0/um/x86/drt.lib
f270bb6fce4b1d9408e3c3543530dee7  10.0.17763.0/um/x86/dpx.lib
905c53a4907df12bef0b457ab3b411df  10.0.17763.0/um/x86/WinBio.lib
05bb8b1b42e773b80fce04e7d31e5810  10.0.17763.0/um/x86/dnsrslvr.lib
295795b23acea94979ad9fb24288efeb  10.0.17763.0/um/x86/dnsrpc.lib
d4daa8e8e4dbb7f908ef642ed609d662  10.0.17763.0/um/x86/windows.ai.machinelearning.lib
ba3200c2de62127fdfb85bd00e8e796f  10.0.17763.0/um/x86/dnsperf.lib
87ae9c4323689285923d6bd1b9ef0b2b  10.0.17763.0/um/x86/windows.networking.lib
7b829ec5f38fcba085680d71785aaea3  10.0.17763.0/um/x86/windows.data.pdf.lib
79741ff85125bc3303c2d15e8ea0fc27  10.0.17763.0/um/x86/dnslib.lib
de1831a09868203637425c99e6bd4ad4  10.0.17763.0/um/x86/windows.ui.lib
ead83d027fa2cab7c83bd73b20df202e  10.0.17763.0/um/x86/dnscrcli.lib
6be2439a48ea3e3a99cd25dce5a3b84d  10.0.17763.0/um/x86/WindowsApp.lib
e53081d3ae65d235c0efa1fd550418cc  10.0.17763.0/um/x86/DnsAPI.Lib
c69578cb3be4c36e2e1b289a3563d58d  10.0.17763.0/um/x86/dmprocessxmlfiltered.lib
4e2f384059d1c131f8c722a5daeb5dca  10.0.17763.0/um/x86/WindowsApp_downlevel.lib
8bcf54337cbeb325e1798452b2192d09  10.0.17763.0/um/x86/dmoguids.lib
d06f59b80857a77df6fd124c91a17971  10.0.17763.0/um/x86/windowscodecs.lib
c409f619071cef9a832ffad6a426dffd  10.0.17763.0/um/x86/windowssideshowguids.lib
7cb825a8ed1294d713e94365f75e22a3  10.0.17763.0/um/x86/winfax.lib
6fd6bc004c0bab409f2d22d22e9305a9  10.0.17763.0/um/x86/dloadhelper.lib
0fbf0eb2c391c2fb8b1b1bd7d8f64a1d  10.0.17763.0/um/x86/winhttp.lib
8a643c1147cdb3dc5e6ea6d316b56127  10.0.17763.0/um/x86/dinput8.lib
d735693b5831193bf6a2794cd6ce0b72  10.0.17763.0/um/x86/difxapi.lib
566b64e3454924b431b5808ef7b9964c  10.0.17763.0/um/x86/dhcpsapi.lib
bc709ac7e367f7db4f94241cad8c3567  10.0.17763.0/um/x86/DhcpCSvc6.Lib
a0f42baea30d9dbdbfbe4fdc7596bf5b  10.0.17763.0/um/x86/WinInet.Lib
3dc0248c61518b910f6cd2ddd25155ed  10.0.17763.0/um/x86/winml.lib
c44eda23d2e80b4afda03d0de923ffe9  10.0.17763.0/um/x86/WinMM.Lib
ee22b4329e767075baa631796598b931  10.0.17763.0/um/x86/winsatapi.lib
33fb1de27edba180e9dd433c72f92c4f  10.0.17763.0/um/x86/winscard.lib
95aba5cd172b01b1439185b8324bae82  10.0.17763.0/um/x86/WinSpool.Lib
2137978e80d12499fbe843806d692f0f  10.0.17763.0/um/x86/DhcpCSvc.Lib
55ef7a8c0912441ab82b6577fb339dbf  10.0.17763.0/um/x86/winsta.lib
f270f8d389953e4e96b71ca7c59bb75c  10.0.17763.0/um/x86/winsqlite3.lib
07629a3e9464795ef663aea40c60468e  10.0.17763.0/um/x86/WinStrm.Lib
c984e990573939be65a615e9ae61c1e9  10.0.17763.0/um/x86/WinTrust.Lib
840f2b2cabf8fab6ef59aad1e63cdaf1  10.0.17763.0/um/x86/wlanapi.lib
4b93744123489972b248a250403eeb21  10.0.17763.0/um/x86/winusb.lib
aa255b91ab10f25befafd1fe0f425a9d  10.0.17763.0/um/x86/wlanui.lib
83582cc3c5444c8d2e9336d334e581ee  10.0.17763.0/um/x86/Wldp.Lib
0cde1e6a863e59ee89cdb0778a41c3e3  10.0.17763.0/um/x86/Wldap32.Lib
58eccd8df2fde5cf00e7eb8c63996e1f  10.0.17763.0/um/x86/wmcodecdspuuid.lib
641cfc87f413143c2f27fd14cdd5b6f4  10.0.17763.0/um/x86/wmvcore.lib
a3f5e18c09692c818f93eae119b28aaa  10.0.17763.0/um/x86/wmip.lib
932ef39dffdb2e308c103b72b5c1492c  10.0.17763.0/um/x86/wmiutils.lib
343f9165750637d713a92890f49d5c76  10.0.17763.0/um/x86/dflayout.lib
77fc5dca85c276c9fcacee7fd71bce82  10.0.17763.0/um/x86/devmgr.lib
f5f59ccc0940cdbab134874e668c2a15  10.0.17763.0/um/x86/deviceaccess.lib
524414eb168cdb06c63f477f1f9a3736  10.0.17763.0/um/x86/devenum.lib
5d369eacd1ebe47efa2e8ba7e225e6af  10.0.17763.0/um/x86/ddraw.lib
bc9f559b2dcae01f1d22ac6c4cd7cad6  10.0.17763.0/um/x86/dcomp.lib
10ed1ab67f561587466c0276b7539ded  10.0.17763.0/um/x86/dciman32.lib
53ea1e3cfdeccf098062e461eeebc4ad  10.0.17763.0/um/x86/DbgModel.Lib
e9654aa5936ee237dc798f5496314a96  10.0.17763.0/um/x86/workspaceax.lib
98d2e12a07aa8b432769ec832441fdbb  10.0.17763.0/um/x86/DbgHelp.Lib
b4ab9dab5a14bd8cc1346fc67a0ffbd9  10.0.17763.0/um/x86/wofutil.lib
1b7c051f5d6cb313fde905d726316673  10.0.17763.0/um/x86/Wow32.Lib
61995b46f4f685556225d23c8614950d  10.0.17763.0/um/x86/DbgEng.Lib
4dd9385af0d3884cc1dadc5710f4d9b0  10.0.17763.0/um/x86/WS2_32.Lib
6dd306b517b3cf7f2459d2e57eef3a9f  10.0.17763.0/um/x86/wsbapp_uuid.Lib
755690980f5398b1d06d1b8a8d795205  10.0.17763.0/um/x86/wscapi.lib
ebc3923954df408cf6ba12d5945c5484  10.0.17763.0/um/x86/wsclient.lib
aaac47f1fbdb2d53eaaf83ca764667cb  10.0.17763.0/um/x86/wsdapi.lib
2935d5ac6b58b1fc6814107980b4e0f8  10.0.17763.0/um/x86/wsbonline.lib
944b7d3f10302ed08a30e0c2b322c195  10.0.17763.0/um/x86/davclnt.lib
d7e8f6361a313035381bbceb6eaac7a1  10.0.17763.0/um/x86/d3dcsxd.lib
4e7b722471463b44f7038e894ffbd046  10.0.17763.0/um/x86/d3dcsx.lib
6a039118dc235e856735605fcd24261e  10.0.17763.0/um/x86/d3dcompiler.lib
55f9be99cc72d1ffcb39a53742a3b29a  10.0.17763.0/um/x86/d3d9.lib
d632431e09972cbaae0ddd013ebb1d44  10.0.17763.0/um/x86/d3d12.lib
ee6ffaca4a585957d287767f0ebf296e  10.0.17763.0/um/x86/d3d11.lib
435b14712ecd9d3b527ada6ff9c61fa7  10.0.17763.0/um/x86/d3d10_1.lib
e2de48b23f0921abb8cd2f7de87ef6fe  10.0.17763.0/um/x86/d3d10.lib
0c96fd1e2c03cbf3ed0cbd8dedd53600  10.0.17763.0/um/x86/d2d1.lib
8efe6db86170ee704dfab1d53b2276ae  10.0.17763.0/um/x86/cscdll.lib
81acd7b9335effe51b823a5ece6af687  10.0.17763.0/um/x86/cscapi.lib
cede49cb4c716d96d8dfce2d1f05e3ed  10.0.17763.0/um/x86/cryptxml.lib
4fa549ba84247e262b32148244d5a9dc  10.0.17763.0/um/x86/cryptui.lib
e6bba5b377d73443ca6943f67698582f  10.0.17763.0/um/x86/CryptNet.Lib
f595a5b981345127d97f38d79f4aa8ad  10.0.17763.0/um/x86/cryptdll.lib
2b845433bf63ea48032b00137e161209  10.0.17763.0/um/x86/Crypt32.Lib
27a707e83bbf1af87d76762b0d9292fb  10.0.17763.0/um/x86/Credui.lib
47f355cf3fc3caf5260c6d569c1c1edd  10.0.17763.0/um/x86/corrEngine.lib
d480cd6d0bfa9d1d01b1f91925d71a3a  10.0.17763.0/um/x86/CoreMessaging.lib
f1b88e9886f943b8b356b17460ea8cac  10.0.17763.0/um/x86/ComSvcs.Lib
dbf9c5852a04fc46c70880f2ec65019c  10.0.17763.0/um/x86/compstui.lib
3b1465190c2aa56e9f1dd82098261287  10.0.17763.0/um/x86/CompPkgSup.lib
5c10f9314cc62dbb6614245d4e9e5ecf  10.0.17763.0/um/x86/ComDlg32.Lib
1e55a88c6ccb3a644c7fcb9f8112708d  10.0.17763.0/um/x86/ComCtl32.Lib
beae3561769d29b4db4d976ab3e5bcf3  10.0.17763.0/um/x86/ClusApi.Lib
7b8a7bc9b1375669e94cfab25fbc5f94  10.0.17763.0/um/x86/clfsw32.lib
c82f4d02403f61cdb71a793fae049280  10.0.17763.0/um/x86/clfsmgmt.lib
c7ac7db6c8f775531b749366b728c912  10.0.17763.0/um/x86/cldapi.lib
d365a08ee27b4a78ff7eb9da36bf8471  10.0.17763.0/um/x86/Chakrart.lib
63dbd1f141418c29b7657851e11351d2  10.0.17763.0/um/x86/cfgmgr32.lib
a41c20c36768592d51f9db84ec07b118  10.0.17763.0/um/x86/CertPolEng.Lib
800c42895606e9cb307190892ad6ae7a  10.0.17763.0/um/x86/certcli.lib
04953f2e32d2a645acc53fc6f4f7dae7  10.0.17763.0/um/x86/CertIdl.Lib
86fca383a3e9ff49e75f15ea7e4295fa  10.0.17763.0/um/x86/certca.lib
09944843056b23340c6fa50a90caa159  10.0.17763.0/um/x86/certadm.lib
25f5f47d5701a889668075347b298cac  10.0.17763.0/um/x86/Cabinet.Lib
1a8fa26c7d1c8e9e2bb0987069c98f9c  10.0.17763.0/um/x86/BufferOverflowU.lib
47e3ed793333876a6703b3f6fb7674dc  10.0.17763.0/um/x86/bthprops.lib
b8e8e0e0c39bca1303bcce8b153a124a  10.0.17763.0/um/x86/BluetoothApis.lib
d3436031618a582a7b1d4a24b06bc12d  10.0.17763.0/um/x86/BufferOverflow.lib
ba2c60c43e9b2a45aa938eaed54ccd04  10.0.17763.0/um/x86/Bits.Lib
c75a71daeccfac3ff1f208e324d79d91  10.0.17763.0/um/x86/basesrv.lib
e517da626b0faef0b066a9405ae6c633  10.0.17763.0/um/x86/bcrypt.lib
c3733c31e401af9aa1b66de1da5cae2a  10.0.17763.0/um/x86/avifil32.Lib
de0615a26a5fa0f11782cbafa998c674  10.0.17763.0/um/x86/aux_ulib.lib
8466b0dcc7dd958bbe30cd802690ea8d  10.0.17763.0/um/x86/avrt.lib
6de197566cc1cef14d63897bf93535ec  10.0.17763.0/um/x86/AuthZ.Lib
716efd79a0b0d8466f548273d9af193d  10.0.17763.0/um/x86/audiomediatypecrt.lib
5a18b94ca3145f4b137b7e0707a130fb  10.0.17763.0/um/x86/audioeng.lib
dd7ed2a57d0ccc4eb1fe1442a914c19d  10.0.17763.0/um/x86/AudioBaseProcessingObjectV140.lib
c39b5f98ed17f00ec42ba0a533562b30  10.0.17763.0/um/x86/audiobaseprocessingobject.lib
38f304d8a3cd2877ee42c8d5ece1dda7  10.0.17763.0/um/x86/ASycFilt.Lib
28518c07023a0905b7466280ca74f95d  10.0.17763.0/um/x86/appnotify.lib
60db52d7b274124fa734a59ed1925a38  10.0.17763.0/um/x86/appmgr.lib
3866b7ddc482c382b0d416bac147f384  10.0.17763.0/um/x86/appmgmts.lib
92088b79f2e26d2cc65659a8aec901a5  10.0.17763.0/um/x86/apidll.lib
5e5fb9ef93f4483f88eb37f75d31b828  10.0.17763.0/um/x86/api-ms-win-net-isolation-l1-1-0.lib
ec6375700e62622a76ec33cbe9314088  10.0.17763.0/um/x86/amstrmid.lib
4b08c2202734376e67984a3881a5f93a  10.0.17763.0/um/x86/amsi.lib
45bd6c5155521bcdfe55482d908f41b7  10.0.17763.0/um/x86/ahadmin.lib
ea27ddbb7f77831e521eca8b19e6edd9  10.0.17763.0/um/x86/advpack.Lib
4c06b0727041fee938fdea1c41517670  10.0.17763.0/um/x86/AdvAPI32.Lib
f751399897b898751ea5755ef4ddfe73  10.0.17763.0/um/x86/ADSIid.Lib
f3d31391d084bb2531f94d2ebd8d8858  10.0.17763.0/um/x86/ActiveDS.Lib
71c5afccc59779cadaae587c9539c5b0  10.0.17763.0/um/x86/AclUI.Lib
ba4068a4ecebe000e6b26c707d40c145  10.0.17763.0/um/x86/WtsApi32.Lib
22d029ff08c56fe6ef4951c0b1e3db30  10.0.17763.0/um/x86/xapobase.lib
ca04078ded3258da4d1b0ef473cf7bac  10.0.17763.0/um/x86/wuguid.lib
1bdeb9502278c298ef7d58cf8f351367  10.0.17763.0/um/x86/xaswitch.lib
76e24277845f4f653d69f9627370af92  10.0.17763.0/um/x86/xapobase2_8.lib
67c370f85f40fb24bdb32a2e65f945ed  10.0.17763.0/um/x86/WSock32.Lib
cfc8dd95a7a77800531c358b2a86f166  10.0.17763.0/um/x86/xaudio2_8.lib
241395c1ecb03142f1f655557f37eba8  10.0.17763.0/um/x86/xinput.lib
f8f488055d1056d05c93b54c28d7e533  10.0.17763.0/um/x86/Xinput9_1_0.lib
b23eb4648b2c18633ac4b8ccca0cdcf0  10.0.17763.0/um/x86/xmllite.lib
fdd18e42e9c99930418485ba953b44c0  10.0.17763.0/um/x86/xolehlp.lib
7d1aac20978eea10934129747922cc4a  10.0.17763.0/um/x86/xpsprint.lib
fe141046e0f45ee1f805568c7ce5e30e  10.0.17763.0/um/x86/xpsdocumenttargetprint.lib
93157d0bd4e5d10b02bf348d2d5e6158  10.0.17763.0/um/x86/xinputuap.lib
c8d3ac1a2b04b44994b0d9552381089b  10.0.17763.0/um/x86/xaudio2.lib
95ce46b23099ec80a792b2b452723bd1  10.0.17763.0/um/x86/WSnmp32.Lib
84fb6b704f3b11c403c7d518812bbbac  10.0.17763.0/um/x86/wsmsvc.lib
5f06a35536075be48b883623a6f375e6  10.0.17763.0/ucrt/x64/ucrtd.lib
b7cd4e115e865ad89e5884982c7c1826  10.0.17763.0/ucrt/x64/ucrt.lib
1a2f70e9cca5cf149934467f42d828cf  10.0.17763.0/ucrt/x64/libucrtd.lib
9786253e3c028af5e85a84eb1022d1c3  10.0.17763.0/ucrt/x64/libucrt.lib
cd894efc37dd38c7b0973bc7da07f08e  10.0.17763.0/um/x64/wsclient.lib
1ab4c6a67342242dbe764c46abba75bc  10.0.17763.0/um/x64/wscapi.lib
d67ac0dff240b1be80ee2b488c613cbe  10.0.17763.0/um/x64/wsbonline.lib
b2e69bb4353ab2e6ecf765b37ae9ff5a  10.0.17763.0/um/x64/wsbapp_uuid.Lib
d936aca5913c575eaa74a73a878242e3  10.0.17763.0/um/x64/WS2_32.Lib
176fab86ebeda7893d3722592d20ba68  10.0.17763.0/um/x64/workspaceax.lib
2c7bc4fd118aa90c5db2c1503f38f074  10.0.17763.0/um/x64/wofutil.lib
9911028d40c97c6bbfb10a62dd72a95b  10.0.17763.0/um/x64/wmvcore.lib
32c34087e6abc8a0fb603e6858fe24b7  10.0.17763.0/um/x64/wnvapi.lib
9a76c0eb18ff02f0168d398ba687bb80  10.0.17763.0/um/x64/wmiutils.lib
97fc21b5624119b76ec7d713e8d9c1e3  10.0.17763.0/um/x64/wmip.lib
230859205562472c7747813bf1040288  10.0.17763.0/um/x64/wmcodecdspuuid.lib
373f6f9713f7daf38feb9bc65a5fb23c  10.0.17763.0/um/x64/Wldp.Lib
28985926d12b535ab42c9eff5fdecccf  10.0.17763.0/um/x64/Wldap32.Lib
700168a1cdcbeaa1bb10f52c2c00c969  10.0.17763.0/um/x64/wlanui.lib
b0dd75342b74a38624175959f32f4390  10.0.17763.0/um/x64/wlanapi.lib
f38acd1e6e22358c14ac2e8ae7d15381  10.0.17763.0/um/x64/winusb.lib
578ffffa6b770af3f2fe89a8c4d6fd0c  10.0.17763.0/um/x64/WinStrm.Lib
59b261592cb7d944037193a634250f9f  10.0.17763.0/um/x64/WinTrust.Lib
363bc190383839f5c3ed1fef27a23745  10.0.17763.0/um/x64/winsta.lib
edbcc47d3995288206dee04dddfcc2f8  10.0.17763.0/um/x64/winsqlite3.lib
18d42f5078e0b05ee3c227240b8ebeb5  10.0.17763.0/um/x64/WinSpool.Lib
d18ece670723f541339c8fcc1a96bcb3  10.0.17763.0/um/x64/winscard.lib
e47e2abe83d4ee96b38830feb9a89cf4  10.0.17763.0/um/x64/WinMM.Lib
5347e358bb3e47275d46fa14f197d884  10.0.17763.0/um/x64/winsatapi.lib
ebc0ef57573d7eeaa5feec068807c869  10.0.17763.0/um/x64/winml.lib
7da727579d86e0b489451469dc34032d  10.0.17763.0/um/x64/WinInet.Lib
442595c7b2065257b2e5fa4fbe8964b5  10.0.17763.0/um/x64/WinHvPlatform.lib
d975ff5d8a0b8d27fb782bb2e4bf7e30  10.0.17763.0/um/x64/WinHvEmulation.lib
b34dba36f6f199a62564e1d64820fb95  10.0.17763.0/um/x64/winhttp.lib
a443f7959d97110a40b0d5fb67f4eb27  10.0.17763.0/um/x64/winfax.lib
0c6269c10d081953416d1c7ed406dfb5  10.0.17763.0/um/x64/windowssideshowguids.lib
63059e1c73c50250dc6a27344ab1bf91  10.0.17763.0/um/x64/windowscodecs.lib
3d937a0c450eaaf46521c7113cca7f37  10.0.17763.0/um/x64/WindowsApp.lib
281dd52e37e64a2445bbe4fec3bab61a  10.0.17763.0/um/x64/WindowsApp_downlevel.lib
c04d0687874ef2c0c6a4af1c96359d1c  10.0.17763.0/um/x64/wsdapi.lib
ad1c26eb4828927122bba97e4c26defc  10.0.17763.0/um/x64/windows.ui.lib
c7e99126f1a87019d586acd05c04584a  10.0.17763.0/um/x64/wsmsvc.lib
2538b2eff94a024900f9310d2361f5e6  10.0.17763.0/um/x64/windows.networking.lib
4809765b5d3ae0e2c31294ec3f271efe  10.0.17763.0/um/x64/WSnmp32.Lib
e1c0bf2fbf169762629bcb3112c7061e  10.0.17763.0/um/x64/windows.data.pdf.lib
263df20f29e0c82ffa6e7efecafea1bc  10.0.17763.0/um/x64/WSock32.Lib
4bd275f08b7ab51b6a41f4ffa03c89e7  10.0.17763.0/um/x64/WtsApi32.Lib
7d306d81375db8e384712497dd60dc5f  10.0.17763.0/um/x64/wuguid.lib
32858ec674e7cc9fc030f610392de064  10.0.17763.0/um/x64/xapobase.lib
c2c265d71a1db717932c0e80d4e450ee  10.0.17763.0/um/x64/windows.ai.machinelearning.lib
beae4f7657cb71eeb54ce226f6307a98  10.0.17763.0/um/x64/xaswitch.lib
51dadcf7217ca319603e9d47587e05b8  10.0.17763.0/um/x64/xaudio2.lib
59d951180785eef43d700d5031782d3c  10.0.17763.0/um/x64/xaudio2_8.lib
ca8ad3d4d30c0dc5769f3fc27b4ee2db  10.0.17763.0/um/x64/xapobase2_8.lib
805eeebbf3717feb1fd18513909175e7  10.0.17763.0/um/x64/WinBio.lib
c7e878e46fb544889bcb7d84fc1e88b4  10.0.17763.0/um/x64/Xinput9_1_0.lib
329ab36b0b14b1a798a55bbab5d9053b  10.0.17763.0/um/x64/xinput.lib
dbd4c14c07529af201f53d0848c00823  10.0.17763.0/um/x64/wiaservc.lib
dde0ee986c02f8e228fec595364de864  10.0.17763.0/um/x64/wiautil.lib
d4560ce9ebb2f61b56164cc717ce02d8  10.0.17763.0/um/x64/WiaGuid.Lib
2b0f9b6276e2115485241ebe0ce26d86  10.0.17763.0/um/x64/xmllite.lib
bf48824120f0db2d32e7ffb64fba3066  10.0.17763.0/um/x64/xinputuap.lib
d04d71c3222b1739e3c19c099d2c4f0a  10.0.17763.0/um/x64/xolehlp.lib
f1d9b928471c55051146fa9a0581cf4e  10.0.17763.0/um/x64/wevtapi.lib
f23124c57ffc7b3c30ec5bdbe3a40b4a  10.0.17763.0/um/x64/xpsdocumenttargetprint.lib
f513c5b47c7ec6f7649a23cd6424d3db  10.0.17763.0/um/x64/xpsprint.lib
11152abb8cb3517698907c8f121c0972  10.0.17763.0/um/x64/Wer.lib
f48ec1f006785e7d1d264f5e2371aa78  10.0.17763.0/um/x64/wecapi.lib
7877ef3189a56d6f3d2162656e5851b2  10.0.17763.0/um/x64/websocket.lib
962db2a5e75d584ff41d13e579857df9  10.0.17763.0/um/x64/WebServices.lib
ddb63c5c52f9a54d4f6795fd400d12af  10.0.17763.0/um/x64/wdstptc.lib
35813109a71650ef3281ce191f7a4512  10.0.17763.0/um/x64/wdspxe.lib
74c6cf5a9c8df51de21f3cef6afe95f1  10.0.17763.0/um/x64/wdsmc.lib
a27407096e1a097788517ac30b0ea8a4  10.0.17763.0/um/x64/wdsbp.lib
d71f6ca549c11f42644a404324576263  10.0.17763.0/um/x64/wcmguid.lib
33b3e4205e6730bd5c15c108ad6b8168  10.0.17763.0/um/x64/wdsClientAPI.LIB
50e39c1dbe9db3b1990db6e95ab8503f  10.0.17763.0/um/x64/wcmapi.lib
0869e09eb7289436dc3d6f89530a8ea3  10.0.17763.0/um/x64/wbemuuid.lib
6a5429e0ac06102d2fae5e169c2cace9  10.0.17763.0/um/x64/vstorinterface.lib
46b440f00506e6d41fd48cf928a00d20  10.0.17763.0/um/x64/vssapi.lib
37dad37beef5937f59421990633f06a9  10.0.17763.0/um/x64/vss_uuid.lib
6f4fd168f9f68cef82d35b485b7697a1  10.0.17763.0/um/x64/vscmgr.lib
6a153b0fc22e446744ff48b94c2d8f6a  10.0.17763.0/um/x64/vmsavedstatedumpprovider.lib
dfbc040535932d5e89a49da3b0115825  10.0.17763.0/um/x64/vmdevicehost.lib
7810c557585fd69d6ccf4be031565e1a  10.0.17763.0/um/x64/Virtdisk.Lib
db733ee8638e1334fe21f212ff87dc8c  10.0.17763.0/um/x64/Vfw32.Lib
909969fb66f546cf2be0305c15da6e2a  10.0.17763.0/um/x64/vertdll.lib
f12d7f9875c26231f1f03b21ef1c2364  10.0.17763.0/um/x64/Version.Lib
25bfd3f31ca338aa66fa751fe78bfda2  10.0.17763.0/um/x64/vds_uuid.lib
a0f7cab4cfa75f96cbf171f97a6e4593  10.0.17763.0/um/x64/vccomsup.lib
4bb166183113d43b8a8a55daa7a0748b  10.0.17763.0/um/x64/Uxtheme.lib
3c18ccb3519c6baf4d3444a5a5d25cec  10.0.17763.0/um/x64/Uuid.Lib
c45a4183e7d87c17b4a696b8377e8dfd  10.0.17763.0/um/x64/USP10.Lib
6fe052c35a1d069b0c0e75184b8d3dc9  10.0.17763.0/um/x64/UserEnv.Lib
f7a30fe3907df76bd874ae31421a909b  10.0.17763.0/um/x64/User32.Lib
7350fdfdc2f0a1f0dec2aed49f2ac907  10.0.17763.0/um/x64/Urlmon.Lib
ee4a4a167c79d8390f39999547ef6da5  10.0.17763.0/um/x64/umpdddi.lib
507683f8283fb0d961895fd2d6ff393c  10.0.17763.0/um/x64/UIAutomationCore.lib
1ff14bad4f1b1279888b0c72104b8b15  10.0.17763.0/um/x64/ualapi.lib
fc8e18a528b5c52f066168e34761d513  10.0.17763.0/um/x64/txfw32.lib
4fed236411fb2fe84c95c56d72962ed4  10.0.17763.0/um/x64/twinapi.lib
a661d1ac9482fe190a7e5024703a7d4f  10.0.17763.0/um/x64/tspubplugincom.lib
3de142fb5c5defb4fec6e29d7ecc2016  10.0.17763.0/um/x64/tsec.lib
81df44ecbee6aa679e191d8160598faa  10.0.17763.0/um/x64/Traffic.Lib
4b192b020e638dd006cd036c83a4a38f  10.0.17763.0/um/x64/TranscodeImageUID.lib
6e71f5381534a58daabc433bbac2fb91  10.0.17763.0/um/x64/tokenbinding.lib
d680173715d97a1ebe2ab185330bb6fa  10.0.17763.0/um/x64/tdh.lib
ef3a7434763b40063cccf820cfe9cc7d  10.0.17763.0/um/x64/tbs.lib
cd0952abfe23003e2c79974706b5ca0f  10.0.17763.0/um/x64/taskschd.lib
d8f1d6fda9bbfa0f92009d00765b9a2d  10.0.17763.0/um/x64/tapi32l.lib
0f3d4a8b59f38750b77b494448ca74dc  10.0.17763.0/um/x64/t2embed.lib
8d0b2188bbd6d523fee09c5526e98c73  10.0.17763.0/um/x64/Tapi32.Lib
eb20d70ef5f4cde42bdda9d9d19646ce  10.0.17763.0/um/x64/synchronization.lib
8f9234f8fc7b949a177af129f6d3c392  10.0.17763.0/um/x64/swdevice.lib
f8f4aa1de59233e87c88bfefcf194028  10.0.17763.0/um/x64/structuredquery.lib
5874e47d16aa73a01b5f8b5f62fb201e  10.0.17763.0/um/x64/Svcguid.Lib
c7619af79808777dd9eea8d7592002e9  10.0.17763.0/um/x64/strsafe.lib
dfdb4f63b49cf4e70f3eeed19758d859  10.0.17763.0/um/x64/strmiids.lib
1db6cc427ae76e09641fe60be657ce72  10.0.17763.0/um/x64/strmbase.lib
0922a9f0c52f1fadc7d2a3a4fc12d1fa  10.0.17763.0/um/x64/Sti.Lib
e9ab7e2422e162fbd1083b6a2b3b617d  10.0.17763.0/um/x64/ssdpapi.lib
fd3d23ba0174dadf35c2e774b3d53d67  10.0.17763.0/um/x64/srpapi.lib
75e3d7ba1e5aa990eb4ff8529c1515cb  10.0.17763.0/um/x64/SrClient.lib
2cb66790b9a806386a0d9e798728b230  10.0.17763.0/um/x64/SpOrder.Lib
764c4f1a31e2d25716059591af586475  10.0.17763.0/um/x64/SnmpAPI.Lib
b4c657f4c007b22fe3f4bc3bd9dcb64b  10.0.17763.0/um/x64/slwga.lib
ff0151b06341368893780fb85d04ad67  10.0.17763.0/um/x64/spoolss.lib
284b7b56c8483f70ce59d1583eb1016f  10.0.17763.0/um/x64/slcext.lib
f62d96087ddac0d21a30d34b3348b2a8  10.0.17763.0/um/x64/slc.lib
a31e27f89cb05246b08894a632c0c56e  10.0.17763.0/um/x64/ShFolder.Lib
bde92a293fba8964901d330c75670583  10.0.17763.0/um/x64/shell32.lib
cf629c5737e039fbea79458af9e586ad  10.0.17763.0/um/x64/shdocvw.lib
d147ea215c35f8d4431f9127b741e53c  10.0.17763.0/um/x64/ShLwApi.Lib
395a01574168b8affe38167e0069ae33  10.0.17763.0/um/x64/shcore.lib
18df9789fc54f525e4116b8887cba926  10.0.17763.0/um/x64/SetupAPI.Lib
10637b17a9437bf4735a5a6510dca347  10.0.17763.0/um/x64/SensorsUtils.lib
edcf815883b858dd0cf8ae42c20d3e5d  10.0.17763.0/um/x64/sensorsapi.lib
3b8c5f38a4fe7ba181a05258754b814e  10.0.17763.0/um/x64/SensAPI.Lib
90671d8608eeb1c2e2e38722fda664de  10.0.17763.0/um/x64/sens.lib
df0418a090901ce35fb11abf9822ade0  10.0.17763.0/um/x64/security.lib
9181a0f0452a0635368e10d119969176  10.0.17763.0/um/x64/Secur32.Lib
0edd2e4811d7fd0db2824d6581c4e529  10.0.17763.0/um/x64/SearchSDK.lib
ede708cdb1fa865badc5d611cd9a4c87  10.0.17763.0/um/x64/ScrnSavW.Lib
a444082cda5676daf67396335e3e4fa8  10.0.17763.0/um/x64/ScrnSave.Lib
9fedbd1971012f50d9ef8794c5bf123c  10.0.17763.0/um/x64/scesrv.lib
c343fc30cfb2f2d63a5cbcc583952efa  10.0.17763.0/um/x64/schannel.lib
a3eb3f24dca62cb5ffd772b17a84369d  10.0.17763.0/um/x64/scecli.lib
f7e73bfdc1dc5f1cfc4a84fa03ea45d5  10.0.17763.0/um/x64/SCardDlg.Lib
bd24481a4ddb02e1f06d7c6c28576bc0  10.0.17763.0/um/x64/sbtsv.lib
62be82d8aaf77701754dfc39e7b9858c  10.0.17763.0/um/x64/sas.lib
9cad4f95b0f5a3c9081c72e461ac4728  10.0.17763.0/um/x64/SAPI.Lib
10992f3560bbfd134071458b1b94dc33  10.0.17763.0/um/x64/samsrv.lib
08142c3bec40a6127fc10dfba4b6fdb1  10.0.17763.0/um/x64/samlib.lib
a78836b05fd2c119b9525339bf4e465e  10.0.17763.0/um/x64/runtimeobject.lib
24d5e1d0b09efadfaf282ef004b47a98  10.0.17763.0/um/x64/RTWorkQ.lib
21df4c94b2bff6288bc22536822dcc29  10.0.17763.0/um/x64/Sfc.Lib
b6d11138a50c064ea0042db82eb1736b  10.0.17763.0/um/x64/rtutils.lib
892a8434aecabb3ac97883f8c2989944  10.0.17763.0/um/x64/Rtm.Lib
af4ce162e97366cef71092694c7bb0f6  10.0.17763.0/um/x64/rstrtmgr.lib
b7a71666e0190678451117990d348327  10.0.17763.0/um/x64/rpcutil.lib
eae636da8a795e6f7b1ac0ee3567d5a9  10.0.17763.0/um/x64/RpcRT4.Lib
ba2ae83786aa88fcda9b8bd87399975a  10.0.17763.0/um/x64/rpcproxy.lib
3b8a10772a29f3c4e7fca076910f31c3  10.0.17763.0/um/x64/Rpcns4.Lib
91554a2552d4148df04185bbf9bbf8f0  10.0.17763.0/um/x64/rometadata.lib
1fa9230ea22329fabc5df79616c7f8af  10.0.17763.0/um/x64/resutils.lib
4c4f686dc28057e51d61e8fbec06ab94  10.0.17763.0/um/x64/rasuser.lib
5bab8c9f0befad1de5234eb45046bc4f  10.0.17763.0/um/x64/RASDlg.Lib
41778f6b2bd41f4d35be965eea31ec9b  10.0.17763.0/um/x64/qwave.lib
df6b7876a82420424862204668208e87  10.0.17763.0/um/x64/RASAPI32.Lib
156d1ac3cad4a5c9a4fde9d07d43eb7f  10.0.17763.0/um/x64/query.lib
9245987fd96c5d47f36a96660f889970  10.0.17763.0/um/x64/quartz.lib
7ab284e7e79c4b4a6effd71df9ff1537  10.0.17763.0/um/x64/Psapi.Lib
ad44c544426b1f7283400860451c9273  10.0.17763.0/um/x64/propsys.lib
3d50fb940d011039b389c37b3a3282bd  10.0.17763.0/um/x64/ProjectedFSLib.lib
93357b4e3f2325d354ebeba5699c6e0a  10.0.17763.0/um/x64/powrprof.lib
6d7f1a885ea8e12de014827b57de224a  10.0.17763.0/um/x64/prntvpt.lib
17531bea981bc59f29592c7ef8a25e1f  10.0.17763.0/um/x64/PortableDeviceGuids.lib
9d8fc909a41bd68df35b16d03baa22d2  10.0.17763.0/um/x64/PeerDist.lib
f4ec98a0e0d171c8c173011c4e9b7df7  10.0.17763.0/um/x64/Pdh.Lib
774f231327a1f08b993beb4831158f7d  10.0.17763.0/um/x64/pathcch.lib
0f5693314ddf46661377aaf8b015adfe  10.0.17763.0/um/x64/p2pgraph.lib
d072f2dbfeeb03a765a0ea294c0f313f  10.0.17763.0/um/x64/p2p.lib
5926ef5a48e5cfbbe010a9fbad1667de  10.0.17763.0/um/x64/osptk.lib
8e53fb9afa18c2a69ad28b1fac2a21d0  10.0.17763.0/um/x64/opmxbox.Lib
a99e158a40da80597331be073568ee3d  10.0.17763.0/um/x64/PhotoAcquireUID.lib
6f0cd58b76b616a8ee44be2c94712e6c  10.0.17763.0/um/x64/OpenGL32.Lib
29123a3e0a778f4fe453a72d5d04caee  10.0.17763.0/um/x64/OneCore_downlevel.Lib
6ca0f82b36f89fdbf480e8d1e1f72e60  10.0.17763.0/um/x64/OneCore_apiset.Lib
f2e51c017fbf1d0b7278466f6909f8c8  10.0.17763.0/um/x64/OneCoreUAP_downlevel.Lib
1b0160dbc4813bb5e187975c2826fd6f  10.0.17763.0/um/x64/OneCoreUAP_apiset.Lib
6beeb2da144a0a234e3896f5d957dd67  10.0.17763.0/um/x64/OneCoreUAP.Lib
14d159447e977048dda2b54fd2ef50ed  10.0.17763.0/um/x64/OneCore.Lib
9375f88faf1d8e84dfae48a8df84135f  10.0.17763.0/um/x64/ondemandconnroutehelper.lib
bbf96e64b12b23509637ddd34a54d3c5  10.0.17763.0/um/x64/olesvr32.lib
05322819a31a38bcbc36bfba3a2fd23c  10.0.17763.0/um/x64/OleDlg.Lib
c97bc7ff93aa93944228976482a2a220  10.0.17763.0/um/x64/oledb.lib
c3fc1fef353526ef423823a989b08ffe  10.0.17763.0/um/x64/olecli32.lib
aff9ef7de2fbdc9fb77abbcc9b2e188f  10.0.17763.0/um/x64/OleAcc.Lib
606185656c9e860467b90961c0d94a60  10.0.17763.0/um/x64/Ole32.Lib
9d85fcb174406040db495638360163cf  10.0.17763.0/um/x64/OleAut32.Lib
801ae5b910e5dded8ab9d8573945a635  10.0.17763.0/um/x64/OemLicense.lib
25322960d9952eb3a474c0eaa8ee0130  10.0.17763.0/um/x64/odbccp32.lib
0c431fb2a4588a36f22b17546d89f80a  10.0.17763.0/um/x64/odbcbcp.lib
1f8a4cd5fabc1ae041135ad6119c6302  10.0.17763.0/um/x64/odbc32.lib
12aeca40d90d8bf8c52d9d13d69b800d  10.0.17763.0/um/x64/objsel.lib
e29fa52fe2d6269d2a19480b70171aca  10.0.17763.0/um/x64/rpcexts.lib
681e593227451a023c9d0ddf4b1596e4  10.0.17763.0/um/x64/ntstc_libcmt.lib
efd2dfbd6bfde8a254b254b3f35b736b  10.0.17763.0/um/x64/ntstc_msvcrt.lib
156d1ac3cad4a5c9a4fde9d07d43eb7f  10.0.17763.0/um/x64/NtQuery.Lib
ed1a87faa7096b2692d36872ef791e6e  10.0.17763.0/um/x64/ntmarta.lib
035cc26191b45fa47650ae32e1abe455  10.0.17763.0/um/x64/ntlanman.lib
1c34541c9214625b0a5533c9bbdfffc4  10.0.17763.0/um/x64/ntfrsapi.lib
a29126213de543fab2f17bc14bc2c635  10.0.17763.0/um/x64/ntdsetup.lib
26087d1ac101acb86c1e0a17cb40188a  10.0.17763.0/um/x64/ntdsatq.lib
b7915dedcfcc2173acd74337b13f75cb  10.0.17763.0/um/x64/ntdsa.lib
350c9bd653ef3080a306fce36cdf904f  10.0.17763.0/um/x64/NtDsAPI.Lib
f1d305ff76bfcfdc4262408b05b949dd  10.0.17763.0/um/x64/ntdll.lib
1e0b97f5352e411a56ec1c2dd342bbec  10.0.17763.0/um/x64/nt.lib
7bb44c019cc7b987b8d8a6fc3e049362  10.0.17763.0/um/x64/normaliz.lib
948f5ee26e35c167b9fd3a0815b87163  10.0.17763.0/um/x64/newdev.lib
1cb185205d9280c49f8a01a70ac8c09f  10.0.17763.0/um/x64/NetSh.Lib
9255222e1772c42151c037cceebea6bb  10.0.17763.0/um/x64/ninput.lib
80660d30df503b04664509a5d39bfd41  10.0.17763.0/um/x64/netlib.lib
a85e5bea26ab2da44610c80c90db607f  10.0.17763.0/um/x64/NetAPI32.Lib
cad1bf8367a996c7a9c0babb1865301b  10.0.17763.0/um/x64/ndproxystub.lib
cf64608fd32ccc244de802a1e49bfee7  10.0.17763.0/um/x64/ndfapi.lib
3600fb1fb1eacb93c9dee8a6d96234f0  10.0.17763.0/um/x64/nddeapi.lib
64fb32d5dda79b806baca6d941de60b9  10.0.17763.0/um/x64/ncrypt.lib
3ba1c347fc5f0d99c64cbc57d4f83f4b  10.0.17763.0/um/x64/nanosrv.lib
92472afd0a29714b49357160c407da4f  10.0.17763.0/um/x64/muiload.lib
4a1d93156cf3cadd7ea3b3b962073317  10.0.17763.0/um/x64/mtxdm.lib
ddc9b8723e8cb07ff1519b7d59071dca  10.0.17763.0/um/x64/Mtx.Lib
24aaee3129e8e899fca0ca330c631104  10.0.17763.0/um/x64/msxml6.lib
3cda48e824f7c2bf8f0fc15e032eac4a  10.0.17763.0/um/x64/MsXml2.Lib
bd5bec2ea95c99c567a4dcb201ea1580  10.0.17763.0/um/x64/MsWSock.Lib
93266bb08e572463e12dc509dccd6e9c  10.0.17763.0/um/x64/msvfw32.Lib
243463e0c31aa8f97526e72df1c0fe08  10.0.17763.0/um/x64/msv1_0.lib
0a4f4a9fba26402cc307dd15337c1f80  10.0.17763.0/um/x64/MSTask.Lib
8fb76dd92b3018f931d376a221e99fc1  10.0.17763.0/um/x64/MSRating.Lib
491c5621fd3c2c441240d8736aabccce  10.0.17763.0/um/x64/msports.lib
077e01aef1450e0c0c643eb078e02da5  10.0.17763.0/um/x64/mspbase.lib
4640c1f086a29504f60905ea8323138e  10.0.17763.0/um/x64/mspatchc.lib
3e3aa355b44f5c51aa102d83b2a0dee6  10.0.17763.0/um/x64/MSImg32.Lib
54cc0b2d71ca2a4d679eb9ae17919593  10.0.17763.0/um/x64/mspatcha.lib
c8e528011c974d70d2561233f3e55288  10.0.17763.0/um/x64/Msi.Lib
f869a83b5344ef52a904d73489841643  10.0.17763.0/um/x64/msdrm.lib
fcd6e6a6e8361675519c203407d1549a  10.0.17763.0/um/x64/msdmo.lib
a1ae529697b74bf891a56be208df1bee  10.0.17763.0/um/x64/msdelta.lib
c8b878d7f8bc0bc3bd5f7629aa3392cf  10.0.17763.0/um/x64/msdasc.lib
95f4bfb8ed2b2b6f156c03c68c833e78  10.0.17763.0/um/x64/MsCtfMonitor.lib
f9c86a48189ee323b10785ae3f8025c0  10.0.17763.0/um/x64/Mscms.Lib
245e0ccf4f3a1e848901e20920748ec1  10.0.17763.0/um/x64/MSAJApi.lib
8f70affdecbed53f4a2daeb7829e865a  10.0.17763.0/um/x64/MSAcm32.Lib
61e2299ae586721886483aa2bab3e2c3  10.0.17763.0/um/x64/MrmSupport.lib
7521d2f115cfc6adf1dc0c43878a2663  10.0.17763.0/um/x64/msaatext.lib
2e7ad1ef42586e3e937375ef843a2ea4  10.0.17763.0/um/x64/MqRt.Lib
ed33ee761aa77979926e50427914ff5a  10.0.17763.0/um/x64/MqOA.Lib
c647d67896ab2ad4134b53dbd57be7ae  10.0.17763.0/um/x64/mprsnap.lib
0ec22eef0741ad7ed8e77db86f314f21  10.0.17763.0/um/x64/Mprapi.Lib
d3004148e209ba46ff2be1725966d806  10.0.17763.0/um/x64/mmdevapi.lib
e2dece0598cdf3e6f57f1bb6ade58d88  10.0.17763.0/um/x64/Mpr.Lib
68ff6f493f5e94ac5c12627d6281e421  10.0.17763.0/um/x64/MMC.Lib
8b32c77cf9b5f8ef7d97a34ffb3b5797  10.0.17763.0/um/x64/mincore_downlevel.lib
23a558b26ae4b1cf2e513f32f97110a3  10.0.17763.0/um/x64/mincore.lib
e225f7522036ad5d70928b97018916f7  10.0.17763.0/um/x64/mi.lib
4e119f3b293846ba2860d5029d43c2ac  10.0.17763.0/um/x64/MgmtAPI.Lib
0f7edd673bf31ddabd166e74311da11b  10.0.17763.0/um/x64/mfuuid.lib
24f4655925f8475256f150ad3a017c3c  10.0.17763.0/um/x64/mfsensorgroup.lib
0cad219e81ff92382ca3a7ce0f362b4c  10.0.17763.0/um/x64/Mfsrcsnk.lib
f94a6bc62d232ace9f522619479da585  10.0.17763.0/um/x64/mfreadwrite.lib
c72e33692f55d6e55e841da07ef83027  10.0.17763.0/um/x64/mfplay.lib
b3eacb8ebc345b68b90a2cd12dd9b95a  10.0.17763.0/um/x64/Mfcore.lib
67af227662323deb332c9d2267f89f0b  10.0.17763.0/um/x64/Mfplat.lib
59af0151794a637d5217c1d1d2da7fe2  10.0.17763.0/um/x64/Mf.lib
04e16c84805b4d4acf67369d3ae0591a  10.0.17763.0/um/x64/MDMRegistration.lib
a48e000144f1c483bafe0f78ebf7ddcf  10.0.17763.0/um/x64/mdmlocalmanagement.lib
65cfb69076ad1fab57980fe38373c9ef  10.0.17763.0/um/x64/mciole32.lib
ffcf23e7f25410e1738f3f4191767674  10.0.17763.0/um/x64/mbnapi_uuid.lib
425f6dc342178f75c7e196c262e77354  10.0.17763.0/um/x64/MAPI32.Lib
f562293922d68d20ec2ff65bd937e078  10.0.17763.0/um/x64/magnification.lib
9e2d5fcf04bc61f85095be8bbbba5bd3  10.0.17763.0/um/x64/Lz32.Lib
404790dcd793516dbfdf28e18ca78f05  10.0.17763.0/um/x64/locationapi.lib
2e9cdfd1ab5359b24c566b2b5683e8dc  10.0.17763.0/um/x64/LoadPerf.Lib
2c8e3a9957b8f6626a8ae7c5853d58b9  10.0.17763.0/um/x64/ktmw32.lib
e6e090c643cf48998cd68daa0fb08bd0  10.0.17763.0/um/x64/ksuser.lib
9cc0314f0de46c0f97398f5074c9d9bc  10.0.17763.0/um/x64/keycredmgr.lib
b282907b062f80391cb2f04c2f9c237b  10.0.17763.0/um/x64/KSProxy.Lib
b51aa83f24e9c7f5f3d9529e4962ca07  10.0.17763.0/um/x64/kernel32legacylib.lib
18e3013eda7edcfa676876e9afa2291a  10.0.17763.0/um/x64/kernel32.Lib
13f4522cd192e19095b5b31bf095c66f  10.0.17763.0/um/x64/kerbcli.lib
c19ed17c7dcbc58fc395a5d8cb053e2b  10.0.17763.0/um/x64/jsrt.lib
520c73c1d7cdff8f1abb2bd5c1f21296  10.0.17763.0/um/x64/irprops.lib
1a65c35bbc75cd0fc3a734216e3e4382  10.0.17763.0/um/x64/iscsidsc.lib
9d1922832fcfb194b06c37f0095b58fe  10.0.17763.0/um/x64/Iprop.Lib
bfe2e9c0d81d89d3089b04640d028b29  10.0.17763.0/um/x64/iphlpapi.lib
487e86e4790415630fa0a0fc3f890d85  10.0.17763.0/um/x64/inseng.lib
d1d9442f245d25db123011d382d060ce  10.0.17763.0/um/x64/inkobjcore.lib
298d30301c93c47bf5af9fc92333a6ec  10.0.17763.0/um/x64/Imm32.Lib
c4de4cc8a517beef960bc15461f50e39  10.0.17763.0/um/x64/infocardapi.Lib
da2dc7ecf61f24c1f0af8d42fa290d86  10.0.17763.0/um/x64/imgutil.Lib
c3173a7952d348aca6ee512a0aa189be  10.0.17763.0/um/x64/ImageHlp.Lib
a801388764304fa292e3b87e2b693d15  10.0.17763.0/um/x64/iesetup.lib
a86bb46b083f6b52f9f2e08f25ef13ab  10.0.17763.0/um/x64/IEPMAPI.Lib
6abedbed773a733c0a869522f0a40d97  10.0.17763.0/um/x64/icuuc.lib
d889b6abace1165f2a7afec6d9b01f61  10.0.17763.0/um/x64/icuin.Lib
ba0c249120f56d54f964424e8d043f49  10.0.17763.0/um/x64/Icmui.Lib
4fdd3b4a9be1367908485419db82028f  10.0.17763.0/um/x64/Icm32.Lib
e6534a045eb716860bae8c9128d3d0a3  10.0.17763.0/um/x64/iashlpr.lib
52f4d8369421789b02c28f41627ee1a6  10.0.17763.0/um/x64/httpapi.lib
2ca93c61d58651cf835c9ca8db70ded8  10.0.17763.0/um/x64/Htmlhelp.Lib
e8be3f82c74fbb78b03a60b366959f28  10.0.17763.0/um/x64/hrtfapo.lib
728c9c247cd04914c1e0bb0429fd4ec5  10.0.17763.0/um/x64/HLink.Lib
716461ae07a191001643e7165dbdb88e  10.0.17763.0/um/x64/hid.lib
8700d3167e0525e883f00cab68a4c6a8  10.0.17763.0/um/x64/hhsetup.lib
26b54b3755d0798a0ba4af99d2874a49  10.0.17763.0/um/x64/hbaapi.lib
0a37723627012280fc1deafd18c91048  10.0.17763.0/um/x64/GPEdit.lib
d9658727dd2991010845b1b8d20f5e86  10.0.17763.0/um/x64/gpmuuid.lib
20d2276b16f3d13440fd50b375128f9a  10.0.17763.0/um/x64/GlU32.Lib
db2660c335b8d7c954cf04843c4b20fe  10.0.17763.0/um/x64/glmf32.lib
11e355411698ab891e79604d8659650e  10.0.17763.0/um/x64/gdiplus.lib
c48113ca8ee019b879fc57dae1e00bf2  10.0.17763.0/um/x64/Gdi32.Lib
77578f8a3f130cf3a63275f933f98ad7  10.0.17763.0/um/x64/fxsutility.lib
1d7c465f314169702ca3a9b147925dfb  10.0.17763.0/um/x64/fwpuclnt.lib
4113c26875151d3eba02d4b46d496628  10.0.17763.0/um/x64/FrameDyn.Lib
aec3c2df4f130f3ddf87b534f3e30d7a  10.0.17763.0/um/x64/FrameDyd.Lib
31f2626a40822b183c85f2baadf73ca9  10.0.17763.0/um/x64/fontsub.lib
0dd5df8a4097ae621fdaa5b10faa652e  10.0.17763.0/um/x64/fileextd.lib
28ecb02efc51c4b8e43e57b0f1bcbc47  10.0.17763.0/um/x64/FhSvcCtl.lib
cb31c201197c9cc81617427aba164f69  10.0.17763.0/um/x64/feclient.lib
22b3f604eaf336394e129ed488f18313  10.0.17763.0/um/x64/FaultRep.Lib
6cebf18f5cee9f1a25440416a3c4ab7c  10.0.17763.0/um/x64/evr.lib
f516b52c87f9b77b6547901483c2356f  10.0.17763.0/um/x64/esent.lib
f1db06c863d58ec8fa118dc3083026e6  10.0.17763.0/um/x64/ElsCore.lib
95648637160a1014a1efad4d1a5bbbd4  10.0.17763.0/um/x64/els.lib
6658e50bf9b6e8f05ff0c60667c5143d  10.0.17763.0/um/x64/elfapi.lib
90d230b89880e7af7c5ba98192541e48  10.0.17763.0/um/x64/ehstorguids.lib
9ec31df0ea1dc675d11376ad0f2c73ca  10.0.17763.0/um/x64/efswrt.lib
32002391c9f396106257596065ac3ea8  10.0.17763.0/um/x64/easregprov.lib
c97ad66dfa7d095c19caf5b0a3754d95  10.0.17763.0/um/x64/eappprxy.lib
e9ae105b32f1b5e33ccc5d272c227482  10.0.17763.0/um/x64/eappcfg.lib
ee41411aedfbae73e04d492a2443ddc3  10.0.17763.0/um/x64/fltLib.lib
28a6dd6b104a1f1d708fe9614b8568cb  10.0.17763.0/um/x64/dxtrans.lib
fe32f433ef23985ea242f149c6c115d7  10.0.17763.0/um/x64/dxva2.lib
168e715098ec0a9328dd9df55ea6959d  10.0.17763.0/um/x64/dxtmsft.lib
7001c5b58b03919dc0ff801d94afe951  10.0.17763.0/um/x64/dxguid.lib
c2163a547ef933fbc866b88da1025bd1  10.0.17763.0/um/x64/dxgi.lib
005713e2a529a08f162d44957731e936  10.0.17763.0/um/x64/dxcompiler.lib
9001aa0b8ea911d4e06c6454ac4217a2  10.0.17763.0/um/x64/dwrite.lib
f118be6ebf83c17a7ec78ee6083de545  10.0.17763.0/um/x64/DtcHelp.Lib
aac830b244afb6545d1a62924dccd41e  10.0.17763.0/um/x64/dwmapi.lib
d4e361b79c55acb0becb64aba76b7388  10.0.17763.0/um/x64/DSUIExt.Lib
daec958e73883b0a20aeaff9bf49d18d  10.0.17763.0/um/x64/dststlog.lib
3f7cf0fda6c713dce88839b19f530ede  10.0.17763.0/um/x64/dssec.lib
1be91412dee05981b5057230e5cc30ac  10.0.17763.0/um/x64/DSProp.Lib
9c5015da177af76cbf5466fe0170b304  10.0.17763.0/um/x64/dsound.lib
f797ad977d1ddb93b48a7fea813f41da  10.0.17763.0/um/x64/drtprov.lib
82821642211d8806624ed59b8d42e843  10.0.17763.0/um/x64/drttransport.lib
0c6e41c677a42c922d9996e1925cec99  10.0.17763.0/um/x64/drt.lib
868e8bb422b3c37f4d1a2a92514de1c9  10.0.17763.0/um/x64/dpx.lib
fa2af16206cd6c2830f889789248b831  10.0.17763.0/um/x64/dnsrslvr.lib
0a107c8c2e99b65e88beab0164fc350d  10.0.17763.0/um/x64/dnsrpc.lib
62b52c4bc2d453716984a256e15f599e  10.0.17763.0/um/x64/dnsperf.lib
61e33cc8c1970a013caa72f2bcd67a3a  10.0.17763.0/um/x64/dnscrcli.lib
215b8c7ef23bfc01f722666746d2d6c0  10.0.17763.0/um/x64/dnslib.lib
311c51fcbbc964b7acbb8e7e734b2593  10.0.17763.0/um/x64/DnsAPI.Lib
231624dd9588a8d4731861d927bb96be  10.0.17763.0/um/x64/dmprocessxmlfiltered.lib
69e11ebd733ad12f38a68121ebd50a50  10.0.17763.0/um/x64/dmoguids.lib
f3ddb9fc2dc42e8e4f7ab58275ee379c  10.0.17763.0/um/x64/dloadhelper.lib
aa4c9917c0ae891a98cc9b8ce94fe2d8  10.0.17763.0/um/x64/dinput8.lib
47d1b01538c844e65ae692830b59627c  10.0.17763.0/um/x64/difxapi.lib
96fbdfc13a1ee514d764bcc031f19439  10.0.17763.0/um/x64/dhcpsapi.lib
59b35a08d39d6e9dc118b4320dfe1d2c  10.0.17763.0/um/x64/DhcpCSvc6.Lib
dc06e1d3f2dec7e463ffdbd3ba4a3ace  10.0.17763.0/um/x64/DhcpCSvc.Lib
a2909b7e4f27fd767d89d8845afbeaa1  10.0.17763.0/um/x64/dflayout.lib
0da088bdb538306234523ec2fb22d216  10.0.17763.0/um/x64/devmgr.lib
0384551faf23de7513c175c06abd4eed  10.0.17763.0/um/x64/deviceaccess.lib
81d6c92d6f26eaab3854572caed76959  10.0.17763.0/um/x64/devenum.lib
5c9e4524ff66a2e62186c910150e9d47  10.0.17763.0/um/x64/ddraw.lib
99d7ca6ea44e50aa709496179dbea40f  10.0.17763.0/um/x64/dcomp.lib
6d125e7dcdaf81c88de3e196f45964e2  10.0.17763.0/um/x64/dciman32.lib
f4bb49b6f912efb90912cf4f291129f3  10.0.17763.0/um/x64/DbgModel.Lib
cc33f48d754b1b709ff2340a71600627  10.0.17763.0/um/x64/DbgHelp.Lib
680fdd8328988c426c6f6910632706a9  10.0.17763.0/um/x64/DbgEng.Lib
412514fd321408a9f9b40318e05fb0f5  10.0.17763.0/um/x64/davclnt.lib
8be1bba71ecc8e1df1f6694e6a6ba0bb  10.0.17763.0/um/x64/d3dcsxd.lib
d63b153e8bef804d9d466de57a500afc  10.0.17763.0/um/x64/d3dcsx.lib
fe95a4613ee30419500dc0505cabe97a  10.0.17763.0/um/x64/d3dcompiler.lib
376492d296fd695200e06562dbcb84b5  10.0.17763.0/um/x64/d3d9.lib
c57d52e4bcc5eca66a8134afa7c218f4  10.0.17763.0/um/x64/d3d12.lib
8c9627304b23034ed9a9f214a9bc9a1e  10.0.17763.0/um/x64/d3d11.lib
6c3c851c21e36af0f75856ac43ae3011  10.0.17763.0/um/x64/d3d10_1.lib
6bbcf41c31093c3fb470f651b09cbf89  10.0.17763.0/um/x64/d3d10.lib
d6389e597c6e3bb81196b4ca936f2da8  10.0.17763.0/um/x64/d2d1.lib
4872d7275a8f5084ecdea21fde7681f3  10.0.17763.0/um/x64/cscdll.lib
937577380ee3ba87c533b44041b97925  10.0.17763.0/um/x64/cryptxml.lib
8a5666a36901abd56e931dbfca958cfd  10.0.17763.0/um/x64/cscapi.lib
977fd652d659e990ede38b82170df0f6  10.0.17763.0/um/x64/cryptui.lib
2c01dc8c9a091e7d9f6f64d64be6e891  10.0.17763.0/um/x64/CryptNet.Lib
68a84b080c398c0a0772d5e822d13379  10.0.17763.0/um/x64/cryptdll.lib
4c2d0aa438a08f90451e7a1c7a382024  10.0.17763.0/um/x64/Crypt32.Lib
0c3513fb82c92a4a1023ee76d9bd5459  10.0.17763.0/um/x64/Credui.lib
9b574750c192fa8a056c7c4a73bbb944  10.0.17763.0/um/x64/CoreMessaging.lib
f26ae378f82ffc28f8ce7df21bac47ab  10.0.17763.0/um/x64/corrEngine.lib
06ca53da331e35d88e30eb5a6a269c40  10.0.17763.0/um/x64/ComSvcs.Lib
d355f1947d10c903f1142581f38fb1b3  10.0.17763.0/um/x64/computestorage.lib
019be20a5e5e31611835bfa598f7d043  10.0.17763.0/um/x64/computenetwork.lib
76c432e2a4bf84de8f2926c24d32dc75  10.0.17763.0/um/x64/computecore.lib
f5b593963a385e2e84fb20543ae2c4d5  10.0.17763.0/um/x64/CompPkgSup.lib
b6effa950fd7a01b4a85ef008b2ad530  10.0.17763.0/um/x64/ComDlg32.Lib
59c8fafc3c0dd4af077eca9455f007e6  10.0.17763.0/um/x64/compstui.lib
45fdccc6e1c43e206710a5c468ce4c31  10.0.17763.0/um/x64/ComCtl32.Lib
71f1b3e4e418f2cf0e977ff811fd2221  10.0.17763.0/um/x64/ClusApi.Lib
9641095ad3fe087d4f362ead021ceacc  10.0.17763.0/um/x64/clfsw32.lib
012437690d1b4c7d1c08f9f68426c3f8  10.0.17763.0/um/x64/clfsmgmt.lib
b1b5220cfaaea35d854a397164b1f34b  10.0.17763.0/um/x64/cldapi.lib
410f82a65c15c84f5feb0c103ee38de8  10.0.17763.0/um/x64/Chakrart.lib
431f0bccf533b9c8404609e315d010f5  10.0.17763.0/um/x64/cfgmgr32.lib
385958b09d10dfd403a3ff03ab846498  10.0.17763.0/um/x64/CertPolEng.Lib
29779eeb4ea3c4fee5a9065bcc924339  10.0.17763.0/um/x64/CertIdl.Lib
8eb31d51a671955a0d53cb4616b4f406  10.0.17763.0/um/x64/certca.lib
2e8e1c554f4b4996793872ba149348bf  10.0.17763.0/um/x64/certadm.lib
ce186af1a381b6e71af5111468687b46  10.0.17763.0/um/x64/certcli.lib
e2f860710bc91e44d860a41ef71403b9  10.0.17763.0/um/x64/Cabinet.Lib
660898471cbd6c15e32271a031920374  10.0.17763.0/um/x64/BufferOverflowU.lib
367156d718ca144b6fe7e6feec8f798e  10.0.17763.0/um/x64/BufferOverflow.lib
cdc9c2cac59436a7e6a545c794145552  10.0.17763.0/um/x64/bthprops.lib
53bdab3354723f5749e344ab8297a3a6  10.0.17763.0/um/x64/BluetoothApis.lib
a462734ed1ddb7b2e430523115429b94  10.0.17763.0/um/x64/Bits.Lib
c70796e02d73ce08a8ea89d86fcd4e2d  10.0.17763.0/um/x64/bcrypt.lib
0bf3841881012cff36e63e1319928c97  10.0.17763.0/um/x64/basesrv.lib
0fa42199e90cfe734579156c18da96ea  10.0.17763.0/um/x64/avrt.lib
25ff22065f0a00eae4bd20131955fa55  10.0.17763.0/um/x64/avifil32.Lib
f31dc77d29a9f3d85abde40e53f229dd  10.0.17763.0/um/x64/aux_ulib.lib
d2c5c1e82b58a06552c7978f660f6357  10.0.17763.0/um/x64/AuthZ.Lib
e734174ea9982ccc5bbddd4396f2fb3e  10.0.17763.0/um/x64/audiomediatypecrt.lib
85977cf4aae062ffd895dc6c28443e91  10.0.17763.0/um/x64/audioeng.lib
84e876531adaff300d5871d4699c01a6  10.0.17763.0/um/x64/AudioBaseProcessingObjectV140.lib
8012f35c5ccdbd2786037bae3319b861  10.0.17763.0/um/x64/audiobaseprocessingobject.lib
bbd6131d31da91c56ea518c3734b6409  10.0.17763.0/um/x64/appnotify.lib
7982a1be704adf2bba457b35d0b20805  10.0.17763.0/um/x64/appmgr.lib
ce73f4c2cc2829b859af6e38398fc2e3  10.0.17763.0/um/x64/appmgmts.lib
dfdb4f63b49cf4e70f3eeed19758d859  10.0.17763.0/um/x64/amstrmid.lib
31c3cd2c1bd990db5ba7d411fcfc9bc5  10.0.17763.0/um/x64/amsi.lib
75b39ebf93e6e6b4fa3004be73650079  10.0.17763.0/um/x64/ahadmin.lib
0ee7726a6aff180556af30a126379732  10.0.17763.0/um/x64/advpack.Lib
2eae76af1d12b6a7c8d475f589dddb38  10.0.17763.0/um/x64/api-ms-win-net-isolation-l1-1-0.lib
c72bfeb49e93646f88faf0817bc5b332  10.0.17763.0/um/x64/AdvAPI32.Lib
05ee6551b3d8c96959ff7d53e3ef96f9  10.0.17763.0/um/x64/ADSIid.Lib
77d4a983600e2e6913db53938e716153  10.0.17763.0/um/x64/AclUI.Lib
74077426011106ff312f27bebce752a9  10.0.17763.0/um/x64/ActiveDS.Lib
```


## .pat

pcf version:
```
COFF parser. Copyright (c) 1997-2019 Hex-Rays SA. Version 1.23
Usage: pcf [-switch or @file or $env_var] file [pattern-file]
        (wildcards are allowed)
```

### compiler: 14.16.27023

```
lib/x86/wsetargv.obj: skipped 1, total 1
lib/x86/vcruntimed.lib: skipped 80, total 81
lib/x86/vcruntime.lib: skipped 80, total 81
lib/x86/vcompd.lib: skipped 113, total 113
lib/x86/vcomp.lib: skipped 113, total 113
lib/x86/vccorlibd.lib: skipped 282, total 569
lib/x86/vccorlib.lib: skipped 285, total 560
lib/x86/vcampd.lib: skipped 166, total 166
lib/x86/vcamp.lib: skipped 165, total 165
lib/x86/threadlocale.obj: skipped 1, total 1
lib/x86/setargv.obj: skipped 1, total 1
lib/x86/pwsetargv.obj: skipped 0, total 1
lib/x86/ptrustud.lib: skipped 0, total 111
lib/x86/ptrustu.lib: skipped 0, total 111
lib/x86/ptrustmd.lib: skipped 0, total 186
lib/x86/ptrustm.lib: skipped 0, total 185
lib/x86/pthreadlocale.obj: skipped 0, total 1
lib/x86/psetargv.obj: skipped 0, total 1
lib/x86/pnothrownew.obj: skipped 0, total 8
lib/x86/pnoenv.obj: skipped 0, total 3
lib/x86/pnoarg.obj: skipped 0, total 3
lib/x86/pnewmode.obj: skipped 0, total 1
lib/x86/pinvalidcontinue.obj: skipped 0, total 4
lib/x86/pgort.lib: skipped 13, total 29
lib/x86/pgobootrun.lib: skipped 2, total 2
lib/x86/pcommode.obj: skipped 0, total 1
lib/x86/pbinmode.obj: skipped 0, total 1
lib/x86/oldnames.lib: skipped 228, total 228
lib/x86/nothrownew.obj: skipped 0, total 4
lib/x86/notelemetry.obj: skipped 4, total 4
lib/x86/noenv.obj: skipped 3, total 3
lib/x86/noarg.obj: skipped 3, total 3
lib/x86/newmode.obj: skipped 1, total 1
lib/x86/msvcurtd.lib: skipped 1879, total 32074
lib/x86/msvcurt.lib: skipped 1871, total 31213
lib/x86/msvcrtd.lib: skipped 276, total 740
lib/x86/msvcrt.lib: skipped 302, total 738
lib/x86/msvcprtd.lib: skipped 1574, total 1728
lib/x86/msvcprt.lib: skipped 1568, total 1708
lib/x86/msvcmrtd.lib: skipped 276, total 581
lib/x86/msvcmrt.lib: skipped 276, total 576
lib/x86/loosefpmath.obj: skipped 0, total 1
lib/x86/libvcruntimed.lib: skipped 0, total 462
lib/x86/libvcruntime.lib: skipped 20, total 461
lib/x86/libcpmtd1.lib: skipped 0, total 10816
lib/x86/libcpmtd0.lib: skipped 0, total 10193
lib/x86/libcpmtd.lib: skipped 0, total 10908
lib/x86/libcpmt1.lib: skipped 1200, total 10219
lib/x86/libcpmt.lib: skipped 1221, total 9594
lib/x86/libconcrtd1.lib: skipped 0, total 5771
lib/x86/libconcrtd0.lib: skipped 0, total 5771
lib/x86/libconcrtd.lib: skipped 0, total 5771
lib/x86/libconcrt1.lib: skipped 682, total 5564
lib/x86/libconcrt.lib: skipped 682, total 5564
lib/x86/libcmtd.lib: skipped 131, total 594
lib/x86/libcmt.lib: skipped 157, total 592
lib/x86/legacy_stdio_wide_specifiers.lib: skipped 0, total 3
lib/x86/legacy_stdio_definitions.lib: skipped 0, total 223
lib/x86/iso_stdio_wide_specifiers.lib: skipped 0, total 3
lib/x86/invalidcontinue.obj: skipped 1, total 2
lib/x86/fp10.obj: skipped 0, total 1
lib/x86/exe_initialize_mta.lib: skipped 0, total 1
lib/x86/delayimp.lib: skipped 0, total 34
lib/x86/concrtd.lib: skipped 291, total 291
lib/x86/concrt.lib: skipped 291, total 291
lib/x86/comsuppwd.lib: skipped 0, total 26
lib/x86/comsuppw.lib: skipped 0, total 26
lib/x86/comsuppd.lib: skipped 0, total 26
lib/x86/comsupp.lib: skipped 0, total 26
lib/x86/commode.obj: skipped 0, total 1
lib/x86/chkstk.obj: skipped 0, total 1
lib/x86/binmode.obj: skipped 0, total 1
lib/x86/aligned_new.lib: skipped 0, total 12
lib/x64/wsetargv.obj: skipped 0, total 1
lib/x64/vcruntimed.lib: skipped 71, total 71
lib/x64/vcruntime.lib: skipped 71, total 71
lib/x64/vcompd.lib: skipped 113, total 113
lib/x64/vcomp.lib: skipped 113, total 113
lib/x64/vccorlib.lib: skipped 289, total 568
lib/x64/vccorlibd.lib: skipped 282, total 573
lib/x64/vcampd.lib: skipped 166, total 166
lib/x64/vcamp.lib: skipped 165, total 165
lib/x64/threadlocale.obj: skipped 1, total 1
lib/x64/setargv.obj: skipped 0, total 1
lib/x64/pwsetargv.obj: skipped 0, total 1
lib/x64/ptrustud.lib: skipped 0, total 111
lib/x64/ptrustu.lib: skipped 0, total 111
lib/x64/ptrustmd.lib: skipped 0, total 186
lib/x64/ptrustm.lib: skipped 0, total 185
lib/x64/pthreadlocale.obj: skipped 0, total 1
lib/x64/psetargv.obj: skipped 0, total 1
lib/x64/pnothrownew.obj: skipped 0, total 8
lib/x64/pnoenv.obj: skipped 0, total 3
lib/x64/pnoarg.obj: skipped 0, total 3
lib/x64/pnewmode.obj: skipped 0, total 1
lib/x64/pinvalidcontinue.obj: skipped 0, total 4
lib/x64/pgort.lib: skipped 9, total 18
lib/x64/pgobootrun.lib: skipped 2, total 2
lib/x64/pcommode.obj: skipped 0, total 1
lib/x64/pbinmode.obj: skipped 0, total 1
lib/x64/oldnames.lib: skipped 228, total 228
lib/x64/nothrownew.obj: skipped 0, total 4
lib/x64/notelemetry.obj: skipped 4, total 4
lib/x64/noenv.obj: skipped 3, total 3
lib/x64/noarg.obj: skipped 3, total 3
lib/x64/newmode.obj: skipped 0, total 1
lib/x64/msvcurtd.lib: skipped 1868, total 32063
lib/x64/msvcurt.lib: skipped 1860, total 31202
lib/x64/msvcrtd.lib: skipped 291, total 728
lib/x64/msvcrt.lib: skipped 302, total 727
lib/x64/msvcprtd.lib: skipped 1575, total 1706
lib/x64/msvcprt.lib: skipped 1576, total 1690
lib/x64/msvcmrtd.lib: skipped 274, total 579
lib/x64/msvcmrt.lib: skipped 274, total 574
lib/x64/loosefpmath.obj: skipped 0, total 1
lib/x64/libvcruntimed.lib: skipped 3, total 555
lib/x64/libvcruntime.lib: skipped 31, total 550
lib/x64/libcpmtd1.lib: skipped 7, total 10859
lib/x64/libcpmtd0.lib: skipped 7, total 10210
lib/x64/libcpmtd.lib: skipped 7, total 10874
lib/x64/libcpmt1.lib: skipped 1604, total 10375
lib/x64/libcpmt.lib: skipped 1537, total 9769
lib/x64/libconcrtd1.lib: skipped 13, total 5686
lib/x64/libconcrtd0.lib: skipped 13, total 5686
lib/x64/libconcrtd.lib: skipped 13, total 5686
lib/x64/libconcrt1.lib: skipped 620, total 5502
lib/x64/libconcrt.lib: skipped 620, total 5502
lib/x64/libcmtd.lib: skipped 147, total 584
lib/x64/libcmt.lib: skipped 158, total 583
lib/x64/legacy_stdio_wide_specifiers.lib: skipped 0, total 3
lib/x64/legacy_stdio_definitions.lib: skipped 0, total 223
lib/x64/iso_stdio_wide_specifiers.lib: skipped 0, total 3
lib/x64/invalidcontinue.obj: skipped 1, total 2
lib/x64/exe_initialize_mta.lib: skipped 0, total 1
lib/x64/delayimp.lib: skipped 5, total 33
lib/x64/concrtd.lib: skipped 291, total 291
lib/x64/concrt.lib: skipped 291, total 291
lib/x64/comsuppwd.lib: skipped 0, total 28
lib/x64/comsuppw.lib: skipped 0, total 26
lib/x64/comsuppd.lib: skipped 0, total 28
lib/x64/comsupp.lib: skipped 0, total 26
lib/x64/commode.obj: skipped 0, total 1
lib/x64/chkstk.obj: skipped 0, total 1
lib/x64/binmode.obj: skipped 0, total 1
lib/x64/aligned_new.lib: skipped 0, total 12
atlmfc/lib/x64/uafxcwd.lib: skipped 2266, total 69582
atlmfc/lib/x64/uafxcw.lib: skipped 7733, total 63473
atlmfc/lib/x64/nafxcwd.lib: skipped 341, total 70535
atlmfc/lib/x64/nafxcw.lib: skipped 5816, total 62355
atlmfc/lib/x64/mfcs140ud.lib: skipped 36, total 1312
atlmfc/lib/x64/mfcs140u.lib: skipped 281, total 868
atlmfc/lib/x64/mfcs140d.lib: skipped 10, total 1356
atlmfc/lib/x64/mfcs140.lib: skipped 258, total 845
atlmfc/lib/x64/MFCM140Ud.lib: skipped 33, total 49
atlmfc/lib/x64/MFCM140U.lib: skipped 27, total 43
atlmfc/lib/x64/MFCM140d.lib: skipped 31, total 47
atlmfc/lib/x64/MFCM140.lib: skipped 25, total 41
atlmfc/lib/x64/mfc140ud.lib: skipped 20273, total 20273
atlmfc/lib/x86/uafxcwd.lib: skipped 2374, total 66977
atlmfc/lib/x64/mfc140u.lib: skipped 17345, total 17345
atlmfc/lib/x64/mfc140d.lib: skipped 17149, total 17149
atlmfc/lib/x86/uafxcw.lib: skipped 8464, total 61067
atlmfc/lib/x64/mfc140.lib: skipped 14638, total 14638
atlmfc/lib/x64/atls.lib: skipped 27, total 79
atlmfc/lib/x86/nafxcwd.lib: skipped 341, total 67614
atlmfc/lib/x64/afxnmcdd.lib: skipped 1, total 261
atlmfc/lib/x86/nafxcw.lib: skipped 6733, total 59840
atlmfc/lib/x64/afxnmcd.lib: skipped 42, total 148
atlmfc/lib/x86/mfcs140ud.lib: skipped 36, total 1354
atlmfc/lib/x86/mfcs140u.lib: skipped 98, total 903
atlmfc/lib/x86/mfcs140d.lib: skipped 10, total 1392
atlmfc/lib/x86/mfcs140.lib: skipped 75, total 880
atlmfc/lib/x86/MFCM140ud.lib: skipped 34, total 50
atlmfc/lib/x86/MFCM140u.lib: skipped 27, total 43
atlmfc/lib/x86/MFCM140d.lib: skipped 32, total 48
atlmfc/lib/x86/MFCM140.lib: skipped 25, total 41
atlmfc/lib/x86/mfc140ud.lib: skipped 20900, total 20900
atlmfc/lib/x86/mfc140u.lib: skipped 17936, total 17936
atlmfc/lib/x86/mfc140d.lib: skipped 17545, total 17545
atlmfc/lib/x86/mfc140.lib: skipped 14998, total 14998
atlmfc/lib/x86/atls.lib: skipped 4, total 1102
atlmfc/lib/x86/afxnmcdd.lib: skipped 0, total 264
atlmfc/lib/x86/afxnmcd.lib: skipped 20, total 152
```
### ucrt: 10.0.16299.0

```
um/x86/advpack.Lib: skipped 84, total 84
um/x86/AdvAPI32.Lib: skipped 782, total 782
um/x86/ADSIid.Lib: skipped 0, total 0
um/x86/ahadmin.lib: skipped 0, total 0
um/x86/amsi.lib: skipped 9, total 9
um/x86/amstrmid.lib: skipped 0, total 0
um/x86/BufferOverflow.lib: skipped 1, total 20
um/x64/d3d10_1.lib: skipped 29, total 29
um/x64/d3dcsxd.lib: skipped 9, total 9
um/x64/ddraw.lib: skipped 13, total 13
um/x64/devmgr.lib: skipped 19, total 19
um/x64/dwrite.lib: skipped 1, total 1
um/x64/dxguid.lib: skipped 0, total 0
um/x64/eappprxy.lib: skipped 18, total 18
um/x64/gdiplus.lib: skipped 630, total 630
um/x86/Credui.lib: skipped 22, total 22
um/x64/GPEdit.lib: skipped 10, total 10
um/x64/hbaapi.lib: skipped 93, total 93
um/x86/DhcpCSvc6.Lib: skipped 22, total 22
um/x86/dinput8.lib: skipped 1, total 2
um/x86/DnsAPI.Lib: skipped 270, total 270
um/x86/dnslib.lib: skipped 2, total 1288
um/x64/imgutil.Lib: skipped 9, total 9
um/x86/drt.lib: skipped 21, total 21
um/x64/Imm32.Lib: skipped 82, total 82
um/x64/inkobjcore.lib: skipped 30, total 30
um/x64/jsrt.lib: skipped 92, total 92
um/x86/drttransport.lib: skipped 2, total 2
um/x86/dsound.lib: skipped 10, total 10
um/x64/KSProxy.Lib: skipped 6, total 6
um/x64/LoadPerf.Lib: skipped 14, total 14
um/x64/mfplay.lib: skipped 1, total 1
um/x64/mfsensorgroup.lib: skipped 3, total 3
um/x86/dwmapi.lib: skipped 30, total 30
um/x64/mincore_downlevel.lib: skipped 451, total 451
um/x86/httpapi.lib: skipped 43, total 43
um/x86/Icmui.Lib: skipped 2, total 2
um/x86/icuuc.lib: skipped 2760, total 2760
um/x86/IEPMAPI.Lib: skipped 1, total 29
um/x64/MSAcm32.Lib: skipped 42, total 42
um/x86/mdmlocalmanagement.lib: skipped 3, total 3
um/x64/ScrnSavW.Lib: skipped 5, total 27
um/x64/SetupAPI.Lib: skipped 558, total 558
um/x64/rpcutil.lib: skipped 0, total 23
um/x64/shcore.lib: skipped 19, total 19
um/x64/shdocvw.lib: skipped 19, total 19
um/x86/MgmtAPI.Lib: skipped 9, total 9
um/x64/ShLwApi.Lib: skipped 365, total 365
um/x86/mincore_downlevel.lib: skipped 451, total 451
um/x64/ShFolder.Lib: skipped 2, total 2
um/x86/Mpr.Lib: skipped 43, total 43
um/x64/spoolss.lib: skipped 206, total 206
um/x64/SrClient.lib: skipped 5, total 35
um/x64/SnmpAPI.Lib: skipped 38, total 38
um/x86/MqRt.Lib: skipped 47, total 47
um/x64/strsafe.lib: skipped 0, total 23
um/x64/structuredquery.lib: skipped 0, total 0
um/x64/Svcguid.Lib: skipped 0, total 0
um/x64/swdevice.lib: skipped 9, total 9
um/x64/t2embed.lib: skipped 14, total 14
um/x86/msdasc.lib: skipped 0, total 0
um/x86/msdmo.lib: skipped 15, total 15
um/x64/taskschd.lib: skipped 0, total 0
um/x64/tdh.lib: skipped 24, total 24
um/x86/msdrm.lib: skipped 85, total 85
um/x86/MSImg32.Lib: skipped 3, total 3
um/x86/Msi.Lib: skipped 290, total 290
um/x86/mspbase.lib: skipped 164, total 1368
um/x64/tsec.lib: skipped 27, total 27
um/x86/MSTask.Lib: skipped 22, total 22
um/x64/twinapi.lib: skipped 0, total 0
um/x64/txfw32.lib: skipped 9, total 9
um/x86/MsXml2.Lib: skipped 0, total 0
um/x64/ualapi.lib: skipped 10, total 10
um/x86/Mtx.Lib: skipped 3, total 3
um/x64/Urlmon.Lib: skipped 95, total 95
um/x86/muiload.lib: skipped 1, total 69
um/x86/ncrypt.lib: skipped 129, total 129
um/x64/USP10.Lib: skipped 40, total 40
um/x64/Uxtheme.lib: skipped 78, total 78
um/x86/ndfapi.lib: skipped 24, total 24
um/x86/ndproxystub.lib: skipped 0, total 0
um/x64/Version.Lib: skipped 12, total 12
um/x64/Vfw32.Lib: skipped 127, total 127
um/x86/newdev.lib: skipped 23, total 23
um/x86/normaliz.lib: skipped 5, total 5
um/x86/ntdsa.lib: skipped 146, total 146
um/x86/NtDsAPI.Lib: skipped 120, total 120
um/x86/ntdsatq.lib: skipped 47, total 47
um/x86/ntfrsapi.lib: skipped 33, total 33
um/x86/NtQuery.Lib: skipped 44, total 44
um/x86/ntstc_msvcrt.lib: skipped 358, total 6200
um/x86/objsel.lib: skipped 0, total 0
um/x86/odbccp32.lib: skipped 1, total 61
um/x86/Ole32.Lib: skipped 432, total 432
um/x86/OleAut32.Lib: skipped 400, total 400
um/x86/oledb.lib: skipped 0, total 0
um/x86/OleDlg.Lib: skipped 23, total 23
um/x86/olesvr32.lib: skipped 23, total 23
um/x86/ondemandconnroutehelper.lib: skipped 8, total 8
um/x86/OlePro32.Lib: skipped 7, total 7
um/x86/OneCoreUAP.Lib: skipped 7884, total 7884
um/x86/OneCore.Lib: skipped 5011, total 5011
um/x86/OneCoreUAP_downlevel.Lib: skipped 4608, total 4608
um/x86/OpenGL32.Lib: skipped 368, total 368
um/x86/OneCore_downlevel.Lib: skipped 4608, total 4608
um/x86/osptk.lib: skipped 0, total 0
um/x86/p2pgraph.lib: skipped 40, total 40
um/x86/olecli32.lib: skipped 178, total 178
um/x86/pathcch.lib: skipped 22, total 22
um/x86/PeerDist.lib: skipped 28, total 28
um/x86/powrprof.lib: skipped 109, total 109
um/x86/prntvpt.lib: skipped 29, total 29
um/x86/Psapi.Lib: skipped 27, total 27
um/x86/qwave.lib: skipped 14, total 14
um/x86/RASAPI32.Lib: skipped 141, total 141
um/x86/rasuser.lib: skipped 5, total 5
um/x64/wcmapi.lib: skipped 37, total 37
um/x86/rometadata.lib: skipped 1, total 1
um/x86/resutils.lib: skipped 126, total 126
um/x64/wdsmc.lib: skipped 13, total 13
um/x64/wdsClientAPI.LIB: skipped 58, total 58
um/x64/wdstptc.lib: skipped 19, total 19
um/x86/rstrtmgr.lib: skipped 12, total 12
um/x86/rtutils.lib: skipped 41, total 41
um/x86/runtimeobject.lib: skipped 60, total 60
um/x64/wiaservc.lib: skipped 55, total 55
um/x86/sbtsv.lib: skipped 0, total 1
um/x86/ScrnSavW.Lib: skipped 1, total 24
um/x86/SearchSDK.lib: skipped 0, total 0
um/x86/SetupAPI.Lib: skipped 558, total 558
um/x86/ShFolder.Lib: skipped 2, total 2
um/x86/sens.lib: skipped 3, total 3
um/x64/WinMM.Lib: skipped 179, total 179
um/x86/structuredquery.lib: skipped 0, total 0
um/x86/Svcguid.Lib: skipped 0, total 0
um/x86/strsafe.lib: skipped 0, total 22
um/x86/strmiids.lib: skipped 0, total 0
um/x86/strmbase.lib: skipped 156, total 1689
um/x86/Sti.Lib: skipped 16, total 16
um/x86/ssdpapi.lib: skipped 29, total 29
um/x86/srpapi.lib: skipped 21, total 21
um/x86/SrClient.lib: skipped 1, total 33
um/x86/SpOrder.Lib: skipped 2, total 2
um/x86/spoolss.lib: skipped 206, total 206
um/x86/SnmpAPI.Lib: skipped 38, total 38
um/x86/slwga.lib: skipped 1, total 1
um/x86/slcext.lib: skipped 9, total 9
um/x86/slc.lib: skipped 41, total 41
um/x86/ShLwApi.Lib: skipped 365, total 365
um/x86/shell32.lib: skipped 399, total 399
um/x86/shdocvw.lib: skipped 19, total 19
um/x64/wlanui.lib: skipped 5, total 5
um/x64/wmcodecdspuuid.lib: skipped 0, total 0
um/x64/wmiutils.lib: skipped 0, total 0
um/x64/wnvapi.lib: skipped 2, total 2
um/x86/synchronization.lib: skipped 3, total 3
um/x64/wofutil.lib: skipped 11, total 11
um/x86/t2embed.lib: skipped 14, total 14
um/x86/tbs.lib: skipped 19, total 19
um/x86/tokenbinding.lib: skipped 8, total 8
um/x86/UIAutomationCore.lib: skipped 100, total 100
um/x86/USP10.Lib: skipped 40, total 40
um/x86/vssapi.lib: skipped 46, total 46
um/x86/wdsmc.lib: skipped 13, total 13
um/x86/wdspxe.lib: skipped 32, total 32
um/x86/wdsbp.lib: skipped 7, total 7
um/x86/wdsClientAPI.LIB: skipped 58, total 58
um/x86/WebServices.lib: skipped 193, total 193
um/x86/websocket.lib: skipped 13, total 13
um/x86/wecapi.lib: skipped 17, total 17
um/x86/wdstptc.lib: skipped 19, total 19
um/x86/wevtapi.lib: skipped 45, total 45
um/x86/WiaGuid.Lib: skipped 0, total 0
um/x86/wiautil.lib: skipped 4, total 133
um/x86/windows.networking.lib: skipped 1, total 1
um/x86/WinTrust.Lib: skipped 143, total 143
um/x86/wlanapi.lib: skipped 64, total 64
um/x86/wmiutils.lib: skipped 0, total 0
um/x86/wofutil.lib: skipped 11, total 11
um/x86/Wow32.Lib: skipped 28, total 28
um/x86/wscapi.lib: skipped 39, total 39
um/x86/wsdapi.lib: skipped 45, total 45
um/x86/WSock32.Lib: skipped 75, total 75
um/x86/wlanui.lib: skipped 5, total 5
um/x86/xmllite.lib: skipped 6, total 6
um/x86/xolehlp.lib: skipped 8, total 8
um/x86/xpsprint.lib: skipped 4, total 4
um/x86/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x86/xinputuap.lib: skipped 8, total 8
um/x86/Xinput9_1_0.lib: skipped 5, total 5
um/x86/xinput.lib: skipped 8, total 8
um/x86/xaudio2_8.lib: skipped 6, total 6
um/x86/xaudio2.lib: skipped 7, total 7
um/x86/xaswitch.lib: skipped 1, total 22
um/x86/xapobase2_8.lib: skipped 4, total 133
um/x86/xapobase.lib: skipped 4, total 157
um/x86/wuguid.lib: skipped 0, total 0
um/x86/WtsApi32.Lib: skipped 65, total 65
um/x86/wsmsvc.lib: skipped 3672, total 3672
um/x86/wsclient.lib: skipped 30, total 30
um/x86/wsbonline.lib: skipped 3, total 3
um/x86/wsbapp_uuid.Lib: skipped 0, total 0
um/x86/WS2_32.Lib: skipped 180, total 180
um/x86/WSnmp32.Lib: skipped 51, total 51
um/x86/workspaceax.lib: skipped 0, total 3
um/x86/wmvcore.lib: skipped 20, total 20
um/x86/wmip.lib: skipped 45, total 45
um/x86/wmcodecdspuuid.lib: skipped 0, total 0
um/x86/Wldap32.Lib: skipped 245, total 245
um/x86/winusb.lib: skipped 37, total 37
um/x86/WinStrm.Lib: skipped 0, total 18
um/x86/winsta.lib: skipped 167, total 167
um/x86/winsqlite3.lib: skipped 238, total 238
um/x86/WinSpool.Lib: skipped 232, total 232
um/x86/winscard.lib: skipped 74, total 74
um/x86/winsatapi.lib: skipped 0, total 0
um/x86/WinMM.Lib: skipped 191, total 191
um/x86/WinInet.Lib: skipped 318, total 318
um/x86/winhttp.lib: skipped 63, total 63
um/x86/winfax.lib: skipped 56, total 56
um/x86/windowssideshowguids.lib: skipped 0, total 0
um/x86/windowscodecs.lib: skipped 114, total 114
um/x86/WindowsApp_downlevel.lib: skipped 2551, total 2551
um/x86/WindowsApp.lib: skipped 3117, total 3117
um/x86/windows.ui.lib: skipped 2, total 2
um/x86/windows.data.pdf.lib: skipped 1, total 1
um/x86/wiaservc.lib: skipped 55, total 55
um/x86/WinBio.lib: skipped 60, total 60
um/x86/Wer.lib: skipped 146, total 146
um/x86/wcmguid.lib: skipped 0, total 0
um/x86/wcmapi.lib: skipped 37, total 37
um/x86/wbemuuid.lib: skipped 0, total 0
um/x86/vstorinterface.lib: skipped 15, total 15
um/x86/vss_uuid.lib: skipped 0, total 0
um/x86/vscmgr.lib: skipped 0, total 0
um/x86/Virtdisk.Lib: skipped 27, total 27
um/x86/Vfw32.Lib: skipped 127, total 127
um/x86/Version.Lib: skipped 12, total 12
um/x86/vds_uuid.lib: skipped 0, total 0
um/x86/VdmDbg.Lib: skipped 28, total 28
um/x86/vccomsup.lib: skipped 1, total 31
um/x86/Uxtheme.lib: skipped 78, total 78
um/x86/Uuid.Lib: skipped 0, total 0
um/x86/UserEnv.Lib: skipped 72, total 72
um/x86/User32.Lib: skipped 762, total 762
um/x86/Urlmon.Lib: skipped 95, total 95
um/x86/unicows.lib: skipped 1011, total 2540
um/x86/umpdddi.lib: skipped 92, total 92
um/x86/ualapi.lib: skipped 10, total 10
um/x86/txfw32.lib: skipped 9, total 9
um/x64/xpsprint.lib: skipped 4, total 4
um/x64/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x86/twinapi.lib: skipped 0, total 0
um/x86/twain_32.lib: skipped 5, total 5
um/x86/tspubplugincom.lib: skipped 1, total 8
um/x64/xolehlp.lib: skipped 8, total 8
um/x86/tsec.lib: skipped 27, total 27
um/x86/TranscodeImageUID.lib: skipped 0, total 0
um/x64/xmllite.lib: skipped 6, total 6
um/x64/xinputuap.lib: skipped 8, total 8
um/x64/Xinput9_1_0.lib: skipped 5, total 5
um/x64/xinput.lib: skipped 8, total 8
um/x64/xaudio2_8.lib: skipped 6, total 6
um/x64/xaudio2.lib: skipped 7, total 7
um/x64/xaswitch.lib: skipped 5, total 24
um/x64/xapobase2_8.lib: skipped 10, total 119
um/x64/xapobase.lib: skipped 10, total 157
um/x64/wuguid.lib: skipped 0, total 0
um/x64/WtsApi32.Lib: skipped 65, total 65
um/x64/WSock32.Lib: skipped 75, total 75
um/x64/WSnmp32.Lib: skipped 51, total 51
um/x64/wsmsvc.lib: skipped 3672, total 3672
um/x64/wsdapi.lib: skipped 45, total 45
um/x64/wsclient.lib: skipped 30, total 30
um/x64/wscapi.lib: skipped 39, total 39
um/x64/wsbapp_uuid.Lib: skipped 0, total 0
um/x64/wsbonline.lib: skipped 3, total 3
um/x64/WS2_32.Lib: skipped 195, total 195
um/x64/workspaceax.lib: skipped 0, total 3
um/x86/Traffic.Lib: skipped 22, total 22
um/x86/Thunk32.Lib: skipped 66, total 66
um/x86/taskschd.lib: skipped 0, total 0
um/x86/tdh.lib: skipped 24, total 24
um/x86/tapi32l.lib: skipped 1, total 255
um/x86/Tapi32.Lib: skipped 278, total 278
um/x64/wmvcore.lib: skipped 20, total 20
um/x86/swdevice.lib: skipped 9, total 9
um/x64/wmip.lib: skipped 45, total 45
um/x64/Wldap32.Lib: skipped 245, total 245
um/x64/wlanapi.lib: skipped 64, total 64
um/x64/winusb.lib: skipped 37, total 37
um/x64/WinTrust.Lib: skipped 143, total 143
um/x64/WinStrm.Lib: skipped 0, total 18
um/x64/winsta.lib: skipped 167, total 167
um/x64/winsqlite3.lib: skipped 238, total 238
um/x64/WinSpool.Lib: skipped 232, total 232
um/x64/winscard.lib: skipped 74, total 74
um/x64/winsatapi.lib: skipped 0, total 0
um/x86/shcore.lib: skipped 19, total 19
um/x86/Sfc.Lib: skipped 16, total 16
um/x86/SensorsUtils.lib: skipped 58, total 58
um/x86/sensorsapi.lib: skipped 0, total 0
um/x86/SensAPI.Lib: skipped 3, total 3
um/x64/WinInet.Lib: skipped 318, total 318
um/x64/winhttp.lib: skipped 63, total 63
um/x86/security.lib: skipped 36, total 36
um/x64/winfax.lib: skipped 56, total 56
um/x86/Secur32.Lib: skipped 96, total 96
um/x64/windowssideshowguids.lib: skipped 0, total 0
um/x64/windowscodecs.lib: skipped 114, total 114
um/x64/WindowsApp_downlevel.lib: skipped 2564, total 2564
um/x64/WindowsApp.lib: skipped 3134, total 3134
um/x86/ScrnSave.Lib: skipped 1, total 24
um/x86/schannel.lib: skipped 35, total 35
um/x64/windows.ui.lib: skipped 2, total 2
um/x86/scecli.lib: skipped 71, total 71
um/x86/scesrv.lib: skipped 2, total 2
um/x64/windows.data.pdf.lib: skipped 1, total 1
um/x64/windows.networking.lib: skipped 1, total 1
um/x86/SCardDlg.Lib: skipped 5, total 5
um/x64/WinBio.lib: skipped 60, total 60
um/x64/wiautil.lib: skipped 8, total 135
um/x86/sas.lib: skipped 1, total 1
um/x86/SAPI.Lib: skipped 0, total 0
um/x86/samsrv.lib: skipped 325, total 325
um/x64/WiaGuid.Lib: skipped 0, total 0
um/x64/wevtapi.lib: skipped 45, total 45
um/x86/samlib.lib: skipped 70, total 70
um/x64/Wer.lib: skipped 146, total 146
um/x86/RTWorkQ.lib: skipped 34, total 34
um/x64/wecapi.lib: skipped 17, total 17
um/x64/websocket.lib: skipped 13, total 13
um/x86/Rtm.Lib: skipped 116, total 116
um/x64/WebServices.lib: skipped 193, total 193
um/x86/rpcutil.lib: skipped 0, total 23
um/x86/RpcRT4.Lib: skipped 534, total 534
um/x64/wdspxe.lib: skipped 32, total 32
um/x86/rpcproxy.lib: skipped 5, total 5
um/x86/Rpcns4.Lib: skipped 62, total 62
um/x86/rpcexts.lib: skipped 58, total 58
um/x64/wdsbp.lib: skipped 7, total 7
um/x64/wcmguid.lib: skipped 0, total 0
um/x64/wbemuuid.lib: skipped 0, total 0
um/x86/RASDlg.Lib: skipped 24, total 24
um/x86/quartz.lib: skipped 4, total 4
um/x86/query.lib: skipped 44, total 44
um/x86/propsys.lib: skipped 219, total 219
um/x86/PortableDeviceGuids.lib: skipped 0, total 0
um/x86/PhotoAcquireUID.lib: skipped 0, total 0
um/x86/patchwiz.lib: skipped 4, total 4
um/x86/Pdh.Lib: skipped 110, total 110
um/x86/OleAcc.Lib: skipped 20, total 20
um/x86/p2p.lib: skipped 112, total 112
um/x86/OemLicense.lib: skipped 6, total 6
um/x86/odbcbcp.lib: skipped 28, total 28
um/x86/odbc32.lib: skipped 176, total 176
um/x86/ntvdm.lib: skipped 162, total 162
um/x86/ntstc_libcmt.lib: skipped 358, total 6200
um/x86/ntmarta.lib: skipped 44, total 44
um/x86/ntlanman.lib: skipped 23, total 23
um/x86/ntdsetup.lib: skipped 24, total 24
um/x86/ntdll.lib: skipped 2031, total 2031
um/x86/nt.lib: skipped 0, total 6
um/x64/vstorinterface.lib: skipped 15, total 15
um/x64/vss_uuid.lib: skipped 0, total 0
um/x64/vssapi.lib: skipped 46, total 46
um/x64/vscmgr.lib: skipped 0, total 0
um/x86/ninput.lib: skipped 23, total 23
um/x86/NetSh.Lib: skipped 23, total 23
um/x64/Virtdisk.Lib: skipped 27, total 27
um/x86/netlib.lib: skipped 2, total 274
um/x64/vertdll.lib: skipped 90, total 93
um/x64/vds_uuid.lib: skipped 0, total 0
um/x86/NetAPI32.Lib: skipped 212, total 212
um/x64/vccomsup.lib: skipped 5, total 33
um/x86/nddeapi.lib: skipped 28, total 28
um/x64/Uuid.Lib: skipped 0, total 0
um/x64/UserEnv.Lib: skipped 72, total 72
um/x64/User32.Lib: skipped 770, total 770
um/x64/umpdddi.lib: skipped 92, total 92
um/x86/mtxdm.lib: skipped 1, total 1
um/x64/UIAutomationCore.lib: skipped 100, total 100
um/x86/msxml6.lib: skipped 0, total 0
um/x86/MsWSock.Lib: skipped 28, total 28
um/x86/msvfw32.Lib: skipped 47, total 47
um/x86/msv1_0.lib: skipped 19, total 19
um/x86/MSRating.Lib: skipped 32, total 32
um/x64/tspubplugincom.lib: skipped 1, total 8
um/x86/msports.lib: skipped 11, total 11
um/x86/mspatchc.lib: skipped 14, total 14
um/x64/TranscodeImageUID.lib: skipped 0, total 0
um/x86/mspatcha.lib: skipped 16, total 16
um/x64/Traffic.Lib: skipped 22, total 22
um/x64/tokenbinding.lib: skipped 8, total 8
um/x64/tbs.lib: skipped 19, total 19
um/x86/msdelta.lib: skipped 15, total 15
um/x64/Tapi32.Lib: skipped 278, total 278
um/x64/tapi32l.lib: skipped 5, total 257
um/x86/MsCtfMonitor.lib: skipped 3, total 3
um/x86/Mscms.Lib: skipped 111, total 111
um/x64/synchronization.lib: skipped 3, total 3
um/x86/MSAJApi.lib: skipped 558, total 558
um/x86/msaatext.lib: skipped 0, total 0
um/x86/MSAcm32.Lib: skipped 44, total 44
um/x64/strmiids.lib: skipped 0, total 0
um/x64/strmbase.lib: skipped 140, total 1688
um/x86/MrmSupport.lib: skipped 4, total 4
um/x64/Sti.Lib: skipped 16, total 16
um/x64/ssdpapi.lib: skipped 29, total 29
um/x64/srpapi.lib: skipped 21, total 21
um/x86/MqOA.Lib: skipped 0, total 0
um/x64/SpOrder.Lib: skipped 2, total 2
um/x86/mprsnap.lib: skipped 46, total 46
um/x86/Mprapi.Lib: skipped 160, total 160
um/x64/slwga.lib: skipped 1, total 1
um/x64/slcext.lib: skipped 9, total 9
um/x86/mmdevapi.lib: skipped 29, total 29
um/x64/slc.lib: skipped 41, total 41
um/x86/MMC.Lib: skipped 1, total 16
um/x86/mincore.lib: skipped 4278, total 4278
um/x86/mi.lib: skipped 2, total 2
um/x64/shell32.lib: skipped 399, total 399
um/x86/mfuuid.lib: skipped 0, total 0
um/x64/Sfc.Lib: skipped 16, total 16
um/x64/SensorsUtils.lib: skipped 58, total 58
um/x64/sensorsapi.lib: skipped 0, total 0
um/x64/SensAPI.Lib: skipped 3, total 3
um/x86/Mfsrcsnk.lib: skipped 2, total 2
um/x64/sens.lib: skipped 3, total 3
um/x86/mfsensorgroup.lib: skipped 3, total 3
um/x64/security.lib: skipped 36, total 36
um/x86/mfreadwrite.lib: skipped 5, total 5
um/x64/Secur32.Lib: skipped 96, total 96
um/x86/mfplay.lib: skipped 1, total 1
um/x64/SearchSDK.lib: skipped 0, total 0
um/x64/ScrnSave.Lib: skipped 5, total 27
um/x64/schannel.lib: skipped 35, total 35
um/x64/scecli.lib: skipped 71, total 71
um/x64/scesrv.lib: skipped 2, total 2
um/x64/SCardDlg.Lib: skipped 5, total 5
um/x64/sbtsv.lib: skipped 0, total 1
um/x64/sas.lib: skipped 1, total 1
um/x64/SAPI.Lib: skipped 0, total 0
um/x64/samsrv.lib: skipped 325, total 325
um/x64/samlib.lib: skipped 70, total 70
um/x64/runtimeobject.lib: skipped 64, total 64
um/x64/RTWorkQ.lib: skipped 34, total 34
um/x64/rtutils.lib: skipped 41, total 41
um/x64/Rtm.Lib: skipped 116, total 116
um/x64/rstrtmgr.lib: skipped 12, total 12
um/x64/RpcRT4.Lib: skipped 541, total 541
um/x64/rpcproxy.lib: skipped 5, total 5
um/x64/Rpcns4.Lib: skipped 62, total 62
um/x64/rpcexts.lib: skipped 58, total 58
um/x64/rometadata.lib: skipped 1, total 1
um/x64/resutils.lib: skipped 126, total 126
um/x64/RASDlg.Lib: skipped 24, total 24
um/x64/rasuser.lib: skipped 5, total 5
um/x86/Mfplat.lib: skipped 150, total 150
um/x64/RASAPI32.Lib: skipped 141, total 141
um/x64/qwave.lib: skipped 14, total 14
um/x64/query.lib: skipped 44, total 44
um/x64/quartz.lib: skipped 4, total 4
um/x64/Psapi.Lib: skipped 27, total 27
um/x64/propsys.lib: skipped 219, total 219
um/x64/prntvpt.lib: skipped 29, total 29
um/x64/powrprof.lib: skipped 109, total 109
um/x64/PortableDeviceGuids.lib: skipped 0, total 0
um/x64/PhotoAcquireUID.lib: skipped 0, total 0
um/x64/PeerDist.lib: skipped 28, total 28
um/x64/Pdh.Lib: skipped 110, total 110
um/x64/pathcch.lib: skipped 22, total 22
um/x64/p2pgraph.lib: skipped 40, total 40
um/x64/p2p.lib: skipped 112, total 112
um/x64/osptk.lib: skipped 0, total 0
um/x64/opmxbox.Lib: skipped 3, total 3
um/x64/OpenGL32.Lib: skipped 368, total 368
um/x64/OneCore_downlevel.Lib: skipped 4673, total 4673
um/x64/OneCoreUAP_downlevel.Lib: skipped 4673, total 4673
um/x64/OneCoreUAP.Lib: skipped 7926, total 7926
um/x64/OneCore.Lib: skipped 5053, total 5053
um/x64/olesvr32.lib: skipped 23, total 23
um/x64/OleDlg.Lib: skipped 23, total 23
um/x64/oledb.lib: skipped 0, total 0
um/x64/ondemandconnroutehelper.lib: skipped 8, total 8
um/x64/olecli32.lib: skipped 178, total 178
um/x64/OleAcc.Lib: skipped 20, total 20
um/x64/OleAut32.Lib: skipped 412, total 412
um/x64/Ole32.Lib: skipped 504, total 504
um/x64/OemLicense.lib: skipped 6, total 6
um/x64/odbcbcp.lib: skipped 28, total 28
um/x64/odbccp32.lib: skipped 5, total 63
um/x64/odbc32.lib: skipped 176, total 176
um/x64/ntstc_msvcrt.lib: skipped 370, total 6197
um/x64/objsel.lib: skipped 0, total 0
um/x64/ntstc_libcmt.lib: skipped 370, total 6197
um/x64/ntmarta.lib: skipped 44, total 44
um/x64/NtQuery.Lib: skipped 44, total 44
um/x64/ntlanman.lib: skipped 23, total 23
um/x64/ntfrsapi.lib: skipped 33, total 33
um/x64/ntdsetup.lib: skipped 24, total 24
um/x64/ntdsatq.lib: skipped 47, total 47
um/x64/NtDsAPI.Lib: skipped 120, total 120
um/x64/ntdsa.lib: skipped 146, total 146
um/x64/ntdll.lib: skipped 2052, total 2052
um/x64/nt.lib: skipped 0, total 6
um/x64/normaliz.lib: skipped 5, total 5
um/x64/ninput.lib: skipped 23, total 23
um/x64/newdev.lib: skipped 23, total 23
um/x64/NetSh.Lib: skipped 23, total 23
um/x64/netlib.lib: skipped 8, total 276
um/x64/NetAPI32.Lib: skipped 212, total 212
um/x64/ndproxystub.lib: skipped 0, total 0
um/x64/ndfapi.lib: skipped 24, total 24
um/x64/nddeapi.lib: skipped 28, total 28
um/x64/ncrypt.lib: skipped 129, total 129
um/x64/nanosrv.lib: skipped 7064, total 7064
um/x64/mtxdm.lib: skipped 1, total 1
um/x64/muiload.lib: skipped 5, total 71
um/x86/Mfcore.lib: skipped 36, total 36
um/x86/Mf.lib: skipped 75, total 75
um/x86/MDMRegistration.lib: skipped 12, total 12
um/x64/Mtx.Lib: skipped 3, total 3
um/x64/msxml6.lib: skipped 0, total 0
um/x64/MsXml2.Lib: skipped 0, total 0
um/x86/mciole32.lib: skipped 11, total 11
um/x86/mbnapi_uuid.lib: skipped 0, total 0
um/x64/MsWSock.Lib: skipped 28, total 28
um/x86/MAPI32.Lib: skipped 155, total 155
um/x64/msvfw32.Lib: skipped 47, total 47
um/x86/magnification.lib: skipped 21, total 21
um/x64/msv1_0.lib: skipped 19, total 19
um/x86/Lz32.Lib: skipped 14, total 14
um/x64/MSTask.Lib: skipped 11, total 11
um/x86/locationapi.lib: skipped 0, total 0
um/x86/LoadPerf.Lib: skipped 14, total 14
um/x64/MSRating.Lib: skipped 32, total 32
um/x64/msports.lib: skipped 11, total 11
um/x64/mspbase.lib: skipped 175, total 1391
um/x86/ktmw32.lib: skipped 44, total 44
um/x86/ksuser.lib: skipped 8, total 8
um/x86/KSProxy.Lib: skipped 6, total 6
um/x64/mspatchc.lib: skipped 14, total 14
um/x64/mspatcha.lib: skipped 16, total 16
um/x64/MSImg32.Lib: skipped 3, total 3
um/x86/kernel32legacylib.lib: skipped 6, total 540
um/x86/kernel32.Lib: skipped 1309, total 1309
um/x64/Msi.Lib: skipped 290, total 290
um/x86/kerbcli.lib: skipped 0, total 3
um/x86/jsrt.lib: skipped 92, total 92
um/x64/msdrm.lib: skipped 85, total 85
um/x86/jetoledb.lib: skipped 0, total 0
um/x64/msdmo.lib: skipped 15, total 15
um/x86/iscsidsc.lib: skipped 80, total 80
um/x64/msdelta.lib: skipped 15, total 15
um/x86/irprops.lib: skipped 35, total 35
um/x64/msdasc.lib: skipped 0, total 0
um/x86/Iprop.Lib: skipped 8, total 8
um/x86/iphlpapi.lib: skipped 279, total 279
um/x64/MsCtfMonitor.lib: skipped 3, total 3
um/x64/Mscms.Lib: skipped 111, total 111
um/x86/int64.lib: skipped 0, total 11
um/x86/inseng.lib: skipped 7, total 7
um/x86/inkobjcore.lib: skipped 30, total 30
um/x86/infocardapi.Lib: skipped 18, total 18
um/x86/Imm32.Lib: skipped 82, total 82
um/x64/MSAJApi.lib: skipped 558, total 558
um/x86/imgutil.Lib: skipped 9, total 9
um/x86/ImageHlp.Lib: skipped 150, total 150
um/x86/iesetup.lib: skipped 7, total 7
um/x86/icuin.Lib: skipped 4475, total 4475
um/x86/Icm32.Lib: skipped 21, total 21
um/x86/iashlpr.lib: skipped 12, total 12
um/x86/Htmlhelp.Lib: skipped 1, total 11
um/x86/hrtfapo.lib: skipped 4, total 4
um/x86/HLink.Lib: skipped 28, total 28
um/x86/hid.lib: skipped 44, total 44
um/x86/hhsetup.lib: skipped 145, total 145
um/x86/hbaapi.lib: skipped 93, total 93
um/x86/GPEdit.lib: skipped 10, total 10
um/x86/gpmuuid.lib: skipped 0, total 0
um/x86/GlU32.Lib: skipped 52, total 52
um/x86/gdiplus.lib: skipped 630, total 630
um/x86/glmf32.lib: skipped 134, total 134
um/x86/Gdi32.Lib: skipped 592, total 592
um/x86/fwpuclnt.lib: skipped 272, total 272
um/x86/fxsutility.lib: skipped 2, total 2
um/x86/FrameDyn.Lib: skipped 604, total 604
um/x86/FrameDyd.Lib: skipped 606, total 606
um/x86/fontsub.lib: skipped 2, total 2
um/x86/fltLib.lib: skipped 29, total 29
um/x86/fileextd.lib: skipped 1, total 22
um/x86/FhSvcCtl.lib: skipped 14, total 14
um/x86/feclient.lib: skipped 45, total 45
um/x64/msaatext.lib: skipped 0, total 0
um/x86/FaultRep.Lib: skipped 14, total 14
um/x64/MrmSupport.lib: skipped 4, total 4
um/x64/MqRt.Lib: skipped 47, total 47
um/x86/evr.lib: skipped 9, total 9
um/x86/esent.lib: skipped 369, total 369
um/x86/ElsCore.lib: skipped 5, total 5
um/x86/els.lib: skipped 0, total 0
um/x86/elfapi.lib: skipped 0, total 65
um/x64/MqOA.Lib: skipped 0, total 0
um/x64/mprsnap.lib: skipped 46, total 46
um/x86/ehstorguids.lib: skipped 0, total 0
um/x64/Mprapi.Lib: skipped 160, total 160
um/x64/Mpr.Lib: skipped 43, total 43
um/x86/efswrt.lib: skipped 18, total 18
um/x64/mmdevapi.lib: skipped 29, total 29
um/x64/MMC.Lib: skipped 5, total 18
um/x86/easregprov.lib: skipped 2, total 2
um/x86/eappprxy.lib: skipped 18, total 18
um/x86/eappcfg.lib: skipped 15, total 15
um/x64/mincore.lib: skipped 4320, total 4320
um/x86/dxva2.lib: skipped 38, total 38
um/x64/mi.lib: skipped 2, total 2
um/x86/dxtrans.lib: skipped 6, total 6
um/x86/dxtmsft.lib: skipped 0, total 0
um/x86/dxguid.lib: skipped 0, total 0
um/x64/MgmtAPI.Lib: skipped 9, total 9
um/x86/dxgi.lib: skipped 14, total 14
um/x64/mfuuid.lib: skipped 0, total 0
um/x86/dwrite.lib: skipped 1, total 1
um/x86/DtcHelp.Lib: skipped 3, total 23
um/x64/Mfsrcsnk.lib: skipped 2, total 2
um/x64/mfreadwrite.lib: skipped 5, total 5
um/x64/Mfplat.lib: skipped 150, total 150
um/x64/Mfcore.lib: skipped 36, total 36
um/x64/Mf.lib: skipped 75, total 75
um/x64/MDMRegistration.lib: skipped 12, total 12
um/x64/mdmlocalmanagement.lib: skipped 3, total 3
um/x86/DSUIExt.Lib: skipped 33, total 33
um/x64/mciole32.lib: skipped 11, total 11
um/x64/mbnapi_uuid.lib: skipped 0, total 0
um/x64/MAPI32.Lib: skipped 136, total 136
um/x64/magnification.lib: skipped 21, total 21
um/x64/Lz32.Lib: skipped 14, total 14
um/x64/locationapi.lib: skipped 0, total 0
um/x86/dststlog.lib: skipped 1, total 1
um/x64/ktmw32.lib: skipped 44, total 44
um/x64/ksuser.lib: skipped 8, total 8
um/x86/dssec.lib: skipped 4, total 4
um/x86/DSProp.Lib: skipped 19, total 19
um/x64/kernel32legacylib.lib: skipped 14, total 600
um/x64/kernel32.Lib: skipped 1335, total 1335
um/x64/kerbcli.lib: skipped 0, total 3
um/x86/drtprov.lib: skipped 9, total 9
um/x64/iscsidsc.lib: skipped 80, total 80
um/x64/irprops.lib: skipped 35, total 35
um/x64/Iprop.Lib: skipped 8, total 8
um/x64/iphlpapi.lib: skipped 279, total 279
um/x64/inseng.lib: skipped 7, total 7
um/x64/infocardapi.Lib: skipped 18, total 18
um/x86/dpx.lib: skipped 5, total 5
um/x86/dnsrslvr.lib: skipped 4, total 4
um/x86/dnsrpc.lib: skipped 1, total 379
um/x86/dnsperf.lib: skipped 3, total 3
um/x86/dnscrcli.lib: skipped 0, total 4
um/x86/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x86/dmoguids.lib: skipped 0, total 0
um/x86/dloadhelper.lib: skipped 0, total 3
um/x86/difxapi.lib: skipped 12, total 12
um/x86/dhcpsapi.lib: skipped 209, total 209
um/x86/DhcpCSvc.Lib: skipped 67, total 67
um/x86/dflayout.lib: skipped 1, total 1
um/x86/devmgr.lib: skipped 19, total 19
um/x86/deviceaccess.lib: skipped 3, total 3
um/x86/devenum.lib: skipped 0, total 0
um/x86/ddraw.lib: skipped 13, total 13
um/x86/dcomp.lib: skipped 6, total 6
um/x86/dciman32.lib: skipped 20, total 20
um/x86/DbgHelp.Lib: skipped 237, total 237
um/x86/DbgEng.Lib: skipped 4, total 4
um/x86/davclnt.lib: skipped 22, total 22
um/x86/d3dcsxd.lib: skipped 9, total 9
um/x64/ImageHlp.Lib: skipped 147, total 147
um/x86/d3dcsx.lib: skipped 9, total 9
um/x86/d3dcompiler.lib: skipped 29, total 29
um/x64/iesetup.lib: skipped 7, total 7
um/x86/d3d9.lib: skipped 14, total 14
um/x64/IEPMAPI.Lib: skipped 5, total 31
um/x64/icuuc.lib: skipped 2760, total 2760
um/x86/d3d12.lib: skipped 10, total 10
um/x64/icuin.Lib: skipped 4475, total 4475
um/x86/d3d11.lib: skipped 45, total 45
um/x86/d3d10_1.lib: skipped 29, total 29
um/x64/Icmui.Lib: skipped 2, total 2
um/x64/Icm32.Lib: skipped 21, total 21
um/x86/d3d10.lib: skipped 29, total 29
um/x64/iashlpr.lib: skipped 12, total 12
um/x86/d2d1.lib: skipped 13, total 13
um/x64/httpapi.lib: skipped 43, total 43
um/x86/cscdll.lib: skipped 18, total 18
um/x64/Htmlhelp.Lib: skipped 5, total 13
um/x86/cscapi.lib: skipped 6, total 6
um/x64/hrtfapo.lib: skipped 4, total 4
um/x86/cryptxml.lib: skipped 19, total 19
um/x64/HLink.Lib: skipped 28, total 28
um/x86/cryptui.lib: skipped 54, total 54
um/x64/hid.lib: skipped 44, total 44
um/x86/CryptNet.Lib: skipped 5, total 5
um/x64/hhsetup.lib: skipped 145, total 145
um/x86/cryptdll.lib: skipped 20, total 20
um/x64/gpmuuid.lib: skipped 0, total 0
um/x86/Crypt32.Lib: skipped 240, total 240
um/x64/GlU32.Lib: skipped 52, total 52
um/x64/glmf32.lib: skipped 134, total 134
um/x64/Gdi32.Lib: skipped 592, total 592
um/x64/fxsutility.lib: skipped 2, total 2
um/x64/fwpuclnt.lib: skipped 272, total 272
um/x64/FrameDyn.Lib: skipped 604, total 604
um/x64/FrameDyd.Lib: skipped 606, total 606
um/x64/fontsub.lib: skipped 2, total 2
um/x64/fltLib.lib: skipped 29, total 29
um/x64/fileextd.lib: skipped 5, total 22
um/x64/FhSvcCtl.lib: skipped 14, total 14
um/x64/feclient.lib: skipped 45, total 45
um/x64/FaultRep.Lib: skipped 14, total 14
um/x64/evr.lib: skipped 9, total 9
um/x86/corrEngine.lib: skipped 0, total 0
um/x64/esent.lib: skipped 369, total 369
um/x86/CoreMessaging.lib: skipped 28, total 28
um/x64/ElsCore.lib: skipped 5, total 5
um/x86/ComSvcs.Lib: skipped 17, total 17
um/x64/els.lib: skipped 0, total 0
um/x86/compstui.lib: skipped 4, total 4
um/x64/elfapi.lib: skipped 0, total 87
um/x86/CompPkgSup.lib: skipped 9, total 9
um/x64/ehstorguids.lib: skipped 0, total 0
um/x64/efswrt.lib: skipped 18, total 18
um/x86/ComDlg32.Lib: skipped 21, total 21
um/x64/easregprov.lib: skipped 2, total 2
um/x86/ComCtl32.Lib: skipped 128, total 128
um/x64/eappcfg.lib: skipped 15, total 15
um/x86/ClusApi.Lib: skipped 280, total 280
um/x64/dxva2.lib: skipped 38, total 38
um/x64/dxtrans.lib: skipped 6, total 6
um/x64/dxtmsft.lib: skipped 0, total 0
um/x64/dxgi.lib: skipped 14, total 14
um/x64/dwmapi.lib: skipped 30, total 30
um/x64/DtcHelp.Lib: skipped 7, total 24
um/x64/DSUIExt.Lib: skipped 33, total 33
um/x64/dststlog.lib: skipped 1, total 1
um/x64/dssec.lib: skipped 4, total 4
um/x64/DSProp.Lib: skipped 19, total 19
um/x64/dsound.lib: skipped 10, total 10
um/x64/drtprov.lib: skipped 9, total 9
um/x64/drttransport.lib: skipped 2, total 2
um/x64/drt.lib: skipped 21, total 21
um/x86/clfsw32.lib: skipped 63, total 63
um/x86/clfsmgmt.lib: skipped 7, total 212
um/x86/cldapi.lib: skipped 44, total 44
um/x86/Chakrart.lib: skipped 138, total 138
um/x86/cfgmgr32.lib: skipped 231, total 231
um/x86/CertPolEng.Lib: skipped 14, total 14
um/x64/dpx.lib: skipped 5, total 5
um/x64/dnsrslvr.lib: skipped 4, total 4
um/x64/dnsrpc.lib: skipped 6, total 382
um/x64/dnsperf.lib: skipped 3, total 3
um/x64/dnslib.lib: skipped 10, total 1290
um/x64/dnscrcli.lib: skipped 0, total 4
um/x64/DnsAPI.Lib: skipped 270, total 270
um/x64/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x64/dmoguids.lib: skipped 0, total 0
um/x64/dloadhelper.lib: skipped 0, total 3
um/x64/dinput8.lib: skipped 1, total 2
um/x64/difxapi.lib: skipped 12, total 12
um/x64/dhcpsapi.lib: skipped 209, total 209
um/x64/DhcpCSvc6.Lib: skipped 22, total 22
um/x64/DhcpCSvc.Lib: skipped 67, total 67
um/x64/dflayout.lib: skipped 1, total 1
um/x64/deviceaccess.lib: skipped 3, total 3
um/x64/devenum.lib: skipped 0, total 0
um/x64/dcomp.lib: skipped 6, total 6
um/x64/dciman32.lib: skipped 20, total 20
um/x64/DbgHelp.Lib: skipped 239, total 239
um/x64/davclnt.lib: skipped 22, total 22
um/x64/DbgEng.Lib: skipped 4, total 4
um/x64/d3dcsx.lib: skipped 9, total 9
um/x64/d3dcompiler.lib: skipped 29, total 29
um/x64/d3d9.lib: skipped 14, total 14
um/x64/d3d12.lib: skipped 10, total 10
um/x64/d3d11.lib: skipped 45, total 45
um/x86/CertIdl.Lib: skipped 0, total 1
um/x86/certcli.lib: skipped 0, total 0
um/x64/d2d1.lib: skipped 13, total 13
um/x64/d3d10.lib: skipped 29, total 29
um/x64/cscdll.lib: skipped 18, total 18
um/x86/certca.lib: skipped 0, total 0
um/x64/cscapi.lib: skipped 6, total 6
um/x86/certadm.lib: skipped 41, total 41
um/x64/cryptxml.lib: skipped 19, total 19
um/x86/Cabinet.Lib: skipped 26, total 26
um/x64/cryptui.lib: skipped 54, total 54
um/x64/CryptNet.Lib: skipped 5, total 5
um/x64/cryptdll.lib: skipped 20, total 20
um/x64/Crypt32.Lib: skipped 240, total 240
um/x64/Credui.lib: skipped 22, total 22
um/x64/corrEngine.lib: skipped 0, total 0
um/x64/ComSvcs.Lib: skipped 17, total 17
um/x64/CoreMessaging.lib: skipped 28, total 28
um/x64/compstui.lib: skipped 4, total 4
um/x86/BufferOverflowU.lib: skipped 1, total 14
um/x64/CompPkgSup.lib: skipped 9, total 9
um/x86/bthprops.lib: skipped 40, total 40
um/x86/BluetoothApis.lib: skipped 96, total 96
um/x64/ComDlg32.Lib: skipped 21, total 21
um/x64/ComCtl32.Lib: skipped 128, total 128
um/x64/ClusApi.Lib: skipped 280, total 280
um/x64/clfsw32.lib: skipped 63, total 63
um/x86/Bits.Lib: skipped 0, total 0
um/x86/bcrypt.lib: skipped 54, total 54
um/x64/clfsmgmt.lib: skipped 9, total 231
um/x86/basesrv.lib: skipped 6, total 6
um/x86/avrt.lib: skipped 20, total 20
um/x64/cldapi.lib: skipped 44, total 44
um/x64/Chakrart.lib: skipped 138, total 138
um/x86/avifil32.Lib: skipped 74, total 74
um/x86/aux_ulib.lib: skipped 1, total 9
um/x64/cfgmgr32.lib: skipped 231, total 231
um/x64/CertPolEng.Lib: skipped 14, total 14
um/x86/AuthZ.Lib: skipped 36, total 36
um/x64/CertIdl.Lib: skipped 0, total 1
um/x64/certcli.lib: skipped 0, total 0
um/x86/audiomediatypecrt.lib: skipped 3, total 32
um/x86/audioeng.lib: skipped 2, total 2
um/x64/certca.lib: skipped 0, total 0
um/x64/certadm.lib: skipped 41, total 41
um/x64/Cabinet.Lib: skipped 26, total 26
um/x86/AudioBaseProcessingObjectV140.lib: skipped 14, total 73
um/x64/BufferOverflowU.lib: skipped 5, total 16
um/x86/audiobaseprocessingobject.lib: skipped 13, total 69
um/x64/BufferOverflow.lib: skipped 7, total 20
um/x86/ASycFilt.Lib: skipped 1, total 1
um/x64/bthprops.lib: skipped 40, total 40
um/x86/appnotify.lib: skipped 2, total 2
um/x64/BluetoothApis.lib: skipped 96, total 96
um/x86/appmgr.lib: skipped 0, total 0
um/x86/appmgmts.lib: skipped 17, total 17
um/x86/apidll.lib: skipped 2, total 2
um/x64/Bits.Lib: skipped 0, total 0
um/x86/api-ms-win-net-isolation-l1-1-0.lib: skipped 8, total 8
um/x86/ActiveDS.Lib: skipped 27, total 27
um/x64/bcrypt.lib: skipped 54, total 54
um/x86/AclUI.Lib: skipped 6, total 6
um/x64/basesrv.lib: skipped 6, total 6
um/x64/avrt.lib: skipped 20, total 20
um/x64/avifil32.Lib: skipped 74, total 74
um/x64/aux_ulib.lib: skipped 6, total 12
um/x64/AuthZ.Lib: skipped 36, total 36
um/x64/audiomediatypecrt.lib: skipped 7, total 34
um/x64/audioeng.lib: skipped 2, total 2
um/x64/AudioBaseProcessingObjectV140.lib: skipped 21, total 75
um/x64/audiobaseprocessingobject.lib: skipped 20, total 71
um/x64/appnotify.lib: skipped 2, total 2
um/x64/appmgr.lib: skipped 0, total 0
um/x64/appmgmts.lib: skipped 17, total 17
um/x64/api-ms-win-net-isolation-l1-1-0.lib: skipped 8, total 8
um/x64/amstrmid.lib: skipped 0, total 0
um/x64/amsi.lib: skipped 9, total 9
um/x64/advpack.Lib: skipped 84, total 84
um/x64/ahadmin.lib: skipped 0, total 0
um/x64/AdvAPI32.Lib: skipped 782, total 782
um/x64/ADSIid.Lib: skipped 0, total 0
ucrt/x86/ucrtd.lib: skipped 1441, total 1441
ucrt/x86/ucrt.lib: skipped 1378, total 1378
um/x64/ActiveDS.Lib: skipped 27, total 27
ucrt/x86/libucrt.lib: skipped 580, total 7872
ucrt/x86/libucrtd.lib: skipped 195, total 8039
um/x64/AclUI.Lib: skipped 6, total 6
ucrt/x64/ucrtd.lib: skipped 1414, total 1414
ucrt/x64/ucrt.lib: skipped 1351, total 1351
ucrt/x64/libucrtd.lib: skipped 144, total 8178
ucrt/x64/libucrt.lib: skipped 528, total 7991
```

### ucrt: 10.0.17134.0

```
um/x64/Bits.Lib: skipped 0, total 0
um/x64/BluetoothApis.lib: skipped 96, total 96
um/x64/bthprops.lib: skipped 40, total 40
um/x64/BufferOverflowU.lib: skipped 5, total 16
um/x64/certadm.lib: skipped 41, total 41
um/x64/icuuc.lib: skipped 2760, total 2760
um/x64/KSProxy.Lib: skipped 6, total 6
um/x64/mciole32.lib: skipped 11, total 11
um/x64/Mfcore.lib: skipped 36, total 36
um/x64/mfplay.lib: skipped 1, total 1
um/x64/MrmSupport.lib: skipped 24, total 24
um/x64/MsCtfMonitor.lib: skipped 3, total 3
um/x64/MSImg32.Lib: skipped 3, total 3
um/x64/NtDsAPI.Lib: skipped 120, total 120
um/x64/ntmarta.lib: skipped 44, total 44
um/x64/ntstc_msvcrt.lib: skipped 370, total 6158
um/x64/slwga.lib: skipped 1, total 1
um/x64/SpOrder.Lib: skipped 2, total 2
um/x64/srpapi.lib: skipped 21, total 21
um/x64/Sti.Lib: skipped 16, total 16
um/x64/txfw32.lib: skipped 9, total 9
um/x64/WinHvPlatform.lib: skipped 15, total 15
um/x64/winscard.lib: skipped 74, total 74
um/x64/WinSpool.Lib: skipped 232, total 232
um/x64/winsta.lib: skipped 167, total 167
um/x64/winusb.lib: skipped 37, total 37
um/x64/wlanapi.lib: skipped 66, total 66
um/x64/Wldap32.Lib: skipped 245, total 245
um/x64/wmip.lib: skipped 45, total 45
um/x64/wnvapi.lib: skipped 2, total 2
um/x64/wsbapp_uuid.Lib: skipped 0, total 0
um/x64/xpsprint.lib: skipped 4, total 4
um/x64/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x64/xolehlp.lib: skipped 8, total 8
um/x64/xmllite.lib: skipped 6, total 6
um/x64/xinputuap.lib: skipped 8, total 8
um/x64/Xinput9_1_0.lib: skipped 5, total 5
um/x64/xinput.lib: skipped 8, total 8
um/x64/xaudio2_8.lib: skipped 6, total 6
um/x64/xaudio2.lib: skipped 7, total 7
um/x64/xaswitch.lib: skipped 5, total 25
um/x64/xapobase2_8.lib: skipped 10, total 158
um/x64/xapobase.lib: skipped 10, total 158
um/x64/wuguid.lib: skipped 0, total 0
um/x64/WtsApi32.Lib: skipped 65, total 65
um/x64/WSock32.Lib: skipped 75, total 75
um/x64/WSnmp32.Lib: skipped 51, total 51
um/x64/wsmsvc.lib: skipped 3672, total 3672
um/x64/wsdapi.lib: skipped 45, total 45
um/x64/wsclient.lib: skipped 30, total 30
um/x64/wscapi.lib: skipped 39, total 39
um/x64/wsbonline.lib: skipped 3, total 3
um/x64/WS2_32.Lib: skipped 195, total 195
um/x64/workspaceax.lib: skipped 0, total 3
um/x64/wofutil.lib: skipped 11, total 11
um/x64/wmvcore.lib: skipped 20, total 20
um/x64/wmiutils.lib: skipped 0, total 0
um/x64/wmcodecdspuuid.lib: skipped 0, total 0
um/x64/Wldp.Lib: skipped 10, total 10
um/x64/wlanui.lib: skipped 5, total 5
um/x64/WinTrust.Lib: skipped 144, total 144
um/x64/WinStrm.Lib: skipped 0, total 18
um/x64/winsqlite3.lib: skipped 243, total 243
um/x64/winsatapi.lib: skipped 0, total 0
um/x64/WinMM.Lib: skipped 179, total 179
um/x64/winml.lib: skipped 1, total 1
um/x64/WinInet.Lib: skipped 319, total 319
um/x64/WinHvEmulation.lib: skipped 4, total 4
um/x64/winhttp.lib: skipped 63, total 63
um/x64/winfax.lib: skipped 56, total 56
um/x64/windowssideshowguids.lib: skipped 0, total 0
um/x64/windowscodecs.lib: skipped 114, total 114
um/x64/WindowsApp_downlevel.lib: skipped 2602, total 2602
um/x64/WindowsApp.lib: skipped 3198, total 3198
um/x64/windows.ui.lib: skipped 2, total 2
um/x64/windows.networking.lib: skipped 1, total 1
um/x64/windows.data.pdf.lib: skipped 1, total 1
um/x64/WinBio.lib: skipped 60, total 60
um/x64/wiautil.lib: skipped 8, total 136
um/x64/wiaservc.lib: skipped 55, total 55
um/x64/WiaGuid.Lib: skipped 0, total 0
um/x64/wevtapi.lib: skipped 45, total 45
um/x64/Wer.lib: skipped 142, total 142
um/x64/wecapi.lib: skipped 17, total 17
um/x64/websocket.lib: skipped 13, total 13
um/x64/WebServices.lib: skipped 193, total 193
um/x64/wdstptc.lib: skipped 19, total 19
um/x64/wdspxe.lib: skipped 32, total 32
um/x64/wdsmc.lib: skipped 13, total 13
um/x64/wdsClientAPI.LIB: skipped 58, total 58
um/x64/wdsbp.lib: skipped 7, total 7
um/x64/wcmapi.lib: skipped 37, total 37
um/x64/wbemuuid.lib: skipped 0, total 0
um/x64/vstorinterface.lib: skipped 15, total 15
um/x64/vss_uuid.lib: skipped 0, total 0
um/x64/vssapi.lib: skipped 46, total 46
um/x64/vscmgr.lib: skipped 0, total 0
um/x64/vmsavedstatedumpprovider.lib: skipped 18, total 18
um/x64/Virtdisk.Lib: skipped 27, total 27
um/x64/Vfw32.Lib: skipped 127, total 127
um/x64/wcmguid.lib: skipped 0, total 0
um/x64/vertdll.lib: skipped 90, total 93
um/x64/vds_uuid.lib: skipped 0, total 0
um/x64/vccomsup.lib: skipped 5, total 34
um/x64/Version.Lib: skipped 12, total 12
um/x64/Uuid.Lib: skipped 0, total 0
um/x64/Uxtheme.lib: skipped 78, total 78
um/x64/USP10.Lib: skipped 40, total 40
um/x64/UserEnv.Lib: skipped 72, total 72
um/x64/User32.Lib: skipped 777, total 777
um/x64/umpdddi.lib: skipped 92, total 92
um/x64/Urlmon.Lib: skipped 95, total 95
um/x64/UIAutomationCore.lib: skipped 100, total 100
um/x64/twinapi.lib: skipped 0, total 0
um/x64/ualapi.lib: skipped 10, total 10
um/x64/tspubplugincom.lib: skipped 1, total 8
um/x64/tsec.lib: skipped 27, total 27
um/x64/TranscodeImageUID.lib: skipped 0, total 0
um/x64/Traffic.Lib: skipped 22, total 22
um/x64/tokenbinding.lib: skipped 8, total 8
um/x64/tdh.lib: skipped 24, total 24
um/x64/tbs.lib: skipped 21, total 21
um/x64/taskschd.lib: skipped 0, total 0
um/x64/tapi32l.lib: skipped 5, total 258
um/x64/Tapi32.Lib: skipped 278, total 278
um/x64/t2embed.lib: skipped 14, total 14
um/x64/synchronization.lib: skipped 3, total 3
um/x64/swdevice.lib: skipped 9, total 9
um/x64/Svcguid.Lib: skipped 0, total 0
um/x64/structuredquery.lib: skipped 0, total 0
um/x64/strsafe.lib: skipped 0, total 23
um/x64/strmiids.lib: skipped 0, total 0
um/x64/strmbase.lib: skipped 140, total 1689
um/x64/ssdpapi.lib: skipped 29, total 29
um/x64/SrClient.lib: skipped 5, total 36
um/x64/spoolss.lib: skipped 206, total 206
um/x64/SnmpAPI.Lib: skipped 38, total 38
um/x64/slcext.lib: skipped 9, total 9
um/x64/slc.lib: skipped 40, total 40
um/x64/ShLwApi.Lib: skipped 365, total 365
um/x64/ShFolder.Lib: skipped 2, total 2
um/x64/shell32.lib: skipped 397, total 397
um/x64/shcore.lib: skipped 19, total 19
um/x64/shdocvw.lib: skipped 19, total 19
um/x64/Sfc.Lib: skipped 16, total 16
um/x64/SetupAPI.Lib: skipped 558, total 558
um/x64/SensorsUtils.lib: skipped 61, total 61
um/x64/sensorsapi.lib: skipped 0, total 0
um/x64/SensAPI.Lib: skipped 3, total 3
um/x64/sens.lib: skipped 3, total 3
um/x64/security.lib: skipped 36, total 36
um/x64/Secur32.Lib: skipped 96, total 96
um/x64/SearchSDK.lib: skipped 0, total 0
um/x64/ScrnSavW.Lib: skipped 5, total 28
um/x64/ScrnSave.Lib: skipped 5, total 28
um/x64/schannel.lib: skipped 35, total 35
um/x64/scesrv.lib: skipped 2, total 2
um/x64/scecli.lib: skipped 72, total 72
um/x64/SCardDlg.Lib: skipped 5, total 5
um/x64/sbtsv.lib: skipped 0, total 1
um/x64/sas.lib: skipped 1, total 1
um/x64/SAPI.Lib: skipped 0, total 0
um/x64/samsrv.lib: skipped 327, total 327
um/x64/samlib.lib: skipped 70, total 70
um/x64/runtimeobject.lib: skipped 64, total 64
um/x64/RTWorkQ.lib: skipped 34, total 34
um/x64/rtutils.lib: skipped 41, total 41
um/x64/rstrtmgr.lib: skipped 12, total 12
um/x64/Rtm.Lib: skipped 116, total 116
um/x64/rpcutil.lib: skipped 0, total 23
um/x64/RpcRT4.Lib: skipped 541, total 541
um/x64/rpcproxy.lib: skipped 5, total 5
um/x64/Rpcns4.Lib: skipped 62, total 62
um/x64/rpcexts.lib: skipped 58, total 58
um/x64/rometadata.lib: skipped 1, total 1
um/x64/resutils.lib: skipped 126, total 126
um/x64/rasuser.lib: skipped 5, total 5
um/x64/RASDlg.Lib: skipped 25, total 25
um/x64/RASAPI32.Lib: skipped 148, total 148
um/x64/qwave.lib: skipped 14, total 14
um/x64/query.lib: skipped 44, total 44
um/x64/quartz.lib: skipped 4, total 4
um/x64/Psapi.Lib: skipped 27, total 27
um/x64/propsys.lib: skipped 219, total 219
um/x64/prntvpt.lib: skipped 29, total 29
um/x64/powrprof.lib: skipped 109, total 109
um/x64/PortableDeviceGuids.lib: skipped 0, total 0
um/x64/PhotoAcquireUID.lib: skipped 0, total 0
um/x64/PeerDist.lib: skipped 28, total 28
um/x64/Pdh.Lib: skipped 110, total 110
um/x64/pathcch.lib: skipped 22, total 22
um/x64/p2pgraph.lib: skipped 40, total 40
um/x64/p2p.lib: skipped 112, total 112
um/x64/osptk.lib: skipped 0, total 0
um/x64/opmxbox.Lib: skipped 3, total 3
um/x64/OpenGL32.Lib: skipped 368, total 368
um/x64/OneCore_downlevel.Lib: skipped 4702, total 4702
um/x64/OneCoreUAP_downlevel.Lib: skipped 4702, total 4702
um/x64/OneCoreUAP.Lib: skipped 8025, total 8025
um/x64/OneCore.Lib: skipped 5108, total 5108
um/x64/ondemandconnroutehelper.lib: skipped 8, total 8
um/x64/olesvr32.lib: skipped 23, total 23
um/x64/OleDlg.Lib: skipped 23, total 23
um/x64/oledb.lib: skipped 0, total 0
um/x64/olecli32.lib: skipped 178, total 178
um/x64/OleAut32.Lib: skipped 412, total 412
um/x64/OleAcc.Lib: skipped 20, total 20
um/x64/Ole32.Lib: skipped 504, total 504
um/x64/OemLicense.lib: skipped 6, total 6
um/x64/odbccp32.lib: skipped 5, total 64
um/x64/odbcbcp.lib: skipped 28, total 28
um/x64/odbc32.lib: skipped 176, total 176
um/x64/ntstc_libcmt.lib: skipped 370, total 6158
um/x64/objsel.lib: skipped 0, total 0
um/x64/NtQuery.Lib: skipped 44, total 44
um/x64/ntlanman.lib: skipped 23, total 23
um/x64/ntfrsapi.lib: skipped 33, total 33
um/x64/ntdsetup.lib: skipped 24, total 24
um/x64/ntdsatq.lib: skipped 47, total 47
um/x64/ntdsa.lib: skipped 146, total 146
um/x64/ntdll.lib: skipped 2063, total 2063
um/x64/nt.lib: skipped 0, total 6
um/x64/normaliz.lib: skipped 5, total 5
um/x64/ninput.lib: skipped 23, total 23
um/x64/newdev.lib: skipped 23, total 23
um/x64/netlib.lib: skipped 8, total 277
um/x64/NetSh.Lib: skipped 23, total 23
um/x64/NetAPI32.Lib: skipped 212, total 212
um/x64/ndproxystub.lib: skipped 0, total 0
um/x64/ndfapi.lib: skipped 24, total 24
um/x64/nddeapi.lib: skipped 28, total 28
um/x64/ncrypt.lib: skipped 129, total 129
um/x64/nanosrv.lib: skipped 7074, total 7074
um/x64/muiload.lib: skipped 5, total 72
um/x64/mtxdm.lib: skipped 1, total 1
um/x64/Mtx.Lib: skipped 3, total 3
um/x64/msxml6.lib: skipped 0, total 0
um/x64/MsXml2.Lib: skipped 0, total 0
um/x64/MsWSock.Lib: skipped 28, total 28
um/x64/msvfw32.Lib: skipped 47, total 47
um/x64/msv1_0.lib: skipped 19, total 19
um/x64/MSTask.Lib: skipped 11, total 11
um/x64/MSRating.Lib: skipped 32, total 32
um/x64/msports.lib: skipped 11, total 11
um/x64/mspbase.lib: skipped 175, total 1351
um/x64/mspatchc.lib: skipped 14, total 14
um/x64/mspatcha.lib: skipped 16, total 16
um/x64/Msi.Lib: skipped 290, total 290
um/x64/msdrm.lib: skipped 85, total 85
um/x64/msdmo.lib: skipped 15, total 15
um/x64/msdelta.lib: skipped 15, total 15
um/x64/msdasc.lib: skipped 0, total 0
um/x64/Mscms.Lib: skipped 121, total 121
um/x64/MSAJApi.lib: skipped 558, total 558
um/x64/MSAcm32.Lib: skipped 42, total 42
um/x64/msaatext.lib: skipped 0, total 0
um/x64/MqRt.Lib: skipped 47, total 47
um/x64/MqOA.Lib: skipped 0, total 0
um/x64/mprsnap.lib: skipped 46, total 46
um/x64/Mprapi.Lib: skipped 160, total 160
um/x64/Mpr.Lib: skipped 43, total 43
um/x64/mmdevapi.lib: skipped 29, total 29
um/x64/MMC.Lib: skipped 5, total 19
um/x64/mincore_downlevel.lib: skipped 451, total 451
um/x64/mincore.lib: skipped 4374, total 4374
um/x64/mi.lib: skipped 2, total 2
um/x64/MgmtAPI.Lib: skipped 9, total 9
um/x64/mfuuid.lib: skipped 0, total 0
um/x64/Mfsrcsnk.lib: skipped 2, total 2
um/x64/mfsensorgroup.lib: skipped 5, total 5
um/x64/mfreadwrite.lib: skipped 5, total 5
um/x64/Mfplat.lib: skipped 150, total 150
um/x64/Mf.lib: skipped 75, total 75
um/x64/MDMRegistration.lib: skipped 12, total 12
um/x64/mdmlocalmanagement.lib: skipped 3, total 3
um/x64/mbnapi_uuid.lib: skipped 0, total 0
um/x64/MAPI32.Lib: skipped 136, total 136
um/x64/Lz32.Lib: skipped 14, total 14
um/x64/LoadPerf.Lib: skipped 14, total 14
um/x64/locationapi.lib: skipped 0, total 0
um/x64/ktmw32.lib: skipped 44, total 44
um/x64/ksuser.lib: skipped 8, total 8
um/x64/keycredmgr.lib: skipped 4, total 4
um/x64/kernel32legacylib.lib: skipped 14, total 606
um/x64/kernel32.Lib: skipped 1335, total 1335
um/x64/kerbcli.lib: skipped 0, total 3
um/x64/jsrt.lib: skipped 92, total 92
um/x64/iscsidsc.lib: skipped 80, total 80
um/x64/magnification.lib: skipped 21, total 21
um/x64/irprops.lib: skipped 35, total 35
um/x64/Iprop.Lib: skipped 8, total 8
um/x64/iphlpapi.lib: skipped 279, total 279
um/x64/inkobjcore.lib: skipped 30, total 30
um/x64/inseng.lib: skipped 7, total 7
um/x64/Imm32.Lib: skipped 82, total 82
um/x64/infocardapi.Lib: skipped 18, total 18
um/x64/imgutil.Lib: skipped 9, total 9
um/x64/ImageHlp.Lib: skipped 147, total 147
um/x64/iesetup.lib: skipped 7, total 7
um/x64/IEPMAPI.Lib: skipped 5, total 32
um/x64/icuin.Lib: skipped 4475, total 4475
um/x64/Icmui.Lib: skipped 2, total 2
um/x64/Icm32.Lib: skipped 21, total 21
um/x64/iashlpr.lib: skipped 12, total 12
um/x64/httpapi.lib: skipped 44, total 44
um/x64/Htmlhelp.Lib: skipped 5, total 14
um/x64/hrtfapo.lib: skipped 4, total 4
um/x64/hid.lib: skipped 44, total 44
um/x64/HLink.Lib: skipped 28, total 28
um/x64/hhsetup.lib: skipped 145, total 145
um/x64/hbaapi.lib: skipped 93, total 93
um/x64/GPEdit.lib: skipped 10, total 10
um/x64/gpmuuid.lib: skipped 0, total 0
um/x64/GlU32.Lib: skipped 52, total 52
um/x64/glmf32.lib: skipped 134, total 134
um/x64/gdiplus.lib: skipped 630, total 630
um/x64/Gdi32.Lib: skipped 599, total 599
um/x64/fxsutility.lib: skipped 2, total 2
um/x64/fwpuclnt.lib: skipped 274, total 274
um/x64/FrameDyd.Lib: skipped 606, total 606
um/x64/FrameDyn.Lib: skipped 604, total 604
um/x64/fontsub.lib: skipped 2, total 2
um/x64/fltLib.lib: skipped 29, total 29
um/x64/fileextd.lib: skipped 5, total 23
um/x64/FhSvcCtl.lib: skipped 14, total 14
um/x64/feclient.lib: skipped 50, total 50
um/x64/FaultRep.Lib: skipped 15, total 15
um/x64/evr.lib: skipped 9, total 9
um/x64/esent.lib: skipped 375, total 375
um/x64/ElsCore.lib: skipped 5, total 5
um/x64/els.lib: skipped 0, total 0
um/x64/elfapi.lib: skipped 0, total 87
um/x64/ehstorguids.lib: skipped 0, total 0
um/x64/efswrt.lib: skipped 23, total 23
um/x64/easregprov.lib: skipped 2, total 2
um/x64/eappprxy.lib: skipped 18, total 18
um/x64/dxva2.lib: skipped 38, total 38
um/x64/eappcfg.lib: skipped 15, total 15
um/x64/dxtrans.lib: skipped 6, total 6
um/x64/dxtmsft.lib: skipped 0, total 0
um/x64/dxguid.lib: skipped 0, total 0
um/x64/dxgi.lib: skipped 15, total 15
um/x64/dwrite.lib: skipped 1, total 1
um/x64/dwmapi.lib: skipped 31, total 31
um/x64/DtcHelp.Lib: skipped 7, total 25
um/x64/DSUIExt.Lib: skipped 33, total 33
um/x64/dststlog.lib: skipped 1, total 1
um/x64/DSProp.Lib: skipped 19, total 19
um/x64/dssec.lib: skipped 4, total 4
um/x64/drttransport.lib: skipped 2, total 2
um/x64/drtprov.lib: skipped 9, total 9
um/x64/drt.lib: skipped 21, total 21
um/x64/dsound.lib: skipped 10, total 10
um/x64/dpx.lib: skipped 5, total 5
um/x64/dnsrslvr.lib: skipped 4, total 4
um/x64/dnsrpc.lib: skipped 6, total 383
um/x64/dnsperf.lib: skipped 3, total 3
um/x64/dnslib.lib: skipped 10, total 1293
um/x64/dnscrcli.lib: skipped 0, total 4
um/x64/DnsAPI.Lib: skipped 271, total 271
um/x64/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x64/dmoguids.lib: skipped 0, total 0
um/x64/dloadhelper.lib: skipped 0, total 3
um/x64/dinput8.lib: skipped 1, total 2
um/x64/dhcpsapi.lib: skipped 209, total 209
um/x64/difxapi.lib: skipped 12, total 12
um/x64/DhcpCSvc.Lib: skipped 67, total 67
um/x64/DhcpCSvc6.Lib: skipped 22, total 22
um/x64/dflayout.lib: skipped 1, total 1
um/x64/devmgr.lib: skipped 19, total 19
um/x64/deviceaccess.lib: skipped 3, total 3
um/x64/devenum.lib: skipped 0, total 0
um/x64/ddraw.lib: skipped 13, total 13
um/x64/dcomp.lib: skipped 6, total 6
um/x64/DbgModel.Lib: skipped 1, total 1
um/x64/dciman32.lib: skipped 20, total 20
um/x64/DbgHelp.Lib: skipped 239, total 239
um/x64/davclnt.lib: skipped 22, total 22
um/x64/d3dcsxd.lib: skipped 9, total 9
um/x64/DbgEng.Lib: skipped 4, total 4
um/x64/d3dcsx.lib: skipped 9, total 9
um/x64/d3d9.lib: skipped 14, total 14
um/x64/d3d12.lib: skipped 10, total 10
um/x64/d3dcompiler.lib: skipped 29, total 29
um/x64/d3d11.lib: skipped 45, total 45
um/x64/d3d10_1.lib: skipped 29, total 29
um/x64/d2d1.lib: skipped 13, total 13
um/x64/d3d10.lib: skipped 29, total 29
um/x64/cscdll.lib: skipped 18, total 18
um/x64/cscapi.lib: skipped 6, total 6
um/x64/cryptxml.lib: skipped 19, total 19
um/x64/cryptui.lib: skipped 54, total 54
um/x64/Crypt32.Lib: skipped 240, total 240
um/x64/cryptdll.lib: skipped 20, total 20
um/x64/CryptNet.Lib: skipped 5, total 5
um/x64/corrEngine.lib: skipped 0, total 0
um/x64/Credui.lib: skipped 22, total 22
um/x64/ComSvcs.Lib: skipped 17, total 17
um/x64/CoreMessaging.lib: skipped 30, total 30
um/x64/ComDlg32.Lib: skipped 21, total 21
um/x64/ComCtl32.Lib: skipped 128, total 128
um/x64/compstui.lib: skipped 4, total 4
um/x64/CompPkgSup.lib: skipped 9, total 9
um/x64/clfsw32.lib: skipped 63, total 63
um/x64/ClusApi.Lib: skipped 281, total 281
um/x64/clfsmgmt.lib: skipped 9, total 231
um/x64/cldapi.lib: skipped 46, total 46
um/x64/CertPolEng.Lib: skipped 14, total 14
um/x64/certcli.lib: skipped 0, total 0
um/x64/Chakrart.lib: skipped 152, total 152
um/x64/CertIdl.Lib: skipped 0, total 1
um/x64/cfgmgr32.lib: skipped 231, total 231
um/x64/certca.lib: skipped 0, total 0
um/x64/Cabinet.Lib: skipped 26, total 26
um/x64/bcrypt.lib: skipped 54, total 54
um/x64/basesrv.lib: skipped 6, total 6
um/x64/BufferOverflow.lib: skipped 7, total 20
um/x64/avifil32.Lib: skipped 74, total 74
um/x64/aux_ulib.lib: skipped 6, total 13
um/x64/avrt.lib: skipped 20, total 20
um/x64/AuthZ.Lib: skipped 36, total 36
um/x64/audioeng.lib: skipped 2, total 2
um/x64/audiomediatypecrt.lib: skipped 7, total 35
um/x64/audiobaseprocessingobject.lib: skipped 20, total 72
um/x64/AudioBaseProcessingObjectV140.lib: skipped 21, total 76
um/x64/appnotify.lib: skipped 2, total 2
um/x64/appmgr.lib: skipped 0, total 0
um/x64/api-ms-win-net-isolation-l1-1-0.lib: skipped 8, total 8
um/x64/appmgmts.lib: skipped 17, total 17
um/x64/amstrmid.lib: skipped 0, total 0
um/x64/amsi.lib: skipped 9, total 9
um/x64/ahadmin.lib: skipped 0, total 0
um/x64/advpack.Lib: skipped 84, total 84
um/x64/ADSIid.Lib: skipped 0, total 0
um/x64/AdvAPI32.Lib: skipped 782, total 782
um/x64/AclUI.Lib: skipped 6, total 6
um/x64/ActiveDS.Lib: skipped 27, total 27
ucrt/x86/ucrtd.lib: skipped 1441, total 1441
ucrt/x86/ucrt.lib: skipped 1378, total 1378
ucrt/x86/libucrtd.lib: skipped 217, total 8463
ucrt/x86/libucrt.lib: skipped 663, total 8274
um/x86/xpsprint.lib: skipped 4, total 4
um/x86/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x86/xolehlp.lib: skipped 8, total 8
um/x86/xmllite.lib: skipped 6, total 6
um/x86/xinputuap.lib: skipped 8, total 8
um/x86/Xinput9_1_0.lib: skipped 5, total 5
um/x86/xinput.lib: skipped 8, total 8
um/x86/xaudio2_8.lib: skipped 6, total 6
um/x86/xaudio2.lib: skipped 7, total 7
um/x86/xaswitch.lib: skipped 1, total 24
um/x86/xapobase2_8.lib: skipped 4, total 157
um/x86/xapobase.lib: skipped 4, total 157
um/x86/wuguid.lib: skipped 0, total 0
um/x86/WtsApi32.Lib: skipped 65, total 65
um/x86/WSock32.Lib: skipped 75, total 75
um/x86/WSnmp32.Lib: skipped 51, total 51
um/x86/wsmsvc.lib: skipped 3672, total 3672
um/x86/wsdapi.lib: skipped 45, total 45
um/x86/wsclient.lib: skipped 30, total 30
um/x86/wscapi.lib: skipped 39, total 39
um/x86/wsbonline.lib: skipped 3, total 3
um/x86/wsbapp_uuid.Lib: skipped 0, total 0
um/x86/WS2_32.Lib: skipped 180, total 180
um/x86/workspaceax.lib: skipped 0, total 3
um/x86/wofutil.lib: skipped 11, total 11
um/x86/wmvcore.lib: skipped 20, total 20
um/x86/Wow32.Lib: skipped 29, total 29
um/x86/wmiutils.lib: skipped 0, total 0
um/x86/wmip.lib: skipped 45, total 45
um/x86/wmcodecdspuuid.lib: skipped 0, total 0
um/x86/Wldp.Lib: skipped 10, total 10
um/x86/Wldap32.Lib: skipped 245, total 245
um/x86/wlanui.lib: skipped 5, total 5
um/x86/wlanapi.lib: skipped 66, total 66
um/x86/winusb.lib: skipped 37, total 37
um/x86/WinTrust.Lib: skipped 144, total 144
um/x86/WinStrm.Lib: skipped 0, total 18
um/x86/winsta.lib: skipped 167, total 167
um/x86/winsqlite3.lib: skipped 243, total 243
um/x86/WinSpool.Lib: skipped 232, total 232
um/x86/winscard.lib: skipped 74, total 74
um/x86/winsatapi.lib: skipped 0, total 0
um/x86/WinMM.Lib: skipped 191, total 191
um/x86/winml.lib: skipped 1, total 1
um/x86/WinInet.Lib: skipped 319, total 319
um/x86/winfax.lib: skipped 56, total 56
um/x86/windowssideshowguids.lib: skipped 0, total 0
um/x86/windowscodecs.lib: skipped 114, total 114
um/x86/WindowsApp_downlevel.lib: skipped 2589, total 2589
um/x86/WindowsApp.lib: skipped 3181, total 3181
um/x86/windows.ui.lib: skipped 2, total 2
um/x86/windows.networking.lib: skipped 1, total 1
um/x86/windows.data.pdf.lib: skipped 1, total 1
um/x86/WinBio.lib: skipped 60, total 60
um/x86/winhttp.lib: skipped 63, total 63
um/x86/wiautil.lib: skipped 4, total 133
um/x86/wiaservc.lib: skipped 55, total 55
um/x86/WiaGuid.Lib: skipped 0, total 0
um/x86/wevtapi.lib: skipped 45, total 45
um/x86/Wer.lib: skipped 142, total 142
um/x86/wecapi.lib: skipped 17, total 17
um/x86/websocket.lib: skipped 13, total 13
um/x86/WebServices.lib: skipped 193, total 193
um/x86/wdstptc.lib: skipped 19, total 19
um/x86/wdspxe.lib: skipped 32, total 32
um/x86/wdsmc.lib: skipped 13, total 13
um/x86/wdsClientAPI.LIB: skipped 58, total 58
um/x86/wdsbp.lib: skipped 7, total 7
um/x86/wcmguid.lib: skipped 0, total 0
um/x86/wbemuuid.lib: skipped 0, total 0
um/x86/wcmapi.lib: skipped 37, total 37
um/x86/vstorinterface.lib: skipped 15, total 15
um/x86/vss_uuid.lib: skipped 0, total 0
um/x86/vssapi.lib: skipped 46, total 46
um/x86/Virtdisk.Lib: skipped 27, total 27
um/x86/vscmgr.lib: skipped 0, total 0
um/x86/Vfw32.Lib: skipped 127, total 127
um/x86/vds_uuid.lib: skipped 0, total 0
um/x86/Version.Lib: skipped 12, total 12
um/x86/vccomsup.lib: skipped 1, total 31
um/x86/VdmDbg.Lib: skipped 28, total 28
um/x86/Uxtheme.lib: skipped 78, total 78
um/x86/Uuid.Lib: skipped 0, total 0
um/x86/USP10.Lib: skipped 40, total 40
um/x86/UserEnv.Lib: skipped 72, total 72
um/x86/User32.Lib: skipped 769, total 769
um/x86/Urlmon.Lib: skipped 95, total 95
um/x86/umpdddi.lib: skipped 92, total 92
um/x86/unicows.lib: skipped 1011, total 2540
um/x86/UIAutomationCore.lib: skipped 100, total 100
um/x86/ualapi.lib: skipped 10, total 10
um/x86/txfw32.lib: skipped 9, total 9
um/x86/twinapi.lib: skipped 0, total 0
um/x86/tsec.lib: skipped 27, total 27
um/x86/tspubplugincom.lib: skipped 1, total 8
um/x86/TranscodeImageUID.lib: skipped 0, total 0
um/x86/Traffic.Lib: skipped 22, total 22
um/x86/tokenbinding.lib: skipped 8, total 8
um/x86/Thunk32.Lib: skipped 66, total 66
um/x86/tbs.lib: skipped 21, total 21
um/x86/taskschd.lib: skipped 0, total 0
um/x86/tdh.lib: skipped 24, total 24
um/x86/tapi32l.lib: skipped 1, total 255
um/x86/Tapi32.Lib: skipped 278, total 278
um/x86/t2embed.lib: skipped 14, total 14
um/x86/synchronization.lib: skipped 3, total 3
um/x86/swdevice.lib: skipped 9, total 9
um/x86/structuredquery.lib: skipped 0, total 0
um/x86/strsafe.lib: skipped 0, total 22
um/x86/strmiids.lib: skipped 0, total 0
um/x86/strmbase.lib: skipped 156, total 1689
um/x86/Sti.Lib: skipped 16, total 16
um/x86/Svcguid.Lib: skipped 0, total 0
um/x86/ssdpapi.lib: skipped 29, total 29
um/x86/srpapi.lib: skipped 21, total 21
um/x86/SrClient.lib: skipped 1, total 33
um/x86/SpOrder.Lib: skipped 2, total 2
um/x86/spoolss.lib: skipped 206, total 206
um/x86/SnmpAPI.Lib: skipped 38, total 38
um/x86/slwga.lib: skipped 1, total 1
um/x86/slcext.lib: skipped 9, total 9
um/x86/slc.lib: skipped 40, total 40
um/x86/ShLwApi.Lib: skipped 365, total 365
um/x86/ShFolder.Lib: skipped 2, total 2
um/x86/shell32.lib: skipped 397, total 397
um/x86/shdocvw.lib: skipped 19, total 19
um/x86/Sfc.Lib: skipped 16, total 16
um/x86/shcore.lib: skipped 19, total 19
um/x86/SetupAPI.Lib: skipped 558, total 558
um/x86/twain_32.lib: skipped 5, total 5
um/x86/SensorsUtils.lib: skipped 61, total 61
um/x86/sensorsapi.lib: skipped 0, total 0
um/x86/SensAPI.Lib: skipped 3, total 3
um/x86/security.lib: skipped 36, total 36
um/x86/sens.lib: skipped 3, total 3
um/x86/Secur32.Lib: skipped 96, total 96
um/x86/SearchSDK.lib: skipped 0, total 0
um/x86/ScrnSavW.Lib: skipped 1, total 24
um/x86/ScrnSave.Lib: skipped 1, total 24
um/x86/scecli.lib: skipped 72, total 72
um/x86/schannel.lib: skipped 35, total 35
um/x86/SCardDlg.Lib: skipped 5, total 5
um/x86/scesrv.lib: skipped 2, total 2
um/x86/sbtsv.lib: skipped 0, total 1
um/x86/sas.lib: skipped 1, total 1
um/x86/SAPI.Lib: skipped 0, total 0
um/x86/samsrv.lib: skipped 327, total 327
um/x86/samlib.lib: skipped 70, total 70
um/x86/rtutils.lib: skipped 41, total 41
um/x86/RTWorkQ.lib: skipped 34, total 34
um/x86/Rtm.Lib: skipped 116, total 116
um/x86/rstrtmgr.lib: skipped 12, total 12
um/x86/runtimeobject.lib: skipped 60, total 60
um/x86/rpcutil.lib: skipped 0, total 23
um/x86/rpcproxy.lib: skipped 5, total 5
um/x86/RpcRT4.Lib: skipped 534, total 534
um/x86/Rpcns4.Lib: skipped 62, total 62
um/x86/rpcexts.lib: skipped 58, total 58
um/x86/rometadata.lib: skipped 1, total 1
um/x86/resutils.lib: skipped 126, total 126
um/x86/rasuser.lib: skipped 5, total 5
um/x86/RASDlg.Lib: skipped 25, total 25
um/x86/qwave.lib: skipped 14, total 14
um/x86/query.lib: skipped 44, total 44
um/x86/quartz.lib: skipped 4, total 4
um/x86/RASAPI32.Lib: skipped 148, total 148
um/x86/Psapi.Lib: skipped 27, total 27
um/x86/propsys.lib: skipped 219, total 219
um/x86/prntvpt.lib: skipped 29, total 29
um/x86/powrprof.lib: skipped 109, total 109
um/x86/PortableDeviceGuids.lib: skipped 0, total 0
um/x86/PeerDist.lib: skipped 28, total 28
um/x86/Pdh.Lib: skipped 110, total 110
um/x86/PhotoAcquireUID.lib: skipped 0, total 0
um/x86/pathcch.lib: skipped 22, total 22
um/x86/patchwiz.lib: skipped 4, total 4
um/x86/p2pgraph.lib: skipped 40, total 40
um/x86/p2p.lib: skipped 112, total 112
um/x86/osptk.lib: skipped 0, total 0
um/x86/OpenGL32.Lib: skipped 368, total 368
um/x86/OneCoreUAP_downlevel.Lib: skipped 4637, total 4637
um/x86/OneCoreUAP.Lib: skipped 7983, total 7983
um/x86/OneCore_downlevel.Lib: skipped 4637, total 4637
um/x86/OneCore.Lib: skipped 5066, total 5066
um/x86/olesvr32.lib: skipped 23, total 23
um/x86/ondemandconnroutehelper.lib: skipped 8, total 8
um/x86/OlePro32.Lib: skipped 7, total 7
um/x86/OleDlg.Lib: skipped 23, total 23
um/x86/oledb.lib: skipped 0, total 0
um/x86/OleAut32.Lib: skipped 400, total 400
um/x86/olecli32.lib: skipped 178, total 178
um/x86/Ole32.Lib: skipped 432, total 432
um/x86/OleAcc.Lib: skipped 20, total 20
um/x86/OemLicense.lib: skipped 6, total 6
um/x86/odbccp32.lib: skipped 1, total 61
um/x86/odbcbcp.lib: skipped 28, total 28
um/x86/ntvdm.lib: skipped 162, total 162
um/x86/ntstc_msvcrt.lib: skipped 358, total 6281
um/x86/objsel.lib: skipped 0, total 0
um/x86/odbc32.lib: skipped 176, total 176
um/x86/ntstc_libcmt.lib: skipped 358, total 6281
um/x86/ntmarta.lib: skipped 44, total 44
um/x86/NtQuery.Lib: skipped 44, total 44
um/x86/ntlanman.lib: skipped 23, total 23
um/x86/ntfrsapi.lib: skipped 33, total 33
um/x86/ntdsetup.lib: skipped 24, total 24
um/x86/NtDsAPI.Lib: skipped 120, total 120
um/x86/ntdsatq.lib: skipped 47, total 47
um/x86/ntdsa.lib: skipped 146, total 146
um/x86/ntdll.lib: skipped 2042, total 2042
um/x86/nt.lib: skipped 0, total 6
um/x86/ninput.lib: skipped 23, total 23
um/x86/newdev.lib: skipped 23, total 23
um/x86/normaliz.lib: skipped 5, total 5
um/x86/netlib.lib: skipped 2, total 274
um/x86/NetAPI32.Lib: skipped 212, total 212
um/x86/ndproxystub.lib: skipped 0, total 0
um/x86/ndfapi.lib: skipped 24, total 24
um/x86/nddeapi.lib: skipped 28, total 28
um/x86/NetSh.Lib: skipped 23, total 23
um/x86/ncrypt.lib: skipped 129, total 129
um/x86/muiload.lib: skipped 1, total 69
um/x86/mtxdm.lib: skipped 1, total 1
um/x86/MsXml2.Lib: skipped 0, total 0
um/x86/msxml6.lib: skipped 0, total 0
um/x86/MsWSock.Lib: skipped 28, total 28
um/x86/msv1_0.lib: skipped 19, total 19
um/x86/msvfw32.Lib: skipped 47, total 47
um/x86/MSTask.Lib: skipped 22, total 22
um/x86/MSRating.Lib: skipped 32, total 32
um/x86/msports.lib: skipped 11, total 11
um/x86/mspbase.lib: skipped 164, total 1425
um/x86/Mtx.Lib: skipped 3, total 3
um/x86/mspatchc.lib: skipped 14, total 14
um/x86/mspatcha.lib: skipped 16, total 16
um/x86/MSImg32.Lib: skipped 3, total 3
um/x86/Msi.Lib: skipped 290, total 290
um/x86/msdmo.lib: skipped 15, total 15
um/x86/msdrm.lib: skipped 85, total 85
um/x86/msdelta.lib: skipped 15, total 15
um/x86/MsCtfMonitor.lib: skipped 3, total 3
um/x86/msdasc.lib: skipped 0, total 0
um/x86/Mscms.Lib: skipped 121, total 121
um/x86/MSAJApi.lib: skipped 558, total 558
um/x86/msaatext.lib: skipped 0, total 0
um/x86/MrmSupport.lib: skipped 24, total 24
um/x86/MSAcm32.Lib: skipped 44, total 44
um/x86/MqRt.Lib: skipped 47, total 47
um/x86/MqOA.Lib: skipped 0, total 0
um/x86/mprsnap.lib: skipped 46, total 46
um/x86/Mprapi.Lib: skipped 160, total 160
um/x86/Mpr.Lib: skipped 43, total 43
um/x86/MMC.Lib: skipped 1, total 16
um/x86/mmdevapi.lib: skipped 29, total 29
um/x86/mincore_downlevel.lib: skipped 451, total 451
um/x86/mincore.lib: skipped 4332, total 4332
um/x86/mi.lib: skipped 2, total 2
um/x86/mfuuid.lib: skipped 0, total 0
um/x86/Mfsrcsnk.lib: skipped 2, total 2
um/x86/MgmtAPI.Lib: skipped 9, total 9
um/x86/mfreadwrite.lib: skipped 5, total 5
um/x86/mfsensorgroup.lib: skipped 5, total 5
um/x86/mfplay.lib: skipped 1, total 1
um/x86/Mfplat.lib: skipped 150, total 150
um/x86/Mfcore.lib: skipped 36, total 36
um/x86/Mf.lib: skipped 75, total 75
um/x86/MDMRegistration.lib: skipped 12, total 12
um/x86/mdmlocalmanagement.lib: skipped 3, total 3
um/x86/mciole32.lib: skipped 11, total 11
um/x86/mbnapi_uuid.lib: skipped 0, total 0
um/x86/MAPI32.Lib: skipped 155, total 155
um/x86/magnification.lib: skipped 21, total 21
um/x86/ktmw32.lib: skipped 44, total 44
um/x86/LoadPerf.Lib: skipped 14, total 14
um/x86/Lz32.Lib: skipped 14, total 14
um/x86/locationapi.lib: skipped 0, total 0
um/x86/ksuser.lib: skipped 8, total 8
um/x86/keycredmgr.lib: skipped 4, total 4
um/x86/kernel32.Lib: skipped 1309, total 1309
um/x86/KSProxy.Lib: skipped 6, total 6
um/x86/kerbcli.lib: skipped 0, total 3
um/x86/kernel32legacylib.lib: skipped 6, total 545
um/x86/jsrt.lib: skipped 92, total 92
um/x86/irprops.lib: skipped 35, total 35
um/x86/iscsidsc.lib: skipped 80, total 80
um/x86/jetoledb.lib: skipped 0, total 0
um/x86/int64.lib: skipped 0, total 11
um/x86/iphlpapi.lib: skipped 279, total 279
um/x86/inseng.lib: skipped 7, total 7
um/x86/Iprop.Lib: skipped 8, total 8
um/x86/inkobjcore.lib: skipped 30, total 30
um/x86/infocardapi.Lib: skipped 18, total 18
um/x86/Imm32.Lib: skipped 82, total 82
um/x86/imgutil.Lib: skipped 9, total 9
um/x86/iesetup.lib: skipped 7, total 7
um/x86/ImageHlp.Lib: skipped 150, total 150
um/x86/IEPMAPI.Lib: skipped 1, total 29
um/x86/icuuc.lib: skipped 2760, total 2760
um/x86/icuin.Lib: skipped 4475, total 4475
um/x86/Icmui.Lib: skipped 2, total 2
um/x86/Icm32.Lib: skipped 21, total 21
um/x86/iashlpr.lib: skipped 12, total 12
um/x86/httpapi.lib: skipped 44, total 44
um/x86/Htmlhelp.Lib: skipped 1, total 11
um/x86/hrtfapo.lib: skipped 4, total 4
um/x86/HLink.Lib: skipped 28, total 28
um/x86/hid.lib: skipped 44, total 44
um/x86/hbaapi.lib: skipped 93, total 93
um/x86/hhsetup.lib: skipped 145, total 145
um/x86/gpmuuid.lib: skipped 0, total 0
um/x86/GPEdit.lib: skipped 10, total 10
um/x86/GlU32.Lib: skipped 52, total 52
um/x86/glmf32.lib: skipped 134, total 134
um/x86/gdiplus.lib: skipped 630, total 630
um/x86/Gdi32.Lib: skipped 599, total 599
um/x86/fxsutility.lib: skipped 2, total 2
um/x86/FrameDyn.Lib: skipped 604, total 604
um/x86/fwpuclnt.lib: skipped 274, total 274
um/x86/FrameDyd.Lib: skipped 606, total 606
um/x86/fontsub.lib: skipped 2, total 2
um/x86/FhSvcCtl.lib: skipped 14, total 14
um/x86/fileextd.lib: skipped 1, total 22
um/x86/feclient.lib: skipped 50, total 50
um/x86/fltLib.lib: skipped 29, total 29
um/x86/evr.lib: skipped 9, total 9
um/x86/FaultRep.Lib: skipped 15, total 15
um/x86/esent.lib: skipped 375, total 375
um/x86/ElsCore.lib: skipped 5, total 5
um/x86/elfapi.lib: skipped 0, total 65
um/x86/ehstorguids.lib: skipped 0, total 0
um/x86/els.lib: skipped 0, total 0
um/x86/efswrt.lib: skipped 23, total 23
um/x86/easregprov.lib: skipped 2, total 2
um/x86/eappprxy.lib: skipped 18, total 18
um/x86/eappcfg.lib: skipped 15, total 15
um/x86/dxva2.lib: skipped 38, total 38
um/x86/dxtrans.lib: skipped 6, total 6
um/x86/dxtmsft.lib: skipped 0, total 0
um/x86/dxguid.lib: skipped 0, total 0
um/x86/dxgi.lib: skipped 15, total 15
um/x86/dwrite.lib: skipped 1, total 1
um/x86/dwmapi.lib: skipped 31, total 31
um/x86/DtcHelp.Lib: skipped 3, total 23
um/x86/dststlog.lib: skipped 1, total 1
um/x86/DSUIExt.Lib: skipped 33, total 33
um/x86/dssec.lib: skipped 4, total 4
um/x86/DSProp.Lib: skipped 19, total 19
um/x86/drttransport.lib: skipped 2, total 2
um/x86/drtprov.lib: skipped 9, total 9
um/x86/drt.lib: skipped 21, total 21
um/x86/dsound.lib: skipped 10, total 10
um/x86/dpx.lib: skipped 5, total 5
um/x86/dnsrslvr.lib: skipped 4, total 4
um/x86/dnsperf.lib: skipped 3, total 3
um/x86/dnslib.lib: skipped 2, total 1290
um/x86/dnsrpc.lib: skipped 1, total 379
um/x86/dnscrcli.lib: skipped 0, total 4
um/x86/DnsAPI.Lib: skipped 271, total 271
um/x86/dmoguids.lib: skipped 0, total 0
um/x86/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x86/dloadhelper.lib: skipped 0, total 3
um/x86/dinput8.lib: skipped 1, total 2
um/x86/difxapi.lib: skipped 12, total 12
um/x86/dhcpsapi.lib: skipped 209, total 209
um/x86/DhcpCSvc6.Lib: skipped 22, total 22
um/x86/DhcpCSvc.Lib: skipped 67, total 67
um/x86/dflayout.lib: skipped 1, total 1
um/x86/deviceaccess.lib: skipped 3, total 3
um/x86/devenum.lib: skipped 0, total 0
um/x86/devmgr.lib: skipped 19, total 19
um/x86/ddraw.lib: skipped 13, total 13
um/x86/dcomp.lib: skipped 6, total 6
um/x86/dciman32.lib: skipped 20, total 20
um/x86/DbgModel.Lib: skipped 1, total 1
um/x86/DbgHelp.Lib: skipped 237, total 237
um/x86/DbgEng.Lib: skipped 4, total 4
um/x86/d3dcsxd.lib: skipped 9, total 9
um/x86/d3dcsx.lib: skipped 9, total 9
um/x86/d3dcompiler.lib: skipped 29, total 29
um/x86/davclnt.lib: skipped 22, total 22
um/x86/d3d9.lib: skipped 14, total 14
um/x86/d3d11.lib: skipped 45, total 45
um/x86/d3d12.lib: skipped 10, total 10
um/x86/d3d10.lib: skipped 29, total 29
um/x86/d2d1.lib: skipped 13, total 13
um/x86/d3d10_1.lib: skipped 29, total 29
um/x86/cscdll.lib: skipped 18, total 18
um/x86/cryptxml.lib: skipped 19, total 19
um/x86/cscapi.lib: skipped 6, total 6
um/x86/cryptui.lib: skipped 54, total 54
um/x86/CryptNet.Lib: skipped 5, total 5
um/x86/cryptdll.lib: skipped 20, total 20
um/x86/Crypt32.Lib: skipped 240, total 240
um/x86/Credui.lib: skipped 22, total 22
um/x86/CoreMessaging.lib: skipped 30, total 30
um/x86/corrEngine.lib: skipped 0, total 0
um/x86/ComSvcs.Lib: skipped 17, total 17
um/x86/compstui.lib: skipped 4, total 4
um/x86/CompPkgSup.lib: skipped 9, total 9
um/x86/ComDlg32.Lib: skipped 21, total 21
um/x86/ComCtl32.Lib: skipped 128, total 128
um/x86/ClusApi.Lib: skipped 281, total 281
um/x86/clfsw32.lib: skipped 63, total 63
um/x86/clfsmgmt.lib: skipped 7, total 212
um/x86/Chakrart.lib: skipped 152, total 152
um/x86/cfgmgr32.lib: skipped 231, total 231
um/x86/cldapi.lib: skipped 46, total 46
um/x86/CertIdl.Lib: skipped 0, total 1
um/x86/CertPolEng.Lib: skipped 14, total 14
um/x86/certcli.lib: skipped 0, total 0
um/x86/certca.lib: skipped 0, total 0
um/x86/certadm.lib: skipped 41, total 41
um/x86/Cabinet.Lib: skipped 26, total 26
um/x86/bthprops.lib: skipped 40, total 40
um/x86/BufferOverflowU.lib: skipped 1, total 14
um/x86/BluetoothApis.lib: skipped 96, total 96
um/x86/Bits.Lib: skipped 0, total 0
um/x86/BufferOverflow.lib: skipped 1, total 20
um/x86/bcrypt.lib: skipped 54, total 54
um/x86/basesrv.lib: skipped 6, total 6
um/x86/avrt.lib: skipped 20, total 20
um/x86/avifil32.Lib: skipped 74, total 74
um/x86/AuthZ.Lib: skipped 36, total 36
um/x86/aux_ulib.lib: skipped 1, total 9
um/x86/audioeng.lib: skipped 2, total 2
um/x86/audiomediatypecrt.lib: skipped 3, total 32
um/x86/AudioBaseProcessingObjectV140.lib: skipped 14, total 73
um/x86/audiobaseprocessingobject.lib: skipped 13, total 69
um/x86/ASycFilt.Lib: skipped 1, total 1
um/x86/appnotify.lib: skipped 2, total 2
um/x86/appmgmts.lib: skipped 17, total 17
um/x86/apidll.lib: skipped 2, total 2
um/x86/api-ms-win-net-isolation-l1-1-0.lib: skipped 8, total 8
um/x86/amstrmid.lib: skipped 0, total 0
um/x86/ahadmin.lib: skipped 0, total 0
um/x86/amsi.lib: skipped 9, total 9
um/x86/advpack.Lib: skipped 84, total 84
um/x86/ADSIid.Lib: skipped 0, total 0
um/x86/ActiveDS.Lib: skipped 27, total 27
um/x86/appmgr.lib: skipped 0, total 0
um/x86/AclUI.Lib: skipped 6, total 6
um/x86/AdvAPI32.Lib: skipped 782, total 782
ucrt/x64/ucrtd.lib: skipped 1414, total 1414
ucrt/x64/ucrt.lib: skipped 1351, total 1351
ucrt/x64/libucrtd.lib: skipped 152, total 8579
ucrt/x64/libucrt.lib: skipped 543, total 8393
```

### ucrt: 10.0.17763.0

```
ucrt/x64/ucrtd.lib: skipped 1414, total 1414
ucrt/x64/ucrt.lib: skipped 1351, total 1351
ucrt/x64/libucrtd.lib: skipped 152, total 8660
ucrt/x64/libucrt.lib: skipped 546, total 8483
um/x64/xpsprint.lib: skipped 4, total 4
um/x64/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x64/xolehlp.lib: skipped 8, total 8
um/x64/xmllite.lib: skipped 6, total 6
um/x64/xinputuap.lib: skipped 8, total 8
um/x64/Xinput9_1_0.lib: skipped 5, total 5
um/x64/xinput.lib: skipped 8, total 8
um/x64/xaudio2_8.lib: skipped 7, total 7
um/x64/xaudio2.lib: skipped 9, total 9
um/x64/xaswitch.lib: skipped 0, total 17
um/x64/xapobase.lib: skipped 5, total 150
um/x64/xapobase2_8.lib: skipped 5, total 150
um/x64/wuguid.lib: skipped 0, total 0
um/x64/WSock32.Lib: skipped 75, total 75
um/x64/WSnmp32.Lib: skipped 51, total 51
um/x64/wsmsvc.lib: skipped 3673, total 3673
um/x64/WtsApi32.Lib: skipped 65, total 65
um/x64/wsdapi.lib: skipped 45, total 45
um/x64/wsclient.lib: skipped 30, total 30
um/x64/wsbonline.lib: skipped 3, total 3
um/x64/wscapi.lib: skipped 39, total 39
um/x64/wsbapp_uuid.Lib: skipped 0, total 0
um/x64/WS2_32.Lib: skipped 195, total 195
um/x64/workspaceax.lib: skipped 0, total 3
um/x64/wnvapi.lib: skipped 2, total 2
um/x64/wmvcore.lib: skipped 20, total 20
um/x64/wofutil.lib: skipped 11, total 11
um/x64/wmiutils.lib: skipped 0, total 0
um/x64/wmip.lib: skipped 45, total 45
um/x64/wmcodecdspuuid.lib: skipped 0, total 0
um/x64/Wldp.Lib: skipped 17, total 17
um/x64/wlanui.lib: skipped 5, total 5
um/x64/Wldap32.Lib: skipped 245, total 245
um/x64/wlanapi.lib: skipped 68, total 68
um/x64/WinTrust.Lib: skipped 145, total 145
um/x64/winusb.lib: skipped 37, total 37
um/x64/winsta.lib: skipped 169, total 169
um/x64/WinStrm.Lib: skipped 0, total 18
um/x64/winsqlite3.lib: skipped 248, total 248
um/x64/WinSpool.Lib: skipped 232, total 232
um/x64/winscard.lib: skipped 74, total 74
um/x64/WinMM.Lib: skipped 179, total 179
um/x64/winsatapi.lib: skipped 0, total 0
um/x64/winml.lib: skipped 1, total 1
um/x64/WinHvPlatform.lib: skipped 23, total 23
um/x64/WinInet.Lib: skipped 319, total 319
um/x64/WinHvEmulation.lib: skipped 4, total 4
um/x64/winhttp.lib: skipped 64, total 64
um/x64/windowssideshowguids.lib: skipped 0, total 0
um/x64/windowscodecs.lib: skipped 114, total 114
um/x64/winfax.lib: skipped 56, total 56
um/x64/WindowsApp_downlevel.lib: skipped 3237, total 3237
um/x64/WindowsApp.lib: skipped 3237, total 3237
um/x64/windows.networking.lib: skipped 1, total 1
um/x64/windows.ui.lib: skipped 2, total 2
um/x64/WinBio.lib: skipped 60, total 60
um/x64/windows.data.pdf.lib: skipped 1, total 1
um/x64/wiautil.lib: skipped 3, total 128
um/x64/wiaservc.lib: skipped 55, total 55
um/x64/windows.ai.machinelearning.lib: skipped 1, total 1
um/x64/WiaGuid.Lib: skipped 0, total 0
um/x64/wevtapi.lib: skipped 45, total 45
um/x64/Wer.lib: skipped 145, total 145
um/x64/wecapi.lib: skipped 17, total 17
um/x64/websocket.lib: skipped 13, total 13
um/x64/WebServices.lib: skipped 193, total 193
um/x64/wdstptc.lib: skipped 19, total 19
um/x64/wdspxe.lib: skipped 32, total 32
um/x64/wdsmc.lib: skipped 13, total 13
um/x64/wdsClientAPI.LIB: skipped 58, total 58
um/x64/wdsbp.lib: skipped 7, total 7
um/x64/wcmguid.lib: skipped 0, total 0
um/x64/wcmapi.lib: skipped 39, total 39
um/x64/wbemuuid.lib: skipped 0, total 0
um/x64/vstorinterface.lib: skipped 15, total 15
um/x64/vss_uuid.lib: skipped 0, total 0
um/x64/vssapi.lib: skipped 46, total 46
um/x64/vscmgr.lib: skipped 0, total 0
um/x64/vmsavedstatedumpprovider.lib: skipped 18, total 18
um/x64/Vfw32.Lib: skipped 127, total 127
um/x64/Virtdisk.Lib: skipped 29, total 29
um/x64/vmdevicehost.lib: skipped 8, total 8
um/x64/Version.Lib: skipped 12, total 12
um/x64/vds_uuid.lib: skipped 0, total 0
um/x64/vccomsup.lib: skipped 0, total 26
um/x64/Uxtheme.lib: skipped 78, total 78
um/x64/Uuid.Lib: skipped 0, total 0
um/x64/USP10.Lib: skipped 40, total 40
um/x64/UserEnv.Lib: skipped 72, total 72
um/x64/User32.Lib: skipped 778, total 778
um/x64/Urlmon.Lib: skipped 95, total 95
um/x64/umpdddi.lib: skipped 92, total 92
um/x64/UIAutomationCore.lib: skipped 99, total 99
um/x64/ualapi.lib: skipped 10, total 10
um/x64/txfw32.lib: skipped 9, total 9
um/x64/twinapi.lib: skipped 0, total 0
um/x64/tspubplugincom.lib: skipped 1, total 8
um/x64/tsec.lib: skipped 27, total 27
um/x64/TranscodeImageUID.lib: skipped 0, total 0
um/x64/Traffic.Lib: skipped 22, total 22
um/x64/tokenbinding.lib: skipped 9, total 9
um/x64/tdh.lib: skipped 24, total 24
um/x64/tbs.lib: skipped 21, total 21
um/x64/taskschd.lib: skipped 0, total 0
um/x64/Tapi32.Lib: skipped 278, total 278
um/x64/tapi32l.lib: skipped 0, total 250
um/x64/t2embed.lib: skipped 14, total 14
um/x64/synchronization.lib: skipped 3, total 3
um/x64/swdevice.lib: skipped 9, total 9
um/x64/Svcguid.Lib: skipped 0, total 0
um/x64/structuredquery.lib: skipped 0, total 0
um/x64/strsafe.lib: skipped 0, total 23
um/x64/strmiids.lib: skipped 0, total 0
um/x64/strmbase.lib: skipped 135, total 1681
um/x64/Sti.Lib: skipped 16, total 16
um/x64/ssdpapi.lib: skipped 29, total 29
um/x64/srpapi.lib: skipped 21, total 21
um/x64/SrClient.lib: skipped 0, total 28
um/x64/SpOrder.Lib: skipped 2, total 2
um/x64/spoolss.lib: skipped 206, total 206
um/x64/SnmpAPI.Lib: skipped 38, total 38
um/x64/slwga.lib: skipped 1, total 1
um/x64/slcext.lib: skipped 9, total 9
um/x64/slc.lib: skipped 40, total 40
um/x64/vertdll.lib: skipped 92, total 95
um/x64/ShLwApi.Lib: skipped 365, total 365
um/x64/ShFolder.Lib: skipped 2, total 2
um/x64/shell32.lib: skipped 397, total 397
um/x64/shdocvw.lib: skipped 19, total 19
um/x64/shcore.lib: skipped 20, total 20
um/x64/Sfc.Lib: skipped 16, total 16
um/x64/SetupAPI.Lib: skipped 558, total 558
um/x64/SensorsUtils.lib: skipped 62, total 62
um/x64/sensorsapi.lib: skipped 0, total 0
um/x64/SensAPI.Lib: skipped 3, total 3
um/x64/security.lib: skipped 36, total 36
um/x64/sens.lib: skipped 3, total 3
um/x64/Secur32.Lib: skipped 96, total 96
um/x64/SearchSDK.lib: skipped 0, total 0
um/x64/ScrnSavW.Lib: skipped 0, total 20
um/x64/ScrnSave.Lib: skipped 0, total 20
um/x64/schannel.lib: skipped 35, total 35
um/x64/scesrv.lib: skipped 2, total 2
um/x64/scecli.lib: skipped 72, total 72
um/x64/SCardDlg.Lib: skipped 5, total 5
um/x64/sbtsv.lib: skipped 0, total 1
um/x64/sas.lib: skipped 1, total 1
um/x64/SAPI.Lib: skipped 0, total 0
um/x64/samsrv.lib: skipped 327, total 327
um/x64/samlib.lib: skipped 70, total 70
um/x64/RTWorkQ.lib: skipped 34, total 34
um/x64/runtimeobject.lib: skipped 64, total 64
um/x64/rtutils.lib: skipped 41, total 41
um/x64/Rtm.Lib: skipped 116, total 116
um/x64/rstrtmgr.lib: skipped 12, total 12
um/x64/rpcutil.lib: skipped 0, total 23
um/x64/rpcproxy.lib: skipped 5, total 5
um/x64/RpcRT4.Lib: skipped 541, total 541
um/x64/Rpcns4.Lib: skipped 62, total 62
um/x64/rpcexts.lib: skipped 58, total 58
um/x64/rometadata.lib: skipped 1, total 1
um/x64/resutils.lib: skipped 126, total 126
um/x64/rasuser.lib: skipped 5, total 5
um/x64/RASDlg.Lib: skipped 25, total 25
um/x64/RASAPI32.Lib: skipped 148, total 148
um/x64/qwave.lib: skipped 14, total 14
um/x64/query.lib: skipped 44, total 44
um/x64/quartz.lib: skipped 4, total 4
um/x64/Psapi.Lib: skipped 27, total 27
um/x64/propsys.lib: skipped 219, total 219
um/x64/prntvpt.lib: skipped 29, total 29
um/x64/powrprof.lib: skipped 112, total 112
um/x64/ProjectedFSLib.lib: skipped 33, total 33
um/x64/PortableDeviceGuids.lib: skipped 0, total 0
um/x64/PhotoAcquireUID.lib: skipped 0, total 0
um/x64/PeerDist.lib: skipped 28, total 28
um/x64/Pdh.Lib: skipped 110, total 110
um/x64/pathcch.lib: skipped 22, total 22
um/x64/p2pgraph.lib: skipped 40, total 40
um/x64/p2p.lib: skipped 112, total 112
um/x64/opmxbox.Lib: skipped 3, total 3
um/x64/osptk.lib: skipped 0, total 0
um/x64/OneCore_downlevel.Lib: skipped 4865, total 4868
um/x64/OpenGL32.Lib: skipped 368, total 368
um/x64/OneCore_apiset.Lib: skipped 5198, total 5198
um/x64/OneCoreUAP_downlevel.Lib: skipped 4865, total 4868
um/x64/OneCoreUAP_apiset.Lib: skipped 8259, total 8259
um/x64/OneCoreUAP.Lib: skipped 10608, total 10611
um/x64/OneCore.Lib: skipped 7653, total 7656
um/x64/ondemandconnroutehelper.lib: skipped 8, total 8
um/x64/olesvr32.lib: skipped 23, total 23
um/x64/oledb.lib: skipped 0, total 0
um/x64/OleDlg.Lib: skipped 23, total 23
um/x64/OleAut32.Lib: skipped 412, total 412
um/x64/olecli32.lib: skipped 178, total 178
um/x64/OleAcc.Lib: skipped 20, total 20
um/x64/OemLicense.lib: skipped 6, total 6
um/x64/Ole32.Lib: skipped 504, total 504
um/x64/odbccp32.lib: skipped 0, total 56
um/x64/odbcbcp.lib: skipped 28, total 28
um/x64/odbc32.lib: skipped 176, total 176
um/x64/ntstc_msvcrt.lib: skipped 369, total 6624
um/x64/ntstc_libcmt.lib: skipped 369, total 6624
um/x64/objsel.lib: skipped 0, total 0
um/x64/NtQuery.Lib: skipped 44, total 44
um/x64/ntlanman.lib: skipped 23, total 23
um/x64/ntmarta.lib: skipped 44, total 44
um/x64/ntfrsapi.lib: skipped 33, total 33
um/x64/ntdsetup.lib: skipped 24, total 24
um/x64/ntdsatq.lib: skipped 47, total 47
um/x64/NtDsAPI.Lib: skipped 120, total 120
um/x64/ntdsa.lib: skipped 146, total 146
um/x64/ntdll.lib: skipped 2071, total 2071
um/x64/normaliz.lib: skipped 5, total 5
um/x64/ninput.lib: skipped 23, total 23
um/x64/newdev.lib: skipped 23, total 23
um/x64/NetSh.Lib: skipped 23, total 23
um/x64/nt.lib: skipped 0, total 6
um/x64/netlib.lib: skipped 3, total 269
um/x64/NetAPI32.Lib: skipped 212, total 212
um/x64/ndproxystub.lib: skipped 0, total 0
um/x64/nddeapi.lib: skipped 28, total 28
um/x64/ndfapi.lib: skipped 24, total 24
um/x64/ncrypt.lib: skipped 136, total 136
um/x64/nanosrv.lib: skipped 7087, total 7087
um/x64/muiload.lib: skipped 0, total 64
um/x64/mtxdm.lib: skipped 1, total 1
um/x64/msxml6.lib: skipped 0, total 0
um/x64/Mtx.Lib: skipped 3, total 3
um/x64/MsXml2.Lib: skipped 0, total 0
um/x64/MsWSock.Lib: skipped 28, total 28
um/x64/msvfw32.Lib: skipped 47, total 47
um/x64/msv1_0.lib: skipped 19, total 19
um/x64/MSTask.Lib: skipped 11, total 11
um/x64/msports.lib: skipped 11, total 11
um/x64/MSRating.Lib: skipped 32, total 32
um/x64/mspbase.lib: skipped 170, total 1367
um/x64/mspatcha.lib: skipped 16, total 16
um/x64/mspatchc.lib: skipped 14, total 14
um/x64/MSImg32.Lib: skipped 3, total 3
um/x64/Msi.Lib: skipped 290, total 290
um/x64/msdrm.lib: skipped 85, total 85
um/x64/msdmo.lib: skipped 15, total 15
um/x64/msdelta.lib: skipped 15, total 15
um/x64/msdasc.lib: skipped 0, total 0
um/x64/MsCtfMonitor.lib: skipped 3, total 3
um/x64/Mscms.Lib: skipped 127, total 127
um/x64/MSAJApi.lib: skipped 558, total 558
um/x64/MSAcm32.Lib: skipped 42, total 42
um/x64/msaatext.lib: skipped 0, total 0
um/x64/MrmSupport.lib: skipped 24, total 24
um/x64/MqRt.Lib: skipped 47, total 47
um/x64/MqOA.Lib: skipped 0, total 0
um/x64/Mprapi.Lib: skipped 160, total 160
um/x64/mprsnap.lib: skipped 46, total 46
um/x64/Mpr.Lib: skipped 43, total 43
um/x64/mmdevapi.lib: skipped 29, total 29
um/x64/MMC.Lib: skipped 0, total 11
um/x64/mincore_downlevel.lib: skipped 451, total 451
um/x64/mincore.lib: skipped 4414, total 4414
um/x64/mi.lib: skipped 2, total 2
um/x64/MgmtAPI.Lib: skipped 9, total 9
um/x64/mfuuid.lib: skipped 0, total 0
um/x64/mfsensorgroup.lib: skipped 5, total 5
um/x64/Mfsrcsnk.lib: skipped 2, total 2
um/x64/mfplay.lib: skipped 1, total 1
um/x64/mfreadwrite.lib: skipped 5, total 5
um/x64/Mfplat.lib: skipped 150, total 150
um/x64/Mf.lib: skipped 75, total 75
um/x64/Mfcore.lib: skipped 38, total 38
um/x64/MDMRegistration.lib: skipped 12, total 12
um/x64/mdmlocalmanagement.lib: skipped 3, total 3
um/x64/mciole32.lib: skipped 11, total 11
um/x64/mbnapi_uuid.lib: skipped 0, total 0
um/x64/MAPI32.Lib: skipped 136, total 136
um/x64/magnification.lib: skipped 21, total 21
um/x64/Lz32.Lib: skipped 14, total 14
um/x64/locationapi.lib: skipped 0, total 0
um/x64/ksuser.lib: skipped 8, total 8
um/x64/ktmw32.lib: skipped 44, total 44
um/x64/LoadPerf.Lib: skipped 14, total 14
um/x64/KSProxy.Lib: skipped 6, total 6
um/x64/keycredmgr.lib: skipped 4, total 4
um/x64/kernel32.Lib: skipped 1343, total 1343
um/x64/kernel32legacylib.lib: skipped 9, total 598
um/x64/kerbcli.lib: skipped 0, total 3
um/x64/jsrt.lib: skipped 92, total 92
um/x64/iscsidsc.lib: skipped 80, total 80
um/x64/irprops.lib: skipped 35, total 35
um/x64/iphlpapi.lib: skipped 290, total 290
um/x64/Iprop.Lib: skipped 8, total 8
um/x64/inseng.lib: skipped 7, total 7
um/x64/inkobjcore.lib: skipped 30, total 30
um/x64/infocardapi.Lib: skipped 18, total 18
um/x64/Imm32.Lib: skipped 82, total 82
um/x64/imgutil.Lib: skipped 9, total 9
um/x64/ImageHlp.Lib: skipped 147, total 147
um/x64/iesetup.lib: skipped 7, total 7
um/x64/IEPMAPI.Lib: skipped 0, total 24
um/x64/icuuc.lib: skipped 2815, total 2815
um/x64/icuin.Lib: skipped 5108, total 5108
um/x64/Icmui.Lib: skipped 2, total 2
um/x64/iashlpr.lib: skipped 12, total 12
um/x64/Icm32.Lib: skipped 21, total 21
um/x64/httpapi.lib: skipped 44, total 44
um/x64/Htmlhelp.Lib: skipped 0, total 6
um/x64/HLink.Lib: skipped 28, total 28
um/x64/hid.lib: skipped 44, total 44
um/x64/hrtfapo.lib: skipped 4, total 4
um/x64/hhsetup.lib: skipped 145, total 145
um/x64/hbaapi.lib: skipped 93, total 93
um/x64/gpmuuid.lib: skipped 0, total 0
um/x64/GPEdit.lib: skipped 10, total 10
um/x64/GlU32.Lib: skipped 52, total 52
um/x64/glmf32.lib: skipped 134, total 134
um/x64/gdiplus.lib: skipped 630, total 630
um/x64/Gdi32.Lib: skipped 606, total 606
um/x64/fxsutility.lib: skipped 2, total 2
um/x64/fwpuclnt.lib: skipped 276, total 276
um/x64/FrameDyn.Lib: skipped 604, total 604
um/x64/FrameDyd.Lib: skipped 606, total 606
um/x64/fontsub.lib: skipped 2, total 2
um/x64/fltLib.lib: skipped 29, total 29
um/x64/fileextd.lib: skipped 0, total 15
um/x64/FhSvcCtl.lib: skipped 14, total 14
um/x64/feclient.lib: skipped 52, total 52
um/x64/FaultRep.Lib: skipped 16, total 16
um/x64/esent.lib: skipped 375, total 375
um/x64/ElsCore.lib: skipped 5, total 5
um/x64/evr.lib: skipped 9, total 9
um/x64/els.lib: skipped 0, total 0
um/x64/ehstorguids.lib: skipped 0, total 0
um/x64/elfapi.lib: skipped 0, total 122
um/x64/efswrt.lib: skipped 27, total 27
um/x64/eappprxy.lib: skipped 18, total 18
um/x64/easregprov.lib: skipped 2, total 2
um/x64/eappcfg.lib: skipped 15, total 15
um/x64/dxva2.lib: skipped 38, total 38
um/x64/dxtmsft.lib: skipped 0, total 0
um/x64/dxtrans.lib: skipped 6, total 6
um/x64/dxguid.lib: skipped 0, total 0
um/x64/dxgi.lib: skipped 15, total 15
um/x64/dxcompiler.lib: skipped 2, total 2
um/x64/DtcHelp.Lib: skipped 2, total 17
um/x64/dwrite.lib: skipped 1, total 1
um/x64/DSUIExt.Lib: skipped 33, total 33
um/x64/dststlog.lib: skipped 1, total 1
um/x64/DSProp.Lib: skipped 19, total 19
um/x64/dssec.lib: skipped 4, total 4
um/x64/dwmapi.lib: skipped 31, total 31
um/x64/dsound.lib: skipped 10, total 10
um/x64/drt.lib: skipped 21, total 21
um/x64/drttransport.lib: skipped 2, total 2
um/x64/drtprov.lib: skipped 9, total 9
um/x64/dpx.lib: skipped 11, total 11
um/x64/dnsrslvr.lib: skipped 4, total 4
um/x64/dnsrpc.lib: skipped 1, total 375
um/x64/dnsperf.lib: skipped 3, total 3
um/x64/dnscrcli.lib: skipped 0, total 4
um/x64/dnslib.lib: skipped 5, total 1392
um/x64/DnsAPI.Lib: skipped 277, total 277
um/x64/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x64/dmoguids.lib: skipped 0, total 0
um/x64/dinput8.lib: skipped 1, total 2
um/x64/dloadhelper.lib: skipped 0, total 3
um/x64/difxapi.lib: skipped 12, total 12
um/x64/dhcpsapi.lib: skipped 209, total 209
um/x64/DhcpCSvc6.Lib: skipped 22, total 22
um/x64/DhcpCSvc.Lib: skipped 67, total 67
um/x64/deviceaccess.lib: skipped 3, total 3
um/x64/dflayout.lib: skipped 1, total 1
um/x64/devmgr.lib: skipped 19, total 19
um/x64/devenum.lib: skipped 0, total 0
um/x64/ddraw.lib: skipped 13, total 13
um/x64/dciman32.lib: skipped 20, total 20
um/x64/dcomp.lib: skipped 6, total 6
um/x64/DbgEng.Lib: skipped 4, total 4
um/x64/DbgHelp.Lib: skipped 239, total 239
um/x64/davclnt.lib: skipped 22, total 22
um/x64/d3dcsx.lib: skipped 9, total 9
um/x64/d3dcsxd.lib: skipped 9, total 9
um/x64/d3dcompiler.lib: skipped 29, total 29
um/x64/d3d9.lib: skipped 14, total 14
um/x64/d3d11.lib: skipped 45, total 45
um/x64/d3d10_1.lib: skipped 29, total 29
um/x64/d3d10.lib: skipped 29, total 29
um/x64/d3d12.lib: skipped 14, total 14
um/x64/d2d1.lib: skipped 13, total 13
um/x64/cscapi.lib: skipped 6, total 6
um/x64/cscdll.lib: skipped 18, total 18
um/x64/cryptui.lib: skipped 54, total 54
um/x64/cryptdll.lib: skipped 20, total 20
um/x64/cryptxml.lib: skipped 19, total 19
um/x64/CryptNet.Lib: skipped 5, total 5
um/x64/Crypt32.Lib: skipped 240, total 240
um/x64/CoreMessaging.lib: skipped 30, total 30
um/x64/Credui.lib: skipped 22, total 22
um/x64/corrEngine.lib: skipped 0, total 0
um/x64/ComSvcs.Lib: skipped 17, total 17
um/x64/computestorage.lib: skipped 11, total 11
um/x64/computenetwork.lib: skipped 30, total 30
um/x64/computecore.lib: skipped 47, total 47
um/x64/compstui.lib: skipped 4, total 4
um/x64/CompPkgSup.lib: skipped 9, total 9
um/x64/ComDlg32.Lib: skipped 21, total 21
um/x64/clfsw32.lib: skipped 63, total 63
um/x64/ComCtl32.Lib: skipped 128, total 128
um/x64/ClusApi.Lib: skipped 284, total 284
um/x64/cldapi.lib: skipped 48, total 48
um/x64/cfgmgr32.lib: skipped 231, total 231
um/x64/Chakrart.lib: skipped 155, total 155
um/x64/clfsmgmt.lib: skipped 9, total 231
um/x64/CertPolEng.Lib: skipped 14, total 14
um/x64/certcli.lib: skipped 0, total 0
um/x64/CertIdl.Lib: skipped 0, total 1
um/x64/certca.lib: skipped 0, total 0
um/x64/BufferOverflowU.lib: skipped 5, total 16
um/x64/certadm.lib: skipped 41, total 41
um/x64/Cabinet.Lib: skipped 26, total 26
um/x64/BufferOverflow.lib: skipped 7, total 20
um/x64/bthprops.lib: skipped 40, total 40
um/x64/BluetoothApis.lib: skipped 96, total 96
um/x64/Bits.Lib: skipped 0, total 0
um/x64/bcrypt.lib: skipped 54, total 54
um/x64/basesrv.lib: skipped 6, total 6
um/x64/avrt.lib: skipped 20, total 20
um/x64/avifil32.Lib: skipped 74, total 74
um/x64/AuthZ.Lib: skipped 36, total 36
um/x64/aux_ulib.lib: skipped 1, total 5
um/x64/audiomediatypecrt.lib: skipped 2, total 27
um/x64/audioeng.lib: skipped 2, total 2
um/x64/audiobaseprocessingobject.lib: skipped 15, total 65
um/x64/appnotify.lib: skipped 2, total 2
um/x64/AudioBaseProcessingObjectV140.lib: skipped 16, total 69
um/x64/appmgr.lib: skipped 0, total 0
um/x64/appmgmts.lib: skipped 17, total 17
ucrt/x86/ucrtd.lib: skipped 1441, total 1441
ucrt/x86/ucrt.lib: skipped 1378, total 1378
um/x64/amstrmid.lib: skipped 0, total 0
ucrt/x86/libucrtd.lib: skipped 218, total 8547
um/x64/amsi.lib: skipped 9, total 9
um/x64/DbgModel.Lib: skipped 1, total 1
um/x64/ahadmin.lib: skipped 0, total 0
um/x64/advpack.Lib: skipped 84, total 84
ucrt/x86/libucrt.lib: skipped 671, total 8368
um/x64/AdvAPI32.Lib: skipped 782, total 782
um/x64/ADSIid.Lib: skipped 0, total 0
um/x64/AclUI.Lib: skipped 6, total 6
um/x86/xpsprint.lib: skipped 4, total 4
um/x64/api-ms-win-net-isolation-l1-1-0.lib: skipped 8, total 8
um/x86/xolehlp.lib: skipped 8, total 8
um/x86/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x86/xmllite.lib: skipped 6, total 6
um/x86/xinputuap.lib: skipped 8, total 8
um/x86/Xinput9_1_0.lib: skipped 5, total 5
um/x86/xinput.lib: skipped 8, total 8
um/x86/xaudio2_8.lib: skipped 7, total 7
um/x86/xaudio2.lib: skipped 9, total 9
um/x64/ActiveDS.Lib: skipped 27, total 27
um/x86/xaswitch.lib: skipped 1, total 24
um/x86/xapobase2_8.lib: skipped 4, total 157
um/x86/xapobase.lib: skipped 4, total 157
um/x86/WtsApi32.Lib: skipped 65, total 65
um/x86/WSock32.Lib: skipped 75, total 75
um/x86/wsmsvc.lib: skipped 3673, total 3673
um/x86/WSnmp32.Lib: skipped 51, total 51
um/x86/wuguid.lib: skipped 0, total 0
um/x86/wsdapi.lib: skipped 45, total 45
um/x86/wsclient.lib: skipped 30, total 30
um/x86/wscapi.lib: skipped 39, total 39
um/x86/wsbonline.lib: skipped 3, total 3
um/x86/WS2_32.Lib: skipped 180, total 180
um/x86/wsbapp_uuid.Lib: skipped 0, total 0
um/x86/Wow32.Lib: skipped 29, total 29
um/x86/workspaceax.lib: skipped 0, total 3
um/x86/wofutil.lib: skipped 11, total 11
um/x86/wmiutils.lib: skipped 0, total 0
um/x86/wmvcore.lib: skipped 20, total 20
um/x86/wmip.lib: skipped 45, total 45
um/x86/wmcodecdspuuid.lib: skipped 0, total 0
um/x86/Wldap32.Lib: skipped 245, total 245
um/x86/Wldp.Lib: skipped 17, total 17
um/x86/wlanapi.lib: skipped 68, total 68
um/x86/wlanui.lib: skipped 5, total 5
um/x86/winusb.lib: skipped 37, total 37
um/x86/WinTrust.Lib: skipped 145, total 145
um/x86/winsta.lib: skipped 169, total 169
um/x86/WinStrm.Lib: skipped 0, total 18
um/x86/winsqlite3.lib: skipped 248, total 248
um/x86/WinSpool.Lib: skipped 232, total 232
um/x86/winscard.lib: skipped 74, total 74
um/x86/winml.lib: skipped 1, total 1
um/x86/winsatapi.lib: skipped 0, total 0
um/x86/WinMM.Lib: skipped 191, total 191
um/x86/WinInet.Lib: skipped 319, total 319
um/x86/winfax.lib: skipped 56, total 56
um/x86/winhttp.lib: skipped 64, total 64
um/x86/windowssideshowguids.lib: skipped 0, total 0
um/x86/WindowsApp_downlevel.lib: skipped 3219, total 3219
um/x86/windowscodecs.lib: skipped 114, total 114
um/x86/WindowsApp.lib: skipped 3219, total 3219
um/x86/windows.networking.lib: skipped 1, total 1
um/x86/windows.data.pdf.lib: skipped 1, total 1
um/x86/WinBio.lib: skipped 60, total 60
um/x86/windows.ai.machinelearning.lib: skipped 1, total 1
um/x86/wiaservc.lib: skipped 55, total 55
um/x86/WiaGuid.Lib: skipped 0, total 0
um/x86/windows.ui.lib: skipped 2, total 2
um/x86/Wer.lib: skipped 145, total 145
um/x86/wevtapi.lib: skipped 45, total 45
um/x86/wiautil.lib: skipped 4, total 133
um/x86/wecapi.lib: skipped 17, total 17
um/x86/WebServices.lib: skipped 193, total 193
um/x86/wdstptc.lib: skipped 19, total 19
um/x86/wdsmc.lib: skipped 13, total 13
um/x86/websocket.lib: skipped 13, total 13
um/x86/wdspxe.lib: skipped 32, total 32
um/x86/wcmguid.lib: skipped 0, total 0
um/x86/wdsbp.lib: skipped 7, total 7
um/x86/wcmapi.lib: skipped 39, total 39
um/x86/wbemuuid.lib: skipped 0, total 0
um/x86/vstorinterface.lib: skipped 15, total 15
um/x86/vss_uuid.lib: skipped 0, total 0
um/x86/wdsClientAPI.LIB: skipped 58, total 58
um/x86/vscmgr.lib: skipped 0, total 0
um/x86/vssapi.lib: skipped 46, total 46
um/x86/Virtdisk.Lib: skipped 29, total 29
um/x86/Vfw32.Lib: skipped 127, total 127
um/x86/Version.Lib: skipped 12, total 12
um/x86/vds_uuid.lib: skipped 0, total 0
um/x86/VdmDbg.Lib: skipped 28, total 28
um/x86/vccomsup.lib: skipped 1, total 31
um/x86/Uxtheme.lib: skipped 78, total 78
um/x86/Uuid.Lib: skipped 0, total 0
um/x86/USP10.Lib: skipped 40, total 40
um/x86/User32.Lib: skipped 770, total 770
um/x86/UserEnv.Lib: skipped 72, total 72
um/x86/umpdddi.lib: skipped 92, total 92
um/x86/unicows.lib: skipped 1011, total 2540
um/x86/Urlmon.Lib: skipped 95, total 95
um/x86/ualapi.lib: skipped 10, total 10
um/x86/txfw32.lib: skipped 9, total 9
um/x86/UIAutomationCore.lib: skipped 99, total 99
um/x86/twain_32.lib: skipped 5, total 5
um/x86/twinapi.lib: skipped 0, total 0
um/x86/tspubplugincom.lib: skipped 1, total 8
um/x86/Traffic.Lib: skipped 22, total 22
um/x86/tokenbinding.lib: skipped 9, total 9
um/x86/TranscodeImageUID.lib: skipped 0, total 0
um/x86/tsec.lib: skipped 27, total 27
um/x86/Thunk32.Lib: skipped 66, total 66
um/x86/tdh.lib: skipped 24, total 24
um/x86/tbs.lib: skipped 21, total 21
um/x86/taskschd.lib: skipped 0, total 0
um/x86/Tapi32.Lib: skipped 278, total 278
um/x86/tapi32l.lib: skipped 1, total 255
um/x86/t2embed.lib: skipped 14, total 14
um/x86/Svcguid.Lib: skipped 0, total 0
um/x86/strsafe.lib: skipped 0, total 22
um/x86/strmiids.lib: skipped 0, total 0
um/x86/swdevice.lib: skipped 9, total 9
um/x86/strmbase.lib: skipped 156, total 1689
um/x86/structuredquery.lib: skipped 0, total 0
um/x86/Sti.Lib: skipped 16, total 16
um/x86/srpapi.lib: skipped 21, total 21
um/x86/SrClient.lib: skipped 1, total 33
um/x86/ssdpapi.lib: skipped 29, total 29
um/x86/SpOrder.Lib: skipped 2, total 2
um/x86/spoolss.lib: skipped 206, total 206
um/x86/SnmpAPI.Lib: skipped 38, total 38
um/x86/synchronization.lib: skipped 3, total 3
um/x86/slwga.lib: skipped 1, total 1
um/x86/slc.lib: skipped 40, total 40
um/x86/ShFolder.Lib: skipped 2, total 2
um/x86/ShLwApi.Lib: skipped 365, total 365
um/x86/shdocvw.lib: skipped 19, total 19
um/x86/shell32.lib: skipped 397, total 397
um/x86/shcore.lib: skipped 20, total 20
um/x86/Sfc.Lib: skipped 16, total 16
um/x86/SensorsUtils.lib: skipped 62, total 62
um/x86/SetupAPI.Lib: skipped 558, total 558
um/x86/sensorsapi.lib: skipped 0, total 0
um/x86/SensAPI.Lib: skipped 3, total 3
um/x86/sens.lib: skipped 3, total 3
um/x86/security.lib: skipped 36, total 36
um/x86/Secur32.Lib: skipped 96, total 96
um/x86/SearchSDK.lib: skipped 0, total 0
um/x86/ScrnSave.Lib: skipped 1, total 24
um/x86/ScrnSavW.Lib: skipped 1, total 24
um/x86/schannel.lib: skipped 35, total 35
um/x86/SCardDlg.Lib: skipped 5, total 5
um/x86/scesrv.lib: skipped 2, total 2
um/x86/scecli.lib: skipped 72, total 72
um/x86/sbtsv.lib: skipped 0, total 1
um/x86/sas.lib: skipped 1, total 1
um/x86/samsrv.lib: skipped 327, total 327
um/x86/SAPI.Lib: skipped 0, total 0
um/x86/samlib.lib: skipped 70, total 70
um/x86/runtimeobject.lib: skipped 60, total 60
um/x86/RTWorkQ.lib: skipped 34, total 34
um/x86/rtutils.lib: skipped 41, total 41
um/x86/Rtm.Lib: skipped 116, total 116
um/x86/rstrtmgr.lib: skipped 12, total 12
um/x86/rpcutil.lib: skipped 0, total 23
um/x86/rpcproxy.lib: skipped 5, total 5
um/x86/RpcRT4.Lib: skipped 534, total 534
um/x86/rpcexts.lib: skipped 58, total 58
um/x86/Rpcns4.Lib: skipped 62, total 62
um/x86/rometadata.lib: skipped 1, total 1
um/x86/resutils.lib: skipped 126, total 126
um/x86/rasuser.lib: skipped 5, total 5
um/x86/RASAPI32.Lib: skipped 148, total 148
um/x86/RASDlg.Lib: skipped 25, total 25
um/x86/query.lib: skipped 44, total 44
um/x86/qwave.lib: skipped 14, total 14
um/x86/quartz.lib: skipped 4, total 4
um/x86/slcext.lib: skipped 9, total 9
um/x86/Psapi.Lib: skipped 27, total 27
um/x86/propsys.lib: skipped 219, total 219
um/x86/ProjectedFSLib.lib: skipped 33, total 33
um/x86/prntvpt.lib: skipped 29, total 29
um/x86/powrprof.lib: skipped 112, total 112
um/x86/PortableDeviceGuids.lib: skipped 0, total 0
um/x86/PhotoAcquireUID.lib: skipped 0, total 0
um/x86/patchwiz.lib: skipped 4, total 4
um/x86/pathcch.lib: skipped 22, total 22
um/x86/Pdh.Lib: skipped 110, total 110
um/x86/PeerDist.lib: skipped 28, total 28
um/x86/p2pgraph.lib: skipped 40, total 40
um/x86/osptk.lib: skipped 0, total 0
um/x86/p2p.lib: skipped 112, total 112
um/x86/OneCore_downlevel.Lib: skipped 4802, total 4809
um/x86/OneCore_apiset.Lib: skipped 5156, total 5156
um/x86/OpenGL32.Lib: skipped 368, total 368
um/x86/OneCoreUAP_apiset.Lib: skipped 8217, total 8217
um/x86/OneCoreUAP.Lib: skipped 10498, total 10505
um/x86/ondemandconnroutehelper.lib: skipped 8, total 8
um/x86/olesvr32.lib: skipped 23, total 23
um/x86/OneCoreUAP_downlevel.Lib: skipped 4802, total 4809
um/x86/OlePro32.Lib: skipped 7, total 7
um/x86/OneCore.Lib: skipped 7543, total 7550
um/x86/OleDlg.Lib: skipped 23, total 23
um/x86/oledb.lib: skipped 0, total 0
um/x86/OleAut32.Lib: skipped 400, total 400
um/x86/OleAcc.Lib: skipped 20, total 20
um/x86/Ole32.Lib: skipped 432, total 432
um/x86/olecli32.lib: skipped 178, total 178
um/x86/odbccp32.lib: skipped 1, total 61
um/x86/odbc32.lib: skipped 176, total 176
um/x86/odbcbcp.lib: skipped 28, total 28
um/x86/OemLicense.lib: skipped 6, total 6
um/x86/objsel.lib: skipped 0, total 0
um/x86/ntstc_msvcrt.lib: skipped 357, total 6280
um/x86/ntvdm.lib: skipped 164, total 164
um/x86/ntstc_libcmt.lib: skipped 357, total 6280
um/x86/ntmarta.lib: skipped 44, total 44
um/x86/ntlanman.lib: skipped 23, total 23
um/x86/ntfrsapi.lib: skipped 33, total 33
um/x86/ntdsetup.lib: skipped 24, total 24
um/x86/ntdsatq.lib: skipped 47, total 47
um/x86/NtQuery.Lib: skipped 44, total 44
um/x86/ntdsa.lib: skipped 146, total 146
um/x86/NtDsAPI.Lib: skipped 120, total 120
um/x86/ntdll.lib: skipped 2047, total 2047
um/x86/nt.lib: skipped 0, total 6
um/x86/normaliz.lib: skipped 5, total 5
um/x86/newdev.lib: skipped 23, total 23
um/x86/ninput.lib: skipped 23, total 23
um/x86/NetSh.Lib: skipped 23, total 23
um/x86/netlib.lib: skipped 2, total 274
um/x86/NetAPI32.Lib: skipped 212, total 212
um/x86/ndproxystub.lib: skipped 0, total 0
um/x86/nddeapi.lib: skipped 28, total 28
um/x86/ncrypt.lib: skipped 136, total 136
um/x86/muiload.lib: skipped 1, total 69
um/x86/mtxdm.lib: skipped 1, total 1
um/x86/msxml6.lib: skipped 0, total 0
um/x86/ndfapi.lib: skipped 24, total 24
um/x86/Mtx.Lib: skipped 3, total 3
um/x86/MsWSock.Lib: skipped 28, total 28
um/x86/msvfw32.Lib: skipped 47, total 47
um/x86/msv1_0.lib: skipped 19, total 19
um/x86/MsXml2.Lib: skipped 0, total 0
um/x86/MSTask.Lib: skipped 22, total 22
um/x86/MSRating.Lib: skipped 32, total 32
um/x86/msports.lib: skipped 11, total 11
um/x86/mspbase.lib: skipped 164, total 1425
um/x86/mspatchc.lib: skipped 14, total 14
um/x86/MSImg32.Lib: skipped 3, total 3
um/x86/Msi.Lib: skipped 290, total 290
um/x86/msdmo.lib: skipped 15, total 15
um/x86/msdrm.lib: skipped 85, total 85
um/x86/mspatcha.lib: skipped 16, total 16
um/x86/msdelta.lib: skipped 15, total 15
um/x86/msdasc.lib: skipped 0, total 0
um/x86/MsCtfMonitor.lib: skipped 3, total 3
um/x86/Mscms.Lib: skipped 127, total 127
um/x86/MSAcm32.Lib: skipped 44, total 44
um/x86/MSAJApi.lib: skipped 558, total 558
um/x86/msaatext.lib: skipped 0, total 0
um/x86/MrmSupport.lib: skipped 24, total 24
um/x86/MqRt.Lib: skipped 47, total 47
um/x86/MqOA.Lib: skipped 0, total 0
um/x86/mprsnap.lib: skipped 46, total 46
um/x86/Mprapi.Lib: skipped 160, total 160
um/x86/MMC.Lib: skipped 1, total 16
um/x86/Mpr.Lib: skipped 43, total 43
um/x86/mmdevapi.lib: skipped 29, total 29
um/x86/mincore_downlevel.lib: skipped 451, total 451
um/x86/mincore.lib: skipped 4372, total 4372
um/x86/MgmtAPI.Lib: skipped 9, total 9
um/x86/Mfsrcsnk.lib: skipped 2, total 2
um/x86/mi.lib: skipped 2, total 2
um/x86/mfuuid.lib: skipped 0, total 0
um/x86/mfsensorgroup.lib: skipped 5, total 5
um/x86/mfplay.lib: skipped 1, total 1
um/x86/mfreadwrite.lib: skipped 5, total 5
um/x86/Mfcore.lib: skipped 38, total 38
um/x86/Mf.lib: skipped 75, total 75
um/x86/MDMRegistration.lib: skipped 12, total 12
um/x86/mdmlocalmanagement.lib: skipped 3, total 3
um/x86/mciole32.lib: skipped 11, total 11
um/x86/Mfplat.lib: skipped 150, total 150
um/x86/MAPI32.Lib: skipped 155, total 155
um/x86/magnification.lib: skipped 21, total 21
um/x86/mbnapi_uuid.lib: skipped 0, total 0
um/x86/Lz32.Lib: skipped 14, total 14
um/x86/locationapi.lib: skipped 0, total 0
um/x86/ktmw32.lib: skipped 44, total 44
um/x86/KSProxy.Lib: skipped 6, total 6
um/x86/ksuser.lib: skipped 8, total 8
um/x86/keycredmgr.lib: skipped 4, total 4
um/x86/kernel32legacylib.lib: skipped 6, total 545
um/x86/LoadPerf.Lib: skipped 14, total 14
um/x86/kernel32.Lib: skipped 1317, total 1317
um/x86/kerbcli.lib: skipped 0, total 3
um/x86/jsrt.lib: skipped 92, total 92
um/x86/irprops.lib: skipped 35, total 35
um/x86/iscsidsc.lib: skipped 80, total 80
um/x86/jetoledb.lib: skipped 0, total 0
um/x86/iphlpapi.lib: skipped 290, total 290
um/x86/Iprop.Lib: skipped 8, total 8
um/x86/int64.lib: skipped 0, total 11
um/x86/inseng.lib: skipped 7, total 7
um/x86/inkobjcore.lib: skipped 30, total 30
um/x86/infocardapi.Lib: skipped 18, total 18
um/x86/Imm32.Lib: skipped 82, total 82
um/x86/imgutil.Lib: skipped 9, total 9
um/x86/ImageHlp.Lib: skipped 150, total 150
um/x86/iesetup.lib: skipped 7, total 7
um/x86/icuuc.lib: skipped 2815, total 2815
um/x86/icuin.Lib: skipped 5108, total 5108
um/x86/Icmui.Lib: skipped 2, total 2
um/x86/Icm32.Lib: skipped 21, total 21
um/x86/IEPMAPI.Lib: skipped 1, total 29
um/x86/iashlpr.lib: skipped 12, total 12
um/x86/httpapi.lib: skipped 44, total 44
um/x86/Htmlhelp.Lib: skipped 1, total 11
um/x86/hrtfapo.lib: skipped 4, total 4
um/x86/hid.lib: skipped 44, total 44
um/x86/HLink.Lib: skipped 28, total 28
um/x86/hhsetup.lib: skipped 145, total 145
um/x86/gpmuuid.lib: skipped 0, total 0
um/x86/hbaapi.lib: skipped 93, total 93
um/x86/GlU32.Lib: skipped 52, total 52
um/x86/GPEdit.lib: skipped 10, total 10
um/x86/gdiplus.lib: skipped 630, total 630
um/x86/Gdi32.Lib: skipped 606, total 606
um/x86/glmf32.lib: skipped 134, total 134
um/x86/fxsutility.lib: skipped 2, total 2
um/x86/fwpuclnt.lib: skipped 276, total 276
um/x86/FrameDyn.Lib: skipped 604, total 604
um/x86/fontsub.lib: skipped 2, total 2
um/x86/fltLib.lib: skipped 29, total 29
um/x86/FrameDyd.Lib: skipped 606, total 606
um/x86/fileextd.lib: skipped 1, total 22
um/x86/feclient.lib: skipped 52, total 52
um/x86/FaultRep.Lib: skipped 16, total 16
um/x86/FhSvcCtl.lib: skipped 14, total 14
um/x86/evr.lib: skipped 9, total 9
um/x86/ElsCore.lib: skipped 5, total 5
um/x86/esent.lib: skipped 375, total 375
um/x86/els.lib: skipped 0, total 0
um/x86/ehstorguids.lib: skipped 0, total 0
um/x86/elfapi.lib: skipped 0, total 100
um/x86/eappprxy.lib: skipped 18, total 18
um/x86/easregprov.lib: skipped 2, total 2
um/x86/efswrt.lib: skipped 27, total 27
um/x86/eappcfg.lib: skipped 15, total 15
um/x86/dxtmsft.lib: skipped 0, total 0
um/x86/dxtrans.lib: skipped 6, total 6
um/x86/dxva2.lib: skipped 38, total 38
um/x86/dxguid.lib: skipped 0, total 0
um/x86/dxgi.lib: skipped 15, total 15
um/x86/dxcompiler.lib: skipped 2, total 2
um/x86/dwmapi.lib: skipped 31, total 31
um/x86/DSUIExt.Lib: skipped 33, total 33
um/x86/DtcHelp.Lib: skipped 3, total 23
um/x86/dststlog.lib: skipped 1, total 1
um/x86/DSProp.Lib: skipped 19, total 19
um/x86/dssec.lib: skipped 4, total 4
um/x86/dsound.lib: skipped 10, total 10
um/x86/drttransport.lib: skipped 2, total 2
um/x86/drtprov.lib: skipped 9, total 9
um/x86/drt.lib: skipped 21, total 21
um/x86/dwrite.lib: skipped 1, total 1
um/x86/dpx.lib: skipped 11, total 11
um/x86/dnsrslvr.lib: skipped 4, total 4
um/x86/dnsrpc.lib: skipped 1, total 379
um/x86/dnsperf.lib: skipped 3, total 3
um/x86/dnscrcli.lib: skipped 0, total 4
um/x86/DnsAPI.Lib: skipped 277, total 277
um/x86/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x86/dloadhelper.lib: skipped 0, total 3
um/x86/dnslib.lib: skipped 2, total 1397
um/x86/dmoguids.lib: skipped 0, total 0
um/x86/dinput8.lib: skipped 1, total 2
um/x86/dhcpsapi.lib: skipped 209, total 209
um/x86/DhcpCSvc.Lib: skipped 67, total 67
um/x86/difxapi.lib: skipped 12, total 12
um/x86/DhcpCSvc6.Lib: skipped 22, total 22
um/x86/deviceaccess.lib: skipped 3, total 3
um/x86/devenum.lib: skipped 0, total 0
um/x86/dflayout.lib: skipped 1, total 1
um/x86/dcomp.lib: skipped 6, total 6
um/x86/ddraw.lib: skipped 13, total 13
um/x86/dciman32.lib: skipped 20, total 20
um/x86/DbgHelp.Lib: skipped 237, total 237
um/x86/devmgr.lib: skipped 19, total 19
um/x86/DbgModel.Lib: skipped 1, total 1
um/x86/DbgEng.Lib: skipped 4, total 4
um/x86/d3dcsxd.lib: skipped 9, total 9
um/x86/davclnt.lib: skipped 22, total 22
um/x86/d3dcsx.lib: skipped 9, total 9
um/x86/d3d9.lib: skipped 14, total 14
um/x86/d3dcompiler.lib: skipped 29, total 29
um/x86/d3d12.lib: skipped 14, total 14
um/x86/d3d11.lib: skipped 45, total 45
um/x86/d3d10.lib: skipped 29, total 29
um/x86/d3d10_1.lib: skipped 29, total 29
um/x86/cscdll.lib: skipped 18, total 18
um/x86/cscapi.lib: skipped 6, total 6
um/x86/d2d1.lib: skipped 13, total 13
um/x86/cryptxml.lib: skipped 19, total 19
um/x86/cryptui.lib: skipped 54, total 54
um/x86/cryptdll.lib: skipped 20, total 20
um/x86/CryptNet.Lib: skipped 5, total 5
um/x86/corrEngine.lib: skipped 0, total 0
um/x86/Credui.lib: skipped 22, total 22
um/x86/ComSvcs.Lib: skipped 17, total 17
um/x86/Crypt32.Lib: skipped 240, total 240
um/x86/CoreMessaging.lib: skipped 30, total 30
um/x86/compstui.lib: skipped 4, total 4
um/x86/ComDlg32.Lib: skipped 21, total 21
um/x86/CompPkgSup.lib: skipped 9, total 9
um/x86/ClusApi.Lib: skipped 284, total 284
um/x86/clfsw32.lib: skipped 63, total 63
um/x86/ComCtl32.Lib: skipped 128, total 128
um/x86/clfsmgmt.lib: skipped 7, total 212
um/x86/cldapi.lib: skipped 48, total 48
um/x86/cfgmgr32.lib: skipped 231, total 231
um/x86/Chakrart.lib: skipped 155, total 155
um/x86/CertIdl.Lib: skipped 0, total 1
um/x86/CertPolEng.Lib: skipped 14, total 14
um/x86/certca.lib: skipped 0, total 0
um/x86/certcli.lib: skipped 0, total 0
um/x86/Cabinet.Lib: skipped 26, total 26
um/x86/certadm.lib: skipped 41, total 41
um/x86/BufferOverflowU.lib: skipped 1, total 14
um/x86/BufferOverflow.lib: skipped 1, total 20
um/x86/BluetoothApis.lib: skipped 96, total 96
um/x86/Bits.Lib: skipped 0, total 0
um/x86/bcrypt.lib: skipped 54, total 54
um/x86/bthprops.lib: skipped 40, total 40
um/x86/avrt.lib: skipped 20, total 20
um/x86/basesrv.lib: skipped 6, total 6
um/x86/AuthZ.Lib: skipped 36, total 36
um/x86/avifil32.Lib: skipped 74, total 74
um/x86/aux_ulib.lib: skipped 1, total 9
um/x86/audioeng.lib: skipped 2, total 2
um/x86/audiomediatypecrt.lib: skipped 3, total 32
um/x86/audiobaseprocessingobject.lib: skipped 13, total 70
um/x86/AudioBaseProcessingObjectV140.lib: skipped 14, total 74
um/x86/ASycFilt.Lib: skipped 1, total 1
um/x86/appnotify.lib: skipped 2, total 2
um/x86/appmgmts.lib: skipped 17, total 17
um/x86/appmgr.lib: skipped 0, total 0
um/x86/apidll.lib: skipped 2, total 2
um/x86/amstrmid.lib: skipped 0, total 0
um/x86/ahadmin.lib: skipped 0, total 0
um/x86/advpack.Lib: skipped 84, total 84
um/x86/amsi.lib: skipped 9, total 9
um/x86/AdvAPI32.Lib: skipped 782, total 782
um/x86/ADSIid.Lib: skipped 0, total 0
um/x86/ActiveDS.Lib: skipped 27, total 27
um/x86/AclUI.Lib: skipped 6, total 6
um/x86/api-ms-win-net-isolation-l1-1-0.lib: skipped 8, total 8
```
