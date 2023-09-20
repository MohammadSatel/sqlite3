import sqlite3

def create_cars_table():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('cars.db')

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Create a table called 'cars_info'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars_info (
            id INTEGER PRIMARY KEY,
            make TEXT,
            model TEXT,
            year INTEGER
        )
    ''')

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print("Database 'cars.db' created with a 'cars_info' table.")

def add_car(make, model, year):
    # Connect to the SQLite database
    conn = sqlite3.connect('cars.db')
    cursor = conn.cursor()

    # Insert a car into the cars_info table
    cursor.execute('''
        INSERT INTO cars_info (make, model, year)
        VALUES (?, ?, ?)
    ''', (make, model, year))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print("Car added to the 'cars_info' table.")

def print_cars_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('cars.db')
    cursor = conn.cursor()

    # Fetch all rows from the cars_info table
    cursor.execute('SELECT * FROM cars_info')
    rows = cursor.fetchall()

    # Print the table contents
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_cars_table()  # Create the table if not already created

    # Add a car for testing
    add_car("Toyota", "Camry", 2020)

    # Print the contents of the table
    print_cars_table()
