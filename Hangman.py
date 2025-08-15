#array of possible words and computer randomly picks one word
#show underscores for length of word
#user has input to guess a letter, if letter in word then show updated underscores with letter
#error if user inputs more than one letter
#if user has already used that letter, output message to try again
#if letter not in word, output message like "left arm drawn, n tries remaining"
#if number of tries < available tries, win, if not then death!

#6 lives, could have 'picture' type thing showing the stages
#could have an option where you can guess word before guessing all the letters correctly...?

import random

words = ["random", "list", "of", "words", "for", "python", "to", "pick", "from"]

stages = [
          """
          +======+
          |      |
                 |
                 |
                 |
                 |
                 |
          ========
          """,
          """
          +======+
          |      |
          0      |
                 |
                 |
                 |
                 |
          ========
            """,
            """
          +======+
          |      |
          0      |
          |      |
                 |
                 |
                 |
          ========
            """,
            """
          +======+
          |      |
          0      |
         /|      |
                 |
                 |
                 |
          ========
            """,
            """
          +======+
          |      |
          0      |
         /|\\     |
                 |
                 |
                 |
          ========
            """,
            """
          +======+
          |      |
          0      |
         /|\\     |
         /       |
                 |
                 |
          ========
            """,
             """
          +======+
          |      |
          0      |
         /|\\     |
         / \\     |
                 |
                 |
          ========
            """
            ]
    
def hangman():
    word = random.choice(words)
    underscored_word = "_"*len(word)
    guessed_letters = []
    lives_remaining = 6
    while underscored_word != word: #has the word yet been guessed

        if lives_remaining == 0:
            break

        else:
            guess = input(f"Guess a letter in the word: {underscored_word}")
            if len(guess) > 1:
                if guess != word:
                    lives_remaining -= 1
                    print(f"Sorry, that is not the word! You have {lives_remaining} lives remaining. \n{stages[6-lives_remaining]}")
                else:
                    underscored_word = word
                    break

            elif guess in guessed_letters:
                print(f"You already tried that letter. Here are your guesses so far: {guessed_letters}.")

            else:
                guessed_letters.append(guess)
                if guess in word:
                    underscored_word = list(underscored_word)
                    for i in range(len(word)):
                        if word[i] == guess:
                            underscored_word[i] = guess
                    underscored_word = "".join(underscored_word)
                    print(f"That letter is in the word: {underscored_word}. You have {lives_remaining} lives left. \n{stages[6-lives_remaining]}")
                else:
                    lives_remaining -= 1
                    print(f"That letter is not in the word. You have {lives_remaining} lives left. \n{stages[6-lives_remaining]}")
    
    if underscored_word == word:
        message = (f"You guessed the word, well done! You had {lives_remaining} lives left")
    else:
        message = (f"Sorry, the man has been hanged! The word was {word}!")
    return message




#are there any lives remaining
#does underscored == word?
#is the guess a letter or a word?
#is the letter in the word?


print(hangman())

