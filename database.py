import sqlite3
import os

def checkUser(chatID:int, userID:int, adminLevel:int = 0) -> bool:
    """Returns True if user exists in chat DB, else creates and returns False"""
    os.makedirs("databases", exist_ok=True)

    if (not f"{chatID}.db" in os.listdir("databases")):
        conn = sqlite3.connect(f"databases/{chatID}.db")
        curs = conn.cursor()
        curs.execute("""
        CREATE TABLE "users" (
            "id"	INTEGER,
            "admin_level"	INTEGER DEFAULT 0
        );
        """)
        conn.commit()
    else:
        conn = sqlite3.connect(f"databases/{chatID}.db")
        curs = conn.cursor()

    curs.execute("SELECT * FROM users WHERE id = ?", (userID,))
    if curs.fetchone():
        return True
    else:
        curs.execute("INSERT INTO users (id, admin_level) VALUES (?, ?)", (userID, adminLevel))
        conn.commit()
    return False


def setAdminValue(chatID:int, userID:int, adminLevel:int = 0) -> None:
    checkUser(chatID, userID)
    conn = sqlite3.connect(f"databases/{chatID}.db")
    curs = conn.cursor()
    curs.execute("UPDATE users SET admin_level = ? WHERE id = ?", (adminLevel, userID))
    conn.commit()


def getAdminValue(chatID:int, userID:int) -> int:
    checkUser(chatID, userID)
    conn = sqlite3.connect(f"databases/{chatID}.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM users WHERE id = ?", (userID,))
    resp = curs.fetchone()
    if resp: return resp[1]
    else: return 0