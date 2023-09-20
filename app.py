import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('contacts.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create a table called 'contacts'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    )
''')

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Database 'contacts.db' created with a 'contacts' table.")

def create_contact(name, age, email):
    # Connect to the SQLite database
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Insert a contact into the contacts table
    cursor.execute('''
        INSERT INTO contacts (name, age, email)
        VALUES (?, ?, ?)
    ''', (name, age, email))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print("Contact added to the 'contacts' table.")

def read_contacts():
    # Connect to the SQLite database
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Fetch all rows from the contacts table
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()

    # Print the contacts
    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])
        print("Email:", row[3])
        print("\n")

    # Close the cursor and connection
    cursor.close()
    conn.close()

def update_contact(contact_id, name, age, email):
    # Connect to the SQLite database
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Update a contact in the contacts table
    cursor.execute('''
        UPDATE contacts
        SET name=?, age=?, email=?
        WHERE id=?
    ''', (name, age, email, contact_id))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print("Contact updated.")

def delete_contact(contact_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Delete a contact from the contacts table
    cursor.execute('DELETE FROM contacts WHERE id=?', (contact_id,))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    print("Contact deleted.")

def menu():
    print("===== Contact Database Menu =====")
    print("1. Create Contact")
    print("2. Read Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("===============================")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            email = input("Enter the email: ")
            create_contact(name, age, email)
        elif choice == '2':
            print("Contacts:")
            read_contacts()
        elif choice == '3':
            contact_id = int(input("Enter the contact ID to update: "))
            name = input("Enter the new name: ")
            age = int(input("Enter the new age: "))
            email = input("Enter the new email: ")
            update_contact(contact_id, name, age, email)
        elif choice == '4':
            contact_id = int(input("Enter the contact ID to delete: "))
            delete_contact(contact_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
