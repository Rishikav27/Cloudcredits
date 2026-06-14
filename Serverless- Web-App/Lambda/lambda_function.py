import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudTaskDB')


def lambda_handler(event, context):

    method = event['requestContext']['http']['method']


    if method == "POST":

        body = json.loads(event['body'])

        task = {
            'taskId': str(uuid.uuid4()),
            'taskName': body['taskName'],
            'description': body['description'],
            'createdAt': str(datetime.now())
        }

        table.put_item(Item=task)

        return {
            'statusCode': 200,
            'body': json.dumps(
                {
                    'message':'Task Added Successfully'
                }
            )
        }


    elif method == "GET":

        response = table.scan()

        return {
            'statusCode':200,
            'body':json.dumps(response['Items'])
        }


    elif method == "DELETE":

        body=json.loads(event['body'])

        table.delete_item(
            Key={
                'taskId':body['taskId']
            }
        )


        return{
            'statusCode':200,
            'body':json.dumps(
                {
                    'message':'Task Deleted'
                }
            )
        }
