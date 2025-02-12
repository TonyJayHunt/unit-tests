# test_app_code.py
import pytest
import allure
from app_code import (
    create_in_memory_db,
    add_employee,
    get_employee_by_id,
    get_all_employees_in_department,
    remove_employee_by_id
)

@allure.feature("Employee Management")
@allure.story("Add & Retrieve")
@allure.severity(allure.severity_level.NORMAL)
def test_add_employee_and_retrieve():
    """Tests adding an employee and retrieving it by ID."""
    conn = create_in_memory_db()
    new_id = add_employee(conn, "Bob", "HR")
    row = get_employee_by_id(conn, new_id)
    assert row is not None, "Expected newly added employee to be found."  
    assert row[1] == "Bob", "Employee name should match."    
    assert row[2] == "HR",   "Employee department should match." 
    conn.close()

@allure.feature("Employee Management")
@allure.story("Retrieve")
@allure.severity(allure.severity_level.TRIVIAL)
def test_get_employee_by_id_not_found():
    """Tests that looking up a non-existent ID returns None."""
    conn = create_in_memory_db()
    row = get_employee_by_id(conn, 9999)
    assert row is None, "Should get None if employee doesn't exist."    
    conn.close()

@allure.feature("Employee Management")
@allure.story("Query By Department")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_employees_in_department():
    """Tests retrieving all employees in a department."""
    conn = create_in_memory_db()
    add_employee(conn, "Carol", "Marketing")
    add_employee(conn, "Dave", "Marketing")
    add_employee(conn, "Eve", "Engineering")

    marketing_emps = get_all_employees_in_department(conn, "Marketing")
    assert len(marketing_emps) == 2, "There should be exactly 2 employees in Marketing."  
    names = [emp[1] for emp in marketing_emps]
    assert set(names) == {"Carol", "Dave"}, "Expected Carol and Dave in Marketing." 
    conn.close()

@allure.feature("Employee Management")
@allure.story("Removal")
@allure.severity(allure.severity_level.CRITICAL)
def test_remove_employee_by_id():
    """Tests removing an employee by ID."""
    conn = create_in_memory_db()
    emp_id = add_employee(conn, "Frank", "Engineering")
    removed = remove_employee_by_id(conn, emp_id)
    assert removed, "Expected removal of existing employee."  
    row = get_employee_by_id(conn, emp_id)
    assert row is None, "Employee should no longer exist."  
    conn.close()

@allure.feature("Employee Management")
@allure.story("Removal")
@allure.severity(allure.severity_level.NORMAL)
def test_remove_non_existent_employee():
    """Tests removing a non-existent employee returns False."""
    conn = create_in_memory_db()
    removed = remove_employee_by_id(conn, 9999)
    assert not removed, "Should return False when ID doesn't exist."  
    conn.close()
