import csv

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Csere: "\N" -> None, üres string -> None
            cleaned_row = {
                key: None if value == '\\N' or not value.strip() else value
                for key, value in row.items()
            }
            data.append(cleaned_row)
    return data

# Használat:
file_path = r"C:\2025-project\datak\constructor_results.csv"
csv_data = read_csv(file_path)

# Ellenőrzés (pl. első 2 sor kiírása):
for row in csv_data[:2]:
    print(row)