"""Planning a cozy tea party"""

__author__ = "730751163"


def main_planner(guests: int) -> None:
    """This function calls all the other functions and combines them"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    """For this function cost, I have to represent tea count and treat count as the tea_bags and treats functions, where guests is the argument"""


def tea_bags(people: int) -> int:
    """This function makes 2 tea bags per person"""
    return people * 2


def treats(people: int) -> int:
    """This functions makes 1.5 treats per tea bag"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This functions determines the cost of the tea party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
