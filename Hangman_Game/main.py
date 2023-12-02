import random
import hangman_words
import hangman_art

# hangman game

word_list = ["ardvark", "baboon", "camel"]

chosenWord = random.choice(hangman_words.word_list)

hiddenWord = ''
for i in range(len(chosenWord)):
    hiddenWord += "_"

isDone = False
health = 6

print(hangman_art.logo)

while not isDone:
    guessedLetter = input("Type a letter: ").lower()

    if guessedLetter not in chosenWord:
        health -= 1
    print(hangman_art.stages[health])
    for i in range(len(chosenWord)):
        if chosenWord[i] == guessedLetter:
            hiddenWord = hiddenWord[:i] + chosenWord[i] + hiddenWord[i + 1:]

    if health == 0 and hiddenWord != chosenWord:
        isDone = True
        print('you lost')
        break
    elif health >= 0 and hiddenWord == chosenWord:
        print("you won")
        break


    print(hiddenWord)
