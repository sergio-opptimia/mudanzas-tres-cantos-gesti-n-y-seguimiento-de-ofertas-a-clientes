import logging
from typing import Dict, Any, List, Callable

from google.adk.agents.llm_agent import Agent
from google.adk.goal import Goal
from google.adk.persona import Persona
from langchain_google_genai import ChatGoogleGenerativeAI

from src.app.tenants.mudanzas_tres_cantos.tools import create_offer, validate_pii

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MudanzasTresCantosAgent(Agent):
    """
    Agente de IA para Mudanzas Tres Cantos.

    Este agente está diseñado para gestionar el ciclo de vida completo de las ofertas a clientes,
    desde su creación y seguimiento hasta el cierre. Asegura el cumplimiento de las políticas
    de PII (Información de Identificación Personal) y requiere aprobación humana cuando es necesario.

    Atributos:
        config (Dict[str, Any]): Diccionario de configuración inyectado que contiene
                                 parámetros para el LLM y otras configuraciones específicas del agente.
        llm (ChatGoogleGenerativeAI): Instancia del modelo de lenguaje grande (LLM) utilizado por el agente.
    """
    config: Dict[str, Any]
    llm: ChatGoogleGenerativeAI
    
    def __init__(self, config: Dict[str, Any]):
        """
        Inicializa el agente de Mudanzas Tres Cantos.

        Configura el objetivo, la persona, las herramientas disponibles y el modelo LLM
        utilizando la configuración proporcionada.

        Args:
            config (Dict[str, Any]): Diccionario de configuración que debe contener:
                                     - 'llm': dict con 'model_name' (str) y 'temperature' (float).
                                     Ejemplo:
                                     {
                                         "llm": {
                                             "model_name": "gemini-pro",
                                             "temperature": 0.7
                                         }
                                     }
        Raises:
            ValueError: Si la configuración esencial para el LLM no está presente.
        """
        if "llm" not in config or "model_name" not in config["llm"] or "temperature" not in config["llm"]:
            logging.error({"event": "AgentInitializationError", "message": "Missing LLM configuration", "config_provided": config})
            raise ValueError("La configuración del LLM (model_name, temperature) es obligatoria para el agente.")

        # Llama al constructor de la clase base con los parámetros requeridos
        super().__init__(
            name="MudanzasTresCantosAgent",
            goal=Goal(
                'Gestionar ofertas de mudanza',
                description='Crear, seguir y cerrar ofertas de mudanza, asegurando cumplimiento de PII y aprobación humana.'
            ),
            persona=Persona(
                'Asistente de Ventas de Mudanzas Tres Cantos',
                description='Soy un asistente virtual experto en la gestión de ofertas de mudanzas, enfocado en la eficiencia y el cumplimiento.'
            ),
            tools=[create_offer, validate_pii],
            config=config
        )

        # Inicializa el LLM utilizando la configuración inyectada
        self.llm = ChatGoogleGenerativeAI(
            model=config["llm"]["model_name"],
            temperature=config["llm"]["temperature"]
        )
        
        logging.info({"event": "AgentInitialized", "agent_name": self.name, "llm_model": config["llm"]["model_name"]})