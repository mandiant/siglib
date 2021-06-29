function Build-Library {
    [CmdletBinding()]
    param (
        [ValidateNotNullOrEmpty()]
        [string[]]$Libraries = @()
    )

    $platforms = @("x86-windows-static", "x64-windows-static");
    $versions = @("v140", "v141", "v142");

    $arguments = "";

    foreach ($library in $Libraries) {
        foreach ($platform in $platforms) {
            foreach ($version in $versions) {
                $arguments += " ${library}:${platform}-${version}";
            }
        }
    }

    $cmd = "docker run --network 'Default Switch' -v libs:c:\vcpkg\vcpkg-master\installed buildtools install ${arguments}";
    Write-Verbose -Message $cmd;

    Invoke-Expression $cmd;
}
