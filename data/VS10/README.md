# VS10 / Visual Studio 2010

# download
Visual Studio 2010 Professional
`en_visual_studio_2010_professional_x86_dvd_509727.iso`

# prepare
run `setup.exe`

# .lib/.obj
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 10.0/VC/ -iname "*.lib"
./VC/atlmfc/lib/amd64/atl.lib
./VC/atlmfc/lib/amd64/atls.lib
./VC/atlmfc/lib/amd64/atlsd.lib
./VC/atlmfc/lib/amd64/mfc100.lib
./VC/atlmfc/lib/amd64/mfc100d.lib
./VC/atlmfc/lib/amd64/mfc100u.lib
./VC/atlmfc/lib/amd64/mfc100ud.lib
./VC/atlmfc/lib/amd64/MFCM100.lib
./VC/atlmfc/lib/amd64/MFCM100d.lib
./VC/atlmfc/lib/amd64/MFCM100U.lib
./VC/atlmfc/lib/amd64/MFCM100Ud.lib
./VC/atlmfc/lib/amd64/mfcs100.lib
./VC/atlmfc/lib/amd64/mfcs100d.lib
./VC/atlmfc/lib/amd64/mfcs100u.lib
./VC/atlmfc/lib/amd64/mfcs100ud.lib
./VC/atlmfc/lib/amd64/nafxcw.lib
./VC/atlmfc/lib/amd64/nafxcwd.lib
./VC/atlmfc/lib/amd64/uafxcw.lib
./VC/atlmfc/lib/amd64/uafxcwd.lib
./VC/atlmfc/lib/Atl.lib
./VC/atlmfc/lib/atls.lib
./VC/atlmfc/lib/atlsd.lib
./VC/atlmfc/lib/mfc100.lib
./VC/atlmfc/lib/mfc100d.lib
./VC/atlmfc/lib/mfc100u.lib
./VC/atlmfc/lib/mfc100ud.lib
./VC/atlmfc/lib/MFCM100.lib
./VC/atlmfc/lib/MFCM100d.lib
./VC/atlmfc/lib/MFCM100U.lib
./VC/atlmfc/lib/MFCM100Ud.lib
./VC/atlmfc/lib/mfcs100.lib
./VC/atlmfc/lib/mfcs100d.lib
./VC/atlmfc/lib/mfcs100u.lib
./VC/atlmfc/lib/mfcs100ud.lib
./VC/atlmfc/lib/nafxcw.lib
./VC/atlmfc/lib/nafxcwd.lib
./VC/atlmfc/lib/uafxcw.lib
./VC/atlmfc/lib/uafxcwd.lib
./VC/lib/amd64/comsupp.lib
./VC/lib/amd64/comsuppd.lib
./VC/lib/amd64/comsuppw.lib
./VC/lib/amd64/comsuppwd.lib
./VC/lib/amd64/delayimp.lib
./VC/lib/amd64/libcmt.lib
./VC/lib/amd64/libcmtd.lib
./VC/lib/amd64/libcpmt.lib
./VC/lib/amd64/libcpmt1.lib
./VC/lib/amd64/libcpmtd.lib
./VC/lib/amd64/libcpmtd0.lib
./VC/lib/amd64/libcpmtd1.lib
./VC/lib/amd64/msvcmrt.lib
./VC/lib/amd64/msvcmrtd.lib
./VC/lib/amd64/msvcprt.lib
./VC/lib/amd64/msvcprtd.lib
./VC/lib/amd64/msvcrt.lib
./VC/lib/amd64/msvcrtd.lib
./VC/lib/amd64/msvcurt.lib
./VC/lib/amd64/msvcurtd.lib
./VC/lib/amd64/oldnames.lib
./VC/lib/amd64/pgobootrun.lib
./VC/lib/amd64/pgort.lib
./VC/lib/amd64/ptrustm.lib
./VC/lib/amd64/ptrustmd.lib
./VC/lib/amd64/ptrustu.lib
./VC/lib/amd64/ptrustud.lib
./VC/lib/amd64/runtmchk.lib
./VC/lib/amd64/vcomp.lib
./VC/lib/amd64/vcompd.lib
./VC/lib/comsupp.lib
./VC/lib/comsuppd.lib
./VC/lib/comsuppw.lib
./VC/lib/comsuppwd.lib
./VC/lib/delayimp.lib
./VC/lib/libcmt.lib
./VC/lib/libcmtd.lib
./VC/lib/libcpmt.lib
./VC/lib/libcpmt1.lib
./VC/lib/libcpmtd.lib
./VC/lib/libcpmtd0.lib
./VC/lib/libcpmtd1.lib
./VC/lib/msvcmrt.lib
./VC/lib/msvcmrtd.lib
./VC/lib/msvcprt.lib
./VC/lib/msvcprtd.lib
./VC/lib/msvcrt.lib
./VC/lib/msvcrtd.lib
./VC/lib/msvcurt.lib
./VC/lib/msvcurtd.lib
./VC/lib/oldnames.lib
./VC/lib/pgobootrun.lib
./VC/lib/pgort.lib
./VC/lib/ptrustm.lib
./VC/lib/ptrustmd.lib
./VC/lib/ptrustu.lib
./VC/lib/ptrustud.lib
./VC/lib/RunTmChk.lib
./VC/lib/vcomp.lib
./VC/lib/vcompd.lib

