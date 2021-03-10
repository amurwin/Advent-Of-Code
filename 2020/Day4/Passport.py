import re

class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

        self.isValid = False
        
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            #print(byr)
            if len(byr) == 4 and re.match(r"19[2-9][0-9]|200[0-2]", byr):
                #print(iyr)
                if len(iyr) == 4 and re.match(r"201[0-9]|2020", iyr):
                    #print(eyr)
                    if len(eyr) == 4 and re.match(r"202[0-9]|2030", eyr):
                        #print(hcl)
                        if re.match(r"\#[a-f0-9]{6}", hcl):
                            #print(ecl)
                            if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth":
                                print(pid)
                                if re.match(r"^[0-9]{9}$", pid):
                                    print(hgt)
                                    if "cm" in hgt:
                                        if int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193:
                                            self.isValid = True
                                            print("Y")
                                    elif "in" in hgt:
                                        if int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76:
                                            self.isValid = True
                                            print("Y")
                                    

    def getIsValid(self):
        return self.isValid
