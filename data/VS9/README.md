# VS9 / Visual Studio 2008

# download
Visual Studio 2008 Professional Edition
`en_visual_studio_2008_professional_x86_dvd_x14-26326.iso`

# prepare
run setup

# .lib/.obj
```
$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 9.0/VC/ -iname "*.lib"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/atldload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfc90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfc90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfc90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfc90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcdload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/MFCM90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/MFCM90D.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/MFCM90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/MFCM90UD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcs90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcs90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcs90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/mfcs90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/amd64/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/Atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/atldload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfc90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfc90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfc90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfc90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcdload.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcm90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcm90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcm90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcm90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcs90.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcs90d.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcs90u.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/mfcs90ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/nafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/nafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/uafxcw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/atlmfc/lib/uafxcwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/armv4i/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsii_fp/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/mipsiv_fp/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/sh4/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/atl.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/atlosapis.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/atls.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/atlsd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/MFC90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/MFC90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/mfcs90U.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/mfcs90Ud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/UafxcW.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/atlmfc/lib/x86/UafxcWD.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/armv4i/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsii_fp/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/mipsiv_fp/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/sh4/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/ce/lib/x86/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/almap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/almapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/sdknames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/tcmap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/tcmapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/almap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/almapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/sdknames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/tcmap.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/tcmapdll.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/conv.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/eh.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/rtc.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/tran.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/runtmchk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/vcompd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/comsupp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/comsuppd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/comsuppw.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/comsuppwd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/delayimp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/libcmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/libcmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/libcpmt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/libcpmtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcmrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcmrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcprt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcprtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcrt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcrtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcurt.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/msvcurtd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/oldnames.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/opends60.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pgobootrun.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pgort.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/ptrustm.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/ptrustmd.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/ptrustu.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/ptrustud.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/RunTmChk.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/vcomp.lib
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/vcompd.lib


$ find /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 9.0/VC/ -iname "*.obj"
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/dll_lib/unhandld.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/mt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xdll_lib/unhandld.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/amdsecgs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/chandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/chkstk2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/gshandler.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/gshandlereh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/gshandlerseh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/jmpuwind.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/rtcmd.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/AMD64/xmt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/cpu_disp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/dllsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehprolg2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehprolg3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehprolg3a.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehprolog.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ftol2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/unhandld.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/dll_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/mt_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/clr_obj/mstdexpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/cpu_disp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/dllsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehprolg2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehprolg3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehprolg3a.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehprolog.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ftol2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/oldexcpt.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/managdeh.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehvccctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehvcccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehvecctr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehveccvb.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/mehvecdtr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/pure_obj/rtti.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/tncleanup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/unhandld.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xdll_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/alloca16.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/atlssup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/calldtor.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/chandler4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/chandler4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/chkesp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/eh3valid.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/enable.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/exsup.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/exsup2.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/exsup3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/exsup4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/inp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/lldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/lldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/llmul.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/llrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/llshl.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/llshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/longjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/matherr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memccpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memmove.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/outp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/p4_memcpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/p4_memset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/sehprolg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/sehprolg4.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/sehprolg4gs.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/sehsupp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/setjmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/setjmp3.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/setjmpex.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strcat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strcmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strcspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strlen.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strncat.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strncpy.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strnset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strpbrk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strrchr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strrev.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strset.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strspn.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/strstr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/ulldiv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/ulldvrm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/ullrem.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/ullshr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/_memicmp.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/crt/src/intel/xmt_lib/_strnicm.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/nochkclr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/amd64/wsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/binmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/chkstk.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/commode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/fp10.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/invalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/loosefpmath.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/newmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/noarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/nochkclr.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/noenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/nothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pbinmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pcommode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pinvalidcontinue.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pnewmode.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pnoarg.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pnoenv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pnothrownew.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/psetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pthreadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/pwsetargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/setargv.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/smalheap.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/threadlocale.obj
/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/lib/wsetargv.obj


$ rsync -a --prune-empty-dirs --include '*/' --include '*.obj' --include '*.Obj' --include '*.lib' --include '*.Lib' --exclude '*' /cygdrive/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio\ 9.0/VC/ VS9/
```

## manually deleted
- `ce`

