from validator import validate_data
def process_data(data):
    if validate_data(data):
        return f'processed Data: {data}'
    return 'Invalid data'
