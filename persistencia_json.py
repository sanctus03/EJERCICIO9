import json

def store(variable, nombrearchivo):
    variable = input(print("introduce la varibale cualquiera: "))
    nombrearchivo = input(print("introduce el nombre del archivo: "))
    json.dump(json.dumps(nombrearchivo), open(nombrearchivo, "w"))
def retrieve(nombrearchivo):
    return json.load
