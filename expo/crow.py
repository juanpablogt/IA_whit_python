import random
ram2
# Parámetros del algoritmo

main
def objective_function(x):

    return x ** 2  # Ejemplo de una función simple (x^2).

# Parámetros del algoritmo
N = 50  # Tamaño de la población (número de cuervos)
T = 100  # Número máximo de iteraciones
fl = 0.1  # Longitud de vuelo
AP = 0.5  # Probabilidad de conciencia

# Inicialización de la población de cuervos
population = [random.uniform(-10, 10) for _ in range(N)]  
# recuerdos de los cuervos
memories = [None] * N

# Bucle principal
t = 0
while t < T:
    for i in range(N):
        # Elegir aleatoriamente a un cuervo a seguir
        j = random.randint(0, N - 1)
        
        # Generar rj
        rj = random.random()
        
        if rj >= AP:
            # Mover al cuervo en la dirección del cuervo seguido
            step = random.uniform(-fl, fl)
            new_position = population[j] + step
            
            # Comprobar la viabilidad de la nueva posición
            if -10 <= new_position <= 10:
                population[i] = new_position
        else:
            # Mover al cuervo a un lugar aleatorio en el espacio de búsqueda
            population[i] = random.uniform(-10, 10)
        
        # Evaluar la nueva posición y actualizar los recuerdos
        current_value = objective_function(population[i])
        if memories[i] is None or current_value < objective_function(memories[i]):
            memories[i] = population[i]
    
    t += 1

# Encontrar la mejor solución
best_solution = min(population, key=objective_function)
best_value = objective_function(best_solution)

print(f"Mejor solucion encontrada: {best_solution}")
print(f"Valor objetivo optimo: {best_value}")