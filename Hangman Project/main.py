import random # random inputs
import webbrowser # for github webbrowser open

def menu():
        print("Welcome To Hangman!")
        print("Made by Cayden Hutcheson")
        print("\n")
        print("[1] Play Hangman")
        print("[2] About")
        print("[3] Exit the program")
menu()
option = int(input("Enter your option: "))
while option != 0:
    if option == 1:
        #open the file
        wordList = open("wordList.txt", "rt")

        #Step 3: Make lists and lives variable
        hangman = []
        lives = 7
        guessed = False
        guessed_letters = []
        guessed_words = []

        #Step 4: append the words to the list
        for words in wordList:
            word = words.rstrip()
            hangman.append(word.upper())
        wordList.close()

        #Step 5: randomly select a word from the list
        randNum = random.randint(0, len(hangman))
        word = hangman[randNum]
        word_completion = "_ " * len(word)
        
        print("\n")
        print("Welcome To Hangman!")
        print("\n")
        print("Size: ", len(word))
        print("\n")
        print(word_completion)
        print("\n")

#Step 7: While Loop
        while not guessed and lives > 0:
                guess = input("Please guess a letter or word: ").upper()
                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letters:
                        print("You already guessed the letter", guess)
                    elif guess not in word:
                        print(guess, "is not in the word.")
                        lives -= 1
                        print("You have:", (lives), "Lives")
                        guessed_letters.append(guess)
                    else:
                        print("Good job,", guess, "is in the word!")
                        guessed_letters.append(guess)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        if "_" not in word_completion:
                            guessed = True
                elif len(guess) == len(word) and guess.isalpha():
                    if guess in guessed_words:
                        print("You already guessed the word", guess)
                    elif guess != word:
                        print(guess, "is not the word.")
                        lives -= 1
                        guessed_words.append(guess)
                    else:
                        guessed = True
                        word_completion = word
                else:
                    print("Invalid Guess")
                print(word_completion)
                print("\n")
        if guessed:
                print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of lives. The word was " + word + ". Maybe next time!")
            break
    elif option == 2:
        webbrowser.open("https://github.com/ExzellTv/Comp-Sci-1-Project-s")
        break
    elif option == 3:
        print("Quitting... the program")
        break
