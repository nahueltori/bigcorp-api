from api.model.resource import ResourceList
from api.model.localDatasource import requestDepartment

class Department:
    def __init__(self):
        self.id = None
        self.name = None
        self.superdepartment = None

    def __str__(self):
        return "{}".format(self.to_dict())
        
    def from_dict(self, data):
        for field in ['id', 'name', 'superdepartment']:
            if field in data:
                setattr(self, field, data[field])
        return self

    def to_dict(self):
        if type(self.superdepartment) == Department:
            superdepartment_dict = self.superdepartment.to_dict()
        else:
            superdepartment_dict = self.superdepartment

        return {
            'id': self.id,
            'name': self.name,
            'superdepartment': superdepartment_dict
        }

    def expand(self, expandLists):
        # Para cad una de los parametros expand
        for expandList in expandLists:
            if expandList[0] == 'superdepartment' and self.superdepartment:     # Sólo expando si el campo tiene datos
                superdept = Department()
                requestDepartment(self.superdepartment, superdept)
                self.superdepartment = superdept
                if len(expandList) > 1:
                    subexpand = list(expandList)
                    subexpand.pop(0)
                    superdept.expand([subexpand])


class DepartmentList(ResourceList):
    def __init__(self):
        self.list = []

    def load_data(self, data):
        for element in data:
            dept = Department()
            dept.from_dict(element)
            self.list.append(dept)

