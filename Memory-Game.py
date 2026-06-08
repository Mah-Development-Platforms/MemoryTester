'''
Author:  Frank Mah
Program Title:  Word Memory Game
Date:  Nov 3, 2023
Description:  A simple word memory game.  Memorize a nonsense word for recall.
'''

# Import neessary library functions.
import random, os, time

# Initialize variables
word = []  # Random letters of the word.
screen = ""  # Stores the arraylist letters in a string for printing horizontally.
playAgain = "y"  # Controls the main program loop.
levelCount = 1  # Difficulty level of the current round.
correct = 0  # Correct answers count.
incorrect = 0  # Incorrect answers count.
timeCount = 0  # Time elapsed in seconds.

# Defined functions.
def randLetter():  # Generate random letters and return each to the function call.
  alpha = chr(random.randrange(65, 91))
  #print (alpha)  # Debugging line.
  return (alpha)

def setWord(counter, countStop):  # Place the letters of the word into the word array.
  while counter < countStop:
    word.append(randLetter())
    counter += 1

  
# ----------- Main Program
os.system('clear')

while playAgain == "y":  # Main game loop.

  counter = 0
  countStop = random.randrange(4, 5+levelCount)  # Set the length of the word.
  
  setWord(counter, countStop)  # Call function to set the random word.

  print("Level", (levelCount),"- Correct: ", correct, "- Incorrect: ", incorrect, "\n-------------------------------------\n") # Banner statement.
  
  for i in word:  # Stores the word array horizontally.
    screen = screen + " " + i
  
  print("Memorize the random letters:\n\n", screen.center(60))  # Prints the word letters to the console screen.
  
  while timeCount < countStop:  # Starts a countdown timer.
    time.sleep(3/levelCount)  # The pause between counting down determined by the difficulty level.
    print(countStop - timeCount)  # Prints the countdown to the screen. 
    timeCount += 1  # Counter increment.

  timeCount = 0  # Reset the counter for the next round.
  os.system('clear')  # Erases the word from the screen.
  
  answerGuess = input("Retype the random letters in order: ").upper()  # Prints the question and its position (one more than the random number because lists start the position count at 0.)
  
  if answerGuess == screen.replace(" ",""):  # Compares the user's guess to the correct letter.
    print("Correct!")  # Prints if the user guessed correctly.
    correct += 1   # Increments the score.
    if correct % 3 == 0:
      levelCount += 1  # Increments the difficulty level.
  else:
    print("\nIncorrect!")  # Prints if the user guessed incorrectly.
    print("\nThe correct answer was", screen)  # Prints the correct answer.
    incorrect += 1

  # Clear the word from the array and the screen string for printing.
  word.clear()
  screen = ""

  #  Reset the game and clear the screen.
  print("\nYour score is ", correct, " out of ", (correct + incorrect), ".")  # Prints the score.
  playAgain = input("\nPlay again? (y/n): ")  #Player input to continue.
  if levelCount >= 10:  # Hold levelCount at 11 to prevent random letter choice errors.
    levelCount = 10
  os.system('clear')

print("Thanks for playing!")  # End message.

