"""Creating a number guessing game"""

__author__ = "730751163"


def guess_a_number() -> None:
    secret: int = 7
    number = int(input("Guess a number: "))
    if number == secret:
        print("Your guess was " + str(number))
        print("You got it!")
    elif number > secret:
        print("Your guess was " + str(number))
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        print("Your guess was " + str(number))
        print("Your guess was too low! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
