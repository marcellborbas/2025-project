filename = r"C:\2025-project\data\constructor_results.csv"  # Cseréld le a fájlnevedre

with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()  # Sorok beolvasása

header = lines[0].strip().split(",")
data = [line.strip().split(",") for line in lines[1:]]

print("Fejléc:", header)
print("Adatok:")
for row in data:
    print(row)
    break