import os
import sqlite3
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core import retry
# Try importing FunctionDeclaration instead
from google.generativeai.types import FunctionDeclaration

db_file = "sample.db"
db_conn = sqlite3.connect(db_file)
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def list_tables() -> list[str]:
    """Retrieve the names of all tables in the database."""
    print(' - DB CALL: list_tables')
    cursor = db_conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [t[0] for t in tables]

def describe_table(table_name: str) -> list[tuple[str, str]]:
    """Look up the table schema.
    Returns:
      List of columns, where each entry is a tuple of (column, type).
    """
    print(' - DB CALL: describe_table')
    cursor = db_conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    schema = cursor.fetchall()
    return [(col[1], col[2]) for col in schema]

def execute_query(sql: str) -> list[list[str]]:
    """Execute a SELECT statement, returning the results."""
    print(' - DB CALL: execute_query')
    cursor = db_conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

# Try one of these approaches:

# Approach 1: Use the current way to create tools
db_tools = [
    {
        "name": "list_tables",
        "description": "Retrieve the names of all tables in the database",
        "function": list_tables
    },
    {
        "name": "describe_table",
        "description": "Look up the table schema",
        "function": describe_table
    },
    {
        "name": "execute_query",
        "description": "Execute a SELECT statement, returning the results",
        "function": execute_query
    }
]


instruction = """You are a helpful chatbot that can interact with an SQL database for a computer
store. You will take the users questions and turn them into SQL queries using the tools
available. Once you have the information you need, you will answer the user's question using
the data returned. Use list_tables to see what tables are present, describe_table to understand
the schema, and execute_query to issue an SQL SELECT query."""

model = genai.GenerativeModel(
    "models/gemini-1.5-flash-latest", tools=db_tools, system_instruction=instruction
)


# Define a retry policy. The model might make multiple consecutive calls automatically
# for a complex query, this ensures the client retries if it hits quota limits.


retry_policy = {"retry": retry.Retry(predicate=retry.if_transient_error)}

# Start a chat with automatic function calling enabled.
chat = model.start_chat(enable_automatic_function_calling=True)

resp = chat.send_message("What is the cheapest product?", request_options=retry_policy)
print(resp.text)
