secretNumber = input("Please pick a number between 0 and 100: ")
while int(secretNumber) >= 100:
    secretNumber = input("I'm sorry your number was too large, please pick a number between 0 and 100: ")
while int(secretNumber) < 0:
  secretNumber = input("I'm sorry, negative numbers are not accepted. Please pick a number between 0 and 100: ")
  
High = 100
Low = 0
guess = 50
while int(secretNumber) != int(guess):
    print('Is your secret number {}?'.format(guess))
    userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if userInput == 'h':
        High = guess
        guess -= (High - Low)//2
    elif userInput == 'l':
        Low = guess
        guess += (High - Low)//2
    else:
        userInput == 'c'
        break

guess = secretNumber
print("Game over. Your secret number was: {}".format(secretNumber))