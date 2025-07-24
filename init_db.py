import sqlite3

with open("schema.sql", "r") as f:
    schema = f.read()

conn = sqlite3.connect("crm.db")
conn.executescript(schema)
conn.commit()
conn.close()

print("✅ Base de données initialisée avec succès.")
