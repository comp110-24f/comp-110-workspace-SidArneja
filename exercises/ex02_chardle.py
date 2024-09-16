"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730751163"


def input_word() -> str:
    """Exit goes before the return statement"""
    word = input("Enter a 5 character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """Exit goes before the return statement"""
    letter = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """Make sure to assign local variables to the functions"""
    count = 0
    print("Searching for " + (letter) + " in " + (word))
    if letter == word[0]:
        print((letter) + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print((letter) + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print((letter) + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print((letter) + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print((letter) + " found at index 4")
        count = count + 1
    """Just if statements, elif would not account for repeating letters in a word"""
    if count > 1:
        print(str(count) + " instances of " + (letter) + " found in " + (word))
    elif count == 1:
        print(str(count) + " instance of " + (letter) + " found in " + (word))


def main() -> None:
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)


main()

if __name__ == "__main__":
    main()
