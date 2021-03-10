def main():
    f = open("day6input.txt", "r")
    counter = 0
    currentString = ''
    personCounter = 0
    for line in f:
        personCounter += 1
        currentString += line
        if line == "\n":
            personCounter -= 1
            for x in range(97,123):
                #if chr(x) in currentString:
                if currentString.count(chr(x)) == personCounter:
                    counter += 1
            personCounter = 0
            currentString = ''
    print(counter)

main()