from app import app
from app import cur
from app import con
import sys

args = sys.argv

def get(num):
    try:
        return args[num]
    except:
        return None

if get(1) == "run":
    app.run("0.0.0.0", 8080)
    quit()
elif get(1) == "setup":
    cur.execute("""
        CREATE TABLE users(
            id INT PRIMARY KEY,
            username TEXT,
            password TEXT,
            friends TEXT,
            banned TEXT,
            rank INT,
            reason TEXT,
            character TEXT,
            sbtoken TEXT,
            twostep TEXT,
            email TEXT,
            verified TEXT,
            code INT,
            sbcoins INT,
            claimedemail TEXT,
            ip TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE ipbans(
            reason TEXT,
            ip TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE verifytokens(
            token TEXT,
            for TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE codes(
            code TEXT,
            uses INT,
            amount INT
        )
    """)

    con.commit()
    con.close()
    print("Done!")
    quit()
elif get(1) == "change" and get(2) == "username" and get(3) != None and get(4) != None:
    cur.execute(f"UPDATE users SET username='{get(4)}' WHERE username='{get(3)}'")
    con.commit()
    con.close()
    print("Done!")
    quit()
elif get(1) == "change" and get(2) == "rank" and get(3) != None and get(4) != None:
    cur.execute(f"UPDATE users SET rank='{int(get(4))}' WHERE username='{get(3)}'")
    con.commit()
    con.close()
    print("Done!")
    quit()

elif get(1) == "change" and get(2) == "sbcoin" and get(3) != None and get(4) != None:
    cur.execute(f"UPDATE users SET sbcoins='{int(get(4))}' WHERE username='{get(3)}'")
    con.commit()
    con.close()
    print("Done!")
    quit()
elif get(1) == "get" and get(2) != None:
    cur.execute(f"SELECT * FROM {get(2)}")
    res = cur.fetchall()
    for i in res:
        print(i)
    print("Done!")
    quit()
elif get(1) == "deleteipban" and get(2) != None:
    cur.execute(f"SELECT ip FROM users WHERE username='{get(2)}'")
    ip = cur.fetchone()
    print(cur.execute(f"DELETE FROM ipbans WHERE ip='{ip[0]}'").lastrowid)
    con.commit()
    print("Done!")
    quit()
elif get(1) == "execute":
    cur.execute(input())
    con.commit()
    print("Done!")
    quit()

con.commit()
print("Nothing to do!")
quit(1)
