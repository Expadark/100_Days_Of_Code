import random
from xml.dom.minidom import ProcessingInstruction

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel", 'electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer',
             'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 'submarine', 'chess',
             'resistance', 'matrix', 'function', 'laser', 'mechanism', 'bodyguard', 'titanic', 'global', 'ozone',
             'bridge', 'technology', 'spider', 'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen',
             'language', 'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus', ]

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
lives = 6
if lives <= 0:
    game_over = True
correct_letters = []

guessed = []

while not game_over:
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    guessed += guess

    print("You have already guessed : " + str(guessed))

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if "_" not in display:
        game_over = True
        print("You win.")
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong, you have {lives} more tries")
    if lives <= 0:
        game_over = True
        print(stages[lives])
        print("Game Over")
        print(chosen_word)
input("")