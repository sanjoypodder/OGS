Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ============================================================================
# Module Dependencies
# ============================================================================

$script:ModuleRoot = Split-Path -Parent $PSCommandPath

$projectReaderPath = Join-Path `
    $script:ModuleRoot `
    'ProjectReader.psm1'

if (-not (Test-Path -LiteralPath $projectReaderPath -PathType Leaf)) {

    throw "Required module was not found: $projectReaderPath"

}

Import-Module `
    $projectReaderPath `
    -ErrorAction Stop

# ============================================================================
# TemplateLoader
#
# OGS Financial Operating System
# Developer Toolkit
# ============================================================================

# ============================================================================
# Constants
# ============================================================================

$script:SupportedTemplateVersion = [Version]'1.0.0'

# ============================================================================
# Cache
# ============================================================================

$script:TemplateCache = @{}

# ============================================================================
# Private Functions
# ============================================================================

function Resolve-TemplatePath {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Name

    )

    $project = Get-OGSProject

    $definitionDirectory = $project.toolkit.definition_directory

    $projectRoot = Get-OGSProjectRoot

    $templatePath = Join-Path `
        $projectRoot `
        $definitionDirectory

    $templateFile = Join-Path `
        $templatePath `
        "$Name.yaml"

    if (-not (Test-Path -LiteralPath $templateFile)) {

        throw @"
Template '$Name' was not found.

Expected:

$templateFile
"@

    }

    return (Resolve-Path $templateFile).Path

}

# ============================================================================
# Resolve Template Definition
# ============================================================================

function Resolve-TemplateDefinition {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [string]$Name

    )

    $project = Get-OGSProject

    $definitionRoot = Join-Path `
        (Get-OGSProjectRoot) `
        $project.toolkit.definition_directory

    return Join-Path `
        $definitionRoot `
        "$Name.yaml"

}

# ============================================================================
# Resolve Template Asset
# ============================================================================

function Resolve-TemplateAsset {

    [CmdletBinding()]
    [OutputType([string])]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$RelativePath

    )

    # ------------------------------------------------------------------------
    # Validate input
    # ------------------------------------------------------------------------

    if ([string]::IsNullOrWhiteSpace($RelativePath)) {
        throw "Template asset relative path cannot be empty or whitespace."
    }

    # ------------------------------------------------------------------------
    # Resolve project configuration
    # ------------------------------------------------------------------------

    $project = Get-OGSProject

    if ($null -eq $project) {
        throw "Unable to load the OGS project configuration."
    }

    if (-not ($project -is [System.Collections.IDictionary])) {
        throw "Invalid OGS project configuration type: $($project.GetType().FullName)"
    }

    if (-not $project.Contains('toolkit')) {
        throw "OGS project configuration does not contain the 'toolkit' section."
    }

    $toolkit = $project['toolkit']

    if ($null -eq $toolkit) {
        throw "OGS project 'toolkit' configuration is null."
    }

    if (-not ($toolkit -is [System.Collections.IDictionary])) {
        throw "Invalid OGS toolkit configuration type: $($toolkit.GetType().FullName)"
    }

    if (-not $toolkit.Contains('asset_directory')) {
        throw "OGS toolkit configuration does not define 'asset_directory'."
    }

    $assetDirectory = [string]$toolkit['asset_directory']

    if ([string]::IsNullOrWhiteSpace($assetDirectory)) {
        throw "OGS toolkit 'asset_directory' cannot be empty."
    }

    # ------------------------------------------------------------------------
    # Resolve asset root
    # ------------------------------------------------------------------------

    $projectRoot = Get-OGSProjectRoot

    $assetRoot = Join-Path `
        $projectRoot `
        $assetDirectory

    if (-not (Test-Path -LiteralPath $assetRoot -PathType Container)) {
        throw "Template asset directory does not exist: $assetRoot"
    }

    # ------------------------------------------------------------------------
    # Resolve requested asset
    # ------------------------------------------------------------------------

    $assetPath = Join-Path `
        $assetRoot `
        $RelativePath

    if (-not (Test-Path -LiteralPath $assetPath -PathType Leaf)) {
        throw @"
Template asset was not found.

Relative path:
$RelativePath

Expected:
$assetPath
"@
    }

    return (Resolve-Path -LiteralPath $assetPath).Path
}


