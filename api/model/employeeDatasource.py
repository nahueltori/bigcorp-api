import json
import requests


URL_EMPLOYEES = "https://rfy56yfcwk.execute-api.us-west-1.amazonaws.com/bigcorp/employees"

cachedEmployees = {}
findEmployees = {}
expandEmployees = {}


def cacheEmployees(list):
    for element in list:
        cachedEmployees[element["id"]] = element


def getEmployeesSource(limit=None, offset=None, id=[]):
    query = {}
    id_values=[]
    if limit:
        query['limit'] = limit
    if offset:
        query["offset"] = offset
    for item in id:
        id_values.append(item)
        query["id"] = id_values

    print("LLAMANDO API de EMPLOYEES con parámetros: ")
    print(query)
    resp = requests.get(URL_EMPLOYEES, params=query)

    listEmployees = json.loads(resp.text)
    cacheEmployees(listEmployees)
    return listEmployees


def requestManager(fieldId, managerObj, subexpand, force=False):
    if force:                                   # If force, busca al employee con la API
        getEmployeesSource(id=[fieldId])

    if fieldId in cachedEmployees:
        managerObj.from_dict(cachedEmployees[fieldId])
        if subexpand:
            managerObj.expand(subexpand)
    else:
        findEmployees[fieldId] = True
        expandEmployees[managerObj] = [fieldId, subexpand]


def flushCachedEmployees():
    cachedEmployees.clear()


def finishExpandEmployees():
    if expandEmployees:
        getEmployeesSource(id=findEmployees.keys())
        for manager, values in expandEmployees.items():
            manager.from_dict(cachedEmployees[values[0]])   # Values[0] tiene el field id
            if values[1]:                                   # Values[1] tiene la lista de subexpand
                manager.expand(values[1], force=True)

    flushCachedEmployees()

