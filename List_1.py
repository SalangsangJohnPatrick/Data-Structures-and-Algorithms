#John Patrick M. Salangsang
#Keeno C. Cruz
#CS - 201
print("John Patrick M. Salangsang\tCS - 201\nKeeno C. Cruz\n")

exampleList = []
print('Generate 15 numbers 10 - 30:')
for i in range(0, 15):
    inputNum = int(input())
    print()
    if inputNum < 10 or inputNum > 30:
        print("Please only enter a number ranges from 10 - 30. Try again.")
        break
    exampleList.append(inputNum)

print('Values:')
for i in exampleList:
    print(i, end=' ')

with open('exampleList.txt', 'w+') as file:
    countNum = 0
    
    file.write('Display the numbers less than 20:\n')
    for i in exampleList:
        if i < 20:
            file.write(f'{str(i)} ')
            countNum += 1
    file.write(f'\nCount the numbers greater than 20:\n')
    file.write(f'{str(countNum)} ')
            
    file.write('\nCombine the first and last four numbers:\n')
    copyList1 = exampleList[:4].copy()
    copyList2 = exampleList[11:].copy()
    copyList1.extend(copyList2)
    for i in copyList1:
        file.write(f'{str(i)} ')

    file.write(f'\nSort the numbers:\n')
    copyList1.sort()
    for i in copyList1:
        file.write(f'{str(i)} ')
file.close()
    
        
    
