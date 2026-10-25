import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
        return {
            "smallest": min(values),
            "largest": max(values),
            "count": len(values)
        }

result = inspect_column("MyData.csv", "block_area")
print(result)

area_result = inspect_column("MyData.csv", "block_area")
pop_result = inspect_column("MyData.csv", "block_peri")

print("Area:", area_result)
print("Perimeter:", pop_result)



''' with open("MyData.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("number of rows:", len(rows))
print("columns:", list(rows[0].keys()))
'''