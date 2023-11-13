import json
import boto3

def convert_dynamodb_to_json(dynamodb_data):
    result = {}
    for key, value in dynamodb_data.items():
        data_type, data_value = next(iter(value.items()))
        if data_type == "M":
            result[key] = convert_dynamodb_to_json(data_value)
        else:
            result[key] = data_value
    return result

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    
    table_name = 'ResultEvents'
    player_table = 'Players'
    
    id_param = event['pathParameters']['DetailID']
    
    headers = {
            'Access-Control-Allow-Origin': '*',  # Replace with your allowed origins
            'Access-Control-Allow-Headers': 'Content-Type',  # Add any custom headers your frontend sends
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'  # Define the allowed HTTP methods
        }
    
    response = dynamodb.get_item(TableName=table_name, Key={'ID': {'S': id_param}})
    
    if 'Item' in response:
        result = response['Item']
        #print("result:", result)
        
        response = convert_dynamodb_to_json(result)
        player_id = response["Goals"]["Goal_1"]["AssisstID"]
        #player_item = dynamodb.get_item(TableName=player_table, Key={'ID': {'S': player_id}})
        #player_firstname = (player_item["Item"]["Firstname"]["S"])
        #player_lastname = (player_item["Item"]["Lastname"]["S"])
        #response["Goals"]["Goal_1"]["Assisst Firstmame"] = player_firstname
        #response["Goals"]["Goal_1"]["Assisst Lastname"] = player_lastname
        
        # TODO implement
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'result': response})
        }
    
    else:
        return {
            'statusCode': 200,
            'headers': headers,
            'body': "Item not found"
        }
