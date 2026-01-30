# Gestión y Seguimiento de Ofertas a Clientes - Opptimia AI Factory

## 🚀 Resumen del Proyecto
Este proyecto tiene como objetivo desarrollar un sistema de agente de IA para "Mudanzas Tres Cantos" que permita la gestión integral y el seguimiento automatizado de ofertas a clientes. Desde la creación de la oferta hasta la interacción y el cierre, el sistema está diseñado para optimizar la eficiencia del proceso de cotización, asegurando al mismo tiempo el cumplimiento estricto de las políticas de la empresa en cuanto a la redacción de PII (Información de Identificación Personal) y la necesidad de aprobación humana en puntos clave.

## ✨ Características Principales
*   **Gestión Integral de Ofertas**: Creación, edición y almacenamiento de ofertas a clientes.
*   **Seguimiento Automatizado**: Monitoreo proactivo del estado de las ofertas y recordatorios.
*   **Interacción con Clientes**: Capacidad del agente para comunicarse o generar borradores de comunicación.
*   **Cumplimiento de PII**: Integración de mecanismos para asegurar la redacción adecuada y la protección de datos personales.
*   **Flujos de Aprobación Humana**: Puntos de control donde se requiere la intervención y aprobación de un humano.
*   **Estructura Monorepo**: Organización de código que facilita la gestión de múltiples servicios o componentes.

## 🛠️ Stack Tecnológico
*   **Lenguaje**: Python
*   **Configuración**: YAML
*   **Arquitectura**: Estructura Monorepo
*   **Framework de Agentes**: LangChain (con integraciones de Google AI)

## 📂 Estructura del Proyecto
Este proyecto sigue una estructura monorepo, con configuraciones y lógica de negocio específicas para cada inquilino ('tenant').

```
.responsory/                 # Archivos de la fábrica Opptimia AI
├── configs/
│   └── tenants/
│       └── mudanzas_tres_cantos/
│           ├── dev.yaml       # Configuración específica para desarrollo
│           └── prod.yaml      # Configuración específica para producción
├── src/
│   ├── __init__.py
│   └── app/
│       ├── __init__.py
│       └── tenants/
│           ├── __init__.py
│           └── mudanzas_tres_cantos/
│               ├── __init__.py
│               ├── tools.py   # Herramientas y funciones auxiliares para el agente
│               └── agent.py   # Lógica principal del agente de IA
├── infra/
│   └── tenants/
│       └── mudanzas_tres_cantos/
│           └── variables.tf # Variables de Terraform para infraestructura (si aplica)
├── README.md                # Este archivo
├── requirements.txt         # Dependencias del proyecto
├── deployment_notes.md      # Notas breves para el despliegue
├── PoC.bat                  # Script de lanzamiento para Windows (CMD)
└── run_project.ps1          # Script de lanzamiento para Windows (PowerShell)
```

## 🚀 Guía de Inicio Rápido

### Prerrequisitos
*   Python 3.9 o superior
*   Conexión a internet para descargar dependencias

### Instalación y Ejecución
Para simplificar la configuración y ejecución, se proporcionan scripts automatizados:

#### Para usuarios de Windows (PowerShell - Recomendado)
1.  Abre PowerShell.
2.  Navega a la raíz del proyecto.
3.  Ejecuta el script de PowerShell:
    ```powershell
    .\run_project.ps1
    ```

#### Para usuarios de Windows (CMD)
1.  Abre la línea de comandos (CMD).
2.  Navega a la raíz del proyecto.
3.  Ejecuta el script batch:
    ```bash
    .\PoC.bat
    ```

Estos scripts se encargarán de:
1.  Crear o activar un entorno virtual (`.venv`).
2.  Instalar todas las dependencias listadas en `requirements.txt`.
3.  Configurar la variable de entorno `PYTHONPATH`.
4.  Lanzar el agente de IA (`src/app/tenants/mudanzas_tres_cantos/agent.py`).

## ⚙️ Configuración
Las configuraciones específicas para desarrollo y producción se encuentran en `configs/tenants/mudanzas_tres_cantos/dev.yaml` y `configs/tenants/mudanzas_tres_cantos/prod.yaml` respectivamente. Asegúrese de revisar y ajustar estos archivos según sea necesario. Es posible que también necesite configurar variables de entorno (ej. claves de API) en un archivo `.env` en la raíz del proyecto o directamente en su sistema.

## 🤝 Soporte y Contacto
Para cualquier consulta o problema, contacte al equipo de Opptimia AI Factory.