#John Patrick M. Salangsang
#CS - 201
print('John Patrick M. Salangsang CS - 201')
print()

sum = 0
evenItem = 0
sumEven = 0
oddItem = 0
sumOdd = 0
countLess = 0
countGreater = 0
listItem = []

print('Input 10 numbers:')

for i in range(1,11):
    item = int(input(f'Item {i}: '))
    sum += item
    listItem.append(item)
print('Sum:', sum)

for i in listItem:
    if i % 2 == 0:
        evenItem += 1
        sumEven += i
    elif i % 2 == 1:
        oddItem += 1
        sumOdd += i
    else:
        None
print(f'Count of all even numbers: {evenItem}')
print(f'Sum of even numbers: {sumEven}')
print(f'Count of all odd numbers: {oddItem}')
print(f'Sum of odd numbers: {sumOdd}')

for i in listItem:
    if i < 10:
        countLess += 1
    elif i >= 10:
        countGreater += 1
print(f'Count all numbers less than 10: {countLess}')
print(f'Count all numbers greater than or equal to 10: {countGreater}')

listItem.reverse()
print(f'Reverse order of the items: {listItem}')
listItem.sort()
print(f'Ascending order: {listItem}')

countSame = 0
sameElement = 5
for i in listItem:
    if i == sameElement:
        countSame += 1
print(f'What number/s occur more than once? {sameElement} Count: {countSame}')
    
change = int(input('Change all odd values to new value: ' ))
for i in range(0, len(listItem), 1):
    if listItem[i] % 2 == 1:
        listItem[i] = change
print(f'New items in the list: {listItem}')

inputNew = int(input('Input a value to add in all the items greater than 10: '))
for j in range(0, len(listItem), 1):
    if listItem[j] > 10:
        listItem[j] += inputNew
print(f'New items in the list: {listItem}')
