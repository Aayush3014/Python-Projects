import random as r
def hangman():
    words_list = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot',
             'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']
    
    select_word = r.choice(words_list)
    chances = 10
    guessmade = ''  # user will guess thiss word
    # print(select_word)


hangman()