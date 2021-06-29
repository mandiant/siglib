# VS11 / Visual Studio 2012

# download
Visual Studio 2012 Professional
`en_visual_studio_professional_2012_x86_dvd_2262334.iso`

# prepare
run `setup.exe`

# .lib/.obj
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 11.0/VC/ -iname "*.lib"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/afxnmcd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/afxnmcdd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/afxnmcd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/afxnmcdd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atlsn.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/atlsnd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfc110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfc110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfc110u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfc110ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/MFCM110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/MFCM110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/MFCM110U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/MFCM110Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfcs110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfcs110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfcs110u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/mfcs110ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/amd64/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atlsn.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/arm/atlsnd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/Atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/atlsn.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/atlsnd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfc110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfc110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfc110u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfc110ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/MFCM110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/MFCM110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/MFCM110U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/MFCM110Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfcs110.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfcs110d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfcs110u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/mfcs110ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/atlmfc/lib/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmt1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmtd0.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/libcpmtd1.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/RunTmChk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vcamp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vcampd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vccorlib.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vccorlibd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/VsGraphicsHelper.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/UnitTest/lib/amd64/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/UnitTest/lib/arm/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/UnitTest/lib/Microsoft.VisualStudio.TestTools.CppUnitTestFramework.lib
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 11.0/VC/ -iname "*.obj"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/amd64/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/arm/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/fp10.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/nohetoc.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 11.0/VC/lib/wsetargv.obj


