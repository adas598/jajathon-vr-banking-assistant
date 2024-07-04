import csv

DIR = "/home/das038/Documents/jajathon/raw_data" # FIXME: Change this according to your directory
PROCESSED_DIR = "/home/das038/Documents/jajathon/processed_data" # FIXME: Change this according to your directory


def parse_bank_statement(file_path):
    transaction_names = []

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            transaction_names.append(row['transaction_name'])  # Assuming the column name is 'transaction_name'

    return transaction_names

def add_category(file_name, transaction_category):
    with open(f"{DIR}/{file_name}", mode='r') as file:
        csv_reader = csv.DictReader(file)
        fieldnames = csv_reader.fieldnames + ['category']
        
        with open(f'{PROCESSED_DIR}/{file_name}', mode='w', newline='') as output_file:
            csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            
            for row, category in zip(csv_reader, transaction_category):
                row['category'] = category
                csv_writer.writerow(row)

# NOTE: Example usage
# file_path = DIR + 'customer_1.csv'  # Replace with the actual file path
# transaction_names = parse_bank_statement(file_path)


