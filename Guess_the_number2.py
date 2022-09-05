# Guess the number game (computer)


a = int(input("Enter the number to be guessed : "))
ans = "yes"
count = 5
while ans == "yes" and count > 0:
    input_num = int(input("Enter the number guessed by the participant : "))
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