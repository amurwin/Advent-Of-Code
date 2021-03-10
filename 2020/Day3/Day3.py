def main():
    print(treeEncounters(1)*treeEncounters(3)*treeEncounters(5)*treeEncounters(7)*weirdAssTrees())
    
    print(treeEncounters(1))
    print(treeEncounters(3))
    print(treeEncounters(5))
    print(treeEncounters(7))
    print(weirdAssTrees())


def treeEncounters(n):
    f = open("day3input.txt", "r")
    trees = 0
    i = 0
    lineLenght = 0
    for line in f:
        lineLenght = 31
        if (i >= lineLenght):
            i = i - lineLenght
        if (line[i] == "#"):
            trees += 1
        i = i + n
    f.close()
    return trees


def weirdAssTrees():
    f = open("day3input.txt", "r")
    trees = 0
    i = 0
    j = 0
    lineLenght = 0
    for line in f:
        lineLenght = 31
        if (i >= lineLenght):
            i = i - lineLenght

        if j % 2 == 0:
            if (line[i] == '#'):
                trees += 1
            i += 1
        j += 1
    f.close()
    return trees

main()