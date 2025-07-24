-- Table des contacts
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    company TEXT
);

-- Table des interactions
CREATE TABLE IF NOT EXISTS interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_id INTEGER,
    date TEXT,
    note TEXT,
    FOREIGN KEY (contact_id) REFERENCES contacts(id)
);
