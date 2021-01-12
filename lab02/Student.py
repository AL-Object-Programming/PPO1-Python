class Student:
    name = ''
    last_name = ''
    index = 0
    status = False

    def __init__(self, name, last_name, index, status):
        self.name = name
        self.last_name = last_name
        self.index = index
        self.status = status
