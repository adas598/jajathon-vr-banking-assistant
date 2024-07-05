def llm_msg(filename, message):
    with open(filename, mode='r') as f:
        system = f.read()
        msg = [
            {
                'role': 'system',
                'content': f'{system}'
            },
            {
                'role':'user',
                'content':f'{message}'
            }
        ]
    
    return msg