

def magic_number():
    number_to_guess = 6
    user_number = int(input("Guess a number between 1 and 10: "))
    if user_number == number_to_guess:
        print("You Win!")
    else:
        print("You lose: Try Again")
        magic_number()


magic_number()
