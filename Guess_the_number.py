# Guess the number game (computer)
import random

a = random.randint(1, 10)
ans = "yes"
count = 5
while ans == "yes" and count > 0:
    input_num = int(input("Enter the number between 1-10 : "))
    if a == input_num:
        print("congratulations you guessed correct number")
    elif a>input_num:
        print("guess higher")
    elif a<input_num:
        print("guess lower")
    else:
        print("Please try again later")
    count -= 1
    ans = input("Want to give another try ? (yes/no)")
else:
    print("Computer won the game.")


    # helo world


    # hiiiiojfjefoo