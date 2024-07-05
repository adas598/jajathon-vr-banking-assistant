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
                "description": row[2],
                "account_balance": float(row[3]),
                "category": row[4]
            }
            jsonl_file.write(json.dumps(record) + '\n')

# Example usage
csv_file_path = 'CSVData_jacob.csv'
jsonl_file_path = 'transactions.jsonl'
csv_to_jsonl(csv_file_path, jsonl_file_path)