```
$ find VS9/ -type f \( -iname "*.lib" -o -iname "*.obj" \) -exec md5sum {} \;
d30b998406494f75f91dee604bd0baf5 *VS9/VC/atlmfc/lib/amd64/atl.lib
e5d487d7545beaebb7d0ed2a92aab743 *VS9/VC/atlmfc/lib/amd64/atldload.lib
92457005cce60fc5f7f0bef64b09370c *VS9/VC/atlmfc/lib/amd64/atls.lib
cd81bde1c5b37d4bb85636d159d1ac3c *VS9/VC/atlmfc/lib/amd64/atlsd.lib
5dc427e35cb6a3d08377ee5e421e5197 *VS9/VC/atlmfc/lib/amd64/mfc90.lib
017a200cf4a21f8070337425740bf22f *VS9/VC/atlmfc/lib/amd64/mfc90d.lib
bc9fbb17ea189571ffa6d6da4d477a80 *VS9/VC/atlmfc/lib/amd64/mfc90u.lib
0405aa368f482d7e37fbdf651cf38b98 *VS9/VC/atlmfc/lib/amd64/mfc90ud.lib
f7a0fc25a15a616d7df277ab27e71580 *VS9/VC/atlmfc/lib/amd64/mfcdload.lib
aa4bce11845080c2f5b043924b20d55a *VS9/VC/atlmfc/lib/amd64/MFCM90.lib
bcda80bf2c1fb7eac506c258d40a62de *VS9/VC/atlmfc/lib/amd64/MFCM90D.lib
5e75a39f0200aa291e8c1dc9621a9838 *VS9/VC/atlmfc/lib/amd64/MFCM90U.lib
ea4b15b43f76fc0458d16c4f5e06b6ac *VS9/VC/atlmfc/lib/amd64/MFCM90UD.lib
634e71b98c8a871b2c8d3ba6bff65a11 *VS9/VC/atlmfc/lib/amd64/mfcs90.lib
f233f6ee6c99be37df08494daad257f4 *VS9/VC/atlmfc/lib/amd64/mfcs90d.lib
66a5cfa7300cfd9c14033e8934aac4a0 *VS9/VC/atlmfc/lib/amd64/mfcs90u.lib
077bb94145b2b44a3f8c1146cf855641 *VS9/VC/atlmfc/lib/amd64/mfcs90ud.lib
e0c8c93d5308fecef10a26cf518ee552 *VS9/VC/atlmfc/lib/amd64/nafxcw.lib
c4ea857ebbcdd63a362051c78df2d950 *VS9/VC/atlmfc/lib/amd64/nafxcwd.lib
22b36de63fc26c11cb0f3672d566c65f *VS9/VC/atlmfc/lib/amd64/uafxcw.lib
4dc0d2d359c95d56eae87f067ca3c020 *VS9/VC/atlmfc/lib/amd64/uafxcwd.lib
57f7f6cf523b940b7efc0b741dfd1fed *VS9/VC/atlmfc/lib/Atl.lib
ada8105f2a89999c1422763fef57bb42 *VS9/VC/atlmfc/lib/atldload.lib
fae8560baf690b8bc28bbcd4110d73b8 *VS9/VC/atlmfc/lib/atls.lib
2d76c22a58e9ad6158c308af36ca3ab8 *VS9/VC/atlmfc/lib/atlsd.lib
de9a64b129e99107e21225beaa998ff7 *VS9/VC/atlmfc/lib/mfc90.lib
09a9fb586a681e68f4afc0f31c9bf876 *VS9/VC/atlmfc/lib/mfc90d.lib
2fc22369c66bc0719b61dab814f581de *VS9/VC/atlmfc/lib/mfc90u.lib
a13dc11ed8df7dae2897b8862281daab *VS9/VC/atlmfc/lib/mfc90ud.lib
edcbcc0ee335b35ed444ea5a5a48e951 *VS9/VC/atlmfc/lib/mfcdload.lib
c1c97a6257941470a26b322025f54b4d *VS9/VC/atlmfc/lib/mfcm90.lib
0df3c44de3db722b345b3989aa90e032 *VS9/VC/atlmfc/lib/mfcm90d.lib
57e203bb2830ef21c6154da9ced2defd *VS9/VC/atlmfc/lib/mfcm90u.lib
ae0dfe06b9194b395f128ff451152e26 *VS9/VC/atlmfc/lib/mfcm90ud.lib
fb6c187e9d82ea804d3e4f292aba39c2 *VS9/VC/atlmfc/lib/mfcs90.lib
17b99f29683e060899c75f5f698d6a10 *VS9/VC/atlmfc/lib/mfcs90d.lib
664c9e0d8fc3ad24ea54a33d08cf94bd *VS9/VC/atlmfc/lib/mfcs90u.lib
96e7c7b61825dfe47d5922a4fe5e0f20 *VS9/VC/atlmfc/lib/mfcs90ud.lib
a9997ecafc217da1f69f1c4a455d88a0 *VS9/VC/atlmfc/lib/nafxcw.lib
0fe3ff8537dd9ca74eebf7b65d4fed49 *VS9/VC/atlmfc/lib/nafxcwd.lib
ce4604ed9f19cefd654577720e7a7e84 *VS9/VC/atlmfc/lib/uafxcw.lib
43cc7645bc699986776527fa0085446b *VS9/VC/atlmfc/lib/uafxcwd.lib
8c06015c45692803d2b4ba74673e4841 *VS9/VC/crt/src/AMD64/almap.lib
1ba614832c0e2ec48a4e94ab32d89eb4 *VS9/VC/crt/src/AMD64/almapdll.lib
0fbe25d4f714ea7a91a77c2286bf481c *VS9/VC/crt/src/AMD64/dll_lib/amdsecgs.obj
2053b5fcacf4ba59302e475c52a7fc9c *VS9/VC/crt/src/AMD64/dll_lib/chandler.obj
8b69d280285bcb93b18f8a7941d4ac47 *VS9/VC/crt/src/AMD64/dll_lib/chkstk.obj
08e1b66852d23b7838ed67103aa1ef88 *VS9/VC/crt/src/AMD64/dll_lib/chkstk2.obj
0dcba726c5cfbeb0d4d514aa1ea25eac *VS9/VC/crt/src/AMD64/dll_lib/clr_obj/managdeh.obj
27c879a834f045b9ed0489a0c4c15310 *VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehvccctr.obj
ae725f082213eafdca30b7f94c8c0165 *VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehvcccvb.obj
7f7eaa133ebd4d35acd2f75f4086cdbd *VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecctr.obj
90510ce98e0addd507c57a7ed846fdf7 *VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehveccvb.obj
59af3abc6be4c6ba84fb85640c43180b *VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecdtr.obj
9b2c0847722ac08724e270a122cc0ebe *VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mstdexpt.obj
8ba8ce21bc4e53c8746b191582c5f82a *VS9/VC/crt/src/AMD64/dll_lib/conv.lib
11b5f8e2a0cad1a477535412e89c7b46 *VS9/VC/crt/src/AMD64/dll_lib/eh.lib
3fae86ac8826644ae14e90d8f4fd7cb9 *VS9/VC/crt/src/AMD64/dll_lib/ehvccctr.obj
304e1b0821be2a9d478b85122fc2a057 *VS9/VC/crt/src/AMD64/dll_lib/ehvcccvb.obj
dc20875314e397740ec68997a1409bda *VS9/VC/crt/src/AMD64/dll_lib/ehvecctr.obj
6e0f0f18e52a0f106766ed8c6f0aa07e *VS9/VC/crt/src/AMD64/dll_lib/ehveccvb.obj
8b4ff0092551d6759d1e2d3ac3ed1d09 *VS9/VC/crt/src/AMD64/dll_lib/ehvecdtr.obj
923ee59ab7fc24467c678c86e7c966b7 *VS9/VC/crt/src/AMD64/dll_lib/gshandler.obj
353f891c7ebfadd2038f2db01f7d894d *VS9/VC/crt/src/AMD64/dll_lib/gshandlereh.obj
1f8d9a95462f936802a893fce34de349 *VS9/VC/crt/src/AMD64/dll_lib/gshandlerseh.obj
32dc81f7561462860b085015c07f7193 *VS9/VC/crt/src/AMD64/dll_lib/jmpuwind.obj
6eb40320526217da00c5f7edbd027dd4 *VS9/VC/crt/src/AMD64/dll_lib/longjmp.obj
b568b4424b75ee3f142db9fe2e234b12 *VS9/VC/crt/src/AMD64/dll_lib/matherr.obj
399aaa0170744598651d420700ba9abc *VS9/VC/crt/src/AMD64/dll_lib/memcpy.obj
a111f406ab33fa78b54bf42c8742b507 *VS9/VC/crt/src/AMD64/dll_lib/oldexcpt.obj
a38f1a0cb7644b1376a9d626908704a7 *VS9/VC/crt/src/AMD64/dll_lib/pure_obj/managdeh.obj
0aee194d219d68d68cfc6df59a10ce2b *VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehvccctr.obj
393995865d6a9fdbd8efe695517ae752 *VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehvcccvb.obj
ad3163524e401cb92cf99580e1f4d895 *VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecctr.obj
51069725858c5547ff2ed02630256c5a *VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehveccvb.obj
5617f03cf93367ea06de0e8d6cb17cb0 *VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecdtr.obj
693e610405ad0b79dc3b6fb5c0a9c744 *VS9/VC/crt/src/AMD64/dll_lib/pure_obj/rtti.obj
f7c2b07c9c9067f3c5021c5b83af134c *VS9/VC/crt/src/AMD64/dll_lib/rtc.lib
59c9622b779f215c205c90996cbdc634 *VS9/VC/crt/src/AMD64/dll_lib/rtcmd.obj
1d018c01c1701542fcbdf804c1e5d910 *VS9/VC/crt/src/AMD64/dll_lib/setjmp.obj
cfbe7e597ed37a57331a8fd0d2227d43 *VS9/VC/crt/src/AMD64/dll_lib/setjmpex.obj
a1c96386732cd784c35b6eb7e89ae30f *VS9/VC/crt/src/AMD64/dll_lib/tncleanup.obj
0c9f60778fb2572859ce7e0c9e302255 *VS9/VC/crt/src/AMD64/dll_lib/tran.lib
ca5bbea478224282e01d822c156c1237 *VS9/VC/crt/src/AMD64/dll_lib/unhandld.obj
0920f6cfbfe4bbd2165a7366a2e828c5 *VS9/VC/crt/src/AMD64/mt_lib/amdsecgs.obj
620ca9b7cdb903723a05f6e0e11c94c8 *VS9/VC/crt/src/AMD64/mt_lib/chandler.obj
a2f9caae763031f9b208ffa2397cac3c *VS9/VC/crt/src/AMD64/mt_lib/chkstk.obj
f725e118f10f662ea510858d619db5c0 *VS9/VC/crt/src/AMD64/mt_lib/chkstk2.obj
de42c97b706ef1194d292540b10748fd *VS9/VC/crt/src/AMD64/mt_lib/conv.lib
f4d0c157dc24355107d43b1fbd7e0a25 *VS9/VC/crt/src/AMD64/mt_lib/eh.lib
fb0844101c86f9f98a2c4ed2f7f27927 *VS9/VC/crt/src/AMD64/mt_lib/gshandler.obj
f07cf1a9194f488e525d53dabbcdc763 *VS9/VC/crt/src/AMD64/mt_lib/gshandlereh.obj
e1149463ecae3cba1a291904af321811 *VS9/VC/crt/src/AMD64/mt_lib/gshandlerseh.obj
ea6cdd6c2ab6cf8726e2a57cf62a89cc *VS9/VC/crt/src/AMD64/mt_lib/jmpuwind.obj
bd05e62a86003a5f8490d2002a83932f *VS9/VC/crt/src/AMD64/mt_lib/longjmp.obj
b606db8aab3297297bb91693e44eed72 *VS9/VC/crt/src/AMD64/mt_lib/matherr.obj
660390a9fb5557f1c4ce116ea352d574 *VS9/VC/crt/src/AMD64/mt_lib/memcpy.obj
a3f5169b7168dd15699866c33f1c0e73 *VS9/VC/crt/src/AMD64/mt_lib/rtc.lib
7e39848992057c98e6b910e506661962 *VS9/VC/crt/src/AMD64/mt_lib/rtcmd.obj
95453dd9fd265307b988b24b0520c707 *VS9/VC/crt/src/AMD64/mt_lib/setjmp.obj
3bf6fabf1331b20fde91b4ee68b0e444 *VS9/VC/crt/src/AMD64/mt_lib/setjmpex.obj
7c9335161ed21a524d8510b9fb56fb2e *VS9/VC/crt/src/AMD64/mt_lib/tran.lib
3092e8f1487588eadaf2fcd9dbee56d0 *VS9/VC/crt/src/AMD64/sdknames.lib
a3f0cd0b2ba63a0580f2c34f25e0ee96 *VS9/VC/crt/src/AMD64/tcmap.lib
351af841bc78b323b5ff360e64c57b6d *VS9/VC/crt/src/AMD64/tcmapdll.lib
f9ed0a665139a1ffea4bc99c187294cd *VS9/VC/crt/src/AMD64/xdll_lib/amdsecgs.obj
3f018de1984dd4e45a6cab957ac5c184 *VS9/VC/crt/src/AMD64/xdll_lib/chandler.obj
9ebb4aa095ed1c737525e79d331a9801 *VS9/VC/crt/src/AMD64/xdll_lib/chkstk.obj
015a753ffa53da5f058b150ffd391b69 *VS9/VC/crt/src/AMD64/xdll_lib/chkstk2.obj
3bceb1d63e0b7213378c1135ca766f6e *VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/managdeh.obj
83b6695ccee3ef467937c5c3a40b0822 *VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvccctr.obj
3250ecf5c879ed0b5768017cd98f5de5 *VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvcccvb.obj
cf218499782121755c0b23e8c91781ac *VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecctr.obj
5df1d75b5baee862430f8b28f47306c9 *VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehveccvb.obj
f62302adcc87e5b8d9858a1d6db62bc5 *VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecdtr.obj
1b2e6e159a93895875ca3f1af588af03 *VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mstdexpt.obj
6aa58245bbee312eef51d73e6bfdcf6b *VS9/VC/crt/src/AMD64/xdll_lib/conv.lib
e241ee5ea7f4d1049895bedfb1ab3ec1 *VS9/VC/crt/src/AMD64/xdll_lib/eh.lib
55da1b2d2d5792310dd42095acbb7ce8 *VS9/VC/crt/src/AMD64/xdll_lib/ehvccctr.obj
b21cbac6bb9225b755d1d867467a5f86 *VS9/VC/crt/src/AMD64/xdll_lib/ehvcccvb.obj
f1fd3b16c03bbe7a8ecd211bf029196e *VS9/VC/crt/src/AMD64/xdll_lib/ehvecctr.obj
c869ea22bdc7d5e9be67067409e60974 *VS9/VC/crt/src/AMD64/xdll_lib/ehveccvb.obj
f7fdeecd868446b10f007182517f1387 *VS9/VC/crt/src/AMD64/xdll_lib/ehvecdtr.obj
9e1701ef68ca070df6041281d11e4f57 *VS9/VC/crt/src/AMD64/xdll_lib/gshandler.obj
cfcc65188b7998dbf2715d84d16da895 *VS9/VC/crt/src/AMD64/xdll_lib/gshandlereh.obj
5b5fbc7b6580db361c83c689580cc407 *VS9/VC/crt/src/AMD64/xdll_lib/gshandlerseh.obj
4a376e72defff090df234d0640666bed *VS9/VC/crt/src/AMD64/xdll_lib/jmpuwind.obj
6592a221469cb3ed2a75ccbb836464ff *VS9/VC/crt/src/AMD64/xdll_lib/longjmp.obj
783d0e419541c624ec015977a2126707 *VS9/VC/crt/src/AMD64/xdll_lib/matherr.obj
afe8fa907d5f5fd3e296cfa6be7c7b2b *VS9/VC/crt/src/AMD64/xdll_lib/memcpy.obj
3eb43818d9e34ebb5a4a5a6f2dc1fc89 *VS9/VC/crt/src/AMD64/xdll_lib/oldexcpt.obj
0ba3c106ec1c530e9bc64194e4c8c9cb *VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/managdeh.obj
0c6df4616c4928e8ffec77866c50a151 *VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvccctr.obj
fc6df081daf1eee3aec5d59b7b5a6db1 *VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvcccvb.obj
01d81e642abb4f6107ca5f5407da2a82 *VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecctr.obj
629f092da2bc67ff4f4974a5dccda181 *VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehveccvb.obj
d97848689f7dfbd33b115ed556ad4290 *VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecdtr.obj
53118433181373c1d4a195cc5c07cf7c *VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/rtti.obj
0dbf21827110b70225cfa4038321e7db *VS9/VC/crt/src/AMD64/xdll_lib/rtc.lib
717d3c050243b40a8d85c0e7cbb102bb *VS9/VC/crt/src/AMD64/xdll_lib/rtcmd.obj
fe0a7a7254d1c0c5963f9a4b57b0e5e7 *VS9/VC/crt/src/AMD64/xdll_lib/setjmp.obj
1f8695137b1441ff2bce6cabf50713c6 *VS9/VC/crt/src/AMD64/xdll_lib/setjmpex.obj
da43b8671edfeba7221019f6e5124e8f *VS9/VC/crt/src/AMD64/xdll_lib/tncleanup.obj
8edc3d6a896aab6f8e046884f47805c3 *VS9/VC/crt/src/AMD64/xdll_lib/tran.lib
23388126e885f6ecd349eb1debb7656e *VS9/VC/crt/src/AMD64/xdll_lib/unhandld.obj
03210e2bf47add64edb817c0b29f94e6 *VS9/VC/crt/src/AMD64/xmt_lib/amdsecgs.obj
4e3504ddaf9a745cf24974cf38db4e4f *VS9/VC/crt/src/AMD64/xmt_lib/chandler.obj
14cfd8cb9092dcb655e045a1d5a0d6b6 *VS9/VC/crt/src/AMD64/xmt_lib/chkstk.obj
ad8cc1a5235bd6203def798fe482df66 *VS9/VC/crt/src/AMD64/xmt_lib/chkstk2.obj
d7a91d91f2b26d545f52d66e48f7b96e *VS9/VC/crt/src/AMD64/xmt_lib/conv.lib
40f01e9644cdfba3c922612805122326 *VS9/VC/crt/src/AMD64/xmt_lib/eh.lib
251d040483b4a1ef9ded3b532bc71cb1 *VS9/VC/crt/src/AMD64/xmt_lib/gshandler.obj
816e5e3732397a27838a26f153c998bc *VS9/VC/crt/src/AMD64/xmt_lib/gshandlereh.obj
b4e6d8b4e658fb836e9629b05b62534f *VS9/VC/crt/src/AMD64/xmt_lib/gshandlerseh.obj
ab4d77537edb665efb664915065f5888 *VS9/VC/crt/src/AMD64/xmt_lib/jmpuwind.obj
bc6cb79fbf30520a10d8ea37180689a0 *VS9/VC/crt/src/AMD64/xmt_lib/longjmp.obj
3f6b9e33c2e1fefa79a8164e837b0e1f *VS9/VC/crt/src/AMD64/xmt_lib/matherr.obj
8d9b507ec60ec9cd2d1637a40bf5a637 *VS9/VC/crt/src/AMD64/xmt_lib/memcpy.obj
c3cb8e442cd633eccd9aee79ffb30565 *VS9/VC/crt/src/AMD64/xmt_lib/rtc.lib
193f638aa8e17c15a13c105591dab80c *VS9/VC/crt/src/AMD64/xmt_lib/rtcmd.obj
39caee113644a434f24fd420796d48a2 *VS9/VC/crt/src/AMD64/xmt_lib/setjmp.obj
779c27eaab231ec5ed4d6fdce8bfa6b1 *VS9/VC/crt/src/AMD64/xmt_lib/setjmpex.obj
44f3e680c84a5392e6e4463713a71585 *VS9/VC/crt/src/AMD64/xmt_lib/tran.lib
dcc7f8e2c8e33181c5fd908666dc189d *VS9/VC/crt/src/intel/almap.lib
34d34aa18b892c64818c8714817b0f0b *VS9/VC/crt/src/intel/almapdll.lib
d760759a7919734e791b33882de7f3c8 *VS9/VC/crt/src/intel/dll_lib/alloca16.obj
eb80b825c136b4e127696448d15dbe51 *VS9/VC/crt/src/intel/dll_lib/atlssup.obj
f06143a3ba67cd00b09935c4ed103f1c *VS9/VC/crt/src/intel/dll_lib/calldtor.obj
bb6b40c85d54b0de33733f1d0424440c *VS9/VC/crt/src/intel/dll_lib/chandler4.obj
7bb24bb2c7e17be1de4da8dc63e38c77 *VS9/VC/crt/src/intel/dll_lib/chandler4gs.obj
04e212214dcfd3bd54bfa123e4e2e7f5 *VS9/VC/crt/src/intel/dll_lib/chkesp.obj
7a40fe75d29150c001f779282986ed82 *VS9/VC/crt/src/intel/dll_lib/chkstk.obj
2dde8b553ed4da05f04f6d4da9e61fbb *VS9/VC/crt/src/intel/dll_lib/clr_obj/managdeh.obj
7a882a8861ee5cf326f2f1d8e5b38f4b *VS9/VC/crt/src/intel/dll_lib/clr_obj/mehvccctr.obj
17707cc08c94e5596713a368344a6216 *VS9/VC/crt/src/intel/dll_lib/clr_obj/mehvcccvb.obj
c61b80d5695221224b240215747635d0 *VS9/VC/crt/src/intel/dll_lib/clr_obj/mehvecctr.obj
51c4c0000c3a2949c102be6da5bbbffb *VS9/VC/crt/src/intel/dll_lib/clr_obj/mehveccvb.obj
7ae1f9ac499ce04ce083da45d67f9ffa *VS9/VC/crt/src/intel/dll_lib/clr_obj/mehvecdtr.obj
87ca03825f39c03610b67c3e55ce177f *VS9/VC/crt/src/intel/dll_lib/clr_obj/mstdexpt.obj
0d650fedabc36796f2a29842c5e0875b *VS9/VC/crt/src/intel/dll_lib/conv.lib
e027df51bdfa9c71b4235a77213465a1 *VS9/VC/crt/src/intel/dll_lib/cpu_disp.obj
c418671835cb2dee56c35c23cdf1367e *VS9/VC/crt/src/intel/dll_lib/dllsupp.obj
d809cb2da15fc6f86ed2ee4418192e25 *VS9/VC/crt/src/intel/dll_lib/eh.lib
fbc54757e157a097b652adcf2c9f63d0 *VS9/VC/crt/src/intel/dll_lib/eh3valid.obj
1dcc4f8219782e25a212f46e0f89c89f *VS9/VC/crt/src/intel/dll_lib/ehprolg2.obj
71d7ddaba882d95a17170973a513e848 *VS9/VC/crt/src/intel/dll_lib/ehprolg3.obj
06cd360b4824ed3d25d098e074ebc746 *VS9/VC/crt/src/intel/dll_lib/ehprolg3a.obj
5bc8a8fc2c28b3db983ceeb107b0e4bb *VS9/VC/crt/src/intel/dll_lib/ehprolog.obj
6f33bb3bf61131ae64d7e4224cfbf1bc *VS9/VC/crt/src/intel/dll_lib/ehvccctr.obj
5d2262849e43186a6a81bca6ca3dcca7 *VS9/VC/crt/src/intel/dll_lib/ehvcccvb.obj
4309407ac550313cc9456270cdeb64ef *VS9/VC/crt/src/intel/dll_lib/ehvecctr.obj
85794b024ae40209b03d84c1dc7cef6d *VS9/VC/crt/src/intel/dll_lib/ehveccvb.obj
773d304b2715047eb72c796f3c58af65 *VS9/VC/crt/src/intel/dll_lib/ehvecdtr.obj
a5adbff27dea57bb3acae42fc8b55886 *VS9/VC/crt/src/intel/dll_lib/enable.obj
fcfe1778cc894cee39b8e75553f4ef8b *VS9/VC/crt/src/intel/dll_lib/exsup.obj
174cab1260dc91bbd219509b5aee01c2 *VS9/VC/crt/src/intel/dll_lib/exsup2.obj
1e99ba7e68920e47432c39b676b27f90 *VS9/VC/crt/src/intel/dll_lib/exsup3.obj
ecc944bf6ec9363caf8a3b11decfbeef *VS9/VC/crt/src/intel/dll_lib/exsup4.obj
362c0e32cc1cd7adf9ff6ff6b7154362 *VS9/VC/crt/src/intel/dll_lib/ftol2.obj
a408b79bbef4653fc5dd056f516a7afd *VS9/VC/crt/src/intel/dll_lib/inp.obj
3fe6cf37800093be930660f3bba42861 *VS9/VC/crt/src/intel/dll_lib/lldiv.obj
1a0a2a8f2bc69f64ab23db2c34f4f055 *VS9/VC/crt/src/intel/dll_lib/lldvrm.obj
1eabbf73f394c420227fc21d936913bd *VS9/VC/crt/src/intel/dll_lib/llmul.obj
9d2f3d820e5463cd082ad379b75337b3 *VS9/VC/crt/src/intel/dll_lib/llrem.obj
7293d4b6456d243ade708c0695443da1 *VS9/VC/crt/src/intel/dll_lib/llshl.obj
fe0124becd0c19c4180800316df086fa *VS9/VC/crt/src/intel/dll_lib/llshr.obj
6a3685366f97d5419a0bdceb792304e4 *VS9/VC/crt/src/intel/dll_lib/longjmp.obj
e0576e16c250c663c83e0983c4913fcb *VS9/VC/crt/src/intel/dll_lib/matherr.obj
b5c89ea2ebdd811f6e9070dae0b28da3 *VS9/VC/crt/src/intel/dll_lib/memccpy.obj
6fc587ed6ec493a970b7e2b167e948a9 *VS9/VC/crt/src/intel/dll_lib/memchr.obj
66000b884331aa95f96956d83cd7cbd6 *VS9/VC/crt/src/intel/dll_lib/memcmp.obj
fe3ab117e82058d6ac0919c0f8e567c4 *VS9/VC/crt/src/intel/dll_lib/memcpy.obj
4dbda71659c4ce612ffd87a4e56617c9 *VS9/VC/crt/src/intel/dll_lib/memmove.obj
dd8ea0ce85e40d72fa0355f67c597753 *VS9/VC/crt/src/intel/dll_lib/memset.obj
fa219954e8e0268fe86add03304a8d76 *VS9/VC/crt/src/intel/dll_lib/oldexcpt.obj
c3efa060ca96315cd5567f1775cdbf8e *VS9/VC/crt/src/intel/dll_lib/outp.obj
6cb722e4393028e6a6b7cd717be3b4e7 *VS9/VC/crt/src/intel/dll_lib/p4_memcpy.obj
5c8625114bfa90e40b2db5381586fac6 *VS9/VC/crt/src/intel/dll_lib/p4_memset.obj
f63a274aa24093522c19acebee616400 *VS9/VC/crt/src/intel/dll_lib/pure_obj/managdeh.obj
5d220955a6346496157ff016b03b5c84 *VS9/VC/crt/src/intel/dll_lib/pure_obj/mehvccctr.obj
568c9ffd7a5a5a6b9b2fea237e7f33c1 *VS9/VC/crt/src/intel/dll_lib/pure_obj/mehvcccvb.obj
ccfa7225650b66b47b725fcb38bf00ff *VS9/VC/crt/src/intel/dll_lib/pure_obj/mehvecctr.obj
bfdb9bb4a16e580cad5963a8a9736a79 *VS9/VC/crt/src/intel/dll_lib/pure_obj/mehveccvb.obj
59ffcf3ac3a41b5c50c2fe90f78db43d *VS9/VC/crt/src/intel/dll_lib/pure_obj/mehvecdtr.obj
a7e5267bf4bc98d4477ed620b6a47a91 *VS9/VC/crt/src/intel/dll_lib/pure_obj/rtti.obj
400d842f24ae44b0dfa34543c75a5719 *VS9/VC/crt/src/intel/dll_lib/rtc.lib
4763235b763cb2bd791a41b47350fa45 *VS9/VC/crt/src/intel/dll_lib/sehprolg.obj
2dfe5d6d3896fd9229aedf539b9717a2 *VS9/VC/crt/src/intel/dll_lib/sehprolg4.obj
e33dba0ed610806b35012264e10a4427 *VS9/VC/crt/src/intel/dll_lib/sehprolg4gs.obj
f27e3f52a52a5acc896df1f63228a64a *VS9/VC/crt/src/intel/dll_lib/sehsupp.obj
49b885ad86da5ae25329dc08f22a255e *VS9/VC/crt/src/intel/dll_lib/setjmp.obj
b01f98bd5f94ff7ea5a4c75f06defd54 *VS9/VC/crt/src/intel/dll_lib/setjmp3.obj
7608862b85d2f2a61d9efb892261827c *VS9/VC/crt/src/intel/dll_lib/setjmpex.obj
e414e74b9ac15fe0e07ac405d431c692 *VS9/VC/crt/src/intel/dll_lib/strcat.obj
c23f72a09462f399ab31ad8d9928cb2e *VS9/VC/crt/src/intel/dll_lib/strchr.obj
75eb69c8a717880b2bad1b1fe2d275aa *VS9/VC/crt/src/intel/dll_lib/strcmp.obj
38ba729fafe6f422b1520758170d07bc *VS9/VC/crt/src/intel/dll_lib/strcspn.obj
d00211b5799f45606dd0525af94dcd0e *VS9/VC/crt/src/intel/dll_lib/strlen.obj
36c69c5dd354a4566a60451711db7ca3 *VS9/VC/crt/src/intel/dll_lib/strncat.obj
7d50826c2f788e520b0ef6844a59e734 *VS9/VC/crt/src/intel/dll_lib/strncpy.obj
9237151f72816a1596d22e4501503c07 *VS9/VC/crt/src/intel/dll_lib/strnset.obj
98edd1fb06bb4692d95a25f4da35b6b5 *VS9/VC/crt/src/intel/dll_lib/strpbrk.obj
fc5da4e434d71afe6cef248758a13021 *VS9/VC/crt/src/intel/dll_lib/strrchr.obj
fe9b6ecbc8cff6aa8bcbfb95f154fac5 *VS9/VC/crt/src/intel/dll_lib/strrev.obj
0b2631f8fc758f696754da3338b4667a *VS9/VC/crt/src/intel/dll_lib/strset.obj
b5ffded591bf518cc3ff06dea18fe18d *VS9/VC/crt/src/intel/dll_lib/strspn.obj
fc1c4b4b622c5f4a01bcb27438d4c2f2 *VS9/VC/crt/src/intel/dll_lib/strstr.obj
a5767a3aca4c5527c2b7522391151afa *VS9/VC/crt/src/intel/dll_lib/tncleanup.obj
47262ae550d05b6feb407dabe9e6ef66 *VS9/VC/crt/src/intel/dll_lib/tran.lib
bbed637c3b7cd79f255850843bc8ffc3 *VS9/VC/crt/src/intel/dll_lib/ulldiv.obj
160ca9b62ef5f46ad71fde82e3f7d36c *VS9/VC/crt/src/intel/dll_lib/ulldvrm.obj
8527d5be7e17e22026f879b0268ed2bd *VS9/VC/crt/src/intel/dll_lib/ullrem.obj
a7a2c2c902b48ab01dedc6307151d4e0 *VS9/VC/crt/src/intel/dll_lib/ullshr.obj
283ff40a1ccee8fbb9fc881505bf35f1 *VS9/VC/crt/src/intel/dll_lib/unhandld.obj
ce4860ffe5b636b5bc8193950d0839bc *VS9/VC/crt/src/intel/dll_lib/_memicmp.obj
a0b2cbb1a28735d49bfec9c68af04efa *VS9/VC/crt/src/intel/dll_lib/_strnicm.obj
a57ac7b7f9613abbb8ac961cc18a15d7 *VS9/VC/crt/src/intel/mt_lib/alloca16.obj
1e3486d86fca30952aa751de4d2172c9 *VS9/VC/crt/src/intel/mt_lib/atlssup.obj
f57448a13aad2e9b2851f0ed5cdda9cd *VS9/VC/crt/src/intel/mt_lib/calldtor.obj
d7802c95ce2ece497547f37a01fb5eca *VS9/VC/crt/src/intel/mt_lib/chandler4.obj
808e9410b6f96563cf7f3a3389b8c005 *VS9/VC/crt/src/intel/mt_lib/chandler4gs.obj
f46cbbf70b0484dc96d7166be0541498 *VS9/VC/crt/src/intel/mt_lib/chkesp.obj
1dfaee9b0053d1a4bcca7e4d3a00000a *VS9/VC/crt/src/intel/mt_lib/chkstk.obj
02923ba841b08243eda33ac0953a801a *VS9/VC/crt/src/intel/mt_lib/conv.lib
4ae368393be257e6093742083b0aa1c9 *VS9/VC/crt/src/intel/mt_lib/eh.lib
59b7cb2df34f7cf5434e411f09929877 *VS9/VC/crt/src/intel/mt_lib/eh3valid.obj
925775548ecabee6516bcaad511235e2 *VS9/VC/crt/src/intel/mt_lib/enable.obj
336d212e660e52519bba6e4764edfffb *VS9/VC/crt/src/intel/mt_lib/exsup.obj
de4c2af0a29a21a0519ac24248c01738 *VS9/VC/crt/src/intel/mt_lib/exsup2.obj
c8358bea83179e09e41f1cfccb31c32a *VS9/VC/crt/src/intel/mt_lib/exsup3.obj
98f684063e835c52f6e60a9a28cebc62 *VS9/VC/crt/src/intel/mt_lib/exsup4.obj
f24fc9680327c6e515be20837ae08dc2 *VS9/VC/crt/src/intel/mt_lib/inp.obj
e575d69df4eeec1b6b535aed59d5b6e3 *VS9/VC/crt/src/intel/mt_lib/lldiv.obj
593af47e47cd66ef90b9bc8a124e47f0 *VS9/VC/crt/src/intel/mt_lib/lldvrm.obj
9409cf6a84aef69fc1966c2bd155dd37 *VS9/VC/crt/src/intel/mt_lib/llmul.obj
63171ef0b98213dc94b3d336e43b9c89 *VS9/VC/crt/src/intel/mt_lib/llrem.obj
fc4751ff822072f50dd594adbfd17252 *VS9/VC/crt/src/intel/mt_lib/llshl.obj
5852c0462ab34c729cd2c610a39bf570 *VS9/VC/crt/src/intel/mt_lib/llshr.obj
9de7649ea4f879d8cd9467fe69a23e29 *VS9/VC/crt/src/intel/mt_lib/longjmp.obj
845201b6e4bf3db82450a667ccfb9a0c *VS9/VC/crt/src/intel/mt_lib/matherr.obj
884657b9b0e721ad0e45e4aeadb2028a *VS9/VC/crt/src/intel/mt_lib/memccpy.obj
1bddf503514b7ca4fd784607a53debf2 *VS9/VC/crt/src/intel/mt_lib/memchr.obj
8c641fe3fcd252d0fda1ee071a57e6ad *VS9/VC/crt/src/intel/mt_lib/memcmp.obj
43b9c6fa90971758dbd519cd5d8f12a9 *VS9/VC/crt/src/intel/mt_lib/memcpy.obj
8bda0fd9511d1fc1027d18fbc8f7ab9f *VS9/VC/crt/src/intel/mt_lib/memmove.obj
2da229d9e3b1dfa39c95886ac21d3d6d *VS9/VC/crt/src/intel/mt_lib/memset.obj
7279f01c638da9068676f6a5d6778271 *VS9/VC/crt/src/intel/mt_lib/outp.obj
e103ddcc6e9d04a22d5fbb1f32b50905 *VS9/VC/crt/src/intel/mt_lib/p4_memcpy.obj
3fe7cc52ffd04935cc29003db6c2e0d5 *VS9/VC/crt/src/intel/mt_lib/p4_memset.obj
00901b917521c48494e1a1510afbd4e2 *VS9/VC/crt/src/intel/mt_lib/rtc.lib
1cb8b7b6dd6921b507e135ba9a7b96b4 *VS9/VC/crt/src/intel/mt_lib/sehprolg.obj
92eefc86ce8b2415ca5a0b0b1117dfc2 *VS9/VC/crt/src/intel/mt_lib/sehprolg4.obj
3122c0a2d82ba5c6d996273e077f7a99 *VS9/VC/crt/src/intel/mt_lib/sehprolg4gs.obj
670af76eb6642a662729b56c9022fd70 *VS9/VC/crt/src/intel/mt_lib/sehsupp.obj
2f08e5b76407a9f89d07b795c890992a *VS9/VC/crt/src/intel/mt_lib/setjmp.obj
d2648c07f3e9bca50218728e1607107d *VS9/VC/crt/src/intel/mt_lib/setjmp3.obj
102bb286cc0e32c968edb807fe3af4f0 *VS9/VC/crt/src/intel/mt_lib/setjmpex.obj
cc71072649059271dcf98695ac673617 *VS9/VC/crt/src/intel/mt_lib/strcat.obj
b48d27f98965db6164e573f9201e900a *VS9/VC/crt/src/intel/mt_lib/strchr.obj
91234bb7041a7b1f51304d57c7fe0a53 *VS9/VC/crt/src/intel/mt_lib/strcmp.obj
d68557e1dd888b161073e90d62c5954f *VS9/VC/crt/src/intel/mt_lib/strcspn.obj
958190a100a19a7c9b4cec1335c3ff6b *VS9/VC/crt/src/intel/mt_lib/strlen.obj
e9ad06e1ac24d85ed9be9d15907fd5e1 *VS9/VC/crt/src/intel/mt_lib/strncat.obj
4ae693b5fbd81e096853173dd652751e *VS9/VC/crt/src/intel/mt_lib/strncpy.obj
a7a61728eb2a8cb069524cc13f6ce417 *VS9/VC/crt/src/intel/mt_lib/strnset.obj
26c3d5509460692256f183152a906b08 *VS9/VC/crt/src/intel/mt_lib/strpbrk.obj
331395bc428f98e3fd1f1f2a4a381766 *VS9/VC/crt/src/intel/mt_lib/strrchr.obj
f36da81a452e98f97e74ffd54421e5bd *VS9/VC/crt/src/intel/mt_lib/strrev.obj
7fa48fa52e489de2e27a973f9fb2d3da *VS9/VC/crt/src/intel/mt_lib/strset.obj
ebb7d99362276cc30e5695952579273e *VS9/VC/crt/src/intel/mt_lib/strspn.obj
6a9f97cb6322f5c5b77ff33a42f9780d *VS9/VC/crt/src/intel/mt_lib/strstr.obj
89035bc8e2ebbbe27fee17c360e50166 *VS9/VC/crt/src/intel/mt_lib/tran.lib
ed53870b4472352e2882ef361387f92c *VS9/VC/crt/src/intel/mt_lib/ulldiv.obj
2c405864614ad63ef598afcd37093a1f *VS9/VC/crt/src/intel/mt_lib/ulldvrm.obj
da5f3c96decee61ff4e1870f415c03be *VS9/VC/crt/src/intel/mt_lib/ullrem.obj
1e6c5b9a0a3fa4a8aa7d384f3737fe47 *VS9/VC/crt/src/intel/mt_lib/ullshr.obj
e1764d482e14604cd363e0200b791b60 *VS9/VC/crt/src/intel/mt_lib/_memicmp.obj
75a13f1a526a908067db4c5bbcfde267 *VS9/VC/crt/src/intel/mt_lib/_strnicm.obj
397a0ea789fa9ec488f163a0df3efd5e *VS9/VC/crt/src/intel/sdknames.lib
e35c8b57a55b0abb244049ed1ffcadf0 *VS9/VC/crt/src/intel/tcmap.lib
c9f2120c31820f174cf5f166370c8181 *VS9/VC/crt/src/intel/tcmapdll.lib
b9363beed10dbb3729291fc43663038f *VS9/VC/crt/src/intel/xdll_lib/alloca16.obj
a1f84360ee6a400c710bf2c2f7fb2511 *VS9/VC/crt/src/intel/xdll_lib/atlssup.obj
ac15e1330c3d9cb5edb6b146ed0fd205 *VS9/VC/crt/src/intel/xdll_lib/calldtor.obj
dc4c40c04c3dfab1827c078a3e5c4196 *VS9/VC/crt/src/intel/xdll_lib/chandler4.obj
dd1a68cb2b71b3f9ef6d06d7f2c62803 *VS9/VC/crt/src/intel/xdll_lib/chandler4gs.obj
3a695b681a930e51e65961376b44aae1 *VS9/VC/crt/src/intel/xdll_lib/chkesp.obj
a40b1c81b055b6c31397e773fe18464d *VS9/VC/crt/src/intel/xdll_lib/chkstk.obj
d932f77c3185f6a9d30fdbb677356039 *VS9/VC/crt/src/intel/xdll_lib/clr_obj/managdeh.obj
6e814dd912663504e4f6a101472a4a95 *VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehvccctr.obj
cc55b1a85d29bdebc2e34925d6a5c07c *VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehvcccvb.obj
159cc9664d175293b826e39b45f589ec *VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehvecctr.obj
6bdac0eec8cfd4b8990fad5d96c3f5d1 *VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehveccvb.obj
46eda31dfd73a0a2d30ac2d2e8418e5c *VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehvecdtr.obj
87f15b6b3b9d1907c2dda49a5981dad8 *VS9/VC/crt/src/intel/xdll_lib/clr_obj/mstdexpt.obj
0391310ccdbe3705ddeda4fb9e753351 *VS9/VC/crt/src/intel/xdll_lib/conv.lib
5423ad3967ecd9187c61b77c9789bc1e *VS9/VC/crt/src/intel/xdll_lib/cpu_disp.obj
01ebe853183fc0aba5a773a384b9f9a4 *VS9/VC/crt/src/intel/xdll_lib/dllsupp.obj
9ed032d3d8b41a55b08f70ccbc8bb392 *VS9/VC/crt/src/intel/xdll_lib/eh.lib
d8f9a10ea16e9424803a37c06b5218f3 *VS9/VC/crt/src/intel/xdll_lib/eh3valid.obj
8208eb72508bdbdc58be76351a5b3d13 *VS9/VC/crt/src/intel/xdll_lib/ehprolg2.obj
a99dde0ea60885bfc47530b96830ca5c *VS9/VC/crt/src/intel/xdll_lib/ehprolg3.obj
0fdcc856dd0b94a064f8fd7b20229466 *VS9/VC/crt/src/intel/xdll_lib/ehprolg3a.obj
0f7db7cd7b0934df62e4a58dcc2aae4f *VS9/VC/crt/src/intel/xdll_lib/ehprolog.obj
17286b2add07669ca9377d79713c2c71 *VS9/VC/crt/src/intel/xdll_lib/ehvccctr.obj
67d04a73a4027ba347eae135027da7c8 *VS9/VC/crt/src/intel/xdll_lib/ehvcccvb.obj
463ea7c33ae5795348d65891787c5bc4 *VS9/VC/crt/src/intel/xdll_lib/ehvecctr.obj
88c40b611c755ce13c6f8fbe1af2218b *VS9/VC/crt/src/intel/xdll_lib/ehveccvb.obj
33b27cc257bff09c7648f8c411ca160a *VS9/VC/crt/src/intel/xdll_lib/ehvecdtr.obj
c04bbd3af2aa2093800085f946de58b8 *VS9/VC/crt/src/intel/xdll_lib/enable.obj
97b45549e34d88a9fdd58efd4b38eb9d *VS9/VC/crt/src/intel/xdll_lib/exsup.obj
481322ee200cb3c8c173be9ed9372f09 *VS9/VC/crt/src/intel/xdll_lib/exsup2.obj
da8d6b72578ef65714a272eec3781355 *VS9/VC/crt/src/intel/xdll_lib/exsup3.obj
6d48750bee4343dcf8dfff3f23b138d3 *VS9/VC/crt/src/intel/xdll_lib/exsup4.obj
72a0e32a1bbd4733414b26008a33d82a *VS9/VC/crt/src/intel/xdll_lib/ftol2.obj
a787dae4344743ce6fafc402912d2873 *VS9/VC/crt/src/intel/xdll_lib/inp.obj
1826f8a32eaab59848fa7faf48f6ab29 *VS9/VC/crt/src/intel/xdll_lib/lldiv.obj
036ca7423e125dbd46838c5e292f9cf4 *VS9/VC/crt/src/intel/xdll_lib/lldvrm.obj
1b44f6d9a9f4c759f08ddec5fdc899cf *VS9/VC/crt/src/intel/xdll_lib/llmul.obj
6a1fff5d0ccd1235e743325cb5b9f0b2 *VS9/VC/crt/src/intel/xdll_lib/llrem.obj
2c4ab26d782cdf4ddad9afb9b3a30e8f *VS9/VC/crt/src/intel/xdll_lib/llshl.obj
2c81a87ee98116a51f530492d07e2b88 *VS9/VC/crt/src/intel/xdll_lib/llshr.obj
87376cdcebe767cc0708f9a9cc3b23eb *VS9/VC/crt/src/intel/xdll_lib/longjmp.obj
c5d77e8ccca9a3b177866cbea815b7e9 *VS9/VC/crt/src/intel/xdll_lib/matherr.obj
1cec9b60c0e4e5b92af0dd8bb75ced13 *VS9/VC/crt/src/intel/xdll_lib/memccpy.obj
8b9349ad60d0de5c8bde7809ed5380e9 *VS9/VC/crt/src/intel/xdll_lib/memchr.obj
995307e18eb2817021c0f93f60fdd508 *VS9/VC/crt/src/intel/xdll_lib/memcmp.obj
b916293222ef46d0d925aeebc300d76e *VS9/VC/crt/src/intel/xdll_lib/memcpy.obj
786cbdd8a4045e532a5481aa997fef6d *VS9/VC/crt/src/intel/xdll_lib/memmove.obj
98b886eb8d51f8f3e13a15d98102a38c *VS9/VC/crt/src/intel/xdll_lib/memset.obj
790d88ff18e0c1e28dbcca190cc908ed *VS9/VC/crt/src/intel/xdll_lib/oldexcpt.obj
5b8d791a957f6a7a6b95b4a66e43988b *VS9/VC/crt/src/intel/xdll_lib/outp.obj
b75d1489bdb009f73d8991e853c3f1af *VS9/VC/crt/src/intel/xdll_lib/p4_memcpy.obj
b56ad9386cb44d81511bfd0e1e5c4f53 *VS9/VC/crt/src/intel/xdll_lib/p4_memset.obj
76e599a94580898a9dd1802256bac2b8 *VS9/VC/crt/src/intel/xdll_lib/pure_obj/managdeh.obj
d6915a5a464ed700bd3d983cccdcea29 *VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehvccctr.obj
3672c0072877e72f405aa70d29b2f2a9 *VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehvcccvb.obj
b57d25f736c8d606bb44c46f607e3103 *VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehvecctr.obj
a21c50411666686f0262ba22e8b7ea96 *VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehveccvb.obj
6b6af5e46413e1d8a021cbe476d8240f *VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehvecdtr.obj
c9c5f800d9a12b457d06aac430686b07 *VS9/VC/crt/src/intel/xdll_lib/pure_obj/rtti.obj
628f48cca6eb5f49dff45ca8a6aaf36a *VS9/VC/crt/src/intel/xdll_lib/rtc.lib
1d87e672e0973e9f2801ef5e9c5f1b21 *VS9/VC/crt/src/intel/xdll_lib/sehprolg.obj
7f72273ccd81fd0317e1a84bcf21cb81 *VS9/VC/crt/src/intel/xdll_lib/sehprolg4.obj
eca16fbcc96416984cad6a293e6488e2 *VS9/VC/crt/src/intel/xdll_lib/sehprolg4gs.obj
8f631c3695b2f4d27224b380d4b8a897 *VS9/VC/crt/src/intel/xdll_lib/sehsupp.obj
ab427a1a9bb02c05fc65a0e153b94759 *VS9/VC/crt/src/intel/xdll_lib/setjmp.obj
f1de1e7311550595d015ced565e34070 *VS9/VC/crt/src/intel/xdll_lib/setjmp3.obj
eb377342bedf919b1e37a4d0c2f1e876 *VS9/VC/crt/src/intel/xdll_lib/setjmpex.obj
b2a9f4b861dda5cbd639b502ee263069 *VS9/VC/crt/src/intel/xdll_lib/strcat.obj
268c47df1f27c94fb64d76cce7ad4c27 *VS9/VC/crt/src/intel/xdll_lib/strchr.obj
3651186b9e8af289e741bb5aa065b9b7 *VS9/VC/crt/src/intel/xdll_lib/strcmp.obj
2dd0efb34afd70c51a5cfbd4303c5061 *VS9/VC/crt/src/intel/xdll_lib/strcspn.obj
4fe2c0f80b088a98a8deeed1e4a1b71e *VS9/VC/crt/src/intel/xdll_lib/strlen.obj
97504d8a0bc167e5ac9051f1767b6c86 *VS9/VC/crt/src/intel/xdll_lib/strncat.obj
94a04dd7b0d6ae4ca74f99db27ac43c1 *VS9/VC/crt/src/intel/xdll_lib/strncpy.obj
1a187f51f9ddde3c9a0a0fae34717e7b *VS9/VC/crt/src/intel/xdll_lib/strnset.obj
fa243937cea2cec9c35d27bd6921e5d8 *VS9/VC/crt/src/intel/xdll_lib/strpbrk.obj
5ed9eb8101ab370bf0cc9f7e5b0ef731 *VS9/VC/crt/src/intel/xdll_lib/strrchr.obj
c6eeb52d8ede04a21bc8747bac8dcae8 *VS9/VC/crt/src/intel/xdll_lib/strrev.obj
86a2619a58e68e4047ba7d0f12c12d62 *VS9/VC/crt/src/intel/xdll_lib/strset.obj
3a131c1ba451c47d510394bb284ee5e6 *VS9/VC/crt/src/intel/xdll_lib/strspn.obj
79add9227a226f6aaaa71f8fef3fe715 *VS9/VC/crt/src/intel/xdll_lib/strstr.obj
7c84d89a3bf3f0f71dd4760077a02ab0 *VS9/VC/crt/src/intel/xdll_lib/tncleanup.obj
f7a6bc66db5b04b39c24af60122d47dc *VS9/VC/crt/src/intel/xdll_lib/tran.lib
8557e5b7162d21d7f2d2a11722c1a58c *VS9/VC/crt/src/intel/xdll_lib/ulldiv.obj
076971e09a7ae71d02d74c573fc61966 *VS9/VC/crt/src/intel/xdll_lib/ulldvrm.obj
85dda466aeb02a3477e92a9702b4463d *VS9/VC/crt/src/intel/xdll_lib/ullrem.obj
df5b83891a31ec21940a62ea887a7c13 *VS9/VC/crt/src/intel/xdll_lib/ullshr.obj
0d770fc94bac9f4dc59ba05627651f52 *VS9/VC/crt/src/intel/xdll_lib/unhandld.obj
49caa46c4a43e4f5e9a5757540798244 *VS9/VC/crt/src/intel/xdll_lib/_memicmp.obj
76ac2ed99dc99c34e6f2e6ee2e159d28 *VS9/VC/crt/src/intel/xdll_lib/_strnicm.obj
710c03b5b81581254d076554b2573e53 *VS9/VC/crt/src/intel/xmt_lib/alloca16.obj
5b7dac2c9a3d61622417efbfab99c396 *VS9/VC/crt/src/intel/xmt_lib/atlssup.obj
362a2a1c102c9b69fb0291249a1bcb85 *VS9/VC/crt/src/intel/xmt_lib/calldtor.obj
5a52191d490bca73c61c8d6bb2a5a8fb *VS9/VC/crt/src/intel/xmt_lib/chandler4.obj
2bc319ca71e891baeae29cf0911ef7da *VS9/VC/crt/src/intel/xmt_lib/chandler4gs.obj
e18a4540d165cdcaf89fc656aaf65f0e *VS9/VC/crt/src/intel/xmt_lib/chkesp.obj
1a525fbe10b3c7907c7d11f9cd6e9e97 *VS9/VC/crt/src/intel/xmt_lib/chkstk.obj
38da0a7a44fae37f85edd8a068f2b279 *VS9/VC/crt/src/intel/xmt_lib/conv.lib
0000bf1cc70fa6037080f6bde96bd3f1 *VS9/VC/crt/src/intel/xmt_lib/eh.lib
b57d95f8e38d1c9580ddfe30a9ea9aa9 *VS9/VC/crt/src/intel/xmt_lib/eh3valid.obj
552d0baa413a36926d540348fb061ee4 *VS9/VC/crt/src/intel/xmt_lib/enable.obj
cafbe8190d65cf5af2fc49ea7fd3d781 *VS9/VC/crt/src/intel/xmt_lib/exsup.obj
ade215097f0796101fd18c091fddc219 *VS9/VC/crt/src/intel/xmt_lib/exsup2.obj
a1ec793d334a295bba219e0f356c7a6c *VS9/VC/crt/src/intel/xmt_lib/exsup3.obj
fbfa43d344e04ba2c6c378dc5bf8a46d *VS9/VC/crt/src/intel/xmt_lib/exsup4.obj
9d3618b828e8d11fdeff8dbf0a1e60d5 *VS9/VC/crt/src/intel/xmt_lib/inp.obj
25f6bd5ff579035ed635b06dc0bbf8eb *VS9/VC/crt/src/intel/xmt_lib/lldiv.obj
15c9eafcc9b6261712e162fd13389f26 *VS9/VC/crt/src/intel/xmt_lib/lldvrm.obj
e8eec0447e2f2f17da1d4efecfb4caf9 *VS9/VC/crt/src/intel/xmt_lib/llmul.obj
362fb26f29f9cc5cbfdb80fc49766902 *VS9/VC/crt/src/intel/xmt_lib/llrem.obj
f162e89bec19495fe4fceef4702e5dda *VS9/VC/crt/src/intel/xmt_lib/llshl.obj
bd4f8a0ad769a797d120b5b7a39cc681 *VS9/VC/crt/src/intel/xmt_lib/llshr.obj
c04210c3bf93ec93df32a8cb189d3fd7 *VS9/VC/crt/src/intel/xmt_lib/longjmp.obj
bd8350f666c4994cc50e0b56aacb4a86 *VS9/VC/crt/src/intel/xmt_lib/matherr.obj
f2d974f634ee9d4b96dcf59a07eb761f *VS9/VC/crt/src/intel/xmt_lib/memccpy.obj
337e116f1b1a9ef707e26dba415e0ef5 *VS9/VC/crt/src/intel/xmt_lib/memchr.obj
276b7d02269c77325090723f4cadb577 *VS9/VC/crt/src/intel/xmt_lib/memcmp.obj
474889e443729a52bc37995fcfa41cb6 *VS9/VC/crt/src/intel/xmt_lib/memcpy.obj
7ee0672a344734096bbc81c838a0ca04 *VS9/VC/crt/src/intel/xmt_lib/memmove.obj
212257ee86e78fbf1330a05c18316200 *VS9/VC/crt/src/intel/xmt_lib/memset.obj
cfeda146c245ae36f17a220a9d8723e7 *VS9/VC/crt/src/intel/xmt_lib/outp.obj
f32c554a515b87fb60a4fe345e300db8 *VS9/VC/crt/src/intel/xmt_lib/p4_memcpy.obj
cddd6b902650e223f42b2996bca5abe6 *VS9/VC/crt/src/intel/xmt_lib/p4_memset.obj
cbd1ac52d5f91f4d3352b8bf08c143f5 *VS9/VC/crt/src/intel/xmt_lib/rtc.lib
e75430013f995d20bde7d25d7d722817 *VS9/VC/crt/src/intel/xmt_lib/sehprolg.obj
081b09c512186dd3460f49bff69c730a *VS9/VC/crt/src/intel/xmt_lib/sehprolg4.obj
6f49e7aed141096c648ae671f3f09515 *VS9/VC/crt/src/intel/xmt_lib/sehprolg4gs.obj
02c0e58527b548d9a6bf3fd88abe1eac *VS9/VC/crt/src/intel/xmt_lib/sehsupp.obj
76b7441319196ff6d7998eedda1a8135 *VS9/VC/crt/src/intel/xmt_lib/setjmp.obj
1ee2fadecd639babeabc32e5eaf7edbe *VS9/VC/crt/src/intel/xmt_lib/setjmp3.obj
82af2dba99f026f361aaa2b3fa0c5cb3 *VS9/VC/crt/src/intel/xmt_lib/setjmpex.obj
6197f5a17e9b13fa3641a4bce8932d86 *VS9/VC/crt/src/intel/xmt_lib/strcat.obj
bb446936aad252e0ede266bfa05af021 *VS9/VC/crt/src/intel/xmt_lib/strchr.obj
14c5af7869f3e6257d93677ebe04cae2 *VS9/VC/crt/src/intel/xmt_lib/strcmp.obj
69988190b968ac19269ff6bf93f1dd4c *VS9/VC/crt/src/intel/xmt_lib/strcspn.obj
b4473cffb89212ad5405c06308bd60fe *VS9/VC/crt/src/intel/xmt_lib/strlen.obj
bff5997a1cb89e3195e2e90fad274e06 *VS9/VC/crt/src/intel/xmt_lib/strncat.obj
4ef7efdbae2444f765c3b573b6d76883 *VS9/VC/crt/src/intel/xmt_lib/strncpy.obj
8727c20a43d5b7fc25d334f26c0042b3 *VS9/VC/crt/src/intel/xmt_lib/strnset.obj
d0ed7f70a9cd548647baea89c7ad0492 *VS9/VC/crt/src/intel/xmt_lib/strpbrk.obj
6de3de77aba9b8247a774f4f8ab4410a *VS9/VC/crt/src/intel/xmt_lib/strrchr.obj
e5561acc4365f501d1c21bfb4fc5621b *VS9/VC/crt/src/intel/xmt_lib/strrev.obj
888a0bb4238803482f41b9961d95100b *VS9/VC/crt/src/intel/xmt_lib/strset.obj
8a70d11a4586e68ba7437f969bf525c5 *VS9/VC/crt/src/intel/xmt_lib/strspn.obj
f05c86a809603c04fd7701dc89d83ce1 *VS9/VC/crt/src/intel/xmt_lib/strstr.obj
d3e8cd577b3e81c84643303fc00939eb *VS9/VC/crt/src/intel/xmt_lib/tran.lib
97d5a75953122de013d9eb0d7eecbaac *VS9/VC/crt/src/intel/xmt_lib/ulldiv.obj
80e65e3a815c13ee34a1420172af9dd2 *VS9/VC/crt/src/intel/xmt_lib/ulldvrm.obj
ac3c29f23b850327a368abb428f6c304 *VS9/VC/crt/src/intel/xmt_lib/ullrem.obj
15f4f9e1f9af23c788d5c2266555e577 *VS9/VC/crt/src/intel/xmt_lib/ullshr.obj
813d5794da638373f4d8766b11804f3a *VS9/VC/crt/src/intel/xmt_lib/_memicmp.obj
3c97ec640390a21c63fdb011e77a30ca *VS9/VC/crt/src/intel/xmt_lib/_strnicm.obj
013e31238f97956b6b0ed56d89020429 *VS9/VC/lib/amd64/binmode.obj
d111663d6d30ba7a7f7e0767c5705cbd *VS9/VC/lib/amd64/chkstk.obj
45ccf0c42c288947fa74ad3aa4dbd86f *VS9/VC/lib/amd64/commode.obj
71e5b795a8382c246555fc32ee490afc *VS9/VC/lib/amd64/comsupp.lib
c30ee29132610797f5ee39eabe45c5c9 *VS9/VC/lib/amd64/comsuppd.lib
955edc65c4c0edf86d440fadcf60d023 *VS9/VC/lib/amd64/comsuppw.lib
8667d65b468a12df1d0cb73748579e44 *VS9/VC/lib/amd64/comsuppwd.lib
ccee1a7391baa6356530e4d571265497 *VS9/VC/lib/amd64/delayimp.lib
51f324ea32b8325648af54d34e2f7a3c *VS9/VC/lib/amd64/invalidcontinue.obj
0af1d9dfe3c508f94060064f4bf738aa *VS9/VC/lib/amd64/libcmt.lib
928d5df1155060ad39bbb787a75c50e0 *VS9/VC/lib/amd64/libcmtd.lib
a348682c533736f0ece2db6a7ad933f1 *VS9/VC/lib/amd64/libcpmt.lib
947b99f514a780e5c28da47221635517 *VS9/VC/lib/amd64/libcpmtd.lib
eb524ebd24063c995e52a3175e5cbb03 *VS9/VC/lib/amd64/loosefpmath.obj
251972ffb7dc9b2d2b908a048cd7da2d *VS9/VC/lib/amd64/msvcmrt.lib
706f336c55a7d06be9b1471e5905330f *VS9/VC/lib/amd64/msvcmrtd.lib
6b7cbcad13f114f3df1b47b001217c03 *VS9/VC/lib/amd64/msvcprt.lib
b8473a900af9362de690f1645961a438 *VS9/VC/lib/amd64/msvcprtd.lib
1dcf85c4890aee05f21e5c5a172d416a *VS9/VC/lib/amd64/msvcrt.lib
f12ea6b8fee8ee555a35edb22f02c87e *VS9/VC/lib/amd64/msvcrtd.lib
3986f9ea774baf0f017303e3a4be0b20 *VS9/VC/lib/amd64/msvcurt.lib
33caec1be5220ab99472b58eed663b60 *VS9/VC/lib/amd64/msvcurtd.lib
641c91a633e7d6ed132212fac3910297 *VS9/VC/lib/amd64/newmode.obj
6c2cda0a15b70492a9e3d921813498aa *VS9/VC/lib/amd64/noarg.obj
47e793412cd2c4f6f3b964244c2c81ca *VS9/VC/lib/amd64/nochkclr.obj
f9b3f61ca15c2f18371616388478c4d4 *VS9/VC/lib/amd64/noenv.obj
da1028ed628a2ebdfecfa9dc94a1856e *VS9/VC/lib/amd64/nothrownew.obj
b26ed24f4b129d945184f49bb6cc9998 *VS9/VC/lib/amd64/oldnames.lib
72c77f5c6cf980bf2cc4042bc4e4e9da *VS9/VC/lib/amd64/pbinmode.obj
60d8a7ae02f70623ca653ee15bf9c2da *VS9/VC/lib/amd64/pcommode.obj
cc0667d2cf027319b1e9bfcb1fc00b67 *VS9/VC/lib/amd64/pgobootrun.lib
1d12bb0d95d77809b1df32a29ea5f3d5 *VS9/VC/lib/amd64/pgort.lib
35eab6b9decfb0b4011c4442d85ce5e1 *VS9/VC/lib/amd64/pinvalidcontinue.obj
268056ee14513175619e9e6b69fb9a1b *VS9/VC/lib/amd64/pnewmode.obj
ff30d0e2094d47ec6a0ba07335b8f67d *VS9/VC/lib/amd64/pnoarg.obj
52da22385fff5b594721d2fe1f498afa *VS9/VC/lib/amd64/pnoenv.obj
7ad4efcbf57766bc663ca9ca9568931a *VS9/VC/lib/amd64/pnothrownew.obj
d787b57ebcaf5b4dc1d506c0f559dca3 *VS9/VC/lib/amd64/psetargv.obj
3e8ea3346816da5645bc97d09516dcea *VS9/VC/lib/amd64/pthreadlocale.obj
b6a564058cd5eae1df1edc07a7f8c10f *VS9/VC/lib/amd64/ptrustm.lib
2594288cfd630ae98bf9bd410e457fe8 *VS9/VC/lib/amd64/ptrustmd.lib
b6a564058cd5eae1df1edc07a7f8c10f *VS9/VC/lib/amd64/ptrustu.lib
2594288cfd630ae98bf9bd410e457fe8 *VS9/VC/lib/amd64/ptrustud.lib
0078cc95311390c9f9e642cf93175a18 *VS9/VC/lib/amd64/pwsetargv.obj
ce36f59f2a72cb3abda8077ee4e406c4 *VS9/VC/lib/amd64/runtmchk.lib
a7745836d89dc0a892158bf96605b699 *VS9/VC/lib/amd64/setargv.obj
54f269316e60c927cb3ed12d582ebe91 *VS9/VC/lib/amd64/smalheap.obj
fff8f722d1056896584744aafd59c70f *VS9/VC/lib/amd64/threadlocale.obj
7104c1786f96ef7f61fe99831b859144 *VS9/VC/lib/amd64/vcomp.lib
e9bdeae4babbd48c1e315844db7923bc *VS9/VC/lib/amd64/vcompd.lib
b1d74c0dc0eb6d3c4e6bfcfa317bd979 *VS9/VC/lib/amd64/wsetargv.obj
f421a92d2324568cbb6321b0c9604a9f *VS9/VC/lib/binmode.obj
1dfaee9b0053d1a4bcca7e4d3a00000a *VS9/VC/lib/chkstk.obj
e87d0cbf4352264f8f3fd2b24bae4b4a *VS9/VC/lib/commode.obj
2f3da72d76e9d3bb3347b014faa77f21 *VS9/VC/lib/comsupp.lib
3510768502ed5bb8c2154a305a2c4ab6 *VS9/VC/lib/comsuppd.lib
677c60190de6c22974bdc6a1200adbcd *VS9/VC/lib/comsuppw.lib
79589771e88f4b6a43c0c71ac165227d *VS9/VC/lib/comsuppwd.lib
28c0e9dbe272b32fc7f63caa972cdf03 *VS9/VC/lib/delayimp.lib
22c7d53f0087ec4d8a231b27b29af844 *VS9/VC/lib/fp10.obj
2e04a03719534b4275ca7769468ba184 *VS9/VC/lib/invalidcontinue.obj
4504ce5c6ed2b431d2dfb694fe369764 *VS9/VC/lib/libcmt.lib
ddb31aee384cafac3f8a2a8f96a24ec0 *VS9/VC/lib/libcmtd.lib
694018acf53223228da7abdda150391a *VS9/VC/lib/libcpmt.lib
7e876a095106916849d2e9b145cc8bd5 *VS9/VC/lib/libcpmtd.lib
14e2b20302cb6d990bd5185d27cb1c00 *VS9/VC/lib/loosefpmath.obj
f2255d37a65bd4f2ab21aacc00f910ae *VS9/VC/lib/msvcmrt.lib
83e6e9987e424926fb7196c0d457e76c *VS9/VC/lib/msvcmrtd.lib
c786e09ed40f90b4d3e4d4783dfc1e32 *VS9/VC/lib/msvcprt.lib
1d6ce2560f171297ee60344bbc198b78 *VS9/VC/lib/msvcprtd.lib
f15b300c823a13d63121e666b2433672 *VS9/VC/lib/msvcrt.lib
f6b8803049df0b827bceead808e68b34 *VS9/VC/lib/msvcrtd.lib
c4c1643aeb554e3480d8fc918454f345 *VS9/VC/lib/msvcurt.lib
cda86607643fc50b66ae11200735dab9 *VS9/VC/lib/msvcurtd.lib
890c1a27e1d31192a9337fd32432ae84 *VS9/VC/lib/newmode.obj
4b096481c8b9bf57c45fb6b5959a54b3 *VS9/VC/lib/noarg.obj
7fdd252a055f8b2a755bbe78e71e88f5 *VS9/VC/lib/nochkclr.obj
0fc9208eb8a9888a03aac2f7c877db77 *VS9/VC/lib/noenv.obj
1f05d3bc334c2d975839e9285bf109ac *VS9/VC/lib/nothrownew.obj
b7d269f67cf43670f705836b48298f06 *VS9/VC/lib/oldnames.lib
947f21d799b02a0091c648fb1cb01c41 *VS9/VC/lib/opends60.lib
87eb34b7b16974eb3e05f3c081ace367 *VS9/VC/lib/pbinmode.obj
c9a519bdef46902b754672f9818f1aef *VS9/VC/lib/pcommode.obj
318c119e6fdadbb88888479f6f04960b *VS9/VC/lib/pgobootrun.lib
43cd416ecc76e1407b10ee2b7d4a0c40 *VS9/VC/lib/pgort.lib
fc9abc565159541e6a034f210debd7d3 *VS9/VC/lib/pinvalidcontinue.obj
36b2e3a83303ccf0fd9385115600e82f *VS9/VC/lib/pnewmode.obj
b1a1cb1eab51bc02a85de188e2f473ba *VS9/VC/lib/pnoarg.obj
0cba6513a59909d5a344c432e6e25115 *VS9/VC/lib/pnoenv.obj
d30f2dab658d5ebcb43e0336bb1baa5f *VS9/VC/lib/pnothrownew.obj
5d82152bb0fcf95722fd539762210e69 *VS9/VC/lib/psetargv.obj
aabcdd9fbc401a8c3edcd79e19d545b3 *VS9/VC/lib/pthreadlocale.obj
194b0a6244bbcda78b7128d31d477656 *VS9/VC/lib/ptrustm.lib
3e07ec99bd9c45fe14717ed27390db86 *VS9/VC/lib/ptrustmd.lib
194b0a6244bbcda78b7128d31d477656 *VS9/VC/lib/ptrustu.lib
3e07ec99bd9c45fe14717ed27390db86 *VS9/VC/lib/ptrustud.lib
23ca46f1dc453bbab570aedf3ee33c6b *VS9/VC/lib/pwsetargv.obj
af93627fec05c99784cd475f127f7fce *VS9/VC/lib/RunTmChk.lib
7ab9fbe91a382ad15d3fdbc0cab6f183 *VS9/VC/lib/setargv.obj
ff41b2aeae1b98b492eeb0f4e9b95da5 *VS9/VC/lib/smalheap.obj
48cc7f73b73634298fa83e2943e5a840 *VS9/VC/lib/threadlocale.obj
d8d5de9343306497416746f05174f700 *VS9/VC/lib/vcomp.lib
ba1464f100661471a15a471c98d61427 *VS9/VC/lib/vcompd.lib
a8efb493577a9407f9d6b19f5a2285e0 *VS9/VC/lib/wsetargv.obj
```

