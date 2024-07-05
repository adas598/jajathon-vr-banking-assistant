import csv

DIR = "/home/das038/Documents/jajathon/raw_data" # FIXME: Change this according to your directory
PROCESSED_DIR = "/home/das038/Documents/jajathon/processed_data" # FIXME: Change this according to your directory


def parse_bank_statement(file_path):
    column_values = []

    with open(f"{DIR}/{file_path}", mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            if "Transaction Name" in row:
                column_values.append(row["Transaction Name"])
            else:
                print(f"Error: `Transaction Name` not found in row")
                print(row)  # Print the entire row for debugging

    return column_values

def add_category(file_name, transaction_category):
    input_file_path = f"{DIR}/{file_name}"
    output_file_path = f"{PROCESSED_DIR}/categorized_{file_name}"
    
    with open(input_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        fieldnames = csv_reader.fieldnames + ['Category']
        
        with open(output_file_path, mode='w', newline='') as output_file:
            csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            
            for row, category in zip(csv_reader, transaction_category):
                row['Category'] = category
                csv_writer.writerow(row)
    
    print(f"Processed file saved as {output_file_path}")


def remove_column(file_name, col_name):
    input_file_path = f"{PROCESSED_DIR}/{file_name}"
    output_file_path = f"{PROCESSED_DIR}/processed_{file_name}"
    
    with open(input_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        fieldnames = [field for field in csv_reader.fieldnames if field != col_name]

        if col_name not in csv_reader.fieldnames:
            print(f"Column '{col_name}' not found in the file.")
            return

        with open(output_file_path, mode='w', newline='') as output_file:
            csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for row in csv_reader:
                del row[col_name]
                csv_writer.writerow(row)

    print(f"Processed file saved as {output_file_path}")




# NOTE: Example usage
# file_path = DIR + 'customer_1.csv'  # Replace with the actual file path
# transaction_names = parse_bank_statement(file_path)


