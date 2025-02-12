# app_code.py
import sqlite3
from typing import List, Tuple, Optional

def create_in_memory_db() -> sqlite3.Connection:
    """
    Creates an in-memory SQLite database and returns the connection.
    Also initializes a simple schema: an 'employees' table.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn

def add_employee(conn: sqlite3.Connection, name: str, department: str) -> int:
    """
    Inserts a new employee into the 'employees' table.
    Returns the newly inserted employee's ID.
    """
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, department) VALUES (?, ?)",
        (name, department)
    )
    conn.commit()
    return cursor.lastrowid

def get_employee_by_id(conn: sqlite3.Connection, emp_id: int) -> Optional[Tuple[int, str, str]]:
    """
    Fetches an employee by ID.
    Returns a tuple (id, name, department) if found, else None.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, department FROM employees WHERE id = ?",
        (emp_id,)
    )
    return cursor.fetchone()

def get_all_employees_in_department(conn: sqlite3.Connection, dept: str) -> List[Tuple[int, str, str]]:
    """
    Returns all employees in a given department as a list of (id, name, department).
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, department FROM employees WHERE department = ?",
        (dept,)
    )
    return cursor.fetchall()

def remove_employee_by_id(conn: sqlite3.Connection, emp_id: int) -> bool:
    """
    Removes an employee by their ID.
    Returns True if an employee was removed, False otherwise.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    return cursor.rowcount > 0
