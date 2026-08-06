<#
.SYNOPSIS
Template rendering services for the OGS Developer Toolkit.

.DESCRIPTION
Provides reusable template rendering functionality for the
OGS Financial Operating System (OGS-FOS) developer toolkit.

The renderer is responsible for:

    - Building template token contexts
    - Resolving token values
    - Expanding template placeholders
    - Detecting unresolved placeholders
    - Rendering template content

The module does not create directories or manage generation plans.
Filesystem orchestration remains the responsibility of the generator
execution layer.

.NOTES
Project      : OGS Financial Operating System
Short Name   : OGS-FOS
Organization : Om Ganapati Solution
Module       : TemplateRenderer
Version      : 1.0.0
#>

Set-StrictMode -Version Latest

$ErrorActionPreference = 'Stop'


# ============================================================================
# Module Constants
# ============================================================================

$script:RendererVersion = [Version]'1.0.0'

$script:TokenPattern = '\{\{([A-Z][A-Z0-9_]*)\}\}'


# ============================================================================
# Module Information
# ============================================================================

function Get-OGSTemplateRendererVersion {

    [CmdletBinding()]
    [OutputType([Version])]
    param()

    return $script:RendererVersion
}


# ============================================================================
# Public API
# ============================================================================



# ============================================================================
# Token Context
# ============================================================================

function New-OGSTokenContext {

    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$ProjectName,

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$ProjectVersion,

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Organization,

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$ModuleName,

        [Parameter()]
        [AllowEmptyString()]
        [string]$ProjectShortName = '',

        [Parameter()]
        [AllowEmptyString()]
        [string]$Codename = ''

    )

    $normalizedModuleName = $ModuleName.Trim()

    if ([string]::IsNullOrWhiteSpace($normalizedModuleName)) {

        throw "Module name cannot be empty or whitespace."

    }

    $generatedAt = Get-Date

    return [PSCustomObject]@{

        ProjectName      = $ProjectName.Trim()

        ProjectVersion   = $ProjectVersion.Trim()

        ProjectShortName = $ProjectShortName.Trim()

        Organization     = $Organization.Trim()

        Codename         = $Codename.Trim()

        ModuleName       = $normalizedModuleName

        GeneratedAt      = $generatedAt

        Year             = $generatedAt.Year

    }

}
# ============================================================================
# Get Template Tokens
# ============================================================================

function Get-OGSTemplateTokens {

    [CmdletBinding()]
    [OutputType([hashtable])]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNull()]
        [PSCustomObject]$Context

    )

    $tokens = @{

        PROJECT_NAME =
            [string]$Context.ProjectName

        PROJECT_VERSION =
            [string]$Context.ProjectVersion

        PROJECT_SHORT_NAME =
            [string]$Context.ProjectShortName

        ORGANIZATION =
            [string]$Context.Organization

        CODENAME =
            [string]$Context.Codename

        MODULE_NAME =
            [string]$Context.ModuleName

        GENERATED_AT =
            $Context.GeneratedAt.ToString('yyyy-MM-dd HH:mm:ss')

        YEAR =
            [string]$Context.Year

    }

    return $tokens
}

# ============================================================================
# Expand Template Content
# ============================================================================

function Expand-OGSTemplateContent {

    [CmdletBinding()]
    [OutputType([string])]
    param(

        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Content,

        [Parameter(Mandatory)]
        [ValidateNotNull()]
        [hashtable]$Tokens

    )

    if ([string]::IsNullOrEmpty($Content)) {

        return $Content

    }

    $renderedContent = $Content

    foreach ($tokenName in $Tokens.Keys) {

        $placeholder = '{{' + [string]$tokenName + '}}'

        $tokenValue = [string]$Tokens[$tokenName]

        $renderedContent = $renderedContent.Replace(
            $placeholder,
            $tokenValue
        )

    }

    return $renderedContent
}

# ============================================================================
# Test Template Tokens
# ============================================================================

function Test-OGSTemplateTokens {

    [CmdletBinding()]
    [OutputType([bool])]
    param(

        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Content

    )

    if ([string]::IsNullOrEmpty($Content)) {
        return $true
    }

    $matches = [regex]::Matches(
        $Content,
        $script:TokenPattern
    )

    if ($matches.Count -eq 0) {
        return $true
    }

    Write-Verbose "Unresolved template tokens detected."

    foreach ($match in $matches) {

        Write-Verbose (
            "Unresolved token: {0}" -f $match.Value
        )

    }

    return $false
}

# ============================================================================
# Invoke Template Render
# ============================================================================

function Invoke-OGSTemplateRender {

    [CmdletBinding()]
    [OutputType([string])]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$TemplatePath,

        [Parameter(Mandatory)]
        [ValidateNotNull()]
        [hashtable]$Tokens

    )

    # ------------------------------------------------------------------------
    # Validate template path
    # ------------------------------------------------------------------------

    if (-not (Test-Path -LiteralPath $TemplatePath -PathType Leaf)) {

        throw "Template file was not found: $TemplatePath"

    }

    # ------------------------------------------------------------------------
    # Resolve absolute path
    # ------------------------------------------------------------------------

    $resolvedTemplatePath = (Resolve-Path -LiteralPath $TemplatePath).Path

    Write-Verbose (
        "Rendering template: {0}" -f $resolvedTemplatePath
    )

    # ------------------------------------------------------------------------
    # Read template
    # ------------------------------------------------------------------------

    try {

        $content = Get-Content `
            -LiteralPath $resolvedTemplatePath `
            -Raw `
            -Encoding UTF8

    }
    catch {

        throw "Unable to read template '$resolvedTemplatePath'. $($_.Exception.Message)"

    }

    # ------------------------------------------------------------------------
    # Expand tokens
    # ------------------------------------------------------------------------

    $renderedContent = Expand-OGSTemplateContent `
        -Content $content `
        -Tokens $Tokens

    # ------------------------------------------------------------------------
    # Validate rendered content
    # ------------------------------------------------------------------------

    $isValid = Test-OGSTemplateTokens `
        -Content $renderedContent

    if (-not $isValid) {

        $unresolved = [regex]::Matches(
            $renderedContent,
            $script:TokenPattern
        ) |
        ForEach-Object {
            $_.Value
        } |
        Sort-Object -Unique

        $tokenList = $unresolved -join ', '

        throw @"
Template rendering failed.

Template:
$resolvedTemplatePath

Unresolved tokens:
$tokenList
"@

    }

    Write-Verbose (
        "Template rendered successfully: {0}" -f $resolvedTemplatePath
    )

    return $renderedContent
}

# ============================================================================
# Public API
# ============================================================================

Export-ModuleMember -Function @(
    'Get-OGSTemplateRendererVersion',
    'New-OGSTokenContext',
    'Get-OGSTemplateTokens',
    'Expand-OGSTemplateContent',
    'Test-OGSTemplateTokens',
    'Invoke-OGSTemplateRender'
)