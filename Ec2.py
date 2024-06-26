import boto3

client = boto3.client('ec2')

#Create Ec2
def lambda_handler(event, context):
