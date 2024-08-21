from itertools import product



file = input("Digite qual txt File deseja usar... (data.txt, data1.txt, data2.txt): ")


def read(file):
    with open(file, 'r') as f:
        lines = f.read().splitlines()

    num_operation = int(lines[0])
    i = 1

    for j in range(num_operation):
 

        operation = lines[i].strip()
        set1 = set(lines[i + 1].split(','))
        set2 = set(lines[i + 2].split(','))
        i += 3


        if operation == 'U':
            resultado = set1 | set2  
            print(f"União: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}.")


        elif operation == 'I':
            resultado = set1 & set2  
            print(f"Interseção: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}.")


        elif operation == 'D':
            resultado = set1 - set2  
            print(f"Diferença: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}.")


        elif operation == 'C':
            resultado = set(product(set1, set2))  # produc "multiplicar"
            print(f"Produto cartesiano: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}.")


read(file)