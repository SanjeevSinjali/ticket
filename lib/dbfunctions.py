import os
import sqlite3

class dbfunctions(object):
    """sqlite helper"""

    def __init__(self):
        self.db_path = os.path.join("/home/sanjeev/Desktop/Ticket/", 'database.db')
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()


    def create_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                                id INTEGER PRIMARY KEY,
                                email TEXT UNIQUE NOT NULL,
                                fullname TEXT NOT NULL,
                                password TEXT NOT NULL,
                                phonenumber TEXT NOT NULL,
                                role TEXT CHECK(role IN ('ADMIN', 'STAFF', 'CUSTOMER')) NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS agency (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                status TEXT CHECK(status IN ('ACTIVE', 'INACTIVE')) NOT NULL
                                )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS bus (
                                id INTEGER PRIMARY KEY,
                                type TEXT NOT NULL,
                                seatsno INTEGER NOT NULL,
                                departtime TEXT NOT NULL,
                                destination TEXT NOT NULL,
                                source TEXT NOT NULL,
                                operate_date DATE NOT NULL,
                                status TEXT CHECK(status IN ('ACTIVE', 'INACTIVE')) NOT NULL,
                                agency_id INTEGER,
                                FOREIGN KEY (agency_id) REFERENCES agency(id)
                                )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS busseat (
                                id INTEGER PRIMARY KEY,
                                bus_id INTEGER,
                                isAvailable INTEGER NOT NULL CHECK(isAvailable IN (0, 1)),
                                seatnumber INTEGER NOT NULL,
                                FOREIGN KEY (bus_id) REFERENCES bus(id)
                                )''')
        self.conn.commit()
        self.conn.close()

    def reset_database(self):
        self.cursor.execute("DROP TABLE IF EXISTS user")
        self.cursor.execute("DROP TABLE IF EXISTS agency")
        self.cursor.execute("DROP TABLE IF EXISTS bus")
        self.cursor.execute("DROP TABLE IF EXISTS busseat")
        self.conn.commit()
        self.create_database()

    def insert_user(self, fullname, password,email,phonenumber,role):
        fullname = fullname.strip()
        password = password.strip()
        email = email.strip()
        phonenumber = phonenumber.strip()
        role = role.strip()
        info = email ,fullname, password , phonenumber, role
        try:
            self.cursor.execute('INSERT INTO user(name, password) VALUES(?, ?)', info)
            self.conn.commit()
            return True
        except:
            return False

    def has_user(self, fullname, password):
        fullname = fullname.strip()
        password = password.strip()
        info = fullname, password
        flag = self.cursor.execute(
            'SELECT * FROM user WHERE fullname=? and password=?',
            info).fetchall()
        if flag == []:
            return False
        else:
            return True

    def get_all_user_info(self):
        list = []
        rows = self.cursor.execute("SELECT id, name, password FROM user WHERE role NOT 'ADMIN'")
        for item in rows:
            list.append({
                'id': item[0],
                'fullname': item[1],
                'password': item[2],
                'email': item[3],
                'role': item[4]
            })
        return list

    def insert_content_by_username(self, username, title, content, tag):
        try:
            userid = self.cursor.execute('SELECT id FROM user WHERE name=?',
                (username, )).fetchone()
            count = self.cursor.execute('SELECT COUNT(*) FROM user_content').fetchone()
            rows = count[0]
            rows += 1
            self.cursor.execute(
                'INSERT INTO user_content(id, userid) VALUES (?, ?)',
                (rows, userid[0]))
            self.cursor.execute(
                'INSERT INTO content(id, title, content, tag) VALUES (?, ?, ?, ?)',
                (rows, title, content, tag))
            self.conn.commit()
            return True
        except:
            return False

    def get_content_by_username(self, name):
        list = []
        userid = self.cursor.execute(
            'SELECT id FROM user WHERE name=?', (name, )).fetchone()
        id = self.cursor.execute(
            'SELECT id FROM user_content WHERE userid=?', userid).fetchall()
        for item in id:
            if item is not None:
                r = self.cursor.execute(
                    'SELECT id, title, content, tag FROM content WHERE id=?',
                    item).fetchone()
                if r is not None:
                    list.append({
                        'id': r[0],
                        'title': r[1],
                        'content': r[2],
                        'tag': r[3]
                    })
        return list

    def search_travel_from_to(self,source,destination,date,shift):
        info = source , destination , date , shift
        travels = self.cursor.execute('SELECT * FROM bus where source=? AND destination=?',info)
        if travels == []:
            return "No buses available for that route"
        return travels
    
    def 
    

        
