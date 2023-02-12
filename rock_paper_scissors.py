import random

def play():
    user = input("What's your choice ? 'r' for rock , 's' for scissors , 'p' for paper \n")
    computer = random.choice(['r','s','p'])


    if user==computer:
        return "This is a Tie"
    if is_win(user,computer):
        return "You've won the game."
    return "You Lost"

# s>p , p>r , r>s

def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True


print(play())