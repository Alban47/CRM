from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = 'crm.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    contacts = conn.execute('SELECT * FROM contacts').fetchall()
    conn.close()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    company = request.form['company']
    last_contact = request.form['last_contact']
    next_steps = request.form['next_steps']

    conn = get_db_connection()
    conn.execute('INSERT INTO contacts (name, email, phone, company, last_contact, next_steps) VALUES (?, ?, ?, ?, ?, ?)',
                 (name, email, phone, company, last_contact, next_steps))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM contacts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    company = request.form['company']
    last_contact = request.form['last_contact']
    next_steps = request.form['next_steps']

    conn = get_db_connection()
    conn.execute('''
        UPDATE contacts
        SET name = ?, email = ?, phone = ?, company = ?, last_contact = ?, next_steps = ?
        WHERE id = ?
    ''', (name, email, phone, company, last_contact, next_steps, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
