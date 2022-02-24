
#Will open file
# myfile = open('Test.txt')
# print(myfile.read())

#Way of opening file
# contents = myfile.read()
# print(contents)


# myfile = open('G:\\Bac\\Documents\\About_College_Question.txt')
# print(myfile.read())

# with open("Test.txt",mode = 'r') as newfile:
#     content1 = newfile.read()
#     print(content1)

with open("Test.txt",mode = 'a') as newfile1:
    # content1 = newfile.write()
    newfile1.write('This is the fourth line')
with open("Test.txt",mode = 'r') as newfile1:
    print(newfile1.read())