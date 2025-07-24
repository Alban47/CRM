import sqlite3

def init_db():
    with open('schema.sql', 'r', encoding='utf-8') as f:
        schema = f.read()

    conn = sqlite3.connect('crm.db')
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print("✅ Base de données initialisée avec succès.")

if __name__ == '__main__':
    init_db()
