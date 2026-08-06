<#
.SYNOPSIS
    Validation services for OGS generated source files.

.DESCRIPTION
    GenerationValidator provides validation primitives used by the
    OGS module generator after template rendering and file generation.

    The validator is intentionally independent from TemplateLoader and
    TemplateRenderer. It validates final generated content and files
    without modifying them.

.NOTES
    Project      : OGS Financial Operating System
    Organization : Om Ganapati Solution
    Codename     : GARUDA
#>

Set-StrictMode -Version Latest

$ErrorActionPreference = 'Stop'

# ============================================================================
# Module Metadata
# ============================================================================

$script:ValidatorVersion = '1.0.0'


# ============================================================================
# Get-OGSGenerationValidatorVersion
# ============================================================================

function Get-OGSGenerationValidatorVersion {

    [CmdletBinding()]
    [OutputType([string])]
    param()

    return $script:ValidatorVersion
}


# ============================================================================
# Test-OGSGeneratedContent
# ============================================================================

function Test-OGSGeneratedContent {

    [CmdletBinding()]
    [OutputType([bool])]
    param(

        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Content

    )

    # ------------------------------------------------------------------------
    # Empty content
    # ------------------------------------------------------------------------

    if ([string]::IsNullOrWhiteSpace($Content)) {

        Write-Verbose "Generated content is empty."

        return $false
    }


    # ------------------------------------------------------------------------
    # Unresolved OGS template tokens
    # ------------------------------------------------------------------------

    if (
        $Content -match
        '\{\{[A-Za-z_][A-Za-z0-9_]*\}\}'
    ) {

        Write-Verbose (
            "Generated content contains unresolved template tokens."
        )

        return $false
    }


    # ------------------------------------------------------------------------
    # Accidental PowerShell here-string markers
    # ------------------------------------------------------------------------

    if (
        $Content -match
        '(?m)^\s*@''\s*$'
    ) {

        Write-Verbose (
            "Generated content contains a PowerShell here-string opening marker."
        )

        return $false
    }


    if (
        $Content -match
        '(?m)^\s*''@\s*$'
    ) {

        Write-Verbose (
            "Generated content contains a PowerShell here-string closing marker."
        )

        return $false
    }


    # ------------------------------------------------------------------------
    # Accidental template-writing commands
    # ------------------------------------------------------------------------

    if (
        $Content -match
        '(?im)^\s*Set-Content\b'
    ) {

        Write-Verbose (
            "Generated content contains an unexpected Set-Content command."
        )

        return $false
    }


    if (
        $Content -match
        '(?im)''@\s*\|\s*Set-Content\b'
    ) {

        Write-Verbose (
            "Generated content contains a PowerShell template-writing trailer."
        )

        return $false
    }

        # ------------------------------------------------------------------------
    # Accidental PowerShell encoding argument
    # ------------------------------------------------------------------------

    if (
        $Content -match
        '(?im)^\s*-Encoding\s+UTF8\s*$'
    ) {

        Write-Verbose (
            "Generated content contains an unexpected PowerShell encoding argument."
        )

        return $false
    }


    return $true
}


# ============================================================================
# Test-OGSGeneratedFile
# ============================================================================

function Test-OGSGeneratedFile {

    [CmdletBinding()]
    [OutputType([bool])]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Path

    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {

        Write-Verbose (
            "Generated file does not exist: {0}" -f $Path
        )

        return $false
    }

    $content = Get-Content `
        -LiteralPath $Path `
        -Raw

    return Test-OGSGeneratedContent `
        -Content $content
}


# ============================================================================
# Assert-OGSGeneratedFile
# ============================================================================

function Assert-OGSGeneratedFile {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Path

    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {

        throw (
            "Generated file does not exist: {0}" -f $Path
        )
    }

    if (-not (Test-OGSGeneratedFile -Path $Path)) {

        throw (
            "Generated file validation failed: {0}" -f $Path
        )
    }

    Write-Verbose (
        "Generated file validation passed: {0}" -f $Path
    )
}


# ============================================================================
# Public API
# ============================================================================

Export-ModuleMember -Function @(
    'Get-OGSGenerationValidatorVersion',
    'Test-OGSGeneratedContent',
    'Test-OGSGeneratedFile',
    'Assert-OGSGeneratedFile'
)
