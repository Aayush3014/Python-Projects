import random as r
word_list = ["mango", "banana", "apple", "kiwi"]
word_selected = r.choice(word_list)
word_length = len(word_selected)
chances = word_length + 2
print(word_selected)
ans = 'y'
while ans == 'y':
    guess_alphabet = input("Enter the alphabet you want to guess : ")

    if guess_alphabet in word_selected:
        chances -= 1
        print(f"Congratulations You have guessed one correct word {chances} Left.")
        
        for i in word_selected:
            if i == guess_alphabet:
                print(guess_alphabet,"is placed at index",i.index())
            else:
                pass
        
    else:
        chances -= 1
        print(f"You have {chances} more chances Left.")
    ans = input("Do you want to continue guessing the words? : (y/n)")
# print(word_length)
