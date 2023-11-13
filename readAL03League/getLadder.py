import json

def getLadder(dynamodb, table_name, headers):
    response = dynamodb.scan(TableName=table_name)
    
    if 'Items' in response:
        items = response['Items']
        
        for item in items:
            # Access and calculate values from the item's attributes
            wins = int(item.get('Wins', {'N': '0'})['N'])
            draws = int(item.get('Draws', {'N': '0'})['N'])  
            losses = int(item.get('Losses', {'N': '0'})['N'])
            goals = int(item.get('Goals', {'N': '0'})['N'])
            goals_against = int(item.get('GoalsAgainst', {'N': '0'})['N'])
            
            games = wins + draws + losses
            points = wins*3 + draws
            goaldiff = goals - goals_against
            
            item['games']= {"N": games}
            item['points']= {"N": points}
            item['goaldiff']= {"N": goaldiff}
    

        item_list = [{key: list(value.values())[0] for key, value in item.items()} for item in items]

        # Sort items based on points, reverse=True brings highest points on top
        item_list = sorted(item_list, key=lambda x: (-x['points'], -x['goaldiff']))

        lowercase_player_list = [{k.lower(): v for k, v in player.items()} for player in item_list]
        
        return {
            'statusCode': 200,
            'headers':headers,
            'body': json.dumps({'teams':lowercase_player_list})
        }
    
    else:
        return {
            'statusCode': 404,
            'headers':headers,
            'body': 'Item not found'
        }