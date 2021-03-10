def main():
    f = open("day5input.txt", 'r')
    array = [*range(0,1024)]
    largest = 0
    smallest = 1000
    for line in f:
        rowValue = 64
        rowCounter = 0
        for x in range(0,8):
            if line[x] == 'B':
                rowCounter += rowValue
                rowValue /= 2
            else:
                rowValue /= 2
        
        colValue = 4
        colCounter = 0
        for x in range(0,3):
            if line[x + 7] == 'R':
                colCounter += colValue
                colValue /= 2
            else:
                colValue /= 2

        seatId = rowCounter*8+colCounter
        if largest < seatId:
                largest = seatId
        if smallest > seatId:
                smallest = seatId
        array.remove(seatId)
    for x in range(0,int(smallest)):
        array.remove(x)
    for x in range(int(largest)+1,1024):
        array.remove(x)
    print(array[0])
main()