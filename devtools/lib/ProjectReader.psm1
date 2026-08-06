<#
.SYNOPSIS
    OGS Project Configuration Reader

.DESCRIPTION
    Reads and validates the OGS project manifest (ogs.project.yaml).

.NOTES
    Project : OGS Financial Operating System
    Version : 1.0.0
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Ensure YAML support is available
if (-not (Get-Command ConvertFrom-Yaml -ErrorAction SilentlyContinue)) {

    try {
        Import-Module powershell-yaml -ErrorAction Stop
    }
    catch {
        throw @"
The 'powershell-yaml' module is required.

Install it using:

    Install-Module powershell-yaml -Scope CurrentUser

Then restart PowerShell.
"@
    }
}

# ---------------------------------------------------------------------------
# Script Cache
# ---------------------------------------------------------------------------

$script:ProjectCache = $null
$script:ProjectRoot  = $null

# ---------------------------------------------------------------------------
# Private Functions
# ---------------------------------------------------------------------------

function Resolve-ProjectRoot {

    [CmdletBinding()]
    param()

    $current = Get-Item (Get-Location).Path

    while ($null -ne $current) {

        $manifest = Join-Path $current.FullName 'ogs.project.yaml'

        if (Test-Path -LiteralPath $manifest) {

            return $current.FullName

        }

        $current = $current.Parent

    }

    throw "Unable to locate 'ogs.project.yaml'."

}

function Read-ProjectFile {
    [CmdletBinding()]
    param()

    if ($null -ne $script:ProjectCache) {
        return $script:ProjectCache
    }

    $script:ProjectRoot = Resolve-ProjectRoot

    $manifest = Join-Path $script:ProjectRoot 'ogs.project.yaml'

    $yaml = Get-Content `
        -LiteralPath $manifest `
        -Raw

    $config = ConvertFrom-Yaml $yaml

    $null = Validate-Project -Configuration $config

    $script:ProjectCache = $config

    return $script:ProjectCache
}

function Validate-Project {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [object]$Configuration

    )

    $required = @(
        'project',
        'paths',
        'toolkit',
        'development',
        'generator'
    )

    foreach ($section in $required) {

        if ($null -eq $Configuration.$section) {

            throw "Invalid ogs.project.yaml. Missing required section '$section'."

        }

    }

    return
}

# ---------------------------------------------------------------------------
# Public Functions
# ---------------------------------------------------------------------------

function Get-OGSProject {

    [CmdletBinding()]
    param()

    return Read-ProjectFile
}

function Get-OGSVersion {

    [CmdletBinding()]
    param()

    $project = Read-ProjectFile

    return $project.project.version
}

function Get-OGSPath {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [ValidateSet(
            'Source',
            'Tests',
            'Docs',
            'DevTools'
        )]
        [string]$Name
    )

    $project = Read-ProjectFile
    $yaml = ConvertFrom-Yaml $content
    return ConvertTo-OGSObject $yaml

    switch ($Name) {

        'Source'   { return Join-Path $script:ProjectRoot $project.paths.source }

        'Tests'    { return Join-Path $script:ProjectRoot $project.paths.tests }

        'Docs'     { return Join-Path $script:ProjectRoot $project.paths.docs }

        'DevTools' { return Join-Path $script:ProjectRoot $project.paths.devtools }

        default {
            throw "Unknown path '$Name'."
        }
    }
}

function Test-OGSProject {

    [CmdletBinding()]
    param()

    try {

        Read-ProjectFile | Out-Null

        return $true

    }
    catch {

        return $false

    }
}

function Clear-OGSProjectCache {

    [CmdletBinding()]
    param()

    $script:ProjectCache = $null
    $script:ProjectRoot  = $null
}
function Get-OGSProjectRoot {

    [CmdletBinding()]
    param()

    Read-ProjectFile | Out-Null

    return $script:ProjectRoot
}

# ---------------------------------------------------------------------------
# Module Exports
# ---------------------------------------------------------------------------
function ConvertTo-OGSObject {

    param(
        [Parameter(Mandatory)]
        $InputObject
    )

    if ($InputObject -is [System.Collections.IDictionary]) {

        $obj = [PSCustomObject]@{}

        foreach ($key in $InputObject.Keys) {

            $obj | Add-Member `
                -MemberType NoteProperty `
                -Name $key `
                -Value (ConvertTo-OGSObject $InputObject[$key])

        }

        return $obj

    }

    if ($InputObject -is [System.Collections.IEnumerable] -and
        -not ($InputObject -is [string])) {

        $list = @()

        foreach ($item in $InputObject) {

            $list += ConvertTo-OGSObject $item

        }

        return $list

    }

    return $InputObject

}
Export-ModuleMember `
    -Function `
        Get-OGSProject,
        Get-OGSProjectRoot,
        Get-OGSPath,
        Get-OGSVersion,
        Test-OGSProject,
        Clear-OGSProjectCache