# ============================================================================
# Read Template
# ============================================================================

function Read-Template {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Name

    )

    if ([string]::IsNullOrWhiteSpace($Name)) {

        throw "Template name cannot be empty or whitespace."

    }

    $templateFile = Resolve-TemplatePath -Name $Name

    try {

        $content = Get-Content `
            -LiteralPath $templateFile `
            -Raw

        $template = $content | ConvertFrom-Yaml

    }
    catch {

        throw @"
Unable to read template.

Template:
$templateFile

Reason:
$($_.Exception.Message)
"@

    }

    if ($null -eq $template) {

        throw @"
Template '$Name' is empty.
"@

    }

    return $template

}
# ============================================================================
# Validate Template
# ============================================================================

function Validate-Template {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [hashtable]$Template

    )

    # ------------------------------------------------------------------------
    # Required Properties
    # ------------------------------------------------------------------------

    $requiredProperties = @(
        'version'
        'name'
        'description'
        'directories'
        'files'
    )

    foreach ($property in $requiredProperties) {

        if (-not $Template.ContainsKey($property)) {

            throw @"
Template is missing the required property:

    $property
"@

        }

    }

    # ------------------------------------------------------------------------
    # Version Validation
    # ------------------------------------------------------------------------

    try {

        $templateVersion = [Version]([string]$Template.version)

    }
    catch {

        throw @"
Invalid template version.

Found:

    $($Template.version)
"@

    }

    if ($templateVersion -ne $script:SupportedTemplateVersion) {

        throw @"
Unsupported template version.

Supported:

    $script:SupportedTemplateVersion

Found:

    $templateVersion
"@

    }

    # ------------------------------------------------------------------------
    # Name
    # ------------------------------------------------------------------------

    if ([string]::IsNullOrWhiteSpace([string]$Template.name)) {

        throw "Template name cannot be empty."

    }

    # ------------------------------------------------------------------------
    # Description
    # ------------------------------------------------------------------------

    if ([string]::IsNullOrWhiteSpace([string]$Template.description)) {

        throw "Template description cannot be empty."

    }

    # ------------------------------------------------------------------------
    # Directories
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
# Directories
# ------------------------------------------------------------------------

if ($Template.directories.Count -eq 0) {

    throw "Template must define at least one directory."

}

$directorySet = New-Object 'System.Collections.Generic.HashSet[string]'

$directoryIndex = 0

foreach ($directory in $Template.directories) {

    $directoryIndex++

    if ($null -eq $directory) {

        throw @"
Directory definition #$directoryIndex is null.
"@

    }

    $directory = [string]$directory

    if ([string]::IsNullOrWhiteSpace($directory)) {

        throw @"
Directory definition #$directoryIndex is empty.
"@

    }

    if ($directory -ne $directory.Trim()) {

        throw @"
Directory definition #$directoryIndex contains leading or trailing whitespace.

Value:

    '$directory'
"@

    }

    if (-not $directorySet.Add($directory)) {

        throw @"
Duplicate directory definition found.

Directory:

    $directory
"@

    }

}

    # ------------------------------------------------------------------------
    # Files
    # ------------------------------------------------------------------------

    if ($Template.files.Count -eq 0) {

        throw "Template must define at least one file."

    }


    # ------------------------------------------------------------------------
# File Definitions
# ------------------------------------------------------------------------

$fileIndex = 0

foreach ($file in $Template.files) {

    $fileIndex++

    if ($null -eq $file) {

        throw @"
File definition #$fileIndex is null.
"@

    }

    if (-not ($file -is [hashtable])) {

        throw @"
File definition #$fileIndex must be a hashtable.
"@

    }

    foreach ($property in @('source', 'destination')) {

        if (-not $file.ContainsKey($property)) {

            throw @"
File definition #$fileIndex is missing the required property:

    $property
"@

        }

        if ([string]::IsNullOrWhiteSpace([string]$file[$property])) {

            throw @"
File definition #$fileIndex contains an empty value:

    $property
"@

        }

    }

}
    return $true

}

