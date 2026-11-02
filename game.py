import random
from collections import Counter
from wordList import words

# ==================================
# GAME SETTINGS
# ==================================

gameName = 'Word Raiders'
chosenWord = random.choice(words).lower()
maxTurns = 5
maxLength = 5

# ==================================
# VALIDATE PLAYER INPUT
# ==================================

def validInput():
    while True:
        guessedWord = input('What is your guess?\n').lower().strip()
        print('--------------------------------------')
        # Quietly ignore an accidental blank Enter
        if not guessedWord:
            continue

        if not guessedWord.isalpha():
            print('Error: Input must contain only letters (no numbers, spaces, or symbols).')
            continue

        if len(guessedWord) != maxLength:
            print(f'Error: Input must be {maxLength} characters long.')
            continue

        return guessedWord

# ==================================
# CHECK PLAYER'S GUESS
# ==================================

def incorrectLettersPresent(guessedWord):
    remainingLetters = Counter(chosenWord)
    feedback = [None] * len(guessedWord)


    correctLetters = []
    misplacedLetters = []
    incorrectLetters = []

    # First: identify letters in the correct position
    for position, char in enumerate(guessedWord):
        if char == chosenWord[position]:
            feedback[position] = char
            remainingLetters[char] -= 1
            correctLetters.append(char)

    # Second: identify misplaced and incorrect letters
    for position, char in enumerate(guessedWord):
        if feedback[position] is None:
            if remainingLetters[char] > 0:
                feedback[position] = '?'
                remainingLetters[char] -= 1
                misplacedLetters.append(char)
            else:
                feedback[position] = '_'
                incorrectLetters.append(char)

    # Display results
    print('Your guess: ', *guessedWord)
    print('Feedback:   ', *feedback)

    if correctLetters:
        print('Letters that are correct:', *correctLetters)
    if misplacedLetters:
        print('The following letters are correct, but in the wrong place:', *misplacedLetters)
    if incorrectLetters:
        print('Letters that are incorrect:', *incorrectLetters)

# ==================================
# MAIN GAME
# ==================================

def main():
    turnsMade = 0
    guessedWordList = []
    guessedWord = ''

    # Welcome message
    print(f'\nWelcome to {gameName}!')
    print(f'Each word presented in this puzzle contains {maxLength} letters.')
    print(f'\033[1mYou have {maxTurns} turns to guess the word!\033[1m')

    # Uncomment this line for testing
    print('The word is:', chosenWord)

    # Game loop
    while turnsMade < maxTurns:
        print('======================================')
        print(f'Turn {turnsMade + 1} of {maxTurns}')
        print('======================================')
        guessedWord = validInput()
        guessedWordList.append(guessedWord)

        # Check whether the player guessed correctly
        if guessedWord == chosenWord:
            turnsUsed = turnsMade + 1
            print(f'\033[1m\nCONGRATULATIONS! The word is {chosenWord}!\033[0m')
            print(f'You guessed it in {turnsUsed} turn{"s" if turnsUsed != 1 else ""}!')
            break

        # Check letters and display feedback
        incorrectLettersPresent(guessedWord)

        # Increase turn counter
        turnsMade += 1
        print(f'\nYou have {maxTurns - turnsMade} guesses remaining.')
        
        # Display previous guesses
        print('\n\033[3mYour previous guesses:\033[0m')
        for guess in guessedWordList:
            print(f'\033[3m{guess}\033[0m')

    # Game over
    if guessedWord != chosenWord:
        print('\nGame over!')
        print(f'The correct word was {chosenWord}.')

    # Final guess history
    print('\nYour guesses were:')
    for guess in guessedWordList:
        print(guess)

# ==================================
# START GAME
# ==================================

if __name__ == '__main__':
    main()