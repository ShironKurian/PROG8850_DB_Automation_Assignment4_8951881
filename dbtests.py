import unittest
import mysql.connector

class TestDatabaseSchema(unittest.TestCase):
    def setUp(self):
        # Connect to the database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="subscribers_db"
        )
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    def test_subscribers_table_exists(self):
        self.cursor.execute("SHOW TABLES LIKE 'subscribers';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Subscribers table does not exist")

    def test_subscription_date_column(self):
        # Check if the subscription_date column exists in the subscribers table
        self.cursor.execute("DESCRIBE subscribers;")
        columns = [row[0] for row in self.cursor.fetchall()]
        self.assertIn('subscription_date', columns, "subscription_date column is missing")

if __name__ == '__main__':
    unittest.main()
