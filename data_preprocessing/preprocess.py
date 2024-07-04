from process_customer_info import parse_bank_statement, add_category
from ..utils.construct_msg import llm_msg
from openai import OpenAI

def preprocess():
    client = OpenAI(api_key="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")
    
    customer_name = input('Enter customer name: ') + '.csv'

    transaction_names = parse_bank_statement(customer_name)

    msg = llm_msg('data_preprocess_system.txt', transaction_names)

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=msg,
        max_tokens=500
    )

    print(response.choices[0].message.content)

    return

if __name__=="__main__":
    preprocess()