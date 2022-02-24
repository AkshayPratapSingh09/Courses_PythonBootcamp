print("Welcome to my Quiz!!!")

playing = input("Do you really want to play??  ((Yes) to play / (No) for Not )\n-->")

if playing.lower() != "yes":
    print("You successfully exited the game!!")
    quit()

print("The game starts!! ::)")
score = 0
print("\n")
answer = input("What does CPU stands for?\n-->")
if answer.lower() =="central processing unit":
    score += 1
    print("Correct!")
else:
    print("Wrong answer!!\nThe right answer was Central Processing Unit.")

print("\n")
answer = input("What does GPU stands for?\n-->")
if answer.lower() =="graphics processing unit":
    score += 1
    print("Correct!")
else:
    print("Wrong answer!!\nThe right answer was Graphics Processing Unit.")

print("\n")
answer = input("What does CU stands for?\n-->")
if answer.lower() =="central unit":
    score += 1
    print("Correct!")
else:
    print("Wrong answer!!\nThe right answer was Central Unit.")

print("You got " + str(score) + " Questions Correct!!")