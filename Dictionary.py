#Salangsang, John Patrick M. CS - 201

f1QuizSum = f1AssignSum = 0
file1 = {}
f1name = input("Enter Name: ")

for x in range(3):
    f1Quiz = int(input("Enter Quiz Score: "))
    f1QuizSum += f1Quiz
f1AvgQuiz = f1QuizSum // 3

for x in range(2):
    f1Assignment = int(input("Enter Assignment Score: "))
    f1AssignSum += f1Assignment
f1AvgAssign = f1AssignSum // 2

f1Exam = int(input("Enter Exam Score: "))

file1 = {"Name":f1name,
         "AvgQuiz":f1AvgQuiz,
         "AvgA":f1AvgAssign,
         "Exam":f1Exam
    }
print(file1)

f2QuizSum = f2AssignSum = 0
file2 = {}
f2name = input("Enter Name: ")

for x in range(3):
    f2Quiz = int(input("Enter Quiz Score: "))
    f2QuizSum += f2Quiz
f2AvgQuiz = f2QuizSum // 3

for x in range(2):
    f2Assignment = int(input("Enter Assignment Score: "))
    f2AssignSum += f2Assignment
f2AvgAssign = f2AssignSum // 2

f2Exam = int(input("Enter Exam Score: "))

file2 = {"Name":f2name,
         "AvgQuiz":f2AvgQuiz,
         "AvgA":f2AvgAssign,
         "Exam":f2Exam
    }
print(file2)

f3QuizSum = f3AssignSum = 0
file3 = {}
f3name = input("Enter Name: ")

for x in range(3):
    f3Quiz = int(input("Enter Quiz Score: "))
    f3QuizSum += f3Quiz
f3AvgQuiz = f3QuizSum // 3

for x in range(2):
    f3Assignment = int(input("Enter Assignment Score: "))
    f3AssignSum += f3Assignment
f3AvgAssign = f3AssignSum // 2

f3Exam = int(input("Enter Exam Score: "))

file3 = {"Name":f3name,
         "AvgQuiz":f3AvgQuiz,
         "AvgA":f3AvgAssign,
         "Exam":f3Exam
    }
print(file3)

record = {"RF1":file1,
          "RF2":file2,
          "RF3":file3
          }
print(record)

with open("record.txt", "w") as file:
    file.write(f"Name  AvgQuiz  AvgA  Exam")
    file.write("\n")
    for x in record:
        file.write(f'{record[x]["Name"]}\t{record[x]["AvgQuiz"]}\t {record[x]["AvgA"]}\t{record[x]["Exam"]}\t')
        file.write("\n")
file.close()

