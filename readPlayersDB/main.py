import json
import boto3
import getPlayers
import getPlayerByID

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    
    table_name = 'Players'
    
    method = event["httpMethod"]
    
    headers = {
            'Access-Control-Allow-Origin': '*',  # Replace with your allowed origins
            'Access-Control-Allow-Headers': 'Content-Type',  # Add any custom headers your frontend sends
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'  # Define the allowed HTTP methods
        }
    
    #response = dynamodb.get_item(TableName=table_name, Key={'ID': {'S': id_param}})
    #id_param = event['pathParameters']['DetailID']
    
    if method == "POST":
        #TODO: Implement the function
        return {
            'statusCode': 200,
            'body': json.dumps("response post Method")
        }
        
    elif method == "GET" and event['pathParameters'] is None:
        #TODO: Implement the function
        response = getPlayers.getPlayers(dynamodb, table_name, headers)
        return (response)
        
    elif method == "GET" and event['pathParameters'] is not None:
        param_id = event['pathParameters']['playerID']
        response = getPlayerByID.getPlayerByID(dynamodb, table_name, headers, param_id)
        return (response)