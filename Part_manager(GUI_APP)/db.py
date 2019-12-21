import _sqlite3


class Database:
    def __init__(self, db):
        self.conn = _sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS Parts(id INTEGER PRIMARY KEY, part text, customer text, '
                         'retailer text, price text)')
        self.conn.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM Parts')
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute('INSERT INTO Parts VALUES(NULL, ?, ?, ?, ?)',(part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute('DELETE FROM Parts WHERE id=?', (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer,price):
        self.conn.execute('UPDATE Parts set part=?, customer=?, retailer=?, price=? WHERE id=?',(part, customer,
                                                                                                 retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database('store.db')
# db.insert("HP charger", "Girum","Best buy", "180")
# db.insert("HP charger", "Dina","Best buy", "1230")
# db.insert("HP charger", "Gebre","Best buy", "1820")
# db.insert("HP charger", "trevor","Best buy", "1810")
#
#
#



