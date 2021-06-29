# VS12 / Visual Studio 2013

# download
Visual Studio 2013 Professional
`en_visual_studio_professional_2013_x86_dvd_3175298.iso`

# prepare
run setup

# .lib/.obj
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 12.0/VC/ -iname "*.lib"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/afxnmcd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/afxnmcdd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/afxnmcd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/afxnmcdd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/mfc120u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/mfc120ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/MFCM120U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/MFCM120Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/mfcs120u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/mfcs120ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/amd64/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/arm/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/mfc120u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/mfc120ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/MFCM120U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/MFCM120Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/mfcs120u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/mfcs120ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/atlmfc/lib/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/RunTmChk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/arm/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/store/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/UnitTest/lib/amd64/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/UnitTest/lib/arm/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/UnitTest/lib/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib


$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 12.0/VC/ -iname "*.obj"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/amd64/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/arm/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/fp10.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/nohetoc.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 12.0/VC/lib/wsetargv.obj


$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 12.0/VC/ VS12/
```

```
$ find VS12/ -type f \( -iname "*.lib" -o -iname "*.obj" \) -exec md5sum {} \;
f962e4c018808b195a27306ce64e2c94 *VS12/VC/atlmfc/lib/afxnmcd.lib
a576f3ed95d60f789d180b2b997c7485 *VS12/VC/atlmfc/lib/afxnmcdd.lib
8079e969e8c5c2b58c967f8daa14e890 *VS12/VC/atlmfc/lib/amd64/afxnmcd.lib
6c65e565d8891a26ff4468406a7917d3 *VS12/VC/atlmfc/lib/amd64/afxnmcdd.lib
8290e7ec9ad8428ca79301d57b573a05 *VS12/VC/atlmfc/lib/amd64/atls.lib
7653a935a7af6fbe1444a349ab5a0984 *VS12/VC/atlmfc/lib/amd64/mfc120u.lib
3782415a47474b81a23a671a9edd5918 *VS12/VC/atlmfc/lib/amd64/mfc120ud.lib
ae410e014b92c76eec4167de691e1724 *VS12/VC/atlmfc/lib/amd64/MFCM120U.lib
632dce9fa978cf2768c3e59a3ab43277 *VS12/VC/atlmfc/lib/amd64/MFCM120Ud.lib
089b2353eef13c3b43077e3aa03f0f74 *VS12/VC/atlmfc/lib/amd64/mfcs120u.lib
405778cd4ad8b47f2b6027fb4c1d2a79 *VS12/VC/atlmfc/lib/amd64/mfcs120ud.lib
7d15358e6936dc6efdae9da87723a046 *VS12/VC/atlmfc/lib/amd64/uafxcw.lib
2f3d6acfac7daed3bfef0f995df43195 *VS12/VC/atlmfc/lib/amd64/uafxcwd.lib
5c672d95b9ac2dbbb500be68ad8a322d *VS12/VC/atlmfc/lib/atls.lib
024691ea0b7830a5080ec44c7924fd48 *VS12/VC/atlmfc/lib/mfc120u.lib
ee89e0f4e5e8980189f51862be3cb94b *VS12/VC/atlmfc/lib/mfc120ud.lib
16cfe2e4d7cdb95bda1d95012d237fc2 *VS12/VC/atlmfc/lib/MFCM120U.lib
abaf526dc739910931015a875d9c44d8 *VS12/VC/atlmfc/lib/MFCM120Ud.lib
12fda4cf6b30e7de0a344afcda2dfae7 *VS12/VC/atlmfc/lib/mfcs120u.lib
229222b1ea2fc55a31a99c5b4e42b5e7 *VS12/VC/atlmfc/lib/mfcs120ud.lib
b1ce518f804b6f17c6d71e4087cbd09a *VS12/VC/atlmfc/lib/uafxcw.lib
cbc353f9aa727bc77962db404820c453 *VS12/VC/atlmfc/lib/uafxcwd.lib
5fc1882a51fd6db3fa435b849fbcb91d *VS12/VC/lib/amd64/binmode.obj
e998d64096d12bdd6511267c6bd14500 *VS12/VC/lib/amd64/chkstk.obj
e8a892ecca3a71c25af026982703c2c3 *VS12/VC/lib/amd64/commode.obj
78f28eb86e9ff0690ecb76c7bd43a7d0 *VS12/VC/lib/amd64/comsupp.lib
0c29b6ca4191d7c8b307e8c71de86e4d *VS12/VC/lib/amd64/comsuppd.lib
28d38567436db9ee2313471505fd75a0 *VS12/VC/lib/amd64/comsuppw.lib
a6e5f2b0f422f55cbb8b05c82c1373d8 *VS12/VC/lib/amd64/comsuppwd.lib
a4afdc34c0d9d2b917737fb7ca54118a *VS12/VC/lib/amd64/delayimp.lib
a202a9516e69a9be17e77841e12115af *VS12/VC/lib/amd64/invalidcontinue.obj
ddbdbc8ee25b65d9f907fe03ae4dbe76 *VS12/VC/lib/amd64/libcmt.lib
c2029b8268677cf6a0cde48ae9c41c7a *VS12/VC/lib/amd64/libcmtd.lib
3e180e3a5ef5048c9b121831b5d40413 *VS12/VC/lib/amd64/libcpmt.lib
58eed00bbd2ccb244381c6f65e1aeeaa *VS12/VC/lib/amd64/libcpmt1.lib
bff9427565611ba8b205c06d9f6c5406 *VS12/VC/lib/amd64/libcpmtd.lib
a3a0d2b0badbecd4609f33b406953d20 *VS12/VC/lib/amd64/libcpmtd0.lib
e842063ead0e6c0b9a377d4811ee8fd7 *VS12/VC/lib/amd64/libcpmtd1.lib
56dee89e1f71b1a12b7cc9b35dc3be0c *VS12/VC/lib/amd64/loosefpmath.obj
7158f882e1c5d0be36cba1f36b484174 *VS12/VC/lib/amd64/msvcmrt.lib
3294a294632a16a58c0008b196ae9610 *VS12/VC/lib/amd64/msvcmrtd.lib
adf6d7320f8431901ea684a1b51c185f *VS12/VC/lib/amd64/msvcprt.lib
4440cb998b339932ed199d1491726e66 *VS12/VC/lib/amd64/msvcprtd.lib
42ef3ffe36b890adef8bbbbf2b2d60c7 *VS12/VC/lib/amd64/msvcrt.lib
e86e7e97b49dff5da178711c37edf218 *VS12/VC/lib/amd64/msvcrtd.lib
d9cd84cc802065f24097f370ffc7a9dc *VS12/VC/lib/amd64/msvcurt.lib
42cace273de1c6426a661f62868f750c *VS12/VC/lib/amd64/msvcurtd.lib
46b84e0a8f78d8b11753969668ab9af7 *VS12/VC/lib/amd64/newmode.obj
68057174d579be65a5ed511f8e403005 *VS12/VC/lib/amd64/noarg.obj
73223a0eb7c25ea231bd0b6eb1e45b88 *VS12/VC/lib/amd64/noenv.obj
9955314c786c79326d82d082e538d132 *VS12/VC/lib/amd64/nothrownew.obj
2a22149b203dcaf6f80d5858d7cd3786 *VS12/VC/lib/amd64/oldnames.lib
eb5f921bd71598e383bf616962f739e2 *VS12/VC/lib/amd64/pbinmode.obj
38630ae3dba3c2762523fd72b62f2126 *VS12/VC/lib/amd64/pcommode.obj
2ca7cbbb263278581035863d4535ad1f *VS12/VC/lib/amd64/pgobootrun.lib
f818f9f7ed8fe4cd68d7c097e57d0b9e *VS12/VC/lib/amd64/pgort.lib
3f9da77d2aba94488ca227fd8fd620af *VS12/VC/lib/amd64/pinvalidcontinue.obj
cb490357ac1badf0550148718333ea69 *VS12/VC/lib/amd64/pnewmode.obj
546582c116eb42ec679e99ab182f1eb3 *VS12/VC/lib/amd64/pnoarg.obj
fc3091e7ba96fd2f4cea33f8b044ab39 *VS12/VC/lib/amd64/pnoenv.obj
ad53a8b78285cd12c9bfcdd30ac16bfb *VS12/VC/lib/amd64/pnothrownew.obj
988a90479ed31357cab18435444383a9 *VS12/VC/lib/amd64/psetargv.obj
60a9557aa914bc23a49545fc3db803b5 *VS12/VC/lib/amd64/pthreadlocale.obj
68dd4df1c6707519650790f87c00a0ef *VS12/VC/lib/amd64/ptrustm.lib
8890ff3713689765f7e84e13bbe99615 *VS12/VC/lib/amd64/ptrustmd.lib
4e6aaa7b5cdee120c2df1e24b1f4e461 *VS12/VC/lib/amd64/ptrustu.lib
1b12c5454500c5ea2e96acfc7a3c09a0 *VS12/VC/lib/amd64/ptrustud.lib
605423120174e5f5ce53aaead1e5f149 *VS12/VC/lib/amd64/pwsetargv.obj
1f15efed8ac18e82dc7dcdec43df7657 *VS12/VC/lib/amd64/runtmchk.lib
7cf56d224dd1d43d28a0b8ef1884ae76 *VS12/VC/lib/amd64/setargv.obj
d889631594bcb0a8dfa2f95f98c07b52 *VS12/VC/lib/amd64/smalheap.obj
bad5cbecf3da3a95f8d07e5384537610 *VS12/VC/lib/amd64/threadlocale.obj
ad54a0ca766a68e2c0469af09d86aff9 *VS12/VC/lib/amd64/vcamp.lib
2a2fb49945fd760b754b7a1a198a57bf *VS12/VC/lib/amd64/vcampd.lib
4c099d7ea688918d40feebc2db7d0da6 *VS12/VC/lib/amd64/vccorlib.lib
dd635b73c497fd04b538d7997b808a09 *VS12/VC/lib/amd64/vccorlibd.lib
57c8b1a39525e44a8b5a7fdf8f75a074 *VS12/VC/lib/amd64/vcomp.lib
3d8171d706a79d4db83a8e7cb63214a9 *VS12/VC/lib/amd64/vcompd.lib
1c5d4db36dbab862ee0e7523506956c1 *VS12/VC/lib/amd64/VsGraphicsHelper.lib
73ed9426d4e39d6356de281312959f98 *VS12/VC/lib/amd64/wsetargv.obj
48ea7ad2ddde916587925ed68ee6663a *VS12/VC/lib/binmode.obj
a2a389b532979e5d9909985d1b7d1359 *VS12/VC/lib/chkstk.obj
fb7dabc815d921642bd916c62258c318 *VS12/VC/lib/commode.obj
799cf346740ae58cce7107e55526287d *VS12/VC/lib/comsupp.lib
ea4fd1ce9e1d40a5c07abb53c1b631a7 *VS12/VC/lib/comsuppd.lib
6297dbe83406e8489a43b097432197dc *VS12/VC/lib/comsuppw.lib
6e99537347408fc47ea354078e062b3f *VS12/VC/lib/comsuppwd.lib
38ae210361df2c8c8755b5484befcea1 *VS12/VC/lib/delayimp.lib
68e6e9d0089b5f4fdb1370fb67f279ba *VS12/VC/lib/fp10.obj
72689ebcb74cf4b8259071af05b3886a *VS12/VC/lib/invalidcontinue.obj
112f030229f0403d5617d5692ff65316 *VS12/VC/lib/libcmt.lib
0f00fe36ba33cae9608b95dc9e39b8c3 *VS12/VC/lib/libcmtd.lib
a4735b868c1e5cd3c18fa8b4b6eadb75 *VS12/VC/lib/libcpmt.lib
2ae3b60205f4795f90b873df62f46e09 *VS12/VC/lib/libcpmt1.lib
e78602726fa396735eec0c0caf76aa42 *VS12/VC/lib/libcpmtd.lib
d9df0aac90c328bc1b2f9844e6526207 *VS12/VC/lib/libcpmtd0.lib
c5d9538addd18b75e28f5132345406d7 *VS12/VC/lib/libcpmtd1.lib
2bec045ff9dd295b03dd07282b1f1843 *VS12/VC/lib/loosefpmath.obj
971c04eaedb8417652b1d8c2167caa6e *VS12/VC/lib/msvcmrt.lib
781d4cf77bef264561f04b562ff93b81 *VS12/VC/lib/msvcmrtd.lib
edf5ed4648eeae547032a0143557488d *VS12/VC/lib/msvcprt.lib
157afcfd489c09f202b1372b7066770b *VS12/VC/lib/msvcprtd.lib
8bf2e8bb8815472b3c9cea487c5bbf23 *VS12/VC/lib/msvcrt.lib
7d9d8ad3a5d2092571e062851bafc10c *VS12/VC/lib/msvcrtd.lib
09ef762f303a2e1bb618b3bca7879d71 *VS12/VC/lib/msvcurt.lib
582823dbaefb9e0a115e6822611b235d *VS12/VC/lib/msvcurtd.lib
ddaaa38d31360065025bf8ed8fe2d821 *VS12/VC/lib/newmode.obj
1898520540d142c943c00610c71ac80c *VS12/VC/lib/noarg.obj
2d4443a01b292708cf8561c6e1722566 *VS12/VC/lib/noenv.obj
442125cecdd781f6a97cfef84221bdbd *VS12/VC/lib/nohetoc.obj
858e2424d2278f613b9a190076e21569 *VS12/VC/lib/nothrownew.obj
cda5d8fb76bdfc24416a541901f5f8fe *VS12/VC/lib/oldnames.lib
6a9e39eaec633abb2dc47be89c636bd1 *VS12/VC/lib/pbinmode.obj
edf6395912cbe58410bb082b2fe1a630 *VS12/VC/lib/pcommode.obj
544b70920e5f6a09297b633f58c070a1 *VS12/VC/lib/pgobootrun.lib
a1707aae242fb5e48493252ec76eeff6 *VS12/VC/lib/pgort.lib
1cb69c6920dda231743701d64a8ca481 *VS12/VC/lib/pinvalidcontinue.obj
8a0c12ca943edd0de600f8cde47d044c *VS12/VC/lib/pnewmode.obj
1e41e937c2dc9f92fe52f0f770a5a981 *VS12/VC/lib/pnoarg.obj
6b1b66da8394af238fbf70792ac1c5a1 *VS12/VC/lib/pnoenv.obj
3ee2d829fac3e9d66b550ab67f15da62 *VS12/VC/lib/pnothrownew.obj
9d22c5d48954342fa8e4a11bf6562a27 *VS12/VC/lib/psetargv.obj
48972364bfc50836447a222ba6de1ab9 *VS12/VC/lib/pthreadlocale.obj
36f5de51f984cb078d0c90d3fe929dcc *VS12/VC/lib/ptrustm.lib
039abceced1ba0e4ae5415bdc508578e *VS12/VC/lib/ptrustmd.lib
f0ec991f12c62b995a31b1950f9a1aca *VS12/VC/lib/ptrustu.lib
d201861aa8e22ce0b0a21c3c63ade992 *VS12/VC/lib/ptrustud.lib
1d801862c21d46ac72f1f254f1068742 *VS12/VC/lib/pwsetargv.obj
96872972dbe3d1dc4358adba99ede691 *VS12/VC/lib/RunTmChk.lib
2cc07e412f715c222a1010af18007b95 *VS12/VC/lib/setargv.obj
ad91222488cdb3bf6b745c15956fe8ce *VS12/VC/lib/smalheap.obj
3e5cc2dbbf97542499407e9d51cf9818 *VS12/VC/lib/threadlocale.obj
50afb5f6107cb9836669f3dbfa4735bd *VS12/VC/lib/vcamp.lib
98fa74f0c3a9502aef03f3db6d621bbb *VS12/VC/lib/vcampd.lib
4b4b00cd2091094966ac3015309175bf *VS12/VC/lib/vccorlib.lib
11848bd388709cb526783360e0781f46 *VS12/VC/lib/vccorlibd.lib
0fdc0a182bcfdeaa0f62213716b0df75 *VS12/VC/lib/vcomp.lib
4843252cbeb8b05db1322d1c405e09f6 *VS12/VC/lib/vcompd.lib
c0148433a69f1e4236266ea162770d39 *VS12/VC/lib/VsGraphicsHelper.lib
71218bac11d3ebaf6e9eabb9534b98a3 *VS12/VC/lib/wsetargv.obj
```

# .pat
```
$ find VS12/ -type f -exec ../../pcf.exe {} {}.pat \;
.\VS12\VC\atlmfc\lib\afxnmcd.lib: skipped 11, total 130
.\VS12\VC\atlmfc\lib\afxnmcdd.lib: skipped 0, total 182
.\VS12\VC\atlmfc\lib\amd64\afxnmcd.lib: skipped 33, total 129
.\VS12\VC\atlmfc\lib\amd64\afxnmcdd.lib: skipped 1, total 181
.\VS12\VC\atlmfc\lib\amd64\atls.lib: skipped 26, total 69
.\VS12\VC\atlmfc\lib\amd64\mfc120u.lib: skipped 17284, total 17284
.\VS12\VC\atlmfc\lib\amd64\mfc120ud.lib: skipped 20213, total 20213
.\VS12\VC\atlmfc\lib\amd64\MFCM120U.lib: skipped 27, total 43
.\VS12\VC\atlmfc\lib\amd64\MFCM120Ud.lib: skipped 33, total 49
.\VS12\VC\atlmfc\lib\amd64\mfcs120u.lib: skipped 249, total 838
.\VS12\VC\atlmfc\lib\amd64\mfcs120ud.lib: skipped 28, total 1131
.\VS12\VC\atlmfc\lib\amd64\uafxcw.lib: skipped 6929, total 58334
.\VS12\VC\atlmfc\lib\amd64\uafxcwd.lib: skipped 2249, total 57643
.\VS12\VC\atlmfc\lib\atls.lib: skipped 3, total 1091
.\VS12\VC\atlmfc\lib\mfc120u.lib: skipped 17875, total 17875
.\VS12\VC\atlmfc\lib\mfc120ud.lib: skipped 20840, total 20840
.\VS12\VC\atlmfc\lib\MFCM120U.lib: skipped 27, total 43
.\VS12\VC\atlmfc\lib\MFCM120Ud.lib: skipped 34, total 50
.\VS12\VC\atlmfc\lib\mfcs120u.lib: skipped 66, total 851
.\VS12\VC\atlmfc\lib\mfcs120ud.lib: skipped 28, total 1145
.\VS12\VC\atlmfc\lib\uafxcw.lib: skipped 7736, total 59164
.\VS12\VC\atlmfc\lib\uafxcwd.lib: skipped 2357, total 58553
.\VS12\VC\lib\amd64\binmode.obj: skipped 0, total 0
.\VS12\VC\lib\amd64\chkstk.obj: skipped 0, total 1
.\VS12\VC\lib\amd64\commode.obj: skipped 0, total 0
.\VS12\VC\lib\amd64\comsupp.lib: skipped 0, total 26
.\VS12\VC\lib\amd64\comsuppd.lib: skipped 0, total 28
.\VS12\VC\lib\amd64\comsuppw.lib: skipped 0, total 26
.\VS12\VC\lib\amd64\comsuppwd.lib: skipped 0, total 28
.\VS12\VC\lib\amd64\delayimp.lib: skipped 1, total 21
.\VS12\VC\lib\amd64\invalidcontinue.obj: skipped 1, total 2
.\VS12\VC\lib\amd64\libcmt.lib: skipped 614, total 9170
.\VS12\VC\lib\amd64\libcmtd.lib: skipped 147, total 9546
.\VS12\VC\lib\amd64\libcpmt.lib: skipped 1290, total 10543
.\VS12\VC\lib\amd64\libcpmt1.lib: skipped 1521, total 11322
.\VS12\VC\lib\amd64\libcpmtd.lib: skipped 2, total 12118
.\VS12\VC\lib\amd64\libcpmtd0.lib: skipped 2, total 10923
.\VS12\VC\lib\amd64\libcpmtd1.lib: skipped 2, total 11837
.\VS12\VC\lib\amd64\loosefpmath.obj: skipped 0, total 2
.\VS12\VC\lib\amd64\msvcmrt.lib: skipped 283, total 547
.\VS12\VC\lib\amd64\msvcmrtd.lib: skipped 283, total 570
.\VS12\VC\lib\amd64\msvcprt.lib: skipped 1569, total 1577
.\VS12\VC\lib\amd64\msvcprtd.lib: skipped 1576, total 1591
.\VS12\VC\lib\amd64\msvcrt.lib: skipped 2202, total 2488
.\VS12\VC\lib\amd64\msvcrtd.lib: skipped 2264, total 2554
.\VS12\VC\lib\amd64\msvcurt.lib: skipped 3767, total 25676
.\VS12\VC\lib\amd64\msvcurtd.lib: skipped 3838, total 27106
.\VS12\VC\lib\amd64\newmode.obj: skipped 0, total 0
.\VS12\VC\lib\amd64\noarg.obj: skipped 4, total 4
.\VS12\VC\lib\amd64\noenv.obj: skipped 4, total 4
.\VS12\VC\lib\amd64\nothrownew.obj: skipped 0, total 4
.\VS12\VC\lib\amd64\oldnames.lib: skipped 278, total 278
.\VS12\VC\lib\amd64\pbinmode.obj: skipped 0, total 3
.\VS12\VC\lib\amd64\pcommode.obj: skipped 0, total 1
.\VS12\VC\lib\amd64\pgobootrun.lib: skipped 2, total 2
.\VS12\VC\lib\amd64\pgort.lib: skipped 8, total 14
.\VS12\VC\lib\amd64\pinvalidcontinue.obj: skipped 0, total 6
.\VS12\VC\lib\amd64\pnewmode.obj: skipped 0, total 1
.\VS12\VC\lib\amd64\pnoarg.obj: skipped 0, total 4
.\VS12\VC\lib\amd64\pnoenv.obj: skipped 0, total 6
.\VS12\VC\lib\amd64\pnothrownew.obj: skipped 0, total 6
.\VS12\VC\lib\amd64\psetargv.obj: skipped 0, total 1
.\VS12\VC\lib\amd64\pthreadlocale.obj: skipped 0, total 1
.\VS12\VC\lib\amd64\ptrustm.lib: skipped 0, total 173
.\VS12\VC\lib\amd64\ptrustmd.lib: skipped 0, total 174
.\VS12\VC\lib\amd64\ptrustu.lib: skipped 0, total 83
.\VS12\VC\lib\amd64\ptrustud.lib: skipped 0, total 83
.\VS12\VC\lib\amd64\pwsetargv.obj: skipped 0, total 1
.\VS12\VC\lib\amd64\runtmchk.lib: skipped 0, total 98
.\VS12\VC\lib\amd64\setargv.obj: skipped 0, total 1
.\VS12\VC\lib\amd64\smalheap.obj: skipped 0, total 12
.\VS12\VC\lib\amd64\threadlocale.obj: skipped 0, total 0
.\VS12\VC\lib\amd64\vcamp.lib: skipped 165, total 165
.\VS12\VC\lib\amd64\vcampd.lib: skipped 166, total 166
.\VS12\VC\lib\amd64\vccorlib.lib: skipped 429, total 4898
.\VS12\VC\lib\amd64\vccorlibd.lib: skipped 281, total 4910
.\VS12\VC\lib\amd64\vcomp.lib: skipped 113, total 113
.\VS12\VC\lib\amd64\vcompd.lib: skipped 113, total 113
.\VS12\VC\lib\amd64\VsGraphicsHelper.lib: skipped 10, total 10
.\VS12\VC\lib\amd64\wsetargv.obj: skipped 0, total 1
.\VS12\VC\lib\binmode.obj: skipped 0, total 0
.\VS12\VC\lib\chkstk.obj: skipped 0, total 1
.\VS12\VC\lib\commode.obj: skipped 0, total 0
.\VS12\VC\lib\comsupp.lib: skipped 0, total 26
.\VS12\VC\lib\comsuppd.lib: skipped 0, total 26
.\VS12\VC\lib\comsuppw.lib: skipped 0, total 26
.\VS12\VC\lib\comsuppwd.lib: skipped 0, total 26
.\VS12\VC\lib\delayimp.lib: skipped 0, total 21
.\VS12\VC\lib\fp10.obj: skipped 0, total 2
.\VS12\VC\lib\invalidcontinue.obj: skipped 1, total 2
.\VS12\VC\lib\libcmt.lib: skipped 662, total 9232
.\VS12\VC\lib\libcmtd.lib: skipped 134, total 9591
.\VS12\VC\lib\libcpmt.lib: skipped 1042, total 10522
.\VS12\VC\lib\libcpmt1.lib: skipped 1235, total 11302
.\VS12\VC\lib\libcpmtd.lib: skipped 1, total 12219
.\VS12\VC\lib\libcpmtd0.lib: skipped 1, total 11024
.\VS12\VC\lib\libcpmtd1.lib: skipped 1, total 11938
.\VS12\VC\lib\loosefpmath.obj: skipped 0, total 2
.\VS12\VC\lib\msvcmrt.lib: skipped 285, total 549
.\VS12\VC\lib\msvcmrtd.lib: skipped 285, total 572
.\VS12\VC\lib\msvcprt.lib: skipped 1569, total 1577
.\VS12\VC\lib\msvcprtd.lib: skipped 1580, total 1595
.\VS12\VC\lib\msvcrt.lib: skipped 2248, total 2549
.\VS12\VC\lib\msvcrtd.lib: skipped 2309, total 2616
.\VS12\VC\lib\msvcurt.lib: skipped 3813, total 25722
.\VS12\VC\lib\msvcurtd.lib: skipped 3889, total 27241
.\VS12\VC\lib\newmode.obj: skipped 0, total 0
.\VS12\VC\lib\noarg.obj: skipped 4, total 4
.\VS12\VC\lib\noenv.obj: skipped 4, total 4
.\VS12\VC\lib\nohetoc.obj: skipped 0, total 0
.\VS12\VC\lib\nothrownew.obj: skipped 0, total 4
.\VS12\VC\lib\oldnames.lib: skipped 278, total 278
.\VS12\VC\lib\pbinmode.obj: skipped 0, total 3
.\VS12\VC\lib\pcommode.obj: skipped 0, total 1
.\VS12\VC\lib\pgobootrun.lib: skipped 2, total 2
.\VS12\VC\lib\pgort.lib: skipped 11, total 22
.\VS12\VC\lib\pinvalidcontinue.obj: skipped 0, total 6
.\VS12\VC\lib\pnewmode.obj: skipped 0, total 1
.\VS12\VC\lib\pnoarg.obj: skipped 0, total 4
.\VS12\VC\lib\pnoenv.obj: skipped 0, total 6
.\VS12\VC\lib\pnothrownew.obj: skipped 0, total 6
.\VS12\VC\lib\psetargv.obj: skipped 0, total 1
.\VS12\VC\lib\pthreadlocale.obj: skipped 0, total 1
.\VS12\VC\lib\ptrustm.lib: skipped 0, total 173
.\VS12\VC\lib\ptrustmd.lib: skipped 0, total 174
.\VS12\VC\lib\ptrustu.lib: skipped 0, total 83
.\VS12\VC\lib\ptrustud.lib: skipped 0, total 83
.\VS12\VC\lib\pwsetargv.obj: skipped 0, total 1
.\VS12\VC\lib\RunTmChk.lib: skipped 1, total 103
.\VS12\VC\lib\setargv.obj: skipped 0, total 1
.\VS12\VC\lib\smalheap.obj: skipped 0, total 12
.\VS12\VC\lib\threadlocale.obj: skipped 0, total 0
.\VS12\VC\lib\vcamp.lib: skipped 165, total 165
.\VS12\VC\lib\vcampd.lib: skipped 166, total 166
.\VS12\VC\lib\vccorlib.lib: skipped 319, total 4860
.\VS12\VC\lib\vccorlibd.lib: skipped 281, total 4915
.\VS12\VC\lib\vcomp.lib: skipped 113, total 113
.\VS12\VC\lib\vcompd.lib: skipped 113, total 113
.\VS12\VC\lib\VsGraphicsHelper.lib: skipped 10, total 10
.\VS12\VC\lib\wsetargv.obj: skipped 0, total 1
```

```
$ find VS12 -name '*.pat' -print0 | tar -czvf VS12/VS12.tar.gz --null -T -
VS12/VC/atlmfc/lib/afxnmcd.lib.pat
VS12/VC/atlmfc/lib/afxnmcdd.lib.pat
VS12/VC/atlmfc/lib/amd64/afxnmcd.lib.pat
VS12/VC/atlmfc/lib/amd64/afxnmcdd.lib.pat
VS12/VC/atlmfc/lib/amd64/atls.lib.pat
VS12/VC/atlmfc/lib/amd64/mfc120u.lib.pat
VS12/VC/atlmfc/lib/amd64/mfc120ud.lib.pat
VS12/VC/atlmfc/lib/amd64/MFCM120U.lib.pat
VS12/VC/atlmfc/lib/amd64/MFCM120Ud.lib.pat
VS12/VC/atlmfc/lib/amd64/mfcs120u.lib.pat
VS12/VC/atlmfc/lib/amd64/mfcs120ud.lib.pat
VS12/VC/atlmfc/lib/amd64/uafxcw.lib.pat
VS12/VC/atlmfc/lib/amd64/uafxcwd.lib.pat
VS12/VC/atlmfc/lib/atls.lib.pat
VS12/VC/atlmfc/lib/mfc120u.lib.pat
VS12/VC/atlmfc/lib/mfc120ud.lib.pat
VS12/VC/atlmfc/lib/MFCM120U.lib.pat
VS12/VC/atlmfc/lib/MFCM120Ud.lib.pat
VS12/VC/atlmfc/lib/mfcs120u.lib.pat
VS12/VC/atlmfc/lib/mfcs120ud.lib.pat
VS12/VC/atlmfc/lib/uafxcw.lib.pat
VS12/VC/atlmfc/lib/uafxcwd.lib.pat
VS12/VC/lib/amd64/binmode.obj.pat
VS12/VC/lib/amd64/chkstk.obj.pat
VS12/VC/lib/amd64/commode.obj.pat
VS12/VC/lib/amd64/comsupp.lib.pat
VS12/VC/lib/amd64/comsuppd.lib.pat
VS12/VC/lib/amd64/comsuppw.lib.pat
VS12/VC/lib/amd64/comsuppwd.lib.pat
VS12/VC/lib/amd64/delayimp.lib.pat
VS12/VC/lib/amd64/invalidcontinue.obj.pat
VS12/VC/lib/amd64/libcmt.lib.pat
VS12/VC/lib/amd64/libcmtd.lib.pat
VS12/VC/lib/amd64/libcpmt.lib.pat
VS12/VC/lib/amd64/libcpmt1.lib.pat
VS12/VC/lib/amd64/libcpmtd.lib.pat
VS12/VC/lib/amd64/libcpmtd0.lib.pat
VS12/VC/lib/amd64/libcpmtd1.lib.pat
VS12/VC/lib/amd64/loosefpmath.obj.pat
VS12/VC/lib/amd64/msvcmrt.lib.pat
VS12/VC/lib/amd64/msvcmrtd.lib.pat
VS12/VC/lib/amd64/msvcprt.lib.pat
VS12/VC/lib/amd64/msvcprtd.lib.pat
VS12/VC/lib/amd64/msvcrt.lib.pat
VS12/VC/lib/amd64/msvcrtd.lib.pat
VS12/VC/lib/amd64/msvcurt.lib.pat
VS12/VC/lib/amd64/msvcurtd.lib.pat
VS12/VC/lib/amd64/newmode.obj.pat
VS12/VC/lib/amd64/noarg.obj.pat
VS12/VC/lib/amd64/noenv.obj.pat
VS12/VC/lib/amd64/nothrownew.obj.pat
VS12/VC/lib/amd64/oldnames.lib.pat
VS12/VC/lib/amd64/pbinmode.obj.pat
VS12/VC/lib/amd64/pcommode.obj.pat
VS12/VC/lib/amd64/pgobootrun.lib.pat
VS12/VC/lib/amd64/pgort.lib.pat
VS12/VC/lib/amd64/pinvalidcontinue.obj.pat
VS12/VC/lib/amd64/pnewmode.obj.pat
VS12/VC/lib/amd64/pnoarg.obj.pat
VS12/VC/lib/amd64/pnoenv.obj.pat
VS12/VC/lib/amd64/pnothrownew.obj.pat
VS12/VC/lib/amd64/psetargv.obj.pat
VS12/VC/lib/amd64/pthreadlocale.obj.pat
VS12/VC/lib/amd64/ptrustm.lib.pat
VS12/VC/lib/amd64/ptrustmd.lib.pat
VS12/VC/lib/amd64/ptrustu.lib.pat
VS12/VC/lib/amd64/ptrustud.lib.pat
VS12/VC/lib/amd64/pwsetargv.obj.pat
VS12/VC/lib/amd64/runtmchk.lib.pat
VS12/VC/lib/amd64/setargv.obj.pat
VS12/VC/lib/amd64/smalheap.obj.pat
VS12/VC/lib/amd64/threadlocale.obj.pat
VS12/VC/lib/amd64/vcamp.lib.pat
VS12/VC/lib/amd64/vcampd.lib.pat
VS12/VC/lib/amd64/vccorlib.lib.pat
VS12/VC/lib/amd64/vccorlibd.lib.pat
VS12/VC/lib/amd64/vcomp.lib.pat
VS12/VC/lib/amd64/vcompd.lib.pat
VS12/VC/lib/amd64/VsGraphicsHelper.lib.pat
VS12/VC/lib/amd64/wsetargv.obj.pat
VS12/VC/lib/binmode.obj.pat
VS12/VC/lib/chkstk.obj.pat
VS12/VC/lib/commode.obj.pat
VS12/VC/lib/comsupp.lib.pat
VS12/VC/lib/comsuppd.lib.pat
VS12/VC/lib/comsuppw.lib.pat
VS12/VC/lib/comsuppwd.lib.pat
VS12/VC/lib/delayimp.lib.pat
VS12/VC/lib/fp10.obj.pat
VS12/VC/lib/invalidcontinue.obj.pat
VS12/VC/lib/libcmt.lib.pat
VS12/VC/lib/libcmtd.lib.pat
VS12/VC/lib/libcpmt.lib.pat
VS12/VC/lib/libcpmt1.lib.pat
VS12/VC/lib/libcpmtd.lib.pat
VS12/VC/lib/libcpmtd0.lib.pat
VS12/VC/lib/libcpmtd1.lib.pat
VS12/VC/lib/loosefpmath.obj.pat
VS12/VC/lib/msvcmrt.lib.pat
VS12/VC/lib/msvcmrtd.lib.pat
VS12/VC/lib/msvcprt.lib.pat
VS12/VC/lib/msvcprtd.lib.pat
VS12/VC/lib/msvcrt.lib.pat
VS12/VC/lib/msvcrtd.lib.pat
VS12/VC/lib/msvcurt.lib.pat
VS12/VC/lib/msvcurtd.lib.pat
VS12/VC/lib/newmode.obj.pat
VS12/VC/lib/noarg.obj.pat
VS12/VC/lib/noenv.obj.pat
VS12/VC/lib/nohetoc.obj.pat
VS12/VC/lib/nothrownew.obj.pat
VS12/VC/lib/oldnames.lib.pat
VS12/VC/lib/pbinmode.obj.pat
VS12/VC/lib/pcommode.obj.pat
VS12/VC/lib/pgobootrun.lib.pat
VS12/VC/lib/pgort.lib.pat
VS12/VC/lib/pinvalidcontinue.obj.pat
VS12/VC/lib/pnewmode.obj.pat
VS12/VC/lib/pnoarg.obj.pat
VS12/VC/lib/pnoenv.obj.pat
VS12/VC/lib/pnothrownew.obj.pat
VS12/VC/lib/psetargv.obj.pat
VS12/VC/lib/pthreadlocale.obj.pat
VS12/VC/lib/ptrustm.lib.pat
VS12/VC/lib/ptrustmd.lib.pat
VS12/VC/lib/ptrustu.lib.pat
VS12/VC/lib/ptrustud.lib.pat
VS12/VC/lib/pwsetargv.obj.pat
VS12/VC/lib/RunTmChk.lib.pat
VS12/VC/lib/setargv.obj.pat
VS12/VC/lib/smalheap.obj.pat
VS12/VC/lib/threadlocale.obj.pat
VS12/VC/lib/vcamp.lib.pat
VS12/VC/lib/vcampd.lib.pat
VS12/VC/lib/vccorlib.lib.pat
VS12/VC/lib/vccorlibd.lib.pat
VS12/VC/lib/vcomp.lib.pat
VS12/VC/lib/vcompd.lib.pat
VS12/VC/lib/VsGraphicsHelper.lib.pat
VS12/VC/lib/wsetargv.obj.pat
```
