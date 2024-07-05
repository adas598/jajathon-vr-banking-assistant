import csv
import json

def csv_to_jsonl(csv_file_path, jsonl_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file, open(jsonl_file_path, mode='w', encoding='utf-8') as jsonl_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            record = {
                "date_of_transaction": row[0],
                "amount": float(row[1]),
                "account_balance": float(row[2]),
                "category": row[3]
            }
            jsonl_file.write(json.dumps(record) + '\n')

# Example usage
# csv_file_path = 'CSVData_jacob.csv'
# jsonl_file_path = 'transactions.jsonl'
# csv_to_jsonl(csv_file_path, jsonl_file_path)

if __name__=="__main__":
    customer_name = input("Enter customer name: ")
    csv_path = f"processed_data/processed_categorized_{customer_name}.csv"
    jsonl_path = f'database/{customer_name}.jsonl'

    csv_to_jsonl(csv_path, jsonl_path)