# .pat
```
$ find VS9/ -type f -exec ../../pcf.exe {} {}.pat \;
.\VS9\VC\atlmfc\lib\amd64\atl.lib: skipped 52, total 52
.\VS9\VC\atlmfc\lib\amd64\atldload.lib: skipped 32, total 337
.\VS9\VC\atlmfc\lib\amd64\atls.lib: skipped 20, total 298
.\VS9\VC\atlmfc\lib\amd64\atlsd.lib: skipped 0, total 688
.\VS9\VC\atlmfc\lib\amd64\mfc90.lib: skipped 6720, total 6720
.\VS9\VC\atlmfc\lib\amd64\mfc90d.lib: skipped 9213, total 9213
.\VS9\VC\atlmfc\lib\amd64\mfc90u.lib: skipped 8159, total 8159
.\VS9\VC\atlmfc\lib\amd64\mfc90ud.lib: skipped 11067, total 11067
.\VS9\VC\atlmfc\lib\amd64\mfcdload.lib: skipped 295, total 670
.\VS9\VC\atlmfc\lib\amd64\MFCM90.lib: skipped 25, total 41
.\VS9\VC\atlmfc\lib\amd64\MFCM90D.lib: skipped 31, total 47
.\VS9\VC\atlmfc\lib\amd64\MFCM90U.lib: skipped 27, total 43
.\VS9\VC\atlmfc\lib\amd64\MFCM90UD.lib: skipped 33, total 49
.\VS9\VC\atlmfc\lib\amd64\mfcs90.lib: skipped 10, total 106
.\VS9\VC\atlmfc\lib\amd64\mfcs90d.lib: skipped 0, total 129
.\VS9\VC\atlmfc\lib\amd64\mfcs90u.lib: skipped 10, total 106
.\VS9\VC\atlmfc\lib\amd64\mfcs90ud.lib: skipped 2, total 133
.\VS9\VC\atlmfc\lib\amd64\nafxcw.lib: skipped 1704, total 19322
.\VS9\VC\atlmfc\lib\amd64\nafxcwd.lib: skipped 305, total 19482
.\VS9\VC\atlmfc\lib\amd64\uafxcw.lib: skipped 2629, total 19827
.\VS9\VC\atlmfc\lib\amd64\uafxcwd.lib: skipped 1326, total 20316
.\VS9\VC\atlmfc\lib\Atl.lib: skipped 52, total 52
.\VS9\VC\atlmfc\lib\atldload.lib: skipped 7, total 334
.\VS9\VC\atlmfc\lib\atls.lib: skipped 26, total 1314
.\VS9\VC\atlmfc\lib\atlsd.lib: skipped 0, total 1704
.\VS9\VC\atlmfc\lib\mfc90.lib: skipped 7080, total 7080
.\VS9\VC\atlmfc\lib\mfc90d.lib: skipped 9600, total 9600
.\VS9\VC\atlmfc\lib\mfc90u.lib: skipped 8750, total 8750
.\VS9\VC\atlmfc\lib\mfc90ud.lib: skipped 11685, total 11685
.\VS9\VC\atlmfc\lib\mfcdload.lib: skipped 21, total 669
.\VS9\VC\atlmfc\lib\mfcm90.lib: skipped 25, total 41
.\VS9\VC\atlmfc\lib\mfcm90d.lib: skipped 32, total 48
.\VS9\VC\atlmfc\lib\mfcm90u.lib: skipped 27, total 43
.\VS9\VC\atlmfc\lib\mfcm90ud.lib: skipped 34, total 50
.\VS9\VC\atlmfc\lib\mfcs90.lib: skipped 11, total 103
.\VS9\VC\atlmfc\lib\mfcs90d.lib: skipped 0, total 127
.\VS9\VC\atlmfc\lib\mfcs90u.lib: skipped 11, total 103
.\VS9\VC\atlmfc\lib\mfcs90ud.lib: skipped 2, total 131
.\VS9\VC\atlmfc\lib\nafxcw.lib: skipped 1955, total 20002
.\VS9\VC\atlmfc\lib\nafxcwd.lib: skipped 267, total 20163
.\VS9\VC\atlmfc\lib\uafxcw.lib: skipped 2864, total 20646
.\VS9\VC\atlmfc\lib\uafxcwd.lib: skipped 1398, total 21137
.\VS9\VC\crt\src\AMD64\almap.lib: skipped 46, total 46
.\VS9\VC\crt\src\AMD64\almapdll.lib: skipped 45, total 45
.\VS9\VC\crt\src\AMD64\dll_lib\amdsecgs.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\chandler.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\chkstk2.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\clr_obj\managdeh.obj: skipped 0, total 6
.\VS9\VC\crt\src\AMD64\dll_lib\clr_obj\mehvccctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\clr_obj\mehvcccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\clr_obj\mehvecctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\clr_obj\mehveccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\clr_obj\mehvecdtr.obj: skipped 0, total 6
.\VS9\VC\crt\src\AMD64\dll_lib\clr_obj\mstdexpt.obj: skipped 0, total 60
.\VS9\VC\crt\src\AMD64\dll_lib\conv.lib: skipped 3, total 72
.\VS9\VC\crt\src\AMD64\dll_lib\eh.lib: skipped 4, total 359
.\VS9\VC\crt\src\AMD64\dll_lib\ehvccctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\ehvcccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\ehvecctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\ehveccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\ehvecdtr.obj: skipped 0, total 5
.\VS9\VC\crt\src\AMD64\dll_lib\gshandler.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\gshandlereh.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\gshandlerseh.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\jmpuwind.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\longjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\matherr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\memcpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\oldexcpt.obj: skipped 0, total 15
.\VS9\VC\crt\src\AMD64\dll_lib\pure_obj\managdeh.obj: skipped 0, total 21
.\VS9\VC\crt\src\AMD64\dll_lib\pure_obj\mehvccctr.obj: skipped 0, total 8
.\VS9\VC\crt\src\AMD64\dll_lib\pure_obj\mehvcccvb.obj: skipped 0, total 8
.\VS9\VC\crt\src\AMD64\dll_lib\pure_obj\mehvecctr.obj: skipped 0, total 8
.\VS9\VC\crt\src\AMD64\dll_lib\pure_obj\mehveccvb.obj: skipped 0, total 8
.\VS9\VC\crt\src\AMD64\dll_lib\pure_obj\mehvecdtr.obj: skipped 0, total 10
.\VS9\VC\crt\src\AMD64\dll_lib\pure_obj\rtti.obj: skipped 0, total 83
.\VS9\VC\crt\src\AMD64\dll_lib\rtc.lib: skipped 0, total 31
.\VS9\VC\crt\src\AMD64\dll_lib\rtcmd.obj: skipped 2, total 2
.\VS9\VC\crt\src\AMD64\dll_lib\setjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\setjmpex.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\tncleanup.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\dll_lib\tran.lib: skipped 18, total 300
.\VS9\VC\crt\src\AMD64\dll_lib\unhandld.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\mt_lib\amdsecgs.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\chandler.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\chkstk2.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\conv.lib: skipped 2, total 73
.\VS9\VC\crt\src\AMD64\mt_lib\eh.lib: skipped 4, total 314
.\VS9\VC\crt\src\AMD64\mt_lib\gshandler.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\mt_lib\gshandlereh.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\gshandlerseh.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\jmpuwind.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\longjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\matherr.obj: skipped 1, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\memcpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\rtc.lib: skipped 0, total 31
.\VS9\VC\crt\src\AMD64\mt_lib\rtcmd.obj: skipped 2, total 2
.\VS9\VC\crt\src\AMD64\mt_lib\setjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\setjmpex.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\mt_lib\tran.lib: skipped 19, total 299
.\VS9\VC\crt\src\AMD64\sdknames.lib: skipped 20, total 20
.\VS9\VC\crt\src\AMD64\tcmap.lib: skipped 85, total 85
.\VS9\VC\crt\src\AMD64\tcmapdll.lib: skipped 85, total 85
.\VS9\VC\crt\src\AMD64\xdll_lib\amdsecgs.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\chandler.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\chkstk2.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\clr_obj\managdeh.obj: skipped 0, total 6
.\VS9\VC\crt\src\AMD64\xdll_lib\clr_obj\mehvccctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\clr_obj\mehvcccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\clr_obj\mehvecctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\clr_obj\mehveccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\clr_obj\mehvecdtr.obj: skipped 0, total 6
.\VS9\VC\crt\src\AMD64\xdll_lib\clr_obj\mstdexpt.obj: skipped 0, total 60
.\VS9\VC\crt\src\AMD64\xdll_lib\conv.lib: skipped 1, total 72
.\VS9\VC\crt\src\AMD64\xdll_lib\eh.lib: skipped 0, total 365
.\VS9\VC\crt\src\AMD64\xdll_lib\ehvccctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\ehvcccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\ehvecctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\ehveccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\ehvecdtr.obj: skipped 0, total 5
.\VS9\VC\crt\src\AMD64\xdll_lib\gshandler.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\gshandlereh.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\gshandlerseh.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\jmpuwind.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\longjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\matherr.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\memcpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\oldexcpt.obj: skipped 0, total 15
.\VS9\VC\crt\src\AMD64\xdll_lib\pure_obj\managdeh.obj: skipped 0, total 21
.\VS9\VC\crt\src\AMD64\xdll_lib\pure_obj\mehvccctr.obj: skipped 0, total 8
.\VS9\VC\crt\src\AMD64\xdll_lib\pure_obj\mehvcccvb.obj: skipped 0, total 8
.\VS9\VC\crt\src\AMD64\xdll_lib\pure_obj\mehvecctr.obj: skipped 0, total 8
.\VS9\VC\crt\src\AMD64\xdll_lib\pure_obj\mehveccvb.obj: skipped 0, total 8
.\VS9\VC\crt\src\AMD64\xdll_lib\pure_obj\mehvecdtr.obj: skipped 0, total 10
.\VS9\VC\crt\src\AMD64\xdll_lib\pure_obj\rtti.obj: skipped 0, total 83
.\VS9\VC\crt\src\AMD64\xdll_lib\rtc.lib: skipped 0, total 31
.\VS9\VC\crt\src\AMD64\xdll_lib\rtcmd.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xdll_lib\setjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\setjmpex.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\tncleanup.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xdll_lib\tran.lib: skipped 0, total 300
.\VS9\VC\crt\src\AMD64\xdll_lib\unhandld.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xmt_lib\amdsecgs.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\chandler.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\chkstk2.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\conv.lib: skipped 1, total 73
.\VS9\VC\crt\src\AMD64\xmt_lib\eh.lib: skipped 0, total 320
.\VS9\VC\crt\src\AMD64\xmt_lib\gshandler.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xmt_lib\gshandlereh.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\gshandlerseh.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\jmpuwind.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\longjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\matherr.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\memcpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\rtc.lib: skipped 0, total 31
.\VS9\VC\crt\src\AMD64\xmt_lib\rtcmd.obj: skipped 0, total 2
.\VS9\VC\crt\src\AMD64\xmt_lib\setjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\setjmpex.obj: skipped 0, total 1
.\VS9\VC\crt\src\AMD64\xmt_lib\tran.lib: skipped 0, total 299
.\VS9\VC\crt\src\intel\almap.lib: skipped 47, total 47
.\VS9\VC\crt\src\intel\almapdll.lib: skipped 46, total 46
.\VS9\VC\crt\src\intel\dll_lib\alloca16.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\atlssup.obj: skipped 0, total 0
.\VS9\VC\crt\src\intel\dll_lib\calldtor.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\chandler4.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\chandler4gs.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\chkesp.obj: skipped 2, total 3
.\VS9\VC\crt\src\intel\dll_lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\clr_obj\managdeh.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\dll_lib\clr_obj\mehvccctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\clr_obj\mehvcccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\clr_obj\mehvecctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\clr_obj\mehveccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\clr_obj\mehvecdtr.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\dll_lib\clr_obj\mstdexpt.obj: skipped 0, total 60
.\VS9\VC\crt\src\intel\dll_lib\conv.lib: skipped 2, total 72
.\VS9\VC\crt\src\intel\dll_lib\cpu_disp.obj: skipped 0, total 3
.\VS9\VC\crt\src\intel\dll_lib\dllsupp.obj: skipped 0, total 0
.\VS9\VC\crt\src\intel\dll_lib\eh.lib: skipped 6, total 339
.\VS9\VC\crt\src\intel\dll_lib\eh3valid.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\ehprolg2.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ehprolg3.obj: skipped 0, total 7
.\VS9\VC\crt\src\intel\dll_lib\ehprolg3a.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\dll_lib\ehprolog.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ehvccctr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ehvcccvb.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ehvecctr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ehveccvb.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ehvecdtr.obj: skipped 0, total 3
.\VS9\VC\crt\src\intel\dll_lib\enable.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\exsup.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\exsup2.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\exsup3.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\exsup4.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ftol2.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\inp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\lldiv.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\lldvrm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\llmul.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\llrem.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\llshl.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\llshr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\longjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\matherr.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\memccpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\memchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\memcmp.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\dll_lib\memcpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\memmove.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\memset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\oldexcpt.obj: skipped 0, total 15
.\VS9\VC\crt\src\intel\dll_lib\outp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\p4_memcpy.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\p4_memset.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\pure_obj\managdeh.obj: skipped 0, total 21
.\VS9\VC\crt\src\intel\dll_lib\pure_obj\mehvccctr.obj: skipped 0, total 8
.\VS9\VC\crt\src\intel\dll_lib\pure_obj\mehvcccvb.obj: skipped 0, total 8
.\VS9\VC\crt\src\intel\dll_lib\pure_obj\mehvecctr.obj: skipped 0, total 8
.\VS9\VC\crt\src\intel\dll_lib\pure_obj\mehveccvb.obj: skipped 0, total 8
.\VS9\VC\crt\src\intel\dll_lib\pure_obj\mehvecdtr.obj: skipped 0, total 10
.\VS9\VC\crt\src\intel\dll_lib\pure_obj\rtti.obj: skipped 0, total 83
.\VS9\VC\crt\src\intel\dll_lib\rtc.lib: skipped 1, total 32
.\VS9\VC\crt\src\intel\dll_lib\sehprolg.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\sehprolg4.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\sehprolg4gs.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\sehsupp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\setjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\setjmp3.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\setjmpex.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strcat.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strcmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strcspn.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strlen.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strncat.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strncpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strnset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strpbrk.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strrchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strrev.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strspn.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\strstr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\tncleanup.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\tran.lib: skipped 1, total 225
.\VS9\VC\crt\src\intel\dll_lib\ulldiv.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ulldvrm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ullrem.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\ullshr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\unhandld.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\dll_lib\_memicmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\dll_lib\_strnicm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\alloca16.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\atlssup.obj: skipped 0, total 0
.\VS9\VC\crt\src\intel\mt_lib\calldtor.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\chandler4.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\mt_lib\chandler4gs.obj: skipped 0, total 0
.\VS9\VC\crt\src\intel\mt_lib\chkesp.obj: skipped 2, total 3
.\VS9\VC\crt\src\intel\mt_lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\conv.lib: skipped 2, total 73
.\VS9\VC\crt\src\intel\mt_lib\eh.lib: skipped 6, total 294
.\VS9\VC\crt\src\intel\mt_lib\eh3valid.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\mt_lib\enable.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\exsup.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\exsup2.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\exsup3.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\exsup4.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\inp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\lldiv.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\lldvrm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\llmul.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\llrem.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\llshl.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\llshr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\longjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\matherr.obj: skipped 1, total 1
.\VS9\VC\crt\src\intel\mt_lib\memccpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\memchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\memcmp.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\mt_lib\memcpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\memmove.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\memset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\outp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\p4_memcpy.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\mt_lib\p4_memset.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\mt_lib\rtc.lib: skipped 1, total 32
.\VS9\VC\crt\src\intel\mt_lib\sehprolg.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\sehprolg4.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\sehprolg4gs.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\sehsupp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\setjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\setjmp3.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\setjmpex.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strcat.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strcmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strcspn.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strlen.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strncat.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strncpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strnset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strpbrk.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strrchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strrev.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strspn.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\strstr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\tran.lib: skipped 2, total 224
.\VS9\VC\crt\src\intel\mt_lib\ulldiv.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\ulldvrm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\ullrem.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\ullshr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\_memicmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\mt_lib\_strnicm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\sdknames.lib: skipped 20, total 20
.\VS9\VC\crt\src\intel\tcmap.lib: skipped 85, total 85
.\VS9\VC\crt\src\intel\tcmapdll.lib: skipped 85, total 85
.\VS9\VC\crt\src\intel\xdll_lib\alloca16.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\atlssup.obj: skipped 0, total 0
.\VS9\VC\crt\src\intel\xdll_lib\calldtor.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\chandler4.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\chandler4gs.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\chkesp.obj: skipped 0, total 3
.\VS9\VC\crt\src\intel\xdll_lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\clr_obj\managdeh.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\xdll_lib\clr_obj\mehvccctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\clr_obj\mehvcccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\clr_obj\mehvecctr.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\clr_obj\mehveccvb.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\clr_obj\mehvecdtr.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\xdll_lib\clr_obj\mstdexpt.obj: skipped 0, total 60
.\VS9\VC\crt\src\intel\xdll_lib\conv.lib: skipped 0, total 72
.\VS9\VC\crt\src\intel\xdll_lib\cpu_disp.obj: skipped 0, total 3
.\VS9\VC\crt\src\intel\xdll_lib\dllsupp.obj: skipped 0, total 0
.\VS9\VC\crt\src\intel\xdll_lib\eh.lib: skipped 0, total 341
.\VS9\VC\crt\src\intel\xdll_lib\eh3valid.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\ehprolg2.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ehprolg3.obj: skipped 0, total 7
.\VS9\VC\crt\src\intel\xdll_lib\ehprolg3a.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\xdll_lib\ehprolog.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ehvccctr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ehvcccvb.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ehvecctr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ehveccvb.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ehvecdtr.obj: skipped 0, total 3
.\VS9\VC\crt\src\intel\xdll_lib\enable.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\exsup.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\exsup2.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\exsup3.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\exsup4.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ftol2.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\inp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\lldiv.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\lldvrm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\llmul.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\llrem.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\llshl.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\llshr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\longjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\matherr.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\memccpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\memchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\memcmp.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\xdll_lib\memcpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\memmove.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\memset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\oldexcpt.obj: skipped 0, total 15
.\VS9\VC\crt\src\intel\xdll_lib\outp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\p4_memcpy.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\p4_memset.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\pure_obj\managdeh.obj: skipped 0, total 21
.\VS9\VC\crt\src\intel\xdll_lib\pure_obj\mehvccctr.obj: skipped 0, total 8
.\VS9\VC\crt\src\intel\xdll_lib\pure_obj\mehvcccvb.obj: skipped 0, total 8
.\VS9\VC\crt\src\intel\xdll_lib\pure_obj\mehvecctr.obj: skipped 0, total 8
.\VS9\VC\crt\src\intel\xdll_lib\pure_obj\mehveccvb.obj: skipped 0, total 8
.\VS9\VC\crt\src\intel\xdll_lib\pure_obj\mehvecdtr.obj: skipped 0, total 10
.\VS9\VC\crt\src\intel\xdll_lib\pure_obj\rtti.obj: skipped 0, total 83
.\VS9\VC\crt\src\intel\xdll_lib\rtc.lib: skipped 0, total 32
.\VS9\VC\crt\src\intel\xdll_lib\sehprolg.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\sehprolg4.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\sehprolg4gs.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\sehsupp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\setjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\setjmp3.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\setjmpex.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strcat.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strcmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strcspn.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strlen.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strncat.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strncpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strnset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strpbrk.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strrchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strrev.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strspn.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\strstr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\tncleanup.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\tran.lib: skipped 0, total 225
.\VS9\VC\crt\src\intel\xdll_lib\ulldiv.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ulldvrm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ullrem.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\ullshr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\unhandld.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xdll_lib\_memicmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xdll_lib\_strnicm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\alloca16.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\atlssup.obj: skipped 0, total 0
.\VS9\VC\crt\src\intel\xmt_lib\calldtor.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\chandler4.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xmt_lib\chandler4gs.obj: skipped 0, total 0
.\VS9\VC\crt\src\intel\xmt_lib\chkesp.obj: skipped 0, total 3
.\VS9\VC\crt\src\intel\xmt_lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\conv.lib: skipped 0, total 73
.\VS9\VC\crt\src\intel\xmt_lib\eh.lib: skipped 0, total 296
.\VS9\VC\crt\src\intel\xmt_lib\eh3valid.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xmt_lib\enable.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\exsup.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\exsup2.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\exsup3.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\exsup4.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\inp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\lldiv.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\lldvrm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\llmul.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\llrem.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\llshl.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\llshr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\longjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\matherr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\memccpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\memchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\memcmp.obj: skipped 0, total 6
.\VS9\VC\crt\src\intel\xmt_lib\memcpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\memmove.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\memset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\outp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\p4_memcpy.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xmt_lib\p4_memset.obj: skipped 0, total 2
.\VS9\VC\crt\src\intel\xmt_lib\rtc.lib: skipped 0, total 32
.\VS9\VC\crt\src\intel\xmt_lib\sehprolg.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\sehprolg4.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\sehprolg4gs.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\sehsupp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\setjmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\setjmp3.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\setjmpex.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strcat.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strcmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strcspn.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strlen.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strncat.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strncpy.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strnset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strpbrk.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strrchr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strrev.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strset.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strspn.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\strstr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\tran.lib: skipped 0, total 224
.\VS9\VC\crt\src\intel\xmt_lib\ulldiv.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\ulldvrm.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\ullrem.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\ullshr.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\_memicmp.obj: skipped 0, total 1
.\VS9\VC\crt\src\intel\xmt_lib\_strnicm.obj: skipped 0, total 1
.\VS9\VC\lib\amd64\binmode.obj: skipped 0, total 0
.\VS9\VC\lib\amd64\chkstk.obj: skipped 0, total 1
.\VS9\VC\lib\amd64\commode.obj: skipped 0, total 0
.\VS9\VC\lib\amd64\comsupp.lib: skipped 0, total 26
.\VS9\VC\lib\amd64\comsuppd.lib: skipped 0, total 28
.\VS9\VC\lib\amd64\comsuppw.lib: skipped 0, total 26
.\VS9\VC\lib\amd64\comsuppwd.lib: skipped 0, total 28
.\VS9\VC\lib\amd64\delayimp.lib: skipped 1, total 27
.\VS9\VC\lib\amd64\invalidcontinue.obj: skipped 1, total 2
.\VS9\VC\lib\amd64\libcmt.lib: skipped 310, total 3232
.\VS9\VC\lib\amd64\libcmtd.lib: skipped 133, total 3384
.\VS9\VC\lib\amd64\libcpmt.lib: skipped 294, total 4716
.\VS9\VC\lib\amd64\libcpmtd.lib: skipped 0, total 5737
.\VS9\VC\lib\amd64\loosefpmath.obj: skipped 0, total 2
.\VS9\VC\lib\amd64\msvcmrt.lib: skipped 304, total 576
.\VS9\VC\lib\amd64\msvcmrtd.lib: skipped 313, total 596
.\VS9\VC\lib\amd64\msvcprt.lib: skipped 3182, total 3189
.\VS9\VC\lib\amd64\msvcprtd.lib: skipped 3413, total 3425
.\VS9\VC\lib\amd64\msvcrt.lib: skipped 1677, total 1787
.\VS9\VC\lib\amd64\msvcrtd.lib: skipped 1740, total 1853
.\VS9\VC\lib\amd64\msvcurt.lib: skipped 1776, total 8905
.\VS9\VC\lib\amd64\msvcurtd.lib: skipped 1855, total 9640
.\VS9\VC\lib\amd64\newmode.obj: skipped 0, total 0
.\VS9\VC\lib\amd64\noarg.obj: skipped 4, total 4
.\VS9\VC\lib\amd64\nochkclr.obj: skipped 0, total 0
.\VS9\VC\lib\amd64\noenv.obj: skipped 4, total 4
.\VS9\VC\lib\amd64\nothrownew.obj: skipped 0, total 4
.\VS9\VC\lib\amd64\oldnames.lib: skipped 280, total 280
.\VS9\VC\lib\amd64\pbinmode.obj: skipped 0, total 10
.\VS9\VC\lib\amd64\pcommode.obj: skipped 0, total 8
.\VS9\VC\lib\amd64\pgobootrun.lib: skipped 2, total 2
.\VS9\VC\lib\amd64\pgort.lib: skipped 7, total 13
.\VS9\VC\lib\amd64\pinvalidcontinue.obj: skipped 0, total 13
.\VS9\VC\lib\amd64\pnewmode.obj: skipped 0, total 8
.\VS9\VC\lib\amd64\pnoarg.obj: skipped 0, total 11
.\VS9\VC\lib\amd64\pnoenv.obj: skipped 0, total 13
.\VS9\VC\lib\amd64\pnothrownew.obj: skipped 0, total 13
.\VS9\VC\lib\amd64\psetargv.obj: skipped 0, total 8
.\VS9\VC\lib\amd64\pthreadlocale.obj: skipped 0, total 1
.\VS9\VC\lib\amd64\ptrustm.lib: skipped 0, total 173
.\VS9\VC\lib\amd64\ptrustmd.lib: skipped 0, total 174
.\VS9\VC\lib\amd64\ptrustu.lib: skipped 0, total 173
.\VS9\VC\lib\amd64\ptrustud.lib: skipped 0, total 174
.\VS9\VC\lib\amd64\pwsetargv.obj: skipped 0, total 8
.\VS9\VC\lib\amd64\runtmchk.lib: skipped 0, total 43
.\VS9\VC\lib\amd64\setargv.obj: skipped 0, total 1
.\VS9\VC\lib\amd64\smalheap.obj: skipped 0, total 12
.\VS9\VC\lib\amd64\threadlocale.obj: skipped 0, total 0
.\VS9\VC\lib\amd64\vcomp.lib: skipped 112, total 112
.\VS9\VC\lib\amd64\vcompd.lib: skipped 112, total 112
.\VS9\VC\lib\amd64\wsetargv.obj: skipped 0, total 1
.\VS9\VC\lib\binmode.obj: skipped 0, total 0
.\VS9\VC\lib\chkstk.obj: skipped 0, total 1
.\VS9\VC\lib\commode.obj: skipped 0, total 0
.\VS9\VC\lib\comsupp.lib: skipped 0, total 26
.\VS9\VC\lib\comsuppd.lib: skipped 0, total 26
.\VS9\VC\lib\comsuppw.lib: skipped 0, total 26
.\VS9\VC\lib\comsuppwd.lib: skipped 0, total 26
.\VS9\VC\lib\delayimp.lib: skipped 1, total 27
.\VS9\VC\lib\fp10.obj: skipped 0, total 2
.\VS9\VC\lib\invalidcontinue.obj: skipped 1, total 2
.\VS9\VC\lib\libcmt.lib: skipped 294, total 3038
.\VS9\VC\lib\libcmtd.lib: skipped 132, total 3164
.\VS9\VC\lib\libcpmt.lib: skipped 262, total 4648
.\VS9\VC\lib\libcpmtd.lib: skipped 0, total 5784
.\VS9\VC\lib\loosefpmath.obj: skipped 0, total 2
.\VS9\VC\lib\msvcmrt.lib: skipped 306, total 578
.\VS9\VC\lib\msvcmrtd.lib: skipped 315, total 598
.\VS9\VC\lib\msvcprt.lib: skipped 3174, total 3182
.\VS9\VC\lib\msvcprtd.lib: skipped 3417, total 3429
.\VS9\VC\lib\msvcrt.lib: skipped 1724, total 1853
.\VS9\VC\lib\msvcrtd.lib: skipped 1788, total 1922
.\VS9\VC\lib\msvcurt.lib: skipped 1823, total 8951
.\VS9\VC\lib\msvcurtd.lib: skipped 1905, total 9703
.\VS9\VC\lib\newmode.obj: skipped 0, total 0
.\VS9\VC\lib\noarg.obj: skipped 4, total 4
.\VS9\VC\lib\nochkclr.obj: skipped 1, total 1
.\VS9\VC\lib\noenv.obj: skipped 4, total 4
.\VS9\VC\lib\nothrownew.obj: skipped 0, total 4
.\VS9\VC\lib\oldnames.lib: skipped 280, total 280
.\VS9\VC\lib\opends60.lib: skipped 80, total 80
.\VS9\VC\lib\pbinmode.obj: skipped 0, total 10
.\VS9\VC\lib\pcommode.obj: skipped 0, total 8
.\VS9\VC\lib\pgobootrun.lib: skipped 2, total 2
.\VS9\VC\lib\pgort.lib: skipped 10, total 21
.\VS9\VC\lib\pinvalidcontinue.obj: skipped 0, total 13
.\VS9\VC\lib\pnewmode.obj: skipped 0, total 8
.\VS9\VC\lib\pnoarg.obj: skipped 0, total 11
.\VS9\VC\lib\pnoenv.obj: skipped 0, total 13
.\VS9\VC\lib\pnothrownew.obj: skipped 0, total 13
.\VS9\VC\lib\psetargv.obj: skipped 0, total 8
.\VS9\VC\lib\pthreadlocale.obj: skipped 0, total 1
.\VS9\VC\lib\ptrustm.lib: skipped 0, total 173
.\VS9\VC\lib\ptrustmd.lib: skipped 0, total 174
.\VS9\VC\lib\ptrustu.lib: skipped 0, total 173
.\VS9\VC\lib\ptrustud.lib: skipped 0, total 174
.\VS9\VC\lib\pwsetargv.obj: skipped 0, total 8
.\VS9\VC\lib\RunTmChk.lib: skipped 1, total 52
.\VS9\VC\lib\setargv.obj: skipped 0, total 1
.\VS9\VC\lib\smalheap.obj: skipped 0, total 12
.\VS9\VC\lib\threadlocale.obj: skipped 0, total 0
.\VS9\VC\lib\vcomp.lib: skipped 112, total 112
.\VS9\VC\lib\vcompd.lib: skipped 112, total 112
.\VS9\VC\lib\wsetargv.obj: skipped 0, total 1
```

