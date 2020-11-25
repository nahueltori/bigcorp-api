import json
import requests
# from api.model.employee import Employee


URL_EMPLOYEES = "https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees"

cachedEmployees = {}
expandEmployees = {}


def addEmployees(list):
    for element in list:
        cachedEmployees[element["id"]] = element


def getEmployeesSource(limit=None, offset=None, id=[]):
    query = {}
    if limit:
        query['limit'] = limit
    if offset:
        query["offset"] = offset
    for item in id:
        query["id"] = item

    resp = requests.get(URL_EMPLOYEES, params=query)

    listEmployees = json.loads(resp.text)
    addEmployees(listEmployees)
    return listEmployees

def requestOffice(fieldId, employeeObj):
    if fieldId in cachedEmployees:
        manager = Employee().from_dict(cachedEmployees[fieldId])
        setattr(employeeObj, 'manager', manager)
    else:
        expandEmployees[fieldId] = employeeObj
    
