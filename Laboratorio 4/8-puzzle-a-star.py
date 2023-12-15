import heapq
import time
import numpy as np

# Definimos el estado objetivo del puzzle 8
TARGET = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def manhattan_distance(state):
    # Calcula la distancia Manhattan desde un estado hasta el objetivo.
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i, j] != 0:  # Ignora el espacio vacío
                # Obtiene la posición del número en el estado objetivo
                target_i, target_j = divmod(state[i, j] - 1, 3)
                # Suma la distancia Manhattan para el número actual
                distance += abs(i - target_i) + abs(j - target_j)
    return distance


def get_possible_moves(state):
    """Genera todos los movimientos posibles desde un estado dado."""
    possible_moves = []
    # Encuentra la posición del 0 (espacio vacío)
    i, j = np.where(state == 0)
    i, j = i[0], j[0]

    # Definimos los posibles movimientos como (di, dj) donde d es la dirección en la que se mueve el 0
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        # Verifica que los nuevos índices estén dentro de los límites del tablero
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = state.copy()
            # Realiza el movimiento
            new_state[i, j], new_state[ni, nj] = new_state[ni, nj], new_state[i, j]
            possible_moves.append(new_state)

    return possible_moves


def a_star_search(initial_state):
    """Implementa el algoritmo A* para encontrar la solución al puzzle 8."""
    # Usa una cola de prioridad para almacenar los nodos
    pq = []
    # Crea el nodo inicial y lo añade a la cola
    initial_node = Node(initial_state, None, 0, manhattan_distance(initial_state))
    heapq.heappush(pq, initial_node)

    # Usa un conjunto para almacenar los estados explorados
    explored = set()

    while pq:
        # Obtiene el nodo con el menor valor de f de la cola
        current_node = heapq.heappop(pq)
        current_state = current_node.state

        # Si el estado actual es el objetivo, reconstruye el camino y lo retorna
        if np.array_equal(current_state, TARGET):
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        # Marca el estado actual como explorado
        explored.add(tuple(current_state.flatten()))

        # Genera los sucesores del estado actual
        for move in get_possible_moves(current_state):
            # Si el sucesor ya ha sido explorado, lo ignora
            if tuple(move.flatten()) in explored:
                continue
            # Crea un nuevo nodo y lo añade a la cola
            new_node = Node(move, current_node, current_node.g + 1, manhattan_distance(move))
            heapq.heappush(pq, new_node)

    # Si la cola está vacía y no se ha encontrado una solución, retorna None
    return None


if __name__ == '__main__':
    # Ejemplo de estado inicial
    initial_state = np.array([[8, 1, 6], [5, 4, 7], [2, 3, 0]])

    # Tiempo inicial
    start_time = time.time()
    # Buscar la solución
    solution_path = a_star_search(initial_state)
    # Tiempo final
    end_time = time.time()

    # Imprimir la solución
    print("Pasos para llegar al objetivo: \n")
    for state in solution_path:
        print(state, "\n")

    print(f"Solución encontrada en {len(solution_path)} pasos")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
