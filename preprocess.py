# from data_preprocessing.process_customer_info import parse_bank_statement, add_category, remove_column
# from utils.construct_msg import llm_msg
# from openai import OpenAI
# from pdb import set_trace
# import os

# def preprocess():
#     client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
#     customer_name = input('Enter customer name: ') + '.csv'
    
#     transaction_names = parse_bank_statement(customer_name)
    
#     msg = llm_msg('utils/data_preprocess_system.txt', transaction_names)
    
#     response = client.chat.completions.create(
#         model='gpt-4o',
#         messages=msg,
#         max_tokens=4096
#     )

#     # remove_column(customer_name, 'Transaction Name')
#     add_category(customer_name, response.choices[0].message.content.split(','), remove_col='Transaction Name')
#     return

# if __name__=="__main__":
#     # set_trace()
#     preprocess()

from data_preprocessing.process_customer_info import parse_bank_statement, add_category, remove_column
from utils.construct_msg import llm_msg
from openai import OpenAI
import os

DIR = "/home/das038/Documents/jajathon/raw_data"  # Ensure this directory is correct
PROCESSED_DIR = "/home/das038/Documents/jajathon/processed_data"  # Ensure this directory is correct

def preprocess():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    customer_name = input('Enter customer name: ') + '.csv'
    
    transaction_names = parse_bank_statement(customer_name)
    
    msg = llm_msg('utils/data_preprocess_system.txt', transaction_names)
    
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=msg,
        max_tokens=4096
    )
    
    categories = response.choices[0].message.content.split(',')
    
    # Add categories to the original file and save it with a new name
    add_category(customer_name, categories)
    
    # Define the new file name created by add_category
    categorized_file_name = f'categorized_{customer_name}'
    
    # Remove the 'Transaction Name' column from the categorized file
    remove_column(categorized_file_name, 'Transaction Name')

if __name__ == "__main__":
    preprocess()
