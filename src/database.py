import sqlite3
from pathlib import Path
def create_commands_table():
    conn = sqlite3.connect(Path(__file__).parent.parent / 'data' / 'commands.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS commands (
        id INTEGER PRIMARY KEY,
        tool TEXT NOT NULL,
        command TEXT NOT NULL,
        category TEXT,
        note TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def save_command_to_db(tool, command, category, note):
    """Save commands to database"""
    conn = sqlite3.connect(Path(__file__).parent.parent / 'data' / 'commands.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO commands (tool, command, category, note) 
    VALUES (?, ?, ?, ?)
    ''', (tool, command, category, note))
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    print(f"\n✅ Command saved! ID: {last_id}")
    return last_id

def get_all_commands():
    """Select all commands from database"""
    conn = sqlite3.connect(Path(__file__).parent.parent / 'data' / 'commands.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, tool, command, category, note FROM commands ORDER BY id ASC")
    results = cursor.fetchall()
    conn.close()
    return results

def search_commands(keyword):
    """Search commands by keyword"""
    conn = sqlite3.connect(Path(__file__).parent.parent / 'data' / 'commands.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT id, tool, command, category, note 
    FROM commands 
    WHERE tool LIKE ? OR command LIKE ? OR category LIKE ? OR note LIKE ?
    ORDER BY id DESC
    ''', (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    results = cursor.fetchall()
    conn.close()
    return results

def delete_command_by_id(command_id):
    """Hapus command berdasarkan ID"""
    conn = sqlite3.connect(Path(__file__).parent.parent / 'data' / 'commands.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM commands WHERE id = ?", (command_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

