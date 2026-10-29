import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('learners')

def lambda_handler(event, context):
    learner_id = event['learner-id']
    name = event['name']

    table.put_item(
        Item={
            'learner-id': learner_id,
            'name': name
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Learner added successfully!')
    }