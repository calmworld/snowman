from random import choice
import string

words_arr = ['psychiatrist', 'blizzard', 'horseradish', 'mischievous', 'gizmo', 'python', 'snazzy', 'lieutenant', 'reverse', 'irregardless', 'jazz', 'awkward', 'pudgy', 'schnapps']

continue_play = True

class Word():
    def __init__(self, chosen_word):
        self.chosen_word = word
    while continue_play==True:
        win = False
        strikes = []
        guesses = []    
        word = list(choice(words_arr))
        display_word = len(word)*['*']  
        print("\nLet's play SNOWMAN! \nCan you guess the word in 8 strikes or less? \n")
        print("Play Word: ", "".join(display_word) + "\n")
        
        while (win == False and len(strikes) < 8):
            letter = input("Guess a letter: ").lower()

            if not letter in string.ascii_lowercase or letter=='':
                continue

            if letter in guesses:
                print("\nYou already guessed that letter, try again \n")
            else: 
                guesses += [letter]
                if letter in word:
                    print("\n>*>*>    Correct!    <*<*<    Keep Going.. \n")
                    for x in range(0, len(word)):
                        if letter == word[x]:
                            display_word[x] = word[x]
                else:
                    strikes += [letter]
                    print("\n>*>*>    That\'s not right!    <*<*<    Keep Guessing..\n")
            print("Play Word Now: ", "".join(display_word))
            print("Guessed Letters: ", guesses)
            print("Remaining Strikes: " + str(8-len(strikes)) + "\n")

            if display_word == word:
                win = True

        if win == True:
            print("\nRemarkable! You Won!")
        else:
            print("\nBetter Luck Next Time!")
        print("The word was '", ''.join(word) , "'")


        while True:
            play_again = input("\nPlay Again? y/n ? ")
            if play_again == 'n' or play_again == 'N':
                print('ta ta!')
                continue_play = False
                break
            elif play_again == 'y' or play_again == 'Y':
                print('OUTSTANDING!')
                break
            else:
                continue