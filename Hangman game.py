import random

# library that we use in order to choose
# on random words from a list of words

print("GUESS THE WORD.")

name = input("What is your name? ")
# Here the user is asked to enter the name first

print(name, "Welcome to this game")
print("Good Luck!")
print("\nYour friend is in serious trouble and he needs you to save him!")

print(" -------- \n" 
       "|       |\n"
       "|       o \n"
       "|      / \ \n"
       "|       | \n" 
       "|      / \ \n")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 12

while turns > 0:

    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)

        else:
            print("_")

            # for every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win, You save your friend.")

        # this print the correct word
        print("The word is: ", word)
        if word == 'rainbow' or 'computer' or 'science' or 'programming' or 'python' or 'mathematics' or 'player' or 'condition' or 'reverse' or 'water' or 'board' or 'geeks':
            print("--------"
                  "|      \n"
                  "|     o\n"
                  "|    / \ \n"
                  "|     | \n"
                  "|    / \ ")

        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character:")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:

        turns -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")

        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose! You didnot have save your friend.
\n"
                  "--------\n"
                  "|       \n"
                  "|       \n"
                  "|    o  \n"
                  "|   / \| \n"
                  "|   /\   \n")


