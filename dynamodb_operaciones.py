import boto3
import time

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def ejecutar_operaciones():
    try:
        # 1. Crear tabla
        print("Creando tabla devops-tabla...")
        table = dynamodb.create_table(
            TableName='devops-tabla',
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        table.wait_until_exists()
        
        # 2. Insertar registro
        print("Insertando registro...")
        table.put_item(Item={'id': '1', 'nombre': 'Sebastian', 'status': 'activo'})
        
        # 3. Modificar registro (usando ExpressionAttributeNames para evitar conflictos)
        print("Modificando registro...")
        table.update_item(
            Key={'id': '1'},
            UpdateExpression="SET #st = :val",
            ExpressionAttributeNames={'#st': 'status'},
            ExpressionAttributeValues={':val': 'completado'}
        )
        
        # 4. Eliminar registro
        print("Eliminando registro...")
        table.delete_item(Key={'id': '1'})
        
        print("¡Operaciones de DynamoDB completadas con éxito!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar_operaciones()
