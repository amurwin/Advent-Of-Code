def main():
    f = open("day10input.txt", "r")
    numbers = list(map(int, f.readlines()))
    numbers.append(0)
    numbers.append(max(numbers)+3)
    numbers.sort()
    count = [0,0,0]
    for i in range(0,len(numbers)-1):
        count[(numbers[i+1]-numbers[i]-1)] += 1
    print(count[0]*count[2])

    array = arraySplitter(numbers)   
    total = 1    
    for i in array:
        total *= recCheck(i, i[0])
    print(total)

def arraySplitter(numbers):
    splitArray = []
    for i in range(0,len(numbers)-1):
        if (numbers[i+1]-numbers[i]) == 3:
            splitArray.append(numbers[0:i+1])
            splitArray.extend(arraySplitter(numbers[i+1:]))
            break
    return splitArray

def recCheck(numbers, currentNumber):
    total = 0
    if currentNumber == max(numbers):
        return 1
    for i in range(1,4):
        if currentNumber + i in numbers:
            total += recCheck(numbers, currentNumber+i)
    return total

main()