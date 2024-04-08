def applicationStart(studentList):
    TEXT_TEMPLATE = "1. Add student\n2. Delete student by ID\n3. Get all students\n4. Get student by ID\nChoose an option: "
    print(TEXT_TEMPLATE)
    userOption = input()
    if userOption == "1":
        print(addStudent(studentList))
    elif userOption == "2":
        print(deleteStudentById(studentList))
    elif userOption == "3":
        print(getAllStudents(studentList))
    elif userOption == "4":
        print(getStudentById(studentList))
    else:
        print("Unsupported Option \n")
    applicationStart(studentList)


def addStudent(studentList):
    print("Enter student's name:")
    name = input()
    print("Enter student's surname:")
    surname = input()
    studentIndex = createUniqId(studentList)
    studentList.append({'index': studentIndex, 'name': name, 'surname': surname})
    return "Student added successfully."


def deleteStudentById(studentList):
    print("Enter student's ID to delete:")
    studentId = input()
    for student in studentList:
        if student['index'] == studentId:
            studentList.remove(student)
            return "Student deleted successfully."
    return "Student not found."


def getAllStudents(studentList):
    return studentList


def getStudentById(studentList):
    print("Enter student's ID:")
    studentId = int(input())
    for student in studentList:
        if student['index'] == studentId:
            return student
    return "Student not found."


def createUniqId(studentList):
    if studentList:
        return len(studentList) + 1
    else:
        return 1


allStudentList = []
applicationStart(allStudentList)
