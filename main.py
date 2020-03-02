#@title Default title text
#This is a game.

print ("This is a game you will surely enjoy, whether girl or boy, pure intellect is what you must deploy. \nIf you answer each question correctly and fast, you will find that level by level you'll pass. \nBeware that as you get farther and farther, the questions will get harder and harder. \nShould you get them all right, you might crack a grin, but if you don't then up with your chin, at least you learned something, now let's begin... \n")

# Ask the user a series of questions to which the answer is A, B, C, or D.

# Print the first question, and ask the user for their answer

print ("What house is Hermione Granger sorted into?")

print ("A. Ravenclaw \nB. Slytherin \nC. Gryffindor \nD. Hufflepuff\n")

# Create a function that calls for UserAnswer when a question is asked
answer = input ("What is the answer?")

# Determine if the user inputs the correct answer
if (answer == "c") or (answer == "C"):
  print ("Correct.\n")
else:
  print ("The correct answer was C. Gryffindor\n")
  
# Ask the second question and call for UserAnswer to ask for an input
print ("For this question you must anwser three parts. \n")
question = ("What is the spell that Ron just can't say correctly? \nA. Stupify \nB. Wingardium Leviosa \nC. Accio \nD. Alohomora \n")
print (question)

answerCount = 0

answer2 = input ("What is the answer?")

# Determine if the user's answer is correct, and check if all three answers are correct
 
while (answer2 != "b") and (answer2 != "B"):
  answerCount += 1
  print ("Try again.")
  print (question)
  answer2 = input ("What is the answer?")

if (answer2 == "b") or (answer2 == "B"):
  answerCount += 1
  print ("Indeed, you may move on to part two.\n")
  question2 = ("In what class does he learn it?\nA. Charms \nB. Transfiguration \nC. Defense Against the Dark Arts \nD. Potions\n")
  print (question2)
  answer3 = input ("What is the answer?")

while (answer3 != "a") and (answer3 != "A"):
  answerCount += 1
  print ("Keep your wits about you and try once more.")
  print (question2)
  answer3 = input ("What is the answer?")

if (answer3 == "a") or (answer3 == "A"):
  answerCount += 1
  print ("Very good, you may move on to part three.\n")
  question3 = ("Who teaches Ron the spell?\nA. Severus Snape \nB. Minerva McGonagall \nC. Fillius Flitwick \nD. Sybill Trelawney\n")
  print (question3)
  answer4 = input ("What is the answer?")

while (answer4 != "c") and (answer4 != "C"):
  answerCount += 1
  print ("You have been granted another attempt.")
  print (question3)
  answer4 = input ("What is the answer?")

if (answer4 == "c") or (answer4 == "C"):
  answerCount += 1
  print ("Magnificent work!")
  
if ((answer4 == "c") or (answer4 == "C")) and ((answer2 == "b") or (answer2 == "B")) and ((answer3 == "a") or (answer3 == "A")):
  print ("Congratulations, you got all three! It only took you",(answerCount), "tries.")

print ("In this next question there are two in one.")

# Create a function that tells the user what their guess was
def UserAnswer(fullName):
  print ("\nYou guessed that their full name is %s"%(fullName))

# Create a variable for the first name guess
nameGuess = input("What is Ron's full name?")

# Call for the function
UserAnswer(nameGuess)

# Determine if the user's guess is correct
if (nameGuess == "Ronald Weasley"):
  print ("\nThat is his name, now try something that requires skill")
else:
  print ("\nThat is incorrect, you should watch the movies")

# Ask the user the second question
nameGuess2 = input("\nWhat is the full name of the Defense against the dark arts teacher in The Chamber of Secrets?")

UserAnswer(nameGuess2)

if (nameGuess2 == "Gilderoy Lockhart"):
  print ("Well done, I was beginning to think you didn't know your facts")
else:
  print ("His full name is Gilderoy Lockhart; Maybe you aren't so skilled after all")

# Ask the user the third question
nameGuess3 = input("\nWhat is the Headmaster of Hogwarts' FULL name?")

UserAnswer(nameGuess3)

if (nameGuess3 == "Albus Percival Wulfric Brian Dumbledore"):
  print ("Uncanny; I see you are a true fan, maybe too true")
else:
  print ("His full name is Albus Percival Wulfric Brian Dumbledore; if you missed it I don't blame you.")

# Ask a question about point values
print ("How many points were awarded in the sorcerer's stone at the end of term ceremony\n")

# Define the user's guess variables
guess1 = int(input("To Hermione?"))
guess2 = int(input("To Harry?"))
guess3 = int(input("To Ron?"))
guess4 = int(input("To Neville?"))

# Create an if statement that determines if the guessed point values are correct
if (guess1 == 50) and (guess2 == 60) and (guess3 == 50) and (guess4 == 10):
  print ("Congratulations, you guessed the correct total!")
else:
  print ("That is incorrect, I was beginning to think you were a mastermind")