$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 10.0/ -iname "*.obj"
./VC/lib/amd64/binmode.obj
./VC/lib/amd64/chkstk.obj
./VC/lib/amd64/commode.obj
./VC/lib/amd64/invalidcontinue.obj
./VC/lib/amd64/loosefpmath.obj
./VC/lib/amd64/newmode.obj
./VC/lib/amd64/noarg.obj
./VC/lib/amd64/nochkclr.obj
./VC/lib/amd64/noenv.obj
./VC/lib/amd64/nohetoc.obj
./VC/lib/amd64/nothrownew.obj
./VC/lib/amd64/pbinmode.obj
./VC/lib/amd64/pcommode.obj
./VC/lib/amd64/pinvalidcontinue.obj
./VC/lib/amd64/pnewmode.obj
./VC/lib/amd64/pnoarg.obj
./VC/lib/amd64/pnoenv.obj
./VC/lib/amd64/pnothrownew.obj
./VC/lib/amd64/psetargv.obj
./VC/lib/amd64/pthreadlocale.obj
./VC/lib/amd64/pwsetargv.obj
./VC/lib/amd64/setargv.obj
./VC/lib/amd64/smalheap.obj
./VC/lib/amd64/threadlocale.obj
./VC/lib/amd64/wsetargv.obj
./VC/lib/binmode.obj
./VC/lib/chkstk.obj
./VC/lib/commode.obj
./VC/lib/fp10.obj
./VC/lib/invalidcontinue.obj
./VC/lib/loosefpmath.obj
./VC/lib/newmode.obj
./VC/lib/noarg.obj
./VC/lib/nochkclr.obj
./VC/lib/noenv.obj
./VC/lib/nohetoc.obj
./VC/lib/nothrownew.obj
./VC/lib/pbinmode.obj
./VC/lib/pcommode.obj
./VC/lib/pinvalidcontinue.obj
./VC/lib/pnewmode.obj
./VC/lib/pnoarg.obj
./VC/lib/pnoenv.obj
./VC/lib/pnothrownew.obj
./VC/lib/psetargv.obj
./VC/lib/pthreadlocale.obj
./VC/lib/pwsetargv.obj
./VC/lib/setargv.obj
./VC/lib/smalheap.obj
./VC/lib/threadlocale.obj
./VC/lib/wsetargv.obj

