import random 

Easy_turns = 10
Hard_turns = 5


#checks the answer for the right guess
def check_answer(guess, answer,turns):
	if guess > answer:
		print("Too high")
		return turns -1 
	elif guess < answer:
		print("Too low")
		return turns - 1
	else:
		print(f"Your guess was correct ! {answer} was the number")



#checks user selected difficulty  
def dificulty():
	level= input("Select a dificulty level, type easy or hard").lower()
	if level == "easy":
		return Easy_turns
	elif level == "hard":
		return Hard_turns
#main game function 	
def game():
	print("Welcome to the number guessing game")
	print("I am thinking of a number between 1 to 100")
	computer_guess = int(random.uniform(1,100))
	turns = dificulty()
	guess = 0
	while guess != computer_guess:
			
		print(f"You have {turns} attempts remaining to guess the number.")

		#Let the user guess a number.
		guess = int(input("Make a guess: "))

		#Track the number of turns and reduce by 1 if they get it wrong.
		turns = check_answer(guess, computer_guess, turns)
		if turns == 0:
			print("You've run out of guesses, you lose.")
			return
		elif guess != computer_guess:
			print("Guess again.")


game()