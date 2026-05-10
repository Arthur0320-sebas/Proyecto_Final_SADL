import boto3
import os

s3 = boto3.client('s3')

def ejecutar_s3():
    # Obtener el nombre del bucket que creaste con CloudFormation
    # (Buscamos uno que tenga tu Account ID)
    response = s3.list_buckets()
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    bucket_name = f"devops-bucket-{account_id}"
    
    # 1. Crear archivo local
    file_name = "prueba_entrega.txt"
    with open(file_name, "w") as f:
        f.write("Archivo de prueba para la entrega final.")
    
    # 2. Subir a la carpeta pruebas/
    print(f"Subiendo a {bucket_name}/pruebas/...")
    s3.upload_file(file_name, bucket_name, f"pruebas/{file_name}")
    
    # 3. Listar objetos
    print("\nContenido del bucket:")
    objects = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            print(f"- {obj['Key']} (Tamaño: {obj['Size']} bytes, Modificado: {obj['LastModified']})")

if __name__ == "__main__":
    ejecutar_s3()