$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 10.0/VC/ VS10/
```

```
$ find VS10/ -type f \( -iname "*.lib" -o -iname "*.obj" \) -exec md5sum {} \;
ee30573c42c8df39bb02cae4d93d17e1 *VS10/VC/atlmfc/lib/amd64/atl.lib
77a2e61400422105ecd78b6105998d8b *VS10/VC/atlmfc/lib/amd64/atls.lib
1921e55f66feed4824ec2a5f40852a37 *VS10/VC/atlmfc/lib/amd64/atlsd.lib
a17b5e309317f7e1792c019ce1a68918 *VS10/VC/atlmfc/lib/amd64/mfc100.lib
f2f297985d19535c89dc013aa208c31d *VS10/VC/atlmfc/lib/amd64/mfc100d.lib
d6a64b7de5898975eff4923ecdedda9e *VS10/VC/atlmfc/lib/amd64/mfc100u.lib
7aba41f01d47171c4af5fb668e28257e *VS10/VC/atlmfc/lib/amd64/mfc100ud.lib
95267ef30374ee9f3fb5d1d54d5b4510 *VS10/VC/atlmfc/lib/amd64/MFCM100.lib
a2de616e23b134514beeaa0d3b722b44 *VS10/VC/atlmfc/lib/amd64/MFCM100d.lib
6be3fd66010290c60ed8904feebed080 *VS10/VC/atlmfc/lib/amd64/MFCM100U.lib
d381905b8da69af7e97a2c83a1f49472 *VS10/VC/atlmfc/lib/amd64/MFCM100Ud.lib
7498bb0d88a6b1e982f71431af548ca7 *VS10/VC/atlmfc/lib/amd64/mfcs100.lib
23d01f4d522a9ffdb4e91447b0a1e830 *VS10/VC/atlmfc/lib/amd64/mfcs100d.lib
2f1f1a56c7de4c0fbebcf05719d83858 *VS10/VC/atlmfc/lib/amd64/mfcs100u.lib
699f513eb94e285257f7073459a60eab *VS10/VC/atlmfc/lib/amd64/mfcs100ud.lib
f37620a558a1027abc0756ecb7e4773e *VS10/VC/atlmfc/lib/amd64/nafxcw.lib
ec76d008b2920fa01fed7cb819e25cc3 *VS10/VC/atlmfc/lib/amd64/nafxcwd.lib
b2144c80b69de46936740798acb8f75c *VS10/VC/atlmfc/lib/amd64/uafxcw.lib
124eeff1e9ff106af0cc54e44584bd35 *VS10/VC/atlmfc/lib/amd64/uafxcwd.lib
2562a1a25fb8223e25f1829719a51eb1 *VS10/VC/atlmfc/lib/Atl.lib
8c88b41bad1ff6ed5c2ca3eb17071d42 *VS10/VC/atlmfc/lib/atls.lib
ecfe995ab4f27a53e4dad36466fc8a38 *VS10/VC/atlmfc/lib/atlsd.lib
6bf5e0999cdc25e48a6dae80de7ae5ed *VS10/VC/atlmfc/lib/mfc100.lib
14944d99482e61840cfb15bc7aa9eb4e *VS10/VC/atlmfc/lib/mfc100d.lib
9b1c66c8c1271be3d8f8819ac96ae1b3 *VS10/VC/atlmfc/lib/mfc100u.lib
3c1b40efd08ec4a9cf7f6b999a6a02b9 *VS10/VC/atlmfc/lib/mfc100ud.lib
1c8a20575606da6a728825d21e51decf *VS10/VC/atlmfc/lib/MFCM100.lib
94261c6cc206a614084e7f300f21f64d *VS10/VC/atlmfc/lib/MFCM100d.lib
50d3a263c108473b616db4a1bf0f6908 *VS10/VC/atlmfc/lib/MFCM100U.lib
62060c1d0aa16efc86c2843d0fe00e4f *VS10/VC/atlmfc/lib/MFCM100Ud.lib
bd0d7df9017f56b4780d6d7b158b2cb1 *VS10/VC/atlmfc/lib/mfcs100.lib
0e716837b4db97e2bd01b970c55bb700 *VS10/VC/atlmfc/lib/mfcs100d.lib
e503fd913c8346cc2a96eadc7d182d18 *VS10/VC/atlmfc/lib/mfcs100u.lib
ba72e40c54dc5453e3294f6898f0db0b *VS10/VC/atlmfc/lib/mfcs100ud.lib
a4a968eb652f43b83d98aa5733aa8420 *VS10/VC/atlmfc/lib/nafxcw.lib
1859e2ce22e5c34896b90a6527502795 *VS10/VC/atlmfc/lib/nafxcwd.lib
f9157ffa32d206e7eb0b2bb0ad3c820e *VS10/VC/atlmfc/lib/uafxcw.lib
61f17ef1eb14100d790695221d8a6396 *VS10/VC/atlmfc/lib/uafxcwd.lib
b479777f8e65f13864c288985cb65cc6 *VS10/VC/lib/amd64/binmode.obj
d968b489f4545f72ba7993b675b77385 *VS10/VC/lib/amd64/chkstk.obj
7b4f12f841665b097c426ecb4fa58a94 *VS10/VC/lib/amd64/commode.obj
9bba52a3a51e520a1f4589af11db68b3 *VS10/VC/lib/amd64/comsupp.lib
c23d2ff77befeeec03a856092375064b *VS10/VC/lib/amd64/comsuppd.lib
cb75de9d944f68dd707e981d32c465fb *VS10/VC/lib/amd64/comsuppw.lib
06003483dbd59cd483bb233d2a76b8d9 *VS10/VC/lib/amd64/comsuppwd.lib
9152f47b1e41aebf46a3dd9b5da7e005 *VS10/VC/lib/amd64/delayimp.lib
0bc0ad96ec6dd0a1cf6a537e2ca57ff4 *VS10/VC/lib/amd64/invalidcontinue.obj
10f88aa58fb3877baefdae5b532e6c1d *VS10/VC/lib/amd64/libcmt.lib
73dc7c5fb28dde7c193535a7b3333f05 *VS10/VC/lib/amd64/libcmtd.lib
161d38672aa370c8b62d4e9741992d0f *VS10/VC/lib/amd64/libcpmt.lib
1d3473e1dbe799b3cd1cc601e8c2d864 *VS10/VC/lib/amd64/libcpmt1.lib
72346cff5dcdec9299707e9a3c1f82a4 *VS10/VC/lib/amd64/libcpmtd.lib
86c49065d430bb61a851653f25a640d5 *VS10/VC/lib/amd64/libcpmtd0.lib
c94274f781f6b070c237579c78ff31c1 *VS10/VC/lib/amd64/libcpmtd1.lib
380e577c60bd596e05de10515789785b *VS10/VC/lib/amd64/loosefpmath.obj
14b9cbbe4fc25a89a2bfb5dc9a8f2320 *VS10/VC/lib/amd64/msvcmrt.lib
53f2bb449f38cbe9ba30935c753f4de1 *VS10/VC/lib/amd64/msvcmrtd.lib
099c98e974304dbbfb729031a4183ef2 *VS10/VC/lib/amd64/msvcprt.lib
2b8dff50fad19aba588ce3934078953f *VS10/VC/lib/amd64/msvcprtd.lib
d41a3905a2f29aabc15c7acf9c4b9f7f *VS10/VC/lib/amd64/msvcrt.lib
aaab48afa8a52d08f2abc461154cd50e *VS10/VC/lib/amd64/msvcrtd.lib
e37648c19862b1c44fe60dd7749ae58e *VS10/VC/lib/amd64/msvcurt.lib
73e6cec7786ae9d8cb5cef8394d2cc3b *VS10/VC/lib/amd64/msvcurtd.lib
3fe2ac3068f18c93ab88ce7369352bde *VS10/VC/lib/amd64/newmode.obj
eb931bb363101ea93a3055ebfb64cb1a *VS10/VC/lib/amd64/noarg.obj
b4ef34de4379df808eb93405a1cbfb02 *VS10/VC/lib/amd64/nochkclr.obj
4a04020888cfbb4fa53597cc5f3c0ed9 *VS10/VC/lib/amd64/noenv.obj
d2d2795da5a1ca89ce1cee9c2cbcd54d *VS10/VC/lib/amd64/nohetoc.obj
1d4fdf9c2e02788b06af2a7ce80644c9 *VS10/VC/lib/amd64/nothrownew.obj
eeb59833cdeb5e4671f452b333286aa0 *VS10/VC/lib/amd64/oldnames.lib
e443a8513ffde111941965f8f03d12e0 *VS10/VC/lib/amd64/pbinmode.obj
962ae079a1bb7be515237d86daaf3653 *VS10/VC/lib/amd64/pcommode.obj
ee1d36db3d99644bc9d59b3b2c3bfafd *VS10/VC/lib/amd64/pgobootrun.lib
51c33f1b6a420108ef3171eaccff0ffd *VS10/VC/lib/amd64/pgort.lib
033378d34a0996ff67d9f4069b9ed33a *VS10/VC/lib/amd64/pinvalidcontinue.obj
32480782ee52d7e3497853f11959a017 *VS10/VC/lib/amd64/pnewmode.obj
d8f0379e101ee832fec780376703c431 *VS10/VC/lib/amd64/pnoarg.obj
4d9390d8fdcfbbe43beb81fd9f3ccad9 *VS10/VC/lib/amd64/pnoenv.obj
fbe04170c075c90662881e4314cd9564 *VS10/VC/lib/amd64/pnothrownew.obj
0c584bc08b45115fe16dabf0711bb715 *VS10/VC/lib/amd64/psetargv.obj
e4eb11fdadd2f8d2a923ec3b6c2f3c86 *VS10/VC/lib/amd64/pthreadlocale.obj
45af445ed5242788bf9525f3ed210252 *VS10/VC/lib/amd64/ptrustm.lib
5bcc9430e78170d0426ba71c0a5df95d *VS10/VC/lib/amd64/ptrustmd.lib
a6af5bcfefa638b1e351963e2e170e6e *VS10/VC/lib/amd64/ptrustu.lib
1efe89d55709ff00b966ad03366e37fb *VS10/VC/lib/amd64/ptrustud.lib
1aef40ff79ed94db13076bea69773eb5 *VS10/VC/lib/amd64/pwsetargv.obj
878845059de978b68636961f63894c0c *VS10/VC/lib/amd64/runtmchk.lib
6b099d3efb7245b294222adb80950227 *VS10/VC/lib/amd64/setargv.obj
7b8c133560580161edb4fc28c5b6dec3 *VS10/VC/lib/amd64/smalheap.obj
1b4461c13c72a53b88b9c70a1c21641c *VS10/VC/lib/amd64/threadlocale.obj
1376dbc41ec72ecafe829e4d306aac26 *VS10/VC/lib/amd64/vcomp.lib
4006d6d5d0d5385be8076d96c8d8f23e *VS10/VC/lib/amd64/vcompd.lib
a5a297f5564018ef3be55d0f608038cd *VS10/VC/lib/amd64/wsetargv.obj
3ea0e3ba6eac1657ab230ffbf93e0827 *VS10/VC/lib/binmode.obj
251d981d97c6dd61e6d973eeb5b82ba0 *VS10/VC/lib/chkstk.obj
5ce1336315aab9265656129f64fd0cab *VS10/VC/lib/commode.obj
cd20f2cad9384bd8c39948ce95e4a828 *VS10/VC/lib/comsupp.lib
305cff913e38cd801b152faa2dba6602 *VS10/VC/lib/comsuppd.lib
703b3351db51d9ade22eb756dd35a307 *VS10/VC/lib/comsuppw.lib
3a3680dbd9da62cd0c99a60ece113a15 *VS10/VC/lib/comsuppwd.lib
7cce48817400592c1ec6307d3773d809 *VS10/VC/lib/delayimp.lib
1f65d18e34db06e1d145b33526637597 *VS10/VC/lib/fp10.obj
a9352622c4dd2ff00414b111962c0710 *VS10/VC/lib/invalidcontinue.obj
6fd52b779b0b19f1b568f85401a9a367 *VS10/VC/lib/libcmt.lib
2cd424b214b90f06b50cd74286b45e00 *VS10/VC/lib/libcmtd.lib
262e0fe6c254c8cb23ec870284c88270 *VS10/VC/lib/libcpmt.lib
d8944ea54ec0744e62615ed42fdd9563 *VS10/VC/lib/libcpmt1.lib
32e3db44a101b3bd28420dc66d1285f9 *VS10/VC/lib/libcpmtd.lib
476b8d5ea8be69892977293870b54673 *VS10/VC/lib/libcpmtd0.lib
a32b036cf8a1e5e7f67b14ea0bd77df4 *VS10/VC/lib/libcpmtd1.lib
1bf2f04f39a8422e1cb8760e720eeb6e *VS10/VC/lib/loosefpmath.obj
ec7579120740216007f7552324aebbe7 *VS10/VC/lib/msvcmrt.lib
f4f879d6496386220f9027e4e65834de *VS10/VC/lib/msvcmrtd.lib
7b80f3fdcf0e4ca25307cc49603b4a2b *VS10/VC/lib/msvcprt.lib
e7b2a8ace32a74231b3ae34500ef51dc *VS10/VC/lib/msvcprtd.lib
1b886a8520492228a52e7bea8263cd3e *VS10/VC/lib/msvcrt.lib
563d3aae805dc12abe7b1d7c324ad748 *VS10/VC/lib/msvcrtd.lib
11633ee4f0292bf9714ed64ec75c20a2 *VS10/VC/lib/msvcurt.lib
dec37089d5b6a08a0aa9fca460ad1f99 *VS10/VC/lib/msvcurtd.lib
21de1617b2081807903ccc88a5e67abe *VS10/VC/lib/newmode.obj
7a2423128f2aab535fc9431c835d1bfb *VS10/VC/lib/noarg.obj
7e59f265ca0b7321b9a96dc5f2a3d0b5 *VS10/VC/lib/nochkclr.obj
92a16b8b3e129225b6a2cb8ff206915b *VS10/VC/lib/noenv.obj
0b35c509be6a458f2f8e72832b05c628 *VS10/VC/lib/nohetoc.obj
b3f145a37a7362d15d448c2beeb22572 *VS10/VC/lib/nothrownew.obj
ab2b269f360f7ca77e05fc487fd36057 *VS10/VC/lib/oldnames.lib
cd49e0f31e8f96ad7a3a54d3e8af3b90 *VS10/VC/lib/pbinmode.obj
690f5758b66b0c93862e41ef0bf5eb86 *VS10/VC/lib/pcommode.obj
69654e4a255e5d63600b31250c82ce49 *VS10/VC/lib/pgobootrun.lib
d2b93ea545c77cef40033e8eeff0707a *VS10/VC/lib/pgort.lib
da5d2f8cbc11dc65d5ce5632eb28f50d *VS10/VC/lib/pinvalidcontinue.obj
e93b362f605cc9204a0d6e0122eefc72 *VS10/VC/lib/pnewmode.obj
ddec8358d3fce4de9b32dbd2ce1742b2 *VS10/VC/lib/pnoarg.obj
d98ba922cd44c574e1d93e6db1d05d9f *VS10/VC/lib/pnoenv.obj
4be9ac7e5f7b4e441924c42dfe2e3f2f *VS10/VC/lib/pnothrownew.obj
55e59078bb7c1eaa7fb0026b388b785d *VS10/VC/lib/psetargv.obj
ef50069f01024583da8aef4b46627251 *VS10/VC/lib/pthreadlocale.obj
364d6650c28e1cd88493c042da0534ea *VS10/VC/lib/ptrustm.lib
150f3175e230a91b5cc7cb78aa1d15f4 *VS10/VC/lib/ptrustmd.lib
13501c17fb71e45e7ef6fc7406e911dc *VS10/VC/lib/ptrustu.lib
bcf45f127248971475bc6d69cc6e902a *VS10/VC/lib/ptrustud.lib
ecda12c571d29d600b8be420bbfb9bfb *VS10/VC/lib/pwsetargv.obj
68aa2b354b43f050c262c80668db5639 *VS10/VC/lib/RunTmChk.lib
6895304863022f54265c327872b861fe *VS10/VC/lib/setargv.obj
9a1c9ca85979914138bc5ae63f066c38 *VS10/VC/lib/smalheap.obj
059f0ccc4cfe2119c572125045e3c414 *VS10/VC/lib/threadlocale.obj
5e26d7c8e28fe02f5de7fa1648cdc464 *VS10/VC/lib/vcomp.lib
831d8671abb065d0f27a357add627ad7 *VS10/VC/lib/vcompd.lib
051f3cae7589d25c32fa7da53c55a72d *VS10/VC/lib/wsetargv.obj
```

# .pat
```
$ find VS10/ -type f -exec ../../pcf.exe {} {}.pat \;
.\VS10\VC\atlmfc\lib\amd64\atl.lib: skipped 52, total 52
.\VS10\VC\atlmfc\lib\amd64\atls.lib: skipped 20, total 297
.\VS10\VC\atlmfc\lib\amd64\atlsd.lib: skipped 0, total 683
.\VS10\VC\atlmfc\lib\amd64\mfc100.lib: skipped 13912, total 13912
.\VS10\VC\atlmfc\lib\amd64\mfc100d.lib: skipped 16429, total 16429
.\VS10\VC\atlmfc\lib\amd64\mfc100u.lib: skipped 16581, total 16581
.\VS10\VC\atlmfc\lib\amd64\mfc100ud.lib: skipped 19513, total 19513
.\VS10\VC\atlmfc\lib\amd64\MFCM100.lib: skipped 25, total 41
.\VS10\VC\atlmfc\lib\amd64\MFCM100d.lib: skipped 31, total 47
.\VS10\VC\atlmfc\lib\amd64\MFCM100U.lib: skipped 27, total 43
.\VS10\VC\atlmfc\lib\amd64\MFCM100Ud.lib: skipped 33, total 49
.\VS10\VC\atlmfc\lib\amd64\mfcs100.lib: skipped 10, total 104
.\VS10\VC\atlmfc\lib\amd64\mfcs100d.lib: skipped 0, total 129
.\VS10\VC\atlmfc\lib\amd64\mfcs100u.lib: skipped 10, total 104
.\VS10\VC\atlmfc\lib\amd64\mfcs100ud.lib: skipped 2, total 133
.\VS10\VC\atlmfc\lib\amd64\nafxcw.lib: skipped 4979, total 53148
.\VS10\VC\atlmfc\lib\amd64\nafxcwd.lib: skipped 333, total 47350
.\VS10\VC\atlmfc\lib\amd64\uafxcw.lib: skipped 6862, total 54683
.\VS10\VC\atlmfc\lib\amd64\uafxcwd.lib: skipped 2212, total 49203
.\VS10\VC\atlmfc\lib\Atl.lib: skipped 52, total 52
.\VS10\VC\atlmfc\lib\atls.lib: skipped 26, total 1317
.\VS10\VC\atlmfc\lib\atlsd.lib: skipped 0, total 1703
.\VS10\VC\atlmfc\lib\mfc100.lib: skipped 14272, total 14272
.\VS10\VC\atlmfc\lib\mfc100d.lib: skipped 16825, total 16825
.\VS10\VC\atlmfc\lib\mfc100u.lib: skipped 17172, total 17172
.\VS10\VC\atlmfc\lib\mfc100ud.lib: skipped 20140, total 20140
.\VS10\VC\atlmfc\lib\MFCM100.lib: skipped 25, total 41
.\VS10\VC\atlmfc\lib\MFCM100d.lib: skipped 32, total 48
.\VS10\VC\atlmfc\lib\MFCM100U.lib: skipped 27, total 43
.\VS10\VC\atlmfc\lib\MFCM100Ud.lib: skipped 34, total 50
.\VS10\VC\atlmfc\lib\mfcs100.lib: skipped 11, total 101
.\VS10\VC\atlmfc\lib\mfcs100d.lib: skipped 0, total 127
.\VS10\VC\atlmfc\lib\mfcs100u.lib: skipped 11, total 101
.\VS10\VC\atlmfc\lib\mfcs100ud.lib: skipped 2, total 131
.\VS10\VC\atlmfc\lib\nafxcw.lib: skipped 6087, total 53769
.\VS10\VC\atlmfc\lib\nafxcwd.lib: skipped 293, total 48028
.\VS10\VC\atlmfc\lib\uafxcw.lib: skipped 7773, total 55442
.\VS10\VC\atlmfc\lib\uafxcwd.lib: skipped 2282, total 50021
.\VS10\VC\lib\amd64\binmode.obj: skipped 0, total 0
.\VS10\VC\lib\amd64\chkstk.obj: skipped 0, total 1
.\VS10\VC\lib\amd64\commode.obj: skipped 0, total 0
.\VS10\VC\lib\amd64\comsupp.lib: skipped 0, total 26
.\VS10\VC\lib\amd64\comsuppd.lib: skipped 0, total 28
.\VS10\VC\lib\amd64\comsuppw.lib: skipped 0, total 26
.\VS10\VC\lib\amd64\comsuppwd.lib: skipped 0, total 28
.\VS10\VC\lib\amd64\delayimp.lib: skipped 1, total 27
.\VS10\VC\lib\amd64\invalidcontinue.obj: skipped 1, total 2
.\VS10\VC\lib\amd64\libcmt.lib: skipped 513, total 6079
.\VS10\VC\lib\amd64\libcmtd.lib: skipped 147, total 6326
.\VS10\VC\lib\amd64\libcpmt.lib: skipped 435, total 5637
.\VS10\VC\lib\amd64\libcpmt1.lib: skipped 558, total 6083
.\VS10\VC\lib\amd64\libcpmtd.lib: skipped 0, total 6608
.\VS10\VC\lib\amd64\libcpmtd0.lib: skipped 0, total 5890
.\VS10\VC\lib\amd64\libcpmtd1.lib: skipped 0, total 6354
.\VS10\VC\lib\amd64\loosefpmath.obj: skipped 0, total 2
.\VS10\VC\lib\amd64\msvcmrt.lib: skipped 281, total 649
.\VS10\VC\lib\amd64\msvcmrtd.lib: skipped 281, total 698
.\VS10\VC\lib\amd64\msvcprt.lib: skipped 1678, total 1689
.\VS10\VC\lib\amd64\msvcprtd.lib: skipped 1683, total 1699
.\VS10\VC\lib\amd64\msvcrt.lib: skipped 1866, total 1975
.\VS10\VC\lib\amd64\msvcrtd.lib: skipped 1928, total 2040
.\VS10\VC\lib\amd64\msvcurt.lib: skipped 3538, total 21772
.\VS10\VC\lib\amd64\msvcurtd.lib: skipped 3609, total 23049
.\VS10\VC\lib\amd64\newmode.obj: skipped 0, total 0
.\VS10\VC\lib\amd64\noarg.obj: skipped 4, total 4
.\VS10\VC\lib\amd64\nochkclr.obj: skipped 0, total 0
.\VS10\VC\lib\amd64\noenv.obj: skipped 4, total 4
.\VS10\VC\lib\amd64\nohetoc.obj: skipped 0, total 0
.\VS10\VC\lib\amd64\nothrownew.obj: skipped 0, total 4
.\VS10\VC\lib\amd64\oldnames.lib: skipped 278, total 278
.\VS10\VC\lib\amd64\pbinmode.obj: skipped 0, total 10
.\VS10\VC\lib\amd64\pcommode.obj: skipped 0, total 8
.\VS10\VC\lib\amd64\pgobootrun.lib: skipped 2, total 2
.\VS10\VC\lib\amd64\pgort.lib: skipped 7, total 13
.\VS10\VC\lib\amd64\pinvalidcontinue.obj: skipped 0, total 13
.\VS10\VC\lib\amd64\pnewmode.obj: skipped 0, total 8
.\VS10\VC\lib\amd64\pnoarg.obj: skipped 0, total 11
.\VS10\VC\lib\amd64\pnoenv.obj: skipped 0, total 13
.\VS10\VC\lib\amd64\pnothrownew.obj: skipped 0, total 13
.\VS10\VC\lib\amd64\psetargv.obj: skipped 0, total 8
.\VS10\VC\lib\amd64\pthreadlocale.obj: skipped 0, total 1
.\VS10\VC\lib\amd64\ptrustm.lib: skipped 0, total 175
.\VS10\VC\lib\amd64\ptrustmd.lib: skipped 0, total 176
.\VS10\VC\lib\amd64\ptrustu.lib: skipped 0, total 111
.\VS10\VC\lib\amd64\ptrustud.lib: skipped 0, total 111
.\VS10\VC\lib\amd64\pwsetargv.obj: skipped 0, total 8
.\VS10\VC\lib\amd64\runtmchk.lib: skipped 0, total 42
.\VS10\VC\lib\amd64\setargv.obj: skipped 0, total 1
.\VS10\VC\lib\amd64\smalheap.obj: skipped 0, total 12
.\VS10\VC\lib\amd64\threadlocale.obj: skipped 0, total 0
.\VS10\VC\lib\amd64\vcomp.lib: skipped 112, total 112
.\VS10\VC\lib\amd64\vcompd.lib: skipped 112, total 112
.\VS10\VC\lib\amd64\wsetargv.obj: skipped 0, total 1
.\VS10\VC\lib\binmode.obj: skipped 0, total 0
.\VS10\VC\lib\chkstk.obj: skipped 0, total 1
.\VS10\VC\lib\commode.obj: skipped 0, total 0
.\VS10\VC\lib\comsupp.lib: skipped 0, total 26
.\VS10\VC\lib\comsuppd.lib: skipped 0, total 26
.\VS10\VC\lib\comsuppw.lib: skipped 0, total 26
.\VS10\VC\lib\comsuppwd.lib: skipped 0, total 26
.\VS10\VC\lib\delayimp.lib: skipped 1, total 27
.\VS10\VC\lib\fp10.obj: skipped 0, total 2
.\VS10\VC\lib\invalidcontinue.obj: skipped 1, total 2
.\VS10\VC\lib\libcmt.lib: skipped 586, total 5895
.\VS10\VC\lib\libcmtd.lib: skipped 132, total 6115
.\VS10\VC\lib\libcpmt.lib: skipped 381, total 5587
.\VS10\VC\lib\libcpmt1.lib: skipped 472, total 6005
.\VS10\VC\lib\libcpmtd.lib: skipped 0, total 6657
.\VS10\VC\lib\libcpmtd0.lib: skipped 0, total 5939
.\VS10\VC\lib\libcpmtd1.lib: skipped 0, total 6403
.\VS10\VC\lib\loosefpmath.obj: skipped 0, total 2
.\VS10\VC\lib\msvcmrt.lib: skipped 283, total 651
.\VS10\VC\lib\msvcmrtd.lib: skipped 283, total 700
.\VS10\VC\lib\msvcprt.lib: skipped 1676, total 1689
.\VS10\VC\lib\msvcprtd.lib: skipped 1687, total 1703
.\VS10\VC\lib\msvcrt.lib: skipped 1897, total 2023
.\VS10\VC\lib\msvcrtd.lib: skipped 1958, total 2089
.\VS10\VC\lib\msvcurt.lib: skipped 3569, total 21803
.\VS10\VC\lib\msvcurtd.lib: skipped 3645, total 23139
.\VS10\VC\lib\newmode.obj: skipped 0, total 0
.\VS10\VC\lib\noarg.obj: skipped 4, total 4
.\VS10\VC\lib\nochkclr.obj: skipped 1, total 1
.\VS10\VC\lib\noenv.obj: skipped 4, total 4
.\VS10\VC\lib\nohetoc.obj: skipped 0, total 0
.\VS10\VC\lib\nothrownew.obj: skipped 0, total 4
.\VS10\VC\lib\oldnames.lib: skipped 278, total 278
.\VS10\VC\lib\pbinmode.obj: skipped 0, total 10
.\VS10\VC\lib\pcommode.obj: skipped 0, total 8
.\VS10\VC\lib\pgobootrun.lib: skipped 2, total 2
.\VS10\VC\lib\pgort.lib: skipped 10, total 21
.\VS10\VC\lib\pinvalidcontinue.obj: skipped 0, total 13
.\VS10\VC\lib\pnewmode.obj: skipped 0, total 8
.\VS10\VC\lib\pnoarg.obj: skipped 0, total 11
.\VS10\VC\lib\pnoenv.obj: skipped 0, total 13
.\VS10\VC\lib\pnothrownew.obj: skipped 0, total 13
.\VS10\VC\lib\psetargv.obj: skipped 0, total 8
.\VS10\VC\lib\pthreadlocale.obj: skipped 0, total 1
.\VS10\VC\lib\ptrustm.lib: skipped 0, total 175
.\VS10\VC\lib\ptrustmd.lib: skipped 0, total 176
.\VS10\VC\lib\ptrustu.lib: skipped 0, total 111
.\VS10\VC\lib\ptrustud.lib: skipped 0, total 111
.\VS10\VC\lib\pwsetargv.obj: skipped 0, total 8
.\VS10\VC\lib\RunTmChk.lib: skipped 1, total 51
.\VS10\VC\lib\setargv.obj: skipped 0, total 1
.\VS10\VC\lib\smalheap.obj: skipped 0, total 12
.\VS10\VC\lib\threadlocale.obj: skipped 0, total 0
.\VS10\VC\lib\vcomp.lib: skipped 112, total 112
.\VS10\VC\lib\vcompd.lib: skipped 112, total 112
.\VS10\VC\lib\wsetargv.obj: skipped 0, total 1
```

```
$ find VS10 -name '*.pat' -print0 | tar -czvf VS10/VS10.tar.gz --null -T -
VS10/VC/atlmfc/lib/amd64/atl.lib.pat
VS10/VC/atlmfc/lib/amd64/atls.lib.pat
VS10/VC/atlmfc/lib/amd64/atlsd.lib.pat
VS10/VC/atlmfc/lib/amd64/mfc100.lib.pat
VS10/VC/atlmfc/lib/amd64/mfc100d.lib.pat
VS10/VC/atlmfc/lib/amd64/mfc100u.lib.pat
VS10/VC/atlmfc/lib/amd64/mfc100ud.lib.pat
VS10/VC/atlmfc/lib/amd64/MFCM100.lib.pat
VS10/VC/atlmfc/lib/amd64/MFCM100d.lib.pat
VS10/VC/atlmfc/lib/amd64/MFCM100U.lib.pat
VS10/VC/atlmfc/lib/amd64/MFCM100Ud.lib.pat
VS10/VC/atlmfc/lib/amd64/mfcs100.lib.pat
VS10/VC/atlmfc/lib/amd64/mfcs100d.lib.pat
VS10/VC/atlmfc/lib/amd64/mfcs100u.lib.pat
VS10/VC/atlmfc/lib/amd64/mfcs100ud.lib.pat
VS10/VC/atlmfc/lib/amd64/nafxcw.lib.pat
VS10/VC/atlmfc/lib/amd64/nafxcwd.lib.pat
VS10/VC/atlmfc/lib/amd64/uafxcw.lib.pat
VS10/VC/atlmfc/lib/amd64/uafxcwd.lib.pat
VS10/VC/atlmfc/lib/Atl.lib.pat
VS10/VC/atlmfc/lib/atls.lib.pat
VS10/VC/atlmfc/lib/atlsd.lib.pat
VS10/VC/atlmfc/lib/mfc100.lib.pat
VS10/VC/atlmfc/lib/mfc100d.lib.pat
VS10/VC/atlmfc/lib/mfc100u.lib.pat
VS10/VC/atlmfc/lib/mfc100ud.lib.pat
VS10/VC/atlmfc/lib/MFCM100.lib.pat
VS10/VC/atlmfc/lib/MFCM100d.lib.pat
VS10/VC/atlmfc/lib/MFCM100U.lib.pat
VS10/VC/atlmfc/lib/MFCM100Ud.lib.pat
VS10/VC/atlmfc/lib/mfcs100.lib.pat
VS10/VC/atlmfc/lib/mfcs100d.lib.pat
VS10/VC/atlmfc/lib/mfcs100u.lib.pat
VS10/VC/atlmfc/lib/mfcs100ud.lib.pat
VS10/VC/atlmfc/lib/nafxcw.lib.pat
VS10/VC/atlmfc/lib/nafxcwd.lib.pat
VS10/VC/atlmfc/lib/uafxcw.lib.pat
VS10/VC/atlmfc/lib/uafxcwd.lib.pat
VS10/VC/lib/amd64/binmode.obj.pat
VS10/VC/lib/amd64/chkstk.obj.pat
VS10/VC/lib/amd64/commode.obj.pat
VS10/VC/lib/amd64/comsupp.lib.pat
VS10/VC/lib/amd64/comsuppd.lib.pat
VS10/VC/lib/amd64/comsuppw.lib.pat
VS10/VC/lib/amd64/comsuppwd.lib.pat
VS10/VC/lib/amd64/delayimp.lib.pat
VS10/VC/lib/amd64/invalidcontinue.obj.pat
VS10/VC/lib/amd64/libcmt.lib.pat
VS10/VC/lib/amd64/libcmtd.lib.pat
VS10/VC/lib/amd64/libcpmt.lib.pat
VS10/VC/lib/amd64/libcpmt1.lib.pat
VS10/VC/lib/amd64/libcpmtd.lib.pat
VS10/VC/lib/amd64/libcpmtd0.lib.pat
VS10/VC/lib/amd64/libcpmtd1.lib.pat
VS10/VC/lib/amd64/loosefpmath.obj.pat
VS10/VC/lib/amd64/msvcmrt.lib.pat
VS10/VC/lib/amd64/msvcmrtd.lib.pat
VS10/VC/lib/amd64/msvcprt.lib.pat
VS10/VC/lib/amd64/msvcprtd.lib.pat
VS10/VC/lib/amd64/msvcrt.lib.pat
VS10/VC/lib/amd64/msvcrtd.lib.pat
VS10/VC/lib/amd64/msvcurt.lib.pat
VS10/VC/lib/amd64/msvcurtd.lib.pat
VS10/VC/lib/amd64/newmode.obj.pat
VS10/VC/lib/amd64/noarg.obj.pat
VS10/VC/lib/amd64/nochkclr.obj.pat
VS10/VC/lib/amd64/noenv.obj.pat
VS10/VC/lib/amd64/nohetoc.obj.pat
VS10/VC/lib/amd64/nothrownew.obj.pat
VS10/VC/lib/amd64/oldnames.lib.pat
VS10/VC/lib/amd64/pbinmode.obj.pat
VS10/VC/lib/amd64/pcommode.obj.pat
VS10/VC/lib/amd64/pgobootrun.lib.pat
VS10/VC/lib/amd64/pgort.lib.pat
VS10/VC/lib/amd64/pinvalidcontinue.obj.pat
VS10/VC/lib/amd64/pnewmode.obj.pat
VS10/VC/lib/amd64/pnoarg.obj.pat
VS10/VC/lib/amd64/pnoenv.obj.pat
VS10/VC/lib/amd64/pnothrownew.obj.pat
VS10/VC/lib/amd64/psetargv.obj.pat
VS10/VC/lib/amd64/pthreadlocale.obj.pat
VS10/VC/lib/amd64/ptrustm.lib.pat
VS10/VC/lib/amd64/ptrustmd.lib.pat
VS10/VC/lib/amd64/ptrustu.lib.pat
VS10/VC/lib/amd64/ptrustud.lib.pat
VS10/VC/lib/amd64/pwsetargv.obj.pat
VS10/VC/lib/amd64/runtmchk.lib.pat
VS10/VC/lib/amd64/setargv.obj.pat
VS10/VC/lib/amd64/smalheap.obj.pat
VS10/VC/lib/amd64/threadlocale.obj.pat
VS10/VC/lib/amd64/vcomp.lib.pat
VS10/VC/lib/amd64/vcompd.lib.pat
VS10/VC/lib/amd64/wsetargv.obj.pat
VS10/VC/lib/binmode.obj.pat
VS10/VC/lib/chkstk.obj.pat
VS10/VC/lib/commode.obj.pat
VS10/VC/lib/comsupp.lib.pat
VS10/VC/lib/comsuppd.lib.pat
VS10/VC/lib/comsuppw.lib.pat
VS10/VC/lib/comsuppwd.lib.pat
VS10/VC/lib/delayimp.lib.pat
VS10/VC/lib/fp10.obj.pat
VS10/VC/lib/invalidcontinue.obj.pat
VS10/VC/lib/libcmt.lib.pat
VS10/VC/lib/libcmtd.lib.pat
VS10/VC/lib/libcpmt.lib.pat
VS10/VC/lib/libcpmt1.lib.pat
VS10/VC/lib/libcpmtd.lib.pat
VS10/VC/lib/libcpmtd0.lib.pat
VS10/VC/lib/libcpmtd1.lib.pat
VS10/VC/lib/loosefpmath.obj.pat
VS10/VC/lib/msvcmrt.lib.pat
VS10/VC/lib/msvcmrtd.lib.pat
VS10/VC/lib/msvcprt.lib.pat
VS10/VC/lib/msvcprtd.lib.pat
VS10/VC/lib/msvcrt.lib.pat
VS10/VC/lib/msvcrtd.lib.pat
VS10/VC/lib/msvcurt.lib.pat
VS10/VC/lib/msvcurtd.lib.pat
VS10/VC/lib/newmode.obj.pat
VS10/VC/lib/noarg.obj.pat
VS10/VC/lib/nochkclr.obj.pat
VS10/VC/lib/noenv.obj.pat
VS10/VC/lib/nohetoc.obj.pat
VS10/VC/lib/nothrownew.obj.pat
VS10/VC/lib/oldnames.lib.pat
VS10/VC/lib/pbinmode.obj.pat
VS10/VC/lib/pcommode.obj.pat
VS10/VC/lib/pgobootrun.lib.pat
VS10/VC/lib/pgort.lib.pat
VS10/VC/lib/pinvalidcontinue.obj.pat
VS10/VC/lib/pnewmode.obj.pat
VS10/VC/lib/pnoarg.obj.pat
VS10/VC/lib/pnoenv.obj.pat
VS10/VC/lib/pnothrownew.obj.pat
VS10/VC/lib/psetargv.obj.pat
VS10/VC/lib/pthreadlocale.obj.pat
VS10/VC/lib/ptrustm.lib.pat
VS10/VC/lib/ptrustmd.lib.pat
VS10/VC/lib/ptrustu.lib.pat
VS10/VC/lib/ptrustud.lib.pat
VS10/VC/lib/pwsetargv.obj.pat
VS10/VC/lib/RunTmChk.lib.pat
VS10/VC/lib/setargv.obj.pat
VS10/VC/lib/smalheap.obj.pat
VS10/VC/lib/threadlocale.obj.pat
VS10/VC/lib/vcomp.lib.pat
VS10/VC/lib/vcompd.lib.pat
VS10/VC/lib/wsetargv.obj.pat
```
