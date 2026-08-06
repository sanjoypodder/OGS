$ErrorActionPreference = 'Stop'

$modulePath = Join-Path `
    $PSScriptRoot `
    '..\lib\GenerationValidator.psm1'

$modulePath = [System.IO.Path]::GetFullPath($modulePath)

Remove-Module `
    GenerationValidator `
    -Force `
    -ErrorAction SilentlyContinue

Import-Module `
    $modulePath `
    -Force


Describe 'GenerationValidator' {

    Context 'Module API' {

        It 'exports the expected validator functions' {

            $commands = @(
                Get-Command `
                    -Module GenerationValidator |
                    Select-Object -ExpandProperty Name
            )

            ($commands -contains 'Get-OGSGenerationValidatorVersion') |
                Should Be $true

            ($commands -contains 'Test-OGSGeneratedContent') |
                Should Be $true

            ($commands -contains 'Test-OGSGeneratedFile') |
                Should Be $true

            ($commands -contains 'Assert-OGSGeneratedFile') |
                Should Be $true
        }


        It 'reports validator version 1.0.0' {

            Get-OGSGenerationValidatorVersion |
                Should Be '1.0.0'
        }
    }


    Context 'Generated content validation' {

        It 'accepts valid Python content' {

            $content = @"
from dataclasses import dataclass


@dataclass
class Example:
    value: int
"@

            Test-OGSGeneratedContent `
                -Content $content |
                Should Be $true
        }


        It 'rejects PowerShell here-string opening markers' {

            $content = @"
@'
print("bad template")
"@

            Test-OGSGeneratedContent `
                -Content $content |
                Should Be $false
        }


        It 'rejects leaked Set-Content commands' {

            $content = @"
print("bad template")
'@ | Set-Content example.py
"@

            Test-OGSGeneratedContent `
                -Content $content |
                Should Be $false
        }


        It 'rejects leaked Encoding UTF8 commands' {

            $content = @"
print("bad template")
-Encoding UTF8
"@

            Test-OGSGeneratedContent `
                -Content $content |
                Should Be $false
        }
    }


    Context 'Generated file validation' {

        BeforeEach {

            $script:testFile = Join-Path `
                $TestDrive `
                'generated.py'
        }


        It 'accepts a valid generated file' {

            @"
print("valid")
"@ |
                Set-Content `
                    -LiteralPath $script:testFile `
                    -Encoding UTF8

            Test-OGSGeneratedFile `
                -Path $script:testFile |
                Should Be $true
        }


        It 'rejects a contaminated generated file' {

            @"
@'
print("invalid")
'@ | Set-Content example.py
"@ |
                Set-Content `
                    -LiteralPath $script:testFile `
                    -Encoding UTF8

            Test-OGSGeneratedFile `
                -Path $script:testFile |
                Should Be $false
        }
    }


    Context 'Generated file assertion' {

        BeforeEach {

            $script:testFile = Join-Path `
                $TestDrive `
                'assert-generated.py'
        }


        It 'does not throw for a valid generated file' {

            @"
print("valid")
"@ |
                Set-Content `
                    -LiteralPath $script:testFile `
                    -Encoding UTF8

            {
                Assert-OGSGeneratedFile `
                    -Path $script:testFile
            } |
                Should Not Throw
        }


        It 'throws for a contaminated generated file' {

    $contaminatedContent = @(
        "@'",
        'print("invalid")',
        "'@ | Set-Content example.py"
    )

    $contaminatedContent |
        Set-Content `
            -LiteralPath $script:testFile `
            -Encoding UTF8

    $caughtException = $null

    try {

        Assert-OGSGeneratedFile `
            -Path $script:testFile

    }
    catch {

        $caughtException = $_
    }

    ($null -ne $caughtException) |
        Should Be $true

    $caughtException.Exception.Message |
        Should Match 'Generated file validation failed'
}
    }
}