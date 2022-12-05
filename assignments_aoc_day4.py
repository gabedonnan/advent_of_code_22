def main(fname):
    contained = 0
    with open(fname, "r") as f:
        for line in f:
            line_split = line.split(",")
            first = line_split[0].split("-")
            second = line_split[1].split("-")
            if ((int(first[0]) <= int(second[0])) and (int(first[1]) >= int(second[1]))) or ((int(first[0]) >= int(second[0])) and (int(first[1]) <= int(second[1]))):
                contained += 1
    return contained

def main2(fname):
    contained = 0
    with open(fname, "r") as f:
        for line in f:
            line_split = line.split(",")
            first = line_split[0].split("-")
            second = line_split[1].split("-")
            
            if (int(first[0]) in range(int(second[0]),int(second[1])+1)) or (int(first[1]) in range(int(second[0]),int(second[1])+1)) or (int(second[0]) in range(int(first[0]),int(first[1])+1)) or (int(second[1]) in range(int(first[0]),int(first[1])+1)):
                contained += 1
    return contained

if __name__ == "__main__":
    print(main2("assignments.txt"))
