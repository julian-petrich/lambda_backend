import json

def getResult (dynamodb, table_name, headers, id_param):
    
    response = dynamodb.get_item(TableName=table_name, Key={'ID': {'S': id_param}})

    if 'Item' in response:
        result = response['Item']
        
        # Create an empty dictionary for the standard JSON
        response = {}
        
        # Iterate through the DynamoDB JSON and convert to standard JSON
        for key, value in result.items():
            if "M" in value:
                response[key] = {}
                for sub_key, sub_value in value["M"].items():
                    if "N" in sub_value:
                        response[key][sub_key] = sub_value["N"]
                    elif "S" in sub_value:
                        response[key][sub_key] = sub_value["S"]
            elif "N" in value:
                response[key] = value["N"]
            elif "S" in value:
                response[key] = value["S"]

        # Fetch and modify additional data if needed
        table_name = 'AL03_Teams'
        home_team_id = result['Home Team']['M']['ID']['S']
        away_team_id = result['Away Team']['M']['ID']['S']

        home_team_response = dynamodb.get_item(TableName=table_name, Key={'ID': {'S': home_team_id}})
        away_team_response = dynamodb.get_item(TableName=table_name, Key={'ID': {'S': away_team_id}})

        if 'Item' in home_team_response:
            response['Home Team']['name'] = home_team_response['Item']['Name']['S']

        if 'Item' in away_team_response:
            response['Away Team']['name'] = away_team_response['Item']['Name']['S']

        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'result':response})
        }
    else:
        return {
            'statusCode': 404,
            'headers': headers,
            'body': 'No result found'
        }