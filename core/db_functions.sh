#!/bin/bash

source "$BASE_DIR/core/config.sh"
# Simple Database Functions

DBFILE="$PLACEHOLDERS_DB"

# Func 1 : Init Database
init_db() {
  sqlite3 "$DBFILE" "CREATE TABLE IF NOT EXISTS placeholders (
    name TEXT PRIMARY KEY,
    value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );" 2>/dev/null
}

# Func 2 : Get values from Database
db_get() {
  local name="$1"
  sqlite3 "$DBFILE" \
    "SELECT value FROM placeholders WHERE name='$name';"
}

# Func 3 : Save to Database
db_save() {
  local name="$1"
  local value="$2"

  sqlite3 "$DBFILE" \
    "INSERT OR REPLACE INTO placeholders (name, value) VALUES ('$name', '$value');"

  echo -e "${GREEN}[+]${RESET} Saved '$name' to database"
}

# Function 4: Extract placeholders from command
extract_placeholders() {
  echo "$1" | grep -o '{[^}]*}' | tr -d '{}' | sort -u
}

# Function 5: Check if database file exists
db_exists() {
  [ -f "$DBFILE" ]
}
