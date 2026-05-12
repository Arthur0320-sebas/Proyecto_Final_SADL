import json
import random

def lambda_handler(event, context):
    # El profesor pidió al menos 5 mensajes aleatorios
    mensajes_logistica = [
        "Pedido procesado con éxito en el sistema central.",
        "Inventario actualizado: Stock disponible para envío.",
        "Ruta de entrega optimizada para el transportista local.",
        "Envío internacional recibido en aduana de destino.",
        "Alerta de sistema: Reabastecimiento de almacén completado."
    ]
    
    # Usamos random.choice como solicitó el profesor
    mensaje_seleccionado = random.choice(mensajes_logistica)
    
    # El JSON debe incluir los campos 'mensaje' y 'servicio'
    cuerpo_respuesta = {
        'mensaje': mensaje_seleccionado,
        'servicio': 'Microservicio de Logística v2'
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(cuerpo_respuesta, ensure_ascii=False)
    }
