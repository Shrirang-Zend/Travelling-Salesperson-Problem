import csv

def remove_quotes(input_file, output_file):
    with open(input_file, 'r') as csv_input, open(output_file, 'w', newline='') as csv_output:
        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output)

        for row in reader:
            # Remove double quotes from each element in the row
            row = [entry.strip('"') for entry in row]
            writer.writerow(row)

# Replace 'input_file.csv' and 'output_file.csv' with your file paths
remove_quotes('try.csv', 'city_data.csv')
