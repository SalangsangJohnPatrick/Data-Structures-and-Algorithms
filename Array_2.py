from array import *

sortAsc = []
sumGreater = sumLess = sumOdd = 0
countLess = sumCol0 = sumCol1 = sumCol2 = sumCol3 = sumCol4 = 0
sumAll = 0

TD = [[1,2,3,4,5], [2,4,6,8,10],
      [25,15,45,36,20], [22,14,30,45,14],
      [17,15,26,34,20], [18,20,1,7,6]]

for m in TD:
    for i in m:
        if i > 20:
            sumGreater += i
print(sumGreater)

for m in TD:
    for i in m:
        if i < 10:
            sumLess += i
            countLess += 1
avgLess = sumLess / countLess
print(avgLess)

for m in range(6):
    innerColumn2 = TD[m][2]
    sumCol2 += innerColumn2
sortAsc.append(sumCol2)
for m in range(6):
    innerColumn3 = TD[m][3]
    sumCol3 += innerColumn3
sortAsc.append(sumCol3)
fSumCol = sumCol2 + sumCol3
colAvg = fSumCol / 12
print(f'Average of column 2 & 3: {colAvg}')

for m in TD:
    for i in m:
        sumAll += i
print(sumAll)

for m in range(6):
    innerColumn0 = TD[m][0]
    sumCol0 += innerColumn0
sortAsc.append(sumCol0)
    
for m in range(6):
    innerColumn1 = TD[m][1]
    sumCol1 += innerColumn1
sortAsc.append(sumCol1)

for m in range(6):
    innerColumn4 = TD[m][4]
    sumCol4 += innerColumn4
sortAsc.append(sumCol4)

sortAsc.sort()
print(sortAsc)

with open("Output.txt", "w+") as file:
    file.write(f'Sum of all numbers greater than 20: {sumGreater}\n')
    file.write(f'Average of all numbers less than 10: {avgLess}\n')
    file.write(f'Average of column 2 and 3: {colAvg}\n')
    file.write(f'Sum of all items: {sumAll}\n')
    file.write(f'Sort in ascending order: {sortAsc}\n')
file.close()
