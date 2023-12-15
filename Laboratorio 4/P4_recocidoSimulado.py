import math
import random

# f(x) a minimizar
def f1(x):
    return x**4 + 3*x**3 + 2*x**2 - 1

def f2(x):
    return x**2 - 3*x - 8

# Función de recocido simulado
def simulated_annealing(func, initial_state, T, T_MIN, cooling_rate, num_iterations):
    current_state = initial_state
    best_state = current_state

    while T > T_MIN:
        for i in range(num_iterations):
            # Estado vecino: La idea es explorar las soluciones cercanas al estado actual
            neighbor = current_state + random.uniform(-0.1, 0.1)
            
            # Diferencia entre la función objetivo en el nuevo estado y el estado actual
            delta = func(neighbor) - func(current_state)

            # Si el nuevo estado es mejor o es aceptado con una probabilidad, actualízalo
            if delta < 0 or random.random() < math.exp(-delta / T):
                current_state = neighbor

            # Actualizar la mejor solución encontrada
            if func(current_state) < func(best_state):
                best_state = current_state
        
        # Enfriar la temperatura
        T *= cooling_rate

    return best_state

# Parámetros del algoritmo
initial_state = 0.0  # Estado inicial
T = 100.0            # Temperatura inicial
T_MIN = 0.01         # Temperatura mínima
cooling_rate = 0.99  # Tasa de enfriamiento
num_iterations = 100 # Iteraciones por temperatura

# Primera funcion aplicacando el recocido simulado
best_solution_f1 = simulated_annealing(f1, initial_state, T, T_MIN, cooling_rate, num_iterations)
print("Mejor solución para f(x) = x^4 + 3x^3 + 2x^2 - 1:", best_solution_f1)
print("Valor mínimo encontrado:", f1(best_solution_f1))

# Segunda funcion aplicacando el recocido simulado
best_solution_f2 = simulated_annealing(f2, initial_state, T, T_MIN, cooling_rate, num_iterations)
print("\nMejor solución para f(x) = x^2 - 3x - 8:", best_solution_f2)
print("Valor mínimo encontrado:", f2(best_solution_f2))
 