import json
import boto3
import getMultipleResults
import getSingleResult

def lambda_handler(event, context):
    # Initialize a DynamoDB client
    dynamodb = boto3.client('dynamodb')
    # Define the input parameters
    table_name = 'AL03_Results'
    
    headers = {
            'Access-Control-Allow-Origin': '*',  # Replace with your allowed origins
            'Access-Control-Allow-Headers': 'Content-Type',  # Add any custom headers your frontend sends
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'  # Define the allowed HTTP methods
        }
        
    #response = dynamodb.scan(TableName=table_name)
        
    # Get httpMethod and possible param
    #http_method = event['httpMethod']
    if 'pathParameters' in event and event['pathParameters'] is not None:
        id_param = event['pathParameters']['id']
        response = getSingleResult.getResult(dynamodb, table_name, headers, str(id_param))
        return (response)

    else:
        response = getMultipleResults.getResults(dynamodb, table_name, headers)
        return (response)