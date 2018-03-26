
class Politician(object):
    def __init__(self, name, number, status):
        self.name = name
        self.number = number
        self.status = status

    def print_data(self):
        print(self.name + " " + self.status)
