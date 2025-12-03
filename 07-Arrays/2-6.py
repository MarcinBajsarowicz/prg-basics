matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]


for i in range(len(matrix)):
    matrix[i][i] = 1

for row in matrix:
    line = ""
    for num in row:
        line += str(num) + " "
    print(line)