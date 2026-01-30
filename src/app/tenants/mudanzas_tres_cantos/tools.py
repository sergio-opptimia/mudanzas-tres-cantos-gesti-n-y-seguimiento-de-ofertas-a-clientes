from typing import Dict, Any, List
import logging
import uuid
import re

from app.core.tools.base import safe_tool
from app.core.config_loader import current_config

logging.basicConfig(level=logging.INFO)

@safe_tool(config=current_config, is_sensitive=True)
def create_offer(client_data: Dict[str, Any], items: List[Dict[str, Any]]) -> str:
    """
    Crea una nueva oferta en el sistema de Mudanzas Tres Cantos.

    Esta función simula la creación de una oferta utilizando los datos del cliente
    y una lista de ítems o servicios. Genera un identificador único para la oferta
    y registra la acción. En un sistema real, interactuaría con un CRM o un sistema
    de gestión de ofertas para persistir los datos.

    Args:
        client_data (Dict[str, Any]): Un diccionario que contiene la información
            del cliente, como nombre, dirección, contacto, etc.
            Ejemplo: {'name': 'Juan Pérez', 'address': 'Calle Falsa 123', 'phone': '555-1234'}
        items (List[Dict[str, Any]]): Una lista de diccionarios, donde cada diccionario
            representa un ítem o servicio incluido en la oferta, con detalles
            como descripción, cantidad, precio, etc.
            Ejemplo: [{'description': 'Mudanza estándar', 'quantity': 1, 'price': 500},
                      {'description': 'Embalaje de fragiles', 'quantity': 1, 'price': 150}]

    Returns:
        str: Un identificador único (ID) de la oferta creada.
    """
    offer_id = str(uuid.uuid4())
    logging.info({
        "event": "offer_creation",
        "offer_id": offer_id,
        "client_name": client_data.get("name", "N/A"),
        "item_count": len(items),
        "status": "success"
    })
    # Simulación de guardado en un sistema externo
    return offer_id

@safe_tool(config=current_config, is_sensitive=False)
def validate_pii(text: str) -> bool:
    """
    Valida si un texto cumple con las políticas de no inclusión de Información de Identificación Personal (PII).

    Esta función examina el texto proporcionado para detectar patrones comunes
    de PII como nombres completos, direcciones, números de teléfono, correos
    electrónicos, etc. Devuelve True si no se encuentra PII sensible y False
    si se detecta PII.

    Args:
        text (str): La cadena de texto a validar.

    Returns:
        bool: True si el texto está libre de PII según las reglas definidas;
              False en caso contrario.
    """
    # Patrones RegEx simplificados para detección de PII (ejemplo, no exhaustivo)
    # En un sistema real, esto sería mucho más sofisticado y configurable.
    pii_patterns = [
        re.compile(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+){1,}\b'), # Nombres completos (ej. Juan Pérez)
        re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'),  # Números de teléfono (ej. 123-456-7890)
        re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}') # Direcciones de correo electrónico
    ]

    for pattern in pii_patterns:
        if pattern.search(text):
            logging.info({
                "event": "pii_validation",
                "status": "failure",
                "reason": "PII detected",
                "detected_pattern": pattern.pattern
            })
            return False
    
    logging.info({
        "event": "pii_validation",
        "status": "success",
        "reason": "No PII detected"
    })
    return True