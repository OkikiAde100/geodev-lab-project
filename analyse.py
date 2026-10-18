with open("wards.csv") as f:
    lines = f.readlines()

print("number of lines:", len(lines))

total = 0

def classify(area):
    if area > 9:
        return "large"
    else:
        return "small"

for line in lines[1:]:  # Skip the header line
    parts = line.strip().split(",")
    wards = parts[0]
    areas = parts[1]
    area_km2 = float(parts[1])
    areas_hectare = area_km2 * 100
    #print(wards, "has area", areas)
    #print(wards, "has area", areas_hectare, "hectare")
    #print(line.strip())
    total += area_km2
    if area_km2 > 9:
        size = "large"
    else:
        size = "small"
    print(wards, "is", size)
    print(classify(area_km2))

print(total)