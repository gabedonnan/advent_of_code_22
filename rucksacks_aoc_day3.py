import string

def getPrio(s):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    if s in lower:
        return lower.find(s) + 1
    else:
        return upper.find(s) + 27

def main(fname):
    total = 0
    equal = ""
    with open(fname, "r") as f:
        for line in f:
            temp = line.strip()
            first = temp[:int((len(temp)/2))]
            second = temp[int((len(temp)/2)):]
            for item in first:
                if item in second:
                    equal = item
                    break
            total += getPrio(equal)
    return total

def main2(fname):
    total = 0
    temp = ["", "", ""]
    badge = ""
    counter = 0
    with open(fname, "r") as f:
        for line in f:
            temp[counter] = line.strip()
            if counter == 2:
                for item in temp[0]:
                    if (item in temp[1]) and (item in temp[2]):
                        badge = item
                total += getPrio(badge)
                counter = 0
            else:
                counter += 1   
    return total
            

if __name__ == "__main__":
    print(main2("rucksacks.txt"))
