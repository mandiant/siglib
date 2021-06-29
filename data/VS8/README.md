# VS8 / Visual Studio 2005

## download
Visual Studio 2005 Professional
`en_vs_2005_pro_dvd.iso`

## prepare
run setup

## .lib/.obj files
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 8/VC/ -iname "*.lib"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atldload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atlmincrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/eafxis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/eafxisd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfc80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfc80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfc80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfc80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcdload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/MFCM80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/MFCM80D.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/MFCM80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/MFCM80UD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcs80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcs80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcs80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/mfcs80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/nafxis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/nafxisd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/amd64/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/Atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/atldload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/atlmincrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/eafxis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/eafxisd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfc80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfc80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfc80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfc80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcdload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcm80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcm80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcm80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcm80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcs80.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcs80d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcs80u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/mfcs80ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/nafxis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/nafxisd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/atlmfc/lib/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/armv4i/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsii_fp/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/mipsiv_fp/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/sh4/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/MFC80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/MFC80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/mfcs80U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/mfcs80Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/atlmfc/lib/x86/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/armv4i/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsii_fp/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/mipsiv_fp/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/sh4/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/ce/lib/x86/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/almap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/almapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/sdknames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/tcmap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/tcmapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/almap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/almapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/sdknames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/tcmap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/tcmapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/opends60.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/RunTmChk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AclUI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ActiveDS.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Ad1.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Adptif.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ADSIid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AdvAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/AclUI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ActiveDS.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Adptif.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ADSIid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/AdvAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/AuthZ.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Bits.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/bufferoverflowu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Cabinet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/CertIdl.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ClusApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ComCtl32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ComDlg32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ComSvcs.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Crypt32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/cryptui.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DbgEng.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DbgHelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/dciman32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DhcpCSvc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DlcAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DnsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DSProp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DSUIExt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/DtcHelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/FaultRep.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Fci.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Fdi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/FrameDyD.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/FrameDyn.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Gdi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/GdiPlus.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/GlAux.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/GlU32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/GPEdit.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/gtrts32w.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/gtrtst32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/HLink.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Htmlhelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/httpapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Icm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Icmui.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ImageHlp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Imm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/inetcomm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/IPHlpApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Iprop.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Kernel32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/KSProxy.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ksuser.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/LoadPerf.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Lz32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MgmtAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MMC.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MobSync.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Mpr.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Mprapi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MqOA.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MqRt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MSAcm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Mscms.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/msdasc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Msi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MSImg32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MSRating.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MSTask.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MsWSock.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/MsXml2.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Mtx.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NetAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/nmapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NMSupp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/normaliz.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/npptools.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NtDsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NtDsBCli.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NTMSAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/NtQuery.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/odbc32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/odbcbcp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/odbccp32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Ole32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OleAcc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OleAut32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/oledb.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OleDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OlePro32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/OpenGL32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/osptk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/parser.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Pdh.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/powrprof.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Psapi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/QosName.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RASAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RASDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RASsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ResUtils.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RpcNdr.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Rpcns4.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/RpcRT4.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Rtm.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Rtutils.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SCardDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ScrnSave.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ScrnSavW.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Secur32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SensAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SetupAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Sfc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Shell32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ShFolder.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/ShLwApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/sisbkup.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SnmpAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/SpOrder.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Sti.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/strsafe.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Svcguid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Tapi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Traffic.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Urlmon.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/User32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/UserEnv.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/USP10.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Uuid.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Uxtheme.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Version.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Vfw32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WbemUuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WiaGuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinInet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinMM.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinSCard.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinSpool.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinStrm.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WinTrust.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/Wldap32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/wmiutils.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WS2_32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WSnmp32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WSock32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/WtsApi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/xaSwitch.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AMD64/xoleHlp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ASycFilt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/AuthZ.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/bhsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Bits.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/bufferoverflowu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Cabinet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Cap.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/certadm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/certidl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/CiUuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ClusApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ComCtl32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ComDlg32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ComSvcs.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/credui.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Crypt32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/CryptNet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/cryptui.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/d3d8thk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/daouuid.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DbgEng.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DbgHelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/dciman32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ddao35.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ddao35d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ddao35u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ddao35ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DhcpCSvc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/dhcpsapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DlcAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DnsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DSProp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DSUIExt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/DtcHelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/FaultRep.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/FCachDll.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Fci.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Fdi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/FrameDyD.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/FrameDyn.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Gdi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/GdiPlus.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/GlAux.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/GlU32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/GPEdit.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/gpmuuid.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/gtrts32w.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/gtrtst32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/HLink.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Htmlhelp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/httpapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/IA64/AuthZ.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Icm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Icmui.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ImageHlp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Imm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/IPHlpApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Iprop.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Kernel32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/KSGuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/KSProxy.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ksuser.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/LoadPerf.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Lz32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MgmtAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MiniDump.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MMC.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MobSync.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Mpr.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Mprapi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MqOA.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MqRt.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MSAcm32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Mscms.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/mscoree.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/msdasc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MSImg32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MSRating.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MSTask.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MsWSock.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/MsXml2.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Mtx.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/mtxdm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NetAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/nmapi.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NMSupp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/npptools.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NtDsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NtDsBCli.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NTMSAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/NtQuery.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/odbc32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/odbcbcp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/odbccp32.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Ole32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OleAcc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OleAut32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/oledb.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OleDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OlePro32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/OpenGL32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/osptk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/parser.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Pdh.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/PEnter.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/powrprof.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Psapi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/QosName.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RASAPI32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RASDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RASsAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ResUtils.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RichEd20.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RpcNdr.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Rpcns4.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/RpcRT4.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Rtm.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Rtutils.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SCardDlg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ScrnSave.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ScrnSavW.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Secur32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SensAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SetupAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Sfc.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Shell32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ShFolder.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ShLwApi.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/sisbkup.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SnmpAPI.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SpOrder.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/SrClient.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Sti.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/strsafe.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Svcguid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Tapi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Thunk32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Traffic.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/unicows.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Url.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Urlmon.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/User32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/UserEnv.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/USP10.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Uuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Uxtheme.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/VdmDbg.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Version.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Vfw32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WbemUuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WebPost.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WiaGuid.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinInet.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinMM.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinSCard.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinSpool.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinStrm.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WinTrust.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Wldap32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/wmiutils.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Wow32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WS2_32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WSnmp32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WSock32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/Wst.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/WtsApi32.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/xaSwitch.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/xoleHlp.Lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/misc/mdac2.8/Conformance/Tests/Libs/amd64/ModuleCore.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/misc/mdac2.8/Conformance/Tests/Libs/x86/ModuleCore.lib
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 8/VC/ -iname "*.obj"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/dll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/mt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xdll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/AMD64/xmt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/cpu_disp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/dllsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehprolg2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehprolg3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehprolg3a.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehprolog.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ftol2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/dll_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/mt_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/cpu_disp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/dllsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehprolg2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehprolg3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehprolg3a.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehprolog.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ftol2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xdll_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/crt/src/intel/xmt_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/nochkclr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/amd64/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/fp10.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/nochkclr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/lib/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/ComMode.Obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 8/VC/PlatformSDK/Lib/sehprolg.obj


