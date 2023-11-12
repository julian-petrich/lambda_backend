import json
import convert_dynamodb_to_json

def getPlayerByID(dynamodb, table_name, headers, param_id):
    
    primary_key = {
        'ID': {
            'S': str(param_id)
        }
    }

    response = dynamodb.get_item(TableName=table_name, Key=primary_key)
    
    if 'Item' in response:
        result = response['Item']
        
        print (result)

        response = convert_dynamodb_to_json.convert_dynamodb_to_json_single_player(result)
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'player': response})
        }
    
    else:
        return {
            'statusCode': 200,
            'headers': headers,
            'body': "No Player with this ID found"
        }
