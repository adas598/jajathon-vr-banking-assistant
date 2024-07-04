def llm_msg(filename, message):
    with open(filename) as f:
        system = f.readlines()
        msg =
        [
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