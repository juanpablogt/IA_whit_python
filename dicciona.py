alien0 = {'color':'azul','altura':1.55, 'ropa':'ninguna'}
alien1 = {'color':'azul','altura':1.56, 'ropa':'pantalones'}
alien2 = {'color':'azul','altura':1.57, 'ropa':'ninguna'}
alien3 = {'color':'azul','altura':1.58, 'ropa':'camisa'}

aliens = [alien0,alien1,alien2,alien3]

for list in aliens:
    print(list)

prompt = "Ingrese el nombre: "

name = input(prompt)
print("el nombre es: " + name)