import random

print("hello world! are you older than the computer let's see!")

age = int(input("what is your age:"))

computerRandomAge = random.randint(0,200)


if computerRandomAge > age:
    print(f"Sorry the computer age is {computerRandomAge} and you age is {age} therefore the computer is older than you 🥲")
elif computerRandomAge < age:
    print(f"your age is {age} and the computer's age is {computerRandomAge} therefore you are older than the computer 😁")    