```
$ find VS9 -name '*.pat' -print0 | tar -czvf VS9/VS9.tar.gz --null -T -
VS9/VC/atlmfc/lib/amd64/atl.lib.pat
VS9/VC/atlmfc/lib/amd64/atldload.lib.pat
VS9/VC/atlmfc/lib/amd64/atls.lib.pat
VS9/VC/atlmfc/lib/amd64/atlsd.lib.pat
VS9/VC/atlmfc/lib/amd64/mfc90.lib.pat
VS9/VC/atlmfc/lib/amd64/mfc90d.lib.pat
VS9/VC/atlmfc/lib/amd64/mfc90u.lib.pat
VS9/VC/atlmfc/lib/amd64/mfc90ud.lib.pat
VS9/VC/atlmfc/lib/amd64/mfcdload.lib.pat
VS9/VC/atlmfc/lib/amd64/MFCM90.lib.pat
VS9/VC/atlmfc/lib/amd64/MFCM90D.lib.pat
VS9/VC/atlmfc/lib/amd64/MFCM90U.lib.pat
VS9/VC/atlmfc/lib/amd64/MFCM90UD.lib.pat
VS9/VC/atlmfc/lib/amd64/mfcs90.lib.pat
VS9/VC/atlmfc/lib/amd64/mfcs90d.lib.pat
VS9/VC/atlmfc/lib/amd64/mfcs90u.lib.pat
VS9/VC/atlmfc/lib/amd64/mfcs90ud.lib.pat
VS9/VC/atlmfc/lib/amd64/nafxcw.lib.pat
VS9/VC/atlmfc/lib/amd64/nafxcwd.lib.pat
VS9/VC/atlmfc/lib/amd64/uafxcw.lib.pat
VS9/VC/atlmfc/lib/amd64/uafxcwd.lib.pat
VS9/VC/atlmfc/lib/Atl.lib.pat
VS9/VC/atlmfc/lib/atldload.lib.pat
VS9/VC/atlmfc/lib/atls.lib.pat
VS9/VC/atlmfc/lib/atlsd.lib.pat
VS9/VC/atlmfc/lib/mfc90.lib.pat
VS9/VC/atlmfc/lib/mfc90d.lib.pat
VS9/VC/atlmfc/lib/mfc90u.lib.pat
VS9/VC/atlmfc/lib/mfc90ud.lib.pat
VS9/VC/atlmfc/lib/mfcdload.lib.pat
VS9/VC/atlmfc/lib/mfcm90.lib.pat
VS9/VC/atlmfc/lib/mfcm90d.lib.pat
VS9/VC/atlmfc/lib/mfcm90u.lib.pat
VS9/VC/atlmfc/lib/mfcm90ud.lib.pat
VS9/VC/atlmfc/lib/mfcs90.lib.pat
VS9/VC/atlmfc/lib/mfcs90d.lib.pat
VS9/VC/atlmfc/lib/mfcs90u.lib.pat
VS9/VC/atlmfc/lib/mfcs90ud.lib.pat
VS9/VC/atlmfc/lib/nafxcw.lib.pat
VS9/VC/atlmfc/lib/nafxcwd.lib.pat
VS9/VC/atlmfc/lib/uafxcw.lib.pat
VS9/VC/atlmfc/lib/uafxcwd.lib.pat
VS9/VC/crt/src/AMD64/almap.lib.pat
VS9/VC/crt/src/AMD64/almapdll.lib.pat
VS9/VC/crt/src/AMD64/dll_lib/amdsecgs.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/chandler.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/chkstk.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/chkstk2.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/clr_obj/managdeh.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehvccctr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehvcccvb.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecctr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehveccvb.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mehvecdtr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/clr_obj/mstdexpt.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/conv.lib.pat
VS9/VC/crt/src/AMD64/dll_lib/eh.lib.pat
VS9/VC/crt/src/AMD64/dll_lib/ehvccctr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/ehvcccvb.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/ehvecctr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/ehveccvb.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/ehvecdtr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/gshandler.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/gshandlereh.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/gshandlerseh.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/jmpuwind.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/longjmp.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/matherr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/memcpy.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/oldexcpt.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/pure_obj/managdeh.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehvccctr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehvcccvb.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecctr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehveccvb.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/pure_obj/mehvecdtr.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/pure_obj/rtti.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/rtc.lib.pat
VS9/VC/crt/src/AMD64/dll_lib/rtcmd.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/setjmp.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/setjmpex.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/tncleanup.obj.pat
VS9/VC/crt/src/AMD64/dll_lib/tran.lib.pat
VS9/VC/crt/src/AMD64/dll_lib/unhandld.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/amdsecgs.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/chandler.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/chkstk.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/chkstk2.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/conv.lib.pat
VS9/VC/crt/src/AMD64/mt_lib/eh.lib.pat
VS9/VC/crt/src/AMD64/mt_lib/gshandler.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/gshandlereh.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/gshandlerseh.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/jmpuwind.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/longjmp.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/matherr.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/memcpy.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/rtc.lib.pat
VS9/VC/crt/src/AMD64/mt_lib/rtcmd.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/setjmp.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/setjmpex.obj.pat
VS9/VC/crt/src/AMD64/mt_lib/tran.lib.pat
VS9/VC/crt/src/AMD64/sdknames.lib.pat
VS9/VC/crt/src/AMD64/tcmap.lib.pat
VS9/VC/crt/src/AMD64/tcmapdll.lib.pat
VS9/VC/crt/src/AMD64/xdll_lib/amdsecgs.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/chandler.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/chkstk.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/chkstk2.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/managdeh.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvccctr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvcccvb.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecctr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehveccvb.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mehvecdtr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/clr_obj/mstdexpt.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/conv.lib.pat
VS9/VC/crt/src/AMD64/xdll_lib/eh.lib.pat
VS9/VC/crt/src/AMD64/xdll_lib/ehvccctr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/ehvcccvb.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/ehvecctr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/ehveccvb.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/ehvecdtr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/gshandler.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/gshandlereh.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/gshandlerseh.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/jmpuwind.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/longjmp.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/matherr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/memcpy.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/oldexcpt.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/managdeh.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvccctr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvcccvb.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecctr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehveccvb.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/mehvecdtr.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/pure_obj/rtti.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/rtc.lib.pat
VS9/VC/crt/src/AMD64/xdll_lib/rtcmd.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/setjmp.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/setjmpex.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/tncleanup.obj.pat
VS9/VC/crt/src/AMD64/xdll_lib/tran.lib.pat
VS9/VC/crt/src/AMD64/xdll_lib/unhandld.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/amdsecgs.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/chandler.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/chkstk.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/chkstk2.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/conv.lib.pat
VS9/VC/crt/src/AMD64/xmt_lib/eh.lib.pat
VS9/VC/crt/src/AMD64/xmt_lib/gshandler.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/gshandlereh.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/gshandlerseh.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/jmpuwind.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/longjmp.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/matherr.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/memcpy.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/rtc.lib.pat
VS9/VC/crt/src/AMD64/xmt_lib/rtcmd.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/setjmp.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/setjmpex.obj.pat
VS9/VC/crt/src/AMD64/xmt_lib/tran.lib.pat
VS9/VC/crt/src/intel/almap.lib.pat
VS9/VC/crt/src/intel/almapdll.lib.pat
VS9/VC/crt/src/intel/dll_lib/alloca16.obj.pat
VS9/VC/crt/src/intel/dll_lib/atlssup.obj.pat
VS9/VC/crt/src/intel/dll_lib/calldtor.obj.pat
VS9/VC/crt/src/intel/dll_lib/chandler4.obj.pat
VS9/VC/crt/src/intel/dll_lib/chandler4gs.obj.pat
VS9/VC/crt/src/intel/dll_lib/chkesp.obj.pat
VS9/VC/crt/src/intel/dll_lib/chkstk.obj.pat
VS9/VC/crt/src/intel/dll_lib/clr_obj/managdeh.obj.pat
VS9/VC/crt/src/intel/dll_lib/clr_obj/mehvccctr.obj.pat
VS9/VC/crt/src/intel/dll_lib/clr_obj/mehvcccvb.obj.pat
VS9/VC/crt/src/intel/dll_lib/clr_obj/mehvecctr.obj.pat
VS9/VC/crt/src/intel/dll_lib/clr_obj/mehveccvb.obj.pat
VS9/VC/crt/src/intel/dll_lib/clr_obj/mehvecdtr.obj.pat
VS9/VC/crt/src/intel/dll_lib/clr_obj/mstdexpt.obj.pat
VS9/VC/crt/src/intel/dll_lib/conv.lib.pat
VS9/VC/crt/src/intel/dll_lib/cpu_disp.obj.pat
VS9/VC/crt/src/intel/dll_lib/dllsupp.obj.pat
VS9/VC/crt/src/intel/dll_lib/eh.lib.pat
VS9/VC/crt/src/intel/dll_lib/eh3valid.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehprolg2.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehprolg3.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehprolg3a.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehprolog.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehvccctr.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehvcccvb.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehvecctr.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehveccvb.obj.pat
VS9/VC/crt/src/intel/dll_lib/ehvecdtr.obj.pat
VS9/VC/crt/src/intel/dll_lib/enable.obj.pat
VS9/VC/crt/src/intel/dll_lib/exsup.obj.pat
VS9/VC/crt/src/intel/dll_lib/exsup2.obj.pat
VS9/VC/crt/src/intel/dll_lib/exsup3.obj.pat
VS9/VC/crt/src/intel/dll_lib/exsup4.obj.pat
VS9/VC/crt/src/intel/dll_lib/ftol2.obj.pat
VS9/VC/crt/src/intel/dll_lib/inp.obj.pat
VS9/VC/crt/src/intel/dll_lib/lldiv.obj.pat
VS9/VC/crt/src/intel/dll_lib/lldvrm.obj.pat
VS9/VC/crt/src/intel/dll_lib/llmul.obj.pat
VS9/VC/crt/src/intel/dll_lib/llrem.obj.pat
VS9/VC/crt/src/intel/dll_lib/llshl.obj.pat
VS9/VC/crt/src/intel/dll_lib/llshr.obj.pat
VS9/VC/crt/src/intel/dll_lib/longjmp.obj.pat
VS9/VC/crt/src/intel/dll_lib/matherr.obj.pat
VS9/VC/crt/src/intel/dll_lib/memccpy.obj.pat
VS9/VC/crt/src/intel/dll_lib/memchr.obj.pat
VS9/VC/crt/src/intel/dll_lib/memcmp.obj.pat
VS9/VC/crt/src/intel/dll_lib/memcpy.obj.pat
VS9/VC/crt/src/intel/dll_lib/memmove.obj.pat
VS9/VC/crt/src/intel/dll_lib/memset.obj.pat
VS9/VC/crt/src/intel/dll_lib/oldexcpt.obj.pat
VS9/VC/crt/src/intel/dll_lib/outp.obj.pat
VS9/VC/crt/src/intel/dll_lib/p4_memcpy.obj.pat
VS9/VC/crt/src/intel/dll_lib/p4_memset.obj.pat
VS9/VC/crt/src/intel/dll_lib/pure_obj/managdeh.obj.pat
VS9/VC/crt/src/intel/dll_lib/pure_obj/mehvccctr.obj.pat
VS9/VC/crt/src/intel/dll_lib/pure_obj/mehvcccvb.obj.pat
VS9/VC/crt/src/intel/dll_lib/pure_obj/mehvecctr.obj.pat
VS9/VC/crt/src/intel/dll_lib/pure_obj/mehveccvb.obj.pat
VS9/VC/crt/src/intel/dll_lib/pure_obj/mehvecdtr.obj.pat
VS9/VC/crt/src/intel/dll_lib/pure_obj/rtti.obj.pat
VS9/VC/crt/src/intel/dll_lib/rtc.lib.pat
VS9/VC/crt/src/intel/dll_lib/sehprolg.obj.pat
VS9/VC/crt/src/intel/dll_lib/sehprolg4.obj.pat
VS9/VC/crt/src/intel/dll_lib/sehprolg4gs.obj.pat
VS9/VC/crt/src/intel/dll_lib/sehsupp.obj.pat
VS9/VC/crt/src/intel/dll_lib/setjmp.obj.pat
VS9/VC/crt/src/intel/dll_lib/setjmp3.obj.pat
VS9/VC/crt/src/intel/dll_lib/setjmpex.obj.pat
VS9/VC/crt/src/intel/dll_lib/strcat.obj.pat
VS9/VC/crt/src/intel/dll_lib/strchr.obj.pat
VS9/VC/crt/src/intel/dll_lib/strcmp.obj.pat
VS9/VC/crt/src/intel/dll_lib/strcspn.obj.pat
VS9/VC/crt/src/intel/dll_lib/strlen.obj.pat
VS9/VC/crt/src/intel/dll_lib/strncat.obj.pat
VS9/VC/crt/src/intel/dll_lib/strncpy.obj.pat
VS9/VC/crt/src/intel/dll_lib/strnset.obj.pat
VS9/VC/crt/src/intel/dll_lib/strpbrk.obj.pat
VS9/VC/crt/src/intel/dll_lib/strrchr.obj.pat
VS9/VC/crt/src/intel/dll_lib/strrev.obj.pat
VS9/VC/crt/src/intel/dll_lib/strset.obj.pat
VS9/VC/crt/src/intel/dll_lib/strspn.obj.pat
VS9/VC/crt/src/intel/dll_lib/strstr.obj.pat
VS9/VC/crt/src/intel/dll_lib/tncleanup.obj.pat
VS9/VC/crt/src/intel/dll_lib/tran.lib.pat
VS9/VC/crt/src/intel/dll_lib/ulldiv.obj.pat
VS9/VC/crt/src/intel/dll_lib/ulldvrm.obj.pat
VS9/VC/crt/src/intel/dll_lib/ullrem.obj.pat
VS9/VC/crt/src/intel/dll_lib/ullshr.obj.pat
VS9/VC/crt/src/intel/dll_lib/unhandld.obj.pat
VS9/VC/crt/src/intel/dll_lib/_memicmp.obj.pat
VS9/VC/crt/src/intel/dll_lib/_strnicm.obj.pat
VS9/VC/crt/src/intel/mt_lib/alloca16.obj.pat
VS9/VC/crt/src/intel/mt_lib/atlssup.obj.pat
VS9/VC/crt/src/intel/mt_lib/calldtor.obj.pat
VS9/VC/crt/src/intel/mt_lib/chandler4.obj.pat
VS9/VC/crt/src/intel/mt_lib/chandler4gs.obj.pat
VS9/VC/crt/src/intel/mt_lib/chkesp.obj.pat
VS9/VC/crt/src/intel/mt_lib/chkstk.obj.pat
VS9/VC/crt/src/intel/mt_lib/conv.lib.pat
VS9/VC/crt/src/intel/mt_lib/eh.lib.pat
VS9/VC/crt/src/intel/mt_lib/eh3valid.obj.pat
VS9/VC/crt/src/intel/mt_lib/enable.obj.pat
VS9/VC/crt/src/intel/mt_lib/exsup.obj.pat
VS9/VC/crt/src/intel/mt_lib/exsup2.obj.pat
VS9/VC/crt/src/intel/mt_lib/exsup3.obj.pat
VS9/VC/crt/src/intel/mt_lib/exsup4.obj.pat
VS9/VC/crt/src/intel/mt_lib/inp.obj.pat
VS9/VC/crt/src/intel/mt_lib/lldiv.obj.pat
VS9/VC/crt/src/intel/mt_lib/lldvrm.obj.pat
VS9/VC/crt/src/intel/mt_lib/llmul.obj.pat
VS9/VC/crt/src/intel/mt_lib/llrem.obj.pat
VS9/VC/crt/src/intel/mt_lib/llshl.obj.pat
VS9/VC/crt/src/intel/mt_lib/llshr.obj.pat
VS9/VC/crt/src/intel/mt_lib/longjmp.obj.pat
VS9/VC/crt/src/intel/mt_lib/matherr.obj.pat
VS9/VC/crt/src/intel/mt_lib/memccpy.obj.pat
VS9/VC/crt/src/intel/mt_lib/memchr.obj.pat
VS9/VC/crt/src/intel/mt_lib/memcmp.obj.pat
VS9/VC/crt/src/intel/mt_lib/memcpy.obj.pat
VS9/VC/crt/src/intel/mt_lib/memmove.obj.pat
VS9/VC/crt/src/intel/mt_lib/memset.obj.pat
VS9/VC/crt/src/intel/mt_lib/outp.obj.pat
VS9/VC/crt/src/intel/mt_lib/p4_memcpy.obj.pat
VS9/VC/crt/src/intel/mt_lib/p4_memset.obj.pat
VS9/VC/crt/src/intel/mt_lib/rtc.lib.pat
VS9/VC/crt/src/intel/mt_lib/sehprolg.obj.pat
VS9/VC/crt/src/intel/mt_lib/sehprolg4.obj.pat
VS9/VC/crt/src/intel/mt_lib/sehprolg4gs.obj.pat
VS9/VC/crt/src/intel/mt_lib/sehsupp.obj.pat
VS9/VC/crt/src/intel/mt_lib/setjmp.obj.pat
VS9/VC/crt/src/intel/mt_lib/setjmp3.obj.pat
VS9/VC/crt/src/intel/mt_lib/setjmpex.obj.pat
VS9/VC/crt/src/intel/mt_lib/strcat.obj.pat
VS9/VC/crt/src/intel/mt_lib/strchr.obj.pat
VS9/VC/crt/src/intel/mt_lib/strcmp.obj.pat
VS9/VC/crt/src/intel/mt_lib/strcspn.obj.pat
VS9/VC/crt/src/intel/mt_lib/strlen.obj.pat
VS9/VC/crt/src/intel/mt_lib/strncat.obj.pat
VS9/VC/crt/src/intel/mt_lib/strncpy.obj.pat
VS9/VC/crt/src/intel/mt_lib/strnset.obj.pat
VS9/VC/crt/src/intel/mt_lib/strpbrk.obj.pat
VS9/VC/crt/src/intel/mt_lib/strrchr.obj.pat
VS9/VC/crt/src/intel/mt_lib/strrev.obj.pat
VS9/VC/crt/src/intel/mt_lib/strset.obj.pat
VS9/VC/crt/src/intel/mt_lib/strspn.obj.pat
VS9/VC/crt/src/intel/mt_lib/strstr.obj.pat
VS9/VC/crt/src/intel/mt_lib/tran.lib.pat
VS9/VC/crt/src/intel/mt_lib/ulldiv.obj.pat
VS9/VC/crt/src/intel/mt_lib/ulldvrm.obj.pat
VS9/VC/crt/src/intel/mt_lib/ullrem.obj.pat
VS9/VC/crt/src/intel/mt_lib/ullshr.obj.pat
VS9/VC/crt/src/intel/mt_lib/_memicmp.obj.pat
VS9/VC/crt/src/intel/mt_lib/_strnicm.obj.pat
VS9/VC/crt/src/intel/sdknames.lib.pat
VS9/VC/crt/src/intel/tcmap.lib.pat
VS9/VC/crt/src/intel/tcmapdll.lib.pat
VS9/VC/crt/src/intel/xdll_lib/alloca16.obj.pat
VS9/VC/crt/src/intel/xdll_lib/atlssup.obj.pat
VS9/VC/crt/src/intel/xdll_lib/calldtor.obj.pat
VS9/VC/crt/src/intel/xdll_lib/chandler4.obj.pat
VS9/VC/crt/src/intel/xdll_lib/chandler4gs.obj.pat
VS9/VC/crt/src/intel/xdll_lib/chkesp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/chkstk.obj.pat
VS9/VC/crt/src/intel/xdll_lib/clr_obj/managdeh.obj.pat
VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehvccctr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehvcccvb.obj.pat
VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehvecctr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehveccvb.obj.pat
VS9/VC/crt/src/intel/xdll_lib/clr_obj/mehvecdtr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/clr_obj/mstdexpt.obj.pat
VS9/VC/crt/src/intel/xdll_lib/conv.lib.pat
VS9/VC/crt/src/intel/xdll_lib/cpu_disp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/dllsupp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/eh.lib.pat
VS9/VC/crt/src/intel/xdll_lib/eh3valid.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehprolg2.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehprolg3.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehprolg3a.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehprolog.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehvccctr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehvcccvb.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehvecctr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehveccvb.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ehvecdtr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/enable.obj.pat
VS9/VC/crt/src/intel/xdll_lib/exsup.obj.pat
VS9/VC/crt/src/intel/xdll_lib/exsup2.obj.pat
VS9/VC/crt/src/intel/xdll_lib/exsup3.obj.pat
VS9/VC/crt/src/intel/xdll_lib/exsup4.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ftol2.obj.pat
VS9/VC/crt/src/intel/xdll_lib/inp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/lldiv.obj.pat
VS9/VC/crt/src/intel/xdll_lib/lldvrm.obj.pat
VS9/VC/crt/src/intel/xdll_lib/llmul.obj.pat
VS9/VC/crt/src/intel/xdll_lib/llrem.obj.pat
VS9/VC/crt/src/intel/xdll_lib/llshl.obj.pat
VS9/VC/crt/src/intel/xdll_lib/llshr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/longjmp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/matherr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/memccpy.obj.pat
VS9/VC/crt/src/intel/xdll_lib/memchr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/memcmp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/memcpy.obj.pat
VS9/VC/crt/src/intel/xdll_lib/memmove.obj.pat
VS9/VC/crt/src/intel/xdll_lib/memset.obj.pat
VS9/VC/crt/src/intel/xdll_lib/oldexcpt.obj.pat
VS9/VC/crt/src/intel/xdll_lib/outp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/p4_memcpy.obj.pat
VS9/VC/crt/src/intel/xdll_lib/p4_memset.obj.pat
VS9/VC/crt/src/intel/xdll_lib/pure_obj/managdeh.obj.pat
VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehvccctr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehvcccvb.obj.pat
VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehvecctr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehveccvb.obj.pat
VS9/VC/crt/src/intel/xdll_lib/pure_obj/mehvecdtr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/pure_obj/rtti.obj.pat
VS9/VC/crt/src/intel/xdll_lib/rtc.lib.pat
VS9/VC/crt/src/intel/xdll_lib/sehprolg.obj.pat
VS9/VC/crt/src/intel/xdll_lib/sehprolg4.obj.pat
VS9/VC/crt/src/intel/xdll_lib/sehprolg4gs.obj.pat
VS9/VC/crt/src/intel/xdll_lib/sehsupp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/setjmp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/setjmp3.obj.pat
VS9/VC/crt/src/intel/xdll_lib/setjmpex.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strcat.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strchr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strcmp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strcspn.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strlen.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strncat.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strncpy.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strnset.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strpbrk.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strrchr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strrev.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strset.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strspn.obj.pat
VS9/VC/crt/src/intel/xdll_lib/strstr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/tncleanup.obj.pat
VS9/VC/crt/src/intel/xdll_lib/tran.lib.pat
VS9/VC/crt/src/intel/xdll_lib/ulldiv.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ulldvrm.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ullrem.obj.pat
VS9/VC/crt/src/intel/xdll_lib/ullshr.obj.pat
VS9/VC/crt/src/intel/xdll_lib/unhandld.obj.pat
VS9/VC/crt/src/intel/xdll_lib/_memicmp.obj.pat
VS9/VC/crt/src/intel/xdll_lib/_strnicm.obj.pat
VS9/VC/crt/src/intel/xmt_lib/alloca16.obj.pat
VS9/VC/crt/src/intel/xmt_lib/atlssup.obj.pat
VS9/VC/crt/src/intel/xmt_lib/calldtor.obj.pat
VS9/VC/crt/src/intel/xmt_lib/chandler4.obj.pat
VS9/VC/crt/src/intel/xmt_lib/chandler4gs.obj.pat
VS9/VC/crt/src/intel/xmt_lib/chkesp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/chkstk.obj.pat
VS9/VC/crt/src/intel/xmt_lib/conv.lib.pat
VS9/VC/crt/src/intel/xmt_lib/eh.lib.pat
VS9/VC/crt/src/intel/xmt_lib/eh3valid.obj.pat
VS9/VC/crt/src/intel/xmt_lib/enable.obj.pat
VS9/VC/crt/src/intel/xmt_lib/exsup.obj.pat
VS9/VC/crt/src/intel/xmt_lib/exsup2.obj.pat
VS9/VC/crt/src/intel/xmt_lib/exsup3.obj.pat
VS9/VC/crt/src/intel/xmt_lib/exsup4.obj.pat
VS9/VC/crt/src/intel/xmt_lib/inp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/lldiv.obj.pat
VS9/VC/crt/src/intel/xmt_lib/lldvrm.obj.pat
VS9/VC/crt/src/intel/xmt_lib/llmul.obj.pat
VS9/VC/crt/src/intel/xmt_lib/llrem.obj.pat
VS9/VC/crt/src/intel/xmt_lib/llshl.obj.pat
VS9/VC/crt/src/intel/xmt_lib/llshr.obj.pat
VS9/VC/crt/src/intel/xmt_lib/longjmp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/matherr.obj.pat
VS9/VC/crt/src/intel/xmt_lib/memccpy.obj.pat
VS9/VC/crt/src/intel/xmt_lib/memchr.obj.pat
VS9/VC/crt/src/intel/xmt_lib/memcmp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/memcpy.obj.pat
VS9/VC/crt/src/intel/xmt_lib/memmove.obj.pat
VS9/VC/crt/src/intel/xmt_lib/memset.obj.pat
VS9/VC/crt/src/intel/xmt_lib/outp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/p4_memcpy.obj.pat
VS9/VC/crt/src/intel/xmt_lib/p4_memset.obj.pat
VS9/VC/crt/src/intel/xmt_lib/rtc.lib.pat
VS9/VC/crt/src/intel/xmt_lib/sehprolg.obj.pat
VS9/VC/crt/src/intel/xmt_lib/sehprolg4.obj.pat
VS9/VC/crt/src/intel/xmt_lib/sehprolg4gs.obj.pat
VS9/VC/crt/src/intel/xmt_lib/sehsupp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/setjmp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/setjmp3.obj.pat
VS9/VC/crt/src/intel/xmt_lib/setjmpex.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strcat.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strchr.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strcmp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strcspn.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strlen.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strncat.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strncpy.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strnset.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strpbrk.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strrchr.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strrev.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strset.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strspn.obj.pat
VS9/VC/crt/src/intel/xmt_lib/strstr.obj.pat
VS9/VC/crt/src/intel/xmt_lib/tran.lib.pat
VS9/VC/crt/src/intel/xmt_lib/ulldiv.obj.pat
VS9/VC/crt/src/intel/xmt_lib/ulldvrm.obj.pat
VS9/VC/crt/src/intel/xmt_lib/ullrem.obj.pat
VS9/VC/crt/src/intel/xmt_lib/ullshr.obj.pat
VS9/VC/crt/src/intel/xmt_lib/_memicmp.obj.pat
VS9/VC/crt/src/intel/xmt_lib/_strnicm.obj.pat
VS9/VC/lib/amd64/binmode.obj.pat
VS9/VC/lib/amd64/chkstk.obj.pat
VS9/VC/lib/amd64/commode.obj.pat
VS9/VC/lib/amd64/comsupp.lib.pat
VS9/VC/lib/amd64/comsuppd.lib.pat
VS9/VC/lib/amd64/comsuppw.lib.pat
VS9/VC/lib/amd64/comsuppwd.lib.pat
VS9/VC/lib/amd64/delayimp.lib.pat
VS9/VC/lib/amd64/invalidcontinue.obj.pat
VS9/VC/lib/amd64/libcmt.lib.pat
VS9/VC/lib/amd64/libcmtd.lib.pat
VS9/VC/lib/amd64/libcpmt.lib.pat
VS9/VC/lib/amd64/libcpmtd.lib.pat
VS9/VC/lib/amd64/loosefpmath.obj.pat
VS9/VC/lib/amd64/msvcmrt.lib.pat
VS9/VC/lib/amd64/msvcmrtd.lib.pat
VS9/VC/lib/amd64/msvcprt.lib.pat
VS9/VC/lib/amd64/msvcprtd.lib.pat
VS9/VC/lib/amd64/msvcrt.lib.pat
VS9/VC/lib/amd64/msvcrtd.lib.pat
VS9/VC/lib/amd64/msvcurt.lib.pat
VS9/VC/lib/amd64/msvcurtd.lib.pat
VS9/VC/lib/amd64/newmode.obj.pat
VS9/VC/lib/amd64/noarg.obj.pat
VS9/VC/lib/amd64/nochkclr.obj.pat
VS9/VC/lib/amd64/noenv.obj.pat
VS9/VC/lib/amd64/nothrownew.obj.pat
VS9/VC/lib/amd64/oldnames.lib.pat
VS9/VC/lib/amd64/pbinmode.obj.pat
VS9/VC/lib/amd64/pcommode.obj.pat
VS9/VC/lib/amd64/pgobootrun.lib.pat
VS9/VC/lib/amd64/pgort.lib.pat
VS9/VC/lib/amd64/pinvalidcontinue.obj.pat
VS9/VC/lib/amd64/pnewmode.obj.pat
VS9/VC/lib/amd64/pnoarg.obj.pat
VS9/VC/lib/amd64/pnoenv.obj.pat
VS9/VC/lib/amd64/pnothrownew.obj.pat
VS9/VC/lib/amd64/psetargv.obj.pat
VS9/VC/lib/amd64/pthreadlocale.obj.pat
VS9/VC/lib/amd64/ptrustm.lib.pat
VS9/VC/lib/amd64/ptrustmd.lib.pat
VS9/VC/lib/amd64/ptrustu.lib.pat
VS9/VC/lib/amd64/ptrustud.lib.pat
VS9/VC/lib/amd64/pwsetargv.obj.pat
VS9/VC/lib/amd64/runtmchk.lib.pat
VS9/VC/lib/amd64/setargv.obj.pat
VS9/VC/lib/amd64/smalheap.obj.pat
VS9/VC/lib/amd64/threadlocale.obj.pat
VS9/VC/lib/amd64/vcomp.lib.pat
VS9/VC/lib/amd64/vcompd.lib.pat
VS9/VC/lib/amd64/wsetargv.obj.pat
VS9/VC/lib/binmode.obj.pat
VS9/VC/lib/chkstk.obj.pat
VS9/VC/lib/commode.obj.pat
VS9/VC/lib/comsupp.lib.pat
VS9/VC/lib/comsuppd.lib.pat
VS9/VC/lib/comsuppw.lib.pat
VS9/VC/lib/comsuppwd.lib.pat
VS9/VC/lib/delayimp.lib.pat
VS9/VC/lib/fp10.obj.pat
VS9/VC/lib/invalidcontinue.obj.pat
VS9/VC/lib/libcmt.lib.pat
VS9/VC/lib/libcmtd.lib.pat
VS9/VC/lib/libcpmt.lib.pat
VS9/VC/lib/libcpmtd.lib.pat
VS9/VC/lib/loosefpmath.obj.pat
VS9/VC/lib/msvcmrt.lib.pat
VS9/VC/lib/msvcmrtd.lib.pat
VS9/VC/lib/msvcprt.lib.pat
VS9/VC/lib/msvcprtd.lib.pat
VS9/VC/lib/msvcrt.lib.pat
VS9/VC/lib/msvcrtd.lib.pat
VS9/VC/lib/msvcurt.lib.pat
VS9/VC/lib/msvcurtd.lib.pat
VS9/VC/lib/newmode.obj.pat
VS9/VC/lib/noarg.obj.pat
VS9/VC/lib/nochkclr.obj.pat
VS9/VC/lib/noenv.obj.pat
VS9/VC/lib/nothrownew.obj.pat
VS9/VC/lib/oldnames.lib.pat
VS9/VC/lib/opends60.lib.pat
VS9/VC/lib/pbinmode.obj.pat
VS9/VC/lib/pcommode.obj.pat
VS9/VC/lib/pgobootrun.lib.pat
VS9/VC/lib/pgort.lib.pat
VS9/VC/lib/pinvalidcontinue.obj.pat
VS9/VC/lib/pnewmode.obj.pat
VS9/VC/lib/pnoarg.obj.pat
VS9/VC/lib/pnoenv.obj.pat
VS9/VC/lib/pnothrownew.obj.pat
VS9/VC/lib/psetargv.obj.pat
VS9/VC/lib/pthreadlocale.obj.pat
VS9/VC/lib/ptrustm.lib.pat
VS9/VC/lib/ptrustmd.lib.pat
VS9/VC/lib/ptrustu.lib.pat
VS9/VC/lib/ptrustud.lib.pat
VS9/VC/lib/pwsetargv.obj.pat
VS9/VC/lib/RunTmChk.lib.pat
VS9/VC/lib/setargv.obj.pat
VS9/VC/lib/smalheap.obj.pat
VS9/VC/lib/threadlocale.obj.pat
VS9/VC/lib/vcomp.lib.pat
VS9/VC/lib/vcompd.lib.pat
VS9/VC/lib/wsetargv.obj.pat
```
