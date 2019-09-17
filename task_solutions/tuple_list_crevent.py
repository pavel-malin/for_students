lists = {
    'Австралия': 127.0,
    'Австрия': 47.2,
    'Алжир': 28.0,
    }

class List_list:
    def __init__(self):
        self.lists = lists
        self.it = input('count: ')
        for key, value in lists.items():
            self.key = key
            self.value = value

    def strta(self):
        if self.it == self.key:
            print(self.key + ': ' + str(self.value))

    def floats(self):
        if self.it == str(self.value):
            print(self.key + ': ' + str(self.value))

listss = List_list()
listss.strta(), listss.floats()
