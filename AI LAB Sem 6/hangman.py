#hangman
import random

def hangman(word):
  maxAttempts = 5
  attempts = 0
  guessWord = "_" * len(word)
  while attempts < maxAttempts:
    print(guessWord)
    guess = input("\nEnter guess: ")
    if len(guess) != 1 and not guess.isalpha():
      print("\nInvalid")
    else:
      if guess in word:
        print("Correct")
        for i in range(len(word)):
          if word[i] == guess:
            guessWord = guessWord[:i] + guess + guessWord[i+1:]
            if guessWord == word:
              break
      else:
        print("Wrong")
        attempts += 1
  if "_" not in guessWord:
    print("Won")
  else:
    print(word)
words = ["yay", "boo"]
word = random.choice(words)
hangman(word)