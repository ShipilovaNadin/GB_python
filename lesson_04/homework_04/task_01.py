# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 4],
          [31, 17, 15],
          [31, 17, 15]]

trans_matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
for a in range(len(matrix)):
    for b in range(len(matrix[0])):
        trans_matrix[b][a] = matrix[a][b]

print("The transpose of matrix is: ")

for res in trans_matrix:
    print(res)

# вариант 2
def turn_matrix(data: list):
    """ Function transposes rectangular and square matrix"""

    turned_matrix = []
    for _ in range(0, len(data[0])):
        turned_matrix.append([])
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            turned_matrix[j].append(data[i][j])
    return turned_matrix


def print_matrix(data: list):
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            print(f"{data[i][j]} ", end="")
        print()


my_matrix = [[1, 2, 3],
             [4, 5, 6]]
print("Заданная матрица:")
print_matrix(my_matrix)

print("Транспонированная матрица:")
print_matrix(turn_matrix(my_matrix))