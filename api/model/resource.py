
class ResourceList():
    def __init__(self):
        self.list = []
    
    def to_collection(self):
        return [item.to_dict() for item in self.list]

    def expandFields(self, expandLists):
        for item in self.list:
            item.expand(expandLists)
