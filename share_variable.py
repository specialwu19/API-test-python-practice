import json

def read():
    with open("data.json" , "r") as file:
        data = json.load(file)
        return data

# read()

def write(str):
    with open("data.json" , "w") as file:
        file.write(str)
# write()
        
def add_variable(key,value):
    original=read()
    original[key] = value
    write(json.dumps(original))
    return original

def get_variable(key):
    original=read()
    return original.get(key)

