param([switch]$CompareBaseline)
$ErrorActionPreference = 'Stop'
$taskWorkspace = Split-Path -Parent $PSScriptRoot
$taskReportRoot = Join-Path $taskWorkspace 'Report template'
$taskCompiler = Join-Path $PSScriptRoot 'tools/tectonic/tectonic.exe'
$taskVerifier = Join-Path $PSScriptRoot 'setup.py'
$taskBootstrap = Join-Path $PSScriptRoot 'bootstrap.py'
$env:TECTONIC_CACHE_DIR = Join-Path $PSScriptRoot 'cache/tectonic'
if ($CompareBaseline) {
    & python $taskBootstrap --pdf
} else {
    & python $taskBootstrap
}
if ($LASTEXITCODE -ne 0) { throw 'Workspace tool bootstrap failed.' }
& python $taskVerifier freeze
if ($LASTEXITCODE -ne 0) { throw 'Source verification failed; compilation stopped.' }
Push-Location -LiteralPath $taskReportRoot
try {
    New-Item -ItemType Directory -Path 'build' -Force | Out-Null
    & $taskCompiler 'main.tex' --outdir 'build' --keep-intermediates --keep-logs --untrusted --color never
    if ($LASTEXITCODE -ne 0) { throw 'LaTeX compilation failed; inspect build/main.log.' }
    Copy-Item -LiteralPath 'build/main.pdf' -Destination 'main.pdf' -Force
    if ($CompareBaseline) {
        & python $taskVerifier compare
        if ($LASTEXITCODE -ne 0) { throw 'Baseline comparison failed; inspect .phase2/verification/comparison.json.' }
    }
} finally {
    Pop-Location
}
