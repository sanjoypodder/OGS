<#
.SYNOPSIS
Creates a new OGS module from a template.

.DESCRIPTION
Reads a template definition and generates the required
directory structure and files for a new module.
#>

[CmdletBinding(SupportsShouldProcess = $true)]
param(

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$Name,

    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$Template

)

Set-StrictMode -Version Latest

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $PSCommandPath
$libraryRoot = Join-Path $scriptRoot 'lib'

Import-Module (Join-Path $libraryRoot 'ProjectReader.psm1') -Force
Import-Module (Join-Path $libraryRoot 'TemplateLoader.psm1') -Force
Import-Module (Join-Path $libraryRoot 'TemplateRenderer.psm1') -Force
Import-Module (Join-Path $libraryRoot 'GenerationValidator.psm1') -Force

# ============================================================================
# Controller Context
# ============================================================================

$script:Context = @{

    ProjectRoot = $null

    Project = $null

    ProjectInfo = $null

    TemplateName = $null

    Template = $null

    ModuleName = $null

    TokenContext = $null

    Tokens = $null

    GenerationPlan = $null

    ExecutionPlan = $null

}
# ============================================================================
# Initialize
# ============================================================================

function Initialize {

    [CmdletBinding()]
    param()

    Write-Verbose "Initializing OGS Module Generator..."

    $script:Context.ModuleName = $Name.Trim()

    $script:Context.TemplateName = $Template.Trim()

}

# ============================================================================
# Validate Environment
# ============================================================================

function ValidateEnvironment {

    [CmdletBinding()]
    param()

    Write-Verbose "Validating environment..."

    if (-not (Test-OGSProject)) {

        throw "Current directory is not an OGS project."

    }

    if (-not (Test-OGSTemplate -Name $script:Context.TemplateName)) {

        throw "Template '$($script:Context.TemplateName)' was not found."

    }

}

# ============================================================================
# Load Project
# ============================================================================

function LoadProject {

    [CmdletBinding()]
    param()

    Write-Verbose "Loading project..."

    $script:Context.ProjectRoot = Get-OGSProjectRoot
    $script:Context.Project     = Get-OGSProject
    $script:Context.ProjectInfo = $script:Context.Project['project']

}

# ============================================================================
# Load Template
# ============================================================================

function LoadTemplate {

    [CmdletBinding()]
    param()

    Write-Verbose "Loading template..."

    $script:Context.Template = Get-OGSTemplate `
        -Name $script:Context.TemplateName

}
# ============================================================================
# Build Template Token Context
# ============================================================================

function BuildTokenContext {

    [CmdletBinding()]
    param()

    Write-Verbose "Building template token context..."

    $projectInfo = $script:Context.ProjectInfo

    if ($null -eq $projectInfo) {

        throw "Project information has not been loaded."

    }

    $script:Context.TokenContext = New-OGSTokenContext `
        -ProjectName ([string]$projectInfo['name']) `
        -ProjectVersion ([string]$projectInfo['version']) `
        -ProjectShortName ([string]$projectInfo['short_name']) `
        -Organization ([string]$projectInfo['organization']) `
        -Codename ([string]$projectInfo['codename']) `
        -ModuleName $script:Context.ModuleName

    $script:Context.Tokens = Get-OGSTemplateTokens `
        -Context $script:Context.TokenContext

    Write-Verbose "Template token context built successfully."

}
# ============================================================================
# Build Generation Plan
# ============================================================================

function BuildGenerationPlan {

    [CmdletBinding()]
    param()

    Write-Verbose "Building generation plan..."

    $operations = @()

    # ----------------------------------------------------------
    # Directories
    # ----------------------------------------------------------

    foreach ($directory in $script:Context.Template.directories) {

        $operations += @{

            Type = 'CreateDirectory'

            Path = $directory

        }

    }

    # ----------------------------------------------------------
    # Files
    # ----------------------------------------------------------

    foreach ($file in $script:Context.Template.files) {

    $source = [string]$file.source
    $destination = [string]$file.destination

    if ([string]::IsNullOrWhiteSpace($source)) {

        throw "Template definition contains a file with an empty source."

    }

    if ([string]::IsNullOrWhiteSpace($destination)) {

        throw "Template definition contains a file with an empty destination."

    }

    $operations += @{

        Type = 'RenderFile'

        Source = $source

        Destination = $destination

    }

}

    $script:Context.GenerationPlan = @{

        Operations = $operations

    }

}

# ============================================================================
# Show Generation Plan
# ============================================================================

# ============================================================================
# Show Generation Plan
# ============================================================================

function ShowGenerationPlan {

    [CmdletBinding()]
    param()

    Write-Host ""

    Write-Host "Generation Plan"

    Write-Host "----------------"

    Write-Host ""

    foreach ($operation in $script:Context.GenerationPlan.Operations) {

        switch ($operation.Type) {

            'CreateDirectory' {

                Write-Host ("[DIR ] {0}" -f $operation.Path)

            }

            'RenderFile' {

                Write-Host (
                    "[FILE] {0}" -f $operation.Destination
            )

            }

        }

    }

    Write-Host ""

}

# ============================================================================
# Build Execution Plan
# ============================================================================

function BuildExecutionPlan {

    [CmdletBinding()]
    param()

    Write-Verbose "Building execution plan..."

    if ($null -eq $script:Context.GenerationPlan) {

        throw "Generation plan has not been built."

    }

    $executionOperations = @()

    foreach ($operation in $script:Context.GenerationPlan.Operations) {

        switch ($operation.Type) {

            'CreateDirectory' {

                $fullPath = Join-Path `
                    $script:Context.ProjectRoot `
                    $operation.Path

                $executionOperations += @{

                    Type = 'CreateDirectory'

                    RelativePath = $operation.Path

                    FullPath = $fullPath

                    Exists = Test-Path -LiteralPath $fullPath

                }

            }

            'RenderFile' {

                $source = [string]$operation.Source

                $destination = Join-Path `
                    $script:Context.ProjectRoot `
                    ([string]$operation.Destination)

                Write-Verbose (
                    "Resolving template asset: {0}" -f $source
                )

                $assetPath = Resolve-TemplateAsset `
                    -RelativePath $source

                Write-Verbose (
                    "Rendering template asset: {0}" -f $source
                )

                $renderedContent = Invoke-OGSTemplateRender `
                    -TemplatePath $assetPath `
                    -Tokens $script:Context.Tokens

                $executionOperations += @{

                    Type = 'WriteFile'

                    Source = $source

                    AssetPath = $assetPath

                    Path = $destination

                    Content = $renderedContent

                }

            }

            default {

                throw (
                    "Unsupported generation operation type: {0}" -f `
                    $operation.Type
                )

            }

        }

    }

    $script:Context.ExecutionPlan = @{

        Operations = $executionOperations

    }

}
# ============================================================================
# Show Execution Plan
# ============================================================================

function ShowExecutionPlan {

    [CmdletBinding()]
    param()

    if ($null -eq $script:Context.ExecutionPlan) {

        throw "Execution plan has not been built."

    }

    Write-Host ""

    Write-Host "Execution Plan"

    Write-Host "--------------"

    Write-Host ""

    foreach ($operation in $script:Context.ExecutionPlan.Operations) {

        switch ($operation.Type) {

            'CreateDirectory' {

                Write-Host ("[DIR ] {0}" -f $operation.FullPath)

            }

            'WriteFile' {

            Write-Host (
                "[WRITE FILE] {0}" -f $operation.Path
            )

            }

        }

    }

    Write-Host ""

}

# ============================================================================
# Execute Create Directory
# ============================================================================

