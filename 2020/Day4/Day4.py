from Passport import *

def main():
    f = open("day4input.txt")
    byr = ''
    iyr = ''
    eyr = ''
    hgt = ''
    hcl = ''
    ecl = ''
    pid = ''
    cid = ''
    valid = 0
    currentString = ""
    passports = []
    for line in f:
        currentString += line
        if line == "\n":
            currentString = currentString.split('\n')
            currentString = " ".join(currentString)
            #print(currentString)

            try:
                byr = currentString[currentString.index('byr')+4:currentString.index(' ',currentString.index('byr')+4)]
            except:
                byr = ''

            try:
                iyr = currentString[currentString.index('iyr')+4:currentString.index(' ',currentString.index('iyr')+4)]
            except:
                iyr = ''

            try:
                eyr = currentString[currentString.index('eyr')+4:currentString.index(' ',currentString.index('eyr')+4)]
            except:
                eyr = ''

            try:
                hgt = currentString[currentString.index('hgt')+4:currentString.index(' ',currentString.index('hgt')+4)]
            except:
                hgt = ''

            try:
                hcl = currentString[currentString.index('hcl')+4:currentString.index(' ',currentString.index('hcl')+4)]
            except:
                hcl = ''

            try:
                ecl = currentString[currentString.index('ecl')+4:currentString.index(' ',currentString.index('ecl')+4)]
            except:
                ecl = ''

            try:
                pid = currentString[currentString.index('pid')+4:currentString.index(' ',currentString.index('pid')+4)]
            except:
                pid = ''

            try:
                cid = currentString[currentString.index('cid')+4:currentString.index(' ',currentString.index('cid')+4)]
            except:
                cid = ''


            passports.append(Passport(byr, iyr, eyr, hgt, hcl, ecl, pid, cid))
            currentString = ""
            print("-------------------")
    for x in passports:
        #if x.getIsValid() == True:
          #  print("T")
        #else:
           # print("F")
        if x.getIsValid() == True:
            valid += 1
main() 

