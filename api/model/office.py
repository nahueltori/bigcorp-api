from api.model.resource import ResourceList

class Office:
    def __init__(self):
        self.id = None
        self.city = None
        self.country = None
        self.address = None

    def __str__(self):
        return "{}".format(self.to_dict())
        
    def from_dict(self, data):
        for field in ['id', 'city', 'country', 'address']:
            if field in data:
                setattr(self, field, data[field])
        return self

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'country': self.country,
            'address': self.address
        }


class OfficeList(ResourceList):
    def __init__(self):
        self.list = []

    def load_data(self, data):
        for element in data:
            office = Office()
            office.from_dict(element)
            self.list.append(office)

