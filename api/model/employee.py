from api.model.department import Department
from api.model.office import Office
from api.model.resource import ResourceList
from api.model.employeeDatasource import requestManager
from api.model.localDatasource import requestDepartment, requestOffice


class Employee():
    def __init__(self):
        self.first = None
        self.last = None
        self.id = None
        self.manager = None
        self.department = None
        self.office = None

    def __str__(self):
        return "{}".format(self.to_dict())
        
    def from_dict(self, data):
        for field in ['first', 'last', 'id', 'manager', 'department', 'office']:
            if field in data:
                setattr(self, field, data[field])
        return self

    def to_dict(self):
        if type(self.manager) == Employee:
            manager_dict = self.manager.to_dict()
        else:
            manager_dict = self.manager
        if type(self.department) == Department:
            dept_dict = self.department.to_dict()
        else:
            dept_dict = self.department
        if type(self.office) == Office:
            office_dict = self.office.to_dict()
        else:
            office_dict = self.office

        return {
            'first': self.first,
            'last': self.last,
            'id': self.id,
            'manager': manager_dict,
            'department': dept_dict,
            'office': office_dict
        }

    def expand(self, expandLists, force=False):
        # Para cada una de los parametros expand
        for expandList in expandLists:
            print(expandList)
            if expandList:      # Si hay más para expandir
                
                for field in ['manager', 'department', 'office']:       # Para cada campo expandible en el Employee
                    fieldId = getattr(self, field)
                    if field == expandList[0] and fieldId:     # Sólo expando si el campo tiene datos

                        if field == 'manager':
                            manager = Employee()
                            subexpand = list(expandList)
                            if len(subexpand) > 0:
                                subexpand.pop(0)
                            requestManager(fieldId, manager, [subexpand], force)
                            self.manager = manager

                        elif field == 'department':
                            dept = Department()
                            requestDepartment(fieldId, dept)
                            self.department = dept
                            if len(expandList) > 0:
                                subexpand = list(expandList)
                                subexpand.pop(0)
                                dept.expand([subexpand])

                        else:
                            office = Office()
                            requestOffice(fieldId, office)
                            self.office = office
            print(expandList)



class EmployeeList(ResourceList):
    def __init__(self):
        self.list = []
    
    def load_data(self, data):
        for element in data:
            empleado = Employee()
            empleado.from_dict(element)
            self.list.append(empleado)

