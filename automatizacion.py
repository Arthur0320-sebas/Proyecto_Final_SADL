import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2', region_name='us-east-1')
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')
autoscaling = boto3.client('autoscaling', region_name='us-east-1')

def listar_instancias_ec2():
    print("\n--- Listado de Instancias EC2 ---")
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']} | Tipo: {instance['InstanceType']} | Estado: {instance['State']['Name']}")

def reporte_cpu_ec2():
    print("\n--- Reporte de Uso de CPU (Últimas 24 horas) ---")
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=datetime.utcnow() - timedelta(days=1),
                EndTime=datetime.utcnow(),
                Period=86400,
                Statistics=['Average']
            )
            if metrics['Datapoints']:
                avg_cpu = metrics['Datapoints'][0]['Average']
                print(f"Instancia {instance_id}: Promedio CPU {avg_cpu:.2f}%")
            else:
                print(f"Instancia {instance_id}: Sin datos.")

def listar_s3():
    print("\n--- Buckets S3 y Objetos ---")
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        print(f"\nBucket: {bucket_name}")
        objetos = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objetos:
            for obj in objetos['Contents']:
                print(f"  - {obj['Key']} ({obj['Size']} bytes)")

def consultar_autoscaling():
    print("\n--- Grupos de Auto Scaling ---")
    response = autoscaling.describe_auto_scaling_groups()
    for asg in response['AutoScalingGroups']:
        print(f"Nombre: {asg['AutoScalingGroupName']} | Cap: {asg['DesiredCapacity']}")

if __name__ == "__main__":
    listar_instancias_ec2()
    reporte_cpu_ec2()
    listar_s3()
    consultar_autoscaling()
