param(
    [string]$AULA = ""
)

$CONFIG_FILE = "config.txt"

function Get-AulaFromConfig {
    if (Test-Path $CONFIG_FILE) {
        $line = Get-Content $CONFIG_FILE | Where-Object { $_ -match "^AULA=" }
        if ($line) {
            return ($line -split "=")[1].Trim()
        }
    }
    return $null
}

if ([string]::IsNullOrEmpty($AULA)) {
    $AULA = Get-AulaFromConfig
    if ([string]::IsNullOrEmpty($AULA)) {
        Write-Host "❌ Erro: AULA não definida em $CONFIG_FILE" -ForegroundColor Red
        Write-Host "Use: .\build.ps1 -AULA docker_tutorial (ou outra aula)" -ForegroundColor Yellow
        exit 1
    }
}

if (-not (Test-Path $AULA)) {
    Write-Host "❌ Erro: Pasta $AULA não encontrada!" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path "$AULA\$AULA.tex")) {
    Write-Host "❌ Erro: Arquivo $AULA\$AULA.tex não encontrado!" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path "main.tex")) {
    Write-Host "❌ Erro: Arquivo main.tex não encontrado!" -ForegroundColor Red
    exit 1
}

Write-Host "📚 Compilando $AULA usando main.tex..." -ForegroundColor Cyan
Write-Host ""

$content = Get-Content "main.tex" -Raw
$content = $content -replace '\\def\\aulanum\{[^}]+\}', "\\def\aulanum{$AULA}"

$tempFile = "main_temp.tex"
$content | Set-Content $tempFile

Write-Host "Compilando main.tex..." -ForegroundColor Yellow

$process = Start-Process -FilePath "pdflatex" -ArgumentList "-interaction=nonstopmode", "-jobname=main", $tempFile -Wait -PassThru -NoNewWindow

if (-not (Test-Path "main.pdf")) {
    Write-Host "❌ Erro na primeira compilação - PDF não foi gerado!" -ForegroundColor Red
    Remove-Item $tempFile -ErrorAction SilentlyContinue
    exit 1
}

for ($pass = 2; $pass -le 6; $pass++) {
    Write-Host "Compilando main.tex (passagem $pass/6)..." -ForegroundColor Yellow
    $process = Start-Process -FilePath "pdflatex" -ArgumentList "-interaction=nonstopmode", "-jobname=main", $tempFile -Wait -PassThru -NoNewWindow
    
    if (Test-Path "main.log") {
        $logContent = Get-Content "main.log" -Raw
        if ($logContent -notmatch "LaTeX Warning.*Reference.*undefined") {
            Write-Host "Todas as referências foram resolvidas na passagem $pass" -ForegroundColor Green
            break
        }
    }
}

Remove-Item $tempFile -ErrorAction SilentlyContinue

if (Test-Path "main.pdf") {
    Write-Host ""
    Write-Host "✅ Compilação bem-sucedida!" -ForegroundColor Green
    Write-Host "📄 Arquivo gerado: $(Resolve-Path main.pdf)" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "❌ Erro: PDF não foi gerado!" -ForegroundColor Red
    exit 1
}
