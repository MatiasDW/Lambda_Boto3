import boto3

client = boto3.client("s3")

#Create Bucket 
def lambda_handler(event, context):
    create_s3bucket = client.create_bucket(
        Bucket = "Almacenamiento",
        CreateBucketConfiguration = {
            "LocationConstraint" : "us-east-1"
        }
    )
2


#Delete Bucket
def lambda_handler(event, context):
        response = client.delete_bucket(
              Bucket = 'Bucket_Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         '
        )

#List Buckets 
def lambda_handler(event, context):
      response = client.list_buckets(
            
      )