from random import randint
from copy import deepcopy

try:
    N = int(input("MATRIX SIZE = "))
    K = int(input("INSERT COEFFICIENT (2 or 3) = "))
except Exception:
    print("Numbers should be integers!")
print(" ")

if not N > 0 or not 2 <= K <= 3:
    K = 0


field = []
ELEMENTS = [1, 2, 3, 4, 5]


def fillField():
    for i in range(N):
        field.append([0] * N)


def printMatrix():
    for row in field:
        print(row, end='\n')
    print(" ")


def insertElements():
    for i in range(0, N):
        for j in range(0, N):
            if field[i][j] == 0:
                field[i][j] = ELEMENTS[randint(0, 4)]


def shiftMatrix():
    for z in range(N):
        for i in range(N):
            for j in range(N):
                if field[i][j] == 0:
                    if i == 0 or (i == 1 and field[i - 1][j] == 0):
                        continue
                    else:
                        field[i][j] = field[i - 1][j]
                        field[i - 1][j] = 0


def isChanged() -> bool:
    global field_copy

    for i in range(N):
        for j in range(N):
            if not field[i][j] == field_copy[i][j]:
                return True
    return False


def check():
    global field_copy
    if K == 2:
        for i in range(N - 1):
            for j in range(N - 1):
                if field[i][j] == field[i][j + 1]:
                    field[i][j] = 0
                    field[i][j + 1] = 0
                    shiftMatrix()
                if field[i][j] == field[i + 1][j]:
                    field[i][j] = 0
                    field[i + 1][j] = 0
                    shiftMatrix()
                if isChanged():
                    field_copy = deepcopy(field)
    if K == 3:
        for i in range(N - 2):
            for j in range(N - 2):
                if field[i][j] == field[i][j + 1] == field[i][j + 2]:
                    field[i][j] = 0
                    field[i][j + 1] = 0
                    field[i][j + 2] = 0
                    shiftMatrix()
                if field[i][j] == field[i + 1][j] == field[i + 2][j]:
                    field[i][j] = 0
                    field[i + 1][j] = 0
                    field[i + 2][j] = 0
                    shiftMatrix()
                if isChanged():
                    field_copy = deepcopy(field)





fillField()
insertElements() 
printMatrix() 

field_copy = deepcopy(field) 
for i in range(N): 
    check()
printMatrix() 
