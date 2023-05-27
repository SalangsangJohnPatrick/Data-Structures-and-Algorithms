#John Patrick M. Salangsang
#CS - 201
print('John Patrick M. Salangsang CS - 201')
print()

#Assign the following values(items) 2,5,8,1,4,7,3,6,9,1 to myListA variable.
myListA = [2,5,8,1,4,7,3,6,9,1]
print('All items in myListA:', myListA)
print()

#Input the following items 7,8,9,4,5,6,1,2,3,2 to myListB variable. (use looping statement)
myListB = []
answer = 'Y'
while answer.upper() == 'Y':
    items = int(input('Input an item to myListB: '))
    myListB.append(items)
    answer = input('Do you want to add another item? (y = yes, anything else = no) ')
print('All items in myListB:', myListB)
print()

#Copy the first five items of myListA and the last five items of myListB to myListC variable. (use looping statement)
myListC = []
for i in myListA[:5]:
    myListC.append(i)
for j in myListB[5:]:
    myListC.append(j)
print('Copy of the first five items of myListA and the last five items of myListB to myListC:', myListC)
print()

#Arrange in ascending order the items of myListC.
myListC.sort()
print('Ascending order of myListC:', myListC)
print()

#Copy all the odd numbers of myListA to myListD. ( use looping and decision statement)
myListD = []
for i in myListA:
    if i % 2 == 1:
        myListD.append(i)
print('Copy of all the odd numbers from myListA to myListD:', myListD)
print()

#Copy all the even numbers of myListB to myListE. ( use looping and decision statement)
myListE = []
for i in myListB:
    if i % 2 == 0:
        myListE.append(i)
print('Copy all the even numbers of myListB to myListE:', myListE)
print()

#Add the following items 1,2,3,4,5 to myListD.
extendListD = [1,2,3,4,5]
myListD.extend(extendListD)
print('Extended list of myListD:', myListD)
print()

#Add the following items 6,7,8,9,10 to myListE.
extendListE = [6,7,8,9,10]
myListE.extend(extendListE)
print('Extended list of myListE:', myListE)
print()
