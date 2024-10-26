from fastapi import FastAPI, Request
import sqlite3
from fastapi.responses import FileResponse

app = FastAPI()

with open("flag.txt") as f:
    FLAG = f.readline()

# Read-only connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect("database.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/recipes")
async def get_recipes():
    conn = get_db_connection()
    recipes = conn.execute("SELECT * FROM recipes").fetchall()
    conn.close()

    return [{"id": row["id"], "name": row["name"], "ingredients": row["ingredients"], "instructions": row["instructions"]} for row in recipes]

@app.post("/login")
async def login(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()
    user = conn.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'").fetchone()
    conn.close()
    print("user")
    if user:
        if user["username"] == "admin":
            return {"message": f"Login successful. Here's your flag {FLAG}"}
        else:
            return {"message": "Login successful, but no flag for non-admin users"}
    else:
        return {"message": "Invalid credentials"}

@app.get("/")
def index():
    return FileResponse("index.html")
