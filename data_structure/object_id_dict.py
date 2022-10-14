class ObjectIdDict(dict):

    def __setitem__(self, key, value):
        super(ObjectIdDict, self).__setitem__(id(key), value)

    def __getitem__(self, key):
        return super(ObjectIdDict, self).__getitem__(id(key))




print()

