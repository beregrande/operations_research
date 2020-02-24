#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", 'index weight value')

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

#Greedy (densidad)
def greedy_algorithm(things, capacity):
    sorted_things = {k: v for k,v in sorted(things.items(), key=lambda item: item[1][1], reverse=True)}

    knapsack = {}

    for thing in sorted_things.items():
        if thing[1][0] <= capacity:
            knapsack.update({thing[0]: thing[1]})
            capacity -= thing[1][0]

    return {'solution': knapsack, 'value': evaluate_solution(knapsack)}
import itertools
import functools

#Fuerza bruta


## TODO: Modifica este diccionario
algorithms = {'trivial_greedy': trivial_greedy, 'greedy_algorithm': greedy_algorithm}

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
