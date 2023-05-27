#John Patrick M. Salangsang CS-201
print('John Patrick M. Salangsang CS-201')

with open("Prob2.txt", "r") as file:
    name = file.readline()
    file.readline()
    q1 = file.readline()
    q2 = file.readline()
    q3 = file.readline()
    q4 = file.readline()
    file.readline()
    a1 = file.readline()
    a2 = file.readline()
    file.readline()
    exam = file.readline()
file.close()

qSum = int(q1) + int(q2) + int(q3) + int(q4)
qAvg = qSum / 4
aSum = int(a1) + int(a2)
aAvg = aSum // 2
grade = qAvg + aAvg + int(exam)
fGrade = grade / 3

if fGrade < 75:
    remarks = 'Failed'
else:
    remarks = 'Passed'

with open("Prob2result.txt", "w") as file:
    file.write(f'Name: {name}')
    file.write('Average Quiz: {:.2f}'.format(qAvg))
    file.write(f'\nAverage Assignment: {aAvg}')
    file.write(f'\nExam: {exam}')
    file.write('\nGrade: {:.2f}'.format(fGrade))
    file.write(f'\nRemarks: {remarks}')
file.close()


    

    
    

    
