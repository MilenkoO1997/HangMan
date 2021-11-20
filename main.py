
import hangman_art
import hangman_words
import random
import os
def clear(): return os.system('cls')


clear()

glisa = hangman_art.stages
glisa.reverse()
while True:
    word_list = hangman_words.word_list

    chosen_word = random.choice(word_list).lower()
    blank = len(chosen_word) * "_"
    blank = list(blank)
    print(hangman_art.logo)
    print()
    print(blank)
    GOver = 0
    tried = []

    while GOver < 6:
        print(glisa[GOver])
        guess = input("Guess the letter:  ").lower()
        clear()
        print(hangman_art.logo)
        print()
        if len(guess) != 1:
            print("Type one letter please!")
        else:
            if guess not in tried:
                tried.append(guess)
                if guess in chosen_word:

                    print("\nThere is '" + guess + "' in the word!\n")

                    for i in range(len(chosen_word)):
                        if chosen_word[i] == guess:
                            blank[i] = guess
                    print(blank)
                    print()
                    if not "_" in blank:
                        print("***YOU WIN!***\n\n\n")
                        break
                else:
                    print("No '" + guess + "'!")
                    print(blank)

                    GOver += 1

                    if GOver == 6:
                        print(glisa[GOver])
                        print("***YOU LOSE!***\n")
                        print("The word was '" + chosen_word + "'!\n\n")
                        break
            else:
                print("\nYou already tried letter '" + guess + "'!\n")

    input("Again? (Press Enter)")
    clear()
