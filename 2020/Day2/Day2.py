def main():
    valid1 = 0
    valid2 = 0
    f = open("day2input.txt", "r")
    for line in f:
        var = line[line.index(' ')+1]
        count = line[line.index(':')+2:].count(line[line.index(' ')+1])
        low = int(line[:line.index('-')])
        high = int(line[line.index('-')+1:line.index('-')+3])
        if count >= low and count <= high:
            valid1 += 1
        nString = line[line.index(':')+2:]
        print(nString)

        if ((nString[low-1] == var) or (nString[high-1] == var)) and (nString[low-1] != nString[high-1]):
            valid2 += 1
    print(valid1)
    print(valid2)
    f.close()


main()