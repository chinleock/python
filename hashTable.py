class HashTable(object):
    def __init__(self, ids = [], values = []):
        self.ID = {}
        if len(ids) < len(values):
            self.msg = 'Missing IDs'
        elif len(ids) > len(values):
            self.msg = 'Missing Values'
        else:
            for i, oid in enumerate(ids):
                self.ID[oid] = values[i]
            self.msg = str(self.ID)
    def __str__(self):
        return self.msg

    def listKeys(self):
        for key in self.ID.keys():
            print(key)
    def listValues(self):
        for key, value in self.ID.items():
            print(value)
    def __getitem__(self, oid):
        return self.ID[oid]


if __name__ == '__main__':
    ht = HashTable(["John", "Eva", "Joe"],[5,7,9])
    print(ht)
    print(ht.listKeys())
    print(ht.listValues())
    print(ht["John"])