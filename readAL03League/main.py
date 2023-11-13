import json
import boto3
import getLadder

def lambda_handler(event, context):
    # Initialize a DynamoDB client
    dynamodb = boto3.client('dynamodb')
    
    # Check the HTTP method of the request
    http_method = event['httpMethod']
    
    # Define the input parameters
    table_name = 'AL03_Teams'
    
    headers = {
            'Access-Control-Allow-Origin': '*',  # Replace with your allowed origins
            'Access-Control-Allow-Headers': 'Content-Type',  # Add any custom headers your frontend sends
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'  # Define the allowed HTTP methods
        }
        
    if http_method == 'GET':
        response = getLadder.getLadder(dynamodb, table_name, headers)
        return (response)
    
    else:
        # Handle other HTTP methods (PUT, DELETE, etc.) if needed
        return {
            'statusCode': 405,  # Method Not Allowed
            'headers': headers,
            'body': json.dumps('Unsupported HTTP method.')
        }
