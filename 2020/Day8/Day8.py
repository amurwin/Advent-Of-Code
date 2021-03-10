def main():
    f = open("day8input.txt", "r")
    commands = []
    for line in f:
        commands.append((line[:line.find(" ")], line[line.find(" ")+1:-1]))
    
    print(recCase(0, commands, [])[0])

    for x in range(len(commands)):
        temp = commands.copy()
        if temp[x][0] == "nop":
            temp[x] = ("jmp", temp[x][1])
        elif temp[x][0] == "jmp":
            temp[x] = ("nop", temp[x][1])
        retval = recCase(0, temp, [])
        if len(commands) in retval[1]:
            print(retval[0])

def recCase(pos, commands, run=[]):
    acc = 0
    if pos not in run:
        run.append(pos)
        if pos <= len(commands)-1:
            if commands[pos][0] == 'acc':
                if commands[pos][1][0] == "+":
                    acc += int(commands[pos][1][1:])
                else:
                    acc -= int(commands[pos][1][1:])
                acc += recCase(pos+1, commands, run)[0]
            elif commands[pos][0] == 'jmp':
                if commands[pos][1][0] == "+":    
                    acc += recCase(pos + int(commands[pos][1][1:]), commands, run)[0]
                else:   
                    acc += recCase(pos - int(commands[pos][1][1:]), commands, run)[0]  
            elif commands[pos][0] == 'nop':
                acc += recCase(pos+1, commands, run)[0]
    return (acc, run)

main()