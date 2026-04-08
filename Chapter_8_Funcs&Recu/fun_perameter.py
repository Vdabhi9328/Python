# without argument simple function
def goodDay():
    print("Good Day")

goodDay()

# with argument
def goodDay(name):
    print(f"Good Day, {name}")

goodDay("Vimal")


# with deafult argument
def goodDay(name, ending="Thanks You"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Vimal", "Thanks")
goodDay("Rohan")