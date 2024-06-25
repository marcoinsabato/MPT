import os
import psycopg2
import sqlite3
import mysql.connector
from config.config import DATABASE_CONFIG


class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.db_type = DATABASE_CONFIG.get('dbtype', 'sqlite').lower()

    def connect(self):
        """Establish a database connection based on the db_type."""
        if self.db_type == 'postgresql':
            self.connection = psycopg2.connect(
                dbname=DATABASE_CONFIG['dbname'],
                user=DATABASE_CONFIG['user'],
                password=DATABASE_CONFIG['password'],
                host=DATABASE_CONFIG['host'],
                port=DATABASE_CONFIG['port']
            )
        elif self.db_type == 'mysql':
            self.connection = mysql.connector.connect(
                database=DATABASE_CONFIG['dbname'],
                user=DATABASE_CONFIG['user'],
                password=DATABASE_CONFIG['password'],
                host=DATABASE_CONFIG['host'],
                port=DATABASE_CONFIG['port']
            )
        elif self.db_type == 'sqlite':
            self.connection = sqlite3.connect(DATABASE_CONFIG['dbname'])
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")

    def disconnect(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        """Execute a read query and return the results."""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        self.disconnect()
        return results

    def execute_insert(self, query, data):
        """Execute an insert or update query."""
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        self.connection.commit()
        self.disconnect()

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager()
    # Example query execution
    db_manager.execute_insert("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)", ())
    db_manager.execute_insert("INSERT INTO users (name) VALUES (?)", ("John Doe",))
    print(db_manager.execute_query("SELECT * FROM users"))