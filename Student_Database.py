print("Welcome To Student Database:!!")
print("Please Tell the what would You like to do\n")
print("1:: Add Student\n2:: Remove Student\n3:: Edit Marks\n4:: Search for a Student By Name\n5:: Search A Student By Number\n")

oper = int(input("Enter the operation --> "))
database = []
stud_name = []
stud_id = []
stud_class = [] 
stud_addr = [] 


def add_stu():
    student = []
    stu_name = input("\nEnter the name of the student\n-->")
    stu_class = int(input("\nEnter the Class of the student\n-->"))
    stu_id = int(input("\nEnter the student ID no \n-->"))
    stu_addr = input("\nEnter the Address of the Guardians\n-->")
    
    student.append(stu_name)
    student.append(stu_class)
    student.append(stu_id)
    student.append(stu_addr)

    stud_name.append(stu_name)
    stud_id.append(stu_id)
    stud_class.append(stu_class)
    stud_addr.append(stu_addr)
    
    database.append(student)

def search_by_roll():
    search1 = int(input("Enter The Roll no. of the Student::\n-->"))
    if search1 in stud_id:
        stu_roll = stud_id.index(search1)
        print("Result Found for The Student With Roll no. : ", (stud_id.index(search1) + 1))
        print("Student's Name :: ", stud_name[stu_roll])
        print("Student's ID :: ", stud_id[stu_roll])
        print("Student's Class :: ", stud_class[stu_roll])
        print("Student's Address :: ", stud_addr[stu_roll])
    else:
        print('Not Found in the Student Database')

# def edit_marks():



def search_by_name():
    search2 = input("Enter The name of the Student::\n-->")
    if search2 in name_list:
        stu_nam = name_list.index(search2)
        print("Result Found for The Student With Name : ", search2)
        # print("")
    else:
        print('Not Found in the Student Database')

# print(database)
if oper == 1:
    n = int(input("\nHow many students would you like to add?\n-->"))
    for i in range(1, n+1):
        add_stu()

# if oper == 5:
#     n = int(input("\nHow many students would you like to add?\n-->"))
#     for i in range(1, n+1):
#         search_by_name()

# if oper == 4:
#     n = int(input("\nHow many students would you like to add?\n-->"))
#     for i in range(1, n+1):
#         search_by_roll()
