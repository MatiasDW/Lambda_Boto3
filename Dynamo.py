import json 
import boto3

#Create Table
client = boto3.client('dynamobd')

def lambda_handler(event, context):
    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'CustomerId',
                'AttributeType': 'S'|'N'|'B'#Select One
            },
            {
                'AttributeName': 'Product',
                'AttributeType': 'S'|'N'|'B'#Select one
            },
        ],
        TableName = 'string',
        KeySchema = [
            {
                'AttributeName': 'Price',
                'KeyType': 'HASH'|'RANGE'#Select one
            },
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 1,
            'WriteCapacityUnits': 1
        },
    )

#Add items to the table


