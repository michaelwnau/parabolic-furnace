import json


def lambda_handler(event, context):
    # TODO implement
    fruit = event['fruit']
    if fruit == 'cherry':
        
        return {
            'stausCode': 200,
            'body': json.dumps('I love {fruit}!')
        }
    return {
        'statusCode': 200,
        'body': json.dumps('No thanks!')
    }