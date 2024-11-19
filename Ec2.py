import boto3

# Crea un cliente de EC2
client = boto3.client('ec2')

# Crea una instancia EC2
def lambda_handler(event, context):
    response = client.run_instances(
        ImageId='ami-07c3ee614638f120d',  # ID de la imagen de la instancia
        InstanceType='t2.micro',  # Tipo de instancia
        MaxCount=1,  # Número máximo de instancias a lanzar
        MinCount=1  # Número mínimo de instancias a lanzar
    )
    # Resto de tu código aquí

# Inicia una instancia EC2
def Lambda_handler(event, context):
    response = client.start_instances(
        InstanceIds=['string'],  # Reemplaza 'string' con el ID de la instancia que deseas iniciar
        AdditionalInfo='string',  # Opcional: información adicional
        DryRun=False  # Opcional: establece en True para verificar permisos sin realizar la acción
    )
    # Resto de tu código aquí

# Detiene una instancia EC2
def Lambda_handler(event, context):
    response = client.stop_instances(
        InstanceIds=['InstanceId']  # Reemplaza 'InstanceId' con el ID de la instancia que deseas detener
    )
    
