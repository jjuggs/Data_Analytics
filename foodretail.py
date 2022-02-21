# Import tools
import sqlite3
import csv

# Connection to database
con = sqlite3.connect("sgfood.sqlite")
cur = con.cursor()

# If table in database exists
cur.executescript('''
DROP TABLE IF EXISTS data;
CREATE TABLE data (
    year TEXT NOT NULL,
    food_description TEXT NOT NULL,
    price INTEGER);
''')

# Open and read csv file and insert content into database
a_file = open("average-retail-prices-of-selected-consumer-items-annual.csv")
rows = csv.reader(a_file)
cur.executemany("INSERT INTO data VALUES (?, ?, ?)", rows)

# Delete first row that on CSV that is header
cur.executescript('''DELETE FROM data WHERE year ='year';
DELETE FROM data WHERE price = 'na'
''')

# Print all data imported to database
cur.execute("SELECT * FROM data")
print(cur.fetchone())

# Commit to memory and close connection
con.commit()
con.close()
