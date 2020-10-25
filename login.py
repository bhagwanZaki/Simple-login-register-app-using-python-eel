import eel
import sqlite3 as sql

eel.init('www')
con = sql.connect('users.db')
c = con.cursor()

def create_db():
    

    c.execute(''' CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )''')

@eel.expose
def register(username,password):
    
    c.execute("SELECT * FROM users WHERE username=:user",{"user":username})
    check = c.fetchall()
    
    if len(check) == 0:
        c.execute("INSERT INTO users(username,password) VALUES (:username,:password)",{"username":username,"password":password})
        con.commit()

        return 1
    else:
        return 0

@eel.expose
def login(username,password):
    c.execute("SELECT * FROM users WHERE username=:user",{"user":username})
    check = c.fetchall()

    
    if len(check) == 1 and check[0][2] == password:
        return 1
    else:
        return 0

if __name__ == "__main__":
   size = (1000,700) #size of App Window
   create_db()  
   eel.start('register.html',size=size, suppress_error=True)
   