import json
import convert_dynamodb_to_json

def getPlayers(dynamodb, table_name, headers):
    
    response = dynamodb.scan(TableName=table_name)

    if 'Items' in response:
        result = response['Items']
        
        print (result)
        
        response = convert_dynamodb_to_json.convert_dynamodb_to_json(result)
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'players': response})
        }
    
    else:
        return {
            'statusCode': 200,
            'headers': headers,
            'body': "No Players available"
        }
