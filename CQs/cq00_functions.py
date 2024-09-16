"""My first Challenge question in COMP110"""

__author__ = "730751163"


def mimic(message: str) -> str:
    """Defining the function mimic as a string type"""
    return message


def main() -> None:
    """Defining the main function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()


def get_tax(price: int, tax_rate: float) -> float:
    return price * tax_rate


def total_cost(cost: int, tax: float) -> float:
    return cost + get_tax(price=cost, tax_rate=tax)


print(total_cost(cost=100, tax=0.07))

print(not not True)