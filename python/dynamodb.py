# import json
# import boto3
# import uuid

# def lambda_handler(event, context):
#     # TODO implement
#     message = event["body"]
    
#     # s3 = boto3.client('s3')
#     # bucket_name = 'hello-s3-20231022'
#     file_name = str(uuid.uuid4()) + '.txt'
#     # file_content = message
    
#     # response = s3.put_object(
#     # Body=file_content,
#     # Bucket=bucket_name,
#     # Key=file_name,
#     # )

#     db = boto3.client('dynamodb')
#     response = db.put_item(
#         TableName='basic-dynamodb-table',
#         Item={
#             'Id': {
#                 'S': file_name
#             },
#             'Message': {
#                 'S': message
#             }
#         })
    
#     return {
#         'statusCode': 200,
#         'body': json.dumps('https://zz604sldm9.execute-api.eu-central-1.amazonaws.com/'+file_name)
#     }
import os
import json
import boto3
from datetime import datetime

# Initialisieren der AWS-SDKs
s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

# Name der DynamoDB-Tabelle
dynamodb_table_name = "basic-dynamodb-table"
bucket_name = 's3u121'
def lambda_handler(event, context):
    for record in event['Records']:
        # Extrahieren der S3-Bucket- und Dateiinformationen aus dem S3-Event
        s3_bucket = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']

        # Erzeugen eines Zeitstempels
        timestamp = datetime.now().isoformat()

        # Schreiben der Daten in die DynamoDB-Tabelle
        response = dynamodb.put_item(
            TableName=dynamodb_table_name,
            Item={
                'Id': {'S': file_key},
                'Message': {'S': timestamp}
            }
        )

        print(f"Datei '{file_key}' mit Zeitstempel '{timestamp}' in DynamoDB geschrieben. Antwort: {response}")

# Beachten Sie, dass Sie in der AWS Lambda-Konsole die erforderlichen Trigger für diese Lambda-Funktion, die Berechtigungen und die Ressourcenrichtlinien einrichten müssen.
