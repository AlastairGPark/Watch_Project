import csv
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS watches;")

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS watches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    case_size TEXT,
    case_material TEXT,
    dial TEXT,
    reference_number TEXT,
    movement TEXT,
    bracelet_material TEXT,
    bracelet_style TEXT,
    bracelet_colour TEXT,
    closing_mechanism TEXT,
    closing_mechanism_material TEXT,
    bezel TEXT,
    bezel_colour TEXT,
    bezel_numbers TEXT,
    price REAL,
    complication_1 TEXT,
    complication_2 TEXT,
    complication_3 TEXT,
    complication_4 TEXT,
    hour_markers TEXT,
    hour_marker_colour TEXT,
    style TEXT,
    exclusivity TEXT,
    edition TEXT,
    image TEXT
);
""")

# Open and read the CSV file
with open("Watches.csv", "r", encoding="UTF-8") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        # Convert "Price on Request" to None, otherwise convert price to float
        raw_price = row.get("Price", "").strip()
        if raw_price.lower() == "price on request":
            price = None
        else:
            try:
                price = float(raw_price.replace(",", "").replace("$", ""))
            except ValueError:
                price = None  # Fallback if price conversion fails
        
        # Match column names with DB schema and safely handle missing values
        formatted_row = (
            row["Brand"].strip(),
            row["Model"].strip(),
            row["Case Size"].strip(),
            row["Case Material"].strip(),
            row["Dial"].strip(),
            row["Reference Number"].strip(),
            row["Movement"].strip(),
            row["Bracelet Material"].strip(),
            row["Bracelet Style"].strip(),
            row["Bracelet Colour"].strip(),
            row["Closing Mechanism"].strip(),
            row["Closing Mechanism Material"].strip(),
            row["Bezel"].strip(),
            row["Bezel Colour"].strip(),
            row["Bezel Numbers"].strip(),
            price,  # Insert the cleaned price
            row.get("Complication 1", "").strip(),
            row.get("Complication 2", "").strip(),
            row.get("Complication 3", "").strip(),
            row.get("Complication 4", "").strip(),
            row["Hour Markers"].strip(),
            row["Hour Marker Colour"].strip(),
            row["Style"].strip(),
            row["Exclusivity"].strip(),
            row["Edition"].strip(),
            row.get("Image", "").strip()
        )
        
        cursor.execute("""
            INSERT INTO watches (
                brand, model, case_size, case_material, dial, reference_number, 
                movement, bracelet_material, bracelet_style, bracelet_colour, 
                closing_mechanism, closing_mechanism_material, bezel, bezel_colour, 
                bezel_numbers, price, complication_1, complication_2, complication_3, complication_4, hour_markers, 
                hour_marker_colour, style, exclusivity, edition, image
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, formatted_row)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data added successfully")
