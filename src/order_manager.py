import sqlite3

class OrderManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_order(self, medications):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for med in medications:
            cursor.execute("SELECT stock FROM medications WHERE name=?", (med['name'],))
            stock = cursor.fetchone()
            if stock and stock[0] > 0:
                # Here, you could update stock or create an order record
                print(f"Order created for {med['name']} ({med['dosage']})")
        conn.close()
