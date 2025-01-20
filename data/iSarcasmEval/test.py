import csv
import random

def shuffle_csv(input_file: str, output_file: str):
    # Read the contents of the CSV file
    with open(input_file, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = list(csv.reader(csv_file))
        
        # Separate the header (if exists) from the data rows
        header = reader[0] if len(reader) > 0 and reader[0][0].isalpha() else None
        rows = reader[1:] if header else reader

        # Shuffle the rows
        random.shuffle(rows)

    # Write the shuffled data to a new CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        if header:
            writer.writerow(header)  # Write the header
        writer.writerows(rows)      # Write the shuffled rows

if __name__ == "__main__":
    # Example usage
    input_csv = 'RQ-sarc-notsarc.csv'    # Replace with your input file name
    output_csv = 'shuffled.csv'  # Replace with your desired output file name

    shuffle_csv(input_csv, output_csv)
    print(f"The shuffled CSV has been saved to '{output_csv}'")
