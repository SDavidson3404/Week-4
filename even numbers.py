guessLeft = 3
secretPass = 123456

while guessLeft > 0:
    passGuess = int(input("Please enter a guess: "))
    if passGuess != secretPass:
        print("Wrong, try again")
    else
        print("Congrats! You got it!")
        break
while guessLeft == 0
    print("locked out.")