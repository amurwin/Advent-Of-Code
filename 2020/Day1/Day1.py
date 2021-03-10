def main():
    array = []
    f = open("day1input.txt", "r")
    for line in f:
        array.append(line)
    for x in array:
        for y in array:
            for z in array:
                if ((int(x) + int(y) + int(z)) == 2020):
                    print(int(x)*int(y)*int(z))
                

main()