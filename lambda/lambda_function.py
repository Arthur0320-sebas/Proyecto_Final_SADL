import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('¡Hola desde AWS Lambda! Microservicio funcionando para el Proyecto Final.')
    }
