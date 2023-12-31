# -*- coding: utf-8 -*-
"""ProyectoIA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bopRi8DFND-PHOij4YNaaB67Po97AqQp
"""

import heapq  # Importa el módulo heapq para manejar una cola de prioridad.
import time  # Importa el módulo time para medir la duración de la ejecución.
import numpy as np  # Importa numpy para trabajar eficientemente con matrices.

# Define el estado objetivo del rompecabezas como una matriz 4x4.
TARGET = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

# Crea un diccionario para mapear cada número a su posición objetivo.
TARGET_POS = {TARGET[i, j]: (i, j) for i in range(4) for j in range(4)}

class Node:
    # Representa un nodo en el espacio de búsqueda.
    def __init__(self, state, parent, g, h):
        # Inicializa un nodo.
        self.state = state  # Estado actual del rompecabezas.
        self.parent = parent  # Nodo padre en el camino de búsqueda.
        self.g = g  # Costo desde el estado inicial hasta el actual.
        self.h = h  # Estimación heurística desde el estado actual hasta el objetivo.
        self.f = g + h  # Costo total estimado (f = g + h).

    def __lt__(self, other):
        # Define la comparación de menor que para la cola de prioridad.
        return self.f < other.f

def manhattan_distance(state):
    # Calcula la distancia de Manhattan como heurística.
    distance = 0
    for i in range(4):
        for j in range(4):
            if state[i, j] != 0:
                # Para cada número, calcula la distancia a su posición objetivo.
                target_i, target_j = TARGET_POS[state[i, j]]
                distance += abs(i - target_i) + abs(j - target_j)
    return distance

def get_possible_moves(state, last_zero_pos):
    # Devuelve los posibles movimientos desde el estado actual.
    possible_moves = []
    i, j = np.where(state == 0)  # Encuentra la posición de la pieza vacía (0).
    i, j = i[0], j[0]

    # Explora los movimientos en las cuatro direcciones.
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        # Verifica si el movimiento es válido y evita regresar a la posición anterior.
        if 0 <= ni < 4 and 0 <= nj < 4:
            if last_zero_pos is None or (ni, nj) != last_zero_pos:
                new_state = np.copy(state)
                # Realiza el movimiento intercambiando la pieza vacía con la adyacente.
                new_state[i, j], new_state[ni, nj] = new_state[ni, nj], new_state[i, j]
                possible_moves.append((new_state, (i, j)))
    return possible_moves

def a_star_search(initial_state):
    # Implementa el algoritmo de búsqueda A*.
    pq = []  # Cola de prioridad para los nodos a explorar.
    initial_node = Node(initial_state, None, 0, manhattan_distance(initial_state))
    heapq.heappush(pq, initial_node)  # Agrega el nodo inicial a la cola.
    explored = set()  # Conjunto para almacenar los estados ya explorados.

    while pq:
        current_node = heapq.heappop(pq)  # Toma el nodo con el menor costo f.
        current_state = current_node.state

        # Verifica si el estado actual es el estado objetivo.
        if np.array_equal(current_state, TARGET):
            path = []
            # Reconstruye el camino desde el estado inicial hasta el objetivo.
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Devuelve el camino en orden correcto.

        # Agrega el estado actual a los explorados.
        explored.add(str(current_state.flatten()))

        # Determina la posición de la pieza vacía en el nodo padre.
        last_zero_pos = None
        if current_node.parent:
            parent_zero_pos = np.where(current_node.parent.state == 0)
            if parent_zero_pos[0].size > 0:
                last_zero_pos = (parent_zero_pos[0][0], parent_zero_pos[1][0])

        # Explora los movimientos posibles desde el estado actual.
        for move, _ in get_possible_moves(current_state, last_zero_pos):
            if str(move.flatten()) in explored:
                continue
            # Crea un nuevo nodo y lo agrega a la cola de prioridad.
            new_node = Node(move, current_node, current_node.g + 1, manhattan_distance(move))
            heapq.heappush(pq, new_node)

    return None  # Retorna None si no se encuentra una solución.

if __name__ == '__main__':
    # Define el estado inicial y ejecuta la búsqueda A*.
    initial_state = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [0, 10, 11, 12], [13, 14, 15, 9]])

    start_time = time.time()  # Inicia el cronómetro.
    solution_path = a_star_search(initial_state)  # Ejecuta la búsqueda A*.
    end_time = time.time()  # Detiene el cronómetro.

    # Imprime cada paso de la solución y estadísticas de la ejecución.
    print("Pasos para llegar al objetivo: \n")
    for state in solution_path:
        print(state, "\n")

    print(f"Solución encontrada en {len(solution_path)} pasos")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")