$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.Obj' --include '*.lib' --include '*.Lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 8/VC/ VS8/
```

## manually deleted
- `PlatformSDK`
- `ce`

```
$ find VS8/ -type f \( -iname "*.lib" -o -iname "*.obj" \) -exec md5sum {} \;
5fc46db6c735523d7481b1c11d82efa9 *VS8/VC/atlmfc/lib/amd64/atl.lib
17c870c8c2e19cc98e6bbca113cd1d04 *VS8/VC/atlmfc/lib/amd64/atldload.lib
29d5430231ae39cf8d9da16e1041dccc *VS8/VC/atlmfc/lib/amd64/atlmincrt.lib
89d9fa0291edc9b022dcbaf8ae12f2b8 *VS8/VC/atlmfc/lib/amd64/atls.lib
1882fd0c8f23568df0b7e46e9715ebb4 *VS8/VC/atlmfc/lib/amd64/atlsd.lib
88660a059f8a323e2e98aed61e0d040b *VS8/VC/atlmfc/lib/amd64/eafxis.lib
6c5edc19f404974efc5d6b421480eca8 *VS8/VC/atlmfc/lib/amd64/eafxisd.lib
fd5a28c5be75bbea8cefe72a1f447719 *VS8/VC/atlmfc/lib/amd64/mfc80.lib
6d8f644033561f2426fc2fe92c088c68 *VS8/VC/atlmfc/lib/amd64/mfc80d.lib
7544569a0daa7bba9a689f7b72a755af *VS8/VC/atlmfc/lib/amd64/mfc80u.lib
9db72f9e92466291e170264317c931cc *VS8/VC/atlmfc/lib/amd64/mfc80ud.lib
5b9758531003f45b620c0d084851473c *VS8/VC/atlmfc/lib/amd64/mfcdload.lib
b1753ccd2973af383ec03a55c5f77efb *VS8/VC/atlmfc/lib/amd64/MFCM80.lib
fbeeb29b2573cf5a965bbdf7c0917959 *VS8/VC/atlmfc/lib/amd64/MFCM80D.lib
98c3a5d7afdd4256f0b8a72e0b9acd23 *VS8/VC/atlmfc/lib/amd64/MFCM80U.lib
019c146e86fe404df18ff5ad1da58eeb *VS8/VC/atlmfc/lib/amd64/MFCM80UD.lib
66c8fd84f3d282121469f126b1ef9769 *VS8/VC/atlmfc/lib/amd64/mfcs80.lib
24bece449279b4223a9dcac1055b5fcb *VS8/VC/atlmfc/lib/amd64/mfcs80d.lib
1901822e70332b5eb575e9f8a8917c0a *VS8/VC/atlmfc/lib/amd64/mfcs80u.lib
c928b24a1e5703c58ed997bb51d106de *VS8/VC/atlmfc/lib/amd64/mfcs80ud.lib
d4f6748825313e011ee240b4dbfd2460 *VS8/VC/atlmfc/lib/amd64/nafxcw.lib
c15d0a4577bca39b3647084f8398309a *VS8/VC/atlmfc/lib/amd64/nafxcwd.lib
a6a974cc802253fd54cc34f6417db22e *VS8/VC/atlmfc/lib/amd64/nafxis.lib
c2f60bfce980b2dc184cc980148c92dd *VS8/VC/atlmfc/lib/amd64/nafxisd.lib
512c76c5efd456fbba99ec6d63e5cf84 *VS8/VC/atlmfc/lib/amd64/uafxcw.lib
26afc46073138ea746852b189936ed95 *VS8/VC/atlmfc/lib/amd64/uafxcwd.lib
134c12ee6adb605b3df1afcf461a5c3e *VS8/VC/atlmfc/lib/Atl.lib
160bc3a4303b9900a6af566ea0af1a9a *VS8/VC/atlmfc/lib/atldload.lib
85614323bf0df213b1673581c42fd5e8 *VS8/VC/atlmfc/lib/atlmincrt.lib
238605aa75247cfcc51290de628e7e60 *VS8/VC/atlmfc/lib/atls.lib
c50f8e09651b00b656039fd633e49810 *VS8/VC/atlmfc/lib/atlsd.lib
0970b85391aa2ffe94460859de634563 *VS8/VC/atlmfc/lib/eafxis.lib
f4a9fed6fc1b98d8e429fb400513835c *VS8/VC/atlmfc/lib/eafxisd.lib
9202b5820ef03747a9c4823d11bde3fa *VS8/VC/atlmfc/lib/mfc80.lib
449fa688a3c2771f530dec536cea81e4 *VS8/VC/atlmfc/lib/mfc80d.lib
6d3067e1cdfb6e5e8f180ee465f6c8d7 *VS8/VC/atlmfc/lib/mfc80u.lib
3107b9595fcfcf0d6e8baccf3d3120fd *VS8/VC/atlmfc/lib/mfc80ud.lib
a76ba33256bc5fb3d0b476c216b2d2f4 *VS8/VC/atlmfc/lib/mfcdload.lib
39d1230251b64d731dce6f7dc71a53ea *VS8/VC/atlmfc/lib/mfcm80.lib
230825b45576797f7503374f0df862d0 *VS8/VC/atlmfc/lib/mfcm80d.lib
0c394fede2e3343cac12c9c09ee11ac2 *VS8/VC/atlmfc/lib/mfcm80u.lib
3b0ef42864e5d170b8f8ecc47f4a1cda *VS8/VC/atlmfc/lib/mfcm80ud.lib
011413476e17624feda020f9721536ad *VS8/VC/atlmfc/lib/mfcs80.lib
0d24cd639379abb2bfc733a34dc007bb *VS8/VC/atlmfc/lib/mfcs80d.lib
0ba94eafec6a93f14c70558250a9eb4c *VS8/VC/atlmfc/lib/mfcs80u.lib
345346c481516be79ddb0e26de30e4cf *VS8/VC/atlmfc/lib/mfcs80ud.lib
d86d98e4ec62973b2be42d891c604651 *VS8/VC/atlmfc/lib/nafxcw.lib
57560dd7e6bc1f651ce1079158e27397 *VS8/VC/atlmfc/lib/nafxcwd.lib
25a688d351cea2a45ff85a49c7c53e8f *VS8/VC/atlmfc/lib/nafxis.lib
5d9630cb944db46b7e20ca9aeafb17ec *VS8/VC/atlmfc/lib/nafxisd.lib
3872286451e25f3a3e08d32dd40acc83 *VS8/VC/atlmfc/lib/uafxcw.lib
004f0c5ac0f76a2da5cf2c1b1deec1e8 *VS8/VC/atlmfc/lib/uafxcwd.lib
e151d8f93528ad422ccf0903e8b893a7 *VS8/VC/crt/src/AMD64/almap.lib
b47d4cf7c7723ff3581bbcef4a2792ae *VS8/VC/crt/src/AMD64/almapdll.lib
4d860aec8c95ac5b9fe5e863c0e30a60 *VS8/VC/crt/src/AMD64/dll_lib/amdsecgs.obj
4a70476f36c27eee3b2d97c2d658adc4 *VS8/VC/crt/src/AMD64/dll_lib/chandler.obj
5cf59c8a0436522d669c733ce3f913a4 *VS8/VC/crt/src/AMD64/dll_lib/chkstk.obj
c9dc4981014eef7f133e7ee954373825 *VS8/VC/crt/src/AMD64/dll_lib/chkstk2.obj
3f54b2ad14483584784eeeba474a8f02 *VS8/VC/crt/src/AMD64/dll_lib/clr_obj/managdeh.obj
46ec5579db2b87725a9cf35144b4c307 *VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvccctr.obj
d09151bd0e0ec87e4949426411acb76a *VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvcccvb.obj
caebd0a9f6509a3ba7d859d06ed50e08 *VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecctr.obj
075c5e0666b5fefe6ca91bc3462e6e90 *VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehveccvb.obj
c45458ac5a32aa6ffac0f7dbc500b775 *VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecdtr.obj
5a7af35594ea2f834c5c96908de8c6eb *VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mstdexpt.obj
681e653e98349872ec2397618a7a7186 *VS8/VC/crt/src/AMD64/dll_lib/conv.lib
8cec5487d0c9761288c21f5670b90cb8 *VS8/VC/crt/src/AMD64/dll_lib/eh.lib
9360351e9ae320939a980ed5f6482da8 *VS8/VC/crt/src/AMD64/dll_lib/ehvccctr.obj
ed0c0df241d94a885c8ec25fdb3aab65 *VS8/VC/crt/src/AMD64/dll_lib/ehvcccvb.obj
0e25e33889d8a496c5b753c913c8cbb7 *VS8/VC/crt/src/AMD64/dll_lib/ehvecctr.obj
6dac5d5ddc87760350ce4a3e6ef2fa2d *VS8/VC/crt/src/AMD64/dll_lib/ehveccvb.obj
1d62868c2bf227156a1429c0d87bd9bc *VS8/VC/crt/src/AMD64/dll_lib/ehvecdtr.obj
d6ff99b8417994c05eb79cc9490701f9 *VS8/VC/crt/src/AMD64/dll_lib/gshandler.obj
8103e29077d4787d616c88797a9f3e71 *VS8/VC/crt/src/AMD64/dll_lib/gshandlereh.obj
7e3c74a1e59a0adc4eb2fa623ab37db4 *VS8/VC/crt/src/AMD64/dll_lib/gshandlerseh.obj
15b1f8bb298d798272fc283cc99293e8 *VS8/VC/crt/src/AMD64/dll_lib/jmpuwind.obj
930f7683b19491ece619375e58d5bc9e *VS8/VC/crt/src/AMD64/dll_lib/longjmp.obj
28cb3db58ac2b4917d34bce759740f24 *VS8/VC/crt/src/AMD64/dll_lib/matherr.obj
a9f665548fe41492293216e04c2b2651 *VS8/VC/crt/src/AMD64/dll_lib/oldexcpt.obj
166c331606f7cc6aaa71524e02355cee *VS8/VC/crt/src/AMD64/dll_lib/pure_obj/managdeh.obj
5127a9f37470910768cf9b595f778b66 *VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvccctr.obj
5852abd9f2e8b74df8227ceaf1f2a355 *VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvcccvb.obj
1ca3b3b4cf183ac46f4afd5df04eeabb *VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecctr.obj
24f22300932cd8cc960c994b7c01352d *VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehveccvb.obj
0acfb7ce9edd877c1364321e3ea6c244 *VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecdtr.obj
e73aba4338dbe2c28971ce5e593eb55a *VS8/VC/crt/src/AMD64/dll_lib/pure_obj/rtti.obj
c8f538fe878f0c0287c8f753decde0b6 *VS8/VC/crt/src/AMD64/dll_lib/rtc.lib
cdcd2d57caf50d40492e1ee40d5fca56 *VS8/VC/crt/src/AMD64/dll_lib/rtcmd.obj
f4cf69021fd5c14d81704c24f4791773 *VS8/VC/crt/src/AMD64/dll_lib/setjmp.obj
f75a9d9b12991340c252d750200f0177 *VS8/VC/crt/src/AMD64/dll_lib/setjmpex.obj
128fa4d2442a2a76be0ca35ad2492167 *VS8/VC/crt/src/AMD64/dll_lib/tncleanup.obj
2b2a574803f532ee22277e949494bdfc *VS8/VC/crt/src/AMD64/dll_lib/tran.lib
d8b823724a3639936af7dd168a56f26c *VS8/VC/crt/src/AMD64/mt_lib/amdsecgs.obj
3086299be6816093a9cd170dfe0425c0 *VS8/VC/crt/src/AMD64/mt_lib/chandler.obj
2d25fc94ea3b1d906a05a98894557bc6 *VS8/VC/crt/src/AMD64/mt_lib/chkstk.obj
c3cdee1727e447cb4e443f5b80b2b84d *VS8/VC/crt/src/AMD64/mt_lib/chkstk2.obj
c295727989478d7dc6d3f1084cafe0de *VS8/VC/crt/src/AMD64/mt_lib/conv.lib
85c160c0402aed6c32671f3b489f6945 *VS8/VC/crt/src/AMD64/mt_lib/eh.lib
8800568476721866688898a96e4af650 *VS8/VC/crt/src/AMD64/mt_lib/gshandler.obj
a3bf5b879a569af86224a1edeb2cf608 *VS8/VC/crt/src/AMD64/mt_lib/gshandlereh.obj
63aad18c8d79ae8bc724b9ec43240e47 *VS8/VC/crt/src/AMD64/mt_lib/gshandlerseh.obj
0640f185392191e02db451b82c208722 *VS8/VC/crt/src/AMD64/mt_lib/jmpuwind.obj
ae065cb2e861529ab4fe7ed952d4a08e *VS8/VC/crt/src/AMD64/mt_lib/longjmp.obj
adfe20cb91385a31f73bf6153a8fe669 *VS8/VC/crt/src/AMD64/mt_lib/matherr.obj
e7cebe17277d49d09608e69a2f7bab8c *VS8/VC/crt/src/AMD64/mt_lib/rtc.lib
569616781ba71d2b8a087789b478c9ad *VS8/VC/crt/src/AMD64/mt_lib/rtcmd.obj
00ce5a9a3fa1dbe52002754b649d1587 *VS8/VC/crt/src/AMD64/mt_lib/setjmp.obj
1ad670f2f9bf62ba4ceb12c51bcd0c6d *VS8/VC/crt/src/AMD64/mt_lib/setjmpex.obj
2e84c51358544af57dfe31abf4db5fd6 *VS8/VC/crt/src/AMD64/mt_lib/tran.lib
2ea092d00689b7dccd5c8d0a60058d3b *VS8/VC/crt/src/AMD64/sdknames.lib
6b1e2ba0d0d963882c67da61d790171c *VS8/VC/crt/src/AMD64/tcmap.lib
40ebfd1e27c069505c6a1def927db09a *VS8/VC/crt/src/AMD64/tcmapdll.lib
d450660b9ed9caccc66aaa0d26d58124 *VS8/VC/crt/src/AMD64/xdll_lib/amdsecgs.obj
966b9652f31ee3c0e89aabc996944a05 *VS8/VC/crt/src/AMD64/xdll_lib/chandler.obj
d033a520bd6f972bfc23df8048d9ba3f *VS8/VC/crt/src/AMD64/xdll_lib/chkstk.obj
969570d316b3ecc0069b4d149c5d52f6 *VS8/VC/crt/src/AMD64/xdll_lib/chkstk2.obj
8132947c31e348e288c30d3a93fa0224 *VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/managdeh.obj
ccacfeb6ec8f810d159f42e767f40bcd *VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvccctr.obj
b1a4988c53cf0bcf69339f563d11402b *VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvcccvb.obj
131fb509b03219a1602650e2fd424f55 *VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecctr.obj
893ec694068618980e99f3a2da8093d4 *VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehveccvb.obj
eaff8be7c63b47125ca40d135aa7fc2b *VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecdtr.obj
d5415b36e24bad4ced715e892b40db19 *VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mstdexpt.obj
adce858001fd30c1de2957229fa65e21 *VS8/VC/crt/src/AMD64/xdll_lib/conv.lib
722801dc12d81d644016a9f81ca4778d *VS8/VC/crt/src/AMD64/xdll_lib/eh.lib
2ea96b4e5097223ba057e15418bff1c3 *VS8/VC/crt/src/AMD64/xdll_lib/ehvccctr.obj
f35ded295322cbfdb8eae28f27590775 *VS8/VC/crt/src/AMD64/xdll_lib/ehvcccvb.obj
f17aa69f30a5acc5f2671dc4824ab361 *VS8/VC/crt/src/AMD64/xdll_lib/ehvecctr.obj
1063424ea251f3f38dd00abd1308f683 *VS8/VC/crt/src/AMD64/xdll_lib/ehveccvb.obj
655fe0916eea6dda8d259e0d8860084b *VS8/VC/crt/src/AMD64/xdll_lib/ehvecdtr.obj
12e90eaac0072e4acb263eb77352453e *VS8/VC/crt/src/AMD64/xdll_lib/gshandler.obj
86fea8663c437c85926910c7743349f9 *VS8/VC/crt/src/AMD64/xdll_lib/gshandlereh.obj
84903a856b3896aad07302d20b3f5f43 *VS8/VC/crt/src/AMD64/xdll_lib/gshandlerseh.obj
42e02c2e92d46a376e763a61cc5ee323 *VS8/VC/crt/src/AMD64/xdll_lib/jmpuwind.obj
d06de19850bcda7123c687f9881b35c2 *VS8/VC/crt/src/AMD64/xdll_lib/longjmp.obj
856a1e4a15aacfea99ea4ab2f28f05cd *VS8/VC/crt/src/AMD64/xdll_lib/matherr.obj
13f2afb4baa97ce2c9493e8c06bda96c *VS8/VC/crt/src/AMD64/xdll_lib/oldexcpt.obj
16ff8196c87bc6c3a21b73019e4384f8 *VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/managdeh.obj
d1d963b9396cc214201654e316805f83 *VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvccctr.obj
76141610a0759d01c1e0300421d221ec *VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvcccvb.obj
2e8c69416445b0a1c51483ff626884c7 *VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecctr.obj
7dfe75732d572782c55c169046f4778d *VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehveccvb.obj
4f1af209cb091bc07d5f5ef496aef026 *VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecdtr.obj
38a4a45eb9f041a55173e9fe4c55156b *VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/rtti.obj
bcdece353fd0506852c3cd2100b48cfe *VS8/VC/crt/src/AMD64/xdll_lib/rtc.lib
52f1b7540085326971d81c442ead5850 *VS8/VC/crt/src/AMD64/xdll_lib/rtcmd.obj
204d0f43cd341446165ac255e3e5ab31 *VS8/VC/crt/src/AMD64/xdll_lib/setjmp.obj
576b041dddf01d0837b5e0bd1de491b2 *VS8/VC/crt/src/AMD64/xdll_lib/setjmpex.obj
1486e65e127f7d5a66c44e415acb825e *VS8/VC/crt/src/AMD64/xdll_lib/tncleanup.obj
6f5a3e015f8cf29e1a5173af6eb63c7d *VS8/VC/crt/src/AMD64/xdll_lib/tran.lib
1c2f358913a511418121d3b2dc7bb3ac *VS8/VC/crt/src/AMD64/xmt_lib/amdsecgs.obj
b4603f70ceb763fdceba078f2d360836 *VS8/VC/crt/src/AMD64/xmt_lib/chandler.obj
cbaa96182b8095ee758a0ab139ef6bc4 *VS8/VC/crt/src/AMD64/xmt_lib/chkstk.obj
84e759ed1b1757317238ff676a0aeb7d *VS8/VC/crt/src/AMD64/xmt_lib/chkstk2.obj
4f2fcc61d5e6796d2aacaac7c00736f8 *VS8/VC/crt/src/AMD64/xmt_lib/conv.lib
7ccc961be07d8f334d73812a15685775 *VS8/VC/crt/src/AMD64/xmt_lib/eh.lib
d82200c350f13263ab33e60252754219 *VS8/VC/crt/src/AMD64/xmt_lib/gshandler.obj
72f49a2216d2ff43d4e60e2a40e501a8 *VS8/VC/crt/src/AMD64/xmt_lib/gshandlereh.obj
45aa41285108a475efd92f347f5eb7ab *VS8/VC/crt/src/AMD64/xmt_lib/gshandlerseh.obj
3a546f7463ef841cf0349070e9ee6ca3 *VS8/VC/crt/src/AMD64/xmt_lib/jmpuwind.obj
d91aa152761c0d8754aa9e58a6844a05 *VS8/VC/crt/src/AMD64/xmt_lib/longjmp.obj
6f25071e6d3aec115af4aa553d80014f *VS8/VC/crt/src/AMD64/xmt_lib/matherr.obj
8ffb7c3ad81b2455fa42188a18c2167a *VS8/VC/crt/src/AMD64/xmt_lib/rtc.lib
6bb68d92fae785a3e2c662fc1f6f2840 *VS8/VC/crt/src/AMD64/xmt_lib/rtcmd.obj
24bb54a609d026c8286651b468dde940 *VS8/VC/crt/src/AMD64/xmt_lib/setjmp.obj
083ccb9da5f072abd8aeaa792bf53899 *VS8/VC/crt/src/AMD64/xmt_lib/setjmpex.obj
4a4e5ed84914eed13b3db25af2d4579a *VS8/VC/crt/src/AMD64/xmt_lib/tran.lib
1f7dda1c0dfb4a3deef3211b5541b05a *VS8/VC/crt/src/intel/almap.lib
595f376cfd0583882f67f3bf16d88760 *VS8/VC/crt/src/intel/almapdll.lib
25ad58abd0866a97fbdef036e5a43da6 *VS8/VC/crt/src/intel/dll_lib/alloca16.obj
d56db73696d63a332cb989a76f680b51 *VS8/VC/crt/src/intel/dll_lib/atlssup.obj
14c9bc820d76459873ca3315a5b5443d *VS8/VC/crt/src/intel/dll_lib/calldtor.obj
23d4f02f35b85bfa56bc68db936813c6 *VS8/VC/crt/src/intel/dll_lib/chandler4.obj
98bb8e62c7cfc243198fb309cd084706 *VS8/VC/crt/src/intel/dll_lib/chandler4gs.obj
78cbc8a96fae8c3c8e005e5c2dabba6e *VS8/VC/crt/src/intel/dll_lib/chkesp.obj
2b5a002ef8a128413b45d5db71013e55 *VS8/VC/crt/src/intel/dll_lib/chkstk.obj
66cbd5a50b3264b2cd90310ddb7db09d *VS8/VC/crt/src/intel/dll_lib/clr_obj/managdeh.obj
11e36fb9c69f077533dfc43339b2be1e *VS8/VC/crt/src/intel/dll_lib/clr_obj/mehvccctr.obj
4a55ea5220ae006a4d91c8b78722ff0a *VS8/VC/crt/src/intel/dll_lib/clr_obj/mehvcccvb.obj
874493c0767ae80e925e5831a1ef8401 *VS8/VC/crt/src/intel/dll_lib/clr_obj/mehvecctr.obj
d5493271b30649eda547800a114be8fe *VS8/VC/crt/src/intel/dll_lib/clr_obj/mehveccvb.obj
89ec2e8485338c175f5e6f8611013254 *VS8/VC/crt/src/intel/dll_lib/clr_obj/mehvecdtr.obj
adc5b1ac604693c72cb6bcf0b9496f79 *VS8/VC/crt/src/intel/dll_lib/clr_obj/mstdexpt.obj
9455e18a0615319c880a3928e77cf2ef *VS8/VC/crt/src/intel/dll_lib/conv.lib
1b8be116b4148218f6175a880780f732 *VS8/VC/crt/src/intel/dll_lib/cpu_disp.obj
b0e607978d3669cdf79b924bbf8dca04 *VS8/VC/crt/src/intel/dll_lib/dllsupp.obj
43bc6e5e0b58592b9143b287a26348cd *VS8/VC/crt/src/intel/dll_lib/eh.lib
a6a00d2549fb12e3b6c7f3e3be783b67 *VS8/VC/crt/src/intel/dll_lib/eh3valid.obj
dc81cb81be40e721f98f60cae463207c *VS8/VC/crt/src/intel/dll_lib/ehprolg2.obj
f8b1cdc50eced3e421f12a422bf5b81d *VS8/VC/crt/src/intel/dll_lib/ehprolg3.obj
6ff1b9d0b1e29489252e049121ac3e25 *VS8/VC/crt/src/intel/dll_lib/ehprolg3a.obj
0b1663047dbb463572cc77617ff8c462 *VS8/VC/crt/src/intel/dll_lib/ehprolog.obj
d3c62c3c57ea54dc9c210206f0855f84 *VS8/VC/crt/src/intel/dll_lib/ehvccctr.obj
f48376ce62752963c54aab906bc5a7d8 *VS8/VC/crt/src/intel/dll_lib/ehvcccvb.obj
f9a839d52f15813574879bab323fad4b *VS8/VC/crt/src/intel/dll_lib/ehvecctr.obj
0a10f4301930603c8f1014a4635d8964 *VS8/VC/crt/src/intel/dll_lib/ehveccvb.obj
cb40e5c92ae9c581173fd38a5b7586be *VS8/VC/crt/src/intel/dll_lib/ehvecdtr.obj
57f89eae0c671646da4977a94495bbfd *VS8/VC/crt/src/intel/dll_lib/enable.obj
8e0982e76ae0f79eb18c8d0025eaa58e *VS8/VC/crt/src/intel/dll_lib/exsup.obj
5284f2a643a7275fddb9919bb7c03f59 *VS8/VC/crt/src/intel/dll_lib/exsup2.obj
5c43968d9aab81a43970d5958ee58d8e *VS8/VC/crt/src/intel/dll_lib/exsup3.obj
17b318be6b86cf79e2998ba1479663c4 *VS8/VC/crt/src/intel/dll_lib/exsup4.obj
22610b290eaf4916b92d0ab548ca7e15 *VS8/VC/crt/src/intel/dll_lib/ftol2.obj
ade7fb7dce5812457443d2dafca077c1 *VS8/VC/crt/src/intel/dll_lib/inp.obj
0e9ecb1c24afb98322aaf941c7af4706 *VS8/VC/crt/src/intel/dll_lib/lldiv.obj
410db8c8a53a161b16e7ce1a36a71a8a *VS8/VC/crt/src/intel/dll_lib/lldvrm.obj
7bcf093c82430d50941d12af43e82b70 *VS8/VC/crt/src/intel/dll_lib/llmul.obj
85f0f9c3806f21b67e9ee5ddab416a87 *VS8/VC/crt/src/intel/dll_lib/llrem.obj
99780e49bf3f71cb61c5ae02ce89e6f2 *VS8/VC/crt/src/intel/dll_lib/llshl.obj
acbb9e48358666426cc8e785b2f43ac6 *VS8/VC/crt/src/intel/dll_lib/llshr.obj
0e346fd36327d256d63bbddd852a66bf *VS8/VC/crt/src/intel/dll_lib/longjmp.obj
13e20618b533beeb3fe4e474a41a0359 *VS8/VC/crt/src/intel/dll_lib/matherr.obj
d77cb2b478ea2b113bb7428b30ebce41 *VS8/VC/crt/src/intel/dll_lib/memccpy.obj
bbcc623030eb870712553336b03e794d *VS8/VC/crt/src/intel/dll_lib/memchr.obj
074bd634c376502716d7bbd1fa0c08c0 *VS8/VC/crt/src/intel/dll_lib/memcmp.obj
4709f8cd464a5b9f39a7b24aa7d940fb *VS8/VC/crt/src/intel/dll_lib/memcpy.obj
5dd4f165354447322e9c215599bb02c5 *VS8/VC/crt/src/intel/dll_lib/memmove.obj
2f22aa59f21bad56ddc60e204a768fbf *VS8/VC/crt/src/intel/dll_lib/memset.obj
e692286a60e4c260452374287f777970 *VS8/VC/crt/src/intel/dll_lib/oldexcpt.obj
0224ce3f5a41cf073d8376004c4e1977 *VS8/VC/crt/src/intel/dll_lib/outp.obj
5512e97481fefcb336a2470dc490d4ff *VS8/VC/crt/src/intel/dll_lib/p4_memcpy.obj
8710804b7062d9ddb1fc99a9414413ed *VS8/VC/crt/src/intel/dll_lib/p4_memset.obj
b340eae38e435e79ad47293cb537b4d6 *VS8/VC/crt/src/intel/dll_lib/pure_obj/managdeh.obj
9337742569b33e7450f03dc0d799897d *VS8/VC/crt/src/intel/dll_lib/pure_obj/mehvccctr.obj
28ed42a7047c280e1abc57c1cad45ad8 *VS8/VC/crt/src/intel/dll_lib/pure_obj/mehvcccvb.obj
e7394250eee3e041189248e178f3646d *VS8/VC/crt/src/intel/dll_lib/pure_obj/mehvecctr.obj
d9f9332d102be40ae4de7cd4cdaa4da5 *VS8/VC/crt/src/intel/dll_lib/pure_obj/mehveccvb.obj
0d43a187fc4b450e4268f4f615eafadf *VS8/VC/crt/src/intel/dll_lib/pure_obj/mehvecdtr.obj
f6b437c285226fb0503cbe1c446798d3 *VS8/VC/crt/src/intel/dll_lib/pure_obj/rtti.obj
73a93e3252b2e9094e808be9e7648ad9 *VS8/VC/crt/src/intel/dll_lib/rtc.lib
8bf9467f40b4a966f2c8074385cbd47b *VS8/VC/crt/src/intel/dll_lib/sehprolg.obj
6ecde05e15fb8ed747dce2508f0e746c *VS8/VC/crt/src/intel/dll_lib/sehprolg4.obj
8c0d379a8961f910b6e2d8e361789caa *VS8/VC/crt/src/intel/dll_lib/sehprolg4gs.obj
8e04454df9bf535935291c9eac58d3c5 *VS8/VC/crt/src/intel/dll_lib/sehsupp.obj
b6890ca42f2fcde6c6525dfa79b08afb *VS8/VC/crt/src/intel/dll_lib/setjmp.obj
06c6e3f810fd0017f8a07a0425ee17ac *VS8/VC/crt/src/intel/dll_lib/setjmp3.obj
a6003739868585505e35a8869128b616 *VS8/VC/crt/src/intel/dll_lib/setjmpex.obj
8fac236f52ee140739defff091509ed9 *VS8/VC/crt/src/intel/dll_lib/strcat.obj
66437629aff60fa4469a3281e57f42d5 *VS8/VC/crt/src/intel/dll_lib/strchr.obj
10a270ac4523ed6fd66261a937d93a2d *VS8/VC/crt/src/intel/dll_lib/strcmp.obj
2e7ad287a1d3cb11848f4dae6bae349c *VS8/VC/crt/src/intel/dll_lib/strcspn.obj
14a94b7592b8341490df4577fda319b7 *VS8/VC/crt/src/intel/dll_lib/strlen.obj
257c7ef6e000a7b8d9f21ca72d0b787f *VS8/VC/crt/src/intel/dll_lib/strncat.obj
f642fa22120a2bf15e7fc15d0548f706 *VS8/VC/crt/src/intel/dll_lib/strncpy.obj
1c6ff00128a55bd4c7675be574847e02 *VS8/VC/crt/src/intel/dll_lib/strnset.obj
f581c7a1b64c40a980d8455700a4a03b *VS8/VC/crt/src/intel/dll_lib/strpbrk.obj
d01eeafa182fd113a8d1c4a628b76a43 *VS8/VC/crt/src/intel/dll_lib/strrchr.obj
c53d44219bc876e0cae3270c91f65e1e *VS8/VC/crt/src/intel/dll_lib/strrev.obj
704c7fc2d7128b166efc85af4e10a2c5 *VS8/VC/crt/src/intel/dll_lib/strset.obj
1e281ed8fee02d9a64a4f74558e014b7 *VS8/VC/crt/src/intel/dll_lib/strspn.obj
f7912174d8c73aeb8b664d6cfbb85d9b *VS8/VC/crt/src/intel/dll_lib/strstr.obj
89b649c6b952c8ca3e27dd868c530bcf *VS8/VC/crt/src/intel/dll_lib/tncleanup.obj
17e104181c53add9e56b7647681c4f89 *VS8/VC/crt/src/intel/dll_lib/tran.lib
d02f88116382bf98fef5df27e71a747e *VS8/VC/crt/src/intel/dll_lib/ulldiv.obj
cc0e4dba27cc2f6419074600b09da855 *VS8/VC/crt/src/intel/dll_lib/ulldvrm.obj
5bcab93434ee5617c66a28dcb599a0d3 *VS8/VC/crt/src/intel/dll_lib/ullrem.obj
0da4a078641e4a9177bfabe3effe8d87 *VS8/VC/crt/src/intel/dll_lib/ullshr.obj
4b5fb5fc6d5a42a4f01d5a7959e78d43 *VS8/VC/crt/src/intel/dll_lib/_memicmp.obj
2062c53a0c0ecfc55fedfd742ca82b52 *VS8/VC/crt/src/intel/dll_lib/_strnicm.obj
8ea9da99373ac07a3c5ff1108eca0ebb *VS8/VC/crt/src/intel/mt_lib/alloca16.obj
7ee0e1d1ff748e3c7ba4d2bd5c3a1092 *VS8/VC/crt/src/intel/mt_lib/atlssup.obj
db667b3ddeb504c91fa8e6c5b268e514 *VS8/VC/crt/src/intel/mt_lib/calldtor.obj
4630ceb6037b34e16927b43cf0a187e6 *VS8/VC/crt/src/intel/mt_lib/chandler4.obj
3227308273890dd96d6249302a5a58df *VS8/VC/crt/src/intel/mt_lib/chandler4gs.obj
53f4bdadaf9447a33ac43b26a6df58a9 *VS8/VC/crt/src/intel/mt_lib/chkesp.obj
f573ac304d627e8221c17ec9dd492e43 *VS8/VC/crt/src/intel/mt_lib/chkstk.obj
ae1bd959537265f1c7917baab3fe4d00 *VS8/VC/crt/src/intel/mt_lib/conv.lib
2e978f29ec7dc13d5c4411a07e757b86 *VS8/VC/crt/src/intel/mt_lib/eh.lib
030863bfa22e447e741b8f18200b4b9e *VS8/VC/crt/src/intel/mt_lib/eh3valid.obj
db4b06be130bd0f2676a35e10d1e7308 *VS8/VC/crt/src/intel/mt_lib/enable.obj
98ed358f09c22e97af4ac20a3cb79389 *VS8/VC/crt/src/intel/mt_lib/exsup.obj
237aa91804586338ecbc0a641943824c *VS8/VC/crt/src/intel/mt_lib/exsup2.obj
344958b5d1f1137a326547d96b5e04aa *VS8/VC/crt/src/intel/mt_lib/exsup3.obj
a073ce7564ff72a6046adaf6e1004836 *VS8/VC/crt/src/intel/mt_lib/exsup4.obj
7895225ddba29a9793697bab82eabdeb *VS8/VC/crt/src/intel/mt_lib/inp.obj
52731babaa1a8af04e545a7e98c89012 *VS8/VC/crt/src/intel/mt_lib/lldiv.obj
af824a21cc9069002f413da0deedc8f0 *VS8/VC/crt/src/intel/mt_lib/lldvrm.obj
65f29907576313625284ad0f245a95b0 *VS8/VC/crt/src/intel/mt_lib/llmul.obj
a60c09d8c2d91dc34ea3327eb1bc9ca0 *VS8/VC/crt/src/intel/mt_lib/llrem.obj
76fccdac48d1e689618df4611a9d2971 *VS8/VC/crt/src/intel/mt_lib/llshl.obj
fb8c6a07736b8f4fddbf61fcbedd45ba *VS8/VC/crt/src/intel/mt_lib/llshr.obj
a051b3f1dfe1bf0613d902d39c397872 *VS8/VC/crt/src/intel/mt_lib/longjmp.obj
b1aba28208ae701ba747a4a6397e921b *VS8/VC/crt/src/intel/mt_lib/matherr.obj
5a740e6b13b280a0c6565419098840a5 *VS8/VC/crt/src/intel/mt_lib/memccpy.obj
e540aab7e1821e1094873b6344b718b3 *VS8/VC/crt/src/intel/mt_lib/memchr.obj
ab4bfa84895a0e233dbfa8fdc076e7eb *VS8/VC/crt/src/intel/mt_lib/memcmp.obj
6e8a4710fb884fe26721548eb5ada897 *VS8/VC/crt/src/intel/mt_lib/memcpy.obj
65d8743d20f1b1cb174b409a8dd4228b *VS8/VC/crt/src/intel/mt_lib/memmove.obj
350793e82ba26040610097e11a27c370 *VS8/VC/crt/src/intel/mt_lib/memset.obj
6e9db0976b05e9891fb548e9fb16ca96 *VS8/VC/crt/src/intel/mt_lib/outp.obj
fd5a17105d98b6332c4fc8143d1855c2 *VS8/VC/crt/src/intel/mt_lib/p4_memcpy.obj
76a13ee1f0652057006feb7d474e0f61 *VS8/VC/crt/src/intel/mt_lib/p4_memset.obj
484b22050da8c5f98f206ed548e70bd3 *VS8/VC/crt/src/intel/mt_lib/rtc.lib
42825c32c921fb2e47f0856d12d4525d *VS8/VC/crt/src/intel/mt_lib/sehprolg.obj
5c5b8b9723d091806715c4285534c8b6 *VS8/VC/crt/src/intel/mt_lib/sehprolg4.obj
48c895aca5a643e99e5578e7f8f03822 *VS8/VC/crt/src/intel/mt_lib/sehprolg4gs.obj
0035bbdb25eb843be2e031e1f61aa6a1 *VS8/VC/crt/src/intel/mt_lib/sehsupp.obj
4b3f6010f01ac71f8f1e6089a541348a *VS8/VC/crt/src/intel/mt_lib/setjmp.obj
d8cea0f8f68ef104bf5d06102702f264 *VS8/VC/crt/src/intel/mt_lib/setjmp3.obj
17866fc573176e07bd4a7b9113ea8e0e *VS8/VC/crt/src/intel/mt_lib/setjmpex.obj
2a99f35799b5a24739a513617f8edb1f *VS8/VC/crt/src/intel/mt_lib/strcat.obj
12c8662c24db4fcb7b4388e5015208c1 *VS8/VC/crt/src/intel/mt_lib/strchr.obj
515eaeae4d86a24bb6ee1531733e7708 *VS8/VC/crt/src/intel/mt_lib/strcmp.obj
a30f2d4db5359bf23ecd7ec28e64e81f *VS8/VC/crt/src/intel/mt_lib/strcspn.obj
c6108d80a30fd578c85cbe59ac7b7db9 *VS8/VC/crt/src/intel/mt_lib/strlen.obj
f1f38af92e9072146ee4e37864a52c9f *VS8/VC/crt/src/intel/mt_lib/strncat.obj
10d3168da80e205853c69aa5693b1bd1 *VS8/VC/crt/src/intel/mt_lib/strncpy.obj
53409434ab6087a2d26780e400d62f4d *VS8/VC/crt/src/intel/mt_lib/strnset.obj
85619e312666e465f3c30323f6d19eb8 *VS8/VC/crt/src/intel/mt_lib/strpbrk.obj
c23cdbdb475f6b0f883af93d863c4a99 *VS8/VC/crt/src/intel/mt_lib/strrchr.obj
431328b6176dd55d68e7a16f551a61cf *VS8/VC/crt/src/intel/mt_lib/strrev.obj
bfbdfcc27688e9565cc3c3979eb58f01 *VS8/VC/crt/src/intel/mt_lib/strset.obj
0f66a167d6f6ef547781210f5a60f604 *VS8/VC/crt/src/intel/mt_lib/strspn.obj
cdad57a06493a39c64cd8dd201b2f402 *VS8/VC/crt/src/intel/mt_lib/strstr.obj
41ae6f36f36e3bf9a2fefedd4fdc6447 *VS8/VC/crt/src/intel/mt_lib/tran.lib
f4811d822462c6cef79fcc11c45e3292 *VS8/VC/crt/src/intel/mt_lib/ulldiv.obj
a3b5006ee837f3484da9be0d2dfc7f00 *VS8/VC/crt/src/intel/mt_lib/ulldvrm.obj
4af32ccd838f178f319e8c590d3e3596 *VS8/VC/crt/src/intel/mt_lib/ullrem.obj
0de9c1e75d8ab65a62f8a5b10a730a30 *VS8/VC/crt/src/intel/mt_lib/ullshr.obj
771b8a87bd5f96a31c7407e620a6e0eb *VS8/VC/crt/src/intel/mt_lib/_memicmp.obj
c49f20b9d9155961d710cbe81f9f90ca *VS8/VC/crt/src/intel/mt_lib/_strnicm.obj
06307e049c4c1ccc82a6bec0e0bfaebe *VS8/VC/crt/src/intel/sdknames.lib
d7b9aa5a66012bbeac5fecbb7a271549 *VS8/VC/crt/src/intel/tcmap.lib
e525ab0de8e0b8e4b51555c509a8a5fb *VS8/VC/crt/src/intel/tcmapdll.lib
37290cdfd08f787b71550c4aea3a9f99 *VS8/VC/crt/src/intel/xdll_lib/alloca16.obj
2625a23e4b29fd37501d7f559286c5e0 *VS8/VC/crt/src/intel/xdll_lib/atlssup.obj
0f802d10f524e680ab6b941e94e3f473 *VS8/VC/crt/src/intel/xdll_lib/calldtor.obj
f7beb806203faa4867d71c559c804451 *VS8/VC/crt/src/intel/xdll_lib/chandler4.obj
3e4a81e67a9121fa858972b1f33a91a0 *VS8/VC/crt/src/intel/xdll_lib/chandler4gs.obj
171ef7063542d389f5b03c273a28dcce *VS8/VC/crt/src/intel/xdll_lib/chkesp.obj
7536c25189bd5106412d628e26e0c922 *VS8/VC/crt/src/intel/xdll_lib/chkstk.obj
9bb6fc52ff7526803b5038ffc8a1469a *VS8/VC/crt/src/intel/xdll_lib/clr_obj/managdeh.obj
777a96ee745d5d8e4b3cc8fddd25afb6 *VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehvccctr.obj
2d79894607d514e3847cececcfd0c55f *VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehvcccvb.obj
e92520704c8236861ce29520876dfa9a *VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehvecctr.obj
52de60314666975e01a1420d4e915ba1 *VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehveccvb.obj
4e366b5a38fec89945df16ec5475612a *VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehvecdtr.obj
5753d5d97b25dc5df4d6710e480f3371 *VS8/VC/crt/src/intel/xdll_lib/clr_obj/mstdexpt.obj
d440f3ff6cbc2e2fdbdcbd9c42a61bb8 *VS8/VC/crt/src/intel/xdll_lib/conv.lib
a27b0b65652ca64051cee75004d0de57 *VS8/VC/crt/src/intel/xdll_lib/cpu_disp.obj
6446006e835502028c4a82eea2bfba7c *VS8/VC/crt/src/intel/xdll_lib/dllsupp.obj
2bd9f3fdafe7d8d8432ab7635da60dc4 *VS8/VC/crt/src/intel/xdll_lib/eh.lib
9643f6e70300b54e6ee6e561e7b3eac1 *VS8/VC/crt/src/intel/xdll_lib/eh3valid.obj
a1ce6d51e4c293497f10c9bc074e0d87 *VS8/VC/crt/src/intel/xdll_lib/ehprolg2.obj
423a951437872662e0b5a3d939d909eb *VS8/VC/crt/src/intel/xdll_lib/ehprolg3.obj
34f24054c22594ccd2b969cfc6d0dbb7 *VS8/VC/crt/src/intel/xdll_lib/ehprolg3a.obj
060689c3c163877d0ddd1888f6acb7c8 *VS8/VC/crt/src/intel/xdll_lib/ehprolog.obj
cbda68197e12c798c0ee2ddfb62e3c57 *VS8/VC/crt/src/intel/xdll_lib/ehvccctr.obj
97a00b829777188f234bbc2ae36acf55 *VS8/VC/crt/src/intel/xdll_lib/ehvcccvb.obj
5a15fff65a98b2df828731db4b61fc73 *VS8/VC/crt/src/intel/xdll_lib/ehvecctr.obj
1d6340039699da32c338440096a06a92 *VS8/VC/crt/src/intel/xdll_lib/ehveccvb.obj
f2834f234f0b99a8fd602fbe4193f773 *VS8/VC/crt/src/intel/xdll_lib/ehvecdtr.obj
af1c0038510f9fffcf3d198520ccd230 *VS8/VC/crt/src/intel/xdll_lib/enable.obj
203be905e6fe0c4eade48944cfa0a752 *VS8/VC/crt/src/intel/xdll_lib/exsup.obj
6e0e8678a24852686fa9ccd2c43a9395 *VS8/VC/crt/src/intel/xdll_lib/exsup2.obj
eb427384fb2a4895f1d9e5f4a8838ed6 *VS8/VC/crt/src/intel/xdll_lib/exsup3.obj
d92c2b364e90596b3e503afa967ca6fa *VS8/VC/crt/src/intel/xdll_lib/exsup4.obj
25180e87002134829638e449ad1d8769 *VS8/VC/crt/src/intel/xdll_lib/ftol2.obj
c83bee44fbe3258dd0cebc5d635615ee *VS8/VC/crt/src/intel/xdll_lib/inp.obj
edc5728686bc9d2a033c6a138acc545e *VS8/VC/crt/src/intel/xdll_lib/lldiv.obj
ae55f39b07b787b9e7259a90517f5f22 *VS8/VC/crt/src/intel/xdll_lib/lldvrm.obj
6187a15310a413ead4f2f5d278f3aea1 *VS8/VC/crt/src/intel/xdll_lib/llmul.obj
580749a219340572360aef898f47c7d6 *VS8/VC/crt/src/intel/xdll_lib/llrem.obj
053380241793193e5c34845aacc161fc *VS8/VC/crt/src/intel/xdll_lib/llshl.obj
c8ca3f737455f9afd02f444a90b39881 *VS8/VC/crt/src/intel/xdll_lib/llshr.obj
4a2fa47285c986224095bfb78a4a9825 *VS8/VC/crt/src/intel/xdll_lib/longjmp.obj
ecbb5a7114f7a94762de2147c69bdbac *VS8/VC/crt/src/intel/xdll_lib/matherr.obj
c5432b63301d167fe6771f1198b385bc *VS8/VC/crt/src/intel/xdll_lib/memccpy.obj
8e1ccf1725382aa1a8e62b59857fea36 *VS8/VC/crt/src/intel/xdll_lib/memchr.obj
39a74f36c1683b41848d1e1515573642 *VS8/VC/crt/src/intel/xdll_lib/memcmp.obj
1b4b82678080225284683ecb97caad83 *VS8/VC/crt/src/intel/xdll_lib/memcpy.obj
534cbefbeb11bfc88d2cec92c6956a73 *VS8/VC/crt/src/intel/xdll_lib/memmove.obj
2787c3edeaefbf09c7d341a2a0bc5b2f *VS8/VC/crt/src/intel/xdll_lib/memset.obj
480e2df56219666a02405422c986ca71 *VS8/VC/crt/src/intel/xdll_lib/oldexcpt.obj
db2bd6ca0c064214e6b8a70b337c11bf *VS8/VC/crt/src/intel/xdll_lib/outp.obj
1bf34ab6f00a414ff8b05c54866834c7 *VS8/VC/crt/src/intel/xdll_lib/p4_memcpy.obj
30dec0641e4b4f5935fcc35377805534 *VS8/VC/crt/src/intel/xdll_lib/p4_memset.obj
24516c381c1aad85626496f6843cbe99 *VS8/VC/crt/src/intel/xdll_lib/pure_obj/managdeh.obj
e8a139a28b43805c30120a37184e67e4 *VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehvccctr.obj
67efbc4f1fb06928f3313ae901cdd884 *VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehvcccvb.obj
3de7b44d0fc1b4d5a0b7e434a26d5cc2 *VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehvecctr.obj
154bf9e954de7c9834aa366221841f16 *VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehveccvb.obj
0bef95da6d1dd948abe7c76ab38e6cbd *VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehvecdtr.obj
a8ff3cc543a319bbea63afc2d396e73f *VS8/VC/crt/src/intel/xdll_lib/pure_obj/rtti.obj
0ee054765b4ac915bb81475401d7435d *VS8/VC/crt/src/intel/xdll_lib/rtc.lib
d3583981249056c9ba842218fd87a8fc *VS8/VC/crt/src/intel/xdll_lib/sehprolg.obj
5f747a00d8f7d48eb5daa93f1c8db8ae *VS8/VC/crt/src/intel/xdll_lib/sehprolg4.obj
ec5e503682da3d8a3552c5be003f0817 *VS8/VC/crt/src/intel/xdll_lib/sehprolg4gs.obj
acf2013f68e7c43b8f3e0cb13f80ae97 *VS8/VC/crt/src/intel/xdll_lib/sehsupp.obj
3ed1654c0bb69ff5c341d6e5c1d7d245 *VS8/VC/crt/src/intel/xdll_lib/setjmp.obj
eaf7650e20605e04414b024f0b0b0682 *VS8/VC/crt/src/intel/xdll_lib/setjmp3.obj
8e607901867e6103b95f52e1c530869a *VS8/VC/crt/src/intel/xdll_lib/setjmpex.obj
de8cfbf6d1d2f449309d124a394b5db6 *VS8/VC/crt/src/intel/xdll_lib/strcat.obj
f36c61327f605622a679144be456e394 *VS8/VC/crt/src/intel/xdll_lib/strchr.obj
594e37950793afcd2928417611c6a7e9 *VS8/VC/crt/src/intel/xdll_lib/strcmp.obj
0e9979ba3572fe6d201d5f01535893e8 *VS8/VC/crt/src/intel/xdll_lib/strcspn.obj
edb732050af9cdf5640e5345c3819af6 *VS8/VC/crt/src/intel/xdll_lib/strlen.obj
194f192f5b12dd246873750caf7388da *VS8/VC/crt/src/intel/xdll_lib/strncat.obj
24bb80436c6842cfc3d17e706ff8d540 *VS8/VC/crt/src/intel/xdll_lib/strncpy.obj
948cca676d4669d9ee402eee66db1d73 *VS8/VC/crt/src/intel/xdll_lib/strnset.obj
98a803f76389c462b1ebad5f90dedeac *VS8/VC/crt/src/intel/xdll_lib/strpbrk.obj
963880246db7a1492dc1f738117f43ae *VS8/VC/crt/src/intel/xdll_lib/strrchr.obj
20e1af12bb5c89869888b252ed96666b *VS8/VC/crt/src/intel/xdll_lib/strrev.obj
0abdaa53f815ed6517a574616bdac921 *VS8/VC/crt/src/intel/xdll_lib/strset.obj
ec66934b8546049876a5b22265619318 *VS8/VC/crt/src/intel/xdll_lib/strspn.obj
e1387a35ddc181f53f13274b713db27d *VS8/VC/crt/src/intel/xdll_lib/strstr.obj
6623f8d31d92f7d0d130cb3f3920fe54 *VS8/VC/crt/src/intel/xdll_lib/tncleanup.obj
cd860223882f53ff9cb5cc8f9f1dfde0 *VS8/VC/crt/src/intel/xdll_lib/tran.lib
f7b266a559dbec6244654aeaf388be9e *VS8/VC/crt/src/intel/xdll_lib/ulldiv.obj
f005a4c0f41c8041e3a95f8ffde2a424 *VS8/VC/crt/src/intel/xdll_lib/ulldvrm.obj
bea64c304dacc25c174c3bfd83de1cdd *VS8/VC/crt/src/intel/xdll_lib/ullrem.obj
d69034c9f2dbdecc4a92fccaeb18dbf1 *VS8/VC/crt/src/intel/xdll_lib/ullshr.obj
b4ecbd65bf04af7787d05d605781ed04 *VS8/VC/crt/src/intel/xdll_lib/_memicmp.obj
1335492449e33b67a4c5072eeb7aa641 *VS8/VC/crt/src/intel/xdll_lib/_strnicm.obj
7370cc452f8ff2f71a97349c852657ba *VS8/VC/crt/src/intel/xmt_lib/alloca16.obj
f3c3bbf02bca0f5c1c05c62c97a57d69 *VS8/VC/crt/src/intel/xmt_lib/atlssup.obj
d7ff4a34fc1fc6c854cb9dbe7c055745 *VS8/VC/crt/src/intel/xmt_lib/calldtor.obj
131e93c1fe9dafea8170689b9f95f168 *VS8/VC/crt/src/intel/xmt_lib/chandler4.obj
e7b8996c1dc265a2c65400c3f12645a1 *VS8/VC/crt/src/intel/xmt_lib/chandler4gs.obj
1d8b71dc5490b4773f12498674c0d47e *VS8/VC/crt/src/intel/xmt_lib/chkesp.obj
965e78702d189ab1c40cc6efd91829c7 *VS8/VC/crt/src/intel/xmt_lib/chkstk.obj
79845f3b123ea213ea844eb3e04947ed *VS8/VC/crt/src/intel/xmt_lib/conv.lib
71c823cae725126ba3b0f05b92338cff *VS8/VC/crt/src/intel/xmt_lib/eh.lib
06d2a52e2adde8b59983e172bd4a134e *VS8/VC/crt/src/intel/xmt_lib/eh3valid.obj
ba2c13558cfd86740cf81f91da5aa4d6 *VS8/VC/crt/src/intel/xmt_lib/enable.obj
5c659d7e54ed936be201974339be0f7b *VS8/VC/crt/src/intel/xmt_lib/exsup.obj
263aa2799f17bcf1a63f39e1ed7ad6b7 *VS8/VC/crt/src/intel/xmt_lib/exsup2.obj
ad31df237d1e20a1548b03b7a88e301e *VS8/VC/crt/src/intel/xmt_lib/exsup3.obj
24f64497c1781e03525e0a3189ec3631 *VS8/VC/crt/src/intel/xmt_lib/exsup4.obj
95bf48b01764abc9d1605fa6549cc5bf *VS8/VC/crt/src/intel/xmt_lib/inp.obj
b67a7a6bfa9270ccb0e6015ac4150ea7 *VS8/VC/crt/src/intel/xmt_lib/lldiv.obj
cb7c08bfa6566238da73470e3c65e821 *VS8/VC/crt/src/intel/xmt_lib/lldvrm.obj
e196bac66cb152d34ea0c68db55a6c62 *VS8/VC/crt/src/intel/xmt_lib/llmul.obj
af1c5383ac5bed32fb8127975a7a13a5 *VS8/VC/crt/src/intel/xmt_lib/llrem.obj
73f778ef6e75c68a1eabd4dc34001cd9 *VS8/VC/crt/src/intel/xmt_lib/llshl.obj
73b9b3747e96082157ebdf08b080661b *VS8/VC/crt/src/intel/xmt_lib/llshr.obj
8047ca3a5aa53dc9326912bc3eaca39e *VS8/VC/crt/src/intel/xmt_lib/longjmp.obj
9c753f1e240e86630611cdf36acbabc7 *VS8/VC/crt/src/intel/xmt_lib/matherr.obj
ccc4d810ee46761e019d4e76eb232dfa *VS8/VC/crt/src/intel/xmt_lib/memccpy.obj
6991b975f368520c42a8eb389f372476 *VS8/VC/crt/src/intel/xmt_lib/memchr.obj
7c8314ebea5e195db02f4061945da8da *VS8/VC/crt/src/intel/xmt_lib/memcmp.obj
7f2e1c9d9f2fc5f60125646d19202dd7 *VS8/VC/crt/src/intel/xmt_lib/memcpy.obj
581d71bf9355d78a0bfbebc9981fbf96 *VS8/VC/crt/src/intel/xmt_lib/memmove.obj
1d640ab29c52ffc97d51bbf4f6b8b4c9 *VS8/VC/crt/src/intel/xmt_lib/memset.obj
ddbb229377df3e7505919bdf7b680811 *VS8/VC/crt/src/intel/xmt_lib/outp.obj
deff92883c4b8aec1fa10165d9941a33 *VS8/VC/crt/src/intel/xmt_lib/p4_memcpy.obj
ff29c8e24be4936ca9ba4928e1c36ee1 *VS8/VC/crt/src/intel/xmt_lib/p4_memset.obj
958632aa2006e98a4bf587f70f2a9d4a *VS8/VC/crt/src/intel/xmt_lib/rtc.lib
30b7382d4278e0dcdb87609e4c910553 *VS8/VC/crt/src/intel/xmt_lib/sehprolg.obj
d6a6621a7bed76e3269b7563b36aa407 *VS8/VC/crt/src/intel/xmt_lib/sehprolg4.obj
06f3fc464d18a24d22f38c08d3170933 *VS8/VC/crt/src/intel/xmt_lib/sehprolg4gs.obj
b7e966a3a8a18c803df58aefea8eb9d9 *VS8/VC/crt/src/intel/xmt_lib/sehsupp.obj
22152681cdee6c8815dba1bce755087c *VS8/VC/crt/src/intel/xmt_lib/setjmp.obj
cb3e61e2699174c9ce08c03bd38b8259 *VS8/VC/crt/src/intel/xmt_lib/setjmp3.obj
f6c34961443e767f8db3209c82b124d3 *VS8/VC/crt/src/intel/xmt_lib/setjmpex.obj
484272669d53bd46b2b6e0e2715b2ce5 *VS8/VC/crt/src/intel/xmt_lib/strcat.obj
45baf823b842cc78c59fd9e3fb38f325 *VS8/VC/crt/src/intel/xmt_lib/strchr.obj
a44c069ac31ba90450ce607df67841a1 *VS8/VC/crt/src/intel/xmt_lib/strcmp.obj
a44b76542062f31f0798a565592d555b *VS8/VC/crt/src/intel/xmt_lib/strcspn.obj
4ddcb6b875eb6d93a1a951c521f03919 *VS8/VC/crt/src/intel/xmt_lib/strlen.obj
09afd2a068d36d40feb082e71f1d43f2 *VS8/VC/crt/src/intel/xmt_lib/strncat.obj
af56a1bfa1e8650d48fa7804c2a44342 *VS8/VC/crt/src/intel/xmt_lib/strncpy.obj
5fac9213311ef5481ca9a55e7d63ceb3 *VS8/VC/crt/src/intel/xmt_lib/strnset.obj
461bcf252cd519594e9c02b5424e1f95 *VS8/VC/crt/src/intel/xmt_lib/strpbrk.obj
bb90878f0f27d16fd239b1e1f47cc8e0 *VS8/VC/crt/src/intel/xmt_lib/strrchr.obj
2e18e29ae4b117d0a7a0aa56cb64ef05 *VS8/VC/crt/src/intel/xmt_lib/strrev.obj
f7fc606ab16559d6e65b805ef76c7531 *VS8/VC/crt/src/intel/xmt_lib/strset.obj
358a7475e82b9229e6452d2dd9eae9aa *VS8/VC/crt/src/intel/xmt_lib/strspn.obj
ed67c4257e099dadd2cccfe8c9d44c0f *VS8/VC/crt/src/intel/xmt_lib/strstr.obj
24e4e75d5896e0a20906bb75012bc2f4 *VS8/VC/crt/src/intel/xmt_lib/tran.lib
73e7e6af8959d0c5c4dcffaee795c490 *VS8/VC/crt/src/intel/xmt_lib/ulldiv.obj
f3fada322baa1da5646b91a9d9ff2cd3 *VS8/VC/crt/src/intel/xmt_lib/ulldvrm.obj
5df0da596bfa4bd2ec216e7168cc240e *VS8/VC/crt/src/intel/xmt_lib/ullrem.obj
f8a8753c705a1f4c08311c0b3ab87e02 *VS8/VC/crt/src/intel/xmt_lib/ullshr.obj
8381fe9bd27272f47cfb351c3baa27a2 *VS8/VC/crt/src/intel/xmt_lib/_memicmp.obj
0cf6ebe312f5dbcdd001bd60fad203e2 *VS8/VC/crt/src/intel/xmt_lib/_strnicm.obj
98b9ace3381189c9dd67ce915a48faf4 *VS8/VC/lib/amd64/binmode.obj
2d25fc94ea3b1d906a05a98894557bc6 *VS8/VC/lib/amd64/chkstk.obj
be4ee2ff52466e790a110aac0b080a73 *VS8/VC/lib/amd64/commode.obj
762ad072a7d9a0cddfb8354deb64bbe0 *VS8/VC/lib/amd64/comsupp.lib
df159524b5d1d60e5c14bc3175f72bf0 *VS8/VC/lib/amd64/comsuppd.lib
2037ffddf7fe1bd5ee1b4868642d5451 *VS8/VC/lib/amd64/comsuppw.lib
93b58ef38d2ea1dea0900bfcd0af366c *VS8/VC/lib/amd64/comsuppwd.lib
dc127b7e57a41171a5e0f2fd36f27e53 *VS8/VC/lib/amd64/delayimp.lib
fdec55369c70577395881f08cce5aa55 *VS8/VC/lib/amd64/invalidcontinue.obj
ca159acd326aac9050847c38fd194572 *VS8/VC/lib/amd64/libcmt.lib
4639f1d8d36ce6efd512bcdb86b60057 *VS8/VC/lib/amd64/libcmtd.lib
35abd4aca812bc94c8473eb74817ebb7 *VS8/VC/lib/amd64/libcpmt.lib
0d0f3aa1aa1806c1c0b7385c3a68346e *VS8/VC/lib/amd64/libcpmtd.lib
1ffb976f7016131bcf4de772ffccf50c *VS8/VC/lib/amd64/loosefpmath.obj
008b9c76edb1cc7e40fe9befbc3d7c06 *VS8/VC/lib/amd64/msvcmrt.lib
9708e0b0cdbc3d201e572667f57a099f *VS8/VC/lib/amd64/msvcmrtd.lib
1ee69764c278e9c6534d334acfae5593 *VS8/VC/lib/amd64/msvcprt.lib
28761739551a09b1eb53c2adda4d6290 *VS8/VC/lib/amd64/msvcprtd.lib
ac009abd3b6218e9b3b152e643233bc1 *VS8/VC/lib/amd64/msvcrt.lib
089469be976852a65dac0675cbfebdb3 *VS8/VC/lib/amd64/msvcrtd.lib
949739a9b628af3b297e67e3a6de4573 *VS8/VC/lib/amd64/msvcurt.lib
a5efef335f5cd6412bd0d3685aca229a *VS8/VC/lib/amd64/msvcurtd.lib
13e75dad402d44178164f52b799223da *VS8/VC/lib/amd64/newmode.obj
376136c657fb93d5dccb634723a033b1 *VS8/VC/lib/amd64/noarg.obj
988632e55ebdcffa39ce910f6bdfc302 *VS8/VC/lib/amd64/nochkclr.obj
50a76cc8c96a300866a283e94185c786 *VS8/VC/lib/amd64/noenv.obj
0122c3482c8817fd9d0ac7dd4d33672a *VS8/VC/lib/amd64/nothrownew.obj
ae4f4a328265e7dab6cfc2a1f608b027 *VS8/VC/lib/amd64/oldnames.lib
dddad714184980898393c46a65783952 *VS8/VC/lib/amd64/pbinmode.obj
081eb000764496dbd3b4f196970b2c09 *VS8/VC/lib/amd64/pcommode.obj
e45e88fd9d744cd89abba1d1f6116ce9 *VS8/VC/lib/amd64/pgobootrun.lib
1ad0bf1332cf4e35db6f1bb5de4fa56f *VS8/VC/lib/amd64/pgort.lib
0a21822a6dff6610c73b6760beb40954 *VS8/VC/lib/amd64/pinvalidcontinue.obj
aa6e0d2e06dc675eb9d513cae23101e9 *VS8/VC/lib/amd64/pnewmode.obj
35fa24c640cf68f4a03b15c367d7e392 *VS8/VC/lib/amd64/pnoarg.obj
b6ff7ee69230c056778b1b341e4db5e4 *VS8/VC/lib/amd64/pnoenv.obj
940421237e0e42acc35c9dba794c3688 *VS8/VC/lib/amd64/pnothrownew.obj
ff60f160edd4183e92ffcafd286db861 *VS8/VC/lib/amd64/psetargv.obj
0c8998ce04bde2e7585543401c40d00f *VS8/VC/lib/amd64/pthreadlocale.obj
a12b315dce922686b8301c3183af493d *VS8/VC/lib/amd64/ptrustm.lib
a49d7162cdc64e6fbab71920f5f1209c *VS8/VC/lib/amd64/ptrustmd.lib
0eb233dbe2a0efae81ff206af3ad6076 *VS8/VC/lib/amd64/ptrustu.lib
69a41611d5ad869056784e12da4d3b3d *VS8/VC/lib/amd64/ptrustud.lib
206fe59c8b094915b003e241f6d551a8 *VS8/VC/lib/amd64/pwsetargv.obj
bf288b624b57c2728163ee46cc9c9ecc *VS8/VC/lib/amd64/runtmchk.lib
6ad3c8c8e4f6d30b2346f810e61e3df2 *VS8/VC/lib/amd64/setargv.obj
79bdc06a863d1f0abc4bbdec89cb6bfc *VS8/VC/lib/amd64/smalheap.obj
5e95dab45ac0e4dd9d1c7e57be224391 *VS8/VC/lib/amd64/threadlocale.obj
38bc6c76aa29c82a08cc4d6ad3a723eb *VS8/VC/lib/amd64/vcomp.lib
e31af3b8a32548786e51863d6dd2c584 *VS8/VC/lib/amd64/vcompd.lib
4904f2d321efad91479d596795f67e73 *VS8/VC/lib/amd64/wsetargv.obj
d4fbd4f6cf189cd4c41484b9e3b69d1a *VS8/VC/lib/binmode.obj
f573ac304d627e8221c17ec9dd492e43 *VS8/VC/lib/chkstk.obj
cf41589114215eb4ac96baae85e3cb68 *VS8/VC/lib/commode.obj
15724fef01ea10992e4999d33f5eba1f *VS8/VC/lib/comsupp.lib
7d20d7a86739102006839d369277a168 *VS8/VC/lib/comsuppd.lib
acb26b69d4a4c0dde09709dfc90b93b3 *VS8/VC/lib/comsuppw.lib
2bc42373cfd634f890c1c2223960e2c9 *VS8/VC/lib/comsuppwd.lib
e14d6b14fc28019ea893478e84eb6d64 *VS8/VC/lib/delayimp.lib
183569a4b16d14834f4bae33136a61a9 *VS8/VC/lib/fp10.obj
86d1a4976b099ee541f5f87c901e8762 *VS8/VC/lib/invalidcontinue.obj
23a5a91898e5387327d1b7f55d3975c4 *VS8/VC/lib/libcmt.lib
29e9d2a0aeed593ce7b72205ed120db2 *VS8/VC/lib/libcmtd.lib
89a8ef9a81454dba9c1d882aa2b8dc4f *VS8/VC/lib/libcpmt.lib
4812dbad4d97d3d9fa13fda4e938f85b *VS8/VC/lib/libcpmtd.lib
36f5096ff7c13770f179bc143aa35776 *VS8/VC/lib/loosefpmath.obj
7a1efaa21907e0b4efd55dbb556c0c32 *VS8/VC/lib/msvcmrt.lib
aad004e115f8fb59853ac5f8ce4667eb *VS8/VC/lib/msvcmrtd.lib
20d64a73a00a7cb0d5118cdce669e143 *VS8/VC/lib/msvcprt.lib
1eb3c50986d54150a4f7daf2ca672df7 *VS8/VC/lib/msvcprtd.lib
9b2e7bce92d7e14136e8332172507eb8 *VS8/VC/lib/msvcrt.lib
9dc7b725adcd5f83ea10ca1a3fa15654 *VS8/VC/lib/msvcrtd.lib
255876bb93f96e559124a55956e2c705 *VS8/VC/lib/msvcurt.lib
cadfec2211d5f4fab19726ac9f05077d *VS8/VC/lib/msvcurtd.lib
f893ccf7bc150eed58711849056364ab *VS8/VC/lib/newmode.obj
969aaabec396354d7f6b95df76ccfd7e *VS8/VC/lib/noarg.obj
a8af4c2cb847ce5afa65e7a73ea1f353 *VS8/VC/lib/nochkclr.obj
3208d127fe3102c7c5fb81c26963dfcb *VS8/VC/lib/noenv.obj
6b25fc3eda400f6d0b9d4ea9bf1896ea *VS8/VC/lib/nothrownew.obj
df62d8d541322c98d480b0a9ea6aa890 *VS8/VC/lib/oldnames.lib
947f21d799b02a0091c648fb1cb01c41 *VS8/VC/lib/opends60.lib
bd4d25fc6fa0482bb7c4b28169fec2bb *VS8/VC/lib/pbinmode.obj
8c44138f0380a82357b1036d5736411e *VS8/VC/lib/pcommode.obj
a710a19b05b03ba0d3449b6656885153 *VS8/VC/lib/pgobootrun.lib
db466fad1559053a12642813a73c8dac *VS8/VC/lib/pgort.lib
c016949ec7ca14a911d34327f775062d *VS8/VC/lib/pinvalidcontinue.obj
399f1ea22e0c3476ff95b55a5c929a4b *VS8/VC/lib/pnewmode.obj
66082becff868bb8618b6b2cf62aad11 *VS8/VC/lib/pnoarg.obj
6465350374cd3e773a4403a893c9a6e4 *VS8/VC/lib/pnoenv.obj
322430eca717cb9fb6f11820d27461cc *VS8/VC/lib/pnothrownew.obj
a2a11c7c86cfd975046ecb4fa865e24e *VS8/VC/lib/psetargv.obj
5062ca8c42dfae0f8f479042710f58af *VS8/VC/lib/pthreadlocale.obj
e349dfcd075536300f3b3f98ea2f29f9 *VS8/VC/lib/ptrustm.lib
d7eeb00687040f6729fc1b3a92b115be *VS8/VC/lib/ptrustmd.lib
e56ef4fad29a27d1900b9237fee0738b *VS8/VC/lib/ptrustu.lib
f539e22052b09ce2d89ac01d1063a34c *VS8/VC/lib/ptrustud.lib
59affd225f7dbf4b948aa8fb2619ba83 *VS8/VC/lib/pwsetargv.obj
e91a69c87866f50dec73b73d95831c4d *VS8/VC/lib/RunTmChk.lib
6f44654969c0705198d4861d2a9e83a5 *VS8/VC/lib/setargv.obj
4c978df16e8d6fb8fa67b9aca407ab12 *VS8/VC/lib/smalheap.obj
0b9b781ed1be9582a54fd097b58fc2ff *VS8/VC/lib/threadlocale.obj
089876202ebfbda51b30d3f41cde7eb1 *VS8/VC/lib/vcomp.lib
d67143084030bb1f9372addf733de04e *VS8/VC/lib/vcompd.lib
da572ae594137ae9516729a22a603598 *VS8/VC/lib/wsetargv.obj
```

# .pat
```
$ find VS8/ -type f -exec ../../pcf.exe {} {}.pat \;
.\VS8\VC\atlmfc\lib\amd64\atl.lib: skipped 53, total 53
.\VS8\VC\atlmfc\lib\amd64\atldload.lib: skipped 35, total 368
.\VS8\VC\atlmfc\lib\amd64\atlmincrt.lib: skipped 0, total 49
.\VS8\VC\atlmfc\lib\amd64\atls.lib: skipped 18, total 282
.\VS8\VC\atlmfc\lib\amd64\atlsd.lib: skipped 0, total 330
.\VS8\VC\atlmfc\lib\amd64\eafxis.lib: skipped 21, total 230
.\VS8\VC\atlmfc\lib\amd64\eafxisd.lib: skipped 2, total 143
.\VS8\VC\atlmfc\lib\amd64\mfc80.lib: skipped 6653, total 6653
.\VS8\VC\atlmfc\lib\amd64\mfc80d.lib: skipped 9093, total 9093
.\VS8\VC\atlmfc\lib\amd64\mfc80u.lib: skipped 8067, total 8067
.\VS8\VC\atlmfc\lib\amd64\mfc80ud.lib: skipped 10871, total 10871
.\VS8\VC\atlmfc\lib\amd64\mfcdload.lib: skipped 277, total 690
.\VS8\VC\atlmfc\lib\amd64\MFCM80.lib: skipped 26, total 42
.\VS8\VC\atlmfc\lib\amd64\MFCM80D.lib: skipped 32, total 48
.\VS8\VC\atlmfc\lib\amd64\MFCM80U.lib: skipped 28, total 44
.\VS8\VC\atlmfc\lib\amd64\MFCM80UD.lib: skipped 34, total 50
.\VS8\VC\atlmfc\lib\amd64\mfcs80.lib: skipped 27, total 220
.\VS8\VC\atlmfc\lib\amd64\mfcs80d.lib: skipped 17, total 234
.\VS8\VC\atlmfc\lib\amd64\mfcs80u.lib: skipped 4, total 70
.\VS8\VC\atlmfc\lib\amd64\mfcs80ud.lib: skipped 2, total 84
.\VS8\VC\atlmfc\lib\amd64\nafxcw.lib: skipped 1645, total 17455
.\VS8\VC\atlmfc\lib\amd64\nafxcwd.lib: skipped 296, total 9730
.\VS8\VC\atlmfc\lib\amd64\nafxis.lib: skipped 7, total 116
.\VS8\VC\atlmfc\lib\amd64\nafxisd.lib: skipped 0, total 35
.\VS8\VC\atlmfc\lib\amd64\uafxcw.lib: skipped 2544, total 17922
.\VS8\VC\atlmfc\lib\amd64\uafxcwd.lib: skipped 1293, total 10479
.\VS8\VC\atlmfc\lib\Atl.lib: skipped 53, total 53
.\VS8\VC\atlmfc\lib\atldload.lib: skipped 9, total 365
.\VS8\VC\atlmfc\lib\atlmincrt.lib: skipped 0, total 49
.\VS8\VC\atlmfc\lib\atls.lib: skipped 23, total 1305
.\VS8\VC\atlmfc\lib\atlsd.lib: skipped 0, total 331
.\VS8\VC\atlmfc\lib\eafxis.lib: skipped 23, total 254
.\VS8\VC\atlmfc\lib\eafxisd.lib: skipped 0, total 159
.\VS8\VC\atlmfc\lib\mfc80.lib: skipped 7013, total 7013
.\VS8\VC\atlmfc\lib\mfc80d.lib: skipped 9480, total 9480
.\VS8\VC\atlmfc\lib\mfc80u.lib: skipped 8658, total 8658
.\VS8\VC\atlmfc\lib\mfc80ud.lib: skipped 11489, total 11489
.\VS8\VC\atlmfc\lib\mfcdload.lib: skipped 21, total 689
.\VS8\VC\atlmfc\lib\mfcm80.lib: skipped 27, total 43
.\VS8\VC\atlmfc\lib\mfcm80d.lib: skipped 34, total 50
.\VS8\VC\atlmfc\lib\mfcm80u.lib: skipped 29, total 45
.\VS8\VC\atlmfc\lib\mfcm80ud.lib: skipped 36, total 52
.\VS8\VC\atlmfc\lib\mfcs80.lib: skipped 31, total 243
.\VS8\VC\atlmfc\lib\mfcs80d.lib: skipped 17, total 259
.\VS8\VC\atlmfc\lib\mfcs80u.lib: skipped 5, total 72
.\VS8\VC\atlmfc\lib\mfcs80ud.lib: skipped 2, total 88
.\VS8\VC\atlmfc\lib\nafxcw.lib: skipped 1810, total 19506
.\VS8\VC\atlmfc\lib\nafxcwd.lib: skipped 259, total 10332
.\VS8\VC\atlmfc\lib\nafxis.lib: skipped 8, total 124
.\VS8\VC\atlmfc\lib\nafxisd.lib: skipped 0, total 36
.\VS8\VC\atlmfc\lib\uafxcw.lib: skipped 2750, total 20075
.\VS8\VC\atlmfc\lib\uafxcwd.lib: skipped 1366, total 11177
.\VS8\VC\crt\src\AMD64\almap.lib: skipped 46, total 46
.\VS8\VC\crt\src\AMD64\almapdll.lib: skipped 45, total 45
.\VS8\VC\crt\src\AMD64\dll_lib\amdsecgs.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\chandler.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\chkstk2.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\clr_obj\managdeh.obj: skipped 0, total 6
.\VS8\VC\crt\src\AMD64\dll_lib\clr_obj\mehvccctr.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\dll_lib\clr_obj\mehvcccvb.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\dll_lib\clr_obj\mehvecctr.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\dll_lib\clr_obj\mehveccvb.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\dll_lib\clr_obj\mehvecdtr.obj: skipped 0, total 6
.\VS8\VC\crt\src\AMD64\dll_lib\clr_obj\mstdexpt.obj: skipped 0, total 60
.\VS8\VC\crt\src\AMD64\dll_lib\conv.lib: skipped 3, total 72
.\VS8\VC\crt\src\AMD64\dll_lib\eh.lib: skipped 4, total 333
.\VS8\VC\crt\src\AMD64\dll_lib\ehvccctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\ehvcccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\ehvecctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\ehveccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\ehvecdtr.obj: skipped 0, total 3
.\VS8\VC\crt\src\AMD64\dll_lib\gshandler.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\dll_lib\gshandlereh.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\gshandlerseh.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\jmpuwind.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\longjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\matherr.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\dll_lib\oldexcpt.obj: skipped 0, total 15
.\VS8\VC\crt\src\AMD64\dll_lib\pure_obj\managdeh.obj: skipped 0, total 14
.\VS8\VC\crt\src\AMD64\dll_lib\pure_obj\mehvccctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\pure_obj\mehvcccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\pure_obj\mehvecctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\pure_obj\mehveccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\pure_obj\mehvecdtr.obj: skipped 0, total 3
.\VS8\VC\crt\src\AMD64\dll_lib\pure_obj\rtti.obj: skipped 0, total 76
.\VS8\VC\crt\src\AMD64\dll_lib\rtc.lib: skipped 0, total 31
.\VS8\VC\crt\src\AMD64\dll_lib\rtcmd.obj: skipped 2, total 2
.\VS8\VC\crt\src\AMD64\dll_lib\setjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\setjmpex.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\tncleanup.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\dll_lib\tran.lib: skipped 0, total 229
.\VS8\VC\crt\src\AMD64\mt_lib\amdsecgs.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\chandler.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\chkstk2.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\conv.lib: skipped 2, total 73
.\VS8\VC\crt\src\AMD64\mt_lib\eh.lib: skipped 4, total 287
.\VS8\VC\crt\src\AMD64\mt_lib\gshandler.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\mt_lib\gshandlereh.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\gshandlerseh.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\jmpuwind.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\longjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\matherr.obj: skipped 1, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\rtc.lib: skipped 0, total 31
.\VS8\VC\crt\src\AMD64\mt_lib\rtcmd.obj: skipped 2, total 2
.\VS8\VC\crt\src\AMD64\mt_lib\setjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\setjmpex.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\mt_lib\tran.lib: skipped 1, total 228
.\VS8\VC\crt\src\AMD64\sdknames.lib: skipped 20, total 20
.\VS8\VC\crt\src\AMD64\tcmap.lib: skipped 74, total 74
.\VS8\VC\crt\src\AMD64\tcmapdll.lib: skipped 74, total 74
.\VS8\VC\crt\src\AMD64\xdll_lib\amdsecgs.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\chandler.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\chkstk2.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\clr_obj\managdeh.obj: skipped 0, total 6
.\VS8\VC\crt\src\AMD64\xdll_lib\clr_obj\mehvccctr.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xdll_lib\clr_obj\mehvcccvb.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xdll_lib\clr_obj\mehvecctr.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xdll_lib\clr_obj\mehveccvb.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xdll_lib\clr_obj\mehvecdtr.obj: skipped 0, total 6
.\VS8\VC\crt\src\AMD64\xdll_lib\clr_obj\mstdexpt.obj: skipped 0, total 60
.\VS8\VC\crt\src\AMD64\xdll_lib\conv.lib: skipped 1, total 72
.\VS8\VC\crt\src\AMD64\xdll_lib\eh.lib: skipped 0, total 334
.\VS8\VC\crt\src\AMD64\xdll_lib\ehvccctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\ehvcccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\ehvecctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\ehveccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\ehvecdtr.obj: skipped 0, total 3
.\VS8\VC\crt\src\AMD64\xdll_lib\gshandler.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xdll_lib\gshandlereh.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\gshandlerseh.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\jmpuwind.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\longjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\matherr.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xdll_lib\oldexcpt.obj: skipped 0, total 15
.\VS8\VC\crt\src\AMD64\xdll_lib\pure_obj\managdeh.obj: skipped 0, total 14
.\VS8\VC\crt\src\AMD64\xdll_lib\pure_obj\mehvccctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\pure_obj\mehvcccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\pure_obj\mehvecctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\pure_obj\mehveccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\pure_obj\mehvecdtr.obj: skipped 0, total 3
.\VS8\VC\crt\src\AMD64\xdll_lib\pure_obj\rtti.obj: skipped 0, total 76
.\VS8\VC\crt\src\AMD64\xdll_lib\rtc.lib: skipped 0, total 31
.\VS8\VC\crt\src\AMD64\xdll_lib\rtcmd.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xdll_lib\setjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\setjmpex.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\tncleanup.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xdll_lib\tran.lib: skipped 0, total 229
.\VS8\VC\crt\src\AMD64\xmt_lib\amdsecgs.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\chandler.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\chkstk2.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\conv.lib: skipped 1, total 73
.\VS8\VC\crt\src\AMD64\xmt_lib\eh.lib: skipped 0, total 288
.\VS8\VC\crt\src\AMD64\xmt_lib\gshandler.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xmt_lib\gshandlereh.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\gshandlerseh.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\jmpuwind.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\longjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\matherr.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\rtc.lib: skipped 0, total 31
.\VS8\VC\crt\src\AMD64\xmt_lib\rtcmd.obj: skipped 0, total 2
.\VS8\VC\crt\src\AMD64\xmt_lib\setjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\setjmpex.obj: skipped 0, total 1
.\VS8\VC\crt\src\AMD64\xmt_lib\tran.lib: skipped 0, total 228
.\VS8\VC\crt\src\intel\almap.lib: skipped 47, total 47
.\VS8\VC\crt\src\intel\almapdll.lib: skipped 46, total 46
.\VS8\VC\crt\src\intel\dll_lib\alloca16.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\atlssup.obj: skipped 0, total 0
.\VS8\VC\crt\src\intel\dll_lib\calldtor.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\chandler4.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\chandler4gs.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\chkesp.obj: skipped 2, total 3
.\VS8\VC\crt\src\intel\dll_lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\clr_obj\managdeh.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\dll_lib\clr_obj\mehvccctr.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\clr_obj\mehvcccvb.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\clr_obj\mehvecctr.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\clr_obj\mehveccvb.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\clr_obj\mehvecdtr.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\dll_lib\clr_obj\mstdexpt.obj: skipped 0, total 60
.\VS8\VC\crt\src\intel\dll_lib\conv.lib: skipped 2, total 72
.\VS8\VC\crt\src\intel\dll_lib\cpu_disp.obj: skipped 0, total 3
.\VS8\VC\crt\src\intel\dll_lib\dllsupp.obj: skipped 0, total 0
.\VS8\VC\crt\src\intel\dll_lib\eh.lib: skipped 7, total 338
.\VS8\VC\crt\src\intel\dll_lib\eh3valid.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\ehprolg2.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ehprolg3.obj: skipped 0, total 7
.\VS8\VC\crt\src\intel\dll_lib\ehprolg3a.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\dll_lib\ehprolog.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ehvccctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ehvcccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ehvecctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ehveccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ehvecdtr.obj: skipped 0, total 3
.\VS8\VC\crt\src\intel\dll_lib\enable.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\exsup.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\exsup2.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\exsup3.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\exsup4.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ftol2.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\inp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\lldiv.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\lldvrm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\llmul.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\llrem.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\llshl.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\llshr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\longjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\matherr.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\memccpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\memchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\memcmp.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\dll_lib\memcpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\memmove.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\memset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\oldexcpt.obj: skipped 0, total 15
.\VS8\VC\crt\src\intel\dll_lib\outp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\p4_memcpy.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\p4_memset.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\dll_lib\pure_obj\managdeh.obj: skipped 0, total 14
.\VS8\VC\crt\src\intel\dll_lib\pure_obj\mehvccctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\pure_obj\mehvcccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\pure_obj\mehvecctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\pure_obj\mehveccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\pure_obj\mehvecdtr.obj: skipped 0, total 3
.\VS8\VC\crt\src\intel\dll_lib\pure_obj\rtti.obj: skipped 0, total 76
.\VS8\VC\crt\src\intel\dll_lib\rtc.lib: skipped 1, total 32
.\VS8\VC\crt\src\intel\dll_lib\sehprolg.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\sehprolg4.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\sehprolg4gs.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\sehsupp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\setjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\setjmp3.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\setjmpex.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strcat.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strcmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strcspn.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strlen.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strncat.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strncpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strnset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strpbrk.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strrchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strrev.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strspn.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\strstr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\tncleanup.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\tran.lib: skipped 1, total 211
.\VS8\VC\crt\src\intel\dll_lib\ulldiv.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ulldvrm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ullrem.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\ullshr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\_memicmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\dll_lib\_strnicm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\alloca16.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\atlssup.obj: skipped 0, total 0
.\VS8\VC\crt\src\intel\mt_lib\calldtor.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\chandler4.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\mt_lib\chandler4gs.obj: skipped 0, total 0
.\VS8\VC\crt\src\intel\mt_lib\chkesp.obj: skipped 2, total 3
.\VS8\VC\crt\src\intel\mt_lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\conv.lib: skipped 2, total 73
.\VS8\VC\crt\src\intel\mt_lib\eh.lib: skipped 7, total 292
.\VS8\VC\crt\src\intel\mt_lib\eh3valid.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\mt_lib\enable.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\exsup.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\exsup2.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\exsup3.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\exsup4.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\inp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\lldiv.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\lldvrm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\llmul.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\llrem.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\llshl.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\llshr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\longjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\matherr.obj: skipped 1, total 1
.\VS8\VC\crt\src\intel\mt_lib\memccpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\memchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\memcmp.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\mt_lib\memcpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\memmove.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\memset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\outp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\p4_memcpy.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\mt_lib\p4_memset.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\mt_lib\rtc.lib: skipped 1, total 32
.\VS8\VC\crt\src\intel\mt_lib\sehprolg.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\sehprolg4.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\sehprolg4gs.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\sehsupp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\setjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\setjmp3.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\setjmpex.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strcat.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strcmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strcspn.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strlen.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strncat.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strncpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strnset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strpbrk.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strrchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strrev.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strspn.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\strstr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\tran.lib: skipped 2, total 210
.\VS8\VC\crt\src\intel\mt_lib\ulldiv.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\ulldvrm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\ullrem.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\ullshr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\_memicmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\mt_lib\_strnicm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\sdknames.lib: skipped 20, total 20
.\VS8\VC\crt\src\intel\tcmap.lib: skipped 74, total 74
.\VS8\VC\crt\src\intel\tcmapdll.lib: skipped 74, total 74
.\VS8\VC\crt\src\intel\xdll_lib\alloca16.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\atlssup.obj: skipped 0, total 0
.\VS8\VC\crt\src\intel\xdll_lib\calldtor.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\chandler4.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\chandler4gs.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\chkesp.obj: skipped 0, total 3
.\VS8\VC\crt\src\intel\xdll_lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\clr_obj\managdeh.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\xdll_lib\clr_obj\mehvccctr.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\clr_obj\mehvcccvb.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\clr_obj\mehvecctr.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\clr_obj\mehveccvb.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\clr_obj\mehvecdtr.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\xdll_lib\clr_obj\mstdexpt.obj: skipped 0, total 60
.\VS8\VC\crt\src\intel\xdll_lib\conv.lib: skipped 0, total 72
.\VS8\VC\crt\src\intel\xdll_lib\cpu_disp.obj: skipped 0, total 3
.\VS8\VC\crt\src\intel\xdll_lib\dllsupp.obj: skipped 0, total 0
.\VS8\VC\crt\src\intel\xdll_lib\eh.lib: skipped 0, total 339
.\VS8\VC\crt\src\intel\xdll_lib\eh3valid.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\ehprolg2.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ehprolg3.obj: skipped 0, total 7
.\VS8\VC\crt\src\intel\xdll_lib\ehprolg3a.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\xdll_lib\ehprolog.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ehvccctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ehvcccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ehvecctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ehveccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ehvecdtr.obj: skipped 0, total 3
.\VS8\VC\crt\src\intel\xdll_lib\enable.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\exsup.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\exsup2.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\exsup3.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\exsup4.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ftol2.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\inp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\lldiv.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\lldvrm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\llmul.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\llrem.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\llshl.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\llshr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\longjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\matherr.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\memccpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\memchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\memcmp.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\xdll_lib\memcpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\memmove.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\memset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\oldexcpt.obj: skipped 0, total 15
.\VS8\VC\crt\src\intel\xdll_lib\outp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\p4_memcpy.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\p4_memset.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xdll_lib\pure_obj\managdeh.obj: skipped 0, total 14
.\VS8\VC\crt\src\intel\xdll_lib\pure_obj\mehvccctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\pure_obj\mehvcccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\pure_obj\mehvecctr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\pure_obj\mehveccvb.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\pure_obj\mehvecdtr.obj: skipped 0, total 3
.\VS8\VC\crt\src\intel\xdll_lib\pure_obj\rtti.obj: skipped 0, total 76
.\VS8\VC\crt\src\intel\xdll_lib\rtc.lib: skipped 0, total 32
.\VS8\VC\crt\src\intel\xdll_lib\sehprolg.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\sehprolg4.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\sehprolg4gs.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\sehsupp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\setjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\setjmp3.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\setjmpex.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strcat.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strcmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strcspn.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strlen.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strncat.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strncpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strnset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strpbrk.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strrchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strrev.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strspn.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\strstr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\tncleanup.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\tran.lib: skipped 0, total 211
.\VS8\VC\crt\src\intel\xdll_lib\ulldiv.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ulldvrm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ullrem.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\ullshr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\_memicmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xdll_lib\_strnicm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\alloca16.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\atlssup.obj: skipped 0, total 0
.\VS8\VC\crt\src\intel\xmt_lib\calldtor.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\chandler4.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xmt_lib\chandler4gs.obj: skipped 0, total 0
.\VS8\VC\crt\src\intel\xmt_lib\chkesp.obj: skipped 0, total 3
.\VS8\VC\crt\src\intel\xmt_lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\conv.lib: skipped 0, total 73
.\VS8\VC\crt\src\intel\xmt_lib\eh.lib: skipped 0, total 293
.\VS8\VC\crt\src\intel\xmt_lib\eh3valid.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xmt_lib\enable.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\exsup.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\exsup2.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\exsup3.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\exsup4.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\inp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\lldiv.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\lldvrm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\llmul.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\llrem.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\llshl.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\llshr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\longjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\matherr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\memccpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\memchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\memcmp.obj: skipped 0, total 6
.\VS8\VC\crt\src\intel\xmt_lib\memcpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\memmove.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\memset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\outp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\p4_memcpy.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xmt_lib\p4_memset.obj: skipped 0, total 2
.\VS8\VC\crt\src\intel\xmt_lib\rtc.lib: skipped 0, total 32
.\VS8\VC\crt\src\intel\xmt_lib\sehprolg.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\sehprolg4.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\sehprolg4gs.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\sehsupp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\setjmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\setjmp3.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\setjmpex.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strcat.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strcmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strcspn.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strlen.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strncat.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strncpy.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strnset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strpbrk.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strrchr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strrev.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strset.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strspn.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\strstr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\tran.lib: skipped 0, total 210
.\VS8\VC\crt\src\intel\xmt_lib\ulldiv.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\ulldvrm.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\ullrem.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\ullshr.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\_memicmp.obj: skipped 0, total 1
.\VS8\VC\crt\src\intel\xmt_lib\_strnicm.obj: skipped 0, total 1
.\VS8\VC\lib\amd64\binmode.obj: skipped 0, total 0
.\VS8\VC\lib\amd64\chkstk.obj: skipped 0, total 1
.\VS8\VC\lib\amd64\commode.obj: skipped 0, total 0
.\VS8\VC\lib\amd64\comsupp.lib: skipped 0, total 23
.\VS8\VC\lib\amd64\comsuppd.lib: skipped 0, total 23
.\VS8\VC\lib\amd64\comsuppw.lib: skipped 0, total 23
.\VS8\VC\lib\amd64\comsuppwd.lib: skipped 0, total 23
.\VS8\VC\lib\amd64\delayimp.lib: skipped 1, total 26
.\VS8\VC\lib\amd64\invalidcontinue.obj: skipped 1, total 2
.\VS8\VC\lib\amd64\libcmt.lib: skipped 281, total 3018
.\VS8\VC\lib\amd64\libcmtd.lib: skipped 122, total 3126
.\VS8\VC\lib\amd64\libcpmt.lib: skipped 262, total 4248
.\VS8\VC\lib\amd64\libcpmtd.lib: skipped 0, total 5149
.\VS8\VC\lib\amd64\loosefpmath.obj: skipped 0, total 2
.\VS8\VC\lib\amd64\msvcmrt.lib: skipped 282, total 498
.\VS8\VC\lib\amd64\msvcmrtd.lib: skipped 291, total 508
.\VS8\VC\lib\amd64\msvcprt.lib: skipped 3180, total 3181
.\VS8\VC\lib\amd64\msvcprtd.lib: skipped 3408, total 3411
.\VS8\VC\lib\amd64\msvcrt.lib: skipped 1661, total 1755
.\VS8\VC\lib\amd64\msvcrtd.lib: skipped 1728, total 1825
.\VS8\VC\lib\amd64\msvcurt.lib: skipped 1827, total 4815
.\VS8\VC\lib\amd64\msvcurtd.lib: skipped 1912, total 5240
.\VS8\VC\lib\amd64\newmode.obj: skipped 0, total 0
.\VS8\VC\lib\amd64\noarg.obj: skipped 4, total 4
.\VS8\VC\lib\amd64\nochkclr.obj: skipped 0, total 0
.\VS8\VC\lib\amd64\noenv.obj: skipped 4, total 4
.\VS8\VC\lib\amd64\nothrownew.obj: skipped 0, total 2
.\VS8\VC\lib\amd64\oldnames.lib: skipped 280, total 280
.\VS8\VC\lib\amd64\pbinmode.obj: skipped 0, total 3
.\VS8\VC\lib\amd64\pcommode.obj: skipped 0, total 1
.\VS8\VC\lib\amd64\pgobootrun.lib: skipped 2, total 2
.\VS8\VC\lib\amd64\pgort.lib: skipped 7, total 13
.\VS8\VC\lib\amd64\pinvalidcontinue.obj: skipped 0, total 6
.\VS8\VC\lib\amd64\pnewmode.obj: skipped 0, total 1
.\VS8\VC\lib\amd64\pnoarg.obj: skipped 0, total 4
.\VS8\VC\lib\amd64\pnoenv.obj: skipped 0, total 6
.\VS8\VC\lib\amd64\pnothrownew.obj: skipped 0, total 4
.\VS8\VC\lib\amd64\psetargv.obj: skipped 0, total 1
.\VS8\VC\lib\amd64\pthreadlocale.obj: skipped 0, total 1
.\VS8\VC\lib\amd64\ptrustm.lib: skipped 0, total 173
.\VS8\VC\lib\amd64\ptrustmd.lib: skipped 0, total 174
.\VS8\VC\lib\amd64\ptrustu.lib: skipped 0, total 91
.\VS8\VC\lib\amd64\ptrustud.lib: skipped 0, total 91
.\VS8\VC\lib\amd64\pwsetargv.obj: skipped 0, total 1
.\VS8\VC\lib\amd64\runtmchk.lib: skipped 0, total 42
.\VS8\VC\lib\amd64\setargv.obj: skipped 0, total 1
.\VS8\VC\lib\amd64\smalheap.obj: skipped 0, total 12
.\VS8\VC\lib\amd64\threadlocale.obj: skipped 0, total 0
.\VS8\VC\lib\amd64\vcomp.lib: skipped 112, total 112
.\VS8\VC\lib\amd64\vcompd.lib: skipped 112, total 112
.\VS8\VC\lib\amd64\wsetargv.obj: skipped 0, total 1
.\VS8\VC\lib\binmode.obj: skipped 0, total 0
.\VS8\VC\lib\chkstk.obj: skipped 0, total 1
.\VS8\VC\lib\commode.obj: skipped 0, total 0
.\VS8\VC\lib\comsupp.lib: skipped 0, total 24
.\VS8\VC\lib\comsuppd.lib: skipped 0, total 24
.\VS8\VC\lib\comsuppw.lib: skipped 0, total 24
.\VS8\VC\lib\comsuppwd.lib: skipped 0, total 24
.\VS8\VC\lib\delayimp.lib: skipped 1, total 26
.\VS8\VC\lib\fp10.obj: skipped 0, total 2
.\VS8\VC\lib\invalidcontinue.obj: skipped 1, total 2
.\VS8\VC\lib\libcmt.lib: skipped 283, total 3056
.\VS8\VC\lib\libcmtd.lib: skipped 121, total 3174
.\VS8\VC\lib\libcpmt.lib: skipped 272, total 4734
.\VS8\VC\lib\libcpmtd.lib: skipped 0, total 5938
.\VS8\VC\lib\loosefpmath.obj: skipped 0, total 2
.\VS8\VC\lib\msvcmrt.lib: skipped 284, total 500
.\VS8\VC\lib\msvcmrtd.lib: skipped 293, total 510
.\VS8\VC\lib\msvcprt.lib: skipped 3172, total 3174
.\VS8\VC\lib\msvcprtd.lib: skipped 3408, total 3411
.\VS8\VC\lib\msvcrt.lib: skipped 1708, total 1835
.\VS8\VC\lib\msvcrtd.lib: skipped 1776, total 1908
.\VS8\VC\lib\msvcurt.lib: skipped 1874, total 4862
.\VS8\VC\lib\msvcurtd.lib: skipped 1962, total 5290
.\VS8\VC\lib\newmode.obj: skipped 0, total 0
.\VS8\VC\lib\noarg.obj: skipped 4, total 4
.\VS8\VC\lib\nochkclr.obj: skipped 1, total 1
.\VS8\VC\lib\noenv.obj: skipped 4, total 4
.\VS8\VC\lib\nothrownew.obj: skipped 0, total 2
.\VS8\VC\lib\oldnames.lib: skipped 280, total 280
.\VS8\VC\lib\opends60.lib: skipped 80, total 80
.\VS8\VC\lib\pbinmode.obj: skipped 0, total 3
.\VS8\VC\lib\pcommode.obj: skipped 0, total 1
.\VS8\VC\lib\pgobootrun.lib: skipped 2, total 2
.\VS8\VC\lib\pgort.lib: skipped 10, total 19
.\VS8\VC\lib\pinvalidcontinue.obj: skipped 0, total 6
.\VS8\VC\lib\pnewmode.obj: skipped 0, total 1
.\VS8\VC\lib\pnoarg.obj: skipped 0, total 4
.\VS8\VC\lib\pnoenv.obj: skipped 0, total 6
.\VS8\VC\lib\pnothrownew.obj: skipped 0, total 4
.\VS8\VC\lib\psetargv.obj: skipped 0, total 1
.\VS8\VC\lib\pthreadlocale.obj: skipped 0, total 1
.\VS8\VC\lib\ptrustm.lib: skipped 0, total 173
.\VS8\VC\lib\ptrustmd.lib: skipped 0, total 174
.\VS8\VC\lib\ptrustu.lib: skipped 0, total 91
.\VS8\VC\lib\ptrustud.lib: skipped 0, total 91
.\VS8\VC\lib\pwsetargv.obj: skipped 0, total 1
.\VS8\VC\lib\RunTmChk.lib: skipped 1, total 52
.\VS8\VC\lib\setargv.obj: skipped 0, total 1
.\VS8\VC\lib\smalheap.obj: skipped 0, total 12
.\VS8\VC\lib\threadlocale.obj: skipped 0, total 0
.\VS8\VC\lib\vcomp.lib: skipped 112, total 112
.\VS8\VC\lib\vcompd.lib: skipped 112, total 112
.\VS8\VC\lib\wsetargv.obj: skipped 0, total 1
```

```
$ find VS8 -name '*.pat' -print0 | tar -czvf VS8/VS8.tar.gz --null -T -
VS8/VC/atlmfc/lib/amd64/atl.lib.pat
VS8/VC/atlmfc/lib/amd64/atldload.lib.pat
VS8/VC/atlmfc/lib/amd64/atlmincrt.lib.pat
VS8/VC/atlmfc/lib/amd64/atls.lib.pat
VS8/VC/atlmfc/lib/amd64/atlsd.lib.pat
VS8/VC/atlmfc/lib/amd64/eafxis.lib.pat
VS8/VC/atlmfc/lib/amd64/eafxisd.lib.pat
VS8/VC/atlmfc/lib/amd64/mfc80.lib.pat
VS8/VC/atlmfc/lib/amd64/mfc80d.lib.pat
VS8/VC/atlmfc/lib/amd64/mfc80u.lib.pat
VS8/VC/atlmfc/lib/amd64/mfc80ud.lib.pat
VS8/VC/atlmfc/lib/amd64/mfcdload.lib.pat
VS8/VC/atlmfc/lib/amd64/MFCM80.lib.pat
VS8/VC/atlmfc/lib/amd64/MFCM80D.lib.pat
VS8/VC/atlmfc/lib/amd64/MFCM80U.lib.pat
VS8/VC/atlmfc/lib/amd64/MFCM80UD.lib.pat
VS8/VC/atlmfc/lib/amd64/mfcs80.lib.pat
VS8/VC/atlmfc/lib/amd64/mfcs80d.lib.pat
VS8/VC/atlmfc/lib/amd64/mfcs80u.lib.pat
VS8/VC/atlmfc/lib/amd64/mfcs80ud.lib.pat
VS8/VC/atlmfc/lib/amd64/nafxcw.lib.pat
VS8/VC/atlmfc/lib/amd64/nafxcwd.lib.pat
VS8/VC/atlmfc/lib/amd64/nafxis.lib.pat
VS8/VC/atlmfc/lib/amd64/nafxisd.lib.pat
VS8/VC/atlmfc/lib/amd64/uafxcw.lib.pat
VS8/VC/atlmfc/lib/amd64/uafxcwd.lib.pat
VS8/VC/atlmfc/lib/Atl.lib.pat
VS8/VC/atlmfc/lib/atldload.lib.pat
VS8/VC/atlmfc/lib/atlmincrt.lib.pat
VS8/VC/atlmfc/lib/atls.lib.pat
VS8/VC/atlmfc/lib/atlsd.lib.pat
VS8/VC/atlmfc/lib/eafxis.lib.pat
VS8/VC/atlmfc/lib/eafxisd.lib.pat
VS8/VC/atlmfc/lib/mfc80.lib.pat
VS8/VC/atlmfc/lib/mfc80d.lib.pat
VS8/VC/atlmfc/lib/mfc80u.lib.pat
VS8/VC/atlmfc/lib/mfc80ud.lib.pat
VS8/VC/atlmfc/lib/mfcdload.lib.pat
VS8/VC/atlmfc/lib/mfcm80.lib.pat
VS8/VC/atlmfc/lib/mfcm80d.lib.pat
VS8/VC/atlmfc/lib/mfcm80u.lib.pat
VS8/VC/atlmfc/lib/mfcm80ud.lib.pat
VS8/VC/atlmfc/lib/mfcs80.lib.pat
VS8/VC/atlmfc/lib/mfcs80d.lib.pat
VS8/VC/atlmfc/lib/mfcs80u.lib.pat
VS8/VC/atlmfc/lib/mfcs80ud.lib.pat
VS8/VC/atlmfc/lib/nafxcw.lib.pat
VS8/VC/atlmfc/lib/nafxcwd.lib.pat
VS8/VC/atlmfc/lib/nafxis.lib.pat
VS8/VC/atlmfc/lib/nafxisd.lib.pat
VS8/VC/atlmfc/lib/uafxcw.lib.pat
VS8/VC/atlmfc/lib/uafxcwd.lib.pat
VS8/VC/crt/src/AMD64/almap.lib.pat
VS8/VC/crt/src/AMD64/almapdll.lib.pat
VS8/VC/crt/src/AMD64/dll_lib/amdsecgs.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/chandler.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/chkstk.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/chkstk2.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/clr_obj/managdeh.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvccctr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvcccvb.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecctr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehveccvb.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecdtr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/clr_obj/mstdexpt.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/conv.lib.pat
VS8/VC/crt/src/AMD64/dll_lib/eh.lib.pat
VS8/VC/crt/src/AMD64/dll_lib/ehvccctr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/ehvcccvb.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/ehvecctr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/ehveccvb.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/ehvecdtr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/gshandler.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/gshandlereh.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/gshandlerseh.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/jmpuwind.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/longjmp.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/matherr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/oldexcpt.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/pure_obj/managdeh.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvccctr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvcccvb.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecctr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehveccvb.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecdtr.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/pure_obj/rtti.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/rtc.lib.pat
VS8/VC/crt/src/AMD64/dll_lib/rtcmd.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/setjmp.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/setjmpex.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/tncleanup.obj.pat
VS8/VC/crt/src/AMD64/dll_lib/tran.lib.pat
VS8/VC/crt/src/AMD64/mt_lib/amdsecgs.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/chandler.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/chkstk.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/chkstk2.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/conv.lib.pat
VS8/VC/crt/src/AMD64/mt_lib/eh.lib.pat
VS8/VC/crt/src/AMD64/mt_lib/gshandler.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/gshandlereh.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/gshandlerseh.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/jmpuwind.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/longjmp.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/matherr.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/rtc.lib.pat
VS8/VC/crt/src/AMD64/mt_lib/rtcmd.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/setjmp.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/setjmpex.obj.pat
VS8/VC/crt/src/AMD64/mt_lib/tran.lib.pat
VS8/VC/crt/src/AMD64/sdknames.lib.pat
VS8/VC/crt/src/AMD64/tcmap.lib.pat
VS8/VC/crt/src/AMD64/tcmapdll.lib.pat
VS8/VC/crt/src/AMD64/xdll_lib/amdsecgs.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/chandler.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/chkstk.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/chkstk2.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/managdeh.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvccctr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvcccvb.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecctr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehveccvb.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecdtr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/clr_obj/mstdexpt.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/conv.lib.pat
VS8/VC/crt/src/AMD64/xdll_lib/eh.lib.pat
VS8/VC/crt/src/AMD64/xdll_lib/ehvccctr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/ehvcccvb.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/ehvecctr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/ehveccvb.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/ehvecdtr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/gshandler.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/gshandlereh.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/gshandlerseh.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/jmpuwind.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/longjmp.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/matherr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/oldexcpt.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/managdeh.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvccctr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvcccvb.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecctr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehveccvb.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecdtr.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/pure_obj/rtti.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/rtc.lib.pat
VS8/VC/crt/src/AMD64/xdll_lib/rtcmd.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/setjmp.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/setjmpex.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/tncleanup.obj.pat
VS8/VC/crt/src/AMD64/xdll_lib/tran.lib.pat
VS8/VC/crt/src/AMD64/xmt_lib/amdsecgs.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/chandler.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/chkstk.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/chkstk2.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/conv.lib.pat
VS8/VC/crt/src/AMD64/xmt_lib/eh.lib.pat
VS8/VC/crt/src/AMD64/xmt_lib/gshandler.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/gshandlereh.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/gshandlerseh.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/jmpuwind.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/longjmp.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/matherr.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/rtc.lib.pat
VS8/VC/crt/src/AMD64/xmt_lib/rtcmd.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/setjmp.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/setjmpex.obj.pat
VS8/VC/crt/src/AMD64/xmt_lib/tran.lib.pat
VS8/VC/crt/src/intel/almap.lib.pat
VS8/VC/crt/src/intel/almapdll.lib.pat
VS8/VC/crt/src/intel/dll_lib/alloca16.obj.pat
VS8/VC/crt/src/intel/dll_lib/atlssup.obj.pat
VS8/VC/crt/src/intel/dll_lib/calldtor.obj.pat
VS8/VC/crt/src/intel/dll_lib/chandler4.obj.pat
VS8/VC/crt/src/intel/dll_lib/chandler4gs.obj.pat
VS8/VC/crt/src/intel/dll_lib/chkesp.obj.pat
VS8/VC/crt/src/intel/dll_lib/chkstk.obj.pat
VS8/VC/crt/src/intel/dll_lib/clr_obj/managdeh.obj.pat
VS8/VC/crt/src/intel/dll_lib/clr_obj/mehvccctr.obj.pat
VS8/VC/crt/src/intel/dll_lib/clr_obj/mehvcccvb.obj.pat
VS8/VC/crt/src/intel/dll_lib/clr_obj/mehvecctr.obj.pat
VS8/VC/crt/src/intel/dll_lib/clr_obj/mehveccvb.obj.pat
VS8/VC/crt/src/intel/dll_lib/clr_obj/mehvecdtr.obj.pat
VS8/VC/crt/src/intel/dll_lib/clr_obj/mstdexpt.obj.pat
VS8/VC/crt/src/intel/dll_lib/conv.lib.pat
VS8/VC/crt/src/intel/dll_lib/cpu_disp.obj.pat
VS8/VC/crt/src/intel/dll_lib/dllsupp.obj.pat
VS8/VC/crt/src/intel/dll_lib/eh.lib.pat
VS8/VC/crt/src/intel/dll_lib/eh3valid.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehprolg2.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehprolg3.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehprolg3a.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehprolog.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehvccctr.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehvcccvb.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehvecctr.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehveccvb.obj.pat
VS8/VC/crt/src/intel/dll_lib/ehvecdtr.obj.pat
VS8/VC/crt/src/intel/dll_lib/enable.obj.pat
VS8/VC/crt/src/intel/dll_lib/exsup.obj.pat
VS8/VC/crt/src/intel/dll_lib/exsup2.obj.pat
VS8/VC/crt/src/intel/dll_lib/exsup3.obj.pat
VS8/VC/crt/src/intel/dll_lib/exsup4.obj.pat
VS8/VC/crt/src/intel/dll_lib/ftol2.obj.pat
VS8/VC/crt/src/intel/dll_lib/inp.obj.pat
VS8/VC/crt/src/intel/dll_lib/lldiv.obj.pat
VS8/VC/crt/src/intel/dll_lib/lldvrm.obj.pat
VS8/VC/crt/src/intel/dll_lib/llmul.obj.pat
VS8/VC/crt/src/intel/dll_lib/llrem.obj.pat
VS8/VC/crt/src/intel/dll_lib/llshl.obj.pat
VS8/VC/crt/src/intel/dll_lib/llshr.obj.pat
VS8/VC/crt/src/intel/dll_lib/longjmp.obj.pat
VS8/VC/crt/src/intel/dll_lib/matherr.obj.pat
VS8/VC/crt/src/intel/dll_lib/memccpy.obj.pat
VS8/VC/crt/src/intel/dll_lib/memchr.obj.pat
VS8/VC/crt/src/intel/dll_lib/memcmp.obj.pat
VS8/VC/crt/src/intel/dll_lib/memcpy.obj.pat
VS8/VC/crt/src/intel/dll_lib/memmove.obj.pat
VS8/VC/crt/src/intel/dll_lib/memset.obj.pat
VS8/VC/crt/src/intel/dll_lib/oldexcpt.obj.pat
VS8/VC/crt/src/intel/dll_lib/outp.obj.pat
VS8/VC/crt/src/intel/dll_lib/p4_memcpy.obj.pat
VS8/VC/crt/src/intel/dll_lib/p4_memset.obj.pat
VS8/VC/crt/src/intel/dll_lib/pure_obj/managdeh.obj.pat
VS8/VC/crt/src/intel/dll_lib/pure_obj/mehvccctr.obj.pat
VS8/VC/crt/src/intel/dll_lib/pure_obj/mehvcccvb.obj.pat
VS8/VC/crt/src/intel/dll_lib/pure_obj/mehvecctr.obj.pat
VS8/VC/crt/src/intel/dll_lib/pure_obj/mehveccvb.obj.pat
VS8/VC/crt/src/intel/dll_lib/pure_obj/mehvecdtr.obj.pat
VS8/VC/crt/src/intel/dll_lib/pure_obj/rtti.obj.pat
VS8/VC/crt/src/intel/dll_lib/rtc.lib.pat
VS8/VC/crt/src/intel/dll_lib/sehprolg.obj.pat
VS8/VC/crt/src/intel/dll_lib/sehprolg4.obj.pat
VS8/VC/crt/src/intel/dll_lib/sehprolg4gs.obj.pat
VS8/VC/crt/src/intel/dll_lib/sehsupp.obj.pat
VS8/VC/crt/src/intel/dll_lib/setjmp.obj.pat
VS8/VC/crt/src/intel/dll_lib/setjmp3.obj.pat
VS8/VC/crt/src/intel/dll_lib/setjmpex.obj.pat
VS8/VC/crt/src/intel/dll_lib/strcat.obj.pat
VS8/VC/crt/src/intel/dll_lib/strchr.obj.pat
VS8/VC/crt/src/intel/dll_lib/strcmp.obj.pat
VS8/VC/crt/src/intel/dll_lib/strcspn.obj.pat
VS8/VC/crt/src/intel/dll_lib/strlen.obj.pat
VS8/VC/crt/src/intel/dll_lib/strncat.obj.pat
VS8/VC/crt/src/intel/dll_lib/strncpy.obj.pat
VS8/VC/crt/src/intel/dll_lib/strnset.obj.pat
VS8/VC/crt/src/intel/dll_lib/strpbrk.obj.pat
VS8/VC/crt/src/intel/dll_lib/strrchr.obj.pat
VS8/VC/crt/src/intel/dll_lib/strrev.obj.pat
VS8/VC/crt/src/intel/dll_lib/strset.obj.pat
VS8/VC/crt/src/intel/dll_lib/strspn.obj.pat
VS8/VC/crt/src/intel/dll_lib/strstr.obj.pat
VS8/VC/crt/src/intel/dll_lib/tncleanup.obj.pat
VS8/VC/crt/src/intel/dll_lib/tran.lib.pat
VS8/VC/crt/src/intel/dll_lib/ulldiv.obj.pat
VS8/VC/crt/src/intel/dll_lib/ulldvrm.obj.pat
VS8/VC/crt/src/intel/dll_lib/ullrem.obj.pat
VS8/VC/crt/src/intel/dll_lib/ullshr.obj.pat
VS8/VC/crt/src/intel/dll_lib/_memicmp.obj.pat
VS8/VC/crt/src/intel/dll_lib/_strnicm.obj.pat
VS8/VC/crt/src/intel/mt_lib/alloca16.obj.pat
VS8/VC/crt/src/intel/mt_lib/atlssup.obj.pat
VS8/VC/crt/src/intel/mt_lib/calldtor.obj.pat
VS8/VC/crt/src/intel/mt_lib/chandler4.obj.pat
VS8/VC/crt/src/intel/mt_lib/chandler4gs.obj.pat
VS8/VC/crt/src/intel/mt_lib/chkesp.obj.pat
VS8/VC/crt/src/intel/mt_lib/chkstk.obj.pat
VS8/VC/crt/src/intel/mt_lib/conv.lib.pat
VS8/VC/crt/src/intel/mt_lib/eh.lib.pat
VS8/VC/crt/src/intel/mt_lib/eh3valid.obj.pat
VS8/VC/crt/src/intel/mt_lib/enable.obj.pat
VS8/VC/crt/src/intel/mt_lib/exsup.obj.pat
VS8/VC/crt/src/intel/mt_lib/exsup2.obj.pat
VS8/VC/crt/src/intel/mt_lib/exsup3.obj.pat
VS8/VC/crt/src/intel/mt_lib/exsup4.obj.pat
VS8/VC/crt/src/intel/mt_lib/inp.obj.pat
VS8/VC/crt/src/intel/mt_lib/lldiv.obj.pat
VS8/VC/crt/src/intel/mt_lib/lldvrm.obj.pat
VS8/VC/crt/src/intel/mt_lib/llmul.obj.pat
VS8/VC/crt/src/intel/mt_lib/llrem.obj.pat
VS8/VC/crt/src/intel/mt_lib/llshl.obj.pat
VS8/VC/crt/src/intel/mt_lib/llshr.obj.pat
VS8/VC/crt/src/intel/mt_lib/longjmp.obj.pat
VS8/VC/crt/src/intel/mt_lib/matherr.obj.pat
VS8/VC/crt/src/intel/mt_lib/memccpy.obj.pat
VS8/VC/crt/src/intel/mt_lib/memchr.obj.pat
VS8/VC/crt/src/intel/mt_lib/memcmp.obj.pat
VS8/VC/crt/src/intel/mt_lib/memcpy.obj.pat
VS8/VC/crt/src/intel/mt_lib/memmove.obj.pat
VS8/VC/crt/src/intel/mt_lib/memset.obj.pat
VS8/VC/crt/src/intel/mt_lib/outp.obj.pat
VS8/VC/crt/src/intel/mt_lib/p4_memcpy.obj.pat
VS8/VC/crt/src/intel/mt_lib/p4_memset.obj.pat
VS8/VC/crt/src/intel/mt_lib/rtc.lib.pat
VS8/VC/crt/src/intel/mt_lib/sehprolg.obj.pat
VS8/VC/crt/src/intel/mt_lib/sehprolg4.obj.pat
VS8/VC/crt/src/intel/mt_lib/sehprolg4gs.obj.pat
VS8/VC/crt/src/intel/mt_lib/sehsupp.obj.pat
VS8/VC/crt/src/intel/mt_lib/setjmp.obj.pat
VS8/VC/crt/src/intel/mt_lib/setjmp3.obj.pat
VS8/VC/crt/src/intel/mt_lib/setjmpex.obj.pat
VS8/VC/crt/src/intel/mt_lib/strcat.obj.pat
VS8/VC/crt/src/intel/mt_lib/strchr.obj.pat
VS8/VC/crt/src/intel/mt_lib/strcmp.obj.pat
VS8/VC/crt/src/intel/mt_lib/strcspn.obj.pat
VS8/VC/crt/src/intel/mt_lib/strlen.obj.pat
VS8/VC/crt/src/intel/mt_lib/strncat.obj.pat
VS8/VC/crt/src/intel/mt_lib/strncpy.obj.pat
VS8/VC/crt/src/intel/mt_lib/strnset.obj.pat
VS8/VC/crt/src/intel/mt_lib/strpbrk.obj.pat
VS8/VC/crt/src/intel/mt_lib/strrchr.obj.pat
VS8/VC/crt/src/intel/mt_lib/strrev.obj.pat
VS8/VC/crt/src/intel/mt_lib/strset.obj.pat
VS8/VC/crt/src/intel/mt_lib/strspn.obj.pat
VS8/VC/crt/src/intel/mt_lib/strstr.obj.pat
VS8/VC/crt/src/intel/mt_lib/tran.lib.pat
VS8/VC/crt/src/intel/mt_lib/ulldiv.obj.pat
VS8/VC/crt/src/intel/mt_lib/ulldvrm.obj.pat
VS8/VC/crt/src/intel/mt_lib/ullrem.obj.pat
VS8/VC/crt/src/intel/mt_lib/ullshr.obj.pat
VS8/VC/crt/src/intel/mt_lib/_memicmp.obj.pat
VS8/VC/crt/src/intel/mt_lib/_strnicm.obj.pat
VS8/VC/crt/src/intel/sdknames.lib.pat
VS8/VC/crt/src/intel/tcmap.lib.pat
VS8/VC/crt/src/intel/tcmapdll.lib.pat
VS8/VC/crt/src/intel/xdll_lib/alloca16.obj.pat
VS8/VC/crt/src/intel/xdll_lib/atlssup.obj.pat
VS8/VC/crt/src/intel/xdll_lib/calldtor.obj.pat
VS8/VC/crt/src/intel/xdll_lib/chandler4.obj.pat
VS8/VC/crt/src/intel/xdll_lib/chandler4gs.obj.pat
VS8/VC/crt/src/intel/xdll_lib/chkesp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/chkstk.obj.pat
VS8/VC/crt/src/intel/xdll_lib/clr_obj/managdeh.obj.pat
VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehvccctr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehvcccvb.obj.pat
VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehvecctr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehveccvb.obj.pat
VS8/VC/crt/src/intel/xdll_lib/clr_obj/mehvecdtr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/clr_obj/mstdexpt.obj.pat
VS8/VC/crt/src/intel/xdll_lib/conv.lib.pat
VS8/VC/crt/src/intel/xdll_lib/cpu_disp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/dllsupp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/eh.lib.pat
VS8/VC/crt/src/intel/xdll_lib/eh3valid.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehprolg2.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehprolg3.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehprolg3a.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehprolog.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehvccctr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehvcccvb.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehvecctr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehveccvb.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ehvecdtr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/enable.obj.pat
VS8/VC/crt/src/intel/xdll_lib/exsup.obj.pat
VS8/VC/crt/src/intel/xdll_lib/exsup2.obj.pat
VS8/VC/crt/src/intel/xdll_lib/exsup3.obj.pat
VS8/VC/crt/src/intel/xdll_lib/exsup4.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ftol2.obj.pat
VS8/VC/crt/src/intel/xdll_lib/inp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/lldiv.obj.pat
VS8/VC/crt/src/intel/xdll_lib/lldvrm.obj.pat
VS8/VC/crt/src/intel/xdll_lib/llmul.obj.pat
VS8/VC/crt/src/intel/xdll_lib/llrem.obj.pat
VS8/VC/crt/src/intel/xdll_lib/llshl.obj.pat
VS8/VC/crt/src/intel/xdll_lib/llshr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/longjmp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/matherr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/memccpy.obj.pat
VS8/VC/crt/src/intel/xdll_lib/memchr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/memcmp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/memcpy.obj.pat
VS8/VC/crt/src/intel/xdll_lib/memmove.obj.pat
VS8/VC/crt/src/intel/xdll_lib/memset.obj.pat
VS8/VC/crt/src/intel/xdll_lib/oldexcpt.obj.pat
VS8/VC/crt/src/intel/xdll_lib/outp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/p4_memcpy.obj.pat
VS8/VC/crt/src/intel/xdll_lib/p4_memset.obj.pat
VS8/VC/crt/src/intel/xdll_lib/pure_obj/managdeh.obj.pat
VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehvccctr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehvcccvb.obj.pat
VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehvecctr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehveccvb.obj.pat
VS8/VC/crt/src/intel/xdll_lib/pure_obj/mehvecdtr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/pure_obj/rtti.obj.pat
VS8/VC/crt/src/intel/xdll_lib/rtc.lib.pat
VS8/VC/crt/src/intel/xdll_lib/sehprolg.obj.pat
VS8/VC/crt/src/intel/xdll_lib/sehprolg4.obj.pat
VS8/VC/crt/src/intel/xdll_lib/sehprolg4gs.obj.pat
VS8/VC/crt/src/intel/xdll_lib/sehsupp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/setjmp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/setjmp3.obj.pat
VS8/VC/crt/src/intel/xdll_lib/setjmpex.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strcat.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strchr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strcmp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strcspn.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strlen.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strncat.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strncpy.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strnset.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strpbrk.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strrchr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strrev.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strset.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strspn.obj.pat
VS8/VC/crt/src/intel/xdll_lib/strstr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/tncleanup.obj.pat
VS8/VC/crt/src/intel/xdll_lib/tran.lib.pat
VS8/VC/crt/src/intel/xdll_lib/ulldiv.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ulldvrm.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ullrem.obj.pat
VS8/VC/crt/src/intel/xdll_lib/ullshr.obj.pat
VS8/VC/crt/src/intel/xdll_lib/_memicmp.obj.pat
VS8/VC/crt/src/intel/xdll_lib/_strnicm.obj.pat
VS8/VC/crt/src/intel/xmt_lib/alloca16.obj.pat
VS8/VC/crt/src/intel/xmt_lib/atlssup.obj.pat
VS8/VC/crt/src/intel/xmt_lib/calldtor.obj.pat
VS8/VC/crt/src/intel/xmt_lib/chandler4.obj.pat
VS8/VC/crt/src/intel/xmt_lib/chandler4gs.obj.pat
VS8/VC/crt/src/intel/xmt_lib/chkesp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/chkstk.obj.pat
VS8/VC/crt/src/intel/xmt_lib/conv.lib.pat
VS8/VC/crt/src/intel/xmt_lib/eh.lib.pat
VS8/VC/crt/src/intel/xmt_lib/eh3valid.obj.pat
VS8/VC/crt/src/intel/xmt_lib/enable.obj.pat
VS8/VC/crt/src/intel/xmt_lib/exsup.obj.pat
VS8/VC/crt/src/intel/xmt_lib/exsup2.obj.pat
VS8/VC/crt/src/intel/xmt_lib/exsup3.obj.pat
VS8/VC/crt/src/intel/xmt_lib/exsup4.obj.pat
VS8/VC/crt/src/intel/xmt_lib/inp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/lldiv.obj.pat
VS8/VC/crt/src/intel/xmt_lib/lldvrm.obj.pat
VS8/VC/crt/src/intel/xmt_lib/llmul.obj.pat
VS8/VC/crt/src/intel/xmt_lib/llrem.obj.pat
VS8/VC/crt/src/intel/xmt_lib/llshl.obj.pat
VS8/VC/crt/src/intel/xmt_lib/llshr.obj.pat
VS8/VC/crt/src/intel/xmt_lib/longjmp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/matherr.obj.pat
VS8/VC/crt/src/intel/xmt_lib/memccpy.obj.pat
VS8/VC/crt/src/intel/xmt_lib/memchr.obj.pat
VS8/VC/crt/src/intel/xmt_lib/memcmp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/memcpy.obj.pat
VS8/VC/crt/src/intel/xmt_lib/memmove.obj.pat
VS8/VC/crt/src/intel/xmt_lib/memset.obj.pat
VS8/VC/crt/src/intel/xmt_lib/outp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/p4_memcpy.obj.pat
VS8/VC/crt/src/intel/xmt_lib/p4_memset.obj.pat
VS8/VC/crt/src/intel/xmt_lib/rtc.lib.pat
VS8/VC/crt/src/intel/xmt_lib/sehprolg.obj.pat
VS8/VC/crt/src/intel/xmt_lib/sehprolg4.obj.pat
VS8/VC/crt/src/intel/xmt_lib/sehprolg4gs.obj.pat
VS8/VC/crt/src/intel/xmt_lib/sehsupp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/setjmp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/setjmp3.obj.pat
VS8/VC/crt/src/intel/xmt_lib/setjmpex.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strcat.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strchr.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strcmp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strcspn.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strlen.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strncat.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strncpy.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strnset.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strpbrk.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strrchr.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strrev.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strset.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strspn.obj.pat
VS8/VC/crt/src/intel/xmt_lib/strstr.obj.pat
VS8/VC/crt/src/intel/xmt_lib/tran.lib.pat
VS8/VC/crt/src/intel/xmt_lib/ulldiv.obj.pat
VS8/VC/crt/src/intel/xmt_lib/ulldvrm.obj.pat
VS8/VC/crt/src/intel/xmt_lib/ullrem.obj.pat
VS8/VC/crt/src/intel/xmt_lib/ullshr.obj.pat
VS8/VC/crt/src/intel/xmt_lib/_memicmp.obj.pat
VS8/VC/crt/src/intel/xmt_lib/_strnicm.obj.pat
VS8/VC/lib/amd64/binmode.obj.pat
VS8/VC/lib/amd64/chkstk.obj.pat
VS8/VC/lib/amd64/commode.obj.pat
VS8/VC/lib/amd64/comsupp.lib.pat
VS8/VC/lib/amd64/comsuppd.lib.pat
VS8/VC/lib/amd64/comsuppw.lib.pat
VS8/VC/lib/amd64/comsuppwd.lib.pat
VS8/VC/lib/amd64/delayimp.lib.pat
VS8/VC/lib/amd64/invalidcontinue.obj.pat
VS8/VC/lib/amd64/libcmt.lib.pat
VS8/VC/lib/amd64/libcmtd.lib.pat
VS8/VC/lib/amd64/libcpmt.lib.pat
VS8/VC/lib/amd64/libcpmtd.lib.pat
VS8/VC/lib/amd64/loosefpmath.obj.pat
VS8/VC/lib/amd64/msvcmrt.lib.pat
VS8/VC/lib/amd64/msvcmrtd.lib.pat
VS8/VC/lib/amd64/msvcprt.lib.pat
VS8/VC/lib/amd64/msvcprtd.lib.pat
VS8/VC/lib/amd64/msvcrt.lib.pat
VS8/VC/lib/amd64/msvcrtd.lib.pat
VS8/VC/lib/amd64/msvcurt.lib.pat
VS8/VC/lib/amd64/msvcurtd.lib.pat
VS8/VC/lib/amd64/newmode.obj.pat
VS8/VC/lib/amd64/noarg.obj.pat
VS8/VC/lib/amd64/nochkclr.obj.pat
VS8/VC/lib/amd64/noenv.obj.pat
VS8/VC/lib/amd64/nothrownew.obj.pat
VS8/VC/lib/amd64/oldnames.lib.pat
VS8/VC/lib/amd64/pbinmode.obj.pat
VS8/VC/lib/amd64/pcommode.obj.pat
VS8/VC/lib/amd64/pgobootrun.lib.pat
VS8/VC/lib/amd64/pgort.lib.pat
VS8/VC/lib/amd64/pinvalidcontinue.obj.pat
VS8/VC/lib/amd64/pnewmode.obj.pat
VS8/VC/lib/amd64/pnoarg.obj.pat
VS8/VC/lib/amd64/pnoenv.obj.pat
VS8/VC/lib/amd64/pnothrownew.obj.pat
VS8/VC/lib/amd64/psetargv.obj.pat
VS8/VC/lib/amd64/pthreadlocale.obj.pat
VS8/VC/lib/amd64/ptrustm.lib.pat
VS8/VC/lib/amd64/ptrustmd.lib.pat
VS8/VC/lib/amd64/ptrustu.lib.pat
VS8/VC/lib/amd64/ptrustud.lib.pat
VS8/VC/lib/amd64/pwsetargv.obj.pat
VS8/VC/lib/amd64/runtmchk.lib.pat
VS8/VC/lib/amd64/setargv.obj.pat
VS8/VC/lib/amd64/smalheap.obj.pat
VS8/VC/lib/amd64/threadlocale.obj.pat
VS8/VC/lib/amd64/vcomp.lib.pat
VS8/VC/lib/amd64/vcompd.lib.pat
VS8/VC/lib/amd64/wsetargv.obj.pat
VS8/VC/lib/binmode.obj.pat
VS8/VC/lib/chkstk.obj.pat
VS8/VC/lib/commode.obj.pat
VS8/VC/lib/comsupp.lib.pat
VS8/VC/lib/comsuppd.lib.pat
VS8/VC/lib/comsuppw.lib.pat
VS8/VC/lib/comsuppwd.lib.pat
VS8/VC/lib/delayimp.lib.pat
VS8/VC/lib/fp10.obj.pat
VS8/VC/lib/invalidcontinue.obj.pat
VS8/VC/lib/libcmt.lib.pat
VS8/VC/lib/libcmtd.lib.pat
VS8/VC/lib/libcpmt.lib.pat
VS8/VC/lib/libcpmtd.lib.pat
VS8/VC/lib/loosefpmath.obj.pat
VS8/VC/lib/msvcmrt.lib.pat
VS8/VC/lib/msvcmrtd.lib.pat
VS8/VC/lib/msvcprt.lib.pat
VS8/VC/lib/msvcprtd.lib.pat
VS8/VC/lib/msvcrt.lib.pat
VS8/VC/lib/msvcrtd.lib.pat
VS8/VC/lib/msvcurt.lib.pat
VS8/VC/lib/msvcurtd.lib.pat
VS8/VC/lib/newmode.obj.pat
VS8/VC/lib/noarg.obj.pat
VS8/VC/lib/nochkclr.obj.pat
VS8/VC/lib/noenv.obj.pat
VS8/VC/lib/nothrownew.obj.pat
VS8/VC/lib/oldnames.lib.pat
VS8/VC/lib/opends60.lib.pat
VS8/VC/lib/pbinmode.obj.pat
VS8/VC/lib/pcommode.obj.pat
VS8/VC/lib/pgobootrun.lib.pat
VS8/VC/lib/pgort.lib.pat
VS8/VC/lib/pinvalidcontinue.obj.pat
VS8/VC/lib/pnewmode.obj.pat
VS8/VC/lib/pnoarg.obj.pat
VS8/VC/lib/pnoenv.obj.pat
VS8/VC/lib/pnothrownew.obj.pat
VS8/VC/lib/psetargv.obj.pat
VS8/VC/lib/pthreadlocale.obj.pat
VS8/VC/lib/ptrustm.lib.pat
VS8/VC/lib/ptrustmd.lib.pat
VS8/VC/lib/ptrustu.lib.pat
VS8/VC/lib/ptrustud.lib.pat
VS8/VC/lib/pwsetargv.obj.pat
VS8/VC/lib/RunTmChk.lib.pat
VS8/VC/lib/setargv.obj.pat
VS8/VC/lib/smalheap.obj.pat
VS8/VC/lib/threadlocale.obj.pat
VS8/VC/lib/vcomp.lib.pat
VS8/VC/lib/vcompd.lib.pat
VS8/VC/lib/wsetargv.obj.pat
```
