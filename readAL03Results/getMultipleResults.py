import json

def getResults(dynamodb, table_name, headers):
    
    response = dynamodb.scan(TableName=table_name)
    
    if 'Items' in response:
        items = response['Items']
        
        table_name = 'AL03_Teams'
        # Modify items as needed
        for item in items:
            home_team_id = item['Home Team']['M']['ID']
            away_team_id = item['Away Team']['M']['ID']
            
            
            home_team = dynamodb.get_item(TableName=table_name, Key={'ID': home_team_id})
            away_team = dynamodb.get_item(TableName=table_name, Key={'ID': away_team_id})
            
            if 'Item' in home_team:
                home_team = home_team['Item']['Name']['S']
                item['Home Team']['M']['name'] = home_team

            if 'Item' in away_team:
                away_team = away_team['Item']['Name']['S']
                item['Away Team']['M']['name'] = away_team

            
        # Create item_list based on the modified items
        item_list = [{key: list(value.values())[0] for key, value in item.items()} for item in items]
    
        # Convert keys to lowercase in item_list
        # Add comment
        lowercase_item_list = [{k.lower(): v for k, v in item.items()} for item in item_list]
    
        return {
            'statusCode': 200,
            'headers':headers,
            'body': json.dumps({'results':lowercase_item_list})
        }
    
    else:
        return {
            'statusCode': 404,
            'headers':headers,
            'body': 'No results found'
        }

        