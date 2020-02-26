#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", 'index weight value')

import itertools
import functools

def trivial_greedy(items, capacity):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

## TODO: ¡¡¡AGREGA  AQUÍ TUS FUNCIONES!!!

def evaluate_solution(solution):
    return functools.reduce(lambda x, value: x + value.value, solution, 0)

#Greedy -> Los artículos de mayor valor primero
def greedy_algorithm(things, capacity):
    sorted_things = sorted(things, key=lambda item: item.value, reverse=True)
    
    value = 0
    weight =0
    taken = [0]*len(things)
    

    for thing in sorted_things:
        if thing.weight <= capacity:
            taken[thing.index] = 1
            value += thing.value
            capacity -= thing.weight

    output_data = str(value) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

#Density greedy -> Artículos de mayor densidad primero

#density_greedy = functools.partial(greedy_algorithm, things=item.value/item.weight, capacity)

def density_greedy(things, capacity):
    sorted_things = sorted(things, key=lambda item: item.value/item.weight, reverse=True)
    
    value = 0
    weight =0
    taken = [0]*len(things)
    

    for thing in sorted_things:
        if thing.weight <= capacity:
            taken[thing.index] = 1
            value += thing.value
            capacity -= thing.weight

    output_data = str(value) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

#Programación dinámica

def knapsack_td(items, capacity):
    # """ Resuelve el problema del knapsack utilizando recursividad  de con memoizacion.
    #  things es una lista de namedtuples de la forma (name, weight, value)"""
    taken = [0]*len(items)
    @functools.lru_cache(maxsize=None)
    def best_value(i, capacity):
        # Return the value of the most valuable subsequence of the first
        # i elements in items whose weights sum to no more than capacity.
        if capacity < 0:
            return float('-inf')
        if i == 0:
            return 0
        _, weight, value  = items[i - 1]
        return max(best_value(i - 1, capacity), best_value(i - 1, capacity - weight) + value)

    j = capacity
    
    for i in reversed(range(len(items))):
        if best_value(i + 1, j) != best_value(i, j):
            j -= items[i][1]
            taken[i]=1
            
    output_data = str(best_value(len(items), capacity)) + '\n'
    output_data += ' '.join(map(str, taken))

    return output_data

## TODO: Modifica este diccionario
algorithms = {'trivial_greedy': trivial_greedy, 'knapsack_td':knapsack_td,
              'greedy_algorithm': greedy_algorithm, 'density_greedy': density_greedy}

def solve_it(input_data, algorithm=trivial_greedy):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[1]), int(parts[0])))

    output_data = algorithm(items, capacity)

    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        file_location = sys.argv[1].strip()
        algorithm = algorithms[sys.argv[2].strip()]

        print(f"Ejecutando el algoritmo {algorithm} en {file_location}")
        
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data, algorithm))
    else:
        print("""Este script requiere dos argumentos: \n"""
              """El archivo con los datos del problema y el nombre del algoritmo que diseñaste.\n"""
              """i.e. python solver.py ./data/ks_4_0 trivial_greedy""")
