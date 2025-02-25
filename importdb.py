import csv
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

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
    complications TEXT,
    complication_colour TEXT,
    hour_markers TEXT,
    hour_marker_colour TEXT,
    style TEXT,
    exclusivity TEXT,
    edition TEXT,
    image TEXT
);
""")

# Open and read the CSV file
with open("Watches.csv", "r", encoding = "UTF-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row
    
    for row in csv_reader:
        # Remove spaces and handle NULL values
        row = [value.strip() if value.strip() != "NULL" else None for value in row]

        # Ensure the row has exactly 27 columns
        if len(row) == 27:
            # Insert values into the database, skipping the unique ID
            cursor.execute("""
                INSERT INTO watches (
                    id, brand, model, case_size, case_material, dial, reference_number, 
                    movement, bracelet_material, bracelet_style, bracelet_colour, 
                    closing_mechanism, closing_mechanism_material, bezel, bezel_colour, 
                    bezel_numbers, price, complications, complication_colour, hour_markers, 
                    hour_marker_colour, style, exclusivity, edition, image
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """)
        else:
            print(f"Skipping row with incorrect column count: {row}")

# Commit changes and close connection
conn.commit()
conn.close()

print("Data added successfully")
