import os
from api import create_app

def load_file(file_dir):
    data = ""
    filepath = os.path.abspath(os.path.dirname(__file__)) + file_dir
    with open(filepath, "r") as f:
        data = f.read()
    return data

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/')
    assert response.data == b'Running OK'


def test_employee(client):
    response = client.get('/api/v1/employees')
    expectedData = format(load_file('/tests/get_employees.json'))
    assert response.data == expectedData.encode('UTF-8')


def test_employee_limit_offset(client):
    response = client.get('/api/v1/employees?limit=10&offset=3')
    expectedData = format(load_file('/tests/get_employees_limit_offset.json'))
    assert response.data == expectedData.encode('UTF-8')


def test_employee_100(client):
    response = client.get('/api/v1/employees/100')
    expectedData = format(load_file('/tests/get_employee_100.json'))
    assert response.data == expectedData.encode('UTF-8')

def test_employee_100_expanded(client):
    response = client.get('/api/v1/employees/100?expand=manager.office&expand=department.superdepartment')
    expectedData = format(load_file('/tests/get_employee_100_expanded.json'))
    assert response.data == expectedData.encode('UTF-8')


def test_departments(client):
    response = client.get('/api/v1/departments')
    expectedData = format(load_file('/tests/get_departments.json'))
    assert response.data == expectedData.encode('UTF-8')


def test_departments_expanded(client):
    response = client.get('/api/v1/departments?expand=superdepartment')
    expectedData = format(load_file('/tests/get_departments_expanded.json'))
    assert response.data == expectedData.encode('UTF-8')


def test_department_8(client):
    response = client.get('/api/v1/departments/8')
    expectedData = format(load_file('/tests/get_department_8.json'))
    assert response.data == expectedData.encode('UTF-8')


def test_offices(client):
    response = client.get('/api/v1/offices')
    expectedData = format(load_file('/tests/get_offices.json'))
    assert response.data == expectedData.encode('UTF-8')


def test_office_3(client):
    response = client.get('/api/v1/offices/3')
    expectedData = format(load_file('/tests/get_office_3.json'))
    assert response.data == expectedData.encode('UTF-8')