# ============================================================================
# Normalize Template
# ============================================================================

function Normalize-Template {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [hashtable]$Template

    )

    $normalized = @{

    version     = [Version]([string]$Template.version)

    name        = ([string]$Template.name).Trim()

    description = ([string]$Template.description).Trim()

    directories = @()

    files       = @()

    }

    # ------------------------------------------------------------------------
    # Directories
    # ------------------------------------------------------------------------

    foreach ($directory in $Template.directories) {

        $normalizedDirectory = ([string]$directory).Trim()

        $normalizedDirectory = $normalizedDirectory.Replace('/', [IO.Path]::DirectorySeparatorChar)

        $normalized.directories += $normalizedDirectory

    }

    # ------------------------------------------------------------------------
    # Files
    # ------------------------------------------------------------------------

    foreach ($file in $Template.files) {

        $normalized.files += @{

            source = ([string]$file.source).Trim().Replace('/', [IO.Path]::DirectorySeparatorChar)

            destination = ([string]$file.destination).Trim().Replace('/', [IO.Path]::DirectorySeparatorChar)

        }

    }

    return $normalized

}

# ============================================================================
# Get Template Cache Key
# ============================================================================


# ============================================================================
# New Template Cache Key
# ============================================================================

function New-TemplateCacheKey {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Name

    )

    if ([string]::IsNullOrWhiteSpace($Name)) {

        throw "Template name cannot be empty."

    }

    return $Name.Trim().ToLowerInvariant()

}
# ============================================================================
# Get OGS Template
# ============================================================================

function Get-OGSTemplate {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Name

    )

    if ([string]::IsNullOrWhiteSpace($Name)) {

        throw "Template name cannot be empty."

    }

    # ------------------------------------------------------------------------
    # Cache Lookup
    # ------------------------------------------------------------------------

    $cacheKey = New-TemplateCacheKey -Name $Name

    if ($script:TemplateCache.ContainsKey($cacheKey)) {

        return $script:TemplateCache[$cacheKey]

    }

    # ------------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------------

    $template = Read-Template -Name $Name

    # ------------------------------------------------------------------------
    # Validate
    # ------------------------------------------------------------------------

    Validate-Template -Template $template | Out-Null

    # ------------------------------------------------------------------------
    # Normalize
    # ------------------------------------------------------------------------

    $template = Normalize-Template -Template $template

    # ------------------------------------------------------------------------
    # Cache
    # ------------------------------------------------------------------------

    $script:TemplateCache[$cacheKey] = $template

    return $template

}
# ============================================================================
# Get Available Templates
# ============================================================================

function Get-AvailableTemplates {

    [CmdletBinding()]
    param()

    $project = Get-OGSProject

    $definitionDirectory = Join-Path `
        (Get-OGSProjectRoot) `
        $project.toolkit.definition_directory

    if (-not (Test-Path -LiteralPath $definitionDirectory)) {

        throw @"
Template definition directory does not exist.

$definitionDirectory
"@

    }

    Get-ChildItem `
        -LiteralPath $definitionDirectory `
        -Filter '*.yaml' `
        -File |
    Sort-Object Name |
    ForEach-Object {

        $_.BaseName

    }

}

# ============================================================================
# Test OGS Template
# ============================================================================

function Test-OGSTemplate {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Name

    )

    if ([string]::IsNullOrWhiteSpace($Name)) {

        return $false

    }

    try {

        $null = Get-OGSTemplate -Name $Name

        return $true

    }
    catch {

        return $false

    }

}

# ============================================================================
# Clear OGS Template Cache
# ============================================================================

function Clear-OGSTemplateCache {

    [CmdletBinding(SupportsShouldProcess = $true)]
    param()

    if ($PSCmdlet.ShouldProcess("Template Cache", "Clear")) {

        $script:TemplateCache.Clear()

    }

}

# ============================================================================
# Public API
# ============================================================================

Export-ModuleMember -Function @(
    'Get-AvailableTemplates',
    'Get-OGSTemplate',
    'Test-OGSTemplate',
    'Clear-OGSTemplateCache',
    'Resolve-TemplateAsset'
)