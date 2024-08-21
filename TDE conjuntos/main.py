from itertools import product

file = input("Digite qual txt File deseja usar... (data.txt, data1.txt, data2.txt): ")

def read(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    num_operation = int(lines[0])
    i = 1

    while num_operation > 0:
        operation = lines[i].strip()
        set1 = set(lines[i + 1].split(','))
        set2 = set(lines[i + 2].split(','))
        i += 3

        if operation == 'U':
            print(f"União: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {set1 | set2}.")

        elif operation == 'I':
            print(f"Interseção: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {set1 & set2}.")

        elif operation == 'D':
            print(f"Diferença: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {set1 - set2}.")


        elif operation == 'C':
            print(f"Produto cartesiano: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {set(product(set1, set2))}.")
        
        num_operation -= 1

read(file)
