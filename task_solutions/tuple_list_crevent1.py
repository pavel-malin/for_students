lists = {
    'Австралия': 127.0,
    'Австрия': 47.2,
    'Алжир': 28.0, 
    }

def tuple_list():
    it = input('Count< WIDTH: ')
    for key, value in lists.items():
        if it == key:
            print(key + ': ' + str(value))

        if it == str(value):
            print(key + ': ' + str(value))
    
tuple_list()