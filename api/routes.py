# -*- coding: UTF-8 -*-
from flask import Blueprint, request, jsonify
from api.model.employee import Employee, EmployeeList
from api.model.employeeDatasource import getEmployeesSource, finishExpandEmployees
from api.model.department import Department, DepartmentList
from api.model.office import Office, OfficeList
from api.model.localDatasource import getDepartmentSource, getOfficeSource


bp = Blueprint('api', __name__, url_prefix='/api/v1')


def getQueryParams():
    limit = 100
    offset = None
    expand = []
    args_dict = request.args.to_dict(flat=False)
    for k, v in args_dict.items():
        if k == "limit":
            limit = v[0]
        elif k == "offset":
            offset = v[0]
        elif k == "expand":
            for item in v:
                expand.append(item.split("."))
    return limit, offset, expand


@bp.route('/employees', methods=['GET'])
def getEmployeesList():
    limit, offset, expand = getQueryParams()
    listEmployees = EmployeeList()
    listEmployees.load_data(getEmployeesSource(limit, offset))
    listEmployees.expandFields(expand)
    finishExpandEmployees()
    return jsonify(listEmployees.to_collection())


@bp.route('/employees/<int:id>', methods=['GET'])
def getEmployee(id):
    limit, offset, expand = getQueryParams()
    employee = Employee()
    employee.from_dict(getEmployeesSource(id=[id])[0])
    employee.expand(expand)
    finishExpandEmployees()
    return employee.to_dict()


@bp.route('/departments', methods=['GET'])
def getDeparments():
    limit, offset, expand = getQueryParams()
    listDepartments = DepartmentList()
    listDepartments.load_data(getDepartmentSource(limit, offset))
    listDepartments.expandFields(expand)
    return jsonify(listDepartments.to_collection())


@bp.route('/departments/<int:id>', methods=['GET'])
def getDeparment(id):
    limit, offset, expand = getQueryParams()
    department = Department()
    department.from_dict(getDepartmentSource(id=[id])[0])
    department.expand(expand)
    return department.to_dict()


@bp.route('/offices', methods=['GET'])
def getOffices():
    limit, offset, expand = getQueryParams()
    listOffices = OfficeList()
    listOffices.load_data(getOfficeSource(limit, offset))
    return jsonify(listOffices.to_collection())


@bp.route('/offices/<int:id>', methods=['GET'])
def getOffice(id):
    office = Office()
    office.from_dict(getOfficeSource(id=[id])[0])
    return office.to_dict()
    
