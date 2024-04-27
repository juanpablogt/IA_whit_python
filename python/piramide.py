altura = 9

for i in range(altura):
    # Imprimir espacios en blanco para alinear la pirámide
    print(" " * (altura - i - 1), end="")
    
    # Imprimir números ascendentes en la pirámide
    for j in range(i + 1):
        print(j + 1, end="")
    
    # Imprimir números descendentes en la pirámide
    for k in range(i, 0, -1):
        print(k, end="")
    
    # Cambiar de línea para el siguiente nivel de la pirámide
    print()
