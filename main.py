# create a number guesser app by using python
import random

generate_random_value = random.randrange(1,51)
print(generate_random_value)

print("You can only try 5 times : ")
print("Let's Try..........")

n = 5
while (n>=0) :
    user_input = input("Enter a random number between the range of (1 to 50) : ")
    user_input = int(user_input)
    if user_input > generate_random_value :
        print("Correct ans is smaller!")
    elif user_input < generate_random_value :
        print("Correct ans is Greater!")
    elif user_input == generate_random_value :
        print("CONGRATULATION!! You WIN THE GAME")
        break
    n-=1
    if n==0 :
        print("SORRY! YOU LOSE THE GAME!! AND THE CORRECT NUMBER IS ",generate_random_value)
        break