function ExecuteCreateDirectory {

    [CmdletBinding()]
    param(

        [Parameter(Mandatory)]
        [PSCustomObject]$Operation

    )

    if ($Operation.Exists) {

        Write-Verbose ("Directory already exists: {0}" -f $Operation.FullPath)

        return

    }

    Write-Host ("[CREATE DIR ] {0}" -f $Operation.FullPath)

    New-Item `
        -ItemType Directory `
        -Path $Operation.FullPath `
        -Force | Out-Null

}
# ============================================================================
# Execute Copy File
# ============================================================================

# ============================================================================
# Execute Write File
# ============================================================================

function ExecuteWriteFile {

    [CmdletBinding(SupportsShouldProcess = $true)]
    param(

        [Parameter(Mandatory)]
        [ValidateNotNull()]
        $Operation

    )

    $path = [string]$Operation.Path
    $content = [string]$Operation.Content

    if ([string]::IsNullOrWhiteSpace($path)) {

        throw "WriteFile operation contains an empty destination path."

    }

    $parentDirectory = Split-Path `
        -Parent $path

    if (
        -not [string]::IsNullOrWhiteSpace($parentDirectory) -and
        -not (Test-Path -LiteralPath $parentDirectory)
    ) {

        if ($PSCmdlet.ShouldProcess(
            $parentDirectory,
            "Create parent directory"
        )) {

            New-Item `
                -ItemType Directory `
                -Path $parentDirectory `
                -Force `
                -ErrorAction Stop |
                Out-Null

        }

    }

    if (Test-Path -LiteralPath $path) {

    $overwriteExisting = $false

    if (
        $null -ne $script:Context.Project.generator -and
        $null -ne $script:Context.Project.generator.overwrite_existing
    ) {

        $overwriteExisting = [bool](
            $script:Context.Project.generator.overwrite_existing
        )

    }

    if (-not $overwriteExisting) {

        if ($WhatIfPreference) {

            Write-Host (
                "[SKIP EXISTING] {0}" -f $path
            )

            return

        }

        throw "Destination file already exists: $path"

    }

}   
        Write-Verbose (
        "Validating rendered content before write: {0}" -f $path
    )

    if (-not (Test-OGSGeneratedContent -Content $content)) {

        throw (
            "Generated content validation failed before write: {0}" -f $path
        )

    }

    Write-Verbose (
        "Rendered content validation passed: {0}" -f $path
    )

    if ($PSCmdlet.ShouldProcess(
        $path,
        "Write rendered template file"
    )) {

        Write-Host (
            "[WRITE FILE] {0}" -f $path
        )

        Set-Content `
            -LiteralPath $path `
            -Value $content `
            -Encoding UTF8 `
            -NoNewline `
            -ErrorAction Stop

    }

}
# ============================================================================
# Execute Generation Plan
# ============================================================================

function ExecuteGenerationPlan {

    [CmdletBinding()]
    param()

    Write-Verbose "Executing generation plan..."

    foreach ($operation in $script:Context.ExecutionPlan.Operations) {

        switch ($operation.Type) {

            'CreateDirectory' {

                ExecuteCreateDirectory `
                    -Operation $operation

            }

            'WriteFile' {

                ExecuteWriteFile `
                    -Operation $operation `
                    -WhatIf:$WhatIfPreference

            }

        }

    }

}

# ============================================================================
# Main
# ============================================================================

function Main {

    [CmdletBinding()]
    param()

    Initialize

    ValidateEnvironment

    LoadProject


    LoadTemplate
    BuildTokenContext


    BuildGenerationPlan

    ShowGenerationPlan
    BuildExecutionPlan

    ShowExecutionPlan
    ExecuteGenerationPlan

    Write-Host ""

    Write-Host "============================================="
    Write-Host "      OGS Module Generator"
    Write-Host "============================================="
    Write-Host ""

    Write-Host ("Project      : {0}" -f $script:Context.ProjectInfo['name'])

    Write-Host ("Organization : {0}" -f $script:Context.ProjectInfo['organization'])

    Write-Host ("Template     : {0}" -f $script:Context.TemplateName)

    Write-Host ("Module       : {0}" -f $script:Context.ModuleName)

    Write-Host ""

    Write-Host "Initialization completed successfully."

}

# Entry Point
# ============================================================================

try {

    Main

}
catch {

    Write-Error $_

    exit 1

}