def convert_dynamodb_to_json(dynamodb_data):
    def convert_item(item):
        result = {}
        for key, value in item.items():
            for data_type, data_value in value.items():
                result[key] = data_value
        return result

    result = []
    for item in dynamodb_data:
        result.append(convert_item(item))

    return result
    
def convert_dynamodb_to_json_single_player(dynamodb_data):
    if isinstance(dynamodb_data, dict):
        result = {}
        for key, value in dynamodb_data.items():
            if isinstance(value, dict) and len(value) == 1:
                data_type, data_value = next(iter(value.items()))
                if data_type in ('S', 'N'):
                    result[key] = data_value
                elif data_type == 'M':
                    result[key] = convert_dynamodb_to_json_single_player(data_value)
            else:
                result[key] = convert_dynamodb_to_json_single_player(value)
        return result
    elif isinstance(dynamodb_data, list):
        # Test comment
        return [convert_dynamodb_to_json_single_player(item) for item in dynamodb_data]
    else:
        return dynamodb_data