# VS14.28 / Visual Studio 2019 / v142

## download

Visual Studio 2019 installer and release channel (used to install Visual Studio 2015 tools):
  - https://aka.ms/vs/16/release/vs_buildtools.exe
  - https://aka.ms/vs/16/release/channel

Install [components](https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019):
  - `Microsoft.VisualStudio.Component.VC.Tools.x86.x64`: MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.28)
  - `Microsoft.VisualStudio.Component.VC.CLI.Support`: C++/CLI support for v142 build tools (14.28)
  - `microsoft.visualstudio.component.vc.atl`: C++ ATL for latest v142 build tools (x86 & x64), version 16.4.29313.120
  - `microsoft.visualstudio.component.vc.atlmfc`: C++ MFC for latest v142 build tools (x86 & x64), version 16.4.29313.120
  - `Microsoft.VisualStudio.Component.Windows10SDK.18362`: Windows 10 SDK (10.0.18362.0), version 16.1.28829.92, usually bundled with Visual Studio 2019

(See [Dockerfile](../../Dockerfile))

This results in:
  - `C:\BuildTools\VC\Tools\MSVC\14.28.29910`: MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.28)
  - `C:\BuildTools\VC\Tools\MSVC\14.28.29910\atlmfc\lib\`: C++ MFC for latest v142 build tools (x86 & x64), version 16.4.29313.120
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.18362.0`: Windows 10 SDK (10.0.18362.0), version 16.1.28829.92, usually bundled with Visual Studio 2019
  - `C:\Program Files (x86)\Windows Kits\10\lib\10.0.19041.0`: Windows 10 SDK (10.0.19041.0), version ???, bundled with VS2019???

We'll ignore the following targets, if present:
  - `arm`
  - `arm64`
  - `store`
  - `onecore`
  - `ucrt_enclave`
  - `uwp`

## .lib/.obj

### compiler: 14.28.29910

```
e89f85e00ea9211eea7350f33249e321  14.28.29910/atlmfc/lib/x64/MFCM140.lib
824e34fec6836705a60641277aa2511b  14.28.29910/atlmfc/lib/x64/MFCM140U.lib
baab45367d8d62148b92b19c70086350  14.28.29910/atlmfc/lib/x64/MFCM140Ud.lib
5032d002825ad0bd2a390ea07847ba31  14.28.29910/atlmfc/lib/x64/MFCM140d.lib
cf8b94a8ff75bc9807e646faf4f36a16  14.28.29910/atlmfc/lib/x64/afxnmcd.lib
e5fe729e8e91da7f9d6e6781b3f2350f  14.28.29910/atlmfc/lib/x64/afxnmcdd.lib
86f68659d3415795dece42e37c3d618a  14.28.29910/atlmfc/lib/x64/atls.lib
6f821fedb3dcd7c02826b40595f4d342  14.28.29910/atlmfc/lib/x64/mfc140.lib
e3ef0f27390e93c5ef204cf1e7660ed7  14.28.29910/atlmfc/lib/x64/mfc140d.lib
c8f39d84f290afd40b14d7ec14270c68  14.28.29910/atlmfc/lib/x64/mfc140u.lib
d10b7841144edc9e71c96f7591e477ef  14.28.29910/atlmfc/lib/x64/mfc140ud.lib
6a4d8ca827d37776a0f267e7b6465ccf  14.28.29910/atlmfc/lib/x64/mfcs140.lib
3a7598a359f7f3ebe86c0ffb519ff840  14.28.29910/atlmfc/lib/x64/mfcs140d.lib
982daef1d1dfc30f2f7a23dba428fb5d  14.28.29910/atlmfc/lib/x64/mfcs140u.lib
c4479e61d5f119def5c027a039cc90a0  14.28.29910/atlmfc/lib/x64/mfcs140ud.lib
64eeb13b3d38bbee38d7a0b673ea4fc9  14.28.29910/atlmfc/lib/x64/nafxcw.lib
d05c440972097963ef58a7ea3f7ab914  14.28.29910/atlmfc/lib/x64/nafxcwd.lib
4ca347722c10a6ed9d66a2474a8f53f8  14.28.29910/atlmfc/lib/x64/uafxcw.lib
415bd30cacb3f7df8135de83dc64078f  14.28.29910/atlmfc/lib/x64/uafxcwd.lib
d26ce8479de0ad35c9d884c1ddab96b2  14.28.29910/atlmfc/lib/x86/MFCM140.lib
ebd7feacfcef0aa4f86e0280e7feb45e  14.28.29910/atlmfc/lib/x86/MFCM140d.lib
a6795d0f68d4d87e196686fe7266fd0f  14.28.29910/atlmfc/lib/x86/MFCM140u.lib
a5a6e0f14333733c12eae7d0bb56a0e6  14.28.29910/atlmfc/lib/x86/MFCM140ud.lib
6546466f4e093abe423533f543752729  14.28.29910/atlmfc/lib/x86/afxnmcd.lib
5280a9bd486401f3147cae07b7b53b06  14.28.29910/atlmfc/lib/x86/afxnmcdd.lib
cd0ab2709b4deafe68fd367bf5fa4553  14.28.29910/atlmfc/lib/x86/atls.lib
5cf0e86d83bca70f5966dc359c58f1a3  14.28.29910/atlmfc/lib/x86/mfc140.lib
7d6981bcabff3fbf27f3b6e1e0dd7c47  14.28.29910/atlmfc/lib/x86/mfc140d.lib
bc9715fcd9aaab454ab171041585f281  14.28.29910/atlmfc/lib/x86/mfc140u.lib
d30b1faea4e32bae1fede363635d1d72  14.28.29910/atlmfc/lib/x86/mfc140ud.lib
49cad67c0d6120d428233bd2e122f64f  14.28.29910/atlmfc/lib/x86/mfcs140.lib
c7bd15c1638cde76a2ec9236c8eb0adf  14.28.29910/atlmfc/lib/x86/mfcs140d.lib
aaa375a8651e35aa9b0e6370a9a07c39  14.28.29910/atlmfc/lib/x86/mfcs140u.lib
5f81452edabe38f6e3c6ac534de4974b  14.28.29910/atlmfc/lib/x86/mfcs140ud.lib
66033f92c8bd79f966c3b3261f21897d  14.28.29910/atlmfc/lib/x86/nafxcw.lib
76ae60d614ab2096cd91f9dabd0a00a9  14.28.29910/atlmfc/lib/x86/nafxcwd.lib
f8d04e0d2d10505d5b5ff5f58c089bd4  14.28.29910/atlmfc/lib/x86/uafxcw.lib
c6770129c59a3cd9e40dfa9b693736af  14.28.29910/atlmfc/lib/x86/uafxcwd.lib
72554e97bd0aad8b009bba443db8b0de  14.28.29910/lib/x64/aligned_new.lib
34908e791d21bde9e8625c864b50dd7a  14.28.29910/lib/x64/binmode.obj
f0838e27687de7550bbee911ce21ad4b  14.28.29910/lib/x64/chkstk.obj
08eacc11f6ac7ecb86cb60f057fc969e  14.28.29910/lib/x64/clang_rt.asan-preinit-x86_64.lib
afbe9a5ef1cf8a2e59a3793e5a7de53a  14.28.29910/lib/x64/clang_rt.asan-x86_64.lib
67e2543447a4f3493f1d9a2c8b5204ff  14.28.29910/lib/x64/clang_rt.asan_cxx-x86_64.lib
5725162c0b091201dda052ed2fb574f0  14.28.29910/lib/x64/clang_rt.asan_cxx_dbg-x86_64.lib
3a101aa56559e320f3b8679024e294ae  14.28.29910/lib/x64/clang_rt.asan_dbg-x86_64.lib
a87f84e1ad484f83700f47b8a9944e3f  14.28.29910/lib/x64/clang_rt.asan_dbg_dll_thunk-x86_64.lib
12cca6e7848f3a99dd5ad27a86e31930  14.28.29910/lib/x64/clang_rt.asan_dbg_dynamic-x86_64.lib
5a516684f00c768f60ddd3121fcdf62e  14.28.29910/lib/x64/clang_rt.asan_dbg_dynamic_runtime_thunk-x86_64.lib
8d7b72195c1d6737aa4411edb050c416  14.28.29910/lib/x64/clang_rt.asan_dll_thunk-x86_64.lib
9fcd771c73144af48499b7495cdd3463  14.28.29910/lib/x64/clang_rt.asan_dynamic-x86_64.lib
191b21305ec0d1ad8c323fd17d9ce158  14.28.29910/lib/x64/clang_rt.asan_dynamic_runtime_thunk-x86_64.lib
29125f0b22a2f28f2f7955e6b436b088  14.28.29910/lib/x64/clang_rt.builtins-x86_64.lib
670bdf446afb40a1729d3d5c32e58175  14.28.29910/lib/x64/clang_rt.fuzzer-x86_64.lib
543c85936f62c8791511a848431f61f3  14.28.29910/lib/x64/clang_rt.fuzzer_no_main-x86_64.lib
6bd27b29ef927370b379a4c53c4ae3ee  14.28.29910/lib/x64/clang_rt.profile-x86_64.lib
3a6e1cb237404798976cfbfd896dcb7e  14.28.29910/lib/x64/clang_rt.stats-x86_64.lib
17452e977be4d3d6031ca58b3165b0d0  14.28.29910/lib/x64/clang_rt.stats_client-x86_64.lib
0e9f4a3c5117a374c4c878c592fade9d  14.28.29910/lib/x64/clang_rt.ubsan_standalone-x86_64.lib
dafa035b811d0635a7d56596b78fbb9e  14.28.29910/lib/x64/clang_rt.ubsan_standalone_cxx-x86_64.lib
de8c0408581dafdede01b3a75ad15cb6  14.28.29910/lib/x64/commode.obj
260e2a58922089f235537c7382df4a8e  14.28.29910/lib/x64/comsupp.lib
fab01b691efcfdb67c9175d9138f2c3c  14.28.29910/lib/x64/comsuppd.lib
e394708c4cc53a86bad0c1ef38cd4ea3  14.28.29910/lib/x64/comsuppw.lib
4efaff21500ec5c2886b4ead62a4950f  14.28.29910/lib/x64/comsuppwd.lib
62159450ee60bb2fe9e0ad8b46d22d08  14.28.29910/lib/x64/concrt.lib
a9a68ba8c19eff39864c3ae0da66f8b4  14.28.29910/lib/x64/concrtd.lib
5f8282df11096095ec9ef4e4ff3f6fa6  14.28.29910/lib/x64/delayimp.lib
46d3c866b25bf030ced91101c4bf34ee  14.28.29910/lib/x64/exe_initialize_mta.lib
b5e258c4ae57d617d5dc5a5e2374d8b8  14.28.29910/lib/x64/invalidcontinue.obj
e478b6bfc360263faa4734c72d4d2486  14.28.29910/lib/x64/iso_stdio_wide_specifiers.lib
68723d550bf4803dc86d501787b53f8e  14.28.29910/lib/x64/legacy_stdio_definitions.lib
a348d91563820f203b67d849c7f3829b  14.28.29910/lib/x64/legacy_stdio_float_rounding.obj
19b9ef15db4c731fdd914ea132b393fa  14.28.29910/lib/x64/legacy_stdio_wide_specifiers.lib
5da7b36320abc640400fc7f1fb8ae89e  14.28.29910/lib/x64/libcmt.lib
6e7755501dc796f007d28fe451ee1929  14.28.29910/lib/x64/libcmtd.lib
dc8b122f33f11296b976970c0426cf34  14.28.29910/lib/x64/libconcrt.lib
0c3a8730baca1d7790f2a7f9d6f42735  14.28.29910/lib/x64/libconcrt1.lib
75c637ed314d773354f81fc9b6722f35  14.28.29910/lib/x64/libconcrtd.lib
305a223f68bc5f8a44f005ea76cd4b1c  14.28.29910/lib/x64/libconcrtd0.lib
1ed07e4163c92b67bccb6e64a0ab71b5  14.28.29910/lib/x64/libconcrtd1.lib
087000cc71848cfeb33936ae6467d268  14.28.29910/lib/x64/libcpmt.lib
f655844b913c0c86d96ec2ef1f094317  14.28.29910/lib/x64/libcpmt1.lib
9b29bbafd2d48d9a279ffec456438729  14.28.29910/lib/x64/libcpmtd.lib
765bb71f3409abd057fdb4aec3639c8d  14.28.29910/lib/x64/libcpmtd0.lib
3f72bcfcfe988eebfe9d75d1110595e0  14.28.29910/lib/x64/libcpmtd1.lib
8a46596b40fd6fe39a41bab2a2cde5be  14.28.29910/lib/x64/libomp.lib
a0ed3c08c2b54960f55d6243a50fc923  14.28.29910/lib/x64/libompd.lib
705fe048bc147c5b0f36be4c7aad88db  14.28.29910/lib/x64/libsancov.lib
257a919e77570b174fbd4e427aaa5039  14.28.29910/lib/x64/libvcasan.lib
c9cbd4b03d15a4c194c8db1226324cf6  14.28.29910/lib/x64/libvcasand.lib
821e19fccd01103fdfcdad50b6e92b39  14.28.29910/lib/x64/libvcruntime.lib
e08ed9e817fc1b3de5e1b1118533db88  14.28.29910/lib/x64/libvcruntimed.lib
4bddaea5d8fae2b09d36d8f52c0ddf48  14.28.29910/lib/x64/loosefpmath.obj
af6813c8c0e72219ff9f99086e758148  14.28.29910/lib/x64/msvcmrt.lib
28762185c9bfd8e061350f77ee253dd8  14.28.29910/lib/x64/msvcmrt_netcore.lib
3d71540cf08ee31825fc0a50d560f482  14.28.29910/lib/x64/msvcmrtd.lib
4b17732da58354b6b0ab28cf213108aa  14.28.29910/lib/x64/msvcmrtd_netcore.lib
ecbabb7526045ba40feae44f334ed3a8  14.28.29910/lib/x64/msvcprt.lib
9ac4bbf3e5e28088594ddd611a368e8d  14.28.29910/lib/x64/msvcprtd.lib
3d40cdca75bbbd4016f9aac869812081  14.28.29910/lib/x64/msvcrt.lib
5e26454d7bf72cb4fcbfea7d74bcc5e7  14.28.29910/lib/x64/msvcrtd.lib
dac322bd729b8d3c6798b618a550dbe8  14.28.29910/lib/x64/msvcurt.lib
02f5964ba7c57a05e8a9cac571dafab1  14.28.29910/lib/x64/msvcurt_netcore.lib
8e233cfbd677502543407601124d47b1  14.28.29910/lib/x64/msvcurtd.lib
7791c8290dc9e29a147df45d4a33e252  14.28.29910/lib/x64/msvcurtd_netcore.lib
076e40a6dec84ef2ec0ddec463fbff2e  14.28.29910/lib/x64/newmode.obj
7ebb06ccecf0337342ef115ad8d4ce7f  14.28.29910/lib/x64/noarg.obj
ccada2bb93a63e6caf52185c38b39fd0  14.28.29910/lib/x64/noenv.obj
307403166c631f99a1b59f2eefb1a582  14.28.29910/lib/x64/notelemetry.obj
da00d327d5020ab18468a559f1377d72  14.28.29910/lib/x64/nothrownew.obj
9251f97a9746df830eb08e491ef1bf7b  14.28.29910/lib/x64/oldnames.lib
39f5196c694a8b94147e8264b0b91e39  14.28.29910/lib/x64/pbinmode.obj
02de8b592f1741f9c129e7f99a4da2ac  14.28.29910/lib/x64/pcommode.obj
d850868e5f3b8d6232794cdc50f257b5  14.28.29910/lib/x64/pgobootrun.lib
04101ded339eb9c7e8b579d3c3a08ae1  14.28.29910/lib/x64/pgort.lib
d969d41255e4d5a293c841a1d407ab18  14.28.29910/lib/x64/pinvalidcontinue.obj
749cb8a97f57e3c7f93f912bf8aba69a  14.28.29910/lib/x64/plegacy_stdio_float_rounding.obj
934b30ca0dfe09306fb89e6f339a9a58  14.28.29910/lib/x64/pnewmode.obj
c177d62d758a9adc511a39d896910bbb  14.28.29910/lib/x64/pnoarg.obj
a91a43706d805fedcabd6f104a36b066  14.28.29910/lib/x64/pnoenv.obj
7264d7c2746897d75d3fccdf677fa806  14.28.29910/lib/x64/pnothrownew.obj
c175d9a7f0c4d7ec24ea40cceded5cd7  14.28.29910/lib/x64/psetargv.obj
85d9eadbedb232164286a836ce8c78c4  14.28.29910/lib/x64/pthreadlocale.obj
794c387fdaab707d1efd77a41e8ac3d9  14.28.29910/lib/x64/ptrustm.lib
e8857faf64f129563eeebac2e3406fe2  14.28.29910/lib/x64/ptrustmd.lib
65b32396d0056750decf17819d2b1051  14.28.29910/lib/x64/ptrustu.lib
61ae79b3ae123a403e62c023465668b7  14.28.29910/lib/x64/ptrustud.lib
b1870a3fee768aebd928f0bf6a59c738  14.28.29910/lib/x64/pwsetargv.obj
0546a38c51df59900938b927fbf1286e  14.28.29910/lib/x64/setargv.obj
74f356e2aba30f63f6da1feed1166eee  14.28.29910/lib/x64/threadlocale.obj
75443b07c72005ab4f08a4c6031e63d1  14.28.29910/lib/x64/vcamp.lib
abd0c43f3fd1bb9fffc8cc1ae3ac6d26  14.28.29910/lib/x64/vcampd.lib
d8ee5418cb3fe834b987172a67b0d58c  14.28.29910/lib/x64/vcasan.lib
cee46b03601e84fd7b9ee6a4717007e2  14.28.29910/lib/x64/vcasand.lib
fc9a2f7adf210221cae83d1c2402dbec  14.28.29910/lib/x64/vccorlib.lib
aab908bd746898df198184322f983c87  14.28.29910/lib/x64/vccorlibd.lib
396f12d8949158db090e5f0d6d2eaa43  14.28.29910/lib/x64/vcomp.lib
94ca5ac9488c7ceabba89b56d6eba85a  14.28.29910/lib/x64/vcompd.lib
f204556e330146b4437b4ab6565a3813  14.28.29910/lib/x64/vcruntime.lib
232e414fb83aa5fd1d49273372d26665  14.28.29910/lib/x64/vcruntimed.lib
3c9a95c9f96a8e188c77c1610a45bf3e  14.28.29910/lib/x64/wsetargv.obj
2ae047ba164d8b5bee455b601f2a4298  14.28.29910/lib/x86/aligned_new.lib
e7d141c91e0892b3eb4c407eef868aff  14.28.29910/lib/x86/binmode.obj
98a34080f71bc21d72dada39a01cce22  14.28.29910/lib/x86/chkstk.obj
bec77f698e68a10bebfce3c7b433ca6a  14.28.29910/lib/x86/clang_rt.asan-i386.lib
7608959b3a2ee2b37076216d97cc20ff  14.28.29910/lib/x86/clang_rt.asan-preinit-i386.lib
f7a5ef9c4bdac17ff1bbb25036e8dd35  14.28.29910/lib/x86/clang_rt.asan_cxx-i386.lib
767206c75fc9aaaa93b6f4e7a2064dc6  14.28.29910/lib/x86/clang_rt.asan_cxx_dbg-i386.lib
1bdc227940238d13e000b737670278a4  14.28.29910/lib/x86/clang_rt.asan_dbg-i386.lib
7247c1bd573610e48774528904b054ff  14.28.29910/lib/x86/clang_rt.asan_dbg_dll_thunk-i386.lib
df2c12ef27e6032fe16158da55f2f552  14.28.29910/lib/x86/clang_rt.asan_dbg_dynamic-i386.lib
8ba771e0cdb37afb8c63f02703acbe90  14.28.29910/lib/x86/clang_rt.asan_dbg_dynamic_runtime_thunk-i386.lib
181f116f0a1f3596139d9b49a292a1a0  14.28.29910/lib/x86/clang_rt.asan_dll_thunk-i386.lib
32a4b946251b7fa22bddd32a8e6f079d  14.28.29910/lib/x86/clang_rt.asan_dynamic-i386.lib
3a57307c6fe6fc7149fe9789410aec39  14.28.29910/lib/x86/clang_rt.asan_dynamic_runtime_thunk-i386.lib
635d012ceef517b8ba655b1003db5b67  14.28.29910/lib/x86/clang_rt.builtins-i386.lib
aef855db003f20004fce832660cb7d0a  14.28.29910/lib/x86/clang_rt.fuzzer-i386.lib
9f1a89b978df463ae3b53987e0695221  14.28.29910/lib/x86/clang_rt.fuzzer_no_main-i386.lib
e04303a5d63196e76d5bb47eb9fd5033  14.28.29910/lib/x86/clang_rt.profile-i386.lib
23e4ca30875f5cf2475804bc3c111de7  14.28.29910/lib/x86/clang_rt.stats-i386.lib
20bfc6cf5b90028bcf05c97395631216  14.28.29910/lib/x86/clang_rt.stats_client-i386.lib
70f148bd634d7b6a30fe65c42aa20a35  14.28.29910/lib/x86/clang_rt.ubsan_standalone-i386.lib
4444a998029b2cf37438b4aac8c81c02  14.28.29910/lib/x86/clang_rt.ubsan_standalone_cxx-i386.lib
de81493493f6e1ecb4e1ea75969e2467  14.28.29910/lib/x86/commode.obj
f99ad0fc229f500e7655be017d26d785  14.28.29910/lib/x86/comsupp.lib
0f0e244ffc33aba411eace6d972e2d19  14.28.29910/lib/x86/comsuppd.lib
11b6bcf89ae6f3460c2aa4dcd167dacc  14.28.29910/lib/x86/comsuppw.lib
7c3f9301852f7dc960fdfa34333680c0  14.28.29910/lib/x86/comsuppwd.lib
ab72ead23d08eccfea4ddd29743e6e8a  14.28.29910/lib/x86/concrt.lib
91f67ecdf952ed4ccd047d3258d8398b  14.28.29910/lib/x86/concrtd.lib
19c23289aa93f15158767a69b00ff198  14.28.29910/lib/x86/delayimp.lib
fe2f8281d6ed18f45815c01165271024  14.28.29910/lib/x86/exe_initialize_mta.lib
aa036f0e7730a4c13c4025eb8edb0636  14.28.29910/lib/x86/fp10.obj
4b2beeda92911ab5b26865fc2936ab4e  14.28.29910/lib/x86/invalidcontinue.obj
5b4ebb7f875bfa9d6576148158c4ecb0  14.28.29910/lib/x86/iso_stdio_wide_specifiers.lib
5ba7c5b0a887285975ed4c04e5cbf2ac  14.28.29910/lib/x86/legacy_stdio_definitions.lib
740a501321e82cc4465c9845f33d655b  14.28.29910/lib/x86/legacy_stdio_float_rounding.obj
3a563969d746af7e85ed8035f3f616a2  14.28.29910/lib/x86/legacy_stdio_wide_specifiers.lib
e8c6841efd38018ded2e2d336adcb100  14.28.29910/lib/x86/legacy_x86_flt_exceptions.lib
25f382f07dc35c0903f69c54a11c23e0  14.28.29910/lib/x86/libcmt.lib
54dd559e4ac2f575b22d2425c7f35dbb  14.28.29910/lib/x86/libcmtd.lib
88c1c0374446aef433743641a792cf85  14.28.29910/lib/x86/libconcrt.lib
a1ab2a893a8c0fe5a795b9abd3f6c730  14.28.29910/lib/x86/libconcrt1.lib
9e15a10fd7c44d3565b20f6f50d81ceb  14.28.29910/lib/x86/libconcrtd.lib
89fe1772f576fb2b294714e7299da990  14.28.29910/lib/x86/libconcrtd0.lib
b8e0342c22e1ff862628b1e8ac522095  14.28.29910/lib/x86/libconcrtd1.lib
a59b49f61cdb70ae785aaed02e62df55  14.28.29910/lib/x86/libcpmt.lib
e3a65d1e792ca9db4eea1e94e1e8ac62  14.28.29910/lib/x86/libcpmt1.lib
fe3efa74030a7406ae0f40c9abc8870f  14.28.29910/lib/x86/libcpmtd.lib
a005dbe8646c042e39c8e1afba1666fa  14.28.29910/lib/x86/libcpmtd0.lib
6376f1b3e5acb5d41de5bb23a49f79b0  14.28.29910/lib/x86/libcpmtd1.lib
63624dec60488aff815dad7e890a7231  14.28.29910/lib/x86/libomp.lib
aff167cbd3a053a1a38a039e4d9e294d  14.28.29910/lib/x86/libompd.lib
8cdba7bfd65b019674ef5cb6b1bb014b  14.28.29910/lib/x86/libsancov.lib
de7181586644ce4015f8b118c34df361  14.28.29910/lib/x86/libvcasan.lib
970cf3d2aaa4a4673faa1c27532ad17e  14.28.29910/lib/x86/libvcasand.lib
f3863b444473f27fbbe24294d890308f  14.28.29910/lib/x86/libvcruntime.lib
773ed5117c6cebca1cd1f0fe2e2f0deb  14.28.29910/lib/x86/libvcruntimed.lib
fe1a75bc543731712671052ae16a9b32  14.28.29910/lib/x86/loosefpmath.obj
480f240c4da04edffc490626660fd876  14.28.29910/lib/x86/msvcmrt.lib
5185884440b314037c64bcba1a092c42  14.28.29910/lib/x86/msvcmrt_netcore.lib
dfa8a91c2e1b760e5a4b435ff927b6e4  14.28.29910/lib/x86/msvcmrtd.lib
d90cc240f2dc958775634c3188ff39bf  14.28.29910/lib/x86/msvcmrtd_netcore.lib
4a8015b74a5cc8bbc688667d32c8eb9b  14.28.29910/lib/x86/msvcprt.lib
d9a53588f03b7d020e6687308b5b24c6  14.28.29910/lib/x86/msvcprtd.lib
8c88cc805660bb63026aca9b8a438614  14.28.29910/lib/x86/msvcrt.lib
4530fbb03b8cbd3a2f63b95b604ebc54  14.28.29910/lib/x86/msvcrtd.lib
305fb09954cb26650a30312bd9dd77de  14.28.29910/lib/x86/msvcurt.lib
5f0042ee05899967c15878381b629d81  14.28.29910/lib/x86/msvcurt_netcore.lib
90f63aa6e4189083b0ff3c0c2dbe94bd  14.28.29910/lib/x86/msvcurtd.lib
7b1648716dcfa6623dfcfab0e6281f16  14.28.29910/lib/x86/msvcurtd_netcore.lib
0e883c5e5a3368cb919c5588ca6034bf  14.28.29910/lib/x86/newmode.obj
cffb97ce1d86121f0d3131a1d62cb590  14.28.29910/lib/x86/noarg.obj
307a044842fc842e85ac70e8fc347db5  14.28.29910/lib/x86/noenv.obj
ca5c2d9489d36ef4543e80f02269fa58  14.28.29910/lib/x86/notelemetry.obj
89d6c05528c1366a9848d9d3d037a30d  14.28.29910/lib/x86/nothrownew.obj
c9ffc627b04a725d1d1840692655f0d7  14.28.29910/lib/x86/oldnames.lib
6e1250f3cca8209b519f661ee1f80d93  14.28.29910/lib/x86/pbinmode.obj
941ec07b300d05a019f6402c5a514236  14.28.29910/lib/x86/pcommode.obj
9c85cb8b79aaf09b2cae16a16a2e0a72  14.28.29910/lib/x86/pgobootrun.lib
4b4138efda76e3ec3cd438c3af113030  14.28.29910/lib/x86/pgort.lib
67da82c5193187878df73e4529ec4de5  14.28.29910/lib/x86/pinvalidcontinue.obj
6c9f22615089484a5fa0e6749039b599  14.28.29910/lib/x86/plegacy_stdio_float_rounding.obj
e02af0fa92cf7210399eba6d08b9ebc3  14.28.29910/lib/x86/pnewmode.obj
fec3289ff46c426778df0f51fd84cc6b  14.28.29910/lib/x86/pnoarg.obj
b4dafbe583e24899351244ee6ad5e0a4  14.28.29910/lib/x86/pnoenv.obj
2f6a53f9f2e85ad9fc481498629b9904  14.28.29910/lib/x86/pnothrownew.obj
7e7207cf3d2d09f4c4133d9a2f862397  14.28.29910/lib/x86/psetargv.obj
6cd64174379fffe008a7a6fa8950de10  14.28.29910/lib/x86/pthreadlocale.obj
c5e0d58c47273e01ea8d1defb2235e6a  14.28.29910/lib/x86/ptrustm.lib
7e0383d0252e1c71f45d5331905a07a8  14.28.29910/lib/x86/ptrustmd.lib
05ed7f59f4dc7a878fac0ef7ad447309  14.28.29910/lib/x86/ptrustu.lib
00eb6e0355e4e1c607055f692813001a  14.28.29910/lib/x86/ptrustud.lib
b3e4a6c4bd93f986fe9f23fae1eae184  14.28.29910/lib/x86/pwsetargv.obj
7b24786764cc45e8edd1c21d097b5852  14.28.29910/lib/x86/setargv.obj
294c8b0d7ece6d94d426dd9a41e397ec  14.28.29910/lib/x86/threadlocale.obj
4919eb1a41e52e1f1beea49e2dc80b10  14.28.29910/lib/x86/vcamp.lib
b9c78f08f5b6d1f3bce01f7cf1d1e097  14.28.29910/lib/x86/vcampd.lib
f7c0c28888df28f5d290d3daaabb68b0  14.28.29910/lib/x86/vcasan.lib
49591b2d652045bed4164b7d47480871  14.28.29910/lib/x86/vcasand.lib
743f924c5a1f5f1697cc919190da64b9  14.28.29910/lib/x86/vccorlib.lib
b3499853572d774024a610f27199e9fa  14.28.29910/lib/x86/vccorlibd.lib
1d3b20ac1d7efa025a7102b02d70504d  14.28.29910/lib/x86/vcomp.lib
8be4df35cf5de928f050ee650fbe53b8  14.28.29910/lib/x86/vcompd.lib
f3309cc69243bfbc3d8deff46699c2f1  14.28.29910/lib/x86/vcruntime.lib
f88f0027feaa865f4f18d9c6a5af2547  14.28.29910/lib/x86/vcruntimed.lib
657e1dade11eebcc9ca688f9936ea578  14.28.29910/lib/x86/wsetargv.obj
```

### ucrt: 10.0.18362.0

```
b6a72ce98efb57497ac847447a0f1ddf  10.0.18362.0/um/x86/NetAPI32.Lib
d73ce22e6524f9af34487c8ad8ac01f4  10.0.18362.0/um/x86/OleAut32.Lib
4d0bea00de66b8b344daa39734834a4b  10.0.18362.0/um/x86/olesvr32.lib
624f3cd3990fb6470537ba1862a9de03  10.0.18362.0/um/x86/ondemandconnroutehelper.lib
6dbef11a887f2bedfe6a0d16569fcb15  10.0.18362.0/um/x86/OneCoreUAP_apiset.Lib
0e2181c33680fe4ac2a63094cab3cdbe  10.0.18362.0/um/x86/prntvpt.lib
b09c49bab40ecab5a2589d316e580d87  10.0.18362.0/um/x86/ProjectedFSLib.lib
5772f2518e81a17810553d17ae156722  10.0.18362.0/um/x86/quartz.lib
0879f04a0fa09f942576038701e1e923  10.0.18362.0/um/x86/query.lib
dc807a4ffd6448f2712170119d7deab8  10.0.18362.0/um/x86/qwave.lib
0ba1058423a4ec13b8acc85a08290b2e  10.0.18362.0/um/x86/RASAPI32.Lib
13ff35f34e10aca5d21955b50ff3c7e0  10.0.18362.0/um/x86/RTWorkQ.lib
dbb0dfc30f095f397226af3bf1d241d9  10.0.18362.0/um/x86/samlib.lib
38bd92141db4b8c34cc263718189c4db  10.0.18362.0/um/x86/security.lib
5a1a4e16a009f1bacad587c95486fbd0  10.0.18362.0/um/x86/SensAPI.Lib
ba170838e67e2776d4b9f25a8967350f  10.0.18362.0/um/x86/shdocvw.lib
b555fb252b733fead07e01a930cf7724  10.0.18362.0/um/x86/ShFolder.Lib
331e05cc70c6aa3f87c1ac6ba3a308de  10.0.18362.0/um/x86/strmbase.lib
eb53f52b147bfd22af8ea22492b2dcef  10.0.18362.0/um/x86/strmiids.lib
46338bbfc8e91a21a0be3ab62b70480c  10.0.18362.0/um/x86/strsafe.lib
b3531b0fb4a1367b8861450e8a6b8979  10.0.18362.0/um/x86/structuredquery.lib
8b99d1b62a9b06da467ec841fbb3ce63  10.0.18362.0/um/x86/Svcguid.Lib
dc95bbcda860d9e966947511667856dd  10.0.18362.0/um/x86/tokenbinding.lib
5040cb23f6d4eb01e39c4c2b568dc4b9  10.0.18362.0/um/x86/Traffic.Lib
87373a937ff738463e1914d3687d225c  10.0.18362.0/um/x86/USP10.Lib
2f5649fa27d77d0d71c7904b51cf3a78  10.0.18362.0/um/x86/VdmDbg.Lib
ca631ae4efc1eaf5727876960a2d3a3b  10.0.18362.0/um/x86/Version.Lib
6d30717631bf6d3926a1878b0552d319  10.0.18362.0/um/x86/wdstptc.lib
3584b016ccbaeb19e04e6acc601898de  10.0.18362.0/um/x86/websocket.lib
bbe8649bfacb99daa4833dc8c54f2b56  10.0.18362.0/um/x86/wecapi.lib
4f53eb90ba2aaeafb66cea67c7b2f21c  10.0.18362.0/um/x86/WindowsApp.lib
bdf54c336c3d8d2e8378e29f6d631682  10.0.18362.0/um/x86/WindowsApp_downlevel.lib
216b07a4b5200cebedd3973f20e4974c  10.0.18362.0/um/x86/windowscodecs.lib
2a5f238491086e438f340637d85573db  10.0.18362.0/um/x86/winml.lib
da32de2dc8edd50189417d05a4203661  10.0.18362.0/um/x86/wsbapp_uuid.Lib
7fa95cd291ad070bd60a4d9accf36382  10.0.18362.0/um/x86/wscapi.lib
f52840b6c0795c121dabc87d951daa1e  10.0.18362.0/um/x86/wsbonline.lib
4a415afb42690c0f60f4a09a7ef0ae28  10.0.18362.0/um/x86/WS2_32.Lib
b513d29bfffaaf9f7161a0347b64f543  10.0.18362.0/um/x86/Wow32.Lib
c0624181457297a5387a55e9bc53888a  10.0.18362.0/um/x86/workspaceax.lib
f9f5629da66b3a3b1dfe610e2a9dfbec  10.0.18362.0/um/x86/wofutil.lib
a59027cf2ccedb50e8c4413ffe4cdd94  10.0.18362.0/um/x86/wmvcore.lib
e57520df22dbc6632cd14396f73fb70c  10.0.18362.0/um/x86/wmiutils.lib
d3f871caf786e6b92dfde635faaec09f  10.0.18362.0/um/x86/wmip.lib
3b87a470cc2dbfc17c2a5a227cdb0912  10.0.18362.0/um/x86/wmcodecdspuuid.lib
a9218082c268309ddd50d7146891251b  10.0.18362.0/um/x86/Wldp.Lib
ce708d71cf8fe6adcc6efe5cb6a7f60e  10.0.18362.0/um/x86/xpsprint.lib
c23705937fa20f3b39844b8dd240848b  10.0.18362.0/um/x86/xpsdocumenttargetprint.lib
ef080c35d2f9d4b8aad5db1914000b60  10.0.18362.0/um/x86/xolehlp.lib
1269d537de2408dcde7e466437abbf98  10.0.18362.0/um/x86/xmllite.lib
fc07c0348d6d49f3396fc84203e129e0  10.0.18362.0/um/x86/xinputuap.lib
3637deaab7a4e33c9d41ff3713478d86  10.0.18362.0/um/x86/Xinput9_1_0.lib
02afc77bded29fd0d58ea8ad1f15a5b1  10.0.18362.0/um/x86/xinput.lib
f8b81223f3c7846af957fedbba19e08d  10.0.18362.0/um/x86/xaudio2_8.lib
db867f83047ed6590e760f5c7455dadd  10.0.18362.0/um/x86/xaudio2.lib
ab59811a9c9bd9930d3efdb1da72928d  10.0.18362.0/um/x86/xaswitch.lib
76dd9e519806b89ecb50dddf5e08868a  10.0.18362.0/um/x86/xapobase2_8.lib
8e9ffe80a870bed2c0a3fa60d42d2195  10.0.18362.0/um/x86/xapobase.lib
deeb4293ab0e9687dd4e688632e6df4d  10.0.18362.0/um/x86/wuguid.lib
875f7da5e283c7b24420b4630b577910  10.0.18362.0/um/x86/WtsApi32.Lib
e8b08630fc3df8b49979bbd7b1e01702  10.0.18362.0/um/x86/WSock32.Lib
b91416ece6ed18c3f20d0ace11d124ff  10.0.18362.0/um/x86/wsmsvc.lib
5dcebd0bd66a458685b65c1afeae4912  10.0.18362.0/um/x86/WSnmp32.Lib
14b849ef002b5eb473d2628ebd0d88da  10.0.18362.0/um/x86/wsdapi.lib
f6a586b8879ec9325863794df0ca59a0  10.0.18362.0/um/x86/wsclient.lib
b1e40fee5b6a198667f8474fcb251041  10.0.18362.0/um/x86/Wldap32.Lib
5661caa7d9d1e51f6526a3bd0796ae30  10.0.18362.0/um/x86/wlanui.lib
a6cf890b6ad365c4c44a437eded60913  10.0.18362.0/um/x86/wlanapi.lib
43bf86e78a1c1c13865f7b6705395388  10.0.18362.0/um/x86/winusb.lib
444a5616af6a04753a34c94a20a8a78d  10.0.18362.0/um/x86/WinTrust.Lib
f7ba4d0a2befaf2a10d7600fa9e786e0  10.0.18362.0/um/x86/WinStrm.Lib
8267138a786b9a6e21e38ec452c338e7  10.0.18362.0/um/x86/winsqlite3.lib
30827caca1809bf9efd611b1b66ffe83  10.0.18362.0/um/x86/winsta.lib
6152bfec7cff08fb2cfe4693b35dbfc4  10.0.18362.0/um/x86/WinSpool.Lib
c67567a2a243a67b5f8f92811e5af104  10.0.18362.0/um/x86/winsatapi.lib
5e828dbcd328dd3624580401b0dad283  10.0.18362.0/um/x86/winscard.lib
91113bc10129ff0edbd34ff087b7d2ce  10.0.18362.0/um/x86/WinMM.Lib
6e70a82ef3118f9672516079ea222bb0  10.0.18362.0/um/x86/WinInet.Lib
4893065bd6f221883918ce0173607636  10.0.18362.0/um/x86/winhttp.lib
71f05f0d94cfcb8e763d09270576a6a0  10.0.18362.0/um/x86/winfax.lib
c2c04afadd0a4a9fbb0f116350ef99d8  10.0.18362.0/um/x86/windowssideshowguids.lib
75fd1500f46ab615861cfe500fc1e658  10.0.18362.0/um/x86/windows.ui.lib
5a2c884ea200cac475f21f430a531c0e  10.0.18362.0/um/x86/windows.networking.lib
16fd264a2640fc1dcc3fe33d1a356152  10.0.18362.0/um/x86/windows.data.pdf.lib
49fd194993bbfd2c9d6ee16d5c5443b4  10.0.18362.0/um/x86/windows.ai.machinelearning.lib
8af55cf55379e664cf21836cbcbbfb7f  10.0.18362.0/um/x86/WinBio.lib
0a1002b50b3ba8f6aa09c12d06abc933  10.0.18362.0/um/x86/wiautil.lib
4bccaff695b38b10f4872e9533e6849f  10.0.18362.0/um/x86/wiaservc.lib
c9463b3cf341d340cb0a226dbf639f80  10.0.18362.0/um/x86/WiaGuid.Lib
a400e19e56eb72fe0393c08e1898a40c  10.0.18362.0/um/x86/wevtapi.lib
099d07f5a28334f0bfbd744eeba293af  10.0.18362.0/um/x86/Wer.lib
3c31d1d3d4dda1f2ebf46f101bd6f406  10.0.18362.0/um/x86/WebServices.lib
27a25bc22e65b01fef4c7076fb82c4ce  10.0.18362.0/um/x86/webauthn.lib
ec0071b97cd6e1a9c54f11532d862717  10.0.18362.0/um/x86/wdspxe.lib
5ff5fffbe02388fcad98cf9e7921daad  10.0.18362.0/um/x86/wdsmc.lib
10c467f0129aac5392cd4100d9cca764  10.0.18362.0/um/x86/wdsClientAPI.LIB
c33dd73f91c482e303363cbd7d2541d7  10.0.18362.0/um/x86/wdsbp.lib
1cf13a6fe759470b471207d1275cc4e3  10.0.18362.0/um/x86/wcmguid.lib
200e36ad82aa4ca6f8512528a23e4865  10.0.18362.0/um/x86/wcmapi.lib
652069e56080ed8bbc59f9d22d0ac2b6  10.0.18362.0/um/x86/wbemuuid.lib
d53e5a00fbaa612c32d3c37daae04b02  10.0.18362.0/um/x86/vstorinterface.lib
4c1816f23bf8e475d534c02d35843e3f  10.0.18362.0/um/x86/vss_uuid.lib
1c29524e7f20429610a2afc9c3783c9d  10.0.18362.0/um/x86/vssapi.lib
d018f178565b87ee547c869f6e43b6e7  10.0.18362.0/um/x86/vscmgr.lib
27f3014b6fa6e6dcec3f2662f90b4b26  10.0.18362.0/um/x86/Virtdisk.Lib
9d3b4c92710b62592333ff9cce747d86  10.0.18362.0/um/x86/Vfw32.Lib
0805d0fddc91a85633e42b231eedde3c  10.0.18362.0/um/x86/vds_uuid.lib
8a60a57e5e33e7560e8fae965057bda4  10.0.18362.0/um/x86/vccomsup.lib
f53eb629c8754cf33f4a90204663f758  10.0.18362.0/um/x86/Uxtheme.lib
bf3a585e6c21d96644156ba78c0d9e65  10.0.18362.0/um/x86/UserEnv.Lib
63bc7d5e8bfeb11539f512dea81dc2f5  10.0.18362.0/um/x86/Uuid.Lib
456971510b9ac6fa3dfa4e4b4e5488f6  10.0.18362.0/um/x86/User32.Lib
b0729d790289e9bc8fdc626c48ae2378  10.0.18362.0/um/x86/Urlmon.Lib
c117cf90f21707ad6a46638cbba990cc  10.0.18362.0/um/x86/unicows.lib
dc5a4f43d2939bfcca71707a93f044e2  10.0.18362.0/um/x86/umpdddi.lib
e894fb350e3feadbac1d24ef89f8ae30  10.0.18362.0/um/x86/UIAutomationCore.lib
92208d12930e9c2af4e9df42a9fd9ef8  10.0.18362.0/um/x86/ualapi.lib
d914d700015340b230a88e4a324ea358  10.0.18362.0/um/x86/txfw32.lib
33d6eb8b2ef38ec681d5aff5d95a88fd  10.0.18362.0/um/x86/twinapi.lib
07a85e78e6fedaf76d51efaf01eacecd  10.0.18362.0/um/x86/twain_32.lib
44f9ca27f8176e2363a2cd7c8f353ca7  10.0.18362.0/um/x86/tspubplugincom.lib
83e3a61ec19043667f8d507c2483de35  10.0.18362.0/um/x86/tsec.lib
38ebb2ddc343994049673242907d48e4  10.0.18362.0/um/x86/TranscodeImageUID.lib
8d647f2cfef558b4eb8c8dd0986d71ab  10.0.18362.0/um/x86/Thunk32.Lib
e12dfe24e9fc1e82b9a65812486ed733  10.0.18362.0/um/x86/tdh.lib
25253db8067f78686c204b87537f2fca  10.0.18362.0/um/x86/tbs.lib
32a995e5ab189e8ef4129ddce16fa06d  10.0.18362.0/um/x86/taskschd.lib
607f4d399dccc950cbb35f4a6f8a9494  10.0.18362.0/um/x86/tapi32l.lib
2eb01036fa9c92c8c8b37b023731742d  10.0.18362.0/um/x86/Tapi32.Lib
20dafa9084fb199775c56b5cfe9ab309  10.0.18362.0/um/x86/t2embed.lib
7c302cd09570e4e45d101ffed2af5466  10.0.18362.0/um/x86/synchronization.lib
ff5031270cb199419e3a8f18e1acf6a5  10.0.18362.0/um/x86/swdevice.lib
2f063f43ddb28e618da8d0bd0641b07c  10.0.18362.0/um/x86/Sti.Lib
4a6423289181d3a8d4b5aa3cc10dd96f  10.0.18362.0/um/x86/ssdpapi.lib
39c5c52ddab6d158f6f79c2132326330  10.0.18362.0/um/x86/srpapi.lib
bf0884cd9a9479cdbc27e76fd9d5e474  10.0.18362.0/um/x86/SrClient.lib
7d506322b02e5a2de6bcc2b56e20488a  10.0.18362.0/um/x86/SpOrder.Lib
6139973993f945275c679092a22f5532  10.0.18362.0/um/x86/spoolss.lib
10a7383b8d282712046bf5f258126d84  10.0.18362.0/um/x86/SnmpAPI.Lib
69582ca6a17f03b996f18d33773c68cb  10.0.18362.0/um/x86/slwga.lib
52063babfd759b4d0d4daa3e6310ff1c  10.0.18362.0/um/x86/slcext.lib
498e358a58edeaad71c373bf951a8015  10.0.18362.0/um/x86/slc.lib
006f7fdaf12b8d398e715bcd1f8ea9a3  10.0.18362.0/um/x86/ShLwApi.Lib
112f646801d32f1e42a2465d14fa4b7b  10.0.18362.0/um/x86/shell32.lib
fb7d9eee6f4d1f4e3655ea89660310c2  10.0.18362.0/um/x86/shcore.lib
b79dae9346ae1a77681da6eb427d15b8  10.0.18362.0/um/x86/Sfc.Lib
2c91f91f58046888ca316cba4106def3  10.0.18362.0/um/x86/SetupAPI.Lib
f9aa2f4eaa8f16ab1871ff585cc99cd5  10.0.18362.0/um/x86/SensorsUtils.lib
77df966e3f56b62045933defd3af0cac  10.0.18362.0/um/x86/sensorsapi.lib
1fee44f569c7964980272f8229138198  10.0.18362.0/um/x86/sens.lib
616a5471df16db9f2a23ee78a9d5bad8  10.0.18362.0/um/x86/Secur32.Lib
61851edb355c03962f80e3192de19f86  10.0.18362.0/um/x86/SearchSDK.lib
e665a56389890267e66c8fd00ace3844  10.0.18362.0/um/x86/ScrnSavW.Lib
00e963a2168c449d92fbcf7eef36ffc5  10.0.18362.0/um/x86/ScrnSave.Lib
0c3c4f40d5c04f2e27105ac66cb4e5ae  10.0.18362.0/um/x86/schannel.lib
a171e3daf5817c41e4261dcca9d621c9  10.0.18362.0/um/x86/scesrv.lib
e912640c8625586e0f6974a3aabab9f0  10.0.18362.0/um/x86/scecli.lib
0c3c0f33b116677d96e46a86a560a946  10.0.18362.0/um/x86/SCardDlg.Lib
09b4ee3a99206a54558bd01ccfadcc4c  10.0.18362.0/um/x86/sbtsv.lib
c3af15ee859f73b4a1e7bb64ba4bb9fa  10.0.18362.0/um/x86/sas.lib
8d5f64b9b9d9f0de2ce88d639c23a3a3  10.0.18362.0/um/x86/SAPI.Lib
b40c89d433122a6c2452cd146f75aa67  10.0.18362.0/um/x86/samsrv.lib
f376658aaa4559833f5a5ac7840153f4  10.0.18362.0/um/x86/runtimeobject.lib
6905a2b7d1d63f1f2e4e0a4363069e82  10.0.18362.0/um/x86/rtutils.lib
3486bc64da6564910c148eefa54fb545  10.0.18362.0/um/x86/Rtm.Lib
25cb6f179c3cda798436f6d37ee23466  10.0.18362.0/um/x86/rstrtmgr.lib
c9f22a4dba616e590a59ddc13c885761  10.0.18362.0/um/x86/RpcRT4.Lib
4d936a826c5cccc7f2e86fbe48fb83be  10.0.18362.0/um/x86/rpcutil.lib
09c008220e3e3f9620c630459681ffdb  10.0.18362.0/um/x86/rpcproxy.lib
00da45b2f51e4b0a2c2b0617c3ae56e9  10.0.18362.0/um/x86/Rpcns4.Lib
50535faedabeadbbcd747ac465b8fb5a  10.0.18362.0/um/x86/rpcexts.lib
0b8d08c31a94c5fc30d6839ac5ea35fb  10.0.18362.0/um/x86/rometadata.lib
0350c98fdc9a60fbfdeb7c1b4b419f11  10.0.18362.0/um/x86/resutils.lib
73b5ffe2b3826bbf0fee314578aada8b  10.0.18362.0/um/x86/rasuser.lib
cc56b3ddd76084e1faa5566bf248c3c9  10.0.18362.0/um/x86/RASDlg.Lib
5614791f9cabd8317661ddf6cc038707  10.0.18362.0/um/x86/Psapi.Lib
f12a1e9216a738be4763862843a642f0  10.0.18362.0/um/x86/propsys.lib
e01c96e2c20971cb761cf2e9d1c5ae2b  10.0.18362.0/um/x86/powrprof.lib
c300fa3170c969729adb4f18ddb230da  10.0.18362.0/um/x86/PortableDeviceGuids.lib
ba9a8a5e3e5a740c6d958c47b7c20d5c  10.0.18362.0/um/x86/PhotoAcquireUID.lib
80385dc5d889aa0b7ef08b4da1f00499  10.0.18362.0/um/x86/PeerDist.lib
d963f26dd268707353b7150935be1241  10.0.18362.0/um/x86/Pdh.Lib
a82c03ff1578e129ca0af7df524274e9  10.0.18362.0/um/x86/pathcch.lib
f21e2b52355cccb8bdeda7b49c7ad2f4  10.0.18362.0/um/x86/patchwiz.lib
b7703d33f5a5d38fb3711faad3510749  10.0.18362.0/um/x86/p2pgraph.lib
792c5ac8ff5aa419433ca9069c03a7cf  10.0.18362.0/um/x86/p2p.lib
7406d47eff8b0dd3bb16e84b18002a44  10.0.18362.0/um/x86/osptk.lib
2acb45eaffbda7476a0162533d34d896  10.0.18362.0/um/x86/OpenGL32.Lib
4a4b212e4c8a2840779b1e4a2d275b77  10.0.18362.0/um/x86/OneCore_downlevel.Lib
f4e03c5fae6c4d4a3e8faa0a5669caa4  10.0.18362.0/um/x86/OneCore_apiset.Lib
320a005c8026af46cb1cd27c7604d559  10.0.18362.0/um/x86/OneCoreUAP_downlevel.Lib
86873e2e4ac3c8d2a2921ceddddb38c4  10.0.18362.0/um/x86/OneCoreUAP.Lib
78b0dc77554ff701f65ce058e4f43278  10.0.18362.0/um/x86/OneCore.Lib
2bdbf2190e880db2aede88e506d1318c  10.0.18362.0/um/x86/OlePro32.Lib
f24003acab2b2aca596afca5a7fa912f  10.0.18362.0/um/x86/OleDlg.Lib
042205a803a71642c88f1ffa6d0a80fe  10.0.18362.0/um/x86/oledb.lib
28e0f3c7197b19d304cbe0250839bc37  10.0.18362.0/um/x86/olecli32.lib
6288fa64b5fb046f7173fdafc9ffe91e  10.0.18362.0/um/x86/OleAcc.Lib
5d4828bdb069b955a251ddc0011bdc9a  10.0.18362.0/um/x86/Ole32.Lib
0278e849d722b55739f3295f52ace4a2  10.0.18362.0/um/x86/OemLicense.lib
a23787bacfa039e5471899b0b29483c7  10.0.18362.0/um/x86/odbccp32.lib
bed152e5a9d56b27ed3b9d88e09671c9  10.0.18362.0/um/x86/odbcbcp.lib
ec0044fa2b21f18da75183b8e0252dfa  10.0.18362.0/um/x86/odbc32.lib
bb08d9dcd3dd7781e1c117cd10802d1a  10.0.18362.0/um/x86/objsel.lib
586437b75cdfb4187abd00aa7f2642d2  10.0.18362.0/um/x86/ntvdm.lib
2c13ce077d1f4ee69acb426333890c5c  10.0.18362.0/um/x86/ntstc_msvcrt.lib
f8c71fbff4f9d87e8c525006f9d0ce16  10.0.18362.0/um/x86/ntstc_libcmt.lib
0879f04a0fa09f942576038701e1e923  10.0.18362.0/um/x86/NtQuery.Lib
af7d23498bf4c2ce1b363df0c62b48ff  10.0.18362.0/um/x86/ntmarta.lib
b49e28956a474a175ed0219f71d18971  10.0.18362.0/um/x86/ntlanman.lib
a66ca325a435f2a6413b49c7c2ef0624  10.0.18362.0/um/x86/ntfrsapi.lib
d8c421265ed172b5d000bd2b08533ee1  10.0.18362.0/um/x86/ntdsetup.lib
30120c583efcd8f5f1c74a9dff608c0d  10.0.18362.0/um/x86/ntdsatq.lib
fe7a8222222245a05f9ee134ac95a7a9  10.0.18362.0/um/x86/NtDsAPI.Lib
45f61ad3349305e8148c8305cb2e9b94  10.0.18362.0/um/x86/ntdsa.lib
0d9fc79a5fe6bbe073d6d11e8bca92ba  10.0.18362.0/um/x86/ntdll.lib
d22595b6a07cc2c168d42326efa9654c  10.0.18362.0/um/x86/nt.lib
42b190ee0b7b98310a0eb3e39bbd18f4  10.0.18362.0/um/x86/normaliz.lib
3a4cd6f3c51357524677a2856abb28ea  10.0.18362.0/um/x86/ninput.lib
2e2a4e549c2bcee72ee5a09959cd1441  10.0.18362.0/um/x86/newdev.lib
2de96931f9311d8a91e4ed241b1f02ff  10.0.18362.0/um/x86/NetSh.Lib
684a3c3832fd926eaf856976d973fc23  10.0.18362.0/um/x86/netlib.lib
16ce495a637f8080fe9a808038446432  10.0.18362.0/um/x86/ndproxystub.lib
bed79e7d0cb5bf0e7d3d762ad7b2f1e9  10.0.18362.0/um/x86/ndfapi.lib
b34f57c9d08939bed1ecceb26a91fc45  10.0.18362.0/um/x86/nddeapi.lib
d5768167a3aa1d95f83f07f3848375ac  10.0.18362.0/um/x86/ncrypt.lib
42bf813ae93ee5547dbe90e28defc553  10.0.18362.0/um/x86/muiload.lib
d79b20cdc1b8f14435c44aff6355fabf  10.0.18362.0/um/x86/mtxdm.lib
e8f813d2fb29656a50127b9e40cda1fe  10.0.18362.0/um/x86/Mtx.Lib
21b53f5cd658719a5092cad30f69bc32  10.0.18362.0/um/x86/msxml6.lib
48a98866dddb88197076b8a7b49e8680  10.0.18362.0/um/x86/MsXml2.Lib
e835179864cd4f0dcdf9fbcfd3868b9a  10.0.18362.0/um/x86/MsWSock.Lib
7797076553c586d89ee545f92e7b9dff  10.0.18362.0/um/x86/msvfw32.Lib
dac5e9e2fa9ede4a3d49608c992296cc  10.0.18362.0/um/x86/msv1_0.lib
8fde8b202ea2ab0535f3f8069281e901  10.0.18362.0/um/x86/MSTask.Lib
38d04d003b011919c7898e77e9cbe307  10.0.18362.0/um/x86/MSRating.Lib
96781c32e7d31e54bb8f4f8d13c3c1e4  10.0.18362.0/um/x86/msports.lib
02157ae6d8240cd40cff245325096a8e  10.0.18362.0/um/x86/mspbase.lib
d2deaf0a90f67667e0f246d13e211b61  10.0.18362.0/um/x86/mspatchc.lib
a49533a916e116daff1e2bbb893b3d54  10.0.18362.0/um/x86/mspatcha.lib
00f3843fe25d94758ecb719cf7fc2368  10.0.18362.0/um/x86/MSImg32.Lib
571714a036f93fa369e37b9586dcb7c2  10.0.18362.0/um/x86/Msi.Lib
7878bcfa12593df916bfbbfa04a46fa3  10.0.18362.0/um/x86/msdrm.lib
e4c2808aa1938e7afb5b15a8cc9661f4  10.0.18362.0/um/x86/msdmo.lib
b80487cc83d38c9ccf1fd6b4b0edaec4  10.0.18362.0/um/x86/msdelta.lib
de1e026d6c3419cd4d712f9f17d836e7  10.0.18362.0/um/x86/msdasc.lib
dfe732bdcddb769943dce657f0f5814d  10.0.18362.0/um/x86/MsCtfMonitor.lib
2502fb63092cd8b0c200936eabc3e95a  10.0.18362.0/um/x86/Mscms.Lib
9d6417aa70051451609c6a6dc993852a  10.0.18362.0/um/x86/MSAJApi.lib
b808f92aea17f6cc1e2a979b52722d06  10.0.18362.0/um/x86/MSAcm32.Lib
7dc6f12554e55dcd151cb8b4f4c9e98b  10.0.18362.0/um/x86/msaatext.lib
fb92a1058fbb2cbfdec0eabc94f72124  10.0.18362.0/um/x86/MrmSupport.lib
d363a3e320ca2442ce2c006a114c6622  10.0.18362.0/um/x86/MqRt.Lib
367d38d8746851aad8a6484ea65942da  10.0.18362.0/um/x86/MqOA.Lib
a2ae16a24ae238ebcccc3b9fc8e988fa  10.0.18362.0/um/x86/mprsnap.lib
84f79bb83d303af9093ef8a7e9f36119  10.0.18362.0/um/x86/Mprapi.Lib
ab4797b1992bd8259efc28d74272de69  10.0.18362.0/um/x86/Mpr.Lib
391d0ab816aa5ac131061e0b8dc4b4e6  10.0.18362.0/um/x86/mmdevapi.lib
dc357b580051c67dbef75b61c1d9877b  10.0.18362.0/um/x86/MMC.Lib
119ba0e3acbce9fe86cb6c36c6354fa0  10.0.18362.0/um/x86/mincore_downlevel.lib
296939400f8150523d347cafb0ad0f75  10.0.18362.0/um/x86/mincore.lib
887af0ad9087d11f27a04fc5edcd919e  10.0.18362.0/um/x86/mi.lib
13529f7dbd06eee62389e20442a7951b  10.0.18362.0/um/x86/MgmtAPI.Lib
e297a5afa7c78f0f0c7d7c8b1fbd037c  10.0.18362.0/um/x86/mfuuid.lib
0a410c77030eeccd1be92d28046406d5  10.0.18362.0/um/x86/Mfsrcsnk.lib
67a462234682176a8dba65681f1db93a  10.0.18362.0/um/x86/mfsensorgroup.lib
8cea5b4b72d5474cf4f305734e3512b8  10.0.18362.0/um/x86/mfreadwrite.lib
a1c682abf43633c140530e5ec449658c  10.0.18362.0/um/x86/mfplay.lib
e8238e297277d4fcc29dd9968e9ccfaa  10.0.18362.0/um/x86/Mfplat.lib
ba3dab5ff91c193f691357b629e5e45c  10.0.18362.0/um/x86/Mfcore.lib
bf3131b7770460a0e29cfd2976421741  10.0.18362.0/um/x86/Mf.lib
0a59281067d8f38337fc3cebf3497c86  10.0.18362.0/um/x86/MDMRegistration.lib
da3d939da0ad042e6c4aa6b5789278b2  10.0.18362.0/um/x86/mdmlocalmanagement.lib
70a6f55aeb26bebe3cb1a475790dd17f  10.0.18362.0/um/x86/mciole32.lib
138f953b0ad356f32fc784bb1542f605  10.0.18362.0/um/x86/mbnapi_uuid.lib
a6e6e05d860088962793f0e0fb809deb  10.0.18362.0/um/x86/MAPI32.Lib
bbc2fde45bcec4edea90a01bc822ae5e  10.0.18362.0/um/x86/magnification.lib
8d76686011985598227e281e0638c6e7  10.0.18362.0/um/x86/Lz32.Lib
e9e127397d0308d464f313391b39d2ea  10.0.18362.0/um/x86/locationapi.lib
a321828dc32f7f631e8733e75e6d6298  10.0.18362.0/um/x86/LoadPerf.Lib
aa90c35e7cd2d89a5344be5494bbf88c  10.0.18362.0/um/x86/ktmw32.lib
a757521f0f4500a08898595be297ccea  10.0.18362.0/um/x86/ksuser.lib
8274ad6deaaa6d396ce780a4fa5518c0  10.0.18362.0/um/x86/KSProxy.Lib
53e9f2c22d45b330754dd8dedf98f2a4  10.0.18362.0/um/x86/keycredmgr.lib
e44eb66efd94ef1a5ca9df43c155bdec  10.0.18362.0/um/x86/kernel32legacylib.lib
c4245ee082716859a0f3e58e7d2dbb35  10.0.18362.0/um/x86/kernel32.Lib
e761db67ec49d9d61f7826bf2803b78a  10.0.18362.0/um/x86/kerbcli.lib
149d55c68a61dc9d27f8762fbe6fe05d  10.0.18362.0/um/x86/jsrt.lib
fd00b65c990cf441b13ea4f7fe7450db  10.0.18362.0/um/x86/jetoledb.lib
ff82b8abe3bde31bed385d4b37042143  10.0.18362.0/um/x86/iscsidsc.lib
8547aa4a95c861c1007f6f6ce7812ce6  10.0.18362.0/um/x86/irprops.lib
cd74ab9e82d62eee0cd7a60aaf052146  10.0.18362.0/um/x86/Iprop.Lib
c2f8851fda45eedfbf2cd32d5acb2f6d  10.0.18362.0/um/x86/iphlpapi.lib
ade09fc6e5740e9116a9c908577344b7  10.0.18362.0/um/x86/int64.lib
4ad3e308242d9c2f1d355e72507c7a07  10.0.18362.0/um/x86/inseng.lib
2bd8f39433c54a7be0e4f0066f59722d  10.0.18362.0/um/x86/inkobjcore.lib
d66360b034534bca06fc4159472ae2fa  10.0.18362.0/um/x86/infocardapi.Lib
ff9e7cd7e330214e4f5c869cfb51b0d9  10.0.18362.0/um/x86/Imm32.Lib
da738dc85965e6a839898a13955a7d68  10.0.18362.0/um/x86/imgutil.Lib
0fec20af94a1d915648baf117cf5eedf  10.0.18362.0/um/x86/ImageHlp.Lib
4b58da624b262207e9b8429c9582f249  10.0.18362.0/um/x86/IEPMAPI.Lib
7d34d62e08b8c7deccd87513f0e29e3a  10.0.18362.0/um/x86/iesetup.lib
51f0b50f93cd3eb345ec19e21a1856fb  10.0.18362.0/um/x86/icuuc.lib
9b8b5e13fb5e9003ce783d2e85d6bc35  10.0.18362.0/um/x86/icuin.Lib
13165b6b1fb4dfc153b478007ae7b89e  10.0.18362.0/um/x86/icu.lib
b438afc868e3b64441571d680ffcd4f4  10.0.18362.0/um/x86/Icmui.Lib
949f52a8930ad883a1e55e3d96bb14ef  10.0.18362.0/um/x86/Icm32.Lib
82ff1fd7924fe14f5605ec6c26d54f8e  10.0.18362.0/um/x86/iashlpr.lib
4edd26a9d0d161d87fb51c35651cf7ac  10.0.18362.0/um/x86/httpapi.lib
d7f0444fb652b76d479b936321059ae1  10.0.18362.0/um/x86/Htmlhelp.Lib
1d4a0f2d2a4d8863cd5e16313c625b25  10.0.18362.0/um/x86/hrtfapo.lib
c01f6bcaafbb195edfb55ff1d7bcc410  10.0.18362.0/um/x86/HLink.Lib
c53868f7b8ccb927aef692cbf3fc2ba0  10.0.18362.0/um/x86/hid.lib
b10c01fdcb65bf3a980af06e631729f0  10.0.18362.0/um/x86/hhsetup.lib
1709e8b14a8aeeff18e68c14d838eabc  10.0.18362.0/um/x86/hbaapi.lib
6ea3a688a998ef36bb840a9a73a141f1  10.0.18362.0/um/x86/gpmuuid.lib
8795ba0a4b1f8aafc98f01d4bd7a4830  10.0.18362.0/um/x86/GPEdit.lib
fce1913982e53f7681e9e1f422bef260  10.0.18362.0/um/x86/GlU32.Lib
b9f23cfb8578d394a9d6181d60c70fca  10.0.18362.0/um/x86/glmf32.lib
3b55aa378f18cbe5345ac1c621d13c6f  10.0.18362.0/um/x86/gdiplus.lib
ed7387b7c53f0b26da073c0e90dbd032  10.0.18362.0/um/x86/Gdi32.Lib
48c3b7c36df001348160fbe489d80141  10.0.18362.0/um/x86/fxsutility.lib
56eab873ddbd735dadc8693837ff83e6  10.0.18362.0/um/x86/fwpuclnt.lib
cf4b485e4e63901494cf2c4af1577c7b  10.0.18362.0/um/x86/FrameDyn.Lib
075178a446eb9c660b1645292c2d763b  10.0.18362.0/um/x86/FrameDyd.Lib
4651bccd0e9e5274849410fd4e0debe6  10.0.18362.0/um/x86/fontsub.lib
28f965c0daa023dc372819c0da992449  10.0.18362.0/um/x86/fltLib.lib
4e0e80caab7d3a509794b318a8e06406  10.0.18362.0/um/x86/fileextd.lib
30942e6981c7f7cdf84a66af55dde707  10.0.18362.0/um/x86/FhSvcCtl.lib
55aa6efc52cd9f64b2cb1c61a9e9d21d  10.0.18362.0/um/x86/feclient.lib
f7067231916bcdcf9ef1275fc59bf902  10.0.18362.0/um/x86/FaultRep.Lib
f25c0a28c5a935fcc89320d5d0b0e0ac  10.0.18362.0/um/x86/evr.lib
094e9e7ef01ed93a76fd18d2d8b76e4d  10.0.18362.0/um/x86/esent.lib
ce0682135daed652352e7b1ee0095752  10.0.18362.0/um/x86/ElsCore.lib
630ec2e6599a2ccc95e699a8defbf5d0  10.0.18362.0/um/x86/els.lib
b665ceef8995cfce98256a3cefdbcb16  10.0.18362.0/um/x86/elfapi.lib
d835dde7367fc892cc36dd7f987f5ccc  10.0.18362.0/um/x86/ehstorguids.lib
5b203ac0f2c47af88e93c1b4c72d5f11  10.0.18362.0/um/x86/efswrt.lib
2cb892646fa3ef0897266bdfa173743b  10.0.18362.0/um/x86/easregprov.lib
111e504d89d26163d126aca718c59cce  10.0.18362.0/um/x86/eappprxy.lib
ddebec809dcbbbe0a4e4115c79e30e73  10.0.18362.0/um/x86/eappcfg.lib
33aa21e2d9276516ee600d28b44234c9  10.0.18362.0/um/x86/dxva2.lib
a6ebfb0bfc9b14e29190961f2bbfa06e  10.0.18362.0/um/x86/dxtrans.lib
7faeff5488542fc0a76b581829880e42  10.0.18362.0/um/x86/dxtmsft.lib
eb58862228d7f93c85f0140d8776d300  10.0.18362.0/um/x86/dxguid.lib
64f4ed051f6b9c0b8ef6cdef85c5f408  10.0.18362.0/um/x86/dxgi.lib
c25cbdb90c53c869055d517400f0458a  10.0.18362.0/um/x86/dxcompiler.lib
4f319244ad6b157d23de1f65b402b66c  10.0.18362.0/um/x86/dwrite.lib
cb77bb2b2ec9194729e0012b6aeda69f  10.0.18362.0/um/x86/dwmapi.lib
91b6cf1bcf5a72e96a1dff86f41641eb  10.0.18362.0/um/x86/DtcHelp.Lib
8ee84b28e138d06883c17042f0a945e8  10.0.18362.0/um/x86/DSUIExt.Lib
baede12c880853ef446b9fdc449cf169  10.0.18362.0/um/x86/dststlog.lib
1549b010af0b966e076a3dfd70cce243  10.0.18362.0/um/x86/dssec.lib
5c7278dac546e54775591905788cfbd9  10.0.18362.0/um/x86/DSProp.Lib
12fd67866e31eea2e0e2f204ce95e81f  10.0.18362.0/um/x86/dsound.lib
e5888aa33e9bcd0a0020838171eb484c  10.0.18362.0/um/x86/drttransport.lib
17392fc46d940ade7675e96da4e2a507  10.0.18362.0/um/x86/drtprov.lib
20c204f644b951f2b58d20eacf6ad7bc  10.0.18362.0/um/x86/drt.lib
ecb1d35f610705d1e25d8f9a5224dcd2  10.0.18362.0/um/x86/dpx.lib
9a792707a9fe3db002cc4ff718cf2c9e  10.0.18362.0/um/x86/dnsrslvr.lib
71d7389d82d34c4a8932d8d17b11fe0e  10.0.18362.0/um/x86/dnsrpc.lib
23a9d8bc18bf2eb5b33cfcf0cecee4d8  10.0.18362.0/um/x86/dnsperf.lib
f7aeac45916ef239aa69f94c7d6f1e30  10.0.18362.0/um/x86/dnslib.lib
da40637939cdca0108410210937e76b1  10.0.18362.0/um/x86/dnscrcli.lib
684bc3ca5bfcffd16ffbd7e74a3e014b  10.0.18362.0/um/x86/DnsAPI.Lib
4f7d7a2094f14d3dd8095226f866d99d  10.0.18362.0/um/x86/dmprocessxmlfiltered.lib
4622b5ecfe9d7531c81e0d5ab30c943e  10.0.18362.0/um/x86/dmoguids.lib
b8a3f8dc0a5561a6386ac638b5804aa4  10.0.18362.0/um/x86/dloadhelper.lib
ade9fbe2e3c1c229f002d9e039026624  10.0.18362.0/um/x86/directml.lib
c55901a131d1ab8e5241d66011fd5bda  10.0.18362.0/um/x86/dinput8.lib
59b3b82c9bda560ec48594cdc7e3a2ff  10.0.18362.0/um/x86/dhcpsapi.lib
6f96cd506da46c8d36299769a0cc32b7  10.0.18362.0/um/x86/DhcpCSvc6.Lib
58c4461b4dded088aedc716135acbc6f  10.0.18362.0/um/x86/DhcpCSvc.Lib
7de17c0f475da9f2b38c90d87c651c57  10.0.18362.0/um/x86/dflayout.lib
80dd2a06621f1649e49027d5844327bd  10.0.18362.0/um/x86/devmgr.lib
717e69bc5d85cddf092e8097ade25ce3  10.0.18362.0/um/x86/deviceaccess.lib
8bcfb39e2a0287cabc019cf24a769425  10.0.18362.0/um/x86/devenum.lib
709e5ab58141158072a9078072b4f7d0  10.0.18362.0/um/x86/ddraw.lib
fbb60010c8fba8b060b0e8942893b485  10.0.18362.0/um/x86/dcomp.lib
24a7abcbe228bbdd9db4bf9385ed0173  10.0.18362.0/um/x86/dciman32.lib
d257b0cc953dabc219d9a5256ec618d1  10.0.18362.0/um/x86/DbgModel.Lib
bea5509215bc3d766774ace65240b66f  10.0.18362.0/um/x86/DbgHelp.Lib
4ac0348d8443d2b134d1b28b3de938be  10.0.18362.0/um/x86/DbgEng.Lib
d878b703bed6576d0805edaf20eb5c67  10.0.18362.0/um/x86/davclnt.lib
37574d0b3f9385da6d0d5f9f306034bb  10.0.18362.0/um/x86/d3dcsxd.lib
7abb7eab4903e314c06f073ae48ad820  10.0.18362.0/um/x86/d3dcsx.lib
f8ab80f0dd714aa67432714187e5b18a  10.0.18362.0/um/x86/d3dcompiler.lib
5f422bd62878c1924031ae23cadfdc1a  10.0.18362.0/um/x86/d3d9.lib
42392e280883521e3ab067db8eeb3deb  10.0.18362.0/um/x86/d3d12.lib
f0b236081b561ace6b557b657ea10d1a  10.0.18362.0/um/x86/d3d11.lib
521f2e0f4bdc0f2bb517bb6306a454ce  10.0.18362.0/um/x86/d3d10_1.lib
512319a872402a92f523ad34acd2d111  10.0.18362.0/um/x86/d3d10.lib
76a5862a3ac9e29db4648cdf3adcd1b2  10.0.18362.0/um/x86/d2d1.lib
bd48ec728944812ae4b408ad4f32e6b3  10.0.18362.0/um/x86/cscdll.lib
fbafdd582b68e1fcfd30d08b11264d09  10.0.18362.0/um/x86/cscapi.lib
640b7a20da112ffd8757dc6e104dcdbb  10.0.18362.0/um/x86/cryptxml.lib
ac0030294cea5c5807c5a2a7128bcdba  10.0.18362.0/um/x86/cryptui.lib
d7228796fbc1138f25fdce999d76a1a3  10.0.18362.0/um/x86/CryptNet.Lib
a10215146a423c1841fc532b1ee31df2  10.0.18362.0/um/x86/cryptdll.lib
19915f53e3f6b8f7efb3e8e3e8d8cfff  10.0.18362.0/um/x86/Crypt32.Lib
ce812acc2b4b2ce02226cee89f638309  10.0.18362.0/um/x86/Credui.lib
f7d1cbd2b5def951d8256d3c65d4e367  10.0.18362.0/um/x86/corrEngine.lib
d0deb5adfb33a421ebdd8e3d2ec15f61  10.0.18362.0/um/x86/CoreMessaging.lib
f1088413933fbbcfdeb95b42e40d1deb  10.0.18362.0/um/x86/ComSvcs.Lib
56d4e4992b9a65bed6c2fe0cccff7bce  10.0.18362.0/um/x86/compstui.lib
e2ce752eb2da47d56a438d92e4044556  10.0.18362.0/um/x86/CompPkgSup.lib
cd773e2a6e4bcd70a25c18f6703191c2  10.0.18362.0/um/x86/ComDlg32.Lib
e87b1e0a9bfcb317772967e235729a5a  10.0.18362.0/um/x86/ComCtl32.Lib
f70b55d2d5f7b2cd78cbafdbf38b142c  10.0.18362.0/um/x86/ClusApi.Lib
57e5462b55b21cf145bd3c6d49d26b1f  10.0.18362.0/um/x86/clfsw32.lib
6eea8d5056c3efa8cadeafeaa5243a29  10.0.18362.0/um/x86/clfsmgmt.lib
4553448bfbaa781397b1eadfc4a1c242  10.0.18362.0/um/x86/cldapi.lib
99813699589a4b3f2807df4a2da1f7e8  10.0.18362.0/um/x86/Chakrart.lib
2caf58e9782df8ba68b1d27159c0e0f9  10.0.18362.0/um/x86/cfgmgr32.lib
6709429853f0e507af3f2203f11bed44  10.0.18362.0/um/x86/CertPolEng.Lib
17db0bf395a09613fa1aef2656e261c1  10.0.18362.0/um/x86/CertIdl.Lib
248a8d19dcfa88eff2c81f553a391600  10.0.18362.0/um/x86/certcli.lib
a81a68057b2acbb7d752a28062988575  10.0.18362.0/um/x86/certca.lib
78a7cbedd0cb5aea431b0e4529e711f6  10.0.18362.0/um/x86/certadm.lib
54d806232897f58fc9eee9a46a0cffd7  10.0.18362.0/um/x86/Cabinet.Lib
2d68effc0882f27d594dd5234af09dc6  10.0.18362.0/um/x86/BufferOverflowU.lib
093d5b41af2d3382272c6e0f89a06629  10.0.18362.0/um/x86/BufferOverflow.lib
b29fdd7260da6373bb74b0e48fb0d26d  10.0.18362.0/um/x86/bthprops.lib
1b088dfb211287c7792d6db53bedbb50  10.0.18362.0/um/x86/BluetoothApis.lib
0173bb65a276186b901baed5e74859ad  10.0.18362.0/um/x86/Bits.Lib
be22f17f491d7c769e5ef4da977f9afa  10.0.18362.0/um/x86/bcrypt.lib
41cb1d0448d0c3228584c37b2d49dd30  10.0.18362.0/um/x86/basesrv.lib
47388016bf991129ebafbbc729277001  10.0.18362.0/um/x86/avrt.lib
88c12bd2aebe67f3603a5ab0f3b4c051  10.0.18362.0/um/x86/avifil32.Lib
78d946db3f23287193461b4e230f8ac8  10.0.18362.0/um/x86/aux_ulib.lib
89d6d8d32e0ee369c28ff344ce3b3be3  10.0.18362.0/um/x86/AuthZ.Lib
e2134b724ebb3eb2a643457058c63e8f  10.0.18362.0/um/x86/audiomediatypecrt.lib
0e89546ee4cb2664f81e7e51844a2a4c  10.0.18362.0/um/x86/audioeng.lib
84cc2ee70e967feb85bcc730633e3887  10.0.18362.0/um/x86/AudioBaseProcessingObjectV140.lib
f9d49e27d0e22bd4f653a48954df9d9c  10.0.18362.0/um/x86/audiobaseprocessingobject.lib
519689f981923f577b1eb06dec6fa47c  10.0.18362.0/um/x86/appnotify.lib
d8034e16acba6e26dc1611841e35e73a  10.0.18362.0/um/x86/ASycFilt.Lib
0fdc3004e92eb501548f1ac480326743  10.0.18362.0/um/x86/appmgr.lib
f967f6042da85c2d461dec420fa66ae0  10.0.18362.0/um/x86/appmgmts.lib
ea15fe58828dc4d4fbbe013f6c2fc858  10.0.18362.0/um/x86/apidll.lib
5e5fb9ef93f4483f88eb37f75d31b828  10.0.18362.0/um/x86/api-ms-win-net-isolation-l1-1-0.lib
eb53f52b147bfd22af8ea22492b2dcef  10.0.18362.0/um/x86/amstrmid.lib
249c784ede443dc604b58902c8e87cf8  10.0.18362.0/um/x86/amsi.lib
a323fc0a46a25ccb5c056f12d020ccdf  10.0.18362.0/um/x86/ahadmin.lib
5f824ba84e5282780d39893e089701c0  10.0.18362.0/um/x86/advpack.Lib
791da286e830f4830aca089f77fd0411  10.0.18362.0/um/x86/AdvAPI32.Lib
b576618a721a1f5d8da22302e0ebbcb8  10.0.18362.0/um/x86/ADSIid.Lib
d86017def73f2368506851f04a8f7a1a  10.0.18362.0/um/x86/ActiveDS.Lib
6b2d107f753bd969904bf9d01f0bf333  10.0.18362.0/um/x86/AclUI.Lib
3ab058debbe9c41be928dd8b1f843801  10.0.18362.0/um/x64/ActiveDS.Lib
87bd0291b3a4bf9ebb56d4384f524d6d  10.0.18362.0/um/x64/ADSIid.Lib
9d2d6de06d07a6d39e87c1c9e4ca972a  10.0.18362.0/um/x64/AdvAPI32.Lib
d772d9fb4512a8b7a56b301f79f9987d  10.0.18362.0/um/x64/advpack.Lib
90ea180f529b4c488aa5b394f3c6e3d7  10.0.18362.0/um/x64/ahadmin.lib
5a5e4602a962094dbdb2925b3017074c  10.0.18362.0/um/x64/amstrmid.lib
8b965471712e804a80ad6861c4a72b87  10.0.18362.0/um/x64/amsi.lib
2470f83d4a6f3b8b06cbbbad3799141e  10.0.18362.0/um/x64/AclUI.Lib
2eae76af1d12b6a7c8d475f589dddb38  10.0.18362.0/um/x64/api-ms-win-net-isolation-l1-1-0.lib
14514389bad0799b30a8ea2876b23da3  10.0.18362.0/um/x64/audioeng.lib
c0fe91a1e851535a848216e74c91cf53  10.0.18362.0/um/x64/audiomediatypecrt.lib
845c908ae79af77ed7239156be722304  10.0.18362.0/um/x64/aux_ulib.lib
020e78bbea4e7499b2d601c476ec41b5  10.0.18362.0/um/x64/avrt.lib
3af1e8bf15bef5f2c301920fe65bc70d  10.0.18362.0/um/x64/basesrv.lib
a91b1feb361d5829f8cca19719ea296e  10.0.18362.0/um/x64/bcrypt.lib
c306075515813661fa7626eea3d1b02a  10.0.18362.0/um/x64/BluetoothApis.lib
9af15cb027bfdd5fa824b10598219fba  10.0.18362.0/um/x64/bthprops.lib
57eec9b84ec5a8cdf61a2ff2e3db0516  10.0.18362.0/um/x64/BufferOverflow.lib
26ad940772fe65196869b4ba30396716  10.0.18362.0/um/x64/BufferOverflowU.lib
5a758d038306b8fb0a34274856702a5f  10.0.18362.0/um/x64/Cabinet.Lib
516c5e56da29c3f6cacea41cc990716e  10.0.18362.0/um/x64/certadm.lib
8215adb2f87f81a0a1a83d4c03676b24  10.0.18362.0/um/x64/certca.lib
487bfa838b77c6121a9d27fa202eb3a5  10.0.18362.0/um/x64/CertPolEng.Lib
47a89dd275a04e17a2c9c902153b67f8  10.0.18362.0/um/x64/cfgmgr32.lib
e98369d321fe437f18bf25ed99571f75  10.0.18362.0/um/x64/Chakrart.lib
ef1282bab49e0bc1c9c937806d0a28ae  10.0.18362.0/um/x64/ComDlg32.Lib
c81b7c8731fbf11f1660f1b762297ad7  10.0.18362.0/um/x64/compstui.lib
cd212386765442b9ec61ad07371e1c75  10.0.18362.0/um/x64/CoreMessaging.lib
0155e84b49c8617b270500ce7cdc594b  10.0.18362.0/um/x64/corrEngine.lib
5150176e6e9c0ed98a8f14fadeee4ff6  10.0.18362.0/um/x64/CryptNet.Lib
79816d1dd4ea48311f7d10386955da1e  10.0.18362.0/um/x64/cryptxml.lib
8a035b4f0e92c5070e6b9d9a5242c0d8  10.0.18362.0/um/x64/cryptui.lib
75a411d743725c91eebec26870f519de  10.0.18362.0/um/x64/cryptdll.lib
7639f12d64d75f709645eb44c2c3b2a8  10.0.18362.0/um/x64/Crypt32.Lib
f32ef19543ad419fb511ad8f7d2d23c3  10.0.18362.0/um/x64/Credui.lib
80f4e511c4e7c6bdf05b5e74428d690e  10.0.18362.0/um/x64/cscapi.lib
80e961fb89c6598346d973e2bfac3652  10.0.18362.0/um/x64/d3d10.lib
902f2309fbf4cd5a6f1ff0f0a9886244  10.0.18362.0/um/x64/d3d9.lib
d01c4c0cb735b44844ffeb4bae19a407  10.0.18362.0/um/x64/d3dcsx.lib
79ee8de1967cc36968fe773335a4a2a2  10.0.18362.0/um/x64/d3dcsxd.lib
3b1a3cfd179510bdc9ad981a766448e9  10.0.18362.0/um/x64/d3dcompiler.lib
251cff091160cb4e065ccdc0379818d1  10.0.18362.0/um/x64/davclnt.lib
bbcac1eeb86932dbc88a3388b6b210a0  10.0.18362.0/um/x64/DbgHelp.Lib
a2339ff9bc7d76bb294918b92f1c032f  10.0.18362.0/um/x64/DbgModel.Lib
166b7fe90897029f78cc4a7325dee581  10.0.18362.0/um/x64/dcomp.lib
7513f4b121834ed072bfc1b668c5e19d  10.0.18362.0/um/x64/ddraw.lib
92e06c63fdba3a26d4fec840a323420b  10.0.18362.0/um/x64/devenum.lib
52c476180f08de136e21c9174ff67e08  10.0.18362.0/um/x64/deviceaccess.lib
ce508be9fd8188882078d89ef77c1a52  10.0.18362.0/um/x64/devmgr.lib
86a401b57575adc2361ffbcd80790213  10.0.18362.0/um/x64/dflayout.lib
ce49d6a28c2903e6044182341b5deaf6  10.0.18362.0/um/x64/DhcpCSvc6.Lib
59bd2a7cc19083fa5daca80a58cadead  10.0.18362.0/um/x64/dhcpsapi.lib
46607f8c4943e730d08407133da48b07  10.0.18362.0/um/x64/dinput8.lib
3e114b175b67159b61bdbe45338c70ae  10.0.18362.0/um/x64/directml.lib
88ae52ce58bff7d1b5d1578a37d5e251  10.0.18362.0/um/x64/dloadhelper.lib
fa1c7b9222ec8eb6dc572932e42697d5  10.0.18362.0/um/x64/dmoguids.lib
2d8d38fba1edf9808d1518c48910dac3  10.0.18362.0/um/x64/dmprocessxmlfiltered.lib
4f3a8024feb86b397cc3c21786c71a3e  10.0.18362.0/um/x64/DnsAPI.Lib
1aad49d655c731e22136043c510a9787  10.0.18362.0/um/x64/dnscrcli.lib
bbc36a59743a260c8fac1d76fc34a4a2  10.0.18362.0/um/x64/dnslib.lib
45f7a35ca00131e3ac4f9c854c82e857  10.0.18362.0/um/x64/dnsperf.lib
c5f66702811b92fdb5ab5d0affc2b8a6  10.0.18362.0/um/x64/dnsrpc.lib
3260bd8c958bed1e2fdd7372f8495ce6  10.0.18362.0/um/x64/drt.lib
a9c53ad7f4174b71e46508a29de573db  10.0.18362.0/um/x64/dsound.lib
79f04326440d4fa101ca05bf380c81ce  10.0.18362.0/um/x64/DSProp.Lib
3dff2dbf45e7dd2dd5dcbd9b475cd1ca  10.0.18362.0/um/x64/drttransport.lib
cd9291fdb168098d3b953bb61cd6eb91  10.0.18362.0/um/x64/drtprov.lib
fef23253d7f8e2baa8170f7cc76c04fb  10.0.18362.0/um/x64/dssec.lib
76f1558ed1f8c0f93f493d2229a989fe  10.0.18362.0/um/x64/dststlog.lib
7ebbdbccea28dd3ecd9c1f025b3c49bf  10.0.18362.0/um/x64/DSUIExt.Lib
e816d1303a9b642bda468163fc590c96  10.0.18362.0/um/x64/dwmapi.lib
3a8479d409a6d6b2eda43e90d9c9ff67  10.0.18362.0/um/x64/dwrite.lib
6d38292816eb45ba36ebe7e10250c43b  10.0.18362.0/um/x64/dxcompiler.lib
d33e3e95060c53d41c6f892ad72323ad  10.0.18362.0/um/x64/dxgi.lib
7a3a6bd3f930d4037ca958f4434c4e83  10.0.18362.0/um/x64/dxguid.lib
5cb70e321610c33138248d8825bad00b  10.0.18362.0/um/x64/dxtmsft.lib
8ce08ad6d9c97616f8df8f8036cd381c  10.0.18362.0/um/x64/dxtrans.lib
c846b1c224ecdcbbe23e548a8723334c  10.0.18362.0/um/x64/dxva2.lib
6032778b7f51e9d37a43675ad3986afc  10.0.18362.0/um/x64/eappprxy.lib
ab4063b871950f544384683ee170a2af  10.0.18362.0/um/x64/easregprov.lib
e7ee4182664e03274706a6fedee4f4dc  10.0.18362.0/um/x64/elfapi.lib
53cf1c6187f75c3821fd652ac12e38e0  10.0.18362.0/um/x64/ElsCore.lib
b5a9d86ec82b24b5ef3ea0adc4483186  10.0.18362.0/um/x64/esent.lib
0285e08df210040e4871abc1890ba078  10.0.18362.0/um/x64/evr.lib
20a4da627853c2dcd3362073a1a8f124  10.0.18362.0/um/x64/feclient.lib
67ef86d3c1db7134024ef0c77c0d5cf9  10.0.18362.0/um/x64/FhSvcCtl.lib
665cb47e04190fcaaf2a3ff6bde12f1c  10.0.18362.0/um/x64/fileextd.lib
70ea67a9833f0eea136885def5da9a75  10.0.18362.0/um/x64/fltLib.lib
8f7fe92c4850c2810dc86f62974f37f8  10.0.18362.0/um/x64/fontsub.lib
a37f455e95a542a9b3ed11bb6c558d80  10.0.18362.0/um/x64/fwpuclnt.lib
28bed554b25e348a6f8052051ef264b4  10.0.18362.0/um/x64/fxsutility.lib
e20efc463091c24f7b756a0168b206f0  10.0.18362.0/um/x64/Gdi32.Lib
a1f5dc7c0b0ca0bd10489c97694b8b5d  10.0.18362.0/um/x64/gdiplus.lib
7e75c82d0ea92e016e94c456b5b18daa  10.0.18362.0/um/x64/glmf32.lib
a22a456bded7b96a988ce86b7dd4bd92  10.0.18362.0/um/x64/GlU32.Lib
30877fddd04db823e8b0740bc683abda  10.0.18362.0/um/x64/hbaapi.lib
488c2db82b113f9f1712da1dc33523b3  10.0.18362.0/um/x64/hhsetup.lib
54a0494bc5025aa732c0f01431018512  10.0.18362.0/um/x64/HLink.Lib
b666a81ed2bccd3c170fe1d440964f03  10.0.18362.0/um/x64/Htmlhelp.Lib
c2c31c9ccf810703ffaa6af2a7eb2b61  10.0.18362.0/um/x64/iashlpr.lib
51e4285e1c8d2c744286d84d813452be  10.0.18362.0/um/x64/Icm32.Lib
0cc4ec1277af732cfbfffd95e7802157  10.0.18362.0/um/x64/icu.lib
543b2797aa425ce5278e44876c939587  10.0.18362.0/um/x64/icuin.Lib
6710a532e1d4c55d9c7cc2975b830e96  10.0.18362.0/um/x64/IEPMAPI.Lib
cd0f7d15319d67aaa5b571c3c88833b3  10.0.18362.0/um/x64/iesetup.lib
c5559b582228f3629dee476cd66d60df  10.0.18362.0/um/x64/ImageHlp.Lib
3703c85f97816afacecf1bd0856139a4  10.0.18362.0/um/x64/imgutil.Lib
49e97b0c3243df1279ea7f087a328961  10.0.18362.0/um/x64/Imm32.Lib
c4de4cc8a517beef960bc15461f50e39  10.0.18362.0/um/x64/infocardapi.Lib
fdaf97371b6b2fc16883ae2eb1c5e0d6  10.0.18362.0/um/x64/inkobjcore.lib
25edd92f1df0fb74d27bc5127120c41f  10.0.18362.0/um/x64/inseng.lib
5bf0d2a02b23c99a970eb4a9058a0eb4  10.0.18362.0/um/x64/iphlpapi.lib
58ded8ea2a9582793beb3b6d56c55b8b  10.0.18362.0/um/x64/iscsidsc.lib
61051319d5b2e5b6bfa0adb8190eee67  10.0.18362.0/um/x64/jsrt.lib
105c220d7ebe539d4f9248aec27668f1  10.0.18362.0/um/x64/kernel32legacylib.lib
3424774d053992aa4420bf9464b62e44  10.0.18362.0/um/x64/keycredmgr.lib
bd0866612291c5fe8c5cd2d9135a73ac  10.0.18362.0/um/x64/kernel32.Lib
da0cacbbfe868601df59b85f21c42c25  10.0.18362.0/um/x64/kerbcli.lib
621fff70839388510294a4bd889808d9  10.0.18362.0/um/x64/irprops.lib
a8e7259fccfbb158617141fba7eac29c  10.0.18362.0/um/x64/KSProxy.Lib
2cd05094de16e33d3488a28253ffba8a  10.0.18362.0/um/x64/ksuser.lib
3bd236f187d28e74c6b16f400de0463f  10.0.18362.0/um/x64/ktmw32.lib
af1a813d1ae931a70c3f3da57288d1cf  10.0.18362.0/um/x64/LoadPerf.Lib
1b0a522278b249e5a136a0c3c39708ce  10.0.18362.0/um/x64/magnification.lib
ec588d59e5b9617c9c8f1a502722fc71  10.0.18362.0/um/x64/MAPI32.Lib
372c2fd20cbc3d75ab26e43f856bae87  10.0.18362.0/um/x64/mdmlocalmanagement.lib
f202438f511061e97359bb9470534a05  10.0.18362.0/um/x64/MDMRegistration.lib
aa4fdcef66ae02beadd72e745f4cf9c1  10.0.18362.0/um/x64/Mf.lib
b636bc667acfdee6215920a15be362e0  10.0.18362.0/um/x64/Mfcore.lib
ef02f376d316af3afe6aab8889c09400  10.0.18362.0/um/x64/Mfsrcsnk.lib
7c2608ea0a26e75ebb4da7259f78f0b3  10.0.18362.0/um/x64/MgmtAPI.Lib
501c2ef631ebdc62d517788a7d38789f  10.0.18362.0/um/x64/mmdevapi.lib
a067eb321408488c779b57489f4c0b13  10.0.18362.0/um/x64/Mpr.Lib
533299dee74be4b8e81a6ff7159f4e4c  10.0.18362.0/um/x64/mprsnap.lib
23824521fc5eb2d145a2de6b9144d7e8  10.0.18362.0/um/x64/MqOA.Lib
80727e225e1dc66037080a4f47d1e53f  10.0.18362.0/um/x64/MrmSupport.lib
0cd6f2ce660666c24658aa71176925cb  10.0.18362.0/um/x64/MqRt.Lib
1ba817051887dd6aa1d64df7888983e5  10.0.18362.0/um/x64/Mscms.Lib
991f47f6e8f0abffbf935dd88a8c7f81  10.0.18362.0/um/x64/msdasc.lib
0c42022f5847eaefe89767d63f0bfdfd  10.0.18362.0/um/x64/msdmo.lib
6ca1e236cea63bd3c0eb9e004a7560e8  10.0.18362.0/um/x64/msdrm.lib
08924b07745ec11906700f462adf8a8e  10.0.18362.0/um/x64/Msi.Lib
86e1cf158067d451b561111bb6d46e84  10.0.18362.0/um/x64/MSImg32.Lib
a2607c655dd9e27973f9965a725f75b4  10.0.18362.0/um/x64/mspatcha.lib
38e93082ba039b97563728bead91c217  10.0.18362.0/um/x64/mspatchc.lib
a81396fb93dd44ffb54e08ea8a61fe18  10.0.18362.0/um/x64/mspbase.lib
1b69f6774741b62d6756f2213c4f36ae  10.0.18362.0/um/x64/msports.lib
af0a90801242e9e6cee3f57d39cf1b1f  10.0.18362.0/um/x64/MSRating.Lib
43a164ccb9dc91866b3b94bfe0d9c8a0  10.0.18362.0/um/x64/msvfw32.Lib
40dd822fe7567b456d5eb5dc4392fe4f  10.0.18362.0/um/x64/msv1_0.lib
8e487e7ad86e36875c3cd9d353f18bbd  10.0.18362.0/um/x64/MsWSock.Lib
9dcfa05213e1dcb442e7f91745b9a24c  10.0.18362.0/um/x64/MsXml2.Lib
ba7557ab4fb5c9f3ff1ada75ffc13b93  10.0.18362.0/um/x64/msxml6.lib
9a36a2229fdadb77296c0a70db5e111e  10.0.18362.0/um/x64/mtxdm.lib
5418a571d918196da82a7368482aad70  10.0.18362.0/um/x64/nanosrv.lib
798832eccab7f38078577704c79f7af5  10.0.18362.0/um/x64/ncrypt.lib
eca221266bf371d201be2a3728cfbb93  10.0.18362.0/um/x64/nddeapi.lib
9abf63df0edae4e8224575a5c25a3edc  10.0.18362.0/um/x64/ndfapi.lib
1573c0ae051a4ca010fc7c58864f6630  10.0.18362.0/um/x64/ndproxystub.lib
25726f3ac6529cdc799de91d977ab6bc  10.0.18362.0/um/x64/NetAPI32.Lib
1f26d9bc347bea8c2e62151a5b7f80fb  10.0.18362.0/um/x64/netlib.lib
efad87a08f57d7e22b88aa659219df73  10.0.18362.0/um/x64/NetSh.Lib
54415a6eda1139f2fd7d96b380db5b6b  10.0.18362.0/um/x64/newdev.lib
e303301f5fb38300c0638f1e07955020  10.0.18362.0/um/x64/ninput.lib
73cddfc6db044d8d6bf60763379e2e27  10.0.18362.0/um/x64/normaliz.lib
ad071533b24ebe9e26e45f4d8968f016  10.0.18362.0/um/x64/muiload.lib
1722df31110ba14089a0ae674338e2f4  10.0.18362.0/um/x64/Mtx.Lib
931405f4c96799d2ed2268da96cae842  10.0.18362.0/um/x64/nt.lib
c30152571879e735bff40c15d7ebeb1e  10.0.18362.0/um/x64/ntdll.lib
8689bfcf9a9be7c0ac80f63eb811c3e6  10.0.18362.0/um/x64/ntdsa.lib
cfe49b0628eb60106cb656ecb94fd37d  10.0.18362.0/um/x64/NtDsAPI.Lib
fe7ff1c9cee1692680146a92293cf417  10.0.18362.0/um/x64/ntdsatq.lib
2520ea92a4c8f6c0f5fa0811ed54e7aa  10.0.18362.0/um/x64/ntdsetup.lib
0e787ddb54614314742136302be03b1c  10.0.18362.0/um/x64/ntfrsapi.lib
839dffaab695b379c7f6ccd8dd65d417  10.0.18362.0/um/x64/ntmarta.lib
7cc0ae72c442828de68306c30ea0234e  10.0.18362.0/um/x64/NtQuery.Lib
8b8b8b5fe9d08d46d927c0ff6a6cd883  10.0.18362.0/um/x64/ntstc_libcmt.lib
bafe43b8aab309a58d2c545ebd65cea3  10.0.18362.0/um/x64/ntlanman.lib
b7e33d7573260a8a7230e08f16c3489f  10.0.18362.0/um/x64/ntstc_msvcrt.lib
992c41ad1257fcfc4bd3530aa51fc189  10.0.18362.0/um/x64/objsel.lib
a6692d079f8abb5590d84e55741c9956  10.0.18362.0/um/x64/odbc32.lib
faea8320f69e49a8811e2f5f393e4ac2  10.0.18362.0/um/x64/odbcbcp.lib
17852aae0e31403076f6ae62fa1ba332  10.0.18362.0/um/x64/OemLicense.lib
cdb55077ea2b7aca400dc4dd2852bab4  10.0.18362.0/um/x64/OleAcc.Lib
03e27fa14e29a5c4c9258713518640ee  10.0.18362.0/um/x64/olecli32.lib
4d85c4cd1901285f6ed2967f6ce17543  10.0.18362.0/um/x64/oledb.lib
48061fbe2319c2083a803a0ee1f8f44f  10.0.18362.0/um/x64/OleDlg.Lib
e974acc4d7bf6647ff228700ca7724fc  10.0.18362.0/um/x64/olesvr32.lib
d3ea0b3f740ab42e8ab6a68f53b73055  10.0.18362.0/um/x64/OneCoreUAP.Lib
2b58eb2e1f8436bfb2934414abcc7e40  10.0.18362.0/um/x64/OneCoreUAP_apiset.Lib
89cc03985b5e92c38d3edc6f9203b368  10.0.18362.0/um/x64/OneCoreUAP_downlevel.Lib
7aca00a80d3d6db172a3b61e3594522a  10.0.18362.0/um/x64/OneCore_apiset.Lib
c7a1f25566e295aec1ac2351fc1e6e2f  10.0.18362.0/um/x64/OneCore_downlevel.Lib
b97683f76cc629f1c95f876288ba6300  10.0.18362.0/um/x64/OpenGL32.Lib
8821948155fa6368cfc24302c20cd080  10.0.18362.0/um/x64/opmxbox.Lib
4b8f6fa5cab9faf9f6c064ed3b3c1bfe  10.0.18362.0/um/x64/osptk.lib
7ae458cc2b9c4ddf3c4c8397854542cf  10.0.18362.0/um/x64/p2p.lib
d0cf337226d6b7f23939a1ebf34d5fee  10.0.18362.0/um/x64/p2pgraph.lib
774f231327a1f08b993beb4831158f7d  10.0.18362.0/um/x64/pathcch.lib
1497a278795d7eb56603d386d673d399  10.0.18362.0/um/x64/Pdh.Lib
4e6a90805349e3b7f403c54d6a0fd5a7  10.0.18362.0/um/x64/PeerDist.lib
3f17aaa5f45362e84b121adaa49d5751  10.0.18362.0/um/x64/PhotoAcquireUID.lib
dd7d441b710a1b451aecc14e7c77dd26  10.0.18362.0/um/x64/PortableDeviceGuids.lib
f09aa46d512f4ad7990f5510d1a62865  10.0.18362.0/um/x64/powrprof.lib
c4723c92275e70ccf41cab2f697e45e5  10.0.18362.0/um/x64/prntvpt.lib
80ec704ddccb5d23498b7bfe61107224  10.0.18362.0/um/x64/ProjectedFSLib.lib
c6626c9bcc61efeaab4bf824212cbe9f  10.0.18362.0/um/x64/propsys.lib
b9534dd1c13e65f0f32075ac6f8122b9  10.0.18362.0/um/x64/Psapi.Lib
2216c36dbdbe016ac8bd4550628d9805  10.0.18362.0/um/x64/quartz.lib
7cc0ae72c442828de68306c30ea0234e  10.0.18362.0/um/x64/query.lib
d1d5822a68c70a42b686491c49bd9a50  10.0.18362.0/um/x64/RASDlg.Lib
46cc8723205b800330d6b5a20b0743ed  10.0.18362.0/um/x64/rasuser.lib
dd1e10005ea5d08a9e6411f3c93c5bc3  10.0.18362.0/um/x64/RASAPI32.Lib
82e419b232a28ab029e0dc04fe46cf7b  10.0.18362.0/um/x64/rometadata.lib
ebfdeba6023e4c500e59b8ae454f1cf3  10.0.18362.0/um/x64/rpcexts.lib
5498cb00abd50126d63d90db2e8bec72  10.0.18362.0/um/x64/Rpcns4.Lib
79a67775ceacb6619207a06373108998  10.0.18362.0/um/x64/rpcproxy.lib
6443412bbdb31c255a810350770f8455  10.0.18362.0/um/x64/RpcRT4.Lib
26be84e1fdcd81126a51c333e23580bc  10.0.18362.0/um/x64/rpcutil.lib
0bb90106271ed82cc992029e0fd46bf3  10.0.18362.0/um/x64/rstrtmgr.lib
746244cb3b7e073cef0c6eaca41ea6b1  10.0.18362.0/um/x64/Rtm.Lib
cb0f0ae8b2214cc42558b473a067dc2e  10.0.18362.0/um/x64/rtutils.lib
87552234d211cb2a4e492a6c63458bb7  10.0.18362.0/um/x64/RTWorkQ.lib
a78836b05fd2c119b9525339bf4e465e  10.0.18362.0/um/x64/runtimeobject.lib
bf9b1d2bdc5668304b32b5293a0429d9  10.0.18362.0/um/x64/samlib.lib
1ec67630d7aa0222df79d104a5dadf23  10.0.18362.0/um/x64/samsrv.lib
61a3c103b27c935c1d04a395fb27f819  10.0.18362.0/um/x64/SAPI.Lib
fad2352f958791d10219e5a1eb604200  10.0.18362.0/um/x64/sas.lib
d120dba0b8b6e53bfd0e7bbcb51bb128  10.0.18362.0/um/x64/sbtsv.lib
84211bc3fe99047408ec34e9d1efb4a0  10.0.18362.0/um/x64/scecli.lib
244671c1648cc2c0d8dfceeb416ba879  10.0.18362.0/um/x64/scesrv.lib
dc43fa89391b3f5b2a42e3d2e337732f  10.0.18362.0/um/x64/schannel.lib
f1ef0ba95979c3fd36163be8ff191e85  10.0.18362.0/um/x64/ScrnSave.Lib
c18700c2291e8c5284b8b4a023e75434  10.0.18362.0/um/x64/ScrnSavW.Lib
6f9e1167fbc0e2ed8d4b4ea69ed77bee  10.0.18362.0/um/x64/SearchSDK.lib
478281e456076f1e63d22ae600cf2125  10.0.18362.0/um/x64/sens.lib
9169a0c93ae88c158ab0cc2e7209fd01  10.0.18362.0/um/x64/sensorsapi.lib
d85fd218676a7ad30febecfa7e100f6d  10.0.18362.0/um/x64/SensorsUtils.lib
6abfebe60fee03fa8dcb6442260eb0f1  10.0.18362.0/um/x64/Sfc.Lib
92c283869042af0d8bf1127f92bed572  10.0.18362.0/um/x64/shdocvw.lib
ce31c6b277c2533317d04cf67810ed99  10.0.18362.0/um/x64/ShFolder.Lib
68e92fd5248893bfba81e7988db54267  10.0.18362.0/um/x64/ShLwApi.Lib
78f95232e6045670a6e28209ba81929b  10.0.18362.0/um/x64/slc.lib
966ad84c514682ee93c2cd43248774cb  10.0.18362.0/um/x64/slcext.lib
f225307857733cc03a036cf0dd58b076  10.0.18362.0/um/x64/slwga.lib
ce8db1642c93a0f1bd0e273761b6e91b  10.0.18362.0/um/x64/SnmpAPI.Lib
21c8af0c46ebf77d4d841c73fbd9a755  10.0.18362.0/um/x64/spoolss.lib
a70558d1b2260a33e766e6e3b05e9360  10.0.18362.0/um/x64/SpOrder.Lib
5617ec2b961337ec8eaa8e98cd62882f  10.0.18362.0/um/x64/Sti.Lib
cfec0806d847784afe5c61ca9ebd0101  10.0.18362.0/um/x64/strmbase.lib
5a5e4602a962094dbdb2925b3017074c  10.0.18362.0/um/x64/strmiids.lib
d23583939a083fd3a2ec11bf95e63ed8  10.0.18362.0/um/x64/strsafe.lib
968ecc4fa44f733aa58ec6bdf11bc612  10.0.18362.0/um/x64/swdevice.lib
eb20d70ef5f4cde42bdda9d9d19646ce  10.0.18362.0/um/x64/synchronization.lib
0fe24760043003ca61a825c30aeacd17  10.0.18362.0/um/x64/t2embed.lib
1fc554a9ca89ea4fc2273390a2ba7aa6  10.0.18362.0/um/x64/tapi32l.lib
22eb57c05c14161da4e5ade4837f8e85  10.0.18362.0/um/x64/taskschd.lib
8de35eb3afd7dac3dbee6ce15ebb5b15  10.0.18362.0/um/x64/tbs.lib
28c40b2f0f79374a8e7ac275bfa93be5  10.0.18362.0/um/x64/tdh.lib
96ce7ebf7211c130bc3ec637b84987a9  10.0.18362.0/um/x64/Traffic.Lib
dc7731811e418a7fb7189caf7361bf79  10.0.18362.0/um/x64/TranscodeImageUID.lib
b8b26e43385fb683750730172ee7fcd8  10.0.18362.0/um/x64/tsec.lib
86f2289a08ecd7f889aac5a5203e4800  10.0.18362.0/um/x64/wcmguid.lib
700acee5810a7da1ac2bbcbe72f6468a  10.0.18362.0/um/x64/wdsmc.lib
100951cf486ed99f606bb655fd9030a3  10.0.18362.0/um/x64/wdspxe.lib
9f6495dfff4ea6e7e1fff6b2ef4bab72  10.0.18362.0/um/x64/wdstptc.lib
f6806b472c5c276edb050d23eebc6981  10.0.18362.0/um/x64/webauthn.lib
e92d289e1c42e35783c177fdb8b838e2  10.0.18362.0/um/x64/WebServices.lib
2523a4d9d77bf2c44bd6c840fcf53dc9  10.0.18362.0/um/x64/websocket.lib
05d8be562e0ec19431dda0569405ee1d  10.0.18362.0/um/x64/wecapi.lib
976fba098af02a86068a37713f989a2e  10.0.18362.0/um/x64/Wer.lib
bfc50aed95119e2b6fed7b6315f064a1  10.0.18362.0/um/x64/wevtapi.lib
0f2e144c9616f8d8120a4bbbd89278e0  10.0.18362.0/um/x64/WiaGuid.Lib
32d898cc8db7ee4e65c50d959e37357a  10.0.18362.0/um/x64/wiaservc.lib
3f92ecb395243b560d18760dcc3ccfab  10.0.18362.0/um/x64/wiautil.lib
2d762078689ce579a3a27d96fc4cc449  10.0.18362.0/um/x64/WinBio.lib
ef87770f5766c01af6b3ae8ef464a237  10.0.18362.0/um/x64/windows.ai.machinelearning.lib
acf4f3250377b5fc99ec5fa80beef411  10.0.18362.0/um/x64/windows.ui.lib
7c03a080cc721295aaf082e6e16ef5f5  10.0.18362.0/um/x64/windowscodecs.lib
88dfcd4b37312450ad521ce97c071a83  10.0.18362.0/um/x64/windowssideshowguids.lib
3a3081e898b6338a4f43447cf957bc18  10.0.18362.0/um/x64/WinHvEmulation.lib
44ccb511487127e8709e9fa9b83d752b  10.0.18362.0/um/x64/WinHvPlatform.lib
803c9277e74d16ac991e32a292208437  10.0.18362.0/um/x64/WinInet.Lib
f09e4c172e64630291e13eaa66db06cd  10.0.18362.0/um/x64/WinMM.Lib
ebbb7797ac7b6b298d06967846b10dba  10.0.18362.0/um/x64/winscard.lib
c9ec29f664d63f991ef6e61037660283  10.0.18362.0/um/x64/WinSpool.Lib
b9dec96d67be25c3ab4bc0581663ccc2  10.0.18362.0/um/x64/winsqlite3.lib
937b995d5a3412c57fde840269922128  10.0.18362.0/um/x64/winsta.lib
4388477a74605bb603e87ab99b3a2687  10.0.18362.0/um/x64/wsbonline.lib
3b4db3cfba34790976817ec2876f66a6  10.0.18362.0/um/x64/wsbapp_uuid.Lib
f71b10171a71c59bd80539095ca6ab51  10.0.18362.0/um/x64/WS2_32.Lib
4d9ed6e0ae6eee06c424c0265c507520  10.0.18362.0/um/x64/workspaceax.lib
d638e87ea6fad9e959dd0da87e7d5a9e  10.0.18362.0/um/x64/wofutil.lib
29cf18121bfba5ed6cb0aaa3953ab552  10.0.18362.0/um/x64/wnvapi.lib
44506a71d5e96575938a81173cf902cd  10.0.18362.0/um/x64/wmvcore.lib
678fae9e44b41911907f968d401b5ead  10.0.18362.0/um/x64/wmiutils.lib
b41ebdbba994e299c577a8a08582bc85  10.0.18362.0/um/x64/wmip.lib
a6c6749977909defa08c179157fef9fa  10.0.18362.0/um/x64/wmcodecdspuuid.lib
caad8326d359e86cfb4a350e28c1bb35  10.0.18362.0/um/x64/Wldp.Lib
fd168b7425a228afaa48364049bca939  10.0.18362.0/um/x64/Wldap32.Lib
7a0ecd9b1eae6c2ebd16af88b226432f  10.0.18362.0/um/x64/wlanui.lib
c9020a2221f965f510bfe81df8977d3a  10.0.18362.0/um/x64/wlanapi.lib
56b1dfe527d421656eeaa36362ad59b4  10.0.18362.0/um/x64/winusb.lib
66bb3ae4bbd20c2227fe26b150728d15  10.0.18362.0/um/x64/WinTrust.Lib
262dbbc8f4e0720085b0441c0acc9531  10.0.18362.0/um/x64/WinStrm.Lib
caaeaad50996da5f34e3a9e07e1c0b12  10.0.18362.0/um/x64/winsatapi.lib
b8f664eb01000f9f322da67846c159b7  10.0.18362.0/um/x64/winml.lib
7c41b1eb883cb8d33d3259f69d033afd  10.0.18362.0/um/x64/winhttp.lib
8bc2e8d8d6225952cd573fa33ce957e6  10.0.18362.0/um/x64/winfax.lib
f9123fe1d855603976cd1cc73b2b9af0  10.0.18362.0/um/x64/WindowsApp_downlevel.lib
c014c34c1d5cab980a80bb4c08dc0047  10.0.18362.0/um/x64/WindowsApp.lib
51e785822cdb2eb150a46e140e3685fb  10.0.18362.0/um/x64/windows.networking.lib
916a1a9d8fc82d7ef47a4d11a91b480c  10.0.18362.0/um/x64/wdsClientAPI.LIB
b9a9307777003c672974b8828da38daa  10.0.18362.0/um/x64/wdsbp.lib
4748d32403e261370ac41f7af2a29329  10.0.18362.0/um/x64/windows.data.pdf.lib
a15b9038195f338db3214242b70f39f4  10.0.18362.0/um/x64/wbemuuid.lib
f5072880e721740e04da9240be731fd2  10.0.18362.0/um/x64/vstorinterface.lib
ca4b57ea3443a9f5267a6e7e1cf9a438  10.0.18362.0/um/x64/vss_uuid.lib
fab60b439ed57777dc0d20cf0cc4c8f3  10.0.18362.0/um/x64/vssapi.lib
50793463dcc31a40072c7a49d1406547  10.0.18362.0/um/x64/vscmgr.lib
07cb220b67cbee047e37ff3162694d14  10.0.18362.0/um/x64/vmsavedstatedumpprovider.lib
2f02c2d5316824b8df02ba777d7f0e7d  10.0.18362.0/um/x64/vmdevicehost.lib
0f8cd42be0d68e031ee0aa4a19de3613  10.0.18362.0/um/x64/Virtdisk.Lib
cd78af632065452302ac84159b9ec7be  10.0.18362.0/um/x64/Vfw32.Lib
e960147778d35c9ef10a7ddfab5bdfad  10.0.18362.0/um/x64/vertdll.lib
9e41a358ba885da1f716363244011b69  10.0.18362.0/um/x64/Version.Lib
35f9ef695ea1e4aa6becae188257a5b4  10.0.18362.0/um/x64/vds_uuid.lib
7aaf2d28c5bb7123e48de258fb33d8d1  10.0.18362.0/um/x64/vccomsup.lib
eaa73aaac78a74ca2b89bc42a36a279b  10.0.18362.0/um/x64/Uxtheme.lib
2a237a27bcb961da54437163867b4b5f  10.0.18362.0/um/x64/Uuid.Lib
6d433e2c15dc8abe69e45a5641c1fba0  10.0.18362.0/um/x64/wcmapi.lib
c0be363c2303160043f951065f668c25  10.0.18362.0/um/x64/USP10.Lib
489ad1cc621d09e1125e269a933070b2  10.0.18362.0/um/x64/UserEnv.Lib
063be04b4ba101363a4ac3b48291c8dc  10.0.18362.0/um/x64/User32.Lib
50675457dbafa614b4fd5d7d359d0403  10.0.18362.0/um/x64/Urlmon.Lib
c531501d9f35dbc99200000a02657d2c  10.0.18362.0/um/x64/umpdddi.lib
7cc6d66516fecb86a48f6cf5ac8a5065  10.0.18362.0/um/x64/UIAutomationCore.lib
3762045fe635642270c3174f5e3f198b  10.0.18362.0/um/x64/ualapi.lib
75f05eb1311c6756c0a88e9e2e184cb3  10.0.18362.0/um/x64/txfw32.lib
5c16a8da01ca78e2df831fb080fb529b  10.0.18362.0/um/x64/twinapi.lib
7343f67e0523dbf81c225f459ba551f5  10.0.18362.0/um/x64/tspubplugincom.lib
d44f0dd3390dee6752ba14a3bd6c6e16  10.0.18362.0/um/x64/tokenbinding.lib
aa80a6ee4df308ccb2f2105e2cd11f19  10.0.18362.0/um/x64/Tapi32.Lib
c80669e3485909def489c9a12f9226a3  10.0.18362.0/um/x64/Svcguid.Lib
2c45d4cc5096e47ed54aabb4942a260c  10.0.18362.0/um/x64/structuredquery.lib
b61df450230043fb8291560a76f4a2ba  10.0.18362.0/um/x64/ssdpapi.lib
6bfccd41117cac21eee79ecfdcbb6df7  10.0.18362.0/um/x64/srpapi.lib
11c7c4cd4d15cc1df74c13535e09cb0d  10.0.18362.0/um/x64/SrClient.lib
395a01574168b8affe38167e0069ae33  10.0.18362.0/um/x64/shcore.lib
11fdd340ecea0e6c0a73357c82b30f5c  10.0.18362.0/um/x64/shell32.lib
26502073aab4734ca03fcede01023e85  10.0.18362.0/um/x64/SetupAPI.Lib
19294145f2369b2cdb9ad9d8578b2e9f  10.0.18362.0/um/x64/SensAPI.Lib
a292032a22bdbac84645cdf99159a278  10.0.18362.0/um/x64/security.lib
fa0f0846671960e6cfa70b06f3b367d0  10.0.18362.0/um/x64/Secur32.Lib
841ad190d60c7aa2efb5fe14846040b6  10.0.18362.0/um/x64/SCardDlg.Lib
92831e85023d732c6827a1321c95e87e  10.0.18362.0/um/x64/resutils.lib
738620bf904f4c5be71852f396bb9f58  10.0.18362.0/um/x64/qwave.lib
f781a0d6dd9d172818ab0bc940061fd3  10.0.18362.0/um/x64/OneCore.Lib
ec02083929cdd1f8980590ad450bb726  10.0.18362.0/um/x64/ondemandconnroutehelper.lib
a474298645d22fbbf01775843083dd48  10.0.18362.0/um/x64/OleAut32.Lib
b9e6a291ae0f20f1e876e842e45379fe  10.0.18362.0/um/x64/Ole32.Lib
4ecbc52503fd68b287715a9fc1c84173  10.0.18362.0/um/x64/odbccp32.lib
4017a5f2fa0b3650902d41dea97ea64f  10.0.18362.0/um/x64/MSTask.Lib
b787268ba09b921a36072d78f4d018a7  10.0.18362.0/um/x64/msdelta.lib
f55eb061cfe18bef1423a71a23c4f3a2  10.0.18362.0/um/x64/MsCtfMonitor.lib
1dfa70e4fc461e589d3d4c55f4155f93  10.0.18362.0/um/x64/MSAJApi.lib
efdb97a0dbd359c47fed71e7a89f983d  10.0.18362.0/um/x64/MSAcm32.Lib
11e2847431f02b28983b452819ca9f7c  10.0.18362.0/um/x64/msaatext.lib
08c151e7c0746a9fa8f36617f39b7fef  10.0.18362.0/um/x64/Mprapi.Lib
8b32c77cf9b5f8ef7d97a34ffb3b5797  10.0.18362.0/um/x64/mincore_downlevel.lib
e1bd475d278ca247956ff3ace5e139d4  10.0.18362.0/um/x64/MMC.Lib
48bed4bbd8539c1b89b2d7f960841169  10.0.18362.0/um/x64/mi.lib
2ee2921a0fdd23dcb84fa920ccdf5c02  10.0.18362.0/um/x64/mfuuid.lib
f3893859c2e606b87aed53d6b736bf96  10.0.18362.0/um/x64/mfsensorgroup.lib
58f580c3be22a3bda2983e3ee9bf1088  10.0.18362.0/um/x64/mfreadwrite.lib
47ded68c97c7d2f113701bdf06e11bcb  10.0.18362.0/um/x64/mfplay.lib
899794d86a74ff8b6b2bf04a58a1f3aa  10.0.18362.0/um/x64/Mfplat.lib
fa6712b4f3595614057a1eb076159d90  10.0.18362.0/um/x64/mciole32.lib
217c6ec1ab703731ffaba4207cb9617a  10.0.18362.0/um/x64/mbnapi_uuid.lib
69cee92a22ef0be3145537dde68d5adf  10.0.18362.0/um/x64/Lz32.Lib
84b204efc953c802330e59b0a4734044  10.0.18362.0/um/x64/locationapi.lib
31d78d88666a201ba9eaeb70020fb112  10.0.18362.0/um/x64/Iprop.Lib
3f8582c08ce8921f294133e22b1da0d1  10.0.18362.0/um/x64/wscapi.lib
76615d590d775aa516bebd202e61a2b9  10.0.18362.0/um/x64/wsdapi.lib
f54240fc1ed0bcd3faf460845335aed4  10.0.18362.0/um/x64/wsmsvc.lib
c2c40558713ddd33f980ebb492346234  10.0.18362.0/um/x64/WSock32.Lib
dd3e8ae4230579cd056a73439913e035  10.0.18362.0/um/x64/xaswitch.lib
688e1f8e9e052f18a9046e9b661b4a2b  10.0.18362.0/um/x64/Xinput9_1_0.lib
82c3ecb96aef5a56705790479ec34d94  10.0.18362.0/um/x64/xmllite.lib
da5a0b6022f8b25778c3879c58cc213a  10.0.18362.0/um/x64/xolehlp.lib
5f5af77c30383ff644756531b65a7eb2  10.0.18362.0/um/x64/xpsdocumenttargetprint.lib
b00b3de72108553d58f3cca0d13f891a  10.0.18362.0/um/x64/xpsprint.lib
a970ee48e37a88211d46af281bb9b87d  10.0.18362.0/um/x64/xinputuap.lib
5c9b8113fd94447288b6dd68a9469201  10.0.18362.0/um/x64/xinput.lib
47621a47252961463bf5ab91f0483c94  10.0.18362.0/um/x64/xaudio2_8.lib
7aeb832eaf65fdfe216c94a38565cbfc  10.0.18362.0/um/x64/xaudio2.lib
a841db61a17842baeeccb3a94e2c21a0  10.0.18362.0/um/x64/xapobase2_8.lib
efeda82a6db564eec82b501efa8cc9e6  10.0.18362.0/um/x64/xapobase.lib
a89ca810666b3fb8c3e29a8bfc4d2726  10.0.18362.0/um/x64/wuguid.lib
e0f84b4a2803e48cf30a013f158564dc  10.0.18362.0/um/x64/WtsApi32.Lib
6f65343be8fa2cc15f3dfb196e303b1d  10.0.18362.0/um/x64/WSnmp32.Lib
35f65400b424f9ebbe197165abe0a6d2  10.0.18362.0/um/x64/wsclient.lib
e6fe421d2970864a92f9f303cd9d880d  10.0.18362.0/um/x64/icuuc.lib
c6ad69eb1d241fabac9d14d4cbbdbd5a  10.0.18362.0/um/x64/Icmui.Lib
8e86b917611afc33961ca0e71e4043ac  10.0.18362.0/um/x64/httpapi.lib
86cbd28c5b6c445130ac13aa518ae320  10.0.18362.0/um/x64/hrtfapo.lib
4cab9c89bda09ec054a1a2f4ab4bb6d6  10.0.18362.0/um/x64/hid.lib
f83ecef0974ceed91f03404fb4e520f9  10.0.18362.0/um/x64/gpmuuid.lib
7fcf9afa6f9b17d8322f344add517f99  10.0.18362.0/um/x64/GPEdit.lib
c041ab31fb6b6e723b5b9565fb11b855  10.0.18362.0/um/x64/FrameDyn.Lib
03b8db81667c0bfcba3a526f0ffcc839  10.0.18362.0/um/x64/FrameDyd.Lib
89947139328808315760f445f37f4653  10.0.18362.0/um/x64/FaultRep.Lib
0ef39068ffcbd3e3e7aed43a69864df3  10.0.18362.0/um/x64/els.lib
308d484f15bc93b3331a3536cb07fc68  10.0.18362.0/um/x64/ehstorguids.lib
fc3faf50c5877e5e25534b9ed0e88ab5  10.0.18362.0/um/x64/efswrt.lib
49bfb5de4a9a646be1b8477be55c2f3a  10.0.18362.0/um/x64/eappcfg.lib
1462ccb1763cc239677e8994220e28be  10.0.18362.0/um/x64/DtcHelp.Lib
308ad1cdd07ea1c2fd54d329a8c45192  10.0.18362.0/um/x64/dpx.lib
0ba604ec98eb5111595944168f6b063f  10.0.18362.0/um/x64/dnsrslvr.lib
3ede080f1344f2702195ae41dc51ee3b  10.0.18362.0/um/x64/DhcpCSvc.Lib
cbaeafa19d0427c284271b7c95c3fd46  10.0.18362.0/um/x64/dciman32.lib
e453e4f90d782b833b0c02447e9a2289  10.0.18362.0/um/x64/DbgEng.Lib
b73704dd07eac3886bd7414f2231c196  10.0.18362.0/um/x64/d3d12.lib
2afcbb646ad618d59a304136b0c0f81b  10.0.18362.0/um/x64/d3d11.lib
500b1136d07115f0ac686b7a19e9db89  10.0.18362.0/um/x64/d3d10_1.lib
1b95d36da8b26e22677e52088ef59510  10.0.18362.0/um/x64/d2d1.lib
8003a5cc1c488e1b9978fbaaf3890438  10.0.18362.0/um/x64/cscdll.lib
0c3c51d3c90f4783ad1bef1c1a754d84  10.0.18362.0/um/x64/ComSvcs.Lib
8df53b7246e04515349d76fb9eb293a0  10.0.18362.0/um/x64/computestorage.lib
ab6b1d1efad75c27aa1d7dcdcd35a09a  10.0.18362.0/um/x64/computenetwork.lib
c97df8ef1ba8351a7bccd4c75db1a090  10.0.18362.0/um/x64/computecore.lib
b7be52580b04a26ae3acf2323116d1b0  10.0.18362.0/um/x64/CompPkgSup.lib
db50ce503600ef9a57ff36ee5d5b3c94  10.0.18362.0/um/x64/ComCtl32.Lib
19bf20636f18c7de55d7b1c8c9662abb  10.0.18362.0/um/x64/ClusApi.Lib
f482521806f352212241701cc0beac17  10.0.18362.0/um/x64/clfsw32.lib
313f22f3250f253efc1ae482bdcdec06  10.0.18362.0/um/x64/clfsmgmt.lib
2a5982c1f10c7b92218625a151ae63bf  10.0.18362.0/um/x64/cldapi.lib
d860458acdca250f7ff28d36f6c36ceb  10.0.18362.0/um/x64/CertIdl.Lib
4209f980a3e298abc841f00fecb4d3af  10.0.18362.0/um/x64/certcli.lib
0fcde5971adbceba8eb52d201bb63060  10.0.18362.0/um/x64/Bits.Lib
2cdfa081b9da5c3a88b6a880802a2c1b  10.0.18362.0/um/x64/avifil32.Lib
da780857981073eb6a69b4f96150a39f  10.0.18362.0/um/x64/AuthZ.Lib
a61bc0e92efd5a4ddac5189c6484eea4  10.0.18362.0/um/x64/AudioBaseProcessingObjectV140.lib
38fc704d7935c396986fb59706bd5d1c  10.0.18362.0/um/x64/audiobaseprocessingobject.lib
51c3719d03580c8183f55571dbc9e198  10.0.18362.0/um/x64/appnotify.lib
ba3f475e12f8e6e327028332d96603f6  10.0.18362.0/um/x64/appmgr.lib
f6e2284c9a3afe88bcc5485fad668572  10.0.18362.0/um/x64/appmgmts.lib
c674acc96c1153cafd50a4a23143cb7d  10.0.18362.0/ucrt/x86/libucrt.lib
43f66241dac7dbd78459d29214c9ef7d  10.0.18362.0/ucrt/x86/ucrtd.lib
51171c76b1c50e38049067d0d7d27d36  10.0.18362.0/ucrt/x86/ucrt.lib
35bd736208f1156c84f1713f5594a246  10.0.18362.0/ucrt/x86/libucrtd.lib
d22131877c145be64dff9a0cdfbca51c  10.0.18362.0/um/x64/mincore.lib
cdc5411520502d69a5f77b548eb668f1  10.0.18362.0/ucrt/x64/ucrtd.lib
b7cd4e115e865ad89e5884982c7c1826  10.0.18362.0/ucrt/x64/ucrt.lib
e49681d4520e4fee27053bd83e8173e5  10.0.18362.0/ucrt/x64/libucrtd.lib
f27086f2670d91c8261a39d150773327  10.0.18362.0/ucrt/x64/libucrt.lib
```

### ucrt: 10.0.19041.0

```
9c4f24de4c8eca643235e15cd07140cf  10.0.19041.0/um/x86/wofutil.lib
cb1b1a955b1ee4796dacb896f094269f  10.0.19041.0/um/x86/wmvcore.lib
f77984d9ce45f0cd24f4cc6f1e0c38ba  10.0.19041.0/um/x86/wmiutils.lib
7f009d617ade7b51e05e468ce153613a  10.0.19041.0/um/x86/wmip.lib
13e124d41fb5c937563c3eaf623edb6e  10.0.19041.0/um/x86/wmcodecdspuuid.lib
f801e2498e5c26db740df204af8ee217  10.0.19041.0/um/x86/Wldp.Lib
3f7c3f6b95dadc2fb2f3014777bf5a5f  10.0.19041.0/um/x86/Wldap32.Lib
77d50ad41455085032984960582345e0  10.0.19041.0/um/x86/wlanui.lib
8cd7630583ad0b8fbeb73bd31efe56ed  10.0.19041.0/um/x86/wlanapi.lib
e96410aab1f7a5eed8045b9ddcae31af  10.0.19041.0/um/x64/AclUI.Lib
681c9c7321c3abd4d2264d37daf51fdf  10.0.19041.0/um/x64/ahadmin.lib
534b0d17dc860957c500e86cb9e1054d  10.0.19041.0/um/x64/amsi.lib
dbf2e79a9f8def5aa5fd35969f520164  10.0.19041.0/um/x64/appmgr.lib
51c3719d03580c8183f55571dbc9e198  10.0.19041.0/um/x64/appnotify.lib
27066fc3cb7fbcf210b5e1e21d512efa  10.0.19041.0/um/x64/appmgmts.lib
5d3e2648643142812f4a360a6681f38d  10.0.19041.0/um/x64/AudioBaseProcessingObjectV140.lib
b106beb800424947564644eb22b87cc6  10.0.19041.0/um/x64/AuthZ.Lib
43a7a92e993e54490f2d6582bad8e84e  10.0.19041.0/um/x64/avifil32.Lib
046aec1ee5392c373ff9b525247b16b4  10.0.19041.0/um/x64/CompPkgSup.lib
43a24a2c201511bd3215e24cb086e2ea  10.0.19041.0/um/x64/CoreMessaging.lib
eb623cb8b9fa6ad05bbeb8a7958ec3f6  10.0.19041.0/um/x64/Credui.lib
3c61ca4b4a5e2c9ccb6b8ab2da611d1e  10.0.19041.0/um/x64/Crypt32.Lib
2c488262229c56ec82cd1431a72c5f03  10.0.19041.0/um/x64/CryptNet.Lib
bc28ebb138cf7c28e165b896f863ed4c  10.0.19041.0/um/x64/cryptui.lib
75a3ab63d4f902621a2b78e8924ca363  10.0.19041.0/um/x64/cryptxml.lib
9b373388772ca4c7c9371198745a2c8b  10.0.19041.0/um/x64/cscapi.lib
79fa7624dc7e23b184a78f03514d9dd8  10.0.19041.0/um/x64/cscdll.lib
cfe45bacd04153fdc4896068c511aeea  10.0.19041.0/um/x64/dhcpsapi.lib
12a6ede73a6bf2ce83f19e57226355ee  10.0.19041.0/um/x64/DhcpCSvc6.Lib
20c67f890eadc73fdceb3ea1068133b6  10.0.19041.0/um/x64/DhcpCSvc.Lib
ce8d8daf520540706bcce4a1027a4fb7  10.0.19041.0/um/x64/dflayout.lib
2618f32317d1d9d4a86a14c99b4a3fd9  10.0.19041.0/um/x64/devmgr.lib
5e183419035b31214e5414f27d90cb7f  10.0.19041.0/um/x64/deviceaccess.lib
c6eb9da7bdd07e0524acee7f7b328d0f  10.0.19041.0/um/x64/devenum.lib
7e7fcf417b051b0519a30383a397fa72  10.0.19041.0/um/x64/ddraw.lib
022b12cbf2e73bf5fc3786976954ad20  10.0.19041.0/um/x64/dcomp.lib
4a1662d7ddc335223d69d9e857b42e79  10.0.19041.0/um/x64/dciman32.lib
b52f1a5e24743b5d537836cdf5dc7a93  10.0.19041.0/um/x64/drt.lib
17351ade636544057867dad09b0b5866  10.0.19041.0/um/x64/drttransport.lib
b763ed0a8ae524ff57215922f37b83cc  10.0.19041.0/um/x64/DSProp.Lib
a9cd09a082cac642194f18c26edb410c  10.0.19041.0/um/x64/dststlog.lib
3e73829141497d89f37bb36dcff2c992  10.0.19041.0/um/x64/eappprxy.lib
8b5b7fb9e50c499d94c0d7d903ed2f71  10.0.19041.0/um/x64/easregprov.lib
db93ad337f2acfb834297b8e50088148  10.0.19041.0/um/x64/efswrt.lib
1098ab642b991cfb55cae089bb65e6d9  10.0.19041.0/um/x64/ehstorguids.lib
fc69a47d6c86ded0fe1ad4f293f0f10b  10.0.19041.0/um/x64/elfapi.lib
a3cae5cf391249e3665f2c5f6dc5233c  10.0.19041.0/um/x64/FrameDyn.Lib
f404887fcfec2f41ed80da2505c5349b  10.0.19041.0/um/x64/fxsutility.lib
b4bd1eb0bc6ac406f8be137b1c9d1053  10.0.19041.0/um/x64/Gdi32.Lib
fffd7e743c34d3e3d0d3c11f2ab78177  10.0.19041.0/um/x64/gdiplus.lib
fe62f2dd600475cbd5ea1114fe88cbda  10.0.19041.0/um/x64/glmf32.lib
f33d7fc1e465e4cd949c69b62326240f  10.0.19041.0/um/x64/GlU32.Lib
798dbb15c286f06d2d6e181b25ac928a  10.0.19041.0/um/x64/hbaapi.lib
4222908a12dd29ff466cf25fc72fc26d  10.0.19041.0/um/x64/ImageHlp.Lib
67272f57eaf0e1d8f0eb78db4d68ff4b  10.0.19041.0/um/x64/imgutil.Lib
10f80d8a9d65a59c474619c360752ddc  10.0.19041.0/um/x64/Imm32.Lib
c4de4cc8a517beef960bc15461f50e39  10.0.19041.0/um/x64/infocardapi.Lib
570ad3945ae675de0c6df08a0f494710  10.0.19041.0/um/x64/inkobjcore.lib
7fdc3b26c7d90344f16cde9b74dfdb8e  10.0.19041.0/um/x64/inseng.lib
714f08bbb856ba4413892927931f1a55  10.0.19041.0/um/x64/Iprop.Lib
d893087e05289caffce920c8fa0bc944  10.0.19041.0/um/x64/iscsidsc.lib
faf5fbd441b55e238b2300312392da7d  10.0.19041.0/um/x64/IsolatedWindowsEnvironmentUtils.lib
967ace104d8393797ededa3f56427e4c  10.0.19041.0/um/x64/kerbcli.lib
bad18dbaade981444c690eae8114f329  10.0.19041.0/um/x64/kernel32.Lib
b2d4d83d005964372bc85e75e9a143ed  10.0.19041.0/um/x64/kernel32legacylib.lib
fe4310de47e483c3531697737e38ab70  10.0.19041.0/um/x64/keycredmgr.lib
073a4f3b79871ea033cfa87e148686a6  10.0.19041.0/um/x64/KSProxy.Lib
c68bb34888a91082a04508d49b9224c6  10.0.19041.0/um/x64/ktmw32.lib
5b395a77518c2255539898318016a2ef  10.0.19041.0/um/x64/LoadPerf.Lib
80e64366f241da95c027eea340323b97  10.0.19041.0/um/x64/locationapi.lib
ad952b36a27318f1da740e2962865d5d  10.0.19041.0/um/x64/Lz32.Lib
148c9fcd211d745dafda1a3909bef391  10.0.19041.0/um/x64/ksuser.lib
d9abc6a763872be681062d069e932a15  10.0.19041.0/um/x64/magnification.lib
ce0c28e44556ae2ca331e9fcaca4f0c7  10.0.19041.0/um/x64/MAPI32.Lib
ac3e4fd88e191cb5d41c00575afbb972  10.0.19041.0/um/x64/mbnapi_uuid.lib
e9d542a19959822e1f204027e47b8942  10.0.19041.0/um/x64/mciole32.lib
1174cdc40ca2f983ff141023330b275e  10.0.19041.0/um/x64/Mf.lib
4e8f3b2e06f06dfd7929344581820ebb  10.0.19041.0/um/x64/Mfcore.lib
9cc92bb132d1be43d8c2ff8d1362b79d  10.0.19041.0/um/x64/Mfplat.lib
dc46e53cf15a8d17b54aeb246b819263  10.0.19041.0/um/x64/mfplay.lib
f3cbf20f267e19d54523d7db1be16604  10.0.19041.0/um/x64/mfreadwrite.lib
436ca370e4a6afee9173769474196a81  10.0.19041.0/um/x64/mfsensorgroup.lib
73829011dc2c7f0a85de3b59b09c1d26  10.0.19041.0/um/x64/Mfsrcsnk.lib
c12bdc909baed6ec6f6e19754dae0f50  10.0.19041.0/um/x64/mfuuid.lib
940cbbff7d57e35008a1414bef3cfb79  10.0.19041.0/um/x64/MgmtAPI.Lib
8b0e2a172f27228906019389fc26cf35  10.0.19041.0/um/x64/mi.lib
b922bb17f8d0087d5b1bbcb362c607d7  10.0.19041.0/um/x64/mincore.lib
a86f0af305343a2f762c1348f38556df  10.0.19041.0/um/x64/mincore_downlevel.lib
e89f093cd07e2934436ba6a3e2e8e45c  10.0.19041.0/um/x64/mmdevapi.lib
f5b1bf8bda4e7d614866b18a888d56b2  10.0.19041.0/um/x64/MMC.Lib
07fbc9de090de831cc50fb1b0449e8f7  10.0.19041.0/um/x64/Mpr.Lib
5cf4925c1ffc228caa522eae64cd11c5  10.0.19041.0/um/x64/Mprapi.Lib
5d0764c24a02412f8d457bb1310a0188  10.0.19041.0/um/x64/MDMRegistration.lib
3e8886e900e256c0ee76bf34d5f70984  10.0.19041.0/um/x64/mprsnap.lib
032eeead99b201e98c15ad4e209adc15  10.0.19041.0/um/x64/mdmlocalmanagement.lib
9e553d1fd49e63eb65b93a1737a0fa5b  10.0.19041.0/um/x64/MqOA.Lib
b6cd9382032e09b5d6193642d15cd816  10.0.19041.0/um/x64/msaatext.lib
5e827fb70a0a01bdf1080faf8929b973  10.0.19041.0/um/x64/MSAcm32.Lib
8c3f990e75e95b3b9393b51912bc0176  10.0.19041.0/um/x64/MSAJApi.lib
a82f6f01bd5d81c46d7ebd5c4582ce7a  10.0.19041.0/um/x64/Mscms.Lib
a6fadcd26418cb0c6facfcbaff3c16f8  10.0.19041.0/um/x64/msdasc.lib
280437a9588aaaaee6479a7891ff594c  10.0.19041.0/um/x64/msdelta.lib
b8750f7245f2e3cfd0f84577687479bd  10.0.19041.0/um/x64/msdrm.lib
5bfadb4c31b427c38c34b635332e5945  10.0.19041.0/um/x86/wsmsvc.lib
25459b5047b364fb909142a2f2d53e3e  10.0.19041.0/um/x86/WSnmp32.Lib
fffbf0287c8f7a6384e641df48a85888  10.0.19041.0/um/x86/WSock32.Lib
c79394267d7432b94a1c960e55c1d1a6  10.0.19041.0/um/x86/wuguid.lib
cf2b76b7ba55cbcb9f11298bf6aecb21  10.0.19041.0/um/x86/xaswitch.lib
41a6b13c40e64fc76a70186921d5df9b  10.0.19041.0/um/x86/Xinput9_1_0.lib
235453bdcc64e1e67330a23cfca8f607  10.0.19041.0/um/x86/xinputuap.lib
8b8ea5e5f91dfd91dcbf94dd26942c15  10.0.19041.0/um/x86/xmllite.lib
f81f0d84d091d1fe89388ede0ffbf4a2  10.0.19041.0/um/x86/xolehlp.lib
00723af8cd30c193229f6deb93e1e36b  10.0.19041.0/um/x86/xpsprint.lib
6876c2e5631a4f19a6acbc6426096995  10.0.19041.0/um/x86/xpsdocumenttargetprint.lib
38bcf561b366b99596172e333fe82ce5  10.0.19041.0/um/x86/xinput.lib
b8bc71b5b6a718f58b593e56b4dd211f  10.0.19041.0/um/x86/xaudio2_8.lib
670ca56b0ce95be262a9119792e80aec  10.0.19041.0/um/x86/xaudio2.lib
0be2ce00552e8767dcd9998ad551352e  10.0.19041.0/um/x86/xapobase2_8.lib
0497cb36fb9728f28661b3343904537c  10.0.19041.0/um/x86/xapobase.lib
4c506daf614f3f84798a4f27471800c2  10.0.19041.0/um/x64/Msi.Lib
95bdaa6c21a51c4edaff133b17e2eec5  10.0.19041.0/um/x64/mspatchc.lib
3eb38ed7af1adee21263bdba8fdebfab  10.0.19041.0/um/x64/mspbase.lib
033c6949227784f39698cec383049bfc  10.0.19041.0/um/x64/MsXml2.Lib
8b199558f413827c9960b7ac113b7c9b  10.0.19041.0/um/x64/msxml6.lib
c155b0b5ed8ffc86957d88b4f3c034d7  10.0.19041.0/um/x64/mtxdm.lib
df363e3e1baaeb8808e3ee4261dfdeac  10.0.19041.0/um/x64/muiload.lib
43e00ea76d3444384855979a44a02069  10.0.19041.0/um/x64/ncrypt.lib
86e35c3f5036d56a7fe1683dff5be8f6  10.0.19041.0/um/x64/nddeapi.lib
7983ad394decff9c694efcc20f25815f  10.0.19041.0/um/x64/ndfapi.lib
59b331fec894347025b7a4a9779dd899  10.0.19041.0/um/x64/ndproxystub.lib
b4df38dc19c211bc510ca623adeee126  10.0.19041.0/um/x64/NetAPI32.Lib
00871c7e104bc0aa32738a4dbd3fa268  10.0.19041.0/um/x64/nanosrv.lib
4ca95505cf8e2efab1961cae3e5866d4  10.0.19041.0/um/x64/NetSh.Lib
5f4dfd7fae0d3dcdea062cd91ab2b74c  10.0.19041.0/um/x64/newdev.lib
3a7941aa16bc8a58099eba67355e101a  10.0.19041.0/um/x64/ninput.lib
3968fc400c255debd860798e1a5df95d  10.0.19041.0/um/x64/normaliz.lib
9f9ae4b69115d425a8eacc9305808529  10.0.19041.0/um/x64/netlib.lib
d95e3c242db4d83892bbc8d6d06a28c2  10.0.19041.0/um/x64/nt.lib
dc4ab5d244d8e1e7cb3539ca41676081  10.0.19041.0/um/x64/ntdll.lib
0d5cf04a44cc9ed03416dd2efca64326  10.0.19041.0/um/x64/ntdsa.lib
e8a9f3cb4247524cbc69e979866cf064  10.0.19041.0/um/x64/NtDsAPI.Lib
30653a9ca9112ec558955843ca986d8f  10.0.19041.0/um/x64/ntdsetup.lib
4d5ef05b7f8ba3e80fb19cb2382d68b4  10.0.19041.0/um/x64/ntfrsapi.lib
c1eac8a096cda55f7a72c01281f9957a  10.0.19041.0/um/x64/ntmarta.lib
b4c101ef1b6ea7465c880d7b6b3611cf  10.0.19041.0/um/x64/NtQuery.Lib
7de20051da6a946cc93701b0807a7a5c  10.0.19041.0/um/x64/ntstc_msvcrt.lib
0d37d3bec453cb0ddffc91b3450379dd  10.0.19041.0/um/x64/objsel.lib
795f579d7a6f30fc42f755c5e961a6b7  10.0.19041.0/um/x64/odbc32.lib
484bc1a9fe7a1305cb6de7a9529266db  10.0.19041.0/um/x64/odbcbcp.lib
83e30fbff8e13c8fc15c596c0192c576  10.0.19041.0/um/x64/OemLicense.lib
e666bd02caa0948593f05c39c7026fa8  10.0.19041.0/um/x64/OleAcc.Lib
f1089f81130c53f1b2f6d2f751a3d255  10.0.19041.0/um/x64/Ole32.Lib
515721b7e1e62309f705cf281fb43c3b  10.0.19041.0/um/x64/olecli32.lib
63e8cdb62428e5f1078ac5a575dd9e6a  10.0.19041.0/um/x64/oledb.lib
fdb2224669edcefad7d15c41c6f72fe9  10.0.19041.0/um/x64/OleDlg.Lib
14021e90dff81bce629a881d458852fa  10.0.19041.0/um/x64/olesvr32.lib
f3aa4e0dee165e7acc03ad19f3817fe0  10.0.19041.0/um/x64/ondemandconnroutehelper.lib
31889d1281b69c9bcc77dc62c18a7767  10.0.19041.0/um/x64/OneCore.Lib
376c271283aba7a7e9821d2bf92af1b9  10.0.19041.0/um/x64/OneCoreUAP.Lib
5cd529460d1f8de053f2146144019e17  10.0.19041.0/um/x64/OneCoreUAP_apiset.Lib
9a9c346d19dab812ce6f86e8a5f38c24  10.0.19041.0/um/x64/OneCoreUAP_downlevel.Lib
4624fa16cac8d2c996b1fe755cc0e241  10.0.19041.0/um/x64/OneCore_apiset.Lib
c30257361b284435d915b5b6143b6325  10.0.19041.0/um/x64/OneCore_downlevel.Lib
07715493b40c3295a1f4c84730aff22c  10.0.19041.0/um/x64/opmxbox.Lib
15a63d86b67529ce439b21e832be8970  10.0.19041.0/um/x64/osptk.lib
7dd75c5326da3ad5c417808eae501472  10.0.19041.0/um/x64/p2p.lib
2e8028840e432b7e322d69d5aecc8970  10.0.19041.0/um/x64/OpenGL32.Lib
faa5ea3232894f56166444aef3913255  10.0.19041.0/um/x64/p2pgraph.lib
774f231327a1f08b993beb4831158f7d  10.0.19041.0/um/x64/pathcch.lib
347e8dcec2a3f7a917f70291976947e0  10.0.19041.0/um/x64/Pdh.Lib
437b438eb311ff1c98e1b9f02dadded1  10.0.19041.0/um/x64/PeerDist.lib
5941d13b6242d586140bcb7e14029338  10.0.19041.0/um/x64/PhotoAcquireUID.lib
9cf68b6405e97dd044e5ba54a614b89a  10.0.19041.0/um/x64/PortableDeviceGuids.lib
834131d6232352420dc00c788ecf731b  10.0.19041.0/um/x64/powrprof.lib
9bbcba754269dae4cdf1d73ba76541fd  10.0.19041.0/um/x64/prntvpt.lib
5fb97a5c621f3ea894f9d3f2c72d6ba4  10.0.19041.0/um/x64/ProjectedFSLib.lib
7c096eaf4aed1f904c7190a2e75b3218  10.0.19041.0/um/x64/propsys.lib
bc3f41487c12a96e5004019bf353276b  10.0.19041.0/um/x64/Psapi.Lib
63d9bfb69e8dc869329db8ae237ede32  10.0.19041.0/um/x64/quartz.lib
b4c101ef1b6ea7465c880d7b6b3611cf  10.0.19041.0/um/x64/query.lib
84fa0973d7086d14492ad229af5a00ce  10.0.19041.0/um/x64/qwave.lib
058c89797a9a72c0c517f49a60f7e4af  10.0.19041.0/um/x64/RASAPI32.Lib
e45d56687c437400160633dba66c9399  10.0.19041.0/um/x64/RASDlg.Lib
0387ffe6b54fd9f024fe359b12eccd9b  10.0.19041.0/um/x64/rasuser.lib
6d4c5e8eeb86a10cf851cac021ee9e7f  10.0.19041.0/um/x64/resutils.lib
82e419b232a28ab029e0dc04fe46cf7b  10.0.19041.0/um/x64/rometadata.lib
8ce3110358b53bbe3f94c230644ce276  10.0.19041.0/um/x64/rpcexts.lib
85a0d3a36a82ef469b1a1c9a91850416  10.0.19041.0/um/x64/Rpcns4.Lib
eecb8114b4b127be2dcc655457ae73ad  10.0.19041.0/um/x64/rpcproxy.lib
d3b391a0b75f9ba4a77d1b970cee80dd  10.0.19041.0/um/x64/OleAut32.Lib
c73aa55f34ace7347fb4f2474299cbd0  10.0.19041.0/um/x64/RpcRT4.Lib
252e4e5d7a8fcf8b7f602bee8e1be5f1  10.0.19041.0/um/x64/rpcutil.lib
48edec346d434ef6302f024797edef4f  10.0.19041.0/um/x64/rstrtmgr.lib
54658dd5ee30aaaf2d3bd0573cbe6925  10.0.19041.0/um/x64/Rtm.Lib
378d751c88d27efa4953b920b41c7f25  10.0.19041.0/um/x64/rtutils.lib
705b7d2eef80ddd0aacfd91b829d357f  10.0.19041.0/um/x64/RTWorkQ.lib
a78836b05fd2c119b9525339bf4e465e  10.0.19041.0/um/x64/runtimeobject.lib
193c29430e0e0b09f955795847f77255  10.0.19041.0/um/x64/samlib.lib
9afa0aaa5ae0e20370215a2993d95a95  10.0.19041.0/um/x64/samsrv.lib
2bed03f4828a453945dd55e359da44f7  10.0.19041.0/um/x64/SAPI.Lib
4db955a68815f7649c59df321ff9f6fb  10.0.19041.0/um/x64/odbccp32.lib
302a7918b48a98025d341c487a2736a7  10.0.19041.0/um/x64/sbtsv.lib
d1d04d8a1b6757aa176a1686cf1146b2  10.0.19041.0/um/x64/sas.lib
c6a06f6b27039b45c936a4a516dc0915  10.0.19041.0/um/x64/SCardDlg.Lib
6f695f57006cd943d21a1902d274f255  10.0.19041.0/um/x64/scecli.lib
df90916c41aab17e0f140d6a9cb8f853  10.0.19041.0/um/x64/scesrv.lib
dd16cd43446c86a579b9afd419bdce10  10.0.19041.0/um/x64/ntstc_libcmt.lib
1aa9f2ddb8425904137ee24d937b65f9  10.0.19041.0/um/x64/schannel.lib
8ef0ecbcc7d23796287d09abc3b19ea0  10.0.19041.0/um/x64/ScrnSave.Lib
71eefed7bae2118a2738e487d778108b  10.0.19041.0/um/x64/ScrnSavW.Lib
a9d0d4c8cf0ee83c294cde68602b892d  10.0.19041.0/um/x64/ntlanman.lib
12d5bae9762aef227b3a797f999da0b4  10.0.19041.0/um/x64/SearchSDK.lib
49721b5db5c6c67b930b7eb6b83f5b8c  10.0.19041.0/um/x64/security.lib
5526ff6c0fad88279c7dbc300f7119c5  10.0.19041.0/um/x64/sens.lib
2d0a8c676a444a0731e2e71cc1b273ed  10.0.19041.0/um/x64/Secur32.Lib
249bee92432813d3c452264078052363  10.0.19041.0/um/x64/SensAPI.Lib
9b871ab06e4bb3414a0e5676fc317aa5  10.0.19041.0/um/x64/sensorsapi.lib
b7892fa38558f0dde28a355916c64ea1  10.0.19041.0/um/x64/ntdsatq.lib
b1a248b95e0fb0ef4736b37f35c2cc9c  10.0.19041.0/um/x64/SensorsUtils.lib
d984902a80f29fb6e5a00b4b60a199ed  10.0.19041.0/um/x64/Sfc.Lib
f7747ae5711144054d3cfa51784af32a  10.0.19041.0/um/x64/SetupAPI.Lib
57018565afc72b9f711be0bf8cfd02ea  10.0.19041.0/um/x64/shdocvw.lib
395a01574168b8affe38167e0069ae33  10.0.19041.0/um/x64/shcore.lib
d6be2ed5e5dac0fb9509298fa1d5ae5e  10.0.19041.0/um/x64/shell32.lib
f561cafb3ba0e63df97f1c3c79cb03af  10.0.19041.0/um/x64/slc.lib
33001ce918a5e5ff2ebd0dffc3541518  10.0.19041.0/um/x64/slwga.lib
5000adf18a77b973c1a509775fe8f4ae  10.0.19041.0/um/x64/SnmpAPI.Lib
b3160acc3bc8130ab379d45f285dc909  10.0.19041.0/um/x64/spoolss.lib
54537933c4a2a8bc8a3f12ce170e1e5c  10.0.19041.0/um/x64/SpOrder.Lib
16f6da56d620091487294ec34e808039  10.0.19041.0/um/x64/SrClient.lib
1635efe321f093241f5bf5169bed62d6  10.0.19041.0/um/x64/srpapi.lib
19488d9fee11b8ca737f7e21aac6bd8b  10.0.19041.0/um/x64/ssdpapi.lib
ab4b26175fdaa041501ce73e6e75e390  10.0.19041.0/um/x64/strmbase.lib
7279c820bc71255707f9f2a78f350c7b  10.0.19041.0/um/x64/strmiids.lib
f6a2e02a4fbb09cc4b651fefd1e3f80b  10.0.19041.0/um/x64/Sti.Lib
f699ee24da3d824dc9cde5a30767365e  10.0.19041.0/um/x64/strsafe.lib
b2173e57da8350bfaf127d360b13c7e8  10.0.19041.0/um/x64/structuredquery.lib
591b44746bc096fac328b4a7d36836f3  10.0.19041.0/um/x64/Svcguid.Lib
a899b457137a1eac9ac13f9ccaceb7cf  10.0.19041.0/um/x64/swdevice.lib
eb20d70ef5f4cde42bdda9d9d19646ce  10.0.19041.0/um/x64/synchronization.lib
867d2c96a727a9f5236b3d14db093d68  10.0.19041.0/um/x64/t2embed.lib
8116550656b5652985eb36ab65585d90  10.0.19041.0/um/x64/Tapi32.Lib
e7495dfbdec16df58a47f2c59264e563  10.0.19041.0/um/x64/tapi32l.lib
7ec26d1b66bfb763db920fb58462135e  10.0.19041.0/um/x64/taskschd.lib
ddfa4e5c989c7cc5811daa1b832626bd  10.0.19041.0/um/x64/tbs.lib
b31d4bd0b32ef130bd0dc1e8d19779e7  10.0.19041.0/um/x64/tdh.lib
8ad4f1f91ec14e380ef2ed2271942342  10.0.19041.0/um/x64/tokenbinding.lib
ff1fb069c0d72e63e39e7589188b28cc  10.0.19041.0/um/x64/Traffic.Lib
546c0d708ffc55cab2af0b4238ddc47f  10.0.19041.0/um/x64/TranscodeImageUID.lib
ae7b7600a99bcc783dbfd26ff8696a46  10.0.19041.0/um/x64/tsec.lib
d42fe3d90fe52175caa69f73bb6f2d57  10.0.19041.0/um/x64/tspubplugincom.lib
76d2db7befc615fc1f6c4eb73587c8c2  10.0.19041.0/um/x64/twinapi.lib
4b194925eb2c78b7315b5b5c33a2ee42  10.0.19041.0/um/x64/txfw32.lib
6b51a91a725af875218c3d9e8518ae00  10.0.19041.0/um/x64/ualapi.lib
379e3c8d6310ce2e7bad2c3b86f8137a  10.0.19041.0/um/x64/UIAutomationCore.lib
b40352943f6cc4a904278c759e687b40  10.0.19041.0/um/x64/umpdddi.lib
3624fad012108f6a410ed0bfd0b904f2  10.0.19041.0/um/x64/Urlmon.Lib
9ba777dd530eb9e6020d02f9ccaa5bfa  10.0.19041.0/um/x64/User32.Lib
3b30b3bdb083e5ddba0a1d8e93a1bc61  10.0.19041.0/um/x64/UserEnv.Lib
09b62aa695d9a6d47a3fd674c18b77d6  10.0.19041.0/um/x64/Uuid.Lib
a21b10e8f2ef605a136700b29c60f149  10.0.19041.0/um/x64/Uxtheme.lib
74810300897512ee4723f0b3e36168b6  10.0.19041.0/um/x64/USP10.Lib
0b2c575245ba05ecaaf20481f1bccde3  10.0.19041.0/um/x64/vccomsup.lib
937e50ecbaab5227236eb5518f9bee51  10.0.19041.0/um/x64/vds_uuid.lib
ee0171bf655a5b070963747b84c540fd  10.0.19041.0/um/x64/Version.Lib
3044484a8cdc9eaf7bf3d7255a9848a7  10.0.19041.0/um/x64/vertdll.lib
2d468d9b9a31bfcc0ec50d73e8db0377  10.0.19041.0/um/x64/Vfw32.Lib
f80eb6a9a82fb3c204de4cc07936ad36  10.0.19041.0/um/x64/Virtdisk.Lib
8362c20ea6d67b89ab0bd95cb0e33442  10.0.19041.0/um/x64/vmsavedstatedumpprovider.lib
0ee6db7532452de93436725eeaf19f54  10.0.19041.0/um/x64/vscmgr.lib
ee5996ad56d04a7a6d9222cf39cc308d  10.0.19041.0/um/x64/vssapi.lib
70e60640b5ee2304d738b1044f6d35dd  10.0.19041.0/um/x64/vss_uuid.lib
ba62192932b69366d7786da49130288b  10.0.19041.0/um/x64/vstorinterface.lib
2cfb8026b9aebf0afef9579ddcd9f71a  10.0.19041.0/um/x64/wbemuuid.lib
e97c6147534d43312970adc2685c967b  10.0.19041.0/um/x64/wdsbp.lib
d1cd1e39fde7338e9273a97bad1f1fb3  10.0.19041.0/um/x64/wdsmc.lib
23688749396ba1521c8456ecdfb10245  10.0.19041.0/um/x64/wdspxe.lib
9541247a2803fd650e482a0978e56500  10.0.19041.0/um/x64/wdstptc.lib
d93f574a351de1bd93d1e5a303cafe3f  10.0.19041.0/um/x64/webauthn.lib
49935646ee8e41af1190feafad680d84  10.0.19041.0/um/x64/WebServices.lib
f214575269370e601c804420425158bc  10.0.19041.0/um/x64/websocket.lib
8722b9f0f1d55346a5fba0cc8fe1817a  10.0.19041.0/um/x64/wecapi.lib
29f7588420d8ef820ab3c7ef0b0c7376  10.0.19041.0/um/x64/Wer.lib
a291b771d2cf1267a1908025a7b6ca10  10.0.19041.0/um/x64/wevtapi.lib
11bfbcd82b4119db82699409773e9940  10.0.19041.0/um/x64/WiaGuid.Lib
9b954bcb889b1c7146e1d0558443ef4d  10.0.19041.0/um/x64/wiaservc.lib
02527dbfb052fbd944bb284fe34ff1f8  10.0.19041.0/um/x64/wiautil.lib
4275cf06cc3503f3e9db549944ecde78  10.0.19041.0/um/x64/WinBio.lib
e0f0fea7c783e74f2c6ef3561147b518  10.0.19041.0/um/x64/windows.ai.machinelearning.lib
e6ffeda5e0fb145e27f82c9f46a85d83  10.0.19041.0/um/x64/windows.data.pdf.lib
0d6f93e5ceb9a299c757e43b75bbc231  10.0.19041.0/um/x64/windows.media.mediacontrol.lib
da962e4111f5a31261106c8b1b2a96cd  10.0.19041.0/um/x64/windows.networking.lib
f34975c94f4ccce818d3beb50279feb9  10.0.19041.0/um/x64/wdsClientAPI.LIB
219a8db3065b234a53bf224b1b01d29b  10.0.19041.0/um/x64/windows.ui.lib
c8165ffe3a7bd2ec848b44e3d2f039fb  10.0.19041.0/um/x64/wcmguid.lib
1ced3acff505da9e694fef6e7801c845  10.0.19041.0/um/x64/WindowsApp.lib
922c0e13beb5364f19a0c9d4e620d5ea  10.0.19041.0/um/x64/wcmapi.lib
645752ab3070a7d39a76009450205990  10.0.19041.0/um/x64/WindowsApp_downlevel.lib
b485323296c17a5429c1d42c213afb6b  10.0.19041.0/um/x64/windowscodecs.lib
31d916a5bd8c0d3a0d28c824cfc9e912  10.0.19041.0/um/x64/windowscoreheadless.Lib
7dbfb5f3a4b38ba44c338abc46607526  10.0.19041.0/um/x64/vmdevicehost.lib
6421ffc19b52db5cacf05abbe67f9b10  10.0.19041.0/um/x64/windowscoreheadless_apiset.Lib
95264752d7f70672f1b22cddb29d45db  10.0.19041.0/um/x64/windowssideshowguids.lib
772bdb0a48425b7d0248d7fda70d72ab  10.0.19041.0/um/x64/winfax.lib
aba291a90b3f672fbc2b1b172f330a91  10.0.19041.0/um/x64/winhttp.lib
be8b44541bf8d38641c8107d8514a664  10.0.19041.0/um/x64/WinHvEmulation.lib
f84a752697e0ab8995cc84dda9a11c40  10.0.19041.0/um/x64/WinHvPlatform.lib
165015417ed248ef58541fc2ba3ed028  10.0.19041.0/um/x64/winml.lib
9143806a61754d927d3ca03dbd74502c  10.0.19041.0/um/x64/winsatapi.lib
8b3177baecde127f1c4ce9c085e2f60e  10.0.19041.0/um/x64/winscard.lib
1fec2165b15d7253082135c097f8a72d  10.0.19041.0/um/x64/winsqlite3.lib
86b31a012812e5f33820a7d79ed7cd61  10.0.19041.0/um/x64/WinMM.Lib
4bf868bf8c83a3ee17bf1509faf986f3  10.0.19041.0/um/x64/winsta.lib
57868ffc4f4a8a4a91ecbaf4875eed61  10.0.19041.0/um/x64/WinStrm.Lib
988b51647c5e7fa84f37560ebcfb2a37  10.0.19041.0/um/x64/WinSpool.Lib
8d39892c74e61ed1113407046da20a9a  10.0.19041.0/um/x64/WinTrust.Lib
4c22aedbdd6fa9e95929cacd0e2f1e6c  10.0.19041.0/um/x64/WinInet.Lib
5cd6bc3268ce0e146aba250581a64842  10.0.19041.0/um/x64/winusb.lib
9a285b47df25856abb4238c7f2c44187  10.0.19041.0/um/x64/wlanapi.lib
39bb8be5bb2040f62f640695d9753ca1  10.0.19041.0/um/x64/wlanui.lib
29f2b0aa7a83d0472b9630fc2cd2a78c  10.0.19041.0/um/x64/Wldap32.Lib
0336a6dbb83c4f93917b1a80169a533a  10.0.19041.0/um/x64/Wldp.Lib
9452c0b3548757389119def2c5f98ab9  10.0.19041.0/um/x64/wmcodecdspuuid.lib
9895d8529bf01a16a9dbf19723c322e3  10.0.19041.0/um/x64/wmip.lib
b0b71c81c4d0b92951125ebd68747ea3  10.0.19041.0/um/x64/slcext.lib
76a981411670eb91b3eceb56b20c9543  10.0.19041.0/um/x64/wmiutils.lib
829a72cfc4a65433f77795e6fb76dc95  10.0.19041.0/um/x64/wmvcore.lib
d11dc3ce3df50e4aee0b08a158581934  10.0.19041.0/um/x64/ShLwApi.Lib
260ac38b95e6aa2297bc40dc3e2e7022  10.0.19041.0/um/x64/wnvapi.lib
cc7ef446cdc4e388c13eaf40dacea27d  10.0.19041.0/um/x64/ShFolder.Lib
3cfaf7aae6b7b99f2b82569854570d54  10.0.19041.0/um/x64/Mtx.Lib
ca7b9d01cdd58bd82771e6e17cad093b  10.0.19041.0/um/x64/MsWSock.Lib
cfb69163daeff5a91439df52f097b712  10.0.19041.0/um/x64/msvfw32.Lib
8242b379b41f8102fe692d6af3096256  10.0.19041.0/um/x64/msv1_0.lib
fb6f802d2b13f494f1b1bbe7066a7b70  10.0.19041.0/um/x64/MSTask.Lib
2ab99f860b2d8a64346253e244eda874  10.0.19041.0/um/x64/MSRating.Lib
f9022119ebd1fe55eb38b83f49ba4644  10.0.19041.0/um/x64/msports.lib
f202c32e3e0e4abd21760a2d239d9ab6  10.0.19041.0/um/x64/mspatcha.lib
9a50df0b8faae6137a6690ea8f0ed551  10.0.19041.0/um/x64/MSImg32.Lib
6c0c6ce7550f33142e1abf7e0edc4b35  10.0.19041.0/um/x86/WtsApi32.Lib
b91b60cffad0a317435b9c0561061e67  10.0.19041.0/um/x86/wsdapi.lib
51d59e6e2720f438c10e30b52bd6c2d0  10.0.19041.0/um/x86/wscapi.lib
0c7a1f82ab13876b510d2f25d9fb0e75  10.0.19041.0/um/x86/wsclient.lib
e1d00df2c89e960188c814e5e90982d6  10.0.19041.0/um/x86/wsbonline.lib
5788b8345e555adb3c2d52c8f9cd5ad2  10.0.19041.0/um/x86/wsbapp_uuid.Lib
2faf7380ce84bc3a8e3bb1c73051c3cc  10.0.19041.0/um/x86/WS2_32.Lib
0c03ec7d8f8be5b96a6df48c0e6e6d9b  10.0.19041.0/um/x86/Wow32.Lib
4249de96324f6287abdaad6be512bb6f  10.0.19041.0/um/x86/workspaceax.lib
f19e6a2d8dfd84e54fd13201a45b39a0  10.0.19041.0/um/x64/msdmo.lib
73960f90fe8e2028e87009fc82a02af0  10.0.19041.0/um/x64/MsCtfMonitor.lib
d9224a00865b337f18161a0c05186da8  10.0.19041.0/um/x64/MqRt.Lib
fda02f2197a0c88ef16e84a535d280c7  10.0.19041.0/um/x64/MrmSupport.lib
b4cfb26df1bf006f275eec84515b3ebb  10.0.19041.0/um/x64/jsrt.lib
5a37ead13cb4774fe35c60e340504630  10.0.19041.0/um/x64/iphlpapi.lib
35c20ba1452a6dbe06038e56a75b001f  10.0.19041.0/um/x64/iesetup.lib
7e69266fddd0aa3143d92a12925fe62f  10.0.19041.0/um/x64/IEPMAPI.Lib
d7f3a6d795f0f0536e4888145fb0065d  10.0.19041.0/um/x64/icuuc.lib
319e839d22178cf805104f7083fe2ae8  10.0.19041.0/um/x64/icuin.Lib
4000f24218c4bf0b2c1d1577706a3c29  10.0.19041.0/um/x64/icu.lib
8124f37f0c00a271a07057a0277d08a9  10.0.19041.0/um/x64/Icmui.Lib
d16c231becb4635e0b9eb8401bad7579  10.0.19041.0/um/x64/Icm32.Lib
206984b93d2a53bba411b73bcb20db59  10.0.19041.0/um/x64/iashlpr.lib
00fab02dceda8e7332bcc990dee628f3  10.0.19041.0/um/x64/httpapi.lib
d3db6f07e406e9ddf905149288c3131d  10.0.19041.0/um/x64/Htmlhelp.Lib
6f10e34864804b4ea47dcfd49e884604  10.0.19041.0/um/x64/hrtfapo.lib
76ca15a1f4ac6a7126302cff2446909a  10.0.19041.0/um/x64/HLink.Lib
6bec3ba784cda98f31dba9bf21988f7b  10.0.19041.0/um/x64/hid.lib
60d1b4456663b2e0d0c2ac9b9aa1d264  10.0.19041.0/um/x64/hhsetup.lib
a9cc2304de6f256f47a65bbf41ca2ed6  10.0.19041.0/um/x64/gpmuuid.lib
37943021413f178bf2b13b1ca39e425e  10.0.19041.0/um/x64/GPEdit.lib
c3d3e800ac67ac9084d43075a44863f7  10.0.19041.0/um/x64/fwpuclnt.lib
4f36fba80ca6c980e07a2d7f4262280c  10.0.19041.0/um/x64/FrameDyd.Lib
a5c6ed78bb8bcf2f124ae0eb7b9e9cfe  10.0.19041.0/um/x64/fontsub.lib
f84f57a9d0a12c0ec2b695881dac3fc6  10.0.19041.0/um/x64/fltLib.lib
3de2cda875b15f537159b02286272d0d  10.0.19041.0/um/x64/fileextd.lib
520048a8cf40eba50ff0155ffc918afc  10.0.19041.0/um/x64/FhSvcCtl.lib
dc28c77475ea7f37708e9b9df46fb156  10.0.19041.0/um/x64/feclient.lib
04ac8bcdd8ca59f3499704ba0b47d670  10.0.19041.0/um/x64/FaultRep.Lib
d163a0165ad748a6d62fe53ae504b508  10.0.19041.0/um/x64/evr.lib
f6c0cc775859e250efd5fb95f49412d4  10.0.19041.0/um/x64/esent.lib
0220f517b192a6d77d7abc9d40b24fdf  10.0.19041.0/um/x64/ElsCore.lib
e36fcc961ef5fec17e8af32cb34c4a55  10.0.19041.0/um/x64/els.lib
c9b9dcf8df8e19d513f96d827e200f1c  10.0.19041.0/um/x64/eappcfg.lib
6f2d25cc5d53f098e7ab1e5a8a941d02  10.0.19041.0/um/x64/dxva2.lib
5a1d8cc41cc7f4381bdd9aa724593fb4  10.0.19041.0/um/x64/dxtrans.lib
1e7e02fce0dfa094e33f833f6688c8b0  10.0.19041.0/um/x64/dxtmsft.lib
669fd4fe1e40ab284d556a008e908b0a  10.0.19041.0/um/x64/dxguid.lib
8034d95269199547e8d5fdafd61e3c7f  10.0.19041.0/um/x64/dxgi.lib
88075382a116ddc9d6af40f5b1bc3bef  10.0.19041.0/um/x64/dxcore.lib
c855b643c2f61835f315f5583c23ae10  10.0.19041.0/um/x64/dwrite.lib
10d547dd3161204ede99d1f1a4b2f56a  10.0.19041.0/um/x64/dxcompiler.lib
e88d3c022cd7134a84d950976cf5b221  10.0.19041.0/um/x64/dwmapi.lib
8576026cce48cd70abb1361b7229a203  10.0.19041.0/um/x64/DtcHelp.Lib
851fab030afea1301d6c249a5b78ea6e  10.0.19041.0/um/x64/DSUIExt.Lib
84e25b55e80f80dd97decb78ca5044c2  10.0.19041.0/um/x64/dssec.lib
abfcffebaf1cfd6893f58313223d9d0e  10.0.19041.0/um/x64/dsound.lib
c3466455f99da153588f0ef67ff4b993  10.0.19041.0/um/x64/drtprov.lib
3b627b564714369d77f0777af0ffbb09  10.0.19041.0/um/x64/dnsrslvr.lib
b425f0b83dbc64dfa9fabc32ad32903a  10.0.19041.0/um/x64/dpx.lib
384fe998d48e609fd33da592d002c0d6  10.0.19041.0/um/x64/dnsrpc.lib
54eb84cdffeb630dfa5416981a903e04  10.0.19041.0/um/x64/dnsperf.lib
6461ac3cfd827d0aef7f7d069e42c1ac  10.0.19041.0/um/x64/dnslib.lib
0328cf8ba20a00a8ff4e3e3f9090350e  10.0.19041.0/um/x64/dnscrcli.lib
b2bccd4c34b132399a035f123a1def69  10.0.19041.0/um/x64/DnsAPI.Lib
e75ea5dc11d4a453cd657ff665691ab6  10.0.19041.0/um/x64/dmprocessxmlfiltered.lib
cd48e9f42ceb88bda63f5ed6c92232d8  10.0.19041.0/um/x64/dmoguids.lib
f5329f5792276f60d99174c6613b3bd5  10.0.19041.0/um/x64/dloadhelper.lib
1c298f685b0dbaf88643afa18fa28d0b  10.0.19041.0/um/x64/directml.lib
f776f3d7ab88c03f7f6f46f7ac1013b1  10.0.19041.0/um/x64/dinput8.lib
60990486c29c24ecfc7ff6a7c0dc35c5  10.0.19041.0/um/x64/DiagnosticDataQuery.Lib
de470af38d15bb18e17f7e6542b52737  10.0.19041.0/um/x64/DbgModel.Lib
b001ad3741aa377b2e51a3bfc64e358e  10.0.19041.0/um/x64/DbgHelp.Lib
3e10680276a3c7685bd603d3da5d8a4f  10.0.19041.0/um/x64/DbgEng.Lib
cd921cfcdbeb412f0ef2b03596a4e094  10.0.19041.0/um/x64/davclnt.lib
74f175e4730950d08987b3d08d44d369  10.0.19041.0/um/x64/d3dcsxd.lib
525986d23219ea9f7c227eaf1d6b2955  10.0.19041.0/um/x64/d3dcsx.lib
db09aa53c1c01bafb39aad6cd526ed99  10.0.19041.0/um/x64/d3dcompiler.lib
c4983116ddf783a183869af8c8b1b609  10.0.19041.0/um/x64/d3d9.lib
7012b72c3c16c9248756fcfdd0fc6115  10.0.19041.0/um/x64/d3d12.lib
7a0810c1fc5eddc6ea62ff78138adf59  10.0.19041.0/um/x64/d3d11.lib
fd373f6dd66d52f604b4cdcf65fc2227  10.0.19041.0/um/x64/d3d10_1.lib
746bed8e386a2fd5c6f84e600cc54100  10.0.19041.0/um/x64/d2d1.lib
fb41a59373939b837f8eaf1d5926d912  10.0.19041.0/um/x64/d3d10.lib
0f334933983da70ca41a2b56a200fe18  10.0.19041.0/um/x64/cryptdll.lib
a77e03407f8a3ed7711919d56e51b11b  10.0.19041.0/um/x64/corrEngine.lib
07d1da654c243c1b1ab1e65be89a2872  10.0.19041.0/um/x64/ComSvcs.Lib
cadad6d73c55b16ffadbc1bcf03bdb16  10.0.19041.0/um/x64/computestorage.lib
d510558b6e25abbc3be7fd48354910d5  10.0.19041.0/um/x64/computenetwork.lib
7295304160ceb18436fb16febdfedfba  10.0.19041.0/um/x64/computecore.lib
50bcb46e0b20350653635cb84aa4bbb6  10.0.19041.0/um/x64/compstui.lib
cbf3309265c23347835502b155eabc27  10.0.19041.0/um/x64/ComDlg32.Lib
20a22657860d24fb180522f73fea9501  10.0.19041.0/um/x64/ComCtl32.Lib
804085a09345b43f2305097fd827e892  10.0.19041.0/um/x64/ClusApi.Lib
aee8d5ffcf1b7e30586f63e50bd1f5e8  10.0.19041.0/um/x64/clfsw32.lib
d9497be1a24b183a39d3c869a19716f0  10.0.19041.0/um/x64/clfsmgmt.lib
b13ae3d3832bf8fd7ccbee33e9b62652  10.0.19041.0/um/x64/cldapi.lib
a6a6faa7bce44b63118a4c5834225204  10.0.19041.0/um/x64/cimfs.lib
c3caac092f13211209286c2b3e20fc34  10.0.19041.0/um/x64/Chakrart.lib
5f3e41768ff9de75796177c20cc908ee  10.0.19041.0/um/x64/cfgmgr32.lib
dc0cb5371c171db29e4c78a689f42986  10.0.19041.0/um/x64/CertPolEng.Lib
fa201e85cd6a256f621efb8b4ee97308  10.0.19041.0/um/x64/CertIdl.Lib
49814fa62ede83dbf6a1132cdd364474  10.0.19041.0/um/x64/certcli.lib
5b69214aa4d5ef8d947f38f01bcda8df  10.0.19041.0/um/x64/certca.lib
ce7902210cba2968600a140a48986711  10.0.19041.0/um/x64/certadm.lib
77c383c075b833756c72b245591be5a5  10.0.19041.0/um/x64/Cabinet.Lib
ce8253a90458882d0f6d2bc5c7a9c354  10.0.19041.0/um/x64/wofutil.lib
6505496c8f4770c72dab5a1a141ffe5d  10.0.19041.0/um/x64/BufferOverflowU.lib
29988d0a0260862903ae5996dbd556c2  10.0.19041.0/um/x64/workspaceax.lib
6cd101b2ed1d8a13b898002e56ab8ce3  10.0.19041.0/um/x64/WS2_32.Lib
634bd5b65b547e3fd1914c3fd8385c0d  10.0.19041.0/um/x64/wsbapp_uuid.Lib
b39b1824195b2faf4a487a44840b41b2  10.0.19041.0/um/x64/wsbonline.lib
6930518e963276c6aa790b69892c8e07  10.0.19041.0/um/x64/wscapi.lib
591aa67eca91af78241969bc8bc0a276  10.0.19041.0/um/x64/bthprops.lib
bbef9a3f9f3cecdaa7b44078900fec60  10.0.19041.0/um/x64/BluetoothApis.lib
1aa592cfb899e010014b4696a6e6595d  10.0.19041.0/um/x64/wsclient.lib
695ffccec498deef7c58cf8552972866  10.0.19041.0/um/x64/Bits.Lib
8d10dca811de1263cd3c373db078dd62  10.0.19041.0/um/x64/BufferOverflow.lib
1bdaf736546dafbcf29be8f4a80ad3da  10.0.19041.0/um/x64/wsdapi.lib
d9a3754fa80ffc3659b98460d936468b  10.0.19041.0/um/x64/bcrypt.lib
aa1958cdc1b6b081c2c9a122cb9a3e7c  10.0.19041.0/um/x64/basesrv.lib
f0f9e59092c50fb20f010363ec927301  10.0.19041.0/um/x64/wsmsvc.lib
6b64c6f83904eb18510378bd88c98f97  10.0.19041.0/um/x64/avrt.lib
37a8a0e40a49f5ae57e13f7502d3bc4c  10.0.19041.0/um/x64/WSnmp32.Lib
5850e75a0957e754e009dfed0d29f46b  10.0.19041.0/um/x64/WSock32.Lib
0b20d4be69981ef7b41cd87b46b35d63  10.0.19041.0/um/x64/WtsApi32.Lib
27745382c5a474f7ec183673e9ee1e63  10.0.19041.0/um/x64/aux_ulib.lib
90e4fb4bfd890ca2f1ccdab264279cdb  10.0.19041.0/um/x64/wuguid.lib
04815f775001107223cabc7fbe622ef1  10.0.19041.0/um/x64/xapobase.lib
5f74dfabe3787188028c4ebc2aa82775  10.0.19041.0/um/x64/audiomediatypecrt.lib
8a3235dc7f5ab188ec0f632b45acec13  10.0.19041.0/um/x64/xapobase2_8.lib
efa0063896129c6fcc255e37e098d52a  10.0.19041.0/um/x64/audioeng.lib
61f19a1f2ef129f71b55108a48238074  10.0.19041.0/um/x64/xaswitch.lib
7b005b6eeeae02e4962915840ee12b1e  10.0.19041.0/um/x64/xaudio2.lib
53c8d8c49e14742fa2f9fa6d5e4777e7  10.0.19041.0/um/x64/audiobaseprocessingobject.lib
a6b6ecbe7f1f77ff7d1a21adb9c64d03  10.0.19041.0/um/x64/xaudio2_8.lib
7fd3453ccb8fbfa9cc3e3eeae3755431  10.0.19041.0/um/x64/xinput.lib
7279c820bc71255707f9f2a78f350c7b  10.0.19041.0/um/x64/amstrmid.lib
ca120b328d6a2a96a3781ca57664cb70  10.0.19041.0/um/x64/Xinput9_1_0.lib
732e9cf51b14e90c3ead226f870c5b84  10.0.19041.0/um/x64/xinputuap.lib
e2a3d80f8905a1f6306b4c6753201528  10.0.19041.0/um/x64/xmllite.lib
0567858247721f94a8d5ca7dda620e7c  10.0.19041.0/um/x64/xolehlp.lib
37cc61ccfb7eee463fb9fc4ce771d5ac  10.0.19041.0/um/x64/advpack.Lib
c9cfb4f779075188dc8ef8b578d40d68  10.0.19041.0/um/x64/xpsdocumenttargetprint.lib
ef404fcb43ea7d40a21e4687c976da12  10.0.19041.0/um/x64/ActiveDS.Lib
7996cace9ab53004fc914bfd692811f2  10.0.19041.0/um/x64/xpsprint.lib
0f7b334186eaa774fbc20cd5efa51f26  10.0.19041.0/um/x64/ADSIid.Lib
6cd204b2f977c072b27ff864f0c42dad  10.0.19041.0/um/x64/AdvAPI32.Lib
dbdf99a73ef406462d9807b04318a48f  10.0.19041.0/um/x86/winusb.lib
1b041b8fefc528bbb51c93269fcd5a3b  10.0.19041.0/um/x86/WinTrust.Lib
0220c82858d513e06cf6849f34d52d69  10.0.19041.0/um/x86/WinStrm.Lib
a9c762ede853f7941e7118dc149c2282  10.0.19041.0/um/x86/winsta.lib
2a3d44c47fa2f2d2e8e39f4e53ac41ef  10.0.19041.0/um/x86/winsqlite3.lib
bf139997bdf0d47822614a4e514036f6  10.0.19041.0/um/x86/WinSpool.Lib
7028c003b8bcd2f194552f19cb69d65d  10.0.19041.0/um/x86/winscard.lib
e19a47af1ef18668825c00235d4d048a  10.0.19041.0/um/x86/winsatapi.lib
aa55dc78d459bf57c0b0f2ba092c9c4c  10.0.19041.0/um/x86/winml.lib
158264f734cc5c0af376a7a016188d7d  10.0.19041.0/um/x86/WinInet.Lib
4d97464c01c389182bbe55abe7ce8a30  10.0.19041.0/um/x86/WinMM.Lib
d72479db57bcf8ed9b067cb14901b43f  10.0.19041.0/um/x86/winhttp.lib
4fe498a012f8e63f308938ff57cdbbfa  10.0.19041.0/um/x86/winfax.lib
2b29885aa66beef5eebe7ff10d43ead0  10.0.19041.0/um/x86/windowssideshowguids.lib
257c058882b499263620f1b201455d52  10.0.19041.0/um/x86/windowscoreheadless_apiset.Lib
eb20495f9b728676f83b6f7199bf1cbe  10.0.19041.0/um/x86/windowscoreheadless.Lib
0dd24c4ab43329a4e780d7c3c4841e08  10.0.19041.0/um/x86/WindowsApp_downlevel.lib
3bf971df54f12f3005f06f7fad985c64  10.0.19041.0/um/x86/WindowsApp.lib
d4c14f18fcb327ed997c0c0a19717d25  10.0.19041.0/um/x86/windowscodecs.lib
643983c8851838743370f9562a7caafc  10.0.19041.0/um/x86/windows.ui.lib
0a513bea456a373662d483f947a40acb  10.0.19041.0/um/x86/windows.media.mediacontrol.lib
1d40c25eaf1447113fa8bc7fb50e268d  10.0.19041.0/um/x86/windows.data.pdf.lib
79234bc8e162fe4c0a575bc9ae21441b  10.0.19041.0/um/x86/windows.networking.lib
de80c003b65b14dfa80a086dfe24ef5a  10.0.19041.0/um/x86/windows.ai.machinelearning.lib
fb34b2c36feb163d1979e9353363b740  10.0.19041.0/um/x86/wiautil.lib
da3859e20d9d7b31b36245da9a85bf08  10.0.19041.0/um/x86/WinBio.lib
efbfada8e9b1e47805717c42dd4a4175  10.0.19041.0/um/x86/wiaservc.lib
929299b9218a46d7c21802ffe753b85e  10.0.19041.0/um/x86/WiaGuid.Lib
7dfae77b6b4f9a6d0ffc36a2330c04ad  10.0.19041.0/um/x86/wevtapi.lib
effa7b1e4ce3ffd49d9dde994653b2f7  10.0.19041.0/um/x86/Wer.lib
93f79a8caf5a106f0a003a88fb58e162  10.0.19041.0/um/x86/wecapi.lib
86e7c06d19e6a2961b4109049df35996  10.0.19041.0/um/x86/websocket.lib
3eec01aec57a04c2d9fde63ee11acd03  10.0.19041.0/um/x86/WebServices.lib
8d7cd4b5539d748b099b3ac3d5ac75aa  10.0.19041.0/um/x86/webauthn.lib
af9257cdda0095a45ca2a57247024760  10.0.19041.0/um/x86/wdsmc.lib
e5409840fbb03e3868ba38f873317d99  10.0.19041.0/um/x86/wdspxe.lib
470cfeb1676390700fa0e3279179854f  10.0.19041.0/um/x86/wdstptc.lib
92dfa70b2bd694321f8e2bf6fbd08d61  10.0.19041.0/um/x86/wdsClientAPI.LIB
bc2eddd7b1389cfd9827f3f1fc8daf41  10.0.19041.0/um/x86/wdsbp.lib
35520b3bb5adfdf6f33964657852989f  10.0.19041.0/um/x86/wcmguid.lib
677f630d0afc892e493d75cfe7e0bdb7  10.0.19041.0/um/x86/wcmapi.lib
834f07f92aa522f1837fcb0581251c8a  10.0.19041.0/um/x86/wbemuuid.lib
ea970512c3756087a64581d9bc29da65  10.0.19041.0/um/x86/vstorinterface.lib
949d4d13dca325e06f1312c8b4dec2ef  10.0.19041.0/um/x86/vss_uuid.lib
9eb8a10994505ee135c3f4f43b987028  10.0.19041.0/um/x86/vssapi.lib
65d174076cb5a10f809336ca807a5962  10.0.19041.0/um/x86/vscmgr.lib
cfe8893208b1fa3308816dcd528858f9  10.0.19041.0/um/x86/Vfw32.Lib
067f52bf8ce02cd14ce185120a11c257  10.0.19041.0/um/x86/Virtdisk.Lib
ef87cc736bcf4df658bfbeb4107c80de  10.0.19041.0/um/x86/Version.Lib
80422c102bdcb32e0107f2f4aa3d0246  10.0.19041.0/um/x86/vds_uuid.lib
65971139d9a6cdac13b57a93af3d3713  10.0.19041.0/um/x86/VdmDbg.Lib
bf577ead64cdc1c5850be89ed782be99  10.0.19041.0/um/x86/vccomsup.lib
f6f57f538a4e85b46d30ea8d6225e4de  10.0.19041.0/um/x86/Uxtheme.lib
1c4e48441da3ee516fead89da22b1f04  10.0.19041.0/um/x86/Uuid.Lib
a695499b2bdb2c57a03725df13c7dfc4  10.0.19041.0/um/x86/USP10.Lib
2cae3273926d4c46e906114b988670b0  10.0.19041.0/um/x86/User32.Lib
a4133c198b2ba1095cb54081d1266780  10.0.19041.0/um/x86/UserEnv.Lib
fddf09c7c440570a1dff0a2d1e7f9dd2  10.0.19041.0/um/x86/Urlmon.Lib
f0413a6b8d7d8490c2c862d74f8024cf  10.0.19041.0/um/x86/unicows.lib
2585e6cc978eb7840c7e6cbb19f1e61a  10.0.19041.0/um/x86/umpdddi.lib
b5ac881f8ea264e7817d74e3b5b9bdba  10.0.19041.0/um/x86/UIAutomationCore.lib
c3f570da2324174d19738267f00d1aec  10.0.19041.0/um/x86/ualapi.lib
0bd6a7396349d72e1b573897c0c70417  10.0.19041.0/um/x86/txfw32.lib
8e106b4e2bcc74b9844ca217a58f3abe  10.0.19041.0/um/x86/twinapi.lib
d9ed7dfa66f56a353f0f85d09dc5b657  10.0.19041.0/um/x86/twain_32.lib
3fd8a8567eb1e4e29a568d59fcab1234  10.0.19041.0/um/x86/tspubplugincom.lib
dcf1e4a439f6ba6f8081efee9b351963  10.0.19041.0/um/x86/tsec.lib
12f232c2f2fe787364ffa62a5941ed57  10.0.19041.0/um/x86/TranscodeImageUID.lib
c3a82ee0c8f4aa25890b8056ac7f0e96  10.0.19041.0/um/x86/Traffic.Lib
dc4f430e36bc1127bdd539f32ed4d31e  10.0.19041.0/ucrt/x64/ucrtd.lib
26f23377a966d02d7b8c113c358622d4  10.0.19041.0/um/x86/tokenbinding.lib
5c386f11d773c7aa230dfa4571833b8a  10.0.19041.0/ucrt/x64/ucrt.lib
bf23b873fa88718c93811db60855add1  10.0.19041.0/um/x86/Thunk32.Lib
4755bdf8e7840f39870d2f3f7e9770a1  10.0.19041.0/um/x86/tdh.lib
063c74ad96aca314d9d2269bfc57f177  10.0.19041.0/ucrt/x64/libucrtd.lib
8a52a25c9ac4c0e59b15b034b056dccf  10.0.19041.0/um/x86/tbs.lib
3598f6756a81a3b26303ea941a98de6c  10.0.19041.0/um/x86/taskschd.lib
15a594fee59db2dfb83ad1d61f5519cf  10.0.19041.0/ucrt/x64/libucrt.lib
cd65d80b71639a74242bd9b0a6a04856  10.0.19041.0/um/x86/tapi32l.lib
c4d1583ff42125a7978d2654f56ac5d8  10.0.19041.0/um/x86/Tapi32.Lib
fade5bd5bd2fc4247d5ed1890f653316  10.0.19041.0/um/x86/t2embed.lib
7c302cd09570e4e45d101ffed2af5466  10.0.19041.0/um/x86/synchronization.lib
d4e3902e792aebaa3062af3aeaab82b3  10.0.19041.0/um/x86/Svcguid.Lib
9aea227b59d01edb69354a9b19d72f8c  10.0.19041.0/um/x86/swdevice.lib
ac6ec20a50cb8eee7f5a0089ea4a45a1  10.0.19041.0/um/x86/structuredquery.lib
b30cf112be234b03f7cc4a816f1cc93d  10.0.19041.0/um/x86/strsafe.lib
69b7fab7dda9d7f7dd990f9101e1072c  10.0.19041.0/um/x86/strmbase.lib
867174f70729c7387984db19e7d40b3a  10.0.19041.0/um/x86/strmiids.lib
312f269e0128c1d91a9347d8bc84e126  10.0.19041.0/um/x86/Sti.Lib
c361dfd279b75d53661add7ecaa5491a  10.0.19041.0/um/x86/ssdpapi.lib
4bf8d64666e4641b845c474e374cbe4f  10.0.19041.0/um/x86/srpapi.lib
a017a38c1d9456ed83daa8324942db84  10.0.19041.0/um/x86/SrClient.lib
8d6b8899d557d4051c152637b260c80f  10.0.19041.0/um/x86/SpOrder.Lib
b4d31006910f39f2941a666993f93f1f  10.0.19041.0/um/x86/spoolss.lib
6d4aeefc7b3b678c8249a1ec82558ca1  10.0.19041.0/um/x86/SnmpAPI.Lib
7e67058e7bf46bdbef338040f4360218  10.0.19041.0/um/x86/slcext.lib
fdbde0008f54f0c678b23c8ca5198a92  10.0.19041.0/um/x86/slwga.lib
6b966163acaa25745fd51f77d8736c20  10.0.19041.0/um/x86/slc.lib
7b81994e07eef8357e1bed02b936c875  10.0.19041.0/um/x86/ShFolder.Lib
4ecc15d6e76bf00f37197429f5f5869a  10.0.19041.0/um/x86/ShLwApi.Lib
68195ab83596fa0a829c11b1a0050254  10.0.19041.0/um/x86/shdocvw.lib
c144cf279c3988da5dc53a2423b9a030  10.0.19041.0/um/x86/shell32.lib
fb7d9eee6f4d1f4e3655ea89660310c2  10.0.19041.0/um/x86/shcore.lib
38bf1fc878de00c32f01238c7f45fece  10.0.19041.0/um/x86/Sfc.Lib
343921d01b54c9b5638d99aa687cd595  10.0.19041.0/um/x86/SetupAPI.Lib
7fbb3dfa3e017e3bddd00b0b02795bd6  10.0.19041.0/um/x86/SensorsUtils.lib
c1614f21dea735e9e7ea59ae76cf81f3  10.0.19041.0/um/x86/sensorsapi.lib
a2ae53ee208c9cbb548ab7ec9d20dfa4  10.0.19041.0/um/x86/SensAPI.Lib
d412d22e5b8936375e456ab30be5c9f8  10.0.19041.0/um/x86/sens.lib
be257fb8e0fb4e24f5f0fd292cf1bb6f  10.0.19041.0/um/x86/security.lib
4aba48418dd9f38cb96601f80a63f0e5  10.0.19041.0/um/x86/Secur32.Lib
7eb02731bab8c44695dc5115955429b7  10.0.19041.0/um/x86/SearchSDK.lib
ff28655690d02a62516aef062a85645b  10.0.19041.0/um/x86/ScrnSavW.Lib
4f89308b46115b5464c602eb1e63b00a  10.0.19041.0/um/x86/ScrnSave.Lib
53047326494651dd541db5b5c4849ad2  10.0.19041.0/um/x86/schannel.lib
5c1d6bd2afe3a1ce24b84666e75b1415  10.0.19041.0/um/x86/scesrv.lib
16b8c83035398bec9309c97e9ab1cb44  10.0.19041.0/um/x86/scecli.lib
b0736e3646d153564ac667e904aa4801  10.0.19041.0/um/x86/SCardDlg.Lib
74de1709a12ef03fd1695a6e56d09227  10.0.19041.0/um/x86/sbtsv.lib
bfb780d8813a4a856881d99c35f951a2  10.0.19041.0/um/x86/sas.lib
da10208fd605c87cc29b10d3c869c682  10.0.19041.0/um/x86/SAPI.Lib
9cc6d63193829711e55ee2b9822882a8  10.0.19041.0/um/x86/samsrv.lib
faa378767318f3218c33e430849489c8  10.0.19041.0/um/x86/samlib.lib
f376658aaa4559833f5a5ac7840153f4  10.0.19041.0/um/x86/runtimeobject.lib
db67837237f945b216ac170d3d0ae97c  10.0.19041.0/um/x86/RTWorkQ.lib
70c326216155c17ca8df1cc8c86eee0f  10.0.19041.0/um/x86/rtutils.lib
b3f64d0230789ab6b2ccfa0fc9965168  10.0.19041.0/um/x86/Rtm.Lib
e8407a599f37ffe1c4f53e1da7395de6  10.0.19041.0/um/x86/rstrtmgr.lib
931eebe8a155ec0b850f19a794184982  10.0.19041.0/um/x86/rpcutil.lib
1cb0cec311071e9b99b80090e344b669  10.0.19041.0/um/x86/RpcRT4.Lib
b219f09219ea8688539b96079d470f14  10.0.19041.0/um/x86/rpcproxy.lib
b23f4fa930cae72434832231ad56d45d  10.0.19041.0/um/x86/Rpcns4.Lib
2af69cb2f1296f364656a0ae0b83bbca  10.0.19041.0/um/x86/rpcexts.lib
e23d39e0efb4463b64ecc19935a95279  10.0.19041.0/um/x86/resutils.lib
0b8d08c31a94c5fc30d6839ac5ea35fb  10.0.19041.0/um/x86/rometadata.lib
d25b08fbd297bc413a5ec072bad8557c  10.0.19041.0/um/x86/rasuser.lib
38643984e91d95bb4d3136b35b5c1953  10.0.19041.0/um/x86/RASAPI32.Lib
6193b57ce1f163a3cb91621237e82110  10.0.19041.0/um/x86/RASDlg.Lib
ffcffd981388055a5de9ad533a63100c  10.0.19041.0/um/x86/qwave.lib
15c8416a43436c0ad1f16c3eccc7e23d  10.0.19041.0/um/x86/query.lib
ce0dd4ad544e829e1186e928f5eaf709  10.0.19041.0/um/x86/quartz.lib
eefc0e6d002d3b491bf666f1fe4b5b4e  10.0.19041.0/um/x86/Psapi.Lib
0e873f883a219a37818ed58e88623941  10.0.19041.0/um/x86/propsys.lib
93e3c4a5e50d72b4c1cdbf4baad5796c  10.0.19041.0/um/x86/ProjectedFSLib.lib
1d8aed7bc3e878dc8f41a09725579b7b  10.0.19041.0/um/x86/powrprof.lib
01d51615e9d346320cb4543053b76571  10.0.19041.0/um/x86/prntvpt.lib
e9ef8c7533798e83fa50be8041773152  10.0.19041.0/um/x86/PortableDeviceGuids.lib
12ecf9600ec44da174e78a21e8b6478e  10.0.19041.0/um/x86/PhotoAcquireUID.lib
249afba013447dede9959312bd17445c  10.0.19041.0/um/x86/PeerDist.lib
51c69802211098c0be8a44bb638d2051  10.0.19041.0/um/x86/Pdh.Lib
5a6b968fdadee19180d8a21151ab9087  10.0.19041.0/um/x86/patchwiz.lib
a82c03ff1578e129ca0af7df524274e9  10.0.19041.0/um/x86/pathcch.lib
0b0f85919ff70536d62df638eb5ee861  10.0.19041.0/um/x86/p2pgraph.lib
9a01f731b42c6a739cacd1441fee339a  10.0.19041.0/um/x86/p2p.lib
6687b6f5a03a64e4c89a752862501a1b  10.0.19041.0/um/x86/osptk.lib
3bff83ba40896964648cea89442061ac  10.0.19041.0/um/x86/OpenGL32.Lib
af80b720de53a884c11c870e947b4d94  10.0.19041.0/um/x86/OneCore_apiset.Lib
db960ce55b2210983b700d5d218b014a  10.0.19041.0/um/x86/OneCore_downlevel.Lib
2ce6de17732da5d955f29896467ecd49  10.0.19041.0/um/x86/OneCoreUAP_downlevel.Lib
dc1542c87dcf6b890ed076255d9b1b3f  10.0.19041.0/um/x86/OneCoreUAP_apiset.Lib
2335aef429ee36047f85421d6ec685db  10.0.19041.0/um/x86/OneCoreUAP.Lib
3bef79e2d382f21ebb275c36b7964efe  10.0.19041.0/um/x86/OneCore.Lib
6331e0cb16409a3de86c6ba4e83e5482  10.0.19041.0/um/x86/ondemandconnroutehelper.lib
7fc6edc3ac2264c560647a257a0b15c7  10.0.19041.0/um/x86/OlePro32.Lib
7224f5f24c6db5f6079c70a4fff191ad  10.0.19041.0/um/x86/olesvr32.lib
0460313136010caba826299488f6aa4c  10.0.19041.0/um/x86/OleDlg.Lib
74dcdcf161c7a66759d657ed0049b4dd  10.0.19041.0/um/x86/olecli32.lib
b474b726336b503c5309ba5458ae1988  10.0.19041.0/um/x86/oledb.lib
e731a559b4127741d8c1d5946db3b48d  10.0.19041.0/um/x86/OleAut32.Lib
641050bcca987470ae5960c65085fd98  10.0.19041.0/um/x86/OleAcc.Lib
9a4e29e1dac13dca023cdeb819c34851  10.0.19041.0/um/x86/Ole32.Lib
7beb7dd65c5dd3dccfd675f27427e9a8  10.0.19041.0/um/x86/OemLicense.lib
41be127eb27dd4d2a937fa9905815186  10.0.19041.0/um/x86/odbccp32.lib
d9fd2fa2ca7230c66488f245530407f0  10.0.19041.0/um/x86/odbcbcp.lib
40d7a670be4482082ad965fc7754a1b5  10.0.19041.0/um/x86/odbc32.lib
2cfe17ab1012023b6db6b723325f7247  10.0.19041.0/um/x86/ntvdm.lib
66cfa5b0c90124d027679680bd59b13d  10.0.19041.0/um/x86/objsel.lib
5cae17775f51852709bff315caabad3a  10.0.19041.0/um/x86/ntstc_msvcrt.lib
b21a3e03de067d78690056dff7a06a64  10.0.19041.0/um/x86/ntstc_libcmt.lib
15c8416a43436c0ad1f16c3eccc7e23d  10.0.19041.0/um/x86/NtQuery.Lib
b7415252221760ec84aec5163ea32259  10.0.19041.0/um/x86/ntmarta.lib
7bcadc97fff79ad6b552a3d4d6d01ba6  10.0.19041.0/um/x86/ntlanman.lib
79e5f03aac211722c83a698040174492  10.0.19041.0/um/x86/ntfrsapi.lib
f9a3b0d525194443597fd137bc100887  10.0.19041.0/um/x86/ntdsetup.lib
a51f69bc9ca5dae13b734d7ea8063a34  10.0.19041.0/um/x86/ntdsatq.lib
3f5703b3c59b4a7b8cdff9c19d753460  10.0.19041.0/um/x86/ntdsa.lib
ad06dad8359ae54c72e94761c96cdcc5  10.0.19041.0/um/x86/NtDsAPI.Lib
f52fc9a3c3e6079f56607639d49f09b5  10.0.19041.0/um/x86/ntdll.lib
ccbc682dc17012934d694e03facb25b7  10.0.19041.0/um/x86/nt.lib
4cb489e2a2c55c8cfb5672af5ca8cb8b  10.0.19041.0/um/x86/normaliz.lib
391d90d7559955ea212e4c8441655332  10.0.19041.0/um/x86/ninput.lib
f68116e793558e833bc1d70a19108b64  10.0.19041.0/um/x86/newdev.lib
29e1cc80cbecf61b9d263d2f0ced0e35  10.0.19041.0/um/x86/NetSh.Lib
e65eaa675d5389958088fd2baf2c7c9c  10.0.19041.0/um/x86/netlib.lib
a7722939648b7c3f1545f0022327d75c  10.0.19041.0/um/x86/NetAPI32.Lib
1645ba355cdeaf0af594125e1dbac8a0  10.0.19041.0/um/x86/ndproxystub.lib
ca6a3ea2338e0e2ae09f075d6362a220  10.0.19041.0/um/x86/ndfapi.lib
98b667082eca159175a4c2857324ffe7  10.0.19041.0/um/x86/nddeapi.lib
6d681a76e73b4dad73ad10d5e2bf2cf7  10.0.19041.0/um/x86/ncrypt.lib
2855c9966bc46311ad519879b66d9452  10.0.19041.0/um/x86/muiload.lib
aec09a062b4669573b6737b178304d23  10.0.19041.0/um/x86/mtxdm.lib
dae97f091b0a61284d4ed0f163e2d141  10.0.19041.0/um/x86/Mtx.Lib
9d52a21fec589c5dc583000f26be5c77  10.0.19041.0/um/x86/msxml6.lib
7143c887ddedd2936fab1334c12a0a72  10.0.19041.0/um/x86/MsXml2.Lib
f82d59943b8cfbb6c1f0a62c8ee6fedc  10.0.19041.0/um/x86/MsWSock.Lib
277ced613951457c84a185a29821e54f  10.0.19041.0/um/x86/msvfw32.Lib
28b907df48ff24362035daf5b5aa03d2  10.0.19041.0/um/x86/msv1_0.lib
57d3cb70077921e8aed800aca0cf1922  10.0.19041.0/um/x86/MSTask.Lib
e8ca302ee1e94ad64784ae9ccc0daaa7  10.0.19041.0/um/x86/MSRating.Lib
c9402a214bf25c5a48afe343f8eef36a  10.0.19041.0/um/x86/msports.lib
995dec0cd5a1a4bb04e4728bb451ce92  10.0.19041.0/um/x86/mspbase.lib
c4eb302b46c77f9cd41d7bd6a57a0e7e  10.0.19041.0/um/x86/mspatchc.lib
d9b75cdb8be42b0ab457daaf05953816  10.0.19041.0/um/x86/mspatcha.lib
b7bdcb0f14d92670d2bf27f7f59c2f53  10.0.19041.0/um/x86/MSImg32.Lib
def29c79fd43ca1160ddbd0492c4ea35  10.0.19041.0/um/x86/Msi.Lib
49f85d6c5fd492909e7894c12dadd124  10.0.19041.0/um/x86/msdrm.lib
0779ce56b2607a43c3e55e711a747681  10.0.19041.0/um/x86/msdmo.lib
efac4f79db8fdb7204387647ecba1cf6  10.0.19041.0/um/x86/msdelta.lib
7fdc92182ee5c85175d57fc2193fd554  10.0.19041.0/um/x86/msdasc.lib
8e3794b6d83365e7bab55036967ddc0c  10.0.19041.0/um/x86/MsCtfMonitor.lib
8d8919636342608ea5b918630a8be1b3  10.0.19041.0/um/x86/Mscms.Lib
3e8a2cadbaa04ee7f4c864a0a6366197  10.0.19041.0/um/x86/MSAcm32.Lib
c5570fda9fa89c51dfd5ab959f7a3851  10.0.19041.0/um/x86/MSAJApi.lib
afad34645ff7e3c240d051d60e1b2709  10.0.19041.0/um/x86/msaatext.lib
2dad17137e8e2961f8897da046f31e6b  10.0.19041.0/um/x86/MrmSupport.lib
6788b2c25d89c7accfc3b30e3abf75fb  10.0.19041.0/um/x86/MqRt.Lib
4a3882d866941b17c17817204a2c781c  10.0.19041.0/um/x86/MqOA.Lib
3afcafc975b972d0bcbd7a3a8e96b59e  10.0.19041.0/um/x86/mprsnap.lib
3a60035ecd92eec133cb1a802b18f75f  10.0.19041.0/um/x86/Mprapi.Lib
724dd5ee12cb814bd86cea155a96f4b9  10.0.19041.0/um/x86/Mpr.Lib
120bc02e3b70d1929cb3c3d22e910f75  10.0.19041.0/um/x86/mmdevapi.lib
a8a2d73492fed81b46b401021e61eb09  10.0.19041.0/um/x86/MMC.Lib
e7521a634f466ebe7dcc481d9e29be7a  10.0.19041.0/um/x86/mincore_downlevel.lib
37e130c1a63bb6d9b22c3a9bb639e9c4  10.0.19041.0/um/x86/mincore.lib
d46aa6732d89dc23028a129cf481497b  10.0.19041.0/um/x86/mi.lib
872024777c28a543fd90be313ceb136e  10.0.19041.0/um/x86/MgmtAPI.Lib
0ba5f643ad8fec68fdfcbf9052640690  10.0.19041.0/um/x86/mfuuid.lib
473c4280aa022daf5b56b6538813f77e  10.0.19041.0/um/x86/Mfsrcsnk.lib
819ea77188d332fa5640f58cbf0c6340  10.0.19041.0/um/x86/mfsensorgroup.lib
392dba4aab5dd8092ec211b88c984df0  10.0.19041.0/um/x86/mfreadwrite.lib
f37eb73a0fa41c4fb2859c4f4e384a82  10.0.19041.0/um/x86/mfplay.lib
fbeefecc28c8298e3c172d87b0c2670c  10.0.19041.0/um/x86/Mfplat.lib
b3516b7ef4d979cc0a7367fec9285431  10.0.19041.0/um/x86/Mfcore.lib
0595461b51d26620cbb7269e0782e7a1  10.0.19041.0/um/x86/Mf.lib
295f6a389d58f99587e9f9177a77ae5e  10.0.19041.0/um/x86/MDMRegistration.lib
2770c21d403a7d86d9c5d7b3effebf5d  10.0.19041.0/um/x86/mdmlocalmanagement.lib
187b6898ce61b6279ec5434fe2713f59  10.0.19041.0/um/x86/mciole32.lib
a11d02baeb80a36cf1fae8543e8dbff8  10.0.19041.0/um/x86/mbnapi_uuid.lib
2ea08309162e7b8db3045c2884ccb9de  10.0.19041.0/um/x86/MAPI32.Lib
b258eb1b2e189bdb315418ec69d16362  10.0.19041.0/um/x86/magnification.lib
b821555c3598aed01a44035637b829a6  10.0.19041.0/um/x86/Lz32.Lib
fc3c8eab762e9e904112ec7cc9a9ec31  10.0.19041.0/um/x86/locationapi.lib
df1d5127dc67b728a920f274219d9eb5  10.0.19041.0/um/x86/LoadPerf.Lib
b24ff48f172dc27028897666c32efadb  10.0.19041.0/um/x86/ktmw32.lib
9b9362b542c157b109d76f2f1d66a39a  10.0.19041.0/um/x86/ksuser.lib
f448cdb1b6634a489948b57618ba89e9  10.0.19041.0/um/x86/KSProxy.Lib
b9d61569db768e12310d4ba529e7194d  10.0.19041.0/um/x86/keycredmgr.lib
2ea18a7196f80328a7cc2b1dd454fbc8  10.0.19041.0/um/x86/kernel32legacylib.lib
6e055d07c76de507e2571104124f9554  10.0.19041.0/um/x86/kernel32.Lib
5eff9100d5104734c322a8ebdcee90fc  10.0.19041.0/um/x86/kerbcli.lib
fd00b65c990cf441b13ea4f7fe7450db  10.0.19041.0/um/x86/jetoledb.lib
c760b8aa165334814a90279d3cf6dda9  10.0.19041.0/um/x86/jsrt.lib
5d76987c60645c01a64a76adc0e72257  10.0.19041.0/um/x86/iscsidsc.lib
903b6738a76e5c3b80b64a6fb997e88e  10.0.19041.0/um/x86/Iprop.Lib
68a1216f485522f4dcc61bab849d0f44  10.0.19041.0/um/x86/IsolatedWindowsEnvironmentUtils.lib
2740ec84b86c4b6784e24a22fc89ae46  10.0.19041.0/um/x86/iphlpapi.lib
5c20969d7227edd885821d11fbdc1f59  10.0.19041.0/um/x86/int64.lib
9c185c186edfb385c5352d73eba0f8f3  10.0.19041.0/um/x86/inseng.lib
f9b122f3f22726df207a63f770acc383  10.0.19041.0/um/x86/inkobjcore.lib
64d7deca2fab862e46302a37e6317f13  10.0.19041.0/um/x86/Imm32.Lib
9f2623aac68cfd8210057c31d4bceb43  10.0.19041.0/um/x86/imgutil.Lib
d66360b034534bca06fc4159472ae2fa  10.0.19041.0/um/x86/infocardapi.Lib
d5cc841395da9831755c979446750d29  10.0.19041.0/um/x86/ImageHlp.Lib
546c3064a7c0881619e116aa86894392  10.0.19041.0/um/x86/iesetup.lib
ffd5c31433b0cb24369693742fc61717  10.0.19041.0/um/x86/IEPMAPI.Lib
c4a346f0b1bf6441abd713cff7102c2a  10.0.19041.0/um/x86/icuuc.lib
69a78521b75bfb4a8ee7a07b01280da3  10.0.19041.0/um/x86/icuin.Lib
9851f55c18bc1de5113b67625a31425f  10.0.19041.0/um/x86/icu.lib
a8328eeda912ca3c72f0a6ee952f77b5  10.0.19041.0/um/x86/Icmui.Lib
2ffb7a4663529ff1083955b53f07dcb1  10.0.19041.0/um/x86/Icm32.Lib
9a45d28d2abd9f8cb6e124e87037261a  10.0.19041.0/um/x86/iashlpr.lib
06df4fe81dc10c54e1034eb87b4bd3f4  10.0.19041.0/um/x86/httpapi.lib
5d8aee50ef7f01d55cbb1673bf82d35c  10.0.19041.0/um/x86/Htmlhelp.Lib
3bd4871a3095aef460b7c7a678a9ce63  10.0.19041.0/um/x86/hrtfapo.lib
2cd49afef201205506afdcee668ec55b  10.0.19041.0/um/x86/HLink.Lib
2b43beef5428cbb46b946a09cb835b1f  10.0.19041.0/um/x86/hid.lib
288c0d9ca41a7e7f99d7521750d5305d  10.0.19041.0/um/x86/hhsetup.lib
aca13216463251cfa95285191bf8df91  10.0.19041.0/um/x86/hbaapi.lib
3ef2ca94e55135804b3466338f065390  10.0.19041.0/um/x86/gpmuuid.lib
d900df8f2eab2bcae16168fc696007b0  10.0.19041.0/um/x86/GPEdit.lib
b52d231e779e808311845c9f319e7930  10.0.19041.0/um/x86/GlU32.Lib
8d85632aa0e85952a9fc3e865bc6b7a2  10.0.19041.0/um/x86/gdiplus.lib
0ea734a4dbd2d4c116ffaf3c54e1cb43  10.0.19041.0/um/x86/glmf32.lib
fbc438c08774ae99712a46db6455f551  10.0.19041.0/um/x86/Gdi32.Lib
afa5a12483d21855fed6312da36af9aa  10.0.19041.0/um/x86/fxsutility.lib
f6247211948893c54e243bf401f09aca  10.0.19041.0/um/x86/fwpuclnt.lib
0b550e1a1abab7f33e531e9ef24f627c  10.0.19041.0/um/x86/FrameDyn.Lib
6f371b34ce601b1d7c4a888e9eac54bc  10.0.19041.0/um/x86/FrameDyd.Lib
8017ca0d7cc0575615a3642f4bb83513  10.0.19041.0/um/x86/fontsub.lib
d4c56d6377872d0feb32a0b463516154  10.0.19041.0/um/x86/fltLib.lib
1629554d557bc754718a7968066b56bb  10.0.19041.0/um/x86/fileextd.lib
002f323ded97b2c9cffbb492c51e91d0  10.0.19041.0/um/x86/FhSvcCtl.lib
a34022ae55253ab6b611aa290c7eb6fe  10.0.19041.0/um/x86/feclient.lib
8d60154d717844aee41c5807adb85fd7  10.0.19041.0/um/x86/FaultRep.Lib
b7a652532278688bf7971881b516106c  10.0.19041.0/um/x86/evr.lib
4b23d95ff25d91a8c3d56f1f572d9a8d  10.0.19041.0/um/x86/ElsCore.lib
a7ed3fcaf59febd5bd444ced744401c2  10.0.19041.0/um/x86/esent.lib
484f1884b72f67b2e50d572161ebb72c  10.0.19041.0/um/x86/els.lib
ec2f55b1bab0add5c72c21347036a593  10.0.19041.0/um/x86/elfapi.lib
5627a56e027a61a42e2de6a5eb21015d  10.0.19041.0/um/x86/ehstorguids.lib
91cd15642461234badf9bbd4580a5117  10.0.19041.0/um/x86/efswrt.lib
cde60c43b486a1ba8a0a51cbc09437f0  10.0.19041.0/um/x86/easregprov.lib
b8ca0e836b2295361a288c38c0d63ea7  10.0.19041.0/um/x86/eappprxy.lib
c0e8e75426a7bd6eff453f6cbfcbd360  10.0.19041.0/um/x86/dxva2.lib
791ce5389bde82340364d208ee277adc  10.0.19041.0/um/x86/eappcfg.lib
7d43fe6f3c98c4f5fb8770780fd455a5  10.0.19041.0/um/x86/dxtrans.lib
c45f67fa8d6bb53586489b5d98d7d6bd  10.0.19041.0/um/x86/dxtmsft.lib
b02ac71ac16f8dd6ef4bc3557a5a9b26  10.0.19041.0/um/x86/dxguid.lib
e918a470572dc002c3c6e1903cf3b0e9  10.0.19041.0/um/x86/dxgi.lib
7ad6918a90d255494573a4dee82b5d3a  10.0.19041.0/um/x86/dxcore.lib
e129f67e3efb852dac8d87e680b9bbe1  10.0.19041.0/um/x86/dxcompiler.lib
10b7c74492f117de05669416d61b4582  10.0.19041.0/um/x86/dwmapi.lib
fc901f2d12a8740bce9a287a9cbbdc5a  10.0.19041.0/um/x86/dwrite.lib
4aae8d2abd4542ddea555faece5bec5f  10.0.19041.0/um/x86/DtcHelp.Lib
421df98e74e733fdc88737700d504204  10.0.19041.0/um/x86/DSUIExt.Lib
8c47d6378f6d9a7833c6a08d0534f4da  10.0.19041.0/um/x86/dssec.lib
f1131790f789bc7453b9ab73c2c562c4  10.0.19041.0/um/x86/dststlog.lib
df8df0a24c973063e2a5d0577dee60bd  10.0.19041.0/um/x86/DSProp.Lib
501fa235ae44dcfa925a41676a2bc4b5  10.0.19041.0/um/x86/drttransport.lib
bfe247a601a76607bb87b5060cbd7648  10.0.19041.0/um/x86/dsound.lib
0e294e0454fe83c5d87de9078223839c  10.0.19041.0/um/x86/drt.lib
48fa649a75061dde57e8c0a057871b39  10.0.19041.0/um/x86/drtprov.lib
07003cc62e7145cab32e6bdca794b8ab  10.0.19041.0/um/x86/dpx.lib
d6bbc29c0423c4d16d1296e9ee24c2b1  10.0.19041.0/um/x86/dnsrslvr.lib
bd0d15cd029b2bd614eefed4c86f06b6  10.0.19041.0/um/x86/dnsrpc.lib
a8acdbbf0db1f765ba52a0203db28ec4  10.0.19041.0/um/x86/dnsperf.lib
c5eb392c723c8fb4a3a2b5bcfa66a703  10.0.19041.0/um/x86/dnslib.lib
309a26371f3024c94d079850ceb7856a  10.0.19041.0/um/x86/dnscrcli.lib
86620fb93bb28746855338cc09229ca0  10.0.19041.0/um/x86/DnsAPI.Lib
a1f50211866054856840eafd9f5f9eed  10.0.19041.0/um/x86/dmprocessxmlfiltered.lib
77ac98aaabc3d0a6ba23f06d57c63a8f  10.0.19041.0/um/x86/dmoguids.lib
56cd40e88233a7df1b931716c82e753c  10.0.19041.0/um/x86/dloadhelper.lib
2b35e2eb9ff07fe48f02121ef87c4f98  10.0.19041.0/um/x86/directml.lib
79cf87a3144df6db96c7025633a09b7f  10.0.19041.0/um/x86/dinput8.lib
b9c2a99af99e083b70e3f0727d3a67c9  10.0.19041.0/um/x86/DiagnosticDataQuery.Lib
c6fbc45874d576669222888fe3beccfa  10.0.19041.0/um/x86/dhcpsapi.lib
ae3dea92ef3433098512ed0d2f0493d5  10.0.19041.0/um/x86/DhcpCSvc6.Lib
f020159598d6f97f9a6b9c8e3fd2b7fc  10.0.19041.0/um/x86/DhcpCSvc.Lib
d3a32706288cad0d296e618b10b62620  10.0.19041.0/um/x86/dflayout.lib
fc219302a8a5143efc4d3d13db5bfdee  10.0.19041.0/um/x86/devmgr.lib
0029a1708beb10493644d330313f317d  10.0.19041.0/um/x86/deviceaccess.lib
eb309104189a7c5ab5b34cc4469f435a  10.0.19041.0/um/x86/devenum.lib
b622b769e77d6aacbf21dc5791e36128  10.0.19041.0/um/x86/ddraw.lib
8756ca1b7983c5c7858c1f0af707595f  10.0.19041.0/um/x86/dcomp.lib
d0fa5b30e2b8b1578595f5e15babe7d5  10.0.19041.0/um/x86/dciman32.lib
982b5ced115488e06713847a88e92db9  10.0.19041.0/um/x86/DbgModel.Lib
5a817d59f81ebb63051e6311e71f1da9  10.0.19041.0/um/x86/DbgHelp.Lib
a116bdf9895480ea0642a8f946b33fb8  10.0.19041.0/um/x86/DbgEng.Lib
e265f2e905137a296bb3eb0b317ec96d  10.0.19041.0/um/x86/davclnt.lib
6239df38fb0ebdfce267f2f25e1ad64e  10.0.19041.0/um/x86/d3dcsxd.lib
808131df3e9affbc274f08e1b631a145  10.0.19041.0/um/x86/d3dcsx.lib
22af91430127642935e06ea6879528f7  10.0.19041.0/um/x86/d3dcompiler.lib
9e6fd1872c900ee681040f8e393f9d6a  10.0.19041.0/um/x86/d3d9.lib
5dc36969df8833f790db4d86b55f2c1a  10.0.19041.0/um/x86/d3d12.lib
ce37d0e545bc01572fea426e8cdd4755  10.0.19041.0/um/x86/d3d11.lib
b4bcfcd5d56756bdce78288b35a14c0a  10.0.19041.0/um/x86/d3d10.lib
ff2a4bd97a353f8711e313ef55e3067c  10.0.19041.0/um/x86/d3d10_1.lib
f15f5360b499038cb99964f491ae19e2  10.0.19041.0/um/x86/d2d1.lib
532fb4265496023e80bea8e5ed260d42  10.0.19041.0/um/x86/cscdll.lib
057497b63c45e316c210de577fc354a4  10.0.19041.0/um/x86/cscapi.lib
cd52062e91f9b04c1b60559b5093eba0  10.0.19041.0/um/x86/cryptxml.lib
440a38b1ec2465320770b5e382b198af  10.0.19041.0/um/x86/CryptNet.Lib
06ca8461af6f413702de188367128c68  10.0.19041.0/um/x86/cryptui.lib
20009e2ae3b00ba88f15492be77947eb  10.0.19041.0/um/x86/cryptdll.lib
64fcf2cdc01032da473a023090da6772  10.0.19041.0/um/x86/Credui.lib
c6cd31ba42b1b7fa1e2aed5d0c271c46  10.0.19041.0/um/x86/Crypt32.Lib
1f0ea0afb50026f7dc1f7adac7c71989  10.0.19041.0/um/x86/corrEngine.lib
156dc818a8cdaf2d1d819f72a3e64e1f  10.0.19041.0/um/x86/CoreMessaging.lib
707131036c1fcdc795be732c259026fb  10.0.19041.0/um/x86/ComSvcs.Lib
7ae100390558097c82f1e4272b44642c  10.0.19041.0/um/x86/compstui.lib
52b4d99760dc524163a9098bf76a5abd  10.0.19041.0/um/x86/CompPkgSup.lib
8c01cdb635f3402eb59162e89df0da7f  10.0.19041.0/um/x86/ComDlg32.Lib
101bff17452a293e00cc3973e7e1bd50  10.0.19041.0/um/x86/ComCtl32.Lib
52605d68cd27e9329556e718831f73c9  10.0.19041.0/um/x86/ClusApi.Lib
2d160cefc66eb4ad506d4ea955ab537f  10.0.19041.0/um/x86/clfsw32.lib
bf8a5ad704eb6ed2bfdd228f88fbbdc5  10.0.19041.0/um/x86/clfsmgmt.lib
d59d284fc57b9af49cb7cd8478e4410c  10.0.19041.0/um/x86/cldapi.lib
7c167210cb5d175f826d7cd31b1e0271  10.0.19041.0/um/x86/Chakrart.lib
86c2f360c8da6ba65a0cb7704a605adc  10.0.19041.0/um/x86/cfgmgr32.lib
20904e5271ae2fb96853fd0df43fc171  10.0.19041.0/um/x86/cimfs.lib
ff0b71272bce69cf110cf9a5c288fa75  10.0.19041.0/um/x86/CertPolEng.Lib
5152e75c05f13a26c1cce431d3130d14  10.0.19041.0/um/x86/CertIdl.Lib
0e593886d4ee670c671afcc9928544ef  10.0.19041.0/um/x86/certcli.lib
beea46c77f8a97c28958abb2a24aa589  10.0.19041.0/um/x86/certca.lib
9c2c39faa2786770f7bf41849871daba  10.0.19041.0/um/x86/certadm.lib
586a67e4a063d9fde976c70ce4a336b6  10.0.19041.0/um/x86/Cabinet.Lib
f7ab7115e9b4b57c7dc94b221fa43b43  10.0.19041.0/um/x86/BufferOverflowU.lib
2ecfbce01ea95f20a537f167b0df874b  10.0.19041.0/um/x86/BufferOverflow.lib
1439ee6aa9ee7a3bcde607c817d72537  10.0.19041.0/um/x86/bthprops.lib
b2f8c3ff4a92741dbfb7ea896781afab  10.0.19041.0/um/x86/Bits.Lib
6ef0a3115102f9e8bed0093dd76da14d  10.0.19041.0/um/x86/bcrypt.lib
1693f3b4f0f04b8cfee3543c3cff5e21  10.0.19041.0/um/x86/BluetoothApis.lib
d781fed18d491aab78fa9b6e2852ef1a  10.0.19041.0/um/x86/basesrv.lib
d029b3995c1b062bbca8bb94550cc0fd  10.0.19041.0/um/x86/avrt.lib
b7218506e9a456700423026cf1263292  10.0.19041.0/um/x86/aux_ulib.lib
3c1d220c2cab2df7ae5a22d56b7dba5d  10.0.19041.0/um/x86/avifil32.Lib
9828e8d32820687e193d501a970b5726  10.0.19041.0/um/x86/AuthZ.Lib
1e52d09d667531d3abb6b05d69283a85  10.0.19041.0/um/x86/audiomediatypecrt.lib
6ffecd949839b2d100d7c9c396730917  10.0.19041.0/um/x86/audioeng.lib
a5f602062f8ebacd53c6506d1eed9cae  10.0.19041.0/um/x86/AudioBaseProcessingObjectV140.lib
5fcc98ce15cbc8eee0e5edf3234e5024  10.0.19041.0/um/x86/audiobaseprocessingobject.lib
a459fcb415525904655de2d6b18883b3  10.0.19041.0/um/x86/ASycFilt.Lib
9b44e7be86441fd4f8fcea660fc60743  10.0.19041.0/um/x86/appmgr.lib
519689f981923f577b1eb06dec6fa47c  10.0.19041.0/um/x86/appnotify.lib
56cedc0698b2e3542fc565f78f9cdb2e  10.0.19041.0/um/x86/appmgmts.lib
5d84befdc28a54b927727e2fdb45b0ca  10.0.19041.0/um/x86/apidll.lib
867174f70729c7387984db19e7d40b3a  10.0.19041.0/um/x86/amstrmid.lib
2ee7b2a599735272dd9be871f46b95d8  10.0.19041.0/um/x86/amsi.lib
108cabae328a675b00bdd98dab9b9e23  10.0.19041.0/um/x86/ahadmin.lib
a70232f3c161d59a5fe673acb7e1bd2b  10.0.19041.0/um/x86/advpack.Lib
59fec8656f26df680131ce881d4f8140  10.0.19041.0/um/x86/AdvAPI32.Lib
04f344de8cdaf8f17b688bbca0871787  10.0.19041.0/um/x86/ADSIid.Lib
4595e5c9d1192047a978e466356caad0  10.0.19041.0/um/x86/ActiveDS.Lib
ea265accdfc09cd6f7dd542aaf2e0861  10.0.19041.0/ucrt/x86/ucrtd.lib
e30c68e0f12e67c67406d3fe8794700a  10.0.19041.0/ucrt/x86/ucrt.lib
dd7b1886ef09701de503370e0afa1390  10.0.19041.0/um/x86/AclUI.Lib
5d5bb328001be888b45765b4a8371a5a  10.0.19041.0/ucrt/x86/libucrt.lib
016fe691d51fa8a4b19d9187840f6e01  10.0.19041.0/ucrt/x86/libucrtd.lib
```

## .pat

pcf version:
```
COFF parser. Copyright (c) 1997-2019 Hex-Rays SA. Version 1.23
Usage: pcf [-switch or @file or $env_var] file [pattern-file]
        (wildcards are allowed)
```

### compiler: 14.28.29910

```
lib/x86/wsetargv.obj: skipped 1, total 1
lib/x86/vcruntimed.lib: skipped 80, total 81
lib/x86/vcruntime.lib: skipped 80, total 81
lib/x86/vcompd.lib: skipped 113, total 113
lib/x86/vcomp.lib: skipped 113, total 113
lib/x86/vccorlibd.lib: skipped 282, total 577
lib/x86/vccorlib.lib: skipped 286, total 568
lib/x86/vcasand.lib: skipped 0, total 33
lib/x86/vcasan.lib: skipped 1, total 32
lib/x86/vcampd.lib: skipped 166, total 166
lib/x86/vcamp.lib: skipped 165, total 165
lib/x86/threadlocale.obj: skipped 1, total 1
lib/x86/setargv.obj: skipped 1, total 1
lib/x86/pwsetargv.obj: skipped 0, total 2
lib/x86/ptrustud.lib: skipped 0, total 112
lib/x86/ptrustu.lib: skipped 0, total 112
lib/x86/ptrustmd.lib: skipped 0, total 190
lib/x86/ptrustm.lib: skipped 0, total 189
lib/x86/pthreadlocale.obj: skipped 0, total 2
lib/x86/psetargv.obj: skipped 0, total 2
lib/x86/pnothrownew.obj: skipped 0, total 9
lib/x86/pnoenv.obj: skipped 0, total 4
lib/x86/pnoarg.obj: skipped 0, total 4
lib/x86/pnewmode.obj: skipped 0, total 2
lib/x86/plegacy_stdio_float_rounding.obj: skipped 0, total 6
lib/x86/pinvalidcontinue.obj: skipped 0, total 5
lib/x86/pgort.lib: skipped 13, total 29
lib/x86/pgobootrun.lib: skipped 2, total 2
lib/x86/pcommode.obj: skipped 0, total 2
lib/x86/pbinmode.obj: skipped 0, total 2
lib/x86/oldnames.lib: skipped 228, total 228
lib/x86/nothrownew.obj: skipped 0, total 4
lib/x86/notelemetry.obj: skipped 4, total 4
lib/x86/noenv.obj: skipped 3, total 3
lib/x86/noarg.obj: skipped 3, total 3
lib/x86/newmode.obj: skipped 1, total 1
lib/x86/msvcurt_netcore.lib: skipped 1871, total 32710
lib/x86/msvcurtd_netcore.lib: skipped 1879, total 33670
lib/x86/msvcurtd.lib: skipped 1879, total 33670
lib/x86/msvcurt.lib: skipped 1871, total 32710
lib/x86/msvcrtd.lib: skipped 279, total 1493
lib/x86/msvcrt.lib: skipped 307, total 1492
lib/x86/msvcprtd.lib: skipped 1600, total 1718
lib/x86/msvcprt.lib: skipped 1594, total 1694
lib/x86/msvcmrt_netcore.lib: skipped 276, total 597
lib/x86/msvcmrtd_netcore.lib: skipped 276, total 602
lib/x86/msvcmrtd.lib: skipped 276, total 602
lib/x86/msvcmrt.lib: skipped 276, total 597
lib/x86/loosefpmath.obj: skipped 0, total 1
lib/x86/libvcruntimed.lib: skipped 1, total 502
lib/x86/libvcruntime.lib: skipped 30, total 501
lib/x86/libvcasand.lib: skipped 0, total 33
lib/x86/libvcasan.lib: skipped 1, total 32
lib/x86/libsancov.lib: skipped 0, total 20
lib/x86/libompd.lib: skipped 690, total 690
lib/x86/libomp.lib: skipped 690, total 690
lib/x86/libcpmtd1.lib: skipped 2, total 10398
lib/x86/libcpmtd0.lib: skipped 2, total 9873
lib/x86/libcpmtd.lib: skipped 2, total 10400
lib/x86/libcpmt1.lib: skipped 874, total 9964
lib/x86/libcpmt.lib: skipped 962, total 9416
lib/x86/libconcrtd1.lib: skipped 0, total 5418
lib/x86/libconcrtd0.lib: skipped 0, total 5418
lib/x86/libconcrtd.lib: skipped 0, total 5418
lib/x86/libconcrt1.lib: skipped 670, total 5224
lib/x86/libconcrt.lib: skipped 670, total 5224
lib/x86/libcmtd.lib: skipped 134, total 1347
lib/x86/libcmt.lib: skipped 162, total 1346
lib/x86/legacy_x86_flt_exceptions.lib: skipped 0, total 1
lib/x86/legacy_stdio_wide_specifiers.lib: skipped 0, total 3
lib/x86/legacy_stdio_float_rounding.obj: skipped 0, total 2
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
lib/x86/clang_rt.ubsan_standalone_cxx-i386.lib: skipped 3, total 21
lib/x86/clang_rt.ubsan_standalone-i386.lib: skipped 80, total 760
lib/x86/clang_rt.stats_client-i386.lib: skipped 0, total 5
lib/x86/clang_rt.stats-i386.lib: skipped 61, total 563
lib/x86/clang_rt.profile-i386.lib: skipped 6, total 156
lib/x86/clang_rt.fuzzer_no_main-i386.lib: skipped 141, total 2318
lib/x86/clang_rt.fuzzer-i386.lib: skipped 141, total 2319
lib/x86/clang_rt.builtins-i386.lib: skipped 1, total 142
lib/x86/clang_rt.asan_dynamic_runtime_thunk-i386.lib: skipped 2, total 10
lib/x86/clang_rt.asan_dynamic-i386.lib: skipped 340, total 340
lib/x86/clang_rt.asan_dll_thunk-i386.lib: skipped 1, total 637
lib/x86/clang_rt.asan_dbg_dynamic_runtime_thunk-i386.lib: skipped 2, total 10
lib/x86/clang_rt.asan_dbg_dynamic-i386.lib: skipped 340, total 340
lib/x86/clang_rt.asan_dbg_dll_thunk-i386.lib: skipped 1, total 651
lib/x86/clang_rt.asan_dbg-i386.lib: skipped 137, total 1714
lib/x86/clang_rt.asan_cxx_dbg-i386.lib: skipped 3, total 53
lib/x86/clang_rt.asan_cxx-i386.lib: skipped 3, total 53
lib/x86/clang_rt.asan-preinit-i386.lib: skipped 0, total 0
lib/x86/clang_rt.asan-i386.lib: skipped 121, total 1659
lib/x86/chkstk.obj: skipped 0, total 1
lib/x86/binmode.obj: skipped 0, total 1
lib/x86/aligned_new.lib: skipped 0, total 12
lib/x64/wsetargv.obj: skipped 0, total 1
lib/x64/vcruntimed.lib: skipped 74, total 74
lib/x64/vcruntime.lib: skipped 74, total 74
lib/x64/vcompd.lib: skipped 113, total 113
lib/x64/vcomp.lib: skipped 113, total 113
lib/x64/vccorlibd.lib: skipped 282, total 581
lib/x64/vccorlib.lib: skipped 291, total 576
lib/x64/vcasand.lib: skipped 0, total 35
lib/x64/vcasan.lib: skipped 1, total 33
lib/x64/vcampd.lib: skipped 166, total 166
lib/x64/vcamp.lib: skipped 165, total 165
atlmfc/lib/x86/uafxcwd.lib: skipped 2374, total 68057
atlmfc/lib/x86/uafxcw.lib: skipped 9290, total 61197
atlmfc/lib/x86/nafxcwd.lib: skipped 341, total 68806
atlmfc/lib/x86/nafxcw.lib: skipped 7559, total 60044
atlmfc/lib/x86/mfcs140ud.lib: skipped 36, total 1354
atlmfc/lib/x86/mfcs140u.lib: skipped 98, total 903
atlmfc/lib/x86/mfcs140d.lib: skipped 10, total 1392
atlmfc/lib/x86/mfcs140.lib: skipped 75, total 880
atlmfc/lib/x86/MFCM140ud.lib: skipped 34, total 52
atlmfc/lib/x86/MFCM140u.lib: skipped 27, total 45
atlmfc/lib/x86/MFCM140d.lib: skipped 32, total 50
atlmfc/lib/x86/MFCM140.lib: skipped 25, total 43
atlmfc/lib/x86/mfc140ud.lib: skipped 20900, total 20900
atlmfc/lib/x86/mfc140u.lib: skipped 17936, total 17936
atlmfc/lib/x86/mfc140d.lib: skipped 17545, total 17545
atlmfc/lib/x86/mfc140.lib: skipped 14998, total 14998
atlmfc/lib/x86/atls.lib: skipped 4, total 1102
atlmfc/lib/x86/afxnmcdd.lib: skipped 0, total 319
atlmfc/lib/x86/afxnmcd.lib: skipped 26, total 170
atlmfc/lib/x64/uafxcwd.lib: skipped 2266, total 68281
atlmfc/lib/x64/uafxcw.lib: skipped 8551, total 62247
atlmfc/lib/x64/nafxcwd.lib: skipped 341, total 69210
atlmfc/lib/x64/nafxcw.lib: skipped 6634, total 61114
atlmfc/lib/x64/mfcs140ud.lib: skipped 36, total 1312
atlmfc/lib/x64/mfcs140u.lib: skipped 281, total 868
atlmfc/lib/x64/mfcs140d.lib: skipped 10, total 1356
atlmfc/lib/x64/mfcs140.lib: skipped 258, total 845
atlmfc/lib/x64/MFCM140Ud.lib: skipped 33, total 51
atlmfc/lib/x64/MFCM140U.lib: skipped 27, total 45
atlmfc/lib/x64/MFCM140d.lib: skipped 31, total 49
atlmfc/lib/x64/MFCM140.lib: skipped 25, total 43
atlmfc/lib/x64/mfc140ud.lib: skipped 20273, total 20273
atlmfc/lib/x64/mfc140u.lib: skipped 17345, total 17345
atlmfc/lib/x64/mfc140d.lib: skipped 17149, total 17149
atlmfc/lib/x64/mfc140.lib: skipped 14638, total 14638
atlmfc/lib/x64/atls.lib: skipped 27, total 79
atlmfc/lib/x64/afxnmcdd.lib: skipped 1, total 278
atlmfc/lib/x64/afxnmcd.lib: skipped 48, total 165
lib/x64/threadlocale.obj: skipped 1, total 1
lib/x64/setargv.obj: skipped 0, total 1
lib/x64/pwsetargv.obj: skipped 0, total 2
lib/x64/ptrustud.lib: skipped 0, total 112
lib/x64/ptrustu.lib: skipped 0, total 112
lib/x64/ptrustmd.lib: skipped 0, total 190
lib/x64/ptrustm.lib: skipped 0, total 189
lib/x64/pthreadlocale.obj: skipped 0, total 2
lib/x64/psetargv.obj: skipped 0, total 2
lib/x64/pnothrownew.obj: skipped 0, total 9
lib/x64/pnoenv.obj: skipped 0, total 4
lib/x64/pnoarg.obj: skipped 0, total 4
lib/x64/pnewmode.obj: skipped 0, total 2
lib/x64/plegacy_stdio_float_rounding.obj: skipped 0, total 6
lib/x64/pinvalidcontinue.obj: skipped 0, total 5
lib/x64/pgort.lib: skipped 9, total 18
lib/x64/pgobootrun.lib: skipped 2, total 2
lib/x64/pcommode.obj: skipped 0, total 2
lib/x64/pbinmode.obj: skipped 0, total 2
lib/x64/oldnames.lib: skipped 228, total 228
lib/x64/nothrownew.obj: skipped 0, total 4
lib/x64/notelemetry.obj: skipped 4, total 4
lib/x64/noenv.obj: skipped 3, total 3
lib/x64/noarg.obj: skipped 3, total 3
lib/x64/newmode.obj: skipped 0, total 1
lib/x64/msvcurt_netcore.lib: skipped 1860, total 32700
lib/x64/msvcurtd_netcore.lib: skipped 1868, total 33660
lib/x64/msvcurtd.lib: skipped 1868, total 33660
lib/x64/msvcurt.lib: skipped 1860, total 32700
lib/x64/msvcrtd.lib: skipped 295, total 1438
lib/x64/msvcrt.lib: skipped 308, total 1437
lib/x64/msvcprtd.lib: skipped 1600, total 1709
lib/x64/msvcprt.lib: skipped 1596, total 1694
lib/x64/msvcmrt_netcore.lib: skipped 274, total 595
lib/x64/msvcmrtd_netcore.lib: skipped 274, total 600
lib/x64/msvcmrtd.lib: skipped 274, total 600
lib/x64/msvcmrt.lib: skipped 274, total 595
lib/x64/loosefpmath.obj: skipped 0, total 1
lib/x64/libvcruntimed.lib: skipped 3, total 588
lib/x64/libvcruntime.lib: skipped 38, total 583
lib/x64/libvcasand.lib: skipped 0, total 35
lib/x64/libvcasan.lib: skipped 1, total 33
lib/x64/libsancov.lib: skipped 0, total 20
lib/x64/libompd.lib: skipped 690, total 690
lib/x64/libomp.lib: skipped 690, total 690
lib/x64/libcpmtd1.lib: skipped 30, total 10698
lib/x64/libcpmtd0.lib: skipped 30, total 10149
lib/x64/libcpmtd.lib: skipped 30, total 10700
lib/x64/libcpmt1.lib: skipped 1354, total 10218
lib/x64/libcpmt.lib: skipped 1349, total 9684
lib/x64/libconcrtd1.lib: skipped 13, total 5419
lib/x64/libconcrtd0.lib: skipped 13, total 5419
lib/x64/libconcrtd.lib: skipped 13, total 5419
lib/x64/libconcrt1.lib: skipped 589, total 5245
lib/x64/libconcrt.lib: skipped 589, total 5245
lib/x64/libcmtd.lib: skipped 151, total 1294
lib/x64/libcmt.lib: skipped 164, total 1293
lib/x64/legacy_stdio_wide_specifiers.lib: skipped 0, total 3
lib/x64/legacy_stdio_float_rounding.obj: skipped 0, total 2
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
lib/x64/clang_rt.ubsan_standalone_cxx-x86_64.lib: skipped 3, total 14
lib/x64/clang_rt.ubsan_standalone-x86_64.lib: skipped 91, total 746
lib/x64/clang_rt.stats_client-x86_64.lib: skipped 0, total 5
lib/x64/clang_rt.stats-x86_64.lib: skipped 71, total 555
lib/x64/clang_rt.profile-x86_64.lib: skipped 6, total 156
lib/x64/clang_rt.fuzzer_no_main-x86_64.lib: skipped 227, total 2270
lib/x64/clang_rt.fuzzer-x86_64.lib: skipped 227, total 2271
lib/x64/clang_rt.builtins-x86_64.lib: skipped 1, total 133
lib/x64/clang_rt.asan_dynamic_runtime_thunk-x86_64.lib: skipped 2, total 10
lib/x64/clang_rt.asan_dynamic-x86_64.lib: skipped 339, total 339
lib/x64/clang_rt.asan_dll_thunk-x86_64.lib: skipped 0, total 637
lib/x64/clang_rt.asan_dbg_dynamic_runtime_thunk-x86_64.lib: skipped 2, total 10
lib/x64/clang_rt.asan_dbg_dynamic-x86_64.lib: skipped 339, total 339
lib/x64/clang_rt.asan_dbg_dll_thunk-x86_64.lib: skipped 0, total 651
lib/x64/clang_rt.asan_dbg-x86_64.lib: skipped 153, total 1706
lib/x64/clang_rt.asan_cxx_dbg-x86_64.lib: skipped 3, total 34
lib/x64/clang_rt.asan_cxx-x86_64.lib: skipped 3, total 34
lib/x64/clang_rt.asan-x86_64.lib: skipped 135, total 1654
lib/x64/clang_rt.asan-preinit-x86_64.lib: skipped 0, total 0
lib/x64/chkstk.obj: skipped 0, total 1
lib/x64/binmode.obj: skipped 0, total 1
lib/x64/aligned_new.lib: skipped 0, total 12
```

### ucrt: 10.0.18362.0

```
um/x64/xpsprint.lib: skipped 4, total 4
um/x64/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x64/xolehlp.lib: skipped 8, total 8
um/x64/xmllite.lib: skipped 6, total 6
um/x64/xinputuap.lib: skipped 8, total 8
um/x64/Xinput9_1_0.lib: skipped 5, total 5
um/x64/xaudio2_8.lib: skipped 7, total 7
um/x64/xaudio2.lib: skipped 10, total 10
um/x64/xaswitch.lib: skipped 0, total 17
um/x64/xapobase2_8.lib: skipped 5, total 150
um/x64/xinput.lib: skipped 8, total 8
um/x64/wuguid.lib: skipped 0, total 0
um/x64/xapobase.lib: skipped 5, total 150
um/x64/WtsApi32.Lib: skipped 65, total 65
um/x64/WSock32.Lib: skipped 75, total 75
um/x64/wsmsvc.lib: skipped 3673, total 3673
um/x64/WSnmp32.Lib: skipped 51, total 51
um/x64/wsdapi.lib: skipped 45, total 45
um/x64/wscapi.lib: skipped 39, total 39
um/x64/wsclient.lib: skipped 30, total 30
um/x64/wsbonline.lib: skipped 3, total 3
um/x64/wsbapp_uuid.Lib: skipped 0, total 0
um/x64/WS2_32.Lib: skipped 195, total 195
um/x64/workspaceax.lib: skipped 0, total 3
um/x64/wofutil.lib: skipped 11, total 11
um/x64/wmvcore.lib: skipped 20, total 20
um/x64/wnvapi.lib: skipped 2, total 2
um/x64/wmiutils.lib: skipped 0, total 0
um/x64/wmip.lib: skipped 45, total 45
um/x64/wmcodecdspuuid.lib: skipped 0, total 0
um/x64/Wldp.Lib: skipped 19, total 19
um/x64/Wldap32.Lib: skipped 245, total 245
um/x64/wlanui.lib: skipped 5, total 5
um/x64/wlanapi.lib: skipped 68, total 68
um/x64/winusb.lib: skipped 37, total 37
um/x64/WinTrust.Lib: skipped 145, total 145
um/x64/WinStrm.Lib: skipped 0, total 18
um/x64/winsqlite3.lib: skipped 263, total 263
um/x64/winsta.lib: skipped 171, total 171
um/x64/WinSpool.Lib: skipped 232, total 232
um/x64/winscard.lib: skipped 74, total 74
um/x64/winsatapi.lib: skipped 0, total 0
um/x64/WinMM.Lib: skipped 179, total 179
um/x64/winml.lib: skipped 1, total 1
um/x64/WinInet.Lib: skipped 319, total 319
um/x64/WinHvEmulation.lib: skipped 4, total 4
um/x64/WinHvPlatform.lib: skipped 25, total 25
um/x64/winfax.lib: skipped 56, total 56
um/x64/winhttp.lib: skipped 64, total 64
um/x64/windowssideshowguids.lib: skipped 0, total 0
um/x64/windowscodecs.lib: skipped 114, total 114
um/x64/WindowsApp_downlevel.lib: skipped 4627, total 4627
um/x64/WindowsApp.lib: skipped 4627, total 4627
um/x64/windows.ui.lib: skipped 2, total 2
um/x64/windows.networking.lib: skipped 1, total 1
um/x64/windows.data.pdf.lib: skipped 1, total 1
um/x64/WinBio.lib: skipped 60, total 60
um/x64/windows.ai.machinelearning.lib: skipped 1, total 1
um/x64/wiautil.lib: skipped 3, total 128
um/x64/WiaGuid.Lib: skipped 0, total 0
um/x64/wevtapi.lib: skipped 45, total 45
um/x64/wiaservc.lib: skipped 55, total 55
um/x64/Wer.lib: skipped 145, total 145
um/x64/websocket.lib: skipped 13, total 13
um/x64/wecapi.lib: skipped 17, total 17
um/x64/WebServices.lib: skipped 193, total 193
um/x64/webauthn.lib: skipped 10, total 10
um/x64/wdstptc.lib: skipped 19, total 19
um/x64/wdsmc.lib: skipped 13, total 13
um/x64/wdspxe.lib: skipped 32, total 32
um/x64/wdsbp.lib: skipped 7, total 7
um/x64/wdsClientAPI.LIB: skipped 58, total 58
um/x64/wcmguid.lib: skipped 0, total 0
um/x64/wcmapi.lib: skipped 39, total 39
um/x64/vstorinterface.lib: skipped 15, total 15
um/x64/wbemuuid.lib: skipped 0, total 0
um/x64/vss_uuid.lib: skipped 0, total 0
um/x64/vssapi.lib: skipped 46, total 46
um/x64/vscmgr.lib: skipped 0, total 0
um/x64/vmdevicehost.lib: skipped 10, total 10
um/x64/vmsavedstatedumpprovider.lib: skipped 24, total 24
um/x64/Virtdisk.Lib: skipped 29, total 29
um/x64/Version.Lib: skipped 12, total 12
um/x64/vds_uuid.lib: skipped 0, total 0
um/x64/vertdll.lib: skipped 92, total 95
um/x64/Vfw32.Lib: skipped 127, total 127
um/x64/vccomsup.lib: skipped 0, total 26
um/x64/Uuid.Lib: skipped 0, total 0
um/x64/USP10.Lib: skipped 40, total 40
um/x64/Uxtheme.lib: skipped 78, total 78
um/x64/UserEnv.Lib: skipped 72, total 72
um/x64/User32.Lib: skipped 780, total 780
um/x64/Urlmon.Lib: skipped 95, total 95
um/x64/umpdddi.lib: skipped 90, total 90
um/x64/ualapi.lib: skipped 10, total 10
um/x64/UIAutomationCore.lib: skipped 99, total 99
um/x64/txfw32.lib: skipped 9, total 9
um/x64/twinapi.lib: skipped 0, total 0
um/x64/tspubplugincom.lib: skipped 1, total 8
um/x64/tsec.lib: skipped 27, total 27
um/x64/TranscodeImageUID.lib: skipped 0, total 0
um/x64/Traffic.Lib: skipped 22, total 22
um/x64/tokenbinding.lib: skipped 10, total 10
um/x64/tdh.lib: skipped 26, total 26
um/x64/tbs.lib: skipped 21, total 21
um/x64/taskschd.lib: skipped 0, total 0
um/x64/tapi32l.lib: skipped 0, total 250
um/x64/Tapi32.Lib: skipped 278, total 278
um/x64/t2embed.lib: skipped 14, total 14
um/x64/synchronization.lib: skipped 3, total 3
um/x64/swdevice.lib: skipped 9, total 9
um/x64/structuredquery.lib: skipped 0, total 0
um/x64/strsafe.lib: skipped 0, total 23
um/x64/Svcguid.Lib: skipped 0, total 0
um/x64/strmiids.lib: skipped 0, total 0
um/x64/strmbase.lib: skipped 135, total 1681
um/x64/Sti.Lib: skipped 16, total 16
um/x64/ssdpapi.lib: skipped 29, total 29
um/x64/srpapi.lib: skipped 21, total 21
um/x64/SrClient.lib: skipped 0, total 28
um/x64/SpOrder.Lib: skipped 2, total 2
um/x64/spoolss.lib: skipped 206, total 206
um/x64/SnmpAPI.Lib: skipped 38, total 38
um/x64/slc.lib: skipped 40, total 40
um/x64/slcext.lib: skipped 9, total 9
um/x64/slwga.lib: skipped 1, total 1
um/x64/ShFolder.Lib: skipped 2, total 2
um/x64/shell32.lib: skipped 399, total 399
um/x64/shdocvw.lib: skipped 19, total 19
um/x64/ShLwApi.Lib: skipped 365, total 365
um/x64/shcore.lib: skipped 20, total 20
um/x64/Sfc.Lib: skipped 16, total 16
um/x64/SensorsUtils.lib: skipped 62, total 62
um/x64/SetupAPI.Lib: skipped 558, total 558
um/x64/sensorsapi.lib: skipped 0, total 0
um/x64/SensAPI.Lib: skipped 3, total 3
um/x64/security.lib: skipped 36, total 36
um/x64/sens.lib: skipped 3, total 3
um/x64/Secur32.Lib: skipped 96, total 96
um/x64/ScrnSavW.Lib: skipped 0, total 20
um/x64/ScrnSave.Lib: skipped 0, total 20
um/x64/SearchSDK.lib: skipped 0, total 0
um/x64/schannel.lib: skipped 36, total 36
um/x64/scesrv.lib: skipped 2, total 2
um/x64/SCardDlg.Lib: skipped 5, total 5
um/x64/sbtsv.lib: skipped 0, total 1
um/x64/scecli.lib: skipped 72, total 72
um/x64/sas.lib: skipped 1, total 1
um/x64/SAPI.Lib: skipped 0, total 0
um/x64/samsrv.lib: skipped 328, total 328
um/x64/samlib.lib: skipped 70, total 70
um/x64/RTWorkQ.lib: skipped 34, total 34
um/x64/rtutils.lib: skipped 41, total 41
um/x64/Rtm.Lib: skipped 116, total 116
um/x64/runtimeobject.lib: skipped 64, total 64
um/x64/rstrtmgr.lib: skipped 12, total 12
um/x64/RpcRT4.Lib: skipped 543, total 543
um/x64/rpcutil.lib: skipped 0, total 23
um/x64/rpcproxy.lib: skipped 5, total 5
um/x64/Rpcns4.Lib: skipped 62, total 62
um/x64/rpcexts.lib: skipped 58, total 58
um/x64/rometadata.lib: skipped 1, total 1
um/x64/resutils.lib: skipped 126, total 126
um/x64/rasuser.lib: skipped 5, total 5
um/x64/RASDlg.Lib: skipped 25, total 25
um/x64/RASAPI32.Lib: skipped 148, total 148
um/x64/qwave.lib: skipped 14, total 14
um/x64/query.lib: skipped 6, total 6
um/x64/Psapi.Lib: skipped 27, total 27
um/x64/propsys.lib: skipped 219, total 219
um/x64/quartz.lib: skipped 4, total 4
um/x64/prntvpt.lib: skipped 29, total 29
um/x64/powrprof.lib: skipped 109, total 109
um/x64/ProjectedFSLib.lib: skipped 33, total 33
um/x64/PhotoAcquireUID.lib: skipped 0, total 0
um/x64/PeerDist.lib: skipped 28, total 28
um/x64/PortableDeviceGuids.lib: skipped 0, total 0
um/x64/Pdh.Lib: skipped 110, total 110
um/x64/pathcch.lib: skipped 22, total 22
ucrt/x86/libucrt.lib: skipped 663, total 8421
ucrt/x86/libucrtd.lib: skipped 214, total 8596
um/x64/p2pgraph.lib: skipped 40, total 40
ucrt/x86/ucrt.lib: skipped 1378, total 1378
ucrt/x86/ucrtd.lib: skipped 1441, total 1441
um/x64/p2p.lib: skipped 112, total 112
um/x64/opmxbox.Lib: skipped 3, total 3
um/x64/osptk.lib: skipped 0, total 0
um/x64/OneCore_downlevel.Lib: skipped 4851, total 4854
um/x64/OpenGL32.Lib: skipped 368, total 368
um/x64/OneCoreUAP_downlevel.Lib: skipped 4851, total 4854
um/x64/OneCore_apiset.Lib: skipped 5218, total 5218
um/x64/OneCoreUAP_apiset.Lib: skipped 9261, total 9261
um/x64/OneCoreUAP.Lib: skipped 11565, total 11568
um/x64/OneCore.Lib: skipped 7618, total 7621
um/x64/olesvr32.lib: skipped 23, total 23
um/x64/ondemandconnroutehelper.lib: skipped 8, total 8
um/x64/OleDlg.Lib: skipped 23, total 23
um/x64/oledb.lib: skipped 0, total 0
um/x64/olecli32.lib: skipped 178, total 178
um/x64/OleAut32.Lib: skipped 412, total 412
um/x64/Ole32.Lib: skipped 504, total 504
um/x64/OleAcc.Lib: skipped 20, total 20
um/x64/OemLicense.lib: skipped 6, total 6
um/x64/odbccp32.lib: skipped 0, total 56
um/x64/odbcbcp.lib: skipped 28, total 28
um/x64/odbc32.lib: skipped 176, total 176
um/x64/objsel.lib: skipped 0, total 0
um/x64/ntstc_msvcrt.lib: skipped 369, total 6624
um/x64/ntstc_libcmt.lib: skipped 369, total 6624
um/x64/NtQuery.Lib: skipped 6, total 6
um/x64/ntmarta.lib: skipped 44, total 44
um/x64/ntfrsapi.lib: skipped 33, total 33
um/x64/ntlanman.lib: skipped 23, total 23
um/x64/ntdsatq.lib: skipped 47, total 47
um/x64/ntdsetup.lib: skipped 24, total 24
um/x64/NtDsAPI.Lib: skipped 120, total 120
um/x64/ntdll.lib: skipped 2084, total 2084
um/x64/ntdsa.lib: skipped 146, total 146
um/x64/nt.lib: skipped 0, total 6
um/x64/normaliz.lib: skipped 5, total 5
um/x64/ninput.lib: skipped 23, total 23
um/x86/xpsprint.lib: skipped 4, total 4
um/x64/newdev.lib: skipped 23, total 23
um/x64/NetSh.Lib: skipped 23, total 23
um/x64/netlib.lib: skipped 3, total 269
um/x64/NetAPI32.Lib: skipped 212, total 212
um/x86/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x64/ndproxystub.lib: skipped 0, total 0
um/x64/ndfapi.lib: skipped 24, total 24
um/x64/nddeapi.lib: skipped 28, total 28
um/x64/ncrypt.lib: skipped 136, total 136
um/x64/nanosrv.lib: skipped 7091, total 7091
um/x64/muiload.lib: skipped 0, total 64
um/x64/mtxdm.lib: skipped 1, total 1
um/x64/Mtx.Lib: skipped 3, total 3
um/x64/msxml6.lib: skipped 0, total 0
um/x64/MsXml2.Lib: skipped 0, total 0
um/x64/MsWSock.Lib: skipped 28, total 28
um/x64/MSTask.Lib: skipped 11, total 11
um/x64/msvfw32.Lib: skipped 47, total 47
um/x64/msv1_0.lib: skipped 19, total 19
um/x64/MSRating.Lib: skipped 32, total 32
um/x64/msports.lib: skipped 11, total 11
um/x64/mspbase.lib: skipped 170, total 1367
um/x86/xolehlp.lib: skipped 8, total 8
um/x64/mspatchc.lib: skipped 14, total 14
um/x86/xmllite.lib: skipped 6, total 6
um/x64/mspatcha.lib: skipped 16, total 16
um/x64/MSImg32.Lib: skipped 3, total 3
um/x86/xinputuap.lib: skipped 8, total 8
um/x86/Xinput9_1_0.lib: skipped 5, total 5
um/x64/Msi.Lib: skipped 290, total 290
um/x86/xinput.lib: skipped 8, total 8
um/x86/xaudio2_8.lib: skipped 7, total 7
um/x64/msdrm.lib: skipped 85, total 85
um/x64/msdmo.lib: skipped 15, total 15
um/x86/xaudio2.lib: skipped 10, total 10
um/x86/xaswitch.lib: skipped 0, total 19
um/x64/msdelta.lib: skipped 15, total 15
um/x86/xapobase2_8.lib: skipped 3, total 152
um/x86/xapobase.lib: skipped 3, total 152
um/x86/wuguid.lib: skipped 0, total 0
um/x64/msdasc.lib: skipped 0, total 0
um/x86/WtsApi32.Lib: skipped 65, total 65
um/x64/MsCtfMonitor.lib: skipped 3, total 3
um/x64/Mscms.Lib: skipped 129, total 129
um/x86/WSock32.Lib: skipped 75, total 75
um/x86/WSnmp32.Lib: skipped 51, total 51
um/x64/MSAcm32.Lib: skipped 42, total 42
um/x64/MSAJApi.lib: skipped 558, total 558
um/x64/msaatext.lib: skipped 0, total 0
um/x86/wsmsvc.lib: skipped 3673, total 3673
um/x86/wsdapi.lib: skipped 45, total 45
um/x64/MqRt.Lib: skipped 47, total 47
um/x64/MrmSupport.lib: skipped 24, total 24
um/x86/wsclient.lib: skipped 30, total 30
um/x86/wscapi.lib: skipped 39, total 39
um/x86/wsbonline.lib: skipped 3, total 3
um/x86/wsbapp_uuid.Lib: skipped 0, total 0
um/x64/MqOA.Lib: skipped 0, total 0
um/x86/WS2_32.Lib: skipped 180, total 180
um/x86/Wow32.Lib: skipped 29, total 29
um/x64/mprsnap.lib: skipped 46, total 46
um/x64/Mprapi.Lib: skipped 160, total 160
um/x64/Mpr.Lib: skipped 43, total 43
um/x86/workspaceax.lib: skipped 0, total 3
um/x64/mmdevapi.lib: skipped 29, total 29
um/x64/MMC.Lib: skipped 11, total 94
um/x64/mincore_downlevel.lib: skipped 451, total 451
um/x64/mincore.lib: skipped 4428, total 4428
um/x64/mi.lib: skipped 2, total 2
um/x64/MgmtAPI.Lib: skipped 9, total 9
um/x64/mfuuid.lib: skipped 0, total 0
um/x64/Mfsrcsnk.lib: skipped 2, total 2
um/x64/mfsensorgroup.lib: skipped 5, total 5
um/x64/mfreadwrite.lib: skipped 5, total 5
um/x64/mfplay.lib: skipped 1, total 1
um/x64/Mfplat.lib: skipped 150, total 150
um/x64/Mfcore.lib: skipped 38, total 38
um/x64/Mf.lib: skipped 75, total 75
um/x64/MDMRegistration.lib: skipped 13, total 13
um/x64/mdmlocalmanagement.lib: skipped 3, total 3
um/x64/mciole32.lib: skipped 11, total 11
um/x64/mbnapi_uuid.lib: skipped 0, total 0
um/x64/MAPI32.Lib: skipped 136, total 136
um/x64/magnification.lib: skipped 21, total 21
um/x64/locationapi.lib: skipped 0, total 0
um/x64/Lz32.Lib: skipped 14, total 14
um/x64/LoadPerf.Lib: skipped 14, total 14
um/x64/ktmw32.lib: skipped 44, total 44
um/x64/ksuser.lib: skipped 8, total 8
um/x64/keycredmgr.lib: skipped 4, total 4
um/x64/KSProxy.Lib: skipped 6, total 6
um/x86/wofutil.lib: skipped 11, total 11
um/x64/kernel32legacylib.lib: skipped 9, total 599
um/x86/wmvcore.lib: skipped 20, total 20
um/x64/kernel32.Lib: skipped 1343, total 1343
um/x86/wmiutils.lib: skipped 0, total 0
um/x64/kerbcli.lib: skipped 0, total 3
um/x86/wmip.lib: skipped 45, total 45
um/x64/jsrt.lib: skipped 92, total 92
um/x86/wmcodecdspuuid.lib: skipped 0, total 0
um/x64/iscsidsc.lib: skipped 80, total 80
um/x64/irprops.lib: skipped 35, total 35
um/x64/Iprop.Lib: skipped 8, total 8
um/x86/Wldp.Lib: skipped 19, total 19
um/x64/iphlpapi.lib: skipped 290, total 290
um/x64/inseng.lib: skipped 7, total 7
um/x86/Wldap32.Lib: skipped 245, total 245
um/x64/inkobjcore.lib: skipped 30, total 30
um/x64/infocardapi.Lib: skipped 18, total 18
um/x86/wlanui.lib: skipped 5, total 5
um/x86/wlanapi.lib: skipped 68, total 68
um/x64/Imm32.Lib: skipped 82, total 82
um/x86/winusb.lib: skipped 37, total 37
um/x64/imgutil.Lib: skipped 9, total 9
um/x86/WinStrm.Lib: skipped 0, total 18
um/x86/WinTrust.Lib: skipped 145, total 145
um/x86/winsta.lib: skipped 171, total 171
um/x64/ImageHlp.Lib: skipped 149, total 149
um/x86/winsqlite3.lib: skipped 263, total 263
um/x86/WinSpool.Lib: skipped 232, total 232
um/x86/winscard.lib: skipped 74, total 74
um/x64/iesetup.lib: skipped 7, total 7
um/x86/winsatapi.lib: skipped 0, total 0
um/x64/IEPMAPI.Lib: skipped 0, total 24
um/x86/WinMM.Lib: skipped 191, total 191
um/x64/icuuc.lib: skipped 542, total 542
um/x64/icuin.Lib: skipped 416, total 416
um/x86/winml.lib: skipped 1, total 1
um/x64/icu.lib: skipped 958, total 958
um/x86/winhttp.lib: skipped 64, total 64
um/x86/WinInet.Lib: skipped 319, total 319
um/x64/Icm32.Lib: skipped 21, total 21
um/x64/Icmui.Lib: skipped 2, total 2
um/x86/winfax.lib: skipped 56, total 56
um/x64/iashlpr.lib: skipped 12, total 12
um/x86/windowssideshowguids.lib: skipped 0, total 0
um/x86/windowscodecs.lib: skipped 114, total 114
um/x64/Htmlhelp.Lib: skipped 0, total 6
um/x86/WindowsApp_downlevel.lib: skipped 4609, total 4609
um/x64/httpapi.lib: skipped 46, total 46
um/x86/WindowsApp.lib: skipped 4609, total 4609
um/x86/windows.ui.lib: skipped 2, total 2
um/x64/hrtfapo.lib: skipped 4, total 4
um/x86/windows.networking.lib: skipped 1, total 1
um/x64/HLink.Lib: skipped 28, total 28
um/x86/windows.data.pdf.lib: skipped 1, total 1
um/x64/hid.lib: skipped 44, total 44
um/x86/windows.ai.machinelearning.lib: skipped 1, total 1
um/x64/hhsetup.lib: skipped 145, total 145
um/x86/WinBio.lib: skipped 60, total 60
um/x86/wiautil.lib: skipped 3, total 128
um/x86/wiaservc.lib: skipped 55, total 55
um/x64/hbaapi.lib: skipped 93, total 93
um/x64/gpmuuid.lib: skipped 0, total 0
um/x64/GPEdit.lib: skipped 10, total 10
um/x86/WiaGuid.Lib: skipped 0, total 0
um/x86/wevtapi.lib: skipped 45, total 45
um/x86/Wer.lib: skipped 145, total 145
um/x86/wecapi.lib: skipped 17, total 17
um/x86/websocket.lib: skipped 13, total 13
um/x64/GlU32.Lib: skipped 52, total 52
um/x86/WebServices.lib: skipped 193, total 193
um/x64/glmf32.lib: skipped 134, total 134
um/x86/webauthn.lib: skipped 10, total 10
um/x64/gdiplus.lib: skipped 630, total 630
um/x64/Gdi32.Lib: skipped 605, total 605
um/x86/wdstptc.lib: skipped 19, total 19
um/x64/fxsutility.lib: skipped 2, total 2
um/x86/wdspxe.lib: skipped 32, total 32
um/x64/fwpuclnt.lib: skipped 276, total 276
um/x86/wdsmc.lib: skipped 13, total 13
um/x64/FrameDyn.Lib: skipped 604, total 604
um/x64/FrameDyd.Lib: skipped 604, total 604
um/x86/wdsbp.lib: skipped 7, total 7
um/x86/wcmguid.lib: skipped 0, total 0
um/x64/fontsub.lib: skipped 2, total 2
um/x86/wcmapi.lib: skipped 39, total 39
um/x64/fltLib.lib: skipped 29, total 29
um/x86/wdsClientAPI.LIB: skipped 58, total 58
um/x86/wbemuuid.lib: skipped 0, total 0
um/x64/fileextd.lib: skipped 0, total 15
um/x86/vstorinterface.lib: skipped 15, total 15
um/x86/vss_uuid.lib: skipped 0, total 0
um/x64/FhSvcCtl.lib: skipped 14, total 14
um/x86/vssapi.lib: skipped 46, total 46
um/x64/feclient.lib: skipped 54, total 54
um/x64/FaultRep.Lib: skipped 16, total 16
um/x86/vscmgr.lib: skipped 0, total 0
um/x64/evr.lib: skipped 9, total 9
um/x86/Virtdisk.Lib: skipped 29, total 29
um/x64/esent.lib: skipped 375, total 375
um/x64/ElsCore.lib: skipped 5, total 5
um/x86/Vfw32.Lib: skipped 127, total 127
um/x86/vds_uuid.lib: skipped 0, total 0
um/x64/els.lib: skipped 0, total 0
um/x86/VdmDbg.Lib: skipped 28, total 28
um/x86/Version.Lib: skipped 12, total 12
um/x64/ehstorguids.lib: skipped 0, total 0
um/x86/vccomsup.lib: skipped 0, total 26
um/x64/efswrt.lib: skipped 27, total 27
um/x86/Uxtheme.lib: skipped 78, total 78
um/x64/easregprov.lib: skipped 2, total 2
um/x86/Uuid.Lib: skipped 0, total 0
um/x64/eappprxy.lib: skipped 18, total 18
um/x64/elfapi.lib: skipped 0, total 122
um/x64/eappcfg.lib: skipped 15, total 15
um/x86/USP10.Lib: skipped 40, total 40
um/x86/UserEnv.Lib: skipped 72, total 72
um/x64/dxtrans.lib: skipped 6, total 6
um/x86/User32.Lib: skipped 772, total 772
um/x64/dxtmsft.lib: skipped 0, total 0
um/x64/dxva2.lib: skipped 38, total 38
um/x86/Urlmon.Lib: skipped 95, total 95
um/x86/unicows.lib: skipped 1010, total 2535
um/x64/dxguid.lib: skipped 0, total 0
um/x64/dxgi.lib: skipped 15, total 15
um/x86/umpdddi.lib: skipped 90, total 90
um/x64/dxcompiler.lib: skipped 2, total 2
um/x64/dwrite.lib: skipped 1, total 1
um/x86/UIAutomationCore.lib: skipped 99, total 99
um/x86/ualapi.lib: skipped 10, total 10
um/x64/dwmapi.lib: skipped 31, total 31
um/x86/txfw32.lib: skipped 9, total 9
um/x64/DtcHelp.Lib: skipped 2, total 17
um/x86/twinapi.lib: skipped 0, total 0
um/x64/DSUIExt.Lib: skipped 33, total 33
um/x86/twain_32.lib: skipped 5, total 5
um/x64/dststlog.lib: skipped 1, total 1
um/x86/tspubplugincom.lib: skipped 1, total 8
um/x64/dssec.lib: skipped 4, total 4
um/x86/tsec.lib: skipped 27, total 27
um/x64/dsound.lib: skipped 10, total 10
um/x64/DSProp.Lib: skipped 19, total 19
um/x86/TranscodeImageUID.lib: skipped 0, total 0
um/x64/drttransport.lib: skipped 2, total 2
um/x86/Traffic.Lib: skipped 22, total 22
um/x64/drtprov.lib: skipped 9, total 9
um/x64/drt.lib: skipped 21, total 21
um/x86/Thunk32.Lib: skipped 66, total 66
um/x86/tdh.lib: skipped 26, total 26
um/x64/dpx.lib: skipped 11, total 11
um/x86/tokenbinding.lib: skipped 10, total 10
um/x64/dnsrslvr.lib: skipped 4, total 4
um/x86/tbs.lib: skipped 21, total 21
um/x86/taskschd.lib: skipped 0, total 0
um/x64/dnsperf.lib: skipped 3, total 3
um/x86/tapi32l.lib: skipped 0, total 250
um/x64/dnsrpc.lib: skipped 1, total 375
um/x64/dnslib.lib: skipped 5, total 1395
um/x86/Tapi32.Lib: skipped 278, total 278
um/x86/t2embed.lib: skipped 14, total 14
um/x64/DnsAPI.Lib: skipped 288, total 288
um/x64/dnscrcli.lib: skipped 0, total 4
um/x86/synchronization.lib: skipped 3, total 3
um/x64/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x86/Svcguid.Lib: skipped 0, total 0
um/x86/swdevice.lib: skipped 9, total 9
um/x86/structuredquery.lib: skipped 0, total 0
um/x86/strsafe.lib: skipped 0, total 22
um/x64/dmoguids.lib: skipped 0, total 0
um/x86/strmiids.lib: skipped 0, total 0
um/x64/dloadhelper.lib: skipped 0, total 3
um/x86/strmbase.lib: skipped 155, total 1684
um/x64/directml.lib: skipped 1, total 1
um/x86/Sti.Lib: skipped 16, total 16
um/x64/dinput8.lib: skipped 1, total 2
um/x64/dhcpsapi.lib: skipped 209, total 209
um/x64/DhcpCSvc6.Lib: skipped 22, total 22
um/x64/DhcpCSvc.Lib: skipped 68, total 68
um/x64/devmgr.lib: skipped 19, total 19
um/x86/srpapi.lib: skipped 21, total 21
um/x86/ssdpapi.lib: skipped 29, total 29
um/x64/dflayout.lib: skipped 1, total 1
um/x64/deviceaccess.lib: skipped 3, total 3
um/x86/SrClient.lib: skipped 0, total 28
um/x64/devenum.lib: skipped 0, total 0
um/x64/ddraw.lib: skipped 13, total 13
um/x86/SpOrder.Lib: skipped 2, total 2
um/x86/spoolss.lib: skipped 206, total 206
um/x64/dcomp.lib: skipped 6, total 6
um/x86/SnmpAPI.Lib: skipped 38, total 38
um/x64/dciman32.lib: skipped 20, total 20
um/x86/slwga.lib: skipped 1, total 1
um/x64/DbgModel.Lib: skipped 1, total 1
um/x64/DbgHelp.Lib: skipped 241, total 241
um/x86/slc.lib: skipped 40, total 40
um/x64/DbgEng.Lib: skipped 4, total 4
um/x86/slcext.lib: skipped 9, total 9
um/x86/ShLwApi.Lib: skipped 365, total 365
um/x64/davclnt.lib: skipped 22, total 22
um/x64/d3dcsxd.lib: skipped 9, total 9
um/x86/ShFolder.Lib: skipped 2, total 2
um/x86/shell32.lib: skipped 399, total 399
um/x64/d3dcsx.lib: skipped 9, total 9
um/x86/shdocvw.lib: skipped 19, total 19
um/x64/d3dcompiler.lib: skipped 29, total 29
um/x86/shcore.lib: skipped 20, total 20
um/x64/d3d9.lib: skipped 14, total 14
um/x86/Sfc.Lib: skipped 16, total 16
um/x64/d3d12.lib: skipped 14, total 14
um/x86/SetupAPI.Lib: skipped 558, total 558
um/x64/d3d11.lib: skipped 45, total 45
um/x86/SensorsUtils.lib: skipped 62, total 62
um/x86/sensorsapi.lib: skipped 0, total 0
um/x64/d3d10_1.lib: skipped 29, total 29
um/x64/d3d10.lib: skipped 29, total 29
um/x86/SensAPI.Lib: skipped 3, total 3
um/x64/cscdll.lib: skipped 18, total 18
um/x64/d2d1.lib: skipped 13, total 13
um/x86/sens.lib: skipped 3, total 3
um/x64/cscapi.lib: skipped 6, total 6
um/x86/security.lib: skipped 36, total 36
um/x86/Secur32.Lib: skipped 96, total 96
um/x64/cryptxml.lib: skipped 19, total 19
um/x86/SearchSDK.lib: skipped 0, total 0
um/x64/cryptui.lib: skipped 54, total 54
um/x86/ScrnSavW.Lib: skipped 0, total 19
um/x86/ScrnSave.Lib: skipped 0, total 19
um/x64/CryptNet.Lib: skipped 5, total 5
um/x64/cryptdll.lib: skipped 20, total 20
um/x86/scesrv.lib: skipped 2, total 2
um/x86/scecli.lib: skipped 72, total 72
um/x86/schannel.lib: skipped 36, total 36
um/x64/Crypt32.Lib: skipped 240, total 240
um/x86/SCardDlg.Lib: skipped 5, total 5
um/x64/Credui.lib: skipped 22, total 22
um/x86/sbtsv.lib: skipped 0, total 1
um/x86/sas.lib: skipped 1, total 1
um/x64/corrEngine.lib: skipped 0, total 0
um/x64/CoreMessaging.lib: skipped 29, total 29
um/x86/SAPI.Lib: skipped 0, total 0
um/x86/samsrv.lib: skipped 328, total 328
um/x86/samlib.lib: skipped 70, total 70
um/x64/ComSvcs.Lib: skipped 17, total 17
um/x86/runtimeobject.lib: skipped 60, total 60
um/x86/RTWorkQ.lib: skipped 34, total 34
um/x86/rtutils.lib: skipped 41, total 41
um/x64/computestorage.lib: skipped 11, total 11
um/x86/Rtm.Lib: skipped 116, total 116
um/x86/rstrtmgr.lib: skipped 12, total 12
um/x64/computenetwork.lib: skipped 41, total 41
um/x86/rpcutil.lib: skipped 0, total 23
um/x86/RpcRT4.Lib: skipped 536, total 536
um/x86/rpcproxy.lib: skipped 5, total 5
um/x64/computecore.lib: skipped 47, total 47
um/x86/Rpcns4.Lib: skipped 62, total 62
um/x64/compstui.lib: skipped 4, total 4
um/x86/rpcexts.lib: skipped 58, total 58
um/x64/CompPkgSup.lib: skipped 9, total 9
um/x86/rometadata.lib: skipped 1, total 1
um/x64/ComDlg32.Lib: skipped 21, total 21
um/x86/resutils.lib: skipped 126, total 126
um/x64/ComCtl32.Lib: skipped 128, total 128
um/x64/ClusApi.Lib: skipped 284, total 284
um/x64/clfsw32.lib: skipped 63, total 63
um/x86/rasuser.lib: skipped 5, total 5
um/x86/RASDlg.Lib: skipped 25, total 25
um/x64/clfsmgmt.lib: skipped 9, total 231
um/x86/RASAPI32.Lib: skipped 148, total 148
um/x64/cldapi.lib: skipped 48, total 48
um/x64/cfgmgr32.lib: skipped 231, total 231
um/x86/qwave.lib: skipped 14, total 14
um/x64/CertPolEng.Lib: skipped 14, total 14
um/x86/query.lib: skipped 6, total 6
um/x86/quartz.lib: skipped 4, total 4
um/x64/Chakrart.lib: skipped 155, total 155
um/x86/Psapi.Lib: skipped 27, total 27
um/x64/CertIdl.Lib: skipped 0, total 1
um/x64/certcli.lib: skipped 0, total 0
um/x86/ProjectedFSLib.lib: skipped 33, total 33
um/x64/certca.lib: skipped 0, total 0
um/x86/propsys.lib: skipped 219, total 219
um/x86/prntvpt.lib: skipped 29, total 29
um/x64/certadm.lib: skipped 41, total 41
um/x64/Cabinet.Lib: skipped 26, total 26
um/x86/powrprof.lib: skipped 109, total 109
um/x86/PortableDeviceGuids.lib: skipped 0, total 0
um/x86/PhotoAcquireUID.lib: skipped 0, total 0
um/x86/PeerDist.lib: skipped 28, total 28
um/x86/Pdh.Lib: skipped 110, total 110
um/x64/BufferOverflowU.lib: skipped 9, total 24
um/x64/BufferOverflow.lib: skipped 11, total 28
um/x86/pathcch.lib: skipped 22, total 22
um/x64/BluetoothApis.lib: skipped 96, total 96
um/x86/patchwiz.lib: skipped 4, total 4
um/x64/bthprops.lib: skipped 40, total 40
um/x86/p2pgraph.lib: skipped 40, total 40
um/x86/p2p.lib: skipped 112, total 112
um/x64/Bits.Lib: skipped 0, total 0
um/x64/bcrypt.lib: skipped 54, total 54
um/x86/osptk.lib: skipped 0, total 0
um/x86/OpenGL32.Lib: skipped 368, total 368
um/x64/avrt.lib: skipped 20, total 20
um/x64/basesrv.lib: skipped 6, total 6
um/x86/OneCore_downlevel.Lib: skipped 4787, total 4790
um/x86/OneCore_apiset.Lib: skipped 5176, total 5176
um/x64/aux_ulib.lib: skipped 1, total 5
um/x64/AuthZ.Lib: skipped 36, total 36
um/x86/OneCoreUAP_downlevel.Lib: skipped 4787, total 4790
um/x64/avifil32.Lib: skipped 74, total 74
um/x64/audiomediatypecrt.lib: skipped 2, total 27
um/x86/OneCoreUAP.Lib: skipped 11458, total 11461
um/x86/OneCoreUAP_apiset.Lib: skipped 9219, total 9219
um/x64/AudioBaseProcessingObjectV140.lib: skipped 15, total 68
um/x64/audioeng.lib: skipped 2, total 2
um/x86/OneCore.Lib: skipped 7511, total 7514
um/x64/audiobaseprocessingobject.lib: skipped 15, total 65
um/x64/appnotify.lib: skipped 4, total 4
um/x86/ondemandconnroutehelper.lib: skipped 8, total 8
um/x86/olesvr32.lib: skipped 23, total 23
um/x64/appmgr.lib: skipped 0, total 0
um/x86/OlePro32.Lib: skipped 7, total 7
um/x64/appmgmts.lib: skipped 17, total 17
um/x86/OleDlg.Lib: skipped 23, total 23
um/x86/oledb.lib: skipped 0, total 0
um/x86/OleAut32.Lib: skipped 400, total 400
um/x86/olecli32.lib: skipped 178, total 178
um/x86/OleAcc.Lib: skipped 20, total 20
um/x86/Ole32.Lib: skipped 432, total 432
um/x86/OemLicense.lib: skipped 6, total 6
um/x64/api-ms-win-net-isolation-l1-1-0.lib: skipped 8, total 8
um/x86/odbcbcp.lib: skipped 28, total 28
um/x86/odbccp32.lib: skipped 0, total 56
um/x86/odbc32.lib: skipped 176, total 176
um/x64/amsi.lib: skipped 9, total 9
um/x86/objsel.lib: skipped 0, total 0
um/x64/amstrmid.lib: skipped 0, total 0
um/x64/ahadmin.lib: skipped 0, total 0
um/x86/ntvdm.lib: skipped 164, total 164
um/x64/advpack.Lib: skipped 84, total 84
um/x64/AdvAPI32.Lib: skipped 782, total 782
um/x86/ntstc_msvcrt.lib: skipped 357, total 6280
um/x64/ADSIid.Lib: skipped 0, total 0
um/x64/ActiveDS.Lib: skipped 27, total 27
um/x86/ntstc_libcmt.lib: skipped 357, total 6280
um/x86/NtQuery.Lib: skipped 6, total 6
um/x64/AclUI.Lib: skipped 6, total 6
um/x86/ntmarta.lib: skipped 44, total 44
um/x86/ntlanman.lib: skipped 23, total 23
um/x86/ntfrsapi.lib: skipped 33, total 33
um/x86/ntdsetup.lib: skipped 24, total 24
um/x86/ntdsa.lib: skipped 146, total 146
um/x86/NtDsAPI.Lib: skipped 120, total 120
um/x86/ntdsatq.lib: skipped 47, total 47
um/x86/ntdll.lib: skipped 2053, total 2053
um/x86/nt.lib: skipped 0, total 6
um/x86/ninput.lib: skipped 23, total 23
um/x86/normaliz.lib: skipped 5, total 5
um/x86/newdev.lib: skipped 23, total 23
um/x86/netlib.lib: skipped 1, total 269
um/x86/NetSh.Lib: skipped 23, total 23
um/x86/ndproxystub.lib: skipped 0, total 0
um/x86/NetAPI32.Lib: skipped 212, total 212
um/x86/ndfapi.lib: skipped 24, total 24
um/x86/nddeapi.lib: skipped 28, total 28
um/x86/ncrypt.lib: skipped 136, total 136
um/x86/mtxdm.lib: skipped 1, total 1
um/x86/muiload.lib: skipped 0, total 64
um/x86/Mtx.Lib: skipped 3, total 3
um/x86/msxml6.lib: skipped 0, total 0
um/x86/MsXml2.Lib: skipped 0, total 0
um/x86/msvfw32.Lib: skipped 47, total 47
um/x86/msv1_0.lib: skipped 19, total 19
um/x86/MSTask.Lib: skipped 22, total 22
um/x86/MsWSock.Lib: skipped 28, total 28
um/x86/MSRating.Lib: skipped 32, total 32
um/x86/msports.lib: skipped 11, total 11
um/x86/mspatcha.lib: skipped 16, total 16
um/x86/mspbase.lib: skipped 163, total 1420
um/x86/MSImg32.Lib: skipped 3, total 3
um/x86/mspatchc.lib: skipped 14, total 14
um/x86/Msi.Lib: skipped 290, total 290
um/x86/msdrm.lib: skipped 85, total 85
um/x86/msdelta.lib: skipped 15, total 15
um/x86/msdmo.lib: skipped 15, total 15
um/x86/MsCtfMonitor.lib: skipped 3, total 3
um/x86/Mscms.Lib: skipped 129, total 129
um/x86/msdasc.lib: skipped 0, total 0
um/x86/MSAJApi.lib: skipped 558, total 558
um/x86/MSAcm32.Lib: skipped 44, total 44
um/x86/MrmSupport.lib: skipped 24, total 24
um/x86/msaatext.lib: skipped 0, total 0
um/x86/MqRt.Lib: skipped 47, total 47
um/x86/MqOA.Lib: skipped 0, total 0
um/x86/mprsnap.lib: skipped 46, total 46
um/x86/Mprapi.Lib: skipped 160, total 160
um/x86/Mpr.Lib: skipped 43, total 43
um/x86/mmdevapi.lib: skipped 29, total 29
um/x86/mincore_downlevel.lib: skipped 451, total 451
um/x86/MMC.Lib: skipped 13, total 94
um/x86/mincore.lib: skipped 4386, total 4386
um/x86/mi.lib: skipped 2, total 2
um/x86/mfuuid.lib: skipped 0, total 0
um/x86/Mfsrcsnk.lib: skipped 2, total 2
um/x86/MgmtAPI.Lib: skipped 9, total 9
um/x86/mfsensorgroup.lib: skipped 5, total 5
um/x86/mfreadwrite.lib: skipped 5, total 5
um/x86/Mfcore.lib: skipped 38, total 38
um/x86/mfplay.lib: skipped 1, total 1
um/x86/Mfplat.lib: skipped 150, total 150
um/x86/Mf.lib: skipped 75, total 75
um/x86/MDMRegistration.lib: skipped 13, total 13
um/x86/mciole32.lib: skipped 11, total 11
um/x86/mdmlocalmanagement.lib: skipped 3, total 3
um/x86/mbnapi_uuid.lib: skipped 0, total 0
um/x86/MAPI32.Lib: skipped 155, total 155
um/x86/magnification.lib: skipped 21, total 21
um/x86/Lz32.Lib: skipped 14, total 14
um/x86/ktmw32.lib: skipped 44, total 44
um/x86/LoadPerf.Lib: skipped 14, total 14
um/x86/ksuser.lib: skipped 8, total 8
um/x86/locationapi.lib: skipped 0, total 0
um/x86/keycredmgr.lib: skipped 4, total 4
um/x86/KSProxy.Lib: skipped 6, total 6
um/x86/kernel32legacylib.lib: skipped 5, total 541
um/x86/kernel32.Lib: skipped 1317, total 1317
um/x86/kerbcli.lib: skipped 0, total 3
um/x86/jetoledb.lib: skipped 0, total 0
um/x86/jsrt.lib: skipped 92, total 92
um/x86/iscsidsc.lib: skipped 80, total 80
um/x86/irprops.lib: skipped 35, total 35
um/x86/Iprop.Lib: skipped 8, total 8
um/x86/int64.lib: skipped 0, total 11
um/x86/iphlpapi.lib: skipped 290, total 290
um/x86/inseng.lib: skipped 7, total 7
um/x86/infocardapi.Lib: skipped 18, total 18
um/x86/inkobjcore.lib: skipped 30, total 30
um/x86/imgutil.Lib: skipped 9, total 9
um/x86/Imm32.Lib: skipped 82, total 82
um/x86/ImageHlp.Lib: skipped 152, total 152
um/x86/iesetup.lib: skipped 7, total 7
um/x86/IEPMAPI.Lib: skipped 0, total 24
um/x86/icuuc.lib: skipped 542, total 542
um/x86/icuin.Lib: skipped 416, total 416
um/x86/icu.lib: skipped 958, total 958
um/x86/Icmui.Lib: skipped 2, total 2
um/x86/Icm32.Lib: skipped 21, total 21
um/x86/iashlpr.lib: skipped 12, total 12
um/x86/httpapi.lib: skipped 46, total 46
um/x86/Htmlhelp.Lib: skipped 0, total 6
um/x86/hrtfapo.lib: skipped 4, total 4
um/x86/HLink.Lib: skipped 28, total 28
um/x86/hid.lib: skipped 44, total 44
um/x86/hbaapi.lib: skipped 93, total 93
um/x86/hhsetup.lib: skipped 145, total 145
um/x86/gpmuuid.lib: skipped 0, total 0
um/x86/GPEdit.lib: skipped 10, total 10
um/x86/GlU32.Lib: skipped 52, total 52
um/x86/gdiplus.lib: skipped 630, total 630
um/x86/glmf32.lib: skipped 134, total 134
um/x86/Gdi32.Lib: skipped 605, total 605
um/x86/fxsutility.lib: skipped 2, total 2
um/x86/fwpuclnt.lib: skipped 276, total 276
um/x86/FrameDyn.Lib: skipped 604, total 604
um/x86/FrameDyd.Lib: skipped 604, total 604
um/x86/fontsub.lib: skipped 2, total 2
um/x86/fltLib.lib: skipped 29, total 29
um/x86/FhSvcCtl.lib: skipped 14, total 14
um/x86/fileextd.lib: skipped 1, total 22
um/x86/feclient.lib: skipped 54, total 54
um/x86/FaultRep.Lib: skipped 16, total 16
um/x86/evr.lib: skipped 9, total 9
um/x86/ElsCore.lib: skipped 5, total 5
um/x86/esent.lib: skipped 375, total 375
um/x86/els.lib: skipped 0, total 0
um/x86/elfapi.lib: skipped 0, total 101
um/x86/ehstorguids.lib: skipped 0, total 0
um/x86/efswrt.lib: skipped 27, total 27
um/x86/easregprov.lib: skipped 2, total 2
um/x86/eappprxy.lib: skipped 18, total 18
um/x86/dxva2.lib: skipped 38, total 38
um/x86/eappcfg.lib: skipped 15, total 15
um/x86/dxtmsft.lib: skipped 0, total 0
um/x86/dxtrans.lib: skipped 6, total 6
um/x86/dxgi.lib: skipped 15, total 15
um/x86/dxguid.lib: skipped 0, total 0
um/x86/dxcompiler.lib: skipped 2, total 2
um/x86/dwrite.lib: skipped 1, total 1
um/x86/DtcHelp.Lib: skipped 2, total 18
um/x86/dwmapi.lib: skipped 31, total 31
um/x86/DSUIExt.Lib: skipped 33, total 33
um/x86/DSProp.Lib: skipped 19, total 19
um/x86/dststlog.lib: skipped 1, total 1
um/x86/dssec.lib: skipped 4, total 4
um/x86/dsound.lib: skipped 10, total 10
um/x86/drttransport.lib: skipped 2, total 2
um/x86/drtprov.lib: skipped 9, total 9
um/x86/drt.lib: skipped 21, total 21
um/x86/dpx.lib: skipped 11, total 11
um/x86/dnsrslvr.lib: skipped 4, total 4
um/x86/dnsrpc.lib: skipped 0, total 374
um/x86/dnsperf.lib: skipped 3, total 3
um/x86/dnscrcli.lib: skipped 0, total 4
um/x86/dnslib.lib: skipped 1, total 1395
um/x86/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x86/DnsAPI.Lib: skipped 288, total 288
um/x86/dmoguids.lib: skipped 0, total 0
um/x86/dloadhelper.lib: skipped 0, total 3
um/x86/directml.lib: skipped 1, total 1
um/x86/dinput8.lib: skipped 1, total 2
um/x86/DhcpCSvc6.Lib: skipped 22, total 22
um/x86/DhcpCSvc.Lib: skipped 68, total 68
um/x86/dhcpsapi.lib: skipped 209, total 209
um/x86/dflayout.lib: skipped 1, total 1
um/x86/deviceaccess.lib: skipped 3, total 3
um/x86/devmgr.lib: skipped 19, total 19
um/x86/devenum.lib: skipped 0, total 0
um/x86/dciman32.lib: skipped 20, total 20
um/x86/dcomp.lib: skipped 6, total 6
um/x86/ddraw.lib: skipped 13, total 13
um/x86/DbgModel.Lib: skipped 1, total 1
um/x86/DbgHelp.Lib: skipped 239, total 239
um/x86/DbgEng.Lib: skipped 4, total 4
um/x86/davclnt.lib: skipped 22, total 22
um/x86/d3dcsxd.lib: skipped 9, total 9
um/x86/d3dcsx.lib: skipped 9, total 9
um/x86/d3d9.lib: skipped 14, total 14
um/x86/d3dcompiler.lib: skipped 29, total 29
um/x86/d3d12.lib: skipped 14, total 14
um/x86/d3d10.lib: skipped 29, total 29
um/x86/d3d11.lib: skipped 45, total 45
um/x86/d3d10_1.lib: skipped 29, total 29
um/x86/d2d1.lib: skipped 13, total 13
um/x86/cscapi.lib: skipped 6, total 6
um/x86/cscdll.lib: skipped 18, total 18
um/x86/cryptui.lib: skipped 54, total 54
um/x86/cryptxml.lib: skipped 19, total 19
um/x86/CryptNet.Lib: skipped 5, total 5
um/x86/Crypt32.Lib: skipped 240, total 240
um/x86/cryptdll.lib: skipped 20, total 20
um/x86/Credui.lib: skipped 22, total 22
um/x86/corrEngine.lib: skipped 0, total 0
um/x86/CoreMessaging.lib: skipped 29, total 29
um/x86/ComSvcs.Lib: skipped 17, total 17
um/x86/CompPkgSup.lib: skipped 9, total 9
um/x86/compstui.lib: skipped 4, total 4
um/x86/ComDlg32.Lib: skipped 21, total 21
um/x86/ComCtl32.Lib: skipped 128, total 128
um/x86/ClusApi.Lib: skipped 284, total 284
um/x86/cldapi.lib: skipped 48, total 48
um/x86/clfsmgmt.lib: skipped 7, total 212
um/x86/clfsw32.lib: skipped 63, total 63
um/x86/Chakrart.lib: skipped 155, total 155
um/x86/cfgmgr32.lib: skipped 231, total 231
um/x86/CertPolEng.Lib: skipped 14, total 14
um/x86/CertIdl.Lib: skipped 0, total 1
um/x86/certcli.lib: skipped 0, total 0
um/x86/certca.lib: skipped 0, total 0
um/x86/certadm.lib: skipped 41, total 41
um/x86/Cabinet.Lib: skipped 26, total 26
um/x86/BufferOverflow.lib: skipped 2, total 25
um/x86/BufferOverflowU.lib: skipped 2, total 19
um/x86/bthprops.lib: skipped 40, total 40
um/x86/BluetoothApis.lib: skipped 96, total 96
um/x86/bcrypt.lib: skipped 54, total 54
um/x86/Bits.Lib: skipped 0, total 0
um/x86/basesrv.lib: skipped 6, total 6
um/x86/avrt.lib: skipped 20, total 20
um/x86/avifil32.Lib: skipped 74, total 74
um/x86/aux_ulib.lib: skipped 0, total 4
um/x86/AuthZ.Lib: skipped 36, total 36
um/x86/AudioBaseProcessingObjectV140.lib: skipped 12, total 68
um/x86/audioeng.lib: skipped 2, total 2
um/x86/audiomediatypecrt.lib: skipped 2, total 27
um/x86/audiobaseprocessingobject.lib: skipped 12, total 65
um/x86/ASycFilt.Lib: skipped 1, total 1
um/x86/appmgr.lib: skipped 0, total 0
um/x86/appnotify.lib: skipped 4, total 4
um/x86/appmgmts.lib: skipped 17, total 17
um/x86/apidll.lib: skipped 2, total 2
um/x86/amstrmid.lib: skipped 0, total 0
um/x86/amsi.lib: skipped 9, total 9
um/x86/advpack.Lib: skipped 84, total 84
um/x86/ahadmin.lib: skipped 0, total 0
um/x86/AdvAPI32.Lib: skipped 782, total 782
um/x86/api-ms-win-net-isolation-l1-1-0.lib: skipped 8, total 8
um/x86/ADSIid.Lib: skipped 0, total 0
um/x86/ActiveDS.Lib: skipped 27, total 27
um/x86/AclUI.Lib: skipped 6, total 6
ucrt/x64/ucrtd.lib: skipped 1414, total 1414
ucrt/x64/ucrt.lib: skipped 1351, total 1351
ucrt/x64/libucrtd.lib: skipped 138, total 8711
ucrt/x64/libucrt.lib: skipped 536, total 8538
```

### ucrt: 10.0.19041.0

```
um/x86/xpsprint.lib: skipped 4, total 4
um/x86/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x86/xolehlp.lib: skipped 8, total 8
um/x86/xmllite.lib: skipped 6, total 6
um/x86/xinputuap.lib: skipped 8, total 8
um/x86/Xinput9_1_0.lib: skipped 5, total 5
um/x86/xinput.lib: skipped 8, total 8
um/x86/xaudio2_8.lib: skipped 7, total 7
um/x86/xaudio2.lib: skipped 10, total 10
um/x86/xaswitch.lib: skipped 0, total 19
um/x86/xapobase2_8.lib: skipped 3, total 152
um/x86/xapobase.lib: skipped 3, total 152
um/x86/wuguid.lib: skipped 0, total 0
um/x86/WtsApi32.Lib: skipped 65, total 65
um/x86/WSock32.Lib: skipped 75, total 75
um/x86/WSnmp32.Lib: skipped 51, total 51
um/x86/wsmsvc.lib: skipped 3673, total 3673
um/x86/wsdapi.lib: skipped 45, total 45
um/x86/wsclient.lib: skipped 30, total 30
um/x86/wscapi.lib: skipped 39, total 39
um/x86/wsbonline.lib: skipped 3, total 3
um/x86/wsbapp_uuid.Lib: skipped 0, total 0
um/x86/WS2_32.Lib: skipped 180, total 180
um/x86/Wow32.Lib: skipped 29, total 29
um/x86/workspaceax.lib: skipped 0, total 3
um/x86/wofutil.lib: skipped 11, total 11
um/x86/wmvcore.lib: skipped 20, total 20
um/x86/wmiutils.lib: skipped 0, total 0
um/x86/wmip.lib: skipped 45, total 45
um/x86/wmcodecdspuuid.lib: skipped 0, total 0
um/x86/Wldp.Lib: skipped 21, total 21
um/x86/Wldap32.Lib: skipped 245, total 245
um/x86/wlanui.lib: skipped 5, total 5
um/x86/wlanapi.lib: skipped 68, total 68
um/x86/winusb.lib: skipped 37, total 37
um/x86/WinTrust.Lib: skipped 145, total 145
um/x86/WinStrm.Lib: skipped 0, total 18
um/x86/winsta.lib: skipped 175, total 175
um/x86/winsqlite3.lib: skipped 268, total 268
um/x86/WinSpool.Lib: skipped 232, total 232
um/x86/winscard.lib: skipped 74, total 74
um/x86/winsatapi.lib: skipped 0, total 0
um/x86/WinMM.Lib: skipped 191, total 191
um/x86/winml.lib: skipped 1, total 1
um/x86/WinInet.Lib: skipped 319, total 319
um/x86/winhttp.lib: skipped 66, total 66
um/x86/winfax.lib: skipped 56, total 56
um/x86/windowssideshowguids.lib: skipped 0, total 0
um/x86/windowscoreheadless_apiset.Lib: skipped 7018, total 7018
um/x86/windowscoreheadless.Lib: skipped 9388, total 9391
um/x86/windowscodecs.lib: skipped 114, total 114
um/x86/WindowsApp_downlevel.lib: skipped 4792, total 4792
um/x86/WindowsApp.lib: skipped 4801, total 4801
um/x86/windows.ui.lib: skipped 2, total 2
um/x86/windows.networking.lib: skipped 1, total 1
um/x86/windows.media.mediacontrol.lib: skipped 8, total 8
um/x86/windows.data.pdf.lib: skipped 1, total 1
um/x86/windows.ai.machinelearning.lib: skipped 1, total 1
um/x86/WinBio.lib: skipped 60, total 60
um/x86/wiautil.lib: skipped 3, total 128
um/x86/wiaservc.lib: skipped 55, total 55
um/x86/WiaGuid.Lib: skipped 0, total 0
um/x86/wevtapi.lib: skipped 45, total 45
um/x86/Wer.lib: skipped 145, total 145
um/x86/wecapi.lib: skipped 17, total 17
um/x86/websocket.lib: skipped 13, total 13
um/x86/WebServices.lib: skipped 193, total 193
um/x86/webauthn.lib: skipped 10, total 10
um/x86/wdstptc.lib: skipped 19, total 19
um/x86/wdspxe.lib: skipped 32, total 32
um/x86/wdsmc.lib: skipped 13, total 13
um/x86/wdsClientAPI.LIB: skipped 58, total 58
um/x86/wdsbp.lib: skipped 7, total 7
um/x86/wcmguid.lib: skipped 0, total 0
um/x86/wcmapi.lib: skipped 39, total 39
um/x86/wbemuuid.lib: skipped 0, total 0
um/x86/vstorinterface.lib: skipped 15, total 15
um/x86/vss_uuid.lib: skipped 0, total 0
um/x86/vssapi.lib: skipped 46, total 46
um/x86/vscmgr.lib: skipped 0, total 0
um/x86/Virtdisk.Lib: skipped 29, total 29
um/x86/Vfw32.Lib: skipped 127, total 127
um/x86/Version.Lib: skipped 12, total 12
um/x86/vds_uuid.lib: skipped 0, total 0
um/x86/VdmDbg.Lib: skipped 28, total 28
um/x86/vccomsup.lib: skipped 0, total 26
um/x86/Uxtheme.lib: skipped 78, total 78
um/x86/Uuid.Lib: skipped 37, total 37
um/x86/USP10.Lib: skipped 40, total 40
um/x86/UserEnv.Lib: skipped 73, total 73
um/x86/User32.Lib: skipped 779, total 779
um/x86/Urlmon.Lib: skipped 95, total 95
um/x86/unicows.lib: skipped 1010, total 2535
um/x86/umpdddi.lib: skipped 92, total 92
um/x86/UIAutomationCore.lib: skipped 99, total 99
um/x86/ualapi.lib: skipped 10, total 10
um/x86/txfw32.lib: skipped 9, total 9
um/x86/twinapi.lib: skipped 0, total 0
um/x86/twain_32.lib: skipped 5, total 5
um/x86/tspubplugincom.lib: skipped 1, total 8
um/x86/tsec.lib: skipped 27, total 27
um/x86/TranscodeImageUID.lib: skipped 0, total 0
um/x86/tokenbinding.lib: skipped 10, total 10
um/x86/Thunk32.Lib: skipped 66, total 66
um/x86/tdh.lib: skipped 26, total 26
um/x86/tbs.lib: skipped 21, total 21
um/x86/taskschd.lib: skipped 0, total 0
um/x86/tapi32l.lib: skipped 0, total 250
um/x86/Tapi32.Lib: skipped 278, total 278
um/x86/t2embed.lib: skipped 14, total 14
um/x86/synchronization.lib: skipped 3, total 3
um/x86/swdevice.lib: skipped 9, total 9
um/x86/Svcguid.Lib: skipped 0, total 0
um/x86/structuredquery.lib: skipped 0, total 0
um/x86/strsafe.lib: skipped 0, total 22
um/x86/strmiids.lib: skipped 0, total 0
um/x86/strmbase.lib: skipped 155, total 1684
um/x86/Sti.Lib: skipped 16, total 16
um/x86/Traffic.Lib: skipped 22, total 22
um/x86/srpapi.lib: skipped 21, total 21
um/x86/ssdpapi.lib: skipped 29, total 29
um/x86/SrClient.lib: skipped 0, total 28
um/x86/spoolss.lib: skipped 206, total 206
um/x86/SpOrder.Lib: skipped 2, total 2
um/x86/SnmpAPI.Lib: skipped 38, total 38
um/x86/slwga.lib: skipped 1, total 1
um/x86/slcext.lib: skipped 9, total 9
um/x86/slc.lib: skipped 40, total 40
um/x86/ShFolder.Lib: skipped 2, total 2
um/x86/ShLwApi.Lib: skipped 365, total 365
um/x86/shell32.lib: skipped 391, total 391
um/x86/shcore.lib: skipped 20, total 20
um/x86/shdocvw.lib: skipped 19, total 19
um/x86/Sfc.Lib: skipped 16, total 16
um/x86/SensorsUtils.lib: skipped 62, total 62
um/x86/SetupAPI.Lib: skipped 558, total 558
um/x86/sensorsapi.lib: skipped 0, total 0
um/x86/SensAPI.Lib: skipped 3, total 3
um/x86/sens.lib: skipped 3, total 3
um/x86/security.lib: skipped 36, total 36
um/x86/Secur32.Lib: skipped 96, total 96
um/x86/SearchSDK.lib: skipped 0, total 0
um/x86/ScrnSavW.Lib: skipped 0, total 19
um/x86/ScrnSave.Lib: skipped 0, total 19
um/x86/schannel.lib: skipped 36, total 36
um/x86/scesrv.lib: skipped 2, total 2
um/x86/scecli.lib: skipped 72, total 72
um/x86/SCardDlg.Lib: skipped 5, total 5
um/x86/sbtsv.lib: skipped 0, total 1
um/x86/sas.lib: skipped 1, total 1
um/x86/SAPI.Lib: skipped 0, total 0
um/x86/samsrv.lib: skipped 328, total 328
um/x86/samlib.lib: skipped 70, total 70
um/x86/RTWorkQ.lib: skipped 34, total 34
um/x86/runtimeobject.lib: skipped 60, total 60
um/x86/rtutils.lib: skipped 41, total 41
um/x86/Rtm.Lib: skipped 116, total 116
um/x86/rstrtmgr.lib: skipped 12, total 12
um/x86/rpcutil.lib: skipped 0, total 23
um/x86/RpcRT4.Lib: skipped 536, total 536
um/x86/rpcproxy.lib: skipped 5, total 5
um/x86/Rpcns4.Lib: skipped 62, total 62
um/x86/rpcexts.lib: skipped 58, total 58
um/x86/rometadata.lib: skipped 1, total 1
um/x86/resutils.lib: skipped 127, total 127
um/x86/rasuser.lib: skipped 5, total 5
um/x86/RASDlg.Lib: skipped 25, total 25
um/x86/RASAPI32.Lib: skipped 149, total 149
um/x86/qwave.lib: skipped 14, total 14
um/x86/query.lib: skipped 6, total 6
um/x86/quartz.lib: skipped 4, total 4
um/x86/Psapi.Lib: skipped 27, total 27
um/x86/propsys.lib: skipped 219, total 219
um/x86/prntvpt.lib: skipped 29, total 29
um/x86/powrprof.lib: skipped 109, total 109
um/x86/ProjectedFSLib.lib: skipped 35, total 35
um/x86/PortableDeviceGuids.lib: skipped 0, total 0
um/x86/PhotoAcquireUID.lib: skipped 0, total 0
um/x86/PeerDist.lib: skipped 28, total 28
um/x86/Pdh.Lib: skipped 110, total 110
um/x86/pathcch.lib: skipped 22, total 22
um/x86/patchwiz.lib: skipped 4, total 4
um/x86/p2pgraph.lib: skipped 40, total 40
um/x86/p2p.lib: skipped 112, total 112
um/x86/OpenGL32.Lib: skipped 368, total 368
um/x86/osptk.lib: skipped 0, total 0
um/x86/OneCore_downlevel.Lib: skipped 4785, total 4788
um/x86/OneCoreUAP_downlevel.Lib: skipped 4785, total 4788
um/x86/OneCore_apiset.Lib: skipped 5342, total 5342
um/x86/OneCoreUAP_apiset.Lib: skipped 9320, total 9320
um/x86/OneCoreUAP.Lib: skipped 11567, total 11570
um/x86/OneCore.Lib: skipped 7795, total 7798
um/x86/ondemandconnroutehelper.lib: skipped 8, total 8
um/x86/OlePro32.Lib: skipped 7, total 7
um/x86/olesvr32.lib: skipped 23, total 23
um/x86/OleDlg.Lib: skipped 23, total 23
um/x86/oledb.lib: skipped 0, total 0
um/x86/olecli32.lib: skipped 178, total 178
um/x86/OleAut32.Lib: skipped 400, total 400
um/x86/OleAcc.Lib: skipped 20, total 20
um/x86/Ole32.Lib: skipped 432, total 432
um/x86/OemLicense.lib: skipped 6, total 6
um/x86/odbccp32.lib: skipped 0, total 56
um/x86/odbcbcp.lib: skipped 28, total 28
um/x86/odbc32.lib: skipped 176, total 176
um/x86/objsel.lib: skipped 0, total 0
um/x86/ntvdm.lib: skipped 164, total 164
um/x86/ntstc_msvcrt.lib: skipped 357, total 6280
um/x86/ntstc_libcmt.lib: skipped 357, total 6280
um/x86/ntmarta.lib: skipped 44, total 44
um/x86/NtQuery.Lib: skipped 6, total 6
um/x86/ntlanman.lib: skipped 25, total 25
um/x86/ntfrsapi.lib: skipped 33, total 33
um/x86/ntdsetup.lib: skipped 24, total 24
um/x86/ntdsatq.lib: skipped 47, total 47
um/x86/ntdsa.lib: skipped 146, total 146
um/x86/NtDsAPI.Lib: skipped 120, total 120
um/x86/ntdll.lib: skipped 2088, total 2088
um/x86/nt.lib: skipped 0, total 6
um/x86/normaliz.lib: skipped 5, total 5
um/x86/ninput.lib: skipped 30, total 30
um/x86/newdev.lib: skipped 23, total 23
um/x86/NetSh.Lib: skipped 23, total 23
um/x86/netlib.lib: skipped 1, total 269
um/x86/NetAPI32.Lib: skipped 212, total 212
um/x86/ndproxystub.lib: skipped 0, total 0
um/x86/ndfapi.lib: skipped 24, total 24
um/x86/nddeapi.lib: skipped 28, total 28
um/x86/ncrypt.lib: skipped 140, total 140
um/x86/muiload.lib: skipped 0, total 64
um/x86/mtxdm.lib: skipped 1, total 1
um/x86/Mtx.Lib: skipped 3, total 3
um/x86/msxml6.lib: skipped 0, total 0
um/x86/MsXml2.Lib: skipped 0, total 0
um/x86/MsWSock.Lib: skipped 28, total 28
um/x86/msvfw32.Lib: skipped 47, total 47
um/x86/msv1_0.lib: skipped 19, total 19
um/x86/MSRating.Lib: skipped 32, total 32
um/x86/MSTask.Lib: skipped 22, total 22
um/x86/msports.lib: skipped 11, total 11
um/x86/mspbase.lib: skipped 163, total 1468
um/x86/mspatchc.lib: skipped 14, total 14
um/x86/mspatcha.lib: skipped 16, total 16
um/x86/MSImg32.Lib: skipped 3, total 3
um/x86/Msi.Lib: skipped 290, total 290
um/x86/msdrm.lib: skipped 85, total 85
um/x86/msdmo.lib: skipped 15, total 15
um/x86/msdelta.lib: skipped 15, total 15
um/x86/msdasc.lib: skipped 0, total 0
um/x86/MsCtfMonitor.lib: skipped 3, total 3
um/x86/Mscms.Lib: skipped 129, total 129
um/x86/MSAJApi.lib: skipped 558, total 558
um/x86/MSAcm32.Lib: skipped 44, total 44
um/x86/msaatext.lib: skipped 0, total 0
um/x86/MrmSupport.lib: skipped 24, total 24
um/x86/MqRt.Lib: skipped 47, total 47
um/x86/MqOA.Lib: skipped 0, total 0
um/x86/mprsnap.lib: skipped 46, total 46
um/x86/Mprapi.Lib: skipped 160, total 160
um/x86/Mpr.Lib: skipped 47, total 47
um/x86/mmdevapi.lib: skipped 31, total 31
um/x86/mincore_downlevel.lib: skipped 595, total 595
um/x86/MMC.Lib: skipped 13, total 94
um/x86/mincore.lib: skipped 4416, total 4416
um/x86/mi.lib: skipped 2, total 2
um/x86/MgmtAPI.Lib: skipped 9, total 9
um/x86/Mfsrcsnk.lib: skipped 2, total 2
um/x86/mfuuid.lib: skipped 0, total 0
um/x86/mfsensorgroup.lib: skipped 6, total 6
um/x86/mfreadwrite.lib: skipped 5, total 5
um/x86/mfplay.lib: skipped 1, total 1
um/x86/Mfplat.lib: skipped 152, total 152
um/x86/Mfcore.lib: skipped 39, total 39
um/x86/Mf.lib: skipped 76, total 76
um/x86/mdmlocalmanagement.lib: skipped 3, total 3
um/x86/mciole32.lib: skipped 11, total 11
um/x86/mbnapi_uuid.lib: skipped 0, total 0
um/x86/MAPI32.Lib: skipped 155, total 155
um/x86/MDMRegistration.lib: skipped 16, total 16
um/x86/magnification.lib: skipped 21, total 21
um/x86/locationapi.lib: skipped 0, total 0
um/x86/Lz32.Lib: skipped 14, total 14
um/x86/LoadPerf.Lib: skipped 14, total 14
um/x86/ktmw32.lib: skipped 44, total 44
um/x86/ksuser.lib: skipped 8, total 8
um/x86/keycredmgr.lib: skipped 4, total 4
um/x86/KSProxy.Lib: skipped 6, total 6
um/x86/kernel32legacylib.lib: skipped 5, total 543
um/x86/kernel32.Lib: skipped 1321, total 1321
um/x86/kerbcli.lib: skipped 0, total 3
um/x86/jsrt.lib: skipped 92, total 92
um/x86/IsolatedWindowsEnvironmentUtils.lib: skipped 1, total 1
um/x86/jetoledb.lib: skipped 0, total 0
um/x86/iscsidsc.lib: skipped 80, total 80
um/x86/Iprop.Lib: skipped 8, total 8
um/x86/iphlpapi.lib: skipped 294, total 294
um/x86/int64.lib: skipped 0, total 11
um/x86/inseng.lib: skipped 7, total 7
um/x86/inkobjcore.lib: skipped 30, total 30
um/x86/infocardapi.Lib: skipped 18, total 18
um/x86/Imm32.Lib: skipped 82, total 82
um/x86/imgutil.Lib: skipped 9, total 9
um/x86/ImageHlp.Lib: skipped 152, total 152
um/x86/iesetup.lib: skipped 7, total 7
um/x86/IEPMAPI.Lib: skipped 0, total 24
um/x86/icuuc.lib: skipped 542, total 542
um/x86/icuin.Lib: skipped 416, total 416
um/x86/icu.lib: skipped 969, total 969
um/x86/Icmui.Lib: skipped 2, total 2
um/x86/Icm32.Lib: skipped 21, total 21
um/x86/iashlpr.lib: skipped 12, total 12
um/x86/httpapi.lib: skipped 46, total 46
um/x86/Htmlhelp.Lib: skipped 0, total 6
um/x86/hrtfapo.lib: skipped 5, total 5
um/x86/HLink.Lib: skipped 28, total 28
um/x86/hhsetup.lib: skipped 145, total 145
um/x86/hbaapi.lib: skipped 93, total 93
um/x86/hid.lib: skipped 44, total 44
um/x86/gpmuuid.lib: skipped 0, total 0
um/x86/GPEdit.lib: skipped 10, total 10
um/x86/GlU32.Lib: skipped 52, total 52
um/x86/glmf32.lib: skipped 134, total 134
um/x86/gdiplus.lib: skipped 630, total 630
um/x86/Gdi32.Lib: skipped 605, total 605
um/x86/fxsutility.lib: skipped 2, total 2
um/x86/FrameDyn.Lib: skipped 604, total 604
um/x86/fwpuclnt.lib: skipped 276, total 276
um/x86/FrameDyd.Lib: skipped 604, total 604
um/x86/fontsub.lib: skipped 2, total 2
um/x86/fltLib.lib: skipped 29, total 29
um/x86/fileextd.lib: skipped 1, total 22
um/x86/FhSvcCtl.lib: skipped 14, total 14
um/x86/feclient.lib: skipped 54, total 54
um/x86/evr.lib: skipped 9, total 9
um/x86/esent.lib: skipped 375, total 375
um/x86/ElsCore.lib: skipped 5, total 5
um/x86/els.lib: skipped 0, total 0
um/x86/elfapi.lib: skipped 0, total 101
um/x86/ehstorguids.lib: skipped 0, total 0
um/x86/efswrt.lib: skipped 28, total 28
um/x86/easregprov.lib: skipped 2, total 2
um/x86/eappprxy.lib: skipped 18, total 18
um/x86/eappcfg.lib: skipped 15, total 15
um/x86/dxva2.lib: skipped 38, total 38
um/x86/dxtrans.lib: skipped 6, total 6
um/x86/dxtmsft.lib: skipped 0, total 0
um/x86/dxguid.lib: skipped 0, total 0
um/x86/dxgi.lib: skipped 15, total 15
um/x86/dxcore.lib: skipped 1, total 1
um/x86/dxcompiler.lib: skipped 2, total 2
um/x86/dwrite.lib: skipped 1, total 1
um/x86/dwmapi.lib: skipped 31, total 31
um/x86/DtcHelp.Lib: skipped 2, total 18
um/x86/DSUIExt.Lib: skipped 33, total 33
um/x86/dssec.lib: skipped 4, total 4
um/x86/dststlog.lib: skipped 1, total 1
um/x86/DSProp.Lib: skipped 19, total 19
um/x86/dsound.lib: skipped 10, total 10
um/x86/drttransport.lib: skipped 2, total 2
um/x86/drtprov.lib: skipped 9, total 9
um/x86/drt.lib: skipped 21, total 21
um/x86/dpx.lib: skipped 11, total 11
um/x86/dnsrslvr.lib: skipped 4, total 4
um/x86/dnsrpc.lib: skipped 0, total 474
um/x86/dnsperf.lib: skipped 3, total 3
um/x86/dnslib.lib: skipped 2, total 1128
um/x86/dnscrcli.lib: skipped 0, total 4
um/x86/DnsAPI.Lib: skipped 289, total 289
um/x86/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x86/dmoguids.lib: skipped 0, total 0
um/x86/dloadhelper.lib: skipped 0, total 3
um/x86/directml.lib: skipped 2, total 2
um/x86/dinput8.lib: skipped 1, total 2
um/x86/DiagnosticDataQuery.Lib: skipped 37, total 37
um/x86/dhcpsapi.lib: skipped 209, total 209
um/x86/FaultRep.Lib: skipped 16, total 16
um/x86/DhcpCSvc6.Lib: skipped 22, total 22
um/x86/DhcpCSvc.Lib: skipped 69, total 69
um/x86/devmgr.lib: skipped 19, total 19
um/x86/deviceaccess.lib: skipped 3, total 3
um/x86/devenum.lib: skipped 0, total 0
um/x86/ddraw.lib: skipped 13, total 13
um/x86/dcomp.lib: skipped 6, total 6
um/x86/dciman32.lib: skipped 20, total 20
um/x86/DbgModel.Lib: skipped 1, total 1
um/x86/dflayout.lib: skipped 1, total 1
um/x86/DbgHelp.Lib: skipped 239, total 239
um/x86/DbgEng.Lib: skipped 4, total 4
um/x86/davclnt.lib: skipped 22, total 22
um/x86/d3dcompiler.lib: skipped 29, total 29
um/x86/d3dcsx.lib: skipped 9, total 9
um/x86/d3d9.lib: skipped 16, total 16
um/x86/d3dcsxd.lib: skipped 9, total 9
um/x86/d3d12.lib: skipped 14, total 14
um/x86/d3d11.lib: skipped 9, total 9
um/x86/d3d10_1.lib: skipped 29, total 29
um/x86/d3d10.lib: skipped 29, total 29
um/x86/d2d1.lib: skipped 13, total 13
um/x86/cscdll.lib: skipped 18, total 18
um/x86/cscapi.lib: skipped 6, total 6
um/x86/cryptxml.lib: skipped 19, total 19
um/x86/CryptNet.Lib: skipped 5, total 5
um/x86/cryptdll.lib: skipped 20, total 20
um/x86/Crypt32.Lib: skipped 240, total 240
um/x86/Credui.lib: skipped 22, total 22
um/x86/cryptui.lib: skipped 54, total 54
um/x86/corrEngine.lib: skipped 0, total 0
um/x86/CoreMessaging.lib: skipped 30, total 30
um/x86/compstui.lib: skipped 4, total 4
um/x86/CompPkgSup.lib: skipped 9, total 9
um/x86/ComDlg32.Lib: skipped 21, total 21
um/x86/ComCtl32.Lib: skipped 128, total 128
um/x86/ComSvcs.Lib: skipped 17, total 17
um/x86/ClusApi.Lib: skipped 290, total 290
um/x86/clfsw32.lib: skipped 63, total 63
um/x86/cldapi.lib: skipped 48, total 48
um/x86/clfsmgmt.lib: skipped 7, total 221
um/x86/cimfs.lib: skipped 11, total 11
um/x86/Chakrart.lib: skipped 155, total 155
um/x86/CertPolEng.Lib: skipped 14, total 14
um/x86/CertIdl.Lib: skipped 0, total 1
um/x86/certcli.lib: skipped 0, total 0
um/x86/certca.lib: skipped 0, total 0
um/x86/cfgmgr32.lib: skipped 231, total 231
um/x86/certadm.lib: skipped 41, total 41
um/x86/Cabinet.Lib: skipped 26, total 26
um/x86/BufferOverflow.lib: skipped 2, total 25
um/x86/bthprops.lib: skipped 40, total 40
um/x86/BufferOverflowU.lib: skipped 2, total 19
um/x86/Bits.Lib: skipped 0, total 0
um/x86/BluetoothApis.lib: skipped 96, total 96
um/x86/basesrv.lib: skipped 6, total 6
um/x86/bcrypt.lib: skipped 54, total 54
um/x86/avifil32.Lib: skipped 74, total 74
um/x86/aux_ulib.lib: skipped 0, total 4
um/x86/AuthZ.Lib: skipped 36, total 36
um/x86/audioeng.lib: skipped 2, total 2
um/x86/audiomediatypecrt.lib: skipped 2, total 27
um/x86/avrt.lib: skipped 20, total 20
um/x86/AudioBaseProcessingObjectV140.lib: skipped 12, total 68
um/x86/audiobaseprocessingobject.lib: skipped 12, total 65
um/x86/ASycFilt.Lib: skipped 1, total 1
um/x86/appnotify.lib: skipped 4, total 4
um/x86/appmgr.lib: skipped 0, total 0
um/x86/appmgmts.lib: skipped 17, total 17
um/x86/apidll.lib: skipped 2, total 2
um/x86/amstrmid.lib: skipped 0, total 0
um/x86/ahadmin.lib: skipped 0, total 0
um/x86/advpack.Lib: skipped 84, total 84
um/x86/AdvAPI32.Lib: skipped 782, total 782
um/x86/ActiveDS.Lib: skipped 27, total 27
um/x86/ADSIid.Lib: skipped 0, total 0
um/x86/AclUI.Lib: skipped 6, total 6
um/x86/amsi.lib: skipped 9, total 9
ucrt/x86/ucrtd.lib: skipped 1441, total 1441
ucrt/x86/ucrt.lib: skipped 1377, total 1377
ucrt/x86/libucrt.lib: skipped 668, total 8721
ucrt/x86/libucrtd.lib: skipped 214, total 8898
ucrt/x64/ucrtd.lib: skipped 1414, total 1414
ucrt/x64/ucrt.lib: skipped 1350, total 1350
ucrt/x64/libucrt.lib: skipped 540, total 8835
ucrt/x64/libucrtd.lib: skipped 139, total 9010
um/x64/MgmtAPI.Lib: skipped 9, total 9
um/x64/Mpr.Lib: skipped 47, total 47
um/x64/MqOA.Lib: skipped 0, total 0
um/x64/MrmSupport.lib: skipped 24, total 24
um/x64/Mscms.Lib: skipped 129, total 129
um/x64/msdmo.lib: skipped 15, total 15
um/x64/MSRating.Lib: skipped 32, total 32
um/x64/ndfapi.lib: skipped 24, total 24
um/x64/NetAPI32.Lib: skipped 212, total 212
um/x64/ntdsetup.lib: skipped 24, total 24
um/x64/ntstc_msvcrt.lib: skipped 369, total 6624
um/x64/odbcbcp.lib: skipped 28, total 28
um/x64/OleAut32.Lib: skipped 412, total 412
um/x64/ondemandconnroutehelper.lib: skipped 8, total 8
um/x64/quartz.lib: skipped 4, total 4
um/x64/qwave.lib: skipped 14, total 14
um/x64/rpcutil.lib: skipped 0, total 23
um/x64/Rtm.Lib: skipped 116, total 116
um/x64/shell32.lib: skipped 391, total 391
um/x64/spoolss.lib: skipped 206, total 206
um/x64/SnmpAPI.Lib: skipped 38, total 38
um/x64/slwga.lib: skipped 1, total 1
um/x64/slcext.lib: skipped 9, total 9
um/x64/slc.lib: skipped 40, total 40
um/x64/SpOrder.Lib: skipped 2, total 2
um/x64/ShLwApi.Lib: skipped 365, total 365
um/x64/ShFolder.Lib: skipped 2, total 2
um/x64/SrClient.lib: skipped 0, total 28
um/x64/srpapi.lib: skipped 21, total 21
um/x64/ssdpapi.lib: skipped 29, total 29
um/x64/Sti.Lib: skipped 16, total 16
um/x64/strmbase.lib: skipped 135, total 1681
um/x64/strmiids.lib: skipped 0, total 0
um/x64/strsafe.lib: skipped 0, total 23
um/x64/structuredquery.lib: skipped 0, total 0
um/x64/Svcguid.Lib: skipped 0, total 0
um/x64/swdevice.lib: skipped 9, total 9
um/x64/t2embed.lib: skipped 14, total 14
um/x64/tapi32l.lib: skipped 0, total 250
um/x64/Tapi32.Lib: skipped 278, total 278
um/x64/taskschd.lib: skipped 0, total 0
um/x64/tbs.lib: skipped 21, total 21
um/x64/tdh.lib: skipped 26, total 26
um/x64/tokenbinding.lib: skipped 10, total 10
um/x64/Traffic.Lib: skipped 22, total 22
um/x64/tsec.lib: skipped 27, total 27
um/x64/tspubplugincom.lib: skipped 1, total 8
um/x64/TranscodeImageUID.lib: skipped 0, total 0
um/x64/synchronization.lib: skipped 3, total 3
um/x64/txfw32.lib: skipped 9, total 9
um/x64/User32.Lib: skipped 787, total 787
um/x64/USP10.Lib: skipped 40, total 40
um/x64/Uxtheme.lib: skipped 78, total 78
um/x64/vds_uuid.lib: skipped 0, total 0
um/x64/Version.Lib: skipped 12, total 12
um/x64/Vfw32.Lib: skipped 127, total 127
um/x64/vmdevicehost.lib: skipped 14, total 14
um/x64/wcmguid.lib: skipped 0, total 0
um/x64/wdspxe.lib: skipped 32, total 32
um/x64/wdstptc.lib: skipped 19, total 19
um/x64/WebServices.lib: skipped 193, total 193
um/x64/wecapi.lib: skipped 17, total 17
um/x64/wevtapi.lib: skipped 45, total 45
um/x64/WiaGuid.Lib: skipped 0, total 0
um/x64/vssapi.lib: skipped 46, total 46
um/x64/wiautil.lib: skipped 3, total 128
um/x64/WinBio.lib: skipped 60, total 60
um/x64/windows.media.mediacontrol.lib: skipped 8, total 8
um/x64/windows.ai.machinelearning.lib: skipped 1, total 1
um/x64/windows.ui.lib: skipped 2, total 2
um/x64/windows.networking.lib: skipped 1, total 1
um/x64/WindowsApp_downlevel.lib: skipped 4814, total 4814
um/x64/WindowsApp.lib: skipped 4823, total 4823
um/x64/windowscodecs.lib: skipped 114, total 114
um/x64/windowscoreheadless.Lib: skipped 9496, total 9499
um/x64/windowscoreheadless_apiset.Lib: skipped 7061, total 7061
um/x64/windowssideshowguids.lib: skipped 0, total 0
um/x64/winfax.lib: skipped 56, total 56
um/x64/winhttp.lib: skipped 66, total 66
um/x64/WinHvEmulation.lib: skipped 4, total 4
um/x64/windows.data.pdf.lib: skipped 1, total 1
um/x64/WinHvPlatform.lib: skipped 29, total 29
um/x64/WinInet.Lib: skipped 319, total 319
um/x64/winml.lib: skipped 1, total 1
um/x64/WinMM.Lib: skipped 179, total 179
um/x64/wiaservc.lib: skipped 55, total 55
um/x64/winsatapi.lib: skipped 0, total 0
um/x64/WinSpool.Lib: skipped 232, total 232
um/x64/winscard.lib: skipped 74, total 74
um/x64/Wer.lib: skipped 145, total 145
um/x64/websocket.lib: skipped 13, total 13
um/x64/winsta.lib: skipped 175, total 175
um/x64/winsqlite3.lib: skipped 268, total 268
um/x64/WinStrm.Lib: skipped 0, total 18
um/x64/WinTrust.Lib: skipped 145, total 145
um/x64/webauthn.lib: skipped 10, total 10
um/x64/wdsmc.lib: skipped 13, total 13
um/x64/wdsbp.lib: skipped 7, total 7
um/x64/winusb.lib: skipped 37, total 37
um/x64/wdsClientAPI.LIB: skipped 58, total 58
um/x64/wlanapi.lib: skipped 68, total 68
um/x64/wlanui.lib: skipped 5, total 5
um/x64/Wldap32.Lib: skipped 245, total 245
um/x64/Wldp.Lib: skipped 21, total 21
um/x64/wmip.lib: skipped 45, total 45
um/x64/wmcodecdspuuid.lib: skipped 0, total 0
um/x64/wmvcore.lib: skipped 20, total 20
um/x64/wmiutils.lib: skipped 0, total 0
um/x64/wnvapi.lib: skipped 2, total 2
um/x64/wofutil.lib: skipped 11, total 11
um/x64/workspaceax.lib: skipped 0, total 3
um/x64/WS2_32.Lib: skipped 195, total 195
um/x64/wsbapp_uuid.Lib: skipped 0, total 0
um/x64/wsbonline.lib: skipped 3, total 3
um/x64/wscapi.lib: skipped 39, total 39
um/x64/wsclient.lib: skipped 30, total 30
um/x64/wcmapi.lib: skipped 39, total 39
um/x64/wsdapi.lib: skipped 45, total 45
um/x64/wsmsvc.lib: skipped 3673, total 3673
um/x64/WSnmp32.Lib: skipped 51, total 51
um/x64/WSock32.Lib: skipped 75, total 75
um/x64/wuguid.lib: skipped 0, total 0
um/x64/WtsApi32.Lib: skipped 65, total 65
um/x64/xapobase2_8.lib: skipped 5, total 147
um/x64/xapobase.lib: skipped 5, total 147
um/x64/xaudio2.lib: skipped 10, total 10
um/x64/xaswitch.lib: skipped 0, total 17
um/x64/xaudio2_8.lib: skipped 7, total 7
um/x64/xinput.lib: skipped 8, total 8
um/x64/Xinput9_1_0.lib: skipped 5, total 5
um/x64/xinputuap.lib: skipped 8, total 8
um/x64/xmllite.lib: skipped 6, total 6
um/x64/wbemuuid.lib: skipped 0, total 0
um/x64/xolehlp.lib: skipped 8, total 8
um/x64/vstorinterface.lib: skipped 15, total 15
um/x64/xpsdocumenttargetprint.lib: skipped 2, total 2
um/x64/xpsprint.lib: skipped 4, total 4
um/x64/vss_uuid.lib: skipped 0, total 0
um/x64/vscmgr.lib: skipped 0, total 0
um/x64/vmsavedstatedumpprovider.lib: skipped 23, total 23
um/x64/Virtdisk.Lib: skipped 29, total 29
um/x64/vertdll.lib: skipped 94, total 97
um/x64/vccomsup.lib: skipped 0, total 26
um/x64/Uuid.Lib: skipped 37, total 37
um/x64/UserEnv.Lib: skipped 73, total 73
um/x64/Urlmon.Lib: skipped 95, total 95
um/x64/umpdddi.lib: skipped 92, total 92
um/x64/UIAutomationCore.lib: skipped 99, total 99
um/x64/ualapi.lib: skipped 10, total 10
um/x64/twinapi.lib: skipped 0, total 0
um/x64/shdocvw.lib: skipped 19, total 19
um/x64/shcore.lib: skipped 20, total 20
um/x64/Sfc.Lib: skipped 16, total 16
um/x64/SetupAPI.Lib: skipped 558, total 558
um/x64/SensorsUtils.lib: skipped 62, total 62
um/x64/sensorsapi.lib: skipped 0, total 0
um/x64/SensAPI.Lib: skipped 3, total 3
um/x64/sens.lib: skipped 3, total 3
um/x64/security.lib: skipped 36, total 36
um/x64/Secur32.Lib: skipped 96, total 96
um/x64/SearchSDK.lib: skipped 0, total 0
um/x64/ScrnSavW.Lib: skipped 0, total 20
um/x64/ScrnSave.Lib: skipped 0, total 20
um/x64/schannel.lib: skipped 36, total 36
um/x64/scesrv.lib: skipped 2, total 2
um/x64/scecli.lib: skipped 72, total 72
um/x64/SCardDlg.Lib: skipped 5, total 5
um/x64/sbtsv.lib: skipped 0, total 1
um/x64/sas.lib: skipped 1, total 1
um/x64/SAPI.Lib: skipped 0, total 0
um/x64/samsrv.lib: skipped 328, total 328
um/x64/samlib.lib: skipped 70, total 70
um/x64/runtimeobject.lib: skipped 64, total 64
um/x64/RTWorkQ.lib: skipped 34, total 34
um/x64/rtutils.lib: skipped 41, total 41
um/x64/rstrtmgr.lib: skipped 12, total 12
um/x64/RpcRT4.Lib: skipped 543, total 543
um/x64/rpcproxy.lib: skipped 5, total 5
um/x64/Rpcns4.Lib: skipped 62, total 62
um/x64/rpcexts.lib: skipped 58, total 58
um/x64/resutils.lib: skipped 127, total 127
um/x64/rometadata.lib: skipped 1, total 1
um/x64/rasuser.lib: skipped 5, total 5
um/x64/RASDlg.Lib: skipped 25, total 25
um/x64/RASAPI32.Lib: skipped 149, total 149
um/x64/query.lib: skipped 6, total 6
um/x64/Psapi.Lib: skipped 27, total 27
um/x64/propsys.lib: skipped 219, total 219
um/x64/ProjectedFSLib.lib: skipped 35, total 35
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
um/x64/OneCore_downlevel.Lib: skipped 4849, total 4852
um/x64/OneCore_apiset.Lib: skipped 5385, total 5385
um/x64/OneCoreUAP_downlevel.Lib: skipped 4849, total 4852
um/x64/OneCoreUAP_apiset.Lib: skipped 9363, total 9363
um/x64/OneCoreUAP.Lib: skipped 11675, total 11678
um/x64/OneCore.Lib: skipped 7903, total 7906
um/x64/olesvr32.lib: skipped 23, total 23
um/x64/OleDlg.Lib: skipped 23, total 23
um/x64/oledb.lib: skipped 0, total 0
um/x64/olecli32.lib: skipped 178, total 178
um/x64/OleAcc.Lib: skipped 20, total 20
um/x64/Ole32.Lib: skipped 504, total 504
um/x64/OemLicense.lib: skipped 6, total 6
um/x64/odbccp32.lib: skipped 0, total 56
um/x64/odbc32.lib: skipped 176, total 176
um/x64/objsel.lib: skipped 0, total 0
um/x64/ntstc_libcmt.lib: skipped 369, total 6624
um/x64/NtQuery.Lib: skipped 6, total 6
um/x64/ntmarta.lib: skipped 44, total 44
um/x64/ntlanman.lib: skipped 25, total 25
um/x64/ntfrsapi.lib: skipped 33, total 33
um/x64/ntdsatq.lib: skipped 47, total 47
um/x64/NtDsAPI.Lib: skipped 120, total 120
um/x64/ntdsa.lib: skipped 146, total 146
um/x64/ntdll.lib: skipped 2133, total 2133
um/x64/nt.lib: skipped 0, total 6
um/x64/normaliz.lib: skipped 5, total 5
um/x64/ninput.lib: skipped 30, total 30
um/x64/newdev.lib: skipped 23, total 23
um/x64/NetSh.Lib: skipped 23, total 23
um/x64/netlib.lib: skipped 3, total 269
um/x64/ndproxystub.lib: skipped 0, total 0
um/x64/nddeapi.lib: skipped 28, total 28
um/x64/ncrypt.lib: skipped 140, total 140
um/x64/nanosrv.lib: skipped 7100, total 7100
um/x64/muiload.lib: skipped 0, total 64
um/x64/mtxdm.lib: skipped 1, total 1
um/x64/Mtx.Lib: skipped 3, total 3
um/x64/msxml6.lib: skipped 0, total 0
um/x64/MsXml2.Lib: skipped 0, total 0
um/x64/MsWSock.Lib: skipped 28, total 28
um/x64/msvfw32.Lib: skipped 47, total 47
um/x64/msv1_0.lib: skipped 19, total 19
um/x64/MSTask.Lib: skipped 11, total 11
um/x64/msports.lib: skipped 11, total 11
um/x64/mspbase.lib: skipped 170, total 1415
um/x64/mspatchc.lib: skipped 14, total 14
um/x64/mspatcha.lib: skipped 16, total 16
um/x64/MSImg32.Lib: skipped 3, total 3
um/x64/Msi.Lib: skipped 290, total 290
um/x64/msdrm.lib: skipped 85, total 85
um/x64/msdelta.lib: skipped 15, total 15
um/x64/msdasc.lib: skipped 0, total 0
um/x64/MsCtfMonitor.lib: skipped 3, total 3
um/x64/MSAJApi.lib: skipped 558, total 558
um/x64/MSAcm32.Lib: skipped 42, total 42
um/x64/msaatext.lib: skipped 0, total 0
um/x64/MqRt.Lib: skipped 47, total 47
um/x64/mprsnap.lib: skipped 46, total 46
um/x64/Mprapi.Lib: skipped 160, total 160
um/x64/mmdevapi.lib: skipped 31, total 31
um/x64/MMC.Lib: skipped 11, total 94
um/x64/mincore_downlevel.lib: skipped 595, total 595
um/x64/mincore.lib: skipped 4459, total 4459
um/x64/mi.lib: skipped 2, total 2
um/x64/mfuuid.lib: skipped 0, total 0
um/x64/Mfsrcsnk.lib: skipped 2, total 2
um/x64/mfsensorgroup.lib: skipped 6, total 6
um/x64/mfreadwrite.lib: skipped 5, total 5
um/x64/mfplay.lib: skipped 1, total 1
um/x64/Mfplat.lib: skipped 152, total 152
um/x64/Mfcore.lib: skipped 39, total 39
um/x64/Mf.lib: skipped 76, total 76
um/x64/MDMRegistration.lib: skipped 16, total 16
um/x64/mdmlocalmanagement.lib: skipped 3, total 3
um/x64/mciole32.lib: skipped 11, total 11
um/x64/mbnapi_uuid.lib: skipped 0, total 0
um/x64/MAPI32.Lib: skipped 136, total 136
um/x64/magnification.lib: skipped 21, total 21
um/x64/Lz32.Lib: skipped 14, total 14
um/x64/locationapi.lib: skipped 0, total 0
um/x64/LoadPerf.Lib: skipped 14, total 14
um/x64/ktmw32.lib: skipped 44, total 44
um/x64/ksuser.lib: skipped 8, total 8
um/x64/KSProxy.Lib: skipped 6, total 6
um/x64/keycredmgr.lib: skipped 4, total 4
um/x64/kernel32legacylib.lib: skipped 9, total 601
um/x64/kernel32.Lib: skipped 1347, total 1347
um/x64/kerbcli.lib: skipped 0, total 3
um/x64/jsrt.lib: skipped 92, total 92
um/x64/IsolatedWindowsEnvironmentUtils.lib: skipped 1, total 1
um/x64/iscsidsc.lib: skipped 80, total 80
um/x64/Iprop.Lib: skipped 8, total 8
um/x64/iphlpapi.lib: skipped 294, total 294
um/x64/inseng.lib: skipped 7, total 7
um/x64/inkobjcore.lib: skipped 30, total 30
um/x64/infocardapi.Lib: skipped 18, total 18
um/x64/Imm32.Lib: skipped 82, total 82
um/x64/imgutil.Lib: skipped 9, total 9
um/x64/ImageHlp.Lib: skipped 149, total 149
um/x64/iesetup.lib: skipped 7, total 7
um/x64/IEPMAPI.Lib: skipped 0, total 24
um/x64/icuuc.lib: skipped 542, total 542
um/x64/icuin.Lib: skipped 416, total 416
um/x64/icu.lib: skipped 969, total 969
um/x64/Icmui.Lib: skipped 2, total 2
um/x64/Icm32.Lib: skipped 21, total 21
um/x64/iashlpr.lib: skipped 12, total 12
um/x64/httpapi.lib: skipped 46, total 46
um/x64/Htmlhelp.Lib: skipped 0, total 6
um/x64/hrtfapo.lib: skipped 5, total 5
um/x64/hid.lib: skipped 44, total 44
um/x64/HLink.Lib: skipped 28, total 28
um/x64/hhsetup.lib: skipped 145, total 145
um/x64/gpmuuid.lib: skipped 0, total 0
um/x64/hbaapi.lib: skipped 93, total 93
um/x64/GPEdit.lib: skipped 10, total 10
um/x64/GlU32.Lib: skipped 52, total 52
um/x64/glmf32.lib: skipped 134, total 134
um/x64/gdiplus.lib: skipped 630, total 630
um/x64/Gdi32.Lib: skipped 605, total 605
um/x64/fxsutility.lib: skipped 2, total 2
um/x64/fwpuclnt.lib: skipped 276, total 276
um/x64/FrameDyn.Lib: skipped 604, total 604
um/x64/FrameDyd.Lib: skipped 604, total 604
um/x64/fontsub.lib: skipped 2, total 2
um/x64/fltLib.lib: skipped 29, total 29
um/x64/fileextd.lib: skipped 0, total 15
um/x64/FhSvcCtl.lib: skipped 14, total 14
um/x64/feclient.lib: skipped 54, total 54
um/x64/FaultRep.Lib: skipped 16, total 16
um/x64/evr.lib: skipped 9, total 9
um/x64/esent.lib: skipped 375, total 375
um/x64/ElsCore.lib: skipped 5, total 5
um/x64/els.lib: skipped 0, total 0
um/x64/elfapi.lib: skipped 0, total 122
um/x64/ehstorguids.lib: skipped 0, total 0
um/x64/efswrt.lib: skipped 28, total 28
um/x64/easregprov.lib: skipped 2, total 2
um/x64/eappprxy.lib: skipped 18, total 18
um/x64/eappcfg.lib: skipped 15, total 15
um/x64/dxva2.lib: skipped 38, total 38
um/x64/dxtrans.lib: skipped 6, total 6
um/x64/dxtmsft.lib: skipped 0, total 0
um/x64/dxguid.lib: skipped 0, total 0
um/x64/dxgi.lib: skipped 15, total 15
um/x64/dxcore.lib: skipped 1, total 1
um/x64/dxcompiler.lib: skipped 2, total 2
um/x64/dwrite.lib: skipped 1, total 1
um/x64/dwmapi.lib: skipped 31, total 31
um/x64/DtcHelp.Lib: skipped 2, total 17
um/x64/DSUIExt.Lib: skipped 33, total 33
um/x64/dststlog.lib: skipped 1, total 1
um/x64/dssec.lib: skipped 4, total 4
um/x64/DSProp.Lib: skipped 19, total 19
um/x64/dsound.lib: skipped 10, total 10
um/x64/drttransport.lib: skipped 2, total 2
um/x64/drtprov.lib: skipped 9, total 9
um/x64/dpx.lib: skipped 11, total 11
um/x64/drt.lib: skipped 21, total 21
um/x64/dnsrslvr.lib: skipped 4, total 4
um/x64/dnsrpc.lib: skipped 1, total 475
um/x64/dnsperf.lib: skipped 3, total 3
um/x64/dnslib.lib: skipped 6, total 1128
um/x64/dnscrcli.lib: skipped 0, total 4
um/x64/DnsAPI.Lib: skipped 289, total 289
um/x64/dmprocessxmlfiltered.lib: skipped 3, total 3
um/x64/dmoguids.lib: skipped 0, total 0
um/x64/dloadhelper.lib: skipped 0, total 3
um/x64/directml.lib: skipped 2, total 2
um/x64/dinput8.lib: skipped 1, total 2
um/x64/DiagnosticDataQuery.Lib: skipped 37, total 37
um/x64/dhcpsapi.lib: skipped 209, total 209
um/x64/DhcpCSvc6.Lib: skipped 22, total 22
um/x64/DhcpCSvc.Lib: skipped 69, total 69
um/x64/dflayout.lib: skipped 1, total 1
um/x64/devmgr.lib: skipped 19, total 19
um/x64/deviceaccess.lib: skipped 3, total 3
um/x64/devenum.lib: skipped 0, total 0
um/x64/ddraw.lib: skipped 13, total 13
um/x64/dcomp.lib: skipped 6, total 6
um/x64/dciman32.lib: skipped 20, total 20
um/x64/DbgModel.Lib: skipped 1, total 1
um/x64/DbgHelp.Lib: skipped 241, total 241
um/x64/DbgEng.Lib: skipped 4, total 4
um/x64/davclnt.lib: skipped 22, total 22
um/x64/d3dcsxd.lib: skipped 9, total 9
um/x64/d3dcsx.lib: skipped 9, total 9
um/x64/d3dcompiler.lib: skipped 29, total 29
um/x64/d3d9.lib: skipped 16, total 16
um/x64/d3d12.lib: skipped 14, total 14
um/x64/d3d11.lib: skipped 9, total 9
um/x64/d3d10.lib: skipped 29, total 29
um/x64/d3d10_1.lib: skipped 29, total 29
um/x64/d2d1.lib: skipped 13, total 13
um/x64/cscdll.lib: skipped 18, total 18
um/x64/cscapi.lib: skipped 6, total 6
um/x64/cryptxml.lib: skipped 19, total 19
um/x64/cryptui.lib: skipped 54, total 54
um/x64/CryptNet.Lib: skipped 5, total 5
um/x64/cryptdll.lib: skipped 20, total 20
um/x64/Crypt32.Lib: skipped 240, total 240
um/x64/Credui.lib: skipped 22, total 22
um/x64/corrEngine.lib: skipped 0, total 0
um/x64/CoreMessaging.lib: skipped 30, total 30
um/x64/ComSvcs.Lib: skipped 17, total 17
um/x64/computestorage.lib: skipped 11, total 11
um/x64/computenetwork.lib: skipped 48, total 48
um/x64/computecore.lib: skipped 53, total 53
um/x64/CompPkgSup.lib: skipped 9, total 9
um/x64/compstui.lib: skipped 4, total 4
um/x64/ComDlg32.Lib: skipped 21, total 21
um/x64/ComCtl32.Lib: skipped 128, total 128
um/x64/ClusApi.Lib: skipped 290, total 290
um/x64/clfsmgmt.lib: skipped 3, total 240
um/x64/clfsw32.lib: skipped 63, total 63
um/x64/cldapi.lib: skipped 48, total 48
um/x64/cimfs.lib: skipped 11, total 11
um/x64/cfgmgr32.lib: skipped 231, total 231
um/x64/Chakrart.lib: skipped 155, total 155
um/x64/CertIdl.Lib: skipped 0, total 1
um/x64/CertPolEng.Lib: skipped 14, total 14
um/x64/certcli.lib: skipped 0, total 0
um/x64/certca.lib: skipped 0, total 0
um/x64/certadm.lib: skipped 41, total 41
um/x64/Cabinet.Lib: skipped 26, total 26
um/x64/BufferOverflowU.lib: skipped 7, total 24
um/x64/BufferOverflow.lib: skipped 9, total 28
um/x64/bthprops.lib: skipped 40, total 40
um/x64/BluetoothApis.lib: skipped 96, total 96
um/x64/Bits.Lib: skipped 0, total 0
um/x64/basesrv.lib: skipped 6, total 6
um/x64/bcrypt.lib: skipped 54, total 54
um/x64/avrt.lib: skipped 20, total 20
um/x64/avifil32.Lib: skipped 74, total 74
um/x64/AuthZ.Lib: skipped 36, total 36
um/x64/aux_ulib.lib: skipped 1, total 5
um/x64/audiomediatypecrt.lib: skipped 2, total 27
um/x64/audioeng.lib: skipped 2, total 2
um/x64/AudioBaseProcessingObjectV140.lib: skipped 15, total 68
um/x64/appnotify.lib: skipped 4, total 4
um/x64/audiobaseprocessingobject.lib: skipped 15, total 65
um/x64/appmgr.lib: skipped 0, total 0
um/x64/appmgmts.lib: skipped 17, total 17
um/x64/amstrmid.lib: skipped 0, total 0
um/x64/amsi.lib: skipped 9, total 9
um/x64/ahadmin.lib: skipped 0, total 0
um/x64/advpack.Lib: skipped 84, total 84
um/x64/AdvAPI32.Lib: skipped 782, total 782
um/x64/ADSIid.Lib: skipped 0, total 0
um/x64/ActiveDS.Lib: skipped 27, total 27
um/x64/AclUI.Lib: skipped 6, total 6
```