$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 11.0/VC/ VS11/
```

```
$ find VS11/ -type f \( -iname "*.lib" -o -iname "*.obj" \) -exec md5sum {} \;
6a55371a39e115d49429b40c5576fbab *VS11/VC/atlmfc/lib/afxnmcd.lib
39a23f4201c98339334939404f3dc26b *VS11/VC/atlmfc/lib/afxnmcdd.lib
2366bef898eebb1fb7bce2eef90eabfe *VS11/VC/atlmfc/lib/amd64/afxnmcd.lib
5a31ac5afc550c0320646121a9132d5f *VS11/VC/atlmfc/lib/amd64/afxnmcdd.lib
18c82a1253989757d1384e3e3ccfe30d *VS11/VC/atlmfc/lib/amd64/atl.lib
5b120ab904baa323614232b0284991a7 *VS11/VC/atlmfc/lib/amd64/atls.lib
f7523f8341f54ed12296651e9d34a926 *VS11/VC/atlmfc/lib/amd64/atlsd.lib
8385152ee56ccad1f8365d50e847733e *VS11/VC/atlmfc/lib/amd64/atlsn.lib
5a0bbb98e69d2f9f36a1d8f8c99b1416 *VS11/VC/atlmfc/lib/amd64/atlsnd.lib
81890d25d2d5c1c7755cb00a76081293 *VS11/VC/atlmfc/lib/amd64/mfc110.lib
0eb3255787923c64f926e11976b0adc3 *VS11/VC/atlmfc/lib/amd64/mfc110d.lib
eabf900c12b7f98fba1f9ae10c2cc832 *VS11/VC/atlmfc/lib/amd64/mfc110u.lib
e7c4de8ef1d92374d0b9cbfedccf63ce *VS11/VC/atlmfc/lib/amd64/mfc110ud.lib
a3df63a40bc54246038087c61dd076b5 *VS11/VC/atlmfc/lib/amd64/MFCM110.lib
5539b39a5d04458f52379bf0a8d41405 *VS11/VC/atlmfc/lib/amd64/MFCM110d.lib
2f358becf4c9eeaf95f59e8c94bd17a7 *VS11/VC/atlmfc/lib/amd64/MFCM110U.lib
ce252a24d2f94b53a66534c6a3fa380f *VS11/VC/atlmfc/lib/amd64/MFCM110Ud.lib
6e38aa06a31dc65450d2ea4396e4530c *VS11/VC/atlmfc/lib/amd64/mfcs110.lib
aa567b22aed4ffd066f0510695128d84 *VS11/VC/atlmfc/lib/amd64/mfcs110d.lib
5115992e24975e68d6f6527a21a2e45b *VS11/VC/atlmfc/lib/amd64/mfcs110u.lib
d328448d6a5b9a9430134ab2070f7ce9 *VS11/VC/atlmfc/lib/amd64/mfcs110ud.lib
03e84ba5ca5dbd97f7c48daae9604787 *VS11/VC/atlmfc/lib/amd64/nafxcw.lib
0731eff328fd2cb3fd65a87af80726d4 *VS11/VC/atlmfc/lib/amd64/nafxcwd.lib
87fe3b76c6912ccedea721d9f4ab5467 *VS11/VC/atlmfc/lib/amd64/uafxcw.lib
c67dfbe1a481178e88416da795304448 *VS11/VC/atlmfc/lib/amd64/uafxcwd.lib
8dbe4d09ab2752640b1acc3667bb111e *VS11/VC/atlmfc/lib/Atl.lib
95acef05b8bfce40954e510d46fffc80 *VS11/VC/atlmfc/lib/atls.lib
dcba4fb5086a5b84656fe87322236d80 *VS11/VC/atlmfc/lib/atlsd.lib
b8c9ff7e416c0939524565bf20359224 *VS11/VC/atlmfc/lib/atlsn.lib
528d495271c6f1122026006cdda6845c *VS11/VC/atlmfc/lib/atlsnd.lib
6e4e5197dfc3d7421e634105af8beddd *VS11/VC/atlmfc/lib/mfc110.lib
99292961ec7a79ffd422c979c3df85a5 *VS11/VC/atlmfc/lib/mfc110d.lib
da89af93ac277125b6f2f93e81bdf411 *VS11/VC/atlmfc/lib/mfc110u.lib
ec5edf56c77d4160a5ac1c290be4e4ef *VS11/VC/atlmfc/lib/mfc110ud.lib
68bfa5f54ba55f43fdf81e0f11adf74e *VS11/VC/atlmfc/lib/MFCM110.lib
871d4b2469a023b0a202f1ba7fd2b53c *VS11/VC/atlmfc/lib/MFCM110d.lib
d1fe42081228739e04d95776dccb43ed *VS11/VC/atlmfc/lib/MFCM110U.lib
2e92735c04cfba3b8e30d6042eaa93d5 *VS11/VC/atlmfc/lib/MFCM110Ud.lib
6f594da24c079ff13bb0c77177f168b8 *VS11/VC/atlmfc/lib/mfcs110.lib
ebbeea335c6c4dca7a2a1408dcba7455 *VS11/VC/atlmfc/lib/mfcs110d.lib
ce7302938671eea4f32d1a893265689f *VS11/VC/atlmfc/lib/mfcs110u.lib
fac887e4a843e545cfac73234b67facb *VS11/VC/atlmfc/lib/mfcs110ud.lib
b8d19675548de08f6e53a06c3d630a5c *VS11/VC/atlmfc/lib/nafxcw.lib
402a75b300b73b91cc9b8234510d355b *VS11/VC/atlmfc/lib/nafxcwd.lib
328a5b35ac6917804102e5ba2188da9e *VS11/VC/atlmfc/lib/uafxcw.lib
8e1e7584523dfd71499b37767edf68ce *VS11/VC/atlmfc/lib/uafxcwd.lib
f2ed930fa90b88c13865ec9be65e3251 *VS11/VC/lib/amd64/binmode.obj
1ac2564f9764271b498ea74be0ad955e *VS11/VC/lib/amd64/chkstk.obj
4793215182e64bca25afbd947d1e872b *VS11/VC/lib/amd64/commode.obj
d84fede466fdf6eaf12e03ab5d1b74cc *VS11/VC/lib/amd64/comsupp.lib
0dfae038c67e785737b55f053dd890b9 *VS11/VC/lib/amd64/comsuppd.lib
a35618746b017aac71932a1b3c453a25 *VS11/VC/lib/amd64/comsuppw.lib
8659a06b6a23f6897998d0e807e51cac *VS11/VC/lib/amd64/comsuppwd.lib
033a0d7cd5cb7c2fb08a9d9ce41c06c6 *VS11/VC/lib/amd64/delayimp.lib
272e42eb03c624f2e23474d86ce89933 *VS11/VC/lib/amd64/invalidcontinue.obj
625c7d7a45e810e39da0e3459e8f8091 *VS11/VC/lib/amd64/libcmt.lib
84782cd8084001b30bdf133525cdae01 *VS11/VC/lib/amd64/libcmtd.lib
b6f20a821197699cd2d2dbcb93c6a4ef *VS11/VC/lib/amd64/libcpmt.lib
25d9e78773a3d62b0ca60c3fdb4bfe38 *VS11/VC/lib/amd64/libcpmt1.lib
17974debb1007b308afdc12e6c36afb6 *VS11/VC/lib/amd64/libcpmtd.lib
fb9b43c4aa68d8ef0c3637005fde9ee3 *VS11/VC/lib/amd64/libcpmtd0.lib
44fd1f6f6ee715017b76498e7d121b13 *VS11/VC/lib/amd64/libcpmtd1.lib
e379ae7afe7c00f75b4c513530656492 *VS11/VC/lib/amd64/loosefpmath.obj
e8ce196212fc8c549f967a1469736dcf *VS11/VC/lib/amd64/msvcmrt.lib
4fd3d6a5d8f8f7c8af4743fa2ffe0393 *VS11/VC/lib/amd64/msvcmrtd.lib
91e532e859b36cdc6f99be11efd1a17d *VS11/VC/lib/amd64/msvcprt.lib
d858184fc6f3669fe749b5c6be12946e *VS11/VC/lib/amd64/msvcprtd.lib
d75c651ddc1c864c9f162ac4509c63a7 *VS11/VC/lib/amd64/msvcrt.lib
656b5599c3f3dba04e4cf0876e477169 *VS11/VC/lib/amd64/msvcrtd.lib
62a2380a4844f8bff0625b59a350a138 *VS11/VC/lib/amd64/msvcurt.lib
855bce1a7c2eb1e68db3534a4a8dd5bb *VS11/VC/lib/amd64/msvcurtd.lib
2cbd7b008881f267bed96242854234c1 *VS11/VC/lib/amd64/newmode.obj
316979df81271165de8d60713561b2ea *VS11/VC/lib/amd64/noarg.obj
6a7123cdfa423f423b559dec8442ada1 *VS11/VC/lib/amd64/noenv.obj
123efb9e9215da1f6062503df29dc676 *VS11/VC/lib/amd64/nothrownew.obj
be6f783c8fe8900c71e737ac90b7ce47 *VS11/VC/lib/amd64/oldnames.lib
02e19caaabef9dec97f482eb5db1caee *VS11/VC/lib/amd64/pbinmode.obj
f9fc53d21a1a8782d5a46bd1a70c7276 *VS11/VC/lib/amd64/pcommode.obj
e128b423bdd564dcfc01632e86fe8dce *VS11/VC/lib/amd64/pgobootrun.lib
d3a1f08026607ef13982e0058e06fe09 *VS11/VC/lib/amd64/pgort.lib
958f06ac5f04352de765c22f3f358cad *VS11/VC/lib/amd64/pinvalidcontinue.obj
17e94de9bfb9dbad368b28d2af3260f8 *VS11/VC/lib/amd64/pnewmode.obj
566555f2d19f38daea5ab5e24aeb3c99 *VS11/VC/lib/amd64/pnoarg.obj
c4300e9c96873c11b0605c3ecf380abc *VS11/VC/lib/amd64/pnoenv.obj
614c47d8728406ae3412af3a7b4f0856 *VS11/VC/lib/amd64/pnothrownew.obj
52f08d4363a8322f8f03dbc56423edc0 *VS11/VC/lib/amd64/psetargv.obj
af04c0682f06ff99441a0f1f259bac13 *VS11/VC/lib/amd64/pthreadlocale.obj
afbf9d89563b66ac9cc6104ca81a8b3a *VS11/VC/lib/amd64/ptrustm.lib
b1cb92c8f1467b7c6416a4f1e9994082 *VS11/VC/lib/amd64/ptrustmd.lib
54d5d8d0ea005075d1457057ab1e1131 *VS11/VC/lib/amd64/ptrustu.lib
9238f2890eb0943fca782e840fb5a9b7 *VS11/VC/lib/amd64/ptrustud.lib
3f7f142fea85e658a76585526daeadfa *VS11/VC/lib/amd64/pwsetargv.obj
d2cddec05ac83d5fc01e92ce91004524 *VS11/VC/lib/amd64/runtmchk.lib
e38c9fae15cf207687add88a2f8fd627 *VS11/VC/lib/amd64/setargv.obj
d3a0d64b40c49ca67c950082d50b6d46 *VS11/VC/lib/amd64/smalheap.obj
0329fc2a8d5776395140d3a51449c925 *VS11/VC/lib/amd64/threadlocale.obj
05df2dcbf19c34b1baf7cd1bba4ecd5f *VS11/VC/lib/amd64/vcamp.lib
b775d6085a0ca3fe6a5ad058673637bb *VS11/VC/lib/amd64/vcampd.lib
2a7d974bda58a3b71a960629f3ae6721 *VS11/VC/lib/amd64/vccorlib.lib
6a649bf4dffb5755a22972a9869e192a *VS11/VC/lib/amd64/vccorlibd.lib
ff571af5fd355318e6091bda9478d6d9 *VS11/VC/lib/amd64/vcomp.lib
b99077d2191103dd2449c4331a33a78f *VS11/VC/lib/amd64/vcompd.lib
f2b00fc4aca63c161fb1d27435ea514c *VS11/VC/lib/amd64/VsGraphicsHelper.lib
267137e35aa33873724ca82dc05981b1 *VS11/VC/lib/amd64/wsetargv.obj
5d4832f50269a290c14188f5eb07b9a5 *VS11/VC/lib/binmode.obj
4dd2705b82ca1571336b9172e1a5d62d *VS11/VC/lib/chkstk.obj
801b9a6b5053b0a6b3e6048a6bcd8789 *VS11/VC/lib/commode.obj
adc163b584c8bb7925446aba6a8a1d20 *VS11/VC/lib/comsupp.lib
52515e37d569f61b02ea79c61438eeb7 *VS11/VC/lib/comsuppd.lib
a22ac8a610c274d0ea00c6b370f0dfdb *VS11/VC/lib/comsuppw.lib
f959e078497abc82a29be076700e6161 *VS11/VC/lib/comsuppwd.lib
12e0a2f86c9d00fe9fc1f4a34eedffe3 *VS11/VC/lib/delayimp.lib
d372a0a6ea9474690297c606fa4817cd *VS11/VC/lib/fp10.obj
19ac6c64e778c0b2665314487698234c *VS11/VC/lib/invalidcontinue.obj
e9c06eb62fc3a90eb4d4f3cd16fadd1b *VS11/VC/lib/libcmt.lib
8d367236bedd1461348971d888749740 *VS11/VC/lib/libcmtd.lib
6107a7b9cac8acf4bc18d1a8099c7416 *VS11/VC/lib/libcpmt.lib
61048d8a9090112e8665e92b4bacf419 *VS11/VC/lib/libcpmt1.lib
2271770d19f55f52b878aa57bf0a5267 *VS11/VC/lib/libcpmtd.lib
fcbab6878371f2b1e37299d98c40e340 *VS11/VC/lib/libcpmtd0.lib
89046c7b1ce92cc74ea95c8ebadaf72c *VS11/VC/lib/libcpmtd1.lib
0e7516692b571b9a587ee2147477926f *VS11/VC/lib/loosefpmath.obj
17b59912e897a651396e59e73036dc34 *VS11/VC/lib/msvcmrt.lib
a88cbccbe18a730e693e2d8324ee534d *VS11/VC/lib/msvcmrtd.lib
540095f4376282444a96e5f315835347 *VS11/VC/lib/msvcprt.lib
0cb0cda4453162a67b952b4761bc1c74 *VS11/VC/lib/msvcprtd.lib
f0271eda37dd690112b0d34e73ddbfff *VS11/VC/lib/msvcrt.lib
6516a12b9ea118431533e3c97c4ded80 *VS11/VC/lib/msvcrtd.lib
1cece1efb82c18cbe59d07db37a2b1f4 *VS11/VC/lib/msvcurt.lib
1cbd218b140786941bd5f580e92a6091 *VS11/VC/lib/msvcurtd.lib
e28483ee555d2153e61e01fe064b8733 *VS11/VC/lib/newmode.obj
fc2b63281034873e02322349dde7b202 *VS11/VC/lib/noarg.obj
7ac7c62653d3c5c9087f157ec0bb8f1f *VS11/VC/lib/noenv.obj
e21ffed6698901f045fa8f18e87c9fdb *VS11/VC/lib/nohetoc.obj
9c42cf0d3e8b53fc8bc3ce4f9b5a3266 *VS11/VC/lib/nothrownew.obj
59442d701f221d9b4b5f03aedaca8ae1 *VS11/VC/lib/oldnames.lib
70bf739ef02e6cfea8f7436324e0657e *VS11/VC/lib/pbinmode.obj
06449815d5c8061771c3525a2206b51a *VS11/VC/lib/pcommode.obj
62aedd4a83e88efaa9b4c1e5b5326793 *VS11/VC/lib/pgobootrun.lib
b8b46bde19c91c0558dcd09161acee14 *VS11/VC/lib/pgort.lib
b1cfb6aead43b012004328e6c04b76f3 *VS11/VC/lib/pinvalidcontinue.obj
b995891c2d3bc6a681e3eacdad4c3a4a *VS11/VC/lib/pnewmode.obj
79bba7c0073c2feb807d13cb81b37535 *VS11/VC/lib/pnoarg.obj
4dbf7333fbbdfd4f5d26f3b55f5d1209 *VS11/VC/lib/pnoenv.obj
c20b15e4406792897daedd0ace7237bd *VS11/VC/lib/pnothrownew.obj
11669a89aa2b6401afaa4c28d1273e98 *VS11/VC/lib/psetargv.obj
3b259d3aa444ef706fa5a8845f5cc456 *VS11/VC/lib/pthreadlocale.obj
897114493bb2affb0d192f5fa04632c4 *VS11/VC/lib/ptrustm.lib
4d73081800e8bd44feda310b975b21c7 *VS11/VC/lib/ptrustmd.lib
29861c8cf5b53aa340896370bf41a5dd *VS11/VC/lib/ptrustu.lib
f4144036f53921f1e9edaf683a093ced *VS11/VC/lib/ptrustud.lib
8fa36df5f57a3b115fff3d2a8b8ac600 *VS11/VC/lib/pwsetargv.obj
766c4004cf5dc4919fb586f2ae880741 *VS11/VC/lib/RunTmChk.lib
8d4970f6eded7c1004fc3ef095c9d95c *VS11/VC/lib/setargv.obj
f3052e3e02d07a6899391f9e309cd57b *VS11/VC/lib/smalheap.obj
8c07b37f6186b2c9158aef085826884d *VS11/VC/lib/threadlocale.obj
42a8cb90e58f27090d95a200e4421c23 *VS11/VC/lib/vcamp.lib
296cb8553f3084cddc745aed19ae02bf *VS11/VC/lib/vcampd.lib
49486c391e4e5f14d6bdb391e1b177a8 *VS11/VC/lib/vccorlib.lib
06d2ce4a6d36d7ee91319b0cd3aad468 *VS11/VC/lib/vccorlibd.lib
fa2fef6ad401ebe6dea43a1108d44986 *VS11/VC/lib/vcomp.lib
80f94586514c1315d794d5e462965a79 *VS11/VC/lib/vcompd.lib
aeba5dad926799ee230c1d506aed6028 *VS11/VC/lib/VsGraphicsHelper.lib
6d0cffa77da8a3d5580b74adfb3b2297 *VS11/VC/lib/wsetargv.obj
```

# .pat
```
$ find VS11/ -type f -exec ../../pcf.exe {} {}.pat \;
.\VS11\VC\atlmfc\lib\afxnmcd.lib: skipped 6, total 37
.\VS11\VC\atlmfc\lib\afxnmcdd.lib: skipped 0, total 40
.\VS11\VC\atlmfc\lib\amd64\afxnmcd.lib: skipped 5, total 38
.\VS11\VC\atlmfc\lib\amd64\afxnmcdd.lib: skipped 1, total 41
.\VS11\VC\atlmfc\lib\amd64\atl.lib: skipped 52, total 52
.\VS11\VC\atlmfc\lib\amd64\atls.lib: skipped 21, total 316
.\VS11\VC\atlmfc\lib\amd64\atlsd.lib: skipped 0, total 661
.\VS11\VC\atlmfc\lib\amd64\atlsn.lib: skipped 19, total 288
.\VS11\VC\atlmfc\lib\amd64\atlsnd.lib: skipped 0, total 633
.\VS11\VC\atlmfc\lib\amd64\mfc110.lib: skipped 14395, total 14395
.\VS11\VC\atlmfc\lib\amd64\mfc110d.lib: skipped 16913, total 16913
.\VS11\VC\atlmfc\lib\amd64\mfc110u.lib: skipped 17072, total 17072
.\VS11\VC\atlmfc\lib\amd64\mfc110ud.lib: skipped 20009, total 20009
.\VS11\VC\atlmfc\lib\amd64\MFCM110.lib: skipped 25, total 41
.\VS11\VC\atlmfc\lib\amd64\MFCM110d.lib: skipped 31, total 47
.\VS11\VC\atlmfc\lib\amd64\MFCM110U.lib: skipped 27, total 43
.\VS11\VC\atlmfc\lib\amd64\MFCM110Ud.lib: skipped 33, total 49
.\VS11\VC\atlmfc\lib\amd64\mfcs110.lib: skipped 2, total 88
.\VS11\VC\atlmfc\lib\amd64\mfcs110d.lib: skipped 0, total 97
.\VS11\VC\atlmfc\lib\amd64\mfcs110u.lib: skipped 2, total 88
.\VS11\VC\atlmfc\lib\amd64\mfcs110ud.lib: skipped 2, total 101
.\VS11\VC\atlmfc\lib\amd64\nafxcw.lib: skipped 4947, total 54147
.\VS11\VC\atlmfc\lib\amd64\nafxcwd.lib: skipped 295, total 48287
.\VS11\VC\atlmfc\lib\amd64\uafxcw.lib: skipped 6827, total 55767
.\VS11\VC\atlmfc\lib\amd64\uafxcwd.lib: skipped 2182, total 50226
.\VS11\VC\atlmfc\lib\Atl.lib: skipped 52, total 52
.\VS11\VC\atlmfc\lib\atls.lib: skipped 26, total 1336
.\VS11\VC\atlmfc\lib\atlsd.lib: skipped 0, total 1681
.\VS11\VC\atlmfc\lib\atlsn.lib: skipped 25, total 1308
.\VS11\VC\atlmfc\lib\atlsnd.lib: skipped 0, total 1653
.\VS11\VC\atlmfc\lib\mfc110.lib: skipped 14755, total 14755
.\VS11\VC\atlmfc\lib\mfc110d.lib: skipped 17309, total 17309
.\VS11\VC\atlmfc\lib\mfc110u.lib: skipped 17663, total 17663
.\VS11\VC\atlmfc\lib\mfc110ud.lib: skipped 20636, total 20636
.\VS11\VC\atlmfc\lib\MFCM110.lib: skipped 25, total 41
.\VS11\VC\atlmfc\lib\MFCM110d.lib: skipped 32, total 48
.\VS11\VC\atlmfc\lib\MFCM110U.lib: skipped 27, total 43
.\VS11\VC\atlmfc\lib\MFCM110Ud.lib: skipped 34, total 50
.\VS11\VC\atlmfc\lib\mfcs110.lib: skipped 3, total 85
.\VS11\VC\atlmfc\lib\mfcs110d.lib: skipped 0, total 95
.\VS11\VC\atlmfc\lib\mfcs110u.lib: skipped 3, total 85
.\VS11\VC\atlmfc\lib\mfcs110ud.lib: skipped 2, total 99
.\VS11\VC\atlmfc\lib\nafxcw.lib: skipped 6127, total 54839
.\VS11\VC\atlmfc\lib\nafxcwd.lib: skipped 295, total 49026
.\VS11\VC\atlmfc\lib\uafxcw.lib: skipped 7823, total 56593
.\VS11\VC\atlmfc\lib\uafxcwd.lib: skipped 2290, total 51102
.\VS11\VC\lib\amd64\binmode.obj: skipped 0, total 0
.\VS11\VC\lib\amd64\chkstk.obj: skipped 0, total 1
.\VS11\VC\lib\amd64\commode.obj: skipped 0, total 0
.\VS11\VC\lib\amd64\comsupp.lib: skipped 0, total 26
.\VS11\VC\lib\amd64\comsuppd.lib: skipped 0, total 28
.\VS11\VC\lib\amd64\comsuppw.lib: skipped 0, total 26
.\VS11\VC\lib\amd64\comsuppwd.lib: skipped 0, total 28
.\VS11\VC\lib\amd64\delayimp.lib: skipped 1, total 21
.\VS11\VC\lib\amd64\invalidcontinue.obj: skipped 1, total 2
.\VS11\VC\lib\amd64\libcmt.lib: skipped 561, total 7084
.\VS11\VC\lib\amd64\libcmtd.lib: skipped 149, total 7514
.\VS11\VC\lib\amd64\libcpmt.lib: skipped 1263, total 10110
.\VS11\VC\lib\amd64\libcpmt1.lib: skipped 1505, total 10951
.\VS11\VC\lib\amd64\libcpmtd.lib: skipped 0, total 11818
.\VS11\VC\lib\amd64\libcpmtd0.lib: skipped 0, total 10498
.\VS11\VC\lib\amd64\libcpmtd1.lib: skipped 0, total 11530
.\VS11\VC\lib\amd64\loosefpmath.obj: skipped 0, total 2
.\VS11\VC\lib\amd64\msvcmrt.lib: skipped 283, total 547
.\VS11\VC\lib\amd64\msvcmrtd.lib: skipped 283, total 568
.\VS11\VC\lib\amd64\msvcprt.lib: skipped 1591, total 1599
.\VS11\VC\lib\amd64\msvcprtd.lib: skipped 1598, total 1612
.\VS11\VC\lib\amd64\msvcrt.lib: skipped 1932, total 2203
.\VS11\VC\lib\amd64\msvcrtd.lib: skipped 1994, total 2269
.\VS11\VC\lib\amd64\msvcurt.lib: skipped 3519, total 25335
.\VS11\VC\lib\amd64\msvcurtd.lib: skipped 3590, total 26679
.\VS11\VC\lib\amd64\newmode.obj: skipped 0, total 0
.\VS11\VC\lib\amd64\noarg.obj: skipped 4, total 4
.\VS11\VC\lib\amd64\noenv.obj: skipped 4, total 4
.\VS11\VC\lib\amd64\nothrownew.obj: skipped 0, total 4
.\VS11\VC\lib\amd64\oldnames.lib: skipped 278, total 278
.\VS11\VC\lib\amd64\pbinmode.obj: skipped 0, total 3
.\VS11\VC\lib\amd64\pcommode.obj: skipped 0, total 1
.\VS11\VC\lib\amd64\pgobootrun.lib: skipped 2, total 2
.\VS11\VC\lib\amd64\pgort.lib: skipped 8, total 14
.\VS11\VC\lib\amd64\pinvalidcontinue.obj: skipped 0, total 6
.\VS11\VC\lib\amd64\pnewmode.obj: skipped 0, total 1
.\VS11\VC\lib\amd64\pnoarg.obj: skipped 0, total 4
.\VS11\VC\lib\amd64\pnoenv.obj: skipped 0, total 6
.\VS11\VC\lib\amd64\pnothrownew.obj: skipped 0, total 6
.\VS11\VC\lib\amd64\psetargv.obj: skipped 0, total 1
.\VS11\VC\lib\amd64\pthreadlocale.obj: skipped 0, total 1
.\VS11\VC\lib\amd64\ptrustm.lib: skipped 0, total 173
.\VS11\VC\lib\amd64\ptrustmd.lib: skipped 0, total 174
.\VS11\VC\lib\amd64\ptrustu.lib: skipped 0, total 83
.\VS11\VC\lib\amd64\ptrustud.lib: skipped 0, total 83
.\VS11\VC\lib\amd64\pwsetargv.obj: skipped 0, total 1
.\VS11\VC\lib\amd64\runtmchk.lib: skipped 0, total 69
.\VS11\VC\lib\amd64\setargv.obj: skipped 0, total 1
.\VS11\VC\lib\amd64\smalheap.obj: skipped 0, total 12
.\VS11\VC\lib\amd64\threadlocale.obj: skipped 0, total 0
.\VS11\VC\lib\amd64\vcamp.lib: skipped 130, total 130
.\VS11\VC\lib\amd64\vcampd.lib: skipped 131, total 131
.\VS11\VC\lib\amd64\vccorlib.lib: skipped 408, total 5177
.\VS11\VC\lib\amd64\vccorlibd.lib: skipped 273, total 5185
.\VS11\VC\lib\amd64\vcomp.lib: skipped 113, total 113
.\VS11\VC\lib\amd64\vcompd.lib: skipped 113, total 113
.\VS11\VC\lib\amd64\VsGraphicsHelper.lib: skipped 5, total 5
.\VS11\VC\lib\amd64\wsetargv.obj: skipped 0, total 1
.\VS11\VC\lib\binmode.obj: skipped 0, total 0
.\VS11\VC\lib\chkstk.obj: skipped 0, total 1
.\VS11\VC\lib\commode.obj: skipped 0, total 0
.\VS11\VC\lib\comsupp.lib: skipped 0, total 26
.\VS11\VC\lib\comsuppd.lib: skipped 0, total 26
.\VS11\VC\lib\comsuppw.lib: skipped 0, total 26
.\VS11\VC\lib\comsuppwd.lib: skipped 0, total 26
.\VS11\VC\lib\delayimp.lib: skipped 0, total 21
.\VS11\VC\lib\fp10.obj: skipped 0, total 2
.\VS11\VC\lib\invalidcontinue.obj: skipped 1, total 2
.\VS11\VC\lib\libcmt.lib: skipped 664, total 6887
.\VS11\VC\lib\libcmtd.lib: skipped 134, total 7300
.\VS11\VC\lib\libcpmt.lib: skipped 1108, total 10080
.\VS11\VC\lib\libcpmt1.lib: skipped 1313, total 10929
.\VS11\VC\lib\libcpmtd.lib: skipped 1, total 11899
.\VS11\VC\lib\libcpmtd0.lib: skipped 1, total 10579
.\VS11\VC\lib\libcpmtd1.lib: skipped 1, total 11611
.\VS11\VC\lib\loosefpmath.obj: skipped 0, total 2
.\VS11\VC\lib\msvcmrt.lib: skipped 285, total 549
.\VS11\VC\lib\msvcmrtd.lib: skipped 285, total 570
.\VS11\VC\lib\msvcprt.lib: skipped 1591, total 1599
.\VS11\VC\lib\msvcprtd.lib: skipped 1602, total 1616
.\VS11\VC\lib\msvcrt.lib: skipped 1976, total 2261
.\VS11\VC\lib\msvcrtd.lib: skipped 2037, total 2328
.\VS11\VC\lib\msvcurt.lib: skipped 3563, total 25379
.\VS11\VC\lib\msvcurtd.lib: skipped 3639, total 26812
.\VS11\VC\lib\newmode.obj: skipped 0, total 0
.\VS11\VC\lib\noarg.obj: skipped 4, total 4
.\VS11\VC\lib\noenv.obj: skipped 4, total 4
.\VS11\VC\lib\nohetoc.obj: skipped 0, total 0
.\VS11\VC\lib\nothrownew.obj: skipped 0, total 4
.\VS11\VC\lib\oldnames.lib: skipped 278, total 278
.\VS11\VC\lib\pbinmode.obj: skipped 0, total 3
.\VS11\VC\lib\pcommode.obj: skipped 0, total 1
.\VS11\VC\lib\pgobootrun.lib: skipped 2, total 2
.\VS11\VC\lib\pgort.lib: skipped 11, total 22
.\VS11\VC\lib\pinvalidcontinue.obj: skipped 0, total 6
.\VS11\VC\lib\pnewmode.obj: skipped 0, total 1
.\VS11\VC\lib\pnoarg.obj: skipped 0, total 4
.\VS11\VC\lib\pnoenv.obj: skipped 0, total 6
.\VS11\VC\lib\pnothrownew.obj: skipped 0, total 6
.\VS11\VC\lib\psetargv.obj: skipped 0, total 1
.\VS11\VC\lib\pthreadlocale.obj: skipped 0, total 1
.\VS11\VC\lib\ptrustm.lib: skipped 0, total 173
.\VS11\VC\lib\ptrustmd.lib: skipped 0, total 174
.\VS11\VC\lib\ptrustu.lib: skipped 0, total 83
.\VS11\VC\lib\ptrustud.lib: skipped 0, total 83
.\VS11\VC\lib\pwsetargv.obj: skipped 0, total 1
.\VS11\VC\lib\RunTmChk.lib: skipped 1, total 74
.\VS11\VC\lib\setargv.obj: skipped 0, total 1
.\VS11\VC\lib\smalheap.obj: skipped 0, total 12
.\VS11\VC\lib\threadlocale.obj: skipped 0, total 0
.\VS11\VC\lib\vcamp.lib: skipped 130, total 130
.\VS11\VC\lib\vcampd.lib: skipped 131, total 131
.\VS11\VC\lib\vccorlib.lib: skipped 322, total 5139
.\VS11\VC\lib\vccorlibd.lib: skipped 273, total 5194
.\VS11\VC\lib\vcomp.lib: skipped 113, total 113
.\VS11\VC\lib\vcompd.lib: skipped 113, total 113
.\VS11\VC\lib\VsGraphicsHelper.lib: skipped 5, total 5
.\VS11\VC\lib\wsetargv.obj: skipped 0, total 1
```

```
$ find VS11 -name '*.pat' -print0 | tar -czvf VS11/VS11.tar.gz --null -T -
VS11/VC/atlmfc/lib/afxnmcd.lib.pat
VS11/VC/atlmfc/lib/afxnmcdd.lib.pat
VS11/VC/atlmfc/lib/amd64/afxnmcd.lib.pat
VS11/VC/atlmfc/lib/amd64/afxnmcdd.lib.pat
VS11/VC/atlmfc/lib/amd64/atl.lib.pat
VS11/VC/atlmfc/lib/amd64/atls.lib.pat
VS11/VC/atlmfc/lib/amd64/atlsd.lib.pat
VS11/VC/atlmfc/lib/amd64/atlsn.lib.pat
VS11/VC/atlmfc/lib/amd64/atlsnd.lib.pat
VS11/VC/atlmfc/lib/amd64/mfc110.lib.pat
VS11/VC/atlmfc/lib/amd64/mfc110d.lib.pat
VS11/VC/atlmfc/lib/amd64/mfc110u.lib.pat
VS11/VC/atlmfc/lib/amd64/mfc110ud.lib.pat
VS11/VC/atlmfc/lib/amd64/MFCM110.lib.pat
VS11/VC/atlmfc/lib/amd64/MFCM110d.lib.pat
VS11/VC/atlmfc/lib/amd64/MFCM110U.lib.pat
VS11/VC/atlmfc/lib/amd64/MFCM110Ud.lib.pat
VS11/VC/atlmfc/lib/amd64/mfcs110.lib.pat
VS11/VC/atlmfc/lib/amd64/mfcs110d.lib.pat
VS11/VC/atlmfc/lib/amd64/mfcs110u.lib.pat
VS11/VC/atlmfc/lib/amd64/mfcs110ud.lib.pat
VS11/VC/atlmfc/lib/amd64/nafxcw.lib.pat
VS11/VC/atlmfc/lib/amd64/nafxcwd.lib.pat
VS11/VC/atlmfc/lib/amd64/uafxcw.lib.pat
VS11/VC/atlmfc/lib/amd64/uafxcwd.lib.pat
VS11/VC/atlmfc/lib/Atl.lib.pat
VS11/VC/atlmfc/lib/atls.lib.pat
VS11/VC/atlmfc/lib/atlsd.lib.pat
VS11/VC/atlmfc/lib/atlsn.lib.pat
VS11/VC/atlmfc/lib/atlsnd.lib.pat
VS11/VC/atlmfc/lib/mfc110.lib.pat
VS11/VC/atlmfc/lib/mfc110d.lib.pat
VS11/VC/atlmfc/lib/mfc110u.lib.pat
VS11/VC/atlmfc/lib/mfc110ud.lib.pat
VS11/VC/atlmfc/lib/MFCM110.lib.pat
VS11/VC/atlmfc/lib/MFCM110d.lib.pat
VS11/VC/atlmfc/lib/MFCM110U.lib.pat
VS11/VC/atlmfc/lib/MFCM110Ud.lib.pat
VS11/VC/atlmfc/lib/mfcs110.lib.pat
VS11/VC/atlmfc/lib/mfcs110d.lib.pat
VS11/VC/atlmfc/lib/mfcs110u.lib.pat
VS11/VC/atlmfc/lib/mfcs110ud.lib.pat
VS11/VC/atlmfc/lib/nafxcw.lib.pat
VS11/VC/atlmfc/lib/nafxcwd.lib.pat
VS11/VC/atlmfc/lib/uafxcw.lib.pat
VS11/VC/atlmfc/lib/uafxcwd.lib.pat
VS11/VC/lib/amd64/binmode.obj.pat
VS11/VC/lib/amd64/chkstk.obj.pat
VS11/VC/lib/amd64/commode.obj.pat
VS11/VC/lib/amd64/comsupp.lib.pat
VS11/VC/lib/amd64/comsuppd.lib.pat
VS11/VC/lib/amd64/comsuppw.lib.pat
VS11/VC/lib/amd64/comsuppwd.lib.pat
VS11/VC/lib/amd64/delayimp.lib.pat
VS11/VC/lib/amd64/invalidcontinue.obj.pat
VS11/VC/lib/amd64/libcmt.lib.pat
VS11/VC/lib/amd64/libcmtd.lib.pat
VS11/VC/lib/amd64/libcpmt.lib.pat
VS11/VC/lib/amd64/libcpmt1.lib.pat
VS11/VC/lib/amd64/libcpmtd.lib.pat
VS11/VC/lib/amd64/libcpmtd0.lib.pat
VS11/VC/lib/amd64/libcpmtd1.lib.pat
VS11/VC/lib/amd64/loosefpmath.obj.pat
VS11/VC/lib/amd64/msvcmrt.lib.pat
VS11/VC/lib/amd64/msvcmrtd.lib.pat
VS11/VC/lib/amd64/msvcprt.lib.pat
VS11/VC/lib/amd64/msvcprtd.lib.pat
VS11/VC/lib/amd64/msvcrt.lib.pat
VS11/VC/lib/amd64/msvcrtd.lib.pat
VS11/VC/lib/amd64/msvcurt.lib.pat
VS11/VC/lib/amd64/msvcurtd.lib.pat
VS11/VC/lib/amd64/newmode.obj.pat
VS11/VC/lib/amd64/noarg.obj.pat
VS11/VC/lib/amd64/noenv.obj.pat
VS11/VC/lib/amd64/nothrownew.obj.pat
VS11/VC/lib/amd64/oldnames.lib.pat
VS11/VC/lib/amd64/pbinmode.obj.pat
VS11/VC/lib/amd64/pcommode.obj.pat
VS11/VC/lib/amd64/pgobootrun.lib.pat
VS11/VC/lib/amd64/pgort.lib.pat
VS11/VC/lib/amd64/pinvalidcontinue.obj.pat
VS11/VC/lib/amd64/pnewmode.obj.pat
VS11/VC/lib/amd64/pnoarg.obj.pat
VS11/VC/lib/amd64/pnoenv.obj.pat
VS11/VC/lib/amd64/pnothrownew.obj.pat
VS11/VC/lib/amd64/psetargv.obj.pat
VS11/VC/lib/amd64/pthreadlocale.obj.pat
VS11/VC/lib/amd64/ptrustm.lib.pat
VS11/VC/lib/amd64/ptrustmd.lib.pat
VS11/VC/lib/amd64/ptrustu.lib.pat
VS11/VC/lib/amd64/ptrustud.lib.pat
VS11/VC/lib/amd64/pwsetargv.obj.pat
VS11/VC/lib/amd64/runtmchk.lib.pat
VS11/VC/lib/amd64/setargv.obj.pat
VS11/VC/lib/amd64/smalheap.obj.pat
VS11/VC/lib/amd64/threadlocale.obj.pat
VS11/VC/lib/amd64/vcamp.lib.pat
VS11/VC/lib/amd64/vcampd.lib.pat
VS11/VC/lib/amd64/vccorlib.lib.pat
VS11/VC/lib/amd64/vccorlibd.lib.pat
VS11/VC/lib/amd64/vcomp.lib.pat
VS11/VC/lib/amd64/vcompd.lib.pat
VS11/VC/lib/amd64/VsGraphicsHelper.lib.pat
VS11/VC/lib/amd64/wsetargv.obj.pat
VS11/VC/lib/binmode.obj.pat
VS11/VC/lib/chkstk.obj.pat
VS11/VC/lib/commode.obj.pat
VS11/VC/lib/comsupp.lib.pat
VS11/VC/lib/comsuppd.lib.pat
VS11/VC/lib/comsuppw.lib.pat
VS11/VC/lib/comsuppwd.lib.pat
VS11/VC/lib/delayimp.lib.pat
VS11/VC/lib/fp10.obj.pat
VS11/VC/lib/invalidcontinue.obj.pat
VS11/VC/lib/libcmt.lib.pat
VS11/VC/lib/libcmtd.lib.pat
VS11/VC/lib/libcpmt.lib.pat
VS11/VC/lib/libcpmt1.lib.pat
VS11/VC/lib/libcpmtd.lib.pat
VS11/VC/lib/libcpmtd0.lib.pat
VS11/VC/lib/libcpmtd1.lib.pat
VS11/VC/lib/loosefpmath.obj.pat
VS11/VC/lib/msvcmrt.lib.pat
VS11/VC/lib/msvcmrtd.lib.pat
VS11/VC/lib/msvcprt.lib.pat
VS11/VC/lib/msvcprtd.lib.pat
VS11/VC/lib/msvcrt.lib.pat
VS11/VC/lib/msvcrtd.lib.pat
VS11/VC/lib/msvcurt.lib.pat
VS11/VC/lib/msvcurtd.lib.pat
VS11/VC/lib/newmode.obj.pat
VS11/VC/lib/noarg.obj.pat
VS11/VC/lib/noenv.obj.pat
VS11/VC/lib/nohetoc.obj.pat
VS11/VC/lib/nothrownew.obj.pat
VS11/VC/lib/oldnames.lib.pat
VS11/VC/lib/pbinmode.obj.pat
VS11/VC/lib/pcommode.obj.pat
VS11/VC/lib/pgobootrun.lib.pat
VS11/VC/lib/pgort.lib.pat
VS11/VC/lib/pinvalidcontinue.obj.pat
VS11/VC/lib/pnewmode.obj.pat
VS11/VC/lib/pnoarg.obj.pat
VS11/VC/lib/pnoenv.obj.pat
VS11/VC/lib/pnothrownew.obj.pat
VS11/VC/lib/psetargv.obj.pat
VS11/VC/lib/pthreadlocale.obj.pat
VS11/VC/lib/ptrustm.lib.pat
VS11/VC/lib/ptrustmd.lib.pat
VS11/VC/lib/ptrustu.lib.pat
VS11/VC/lib/ptrustud.lib.pat
VS11/VC/lib/pwsetargv.obj.pat
VS11/VC/lib/RunTmChk.lib.pat
VS11/VC/lib/setargv.obj.pat
VS11/VC/lib/smalheap.obj.pat
VS11/VC/lib/threadlocale.obj.pat
VS11/VC/lib/vcamp.lib.pat
VS11/VC/lib/vcampd.lib.pat
VS11/VC/lib/vccorlib.lib.pat
VS11/VC/lib/vccorlibd.lib.pat
VS11/VC/lib/vcomp.lib.pat
VS11/VC/lib/vcompd.lib.pat
VS11/VC/lib/VsGraphicsHelper.lib.pat
VS11/VC/lib/wsetargv.obj.pat
```
