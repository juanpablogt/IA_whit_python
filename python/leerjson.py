import json


with open(r'python/json.json') as datos:
    empleado = json.load(datos) 

    sum = empleado['edad'] +30

    print(sum)