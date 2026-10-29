import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('learners')

def lambda_handler(event, context):
    learner_id = event['learner-id']

    table.delete_item(
        Key={
            'learner-id': learner_id
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(
            f'Learner {learner_id} deleted successfully!'
        )
    }