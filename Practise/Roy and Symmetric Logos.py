def check_xaxis(size, matrix):
    for rows in range(size//2):
        if matrix[rows] != matrix[(size-1) - rows]:
            return 0
    return 1

def check_yaxis(size, matrix):
    for rows in matrix:
        for item in range(size//2):
            if rows[item] != rows[(size-1)-item]:
                return 0
    return 1
mat = [[1,1,1],[1,1,1],[1,1,1]]

test = int(input())
for _ in range(test):

    size = int(input())
    matrix = []
    for _ in range(size):
        row = [i for i in str(input())]#list(map(int, input().split()))
        matrix.append(row)
    if check_xaxis(size, matrix) and check_yaxis(size, matrix):
        print('YES')
    else:
        print('NO')