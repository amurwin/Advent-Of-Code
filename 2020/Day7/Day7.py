def main():
    f = open("day7harry.txt", "r")
    key = ["shiny gold"]
    key2 = "shiny gold"
    colorDict = []
    for line in f:
        outer = line[0:line.find("bags")-1]
        inner = []
        innerbreak = line[line.find("contain")+8:]
        processed = innerbreak.split(", ")
        for x in processed:
            if x.find("bags") != -1:
                xString = x[x.find(" ")+1:x.find("bags")-1]
            else:
                xString = x[x.find(" ")+1:x.find("bag")-1]
            number = x[:x.find(" ")]
            inner.append((xString, number))
        for x in inner:
            colorDict.append((x[0], x[1], outer))
        outer = ""
        inner = []
    print(len(recursiveCheckPart1(key, colorDict))-1)
    print(recursiveValue(key2, colorDict)-1)

def recursiveCheckPart1(key, colorDict):
    returnArray = key.copy()
    for pair in colorDict:
        for val in key:
            if pair[0] == val and pair[2] not in returnArray:
                returnArray.append(pair[2])
    if len(returnArray) != len(key):
        returnArray = recursiveCheckPart1(returnArray, colorDict)
    return returnArray

def recursiveValue(key, colorDict, numOfCurrent=1):
    returnValue = 0
    for pair in colorDict:
        if pair[2] == key:
            if pair[1] == "no":
                returnValue += 0
            else:
                returnValue += recursiveValue(pair[0], colorDict, int(pair[1])*int(numOfCurrent))
    return returnValue + numOfCurrent

main()