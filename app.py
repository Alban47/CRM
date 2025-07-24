from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB = "crm.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    contacts = conn.execute("SELECT * FROM contacts").fetchall()
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["POST"])
def add_contact():
    name = request.form["name"]
    email = request.form["email"]
    company = request.form["company"]
    conn = get_db()
    conn.execute("INSERT INTO contacts (name, email, company) VALUES (?, ?, ?)",
                 (name, email, company))
    conn.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
