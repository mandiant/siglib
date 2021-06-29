# escape=`

# A Window 10 Docker container with Visual Studio 2015/2017/2019 installed alongside vcpkg.
#
# prerequisites:
#
#   - Windows 10 with Hyper-V and Containers enabled
#   - Docker for Windows, configured with Windows Containers
#
# build:
#
#   docker build -t buildtools:latest --isolation=hyperv --network "Default Switch" .
#
# available triplets:
# 
#   - `x64-windows-static-v140` - VS 2015 x64
#   - `x64-windows-static-v141` - VS 2017
#   - `x64-windows-static-v142` - VS 2019
#   - `x86-windows-static-v140` - VS 2015 x86
#   - `x86-windows-static-v141` - VS 2017
#   - `x86-windows-static-v142` - VS 2019
#
# invoke vcpkg via Docker container:
#
# ```
# docker volume create libs
# docker run -it `
#   --network "Default Switch" `
#   -v libs:c:\vcpkg\vcpkg-master\installed `
#   buildtools install `
#   zlib:x64-windows-static-v140 `
#   zlib:x64-windows-static-v141 `
#   zlib:x64-windows-static-v142 `
#   zlib:x86-windows-static-v140 `
#   zlib:x86-windows-static-v141 `
#   zlib:x86-windows-static-v142
# ```
#
# or use the ps1 function `Build-Library`:
#
# ```
# PS> . .\buildtools.ps1
# PS> Build-Library -Verbose @("cryptopp", "curl", "detours", "openssl", "mbedtls", "zlib")
# ```
#
# use `docker volume inspect sigs` to figure out where the volume data is stored.
# by default, its probably `C:\ProgramData\Docker\volumes\libs\_data`.


FROM mcr.microsoft.com/windows/servercore:ltsc2019

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

# Visual Studio 2019 online installer
ADD https://aka.ms/vs/16/release/channel C:\TEMP\VisualStudio2019.chman
ADD https://aka.ms/vs/16/release/vs_buildtools.exe C:\TEMP\vs_buildtools2019.exe

SHELL ["cmd", "/S", "/C"]

# install VS2019 build tools and resources
#
# from: https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019
# Microsoft.VisualStudio.Component.VC.Tools.x86.x64    MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.28)
# Microsoft.VisualStudio.Component.VC.CLI.Support      C++/CLI support for v142 build tools (14.28)
RUN C:\TEMP\vs_buildtools2019.exe --quiet --wait --norestart --nocache `
    --installPath C:\BuildTools `
    --channelUri C:\Temp\VisualStudio2019.chman `
    --installChannelUri C:\Temp\VisualStudio2019.chman `
    --add Microsoft.VisualStudio.Workload.VCTools;includeRecommended `
    --add microsoft.visualstudio.component.winxp `
    --add microsoft.visualstudio.component.vc.atl `
    --add microsoft.visualstudio.component.vc.atlmfc `
    --add microsoft.component.vc.runtime.ucrtsdk `
    --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 `
    --add Microsoft.VisualStudio.Component.VC.CLI.Support `
|| IF "%ERRORLEVEL%"=="3010" EXIT 0

# install VS2015 build tools
#
# Microsoft.VisualStudio.Component.VC.140              MSVC v140 - VS 2015 C++ build tools (v14.00)
RUN C:\TEMP\vs_buildtools2019.exe --quiet --wait --norestart --nocache `
    --installPath C:\BuildTools `
    --channelUri C:\Temp\VisualStudio2019.chman `
    --installChannelUri C:\Temp\VisualStudio2019.chman `
    --add Microsoft.VisualStudio.Component.VC.140 `
|| IF "%ERRORLEVEL%"=="3010" EXIT 0

# install VS2017 build tools
#
# Microsoft.VisualStudio.Component.VC.v141.x86.x64     MSVC v141 - VS 2017 C++ x64/x86 build tools (v14.16)
# Microsoft.VisualStudio.Component.VC.v141.CLI.Support C++/CLI support for v141 build tools (14.16)
# Microsoft.VisualStudio.Component.VC.v141.ATL         C++ ATL for v141 build tools (x86 & x64), version 16.0.28625.61
# Microsoft.VisualStudio.Component.VC.v141.MFC         C++ MFC for v141 build tools (x86 & x64), version 16.0.28625.61

RUN C:\TEMP\vs_buildtools2019.exe --quiet --wait --norestart --nocache `
    --installPath C:\BuildTools `
    --channelUri C:\Temp\VisualStudio2019.chman `
    --installChannelUri C:\Temp\VisualStudio2019.chman `
    --add Microsoft.VisualStudio.Component.VC.v141.x86.x64 `
    --add Microsoft.VisualStudio.Component.VC.v141.CLI.Support `
    --add Microsoft.VisualStudio.Component.VC.v141.ATL `
    --add Microsoft.VisualStudio.Component.VC.v141.MFC `
|| IF "%ERRORLEVEL%"=="3010" EXIT 0

# install Windows 10 SDKs
#
# Microsoft.VisualStudio.Component.Windows10SDK.16299  Windows 10 SDK (10.0.16299.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.4 
# Microsoft.VisualStudio.Component.Windows10SDK.17134  Windows 10 SDK (10.0.17134.0), version 16.9.31004.209, usually bundled with Visual Studio 2017 ver.15.7 
# Microsoft.VisualStudio.Component.Windows10SDK.17763  Windows 10 SDK (10.0.17763.0), version 16.0.28517.75, usually bundled with Visual Studio 2017 ver.15.8 
# Microsoft.VisualStudio.Component.Windows10SDK.18362  Windows 10 SDK (10.0.18362.0), version 16.1.28829.92, usually bundled with Visual Studio 2019
RUN C:\TEMP\vs_buildtools2019.exe --quiet --wait --norestart --nocache `
    --channelUri C:\Temp\VisualStudio2019.chman `
    --installChannelUri C:\Temp\VisualStudio2019.chman `
    --add Microsoft.VisualStudio.Component.Windows10SDK.16299 `
    --add Microsoft.VisualStudio.Component.Windows10SDK.17134 `
    --add Microsoft.VisualStudio.Component.Windows10SDK.17763 `
    --add Microsoft.VisualStudio.Component.Windows10SDK.18362 `
|| IF "%ERRORLEVEL%"=="3010" EXIT 0

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

RUN Invoke-WebRequest https://github.com/Microsoft/vcpkg/archive/master.zip -OutFile vcpkg.zip;
RUN Expand-Archive vcpkg.zip -DestinationPath vcpkg;

WORKDIR C:/vcpkg/vcpkg-master
RUN New-Item -ItemType Directory -Path downloads;
RUN New-Item -ItemType File -Path downloads\AlwaysAllowEverything;
RUN scripts\bootstrap.ps1 -disableMetrics;

RUN ./vcpkg.exe integrate install

# prime tools (cmake, git, nuget, 7z, etc)
RUN ./vcpkg.exe install zlib

ADD x64-windows-static-v140.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x64-windows-static-v141.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x64-windows-static-v142.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x86-windows-static-v140.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x86-windows-static-v141.cmake C:/vcpkg/vcpkg-master/triplets/
ADD x86-windows-static-v142.cmake C:/vcpkg/vcpkg-master/triplets/

CMD ["powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass"]
ENTRYPOINT ["C:/vcpkg/vcpkg-master/vcpkg.exe"]