import json
import boto3
import uuid

def lambda_handler(event, context):
    # TODO implement
    message = event["body"]
    
    s3 = boto3.client('s3')
    bucket_name = 's3u121'
    file_name = 'test.txt'
    file_content = message
    
    response = s3.put_object(
    Body=file_content,
    Bucket=bucket_name,
    Key=file_name,
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('https://zz604sldm9.execute-api.eu-central-1.amazonaws.com/'+file_name)
    }