import json


DEPT_FILE = "static/departments.json"
OFFICE_FILE = "static/offices.json"
dept_data = {}
office_data = {}


def load_file(file):
    res_data = []
    with open(file, 'r') as f:
        data = f.read()
        res_data = json.loads(data)
    return res_data


def getResourceById(data, id):
    returnList = [v for (k,v) in data.items() if k in id]
    return returnList
    

def getResourcesList(data, limit, offset):
    if not limit:
        limit = 100
    if not offset:
        offset = 0
    offset = int(offset)
    limit = int(limit) + offset
    values = list(data.values())
    return values[offset:limit]


def getDepartmentSource(limit=None, offset=None, id=[]):
    if not dept_data:
        dept_list = load_file(DEPT_FILE)
        for item in dept_list:
            dept_data[item["id"]] = item

    if id:
        return getResourceById(dept_data, id)

    if limit or offset:
        return getResourcesList(dept_data, limit, offset)

    return []


def getOfficeSource(limit=None, offset=None, id=[]):
    if not office_data:
        office_list = load_file(OFFICE_FILE)
        for item in office_list:
            office_data[item["id"]] = item

    if id:
        return getResourceById(office_data, id)

    if limit or offset:
        return getResourcesList(office_data, limit, offset)

    return []


def requestDepartment(fieldId, deptObj):
    deptList = getDepartmentSource(id=[fieldId])
    deptObj.from_dict(deptList[0])

def requestOffice(fieldId, officeObj):
    officeList = getOfficeSource(id=[fieldId])
    officeObj.from_dict(officeList[0])
