import json
from random import choices

def lambda_handler(event, context):
    # TODO implement
    return {
        'stausCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }