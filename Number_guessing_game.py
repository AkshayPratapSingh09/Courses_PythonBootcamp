import random

r = random.randrange(1, 11)
ipt = int(input("Enter your Guess for numbers b/w 1-10:\n-->"))

if ipt==r:
    print(f"Congrats!!  You guessed {r} Correctly!!")
else:
    print(f"Oops!! you got it wrong!!! The number was {r}")

