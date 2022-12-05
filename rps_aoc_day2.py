def compete(p1, p2):
    if p1 == "A":
        if p2 == "X":
            return 4
        elif p2 == "Y": #P2 wins
            return 8
        else:
            return 3
    elif p1 == "B":
        if p2 == "X":
            return 1
        elif p2 == "Y":
            return 5
        else:
            return 9
    else:
        if p2 == "X":
            return 7
        elif p2 == "Y":
            return 2
        else:
            return 6

def compete_new(p1, p2):
    if p1 == "A":
        if p2 == "X":
            return 3
        elif p2 == "Y": #P2 wins
            return 4
        else:
            return 8
    elif p1 == "B":
        if p2 == "X":
            return 1
        elif p2 == "Y": #P2 wins
            return 5
        else:
            return 9
    else:
        if p2 == "X":
            return 2
        elif p2 == "Y": #P2 wins
            return 6
        else:
            return 7

def main(fname):
    score = 0
    with open(fname, "r") as f:
        for line in f:
            score += compete_new(line[0], line[2])
    return score

if __name__ == "__main__":
    print(main("rps.txt"))
