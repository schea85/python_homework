import sqlite3

# TASK 1-4:

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        
        conn.execute("PRAGMA foreign_keys = 1")
        
        cursor = conn.cursor()
        
        # create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id  INTEGER PRIMARY KEY,
            publisher_name TEXT NOT NULL UNIQUE
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            magazine_name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            subscriber_name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            expiration_date STRING NOT NULL,
            magazine_id INTEGER,
            subscriber_id INTEGER,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
        )
        """)
        
        # add functions to insert data
        def add_publisher(cursor, publisher_name):
            try:
                cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (publisher_name,))
            except sqlite3.IntegrityError:
                print(f"{publisher_name} is already in the database.")
        
        def add_magazine(cursor, magazine_name, publisher_id):
            try:
                cursor.execute("INSERT INTO magazines (magazine_name, publisher_id) VALUES (?, ?)", (magazine_name, publisher_id))
            except sqlite3.IntegrityError:
                print(f"{magazine_name} is already in the database.")
                
        def add_subscriber(cursor, subscriber_name, address):
            cursor.execute("""
            SELECT * FROM subscribers WHERE subscriber_name = ? AND address = ?
            """, (subscriber_name, address))
            results = cursor.fetchall()
            if len(results) > 0:
                print("Already in database.")
                return
            try:
                cursor.execute("INSERT INTO subscribers (subscriber_name, address) VALUES (?, ?)", (subscriber_name, address))
            except sqlite3.IntegrityError:
                print("Subscriber could not be added.")
            
        def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
            try:
                cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))
            except sqlite3.IntegrityError:
                print("The subscription could not be added.")
                
        # enter data into tables
        add_publisher(cursor, "Time Inc")
        add_publisher(cursor, "Penguin Random House")
        add_publisher(cursor, "Macmillan Publishers")
        add_magazine(cursor, "Time Magazine", 1)
        add_magazine(cursor, "Vogue", 2)
        add_magazine(cursor, "Scientific American", 3)
        add_subscriber(cursor, "Alice Johnson", "123 Main St")
        add_subscriber(cursor, "Bob Smith", "456 Oak Ave")
        add_subscriber(cursor, "Charlie Brown", "789 Pine Rd")
        add_subscription(cursor, 1, 1, "2026-12-31")
        add_subscription(cursor, 2, 2, "2026-06-30")
        add_subscription(cursor, 3, 3, "2027-01-15")
        
        conn.commit()
        
        # queries
        # retrieve all info from subscribers table
        cursor.execute("SELECT * FROM subscribers;")
        result1 = cursor.fetchall()
        for row in result1:
            print("All data from Subscribers table:", row)
        
        # retrieve all magazines sorted by name
        cursor.execute("SELECT * FROM magazines ORDER BY magazine_name")
        result2 = cursor.fetchall()
        for row in result2:
            print("Magazines table sorted by Name:", row)
        
        # find all magazines for a particular publisher; use JOIN
        cursor.execute("SELECT publisher_name, magazine_name FROM publishers JOIN magazines ON publishers.publisher_id = magazines.publisher_id WHERE publisher_name = 'Time Inc'")
        result3 = cursor.fetchall()
        for row in result3:
            print("Magazines for particular Publisher:", row)
        
        
except Exception as e:
    print(f"Unable to create database. {e}")
    

    

