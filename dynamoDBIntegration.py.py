import json
import boto3
import time
import urllib

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')

# insert_data function for inserting data into dynamodb table
def insert_data(recList):
    table = dynamodb.Table('employee')
    for i in range(len(recList)):
        record = recList[i]
        table.put_item(
            Item={
                'username': record['username'],
                'lastname' : record['lastname']
                }
        ) 
        
# get_data function for getting lastname based on username
def get_data(username):
    response = client.get_item(
                    Key={
                        'username': {
                            'S': username,
                        }
                    },
                    TableName='employee',
                )
    return response


def lambda_handler(event, context):
    # TODO implement
    print(event)
    return {
        'statusCode' : 200,
        'headers': {
            'Access-Control-Allow-Origin' : '*', 
            'Access-Control-Allow-Credentials' : True
        },
        'body' : json.dumps(event)
    }
    
    """
    httpMethod = event['httpMethod']
    if httpMethod == 'POST':
        # TODO: write code...
        data = event['body']
        insert_data(json.loads(data))
        return {
            'statusCode' : 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body' : json.dumps("Data inserted successfully.")
        }
        
    elif httpMethod == 'GET':
        # TODO: write code...
        username = event['queryStringParameters']['username']
        result = get_data(username)
        return {
            'statusCode' : 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body' : json.dumps({'lastname' : result['Item']['lastname']['S']})
        }
    else :
        return {
            'statusCode' : 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body' : json.dumps
    """