# Script de Lanzamiento para "Gestión y Seguimiento de Ofertas a Clientes"

$ErrorActionPreference = "Stop" # Detener la ejecución en caso de error

try {
    Write-Host "Iniciando configuración del entorno para 'Gestión y Seguimiento de Ofertas a Clientes'..." -ForegroundColor Green

    # 1. Configurar PYTHONPATH
    $currentDir = Get-Location
    $env:PYTHONPATH = "$currentDir;$currentDir\src"
    Write-Host "PYTHONPATH configurado a: $($env:PYTHONPATH)" -ForegroundColor Cyan

    # 2. Definir rutas
    $venvPath = Join-Path $currentDir ".venv"
    $pythonExecutable = "python.exe" # Asumimos que Python está en el PATH o en el venv
    $mainScript = "src/app/tenants/mudanzas_tres_cantos/agent.py"
    $activateScript = Join-Path $venvPath "Scripts" "Activate.ps1"
    $requirementsFile = Join-Path $currentDir "requirements.txt"

    # 3. Crear o activar entorno virtual
    if (-not (Test-Path $venvPath)) {
        Write-Host "Creando entorno virtual en '$venvPath'..." -ForegroundColor Yellow
        & $pythonExecutable -m venv $venvPath
    }

    Write-Host "Activando entorno virtual..." -ForegroundColor Green
    . $activateScript

    # 4. Instalar dependencias
    Write-Host "Actualizando pip e instalando dependencias desde '$requirementsFile'..." -ForegroundColor Green
    pip install --upgrade pip
    pip install -r $requirementsFile

    # 5. Ejecutar el script principal
    Write-Host "Ejecutando el agente '$mainScript'..." -ForegroundColor Green
    & $pythonExecutable $mainScript

    Write-Host "`nEl agente se ejecutó exitosamente." -ForegroundColor Green

}
catch {
    Write-Host "`nERROR: Ha ocurrido un problema durante la ejecución." -ForegroundColor Red
    Write-Host "Detalles del error: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Trace: $($_.ScriptStackTrace)" -ForegroundColor Red
}
finally {
    Write-Host "`nPresione cualquier tecla para continuar o cerrar la ventana..." -ForegroundColor DarkGray
    $null = Read-Host
}