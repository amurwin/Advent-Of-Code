def main():
    f = open("day9input.txt", "r")
    invalidnumber = 0
    numbers = list(map(int, f.readlines()))
    for i in range(25,len(numbers)):
        isValid = False
        start = max(0,i-25)
        for j in numbers[start:i]:
            for k in numbers[start:i]:
                if j != k and j + k == numbers[i]:
                    isValid = True
        if isValid == False:
            print(numbers[i])
            invalidnumber = numbers[i]
            break
        else:
            isValid = False


    for i in range(0, len(numbers[0:numbers.index(invalidnumber)])):
        iter = i
        sumTot = 0
        valArray = []
        while sumTot < invalidnumber:
            valArray.append(numbers[iter])
            sumTot += numbers[iter]
            iter += 1
            if sumTot == invalidnumber:
                print(min(valArray)+max(valArray))
                break           
main()