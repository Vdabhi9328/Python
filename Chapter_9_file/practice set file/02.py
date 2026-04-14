import random

def game():
    print("You are Playing game...")
    score = random.randint(1,62)

    # fatch the hiscore
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your Score: {score}")
    if(score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()