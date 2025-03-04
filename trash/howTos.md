### **Interacting with `sample.db` Using Command Line**
You can use SQLite’s command-line interface to interact with your `sample.db` database.

#### **1. Open SQLite Command Line**
First, open a terminal (Linux/macOS) or Command Prompt (Windows), then navigate to the directory where `sample.db` is located.

```sh
cd /path/to/your/database
```
Then, start SQLite with:
```sh
sqlite3 sample.db
```
This will open an interactive SQLite shell.

#### **2. View Available Tables**
To check what tables exist in the database:
```sql
.tables
```

#### **3. Get Schema of a Table**
To see the structure of a table (replace `your_table` with the table name):
```sql
.schema your_table
```

#### **4. Run SQL Queries**
For example, to select all data from a table:
```sql
SELECT * FROM your_table;
```

#### **5. Insert Data**
To add data into a table:
```sql
INSERT INTO your_table (column1, column2) VALUES ('value1', 'value2');
```

#### **6. Exit SQLite Shell**
To quit:
```sh
.exit
```

---

### **Interacting with `sample.db` Using Python**
Python provides a built-in `sqlite3` module to work with SQLite databases.

#### **1. Connect to the Database**
```python
import sqlite3

# Connect to the database (or create if it doesn't exist)
conn = sqlite3.connect("sample.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()
```

#### **2. Create a Table**
```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")
conn.commit()  # Save changes
```

#### **3. Insert Data**
```python
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()
```

#### **4. Fetch Data**
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)  # Print each row
```

#### **5. Update Data**
```python
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
conn.commit()
```

#### **6. Delete Data**
```python
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
conn.commit()
```

#### **7. Close the Connection**
```python
conn.close()
```

---

### Details about the fxn def

```python
def describe_table(table_name: str) -> list[tuple[str, str]]:
```

### **Breaking it Down**
1. **Function Name:** `describe_table`  
   - This is a function definition, meaning it is designed to describe a table.
  
2. **Parameter:** `table_name: str`  
   - The function expects one argument, `table_name`, which must be a string (`str`).  
   - This likely represents the name of a table in a database.

3. **Return Type:** `-> list[tuple[str, str]]`  
   - This function is expected to return a **list of tuples**.  
   - Each tuple consists of **two strings (`str, str`)**.  
   - This suggests that the function retrieves column names and their corresponding data types from a database table.
