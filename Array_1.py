from array import *

countOdd = sumEven = sumRow = sumCol = sumDiag = 0


TD = [[3,7,2,4,5,8], [4,3,7,1,4,2],
      [2,5,3,8,9,7], [1,7,4,1,5,2],
      [8,9,6,3,1,8], [6,8,2,5,9,4]]

for m in TD:
    for i in m: 
        if i % 2 == 1:
            countOdd += 1
print("Count all odd numbers: ", countOdd)

for m in TD:
    for j in m:
        if j % 2 == 0:
            sumEven += j
print("Sum of even numbers: ", sumEven)

xSum = int(input("Enter row: "))
for m in TD[xSum]:
    sumRow += m
print(f'Sum of row {xSum}: {sumRow}')

y = int(input("Enter column: "))
for m in range(6):
    innerColumn = TD[m][y] 
    sumCol += innerColumn
colAvg = sumCol / 6
print(f'Average of column {y}: {colAvg}')

diagonalTD = [3,3,3,1,1,4]
for i in diagonalTD:
    sumDiag += i
print(f'Sum of Diagonal: {sumDiag}')

rowRev = []
xRev = int(input("Enter row to reverse: "))
for m in TD[xRev]:
    rowRev.append(m)
rowRev.reverse()
print(f'Output: {rowRev}')

rowSort = []
xSort = int(input("Enter row to sort: "))
for m in TD[xSort]:
    rowSort.append(m)
rowSort.sort()
print(f'Output: {rowSort}')

with open("Result.txt", "w+") as file:
    file.write(f'Count all odd numbers: {countOdd}\n')
    file.write(f'Sum of even numbers: {sumEven}\n')
    file.write(f'Sum of row {xSum}: {sumRow}\n')
    file.write(f'Average of column {y}: {colAvg}\n')
    file.write(f'Sum of Diagonal: {sumDiag}\n')
    file.write(f'Reverse of output of row {xRev}: {rowRev}\n')
    file.write(f'Sort of output of row {xSort}: {rowSort}')
file.close()







    


