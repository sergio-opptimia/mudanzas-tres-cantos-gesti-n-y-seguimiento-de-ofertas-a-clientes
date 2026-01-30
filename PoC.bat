@echo off
setlocal

:: Configuración
set VENV_PATH=.venv
set PYTHON_EXE=python
set SCRIPT_TO_RUN=src/app/tenants/mudanzas_tres_cantos/agent.py

echo Iniciando configuración del entorno para "Gestión y Seguimiento de Ofertas a Clientes"...

:: 1. Crear y activar entorno virtual
if not exist %VENV_PATH% (
    echo Creando entorno virtual en %VENV_PATH%...
    %PYTHON_EXE% -m venv %VENV_PATH%
    if errorlevel 1 (
        echo Error: No se pudo crear el entorno virtual. Asegúrese de que Python esté instalado y en el PATH.
        goto :end
    )
)

echo Activando entorno virtual...
call %VENV_PATH%\Scripts\activate.bat
if errorlevel 1 (
    echo Error: No se pudo activar el entorno virtual.
    goto :end
)

:: 2. Instalar dependencias
echo Instalando dependencias desde requirements.txt...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: No se pudieron instalar las dependencias.
    goto :end
)

:: 3. Configurar PYTHONPATH
echo Configurando PYTHONPATH...
set "PYTHONPATH=%CD%;%CD%\src"
echo PYTHONPATH establecido a: %PYTHONPATH%

:: 4. Ejecutar el script principal
echo Ejecutando el agente...
%PYTHON_EXE% %SCRIPT_TO_RUN%
if errorlevel 1 (
    echo Error: El agente terminó con errores.
    goto :end
)

echo El agente se ejecutó exitosamente.

:end
echo.
echo Presione cualquier tecla para finalizar...
pause >nul
endlocal