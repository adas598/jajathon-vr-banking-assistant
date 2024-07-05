import os
import pandas as pd
from openai import OpenAI

# Initialize OpenAI client
client= OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Load the CSV file and parse it
def load_banking_data(file_path):
    return pd.read_csv(file_path)

# Generate the system message
def get_system_message():
    return """You are a financial advising expert. You can design a financial plan for a user by taking in user banking data as context and develop a financial road map to achieve the customer's financial goal.
Please provide an timeline-based roadmap to achieve the goal:
    (1) How to achieve it with the current monthly income (assuming there is no increments)?
    (2) How much additional income might be required to reach the goal?
    (3) Create a succinct monthly budget to achieve this.

Ensure the output is point based and aesthetically pleasing as response will be displayed in the terminal. If using tables please make it `pretty` for the terminal."""

# Format banking data into a readable string
def format_banking_data(data):
    transactions = []
    for index, row in data.iterrows():
        transactions.append(f"Date: {row['Date']}, Credit/Debit: {row['Credit/Debit']}, Balance: {row['Balance']}, Category: {row['Category']}")
    return "\n".join(transactions)

# Query ChatGPT
def query_chatgpt(system_message, user_message, context):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
        {"role": "user", "content": f"Customer banking data:\n{context}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=2048
    )
    return response.choices[0].message.content

# Pretty print response
def pretty_print_response(response):
    print("\nFinancial Plan:\n")
    print(response)

def main():
    # Load the banking data
    
    file_path = f'processed_data/processed_categorized_{input("Enter customer name: ")}.csv'  # Replace with the actual path to your CSV file
    banking_data = load_banking_data(file_path)
    context = format_banking_data(banking_data)

    # System message
    system_message = get_system_message()

    # Enter into a back-and-forth loop with the user
    while True:
        user_query = input("Enter your financial question (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            print("Goodbye!")quit
            break

        # Get response from ChatGPT
        response = query_chatgpt(system_message, user_query, context)

        # Print the response
        pretty_print_response(response)

if __name__ == "__main__":
    main()
