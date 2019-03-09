# make the function inside function

def printoutscore(data):
    # define local function
    def countingscore(uts, uas):
        return (0.4* uts) + (0.6 * uas)

    # define local function
    def getscoreindex(score):
        idx = ''
        if score >= 80: idx = 'A'
        elif score >= 70: idx = 'B'
        elif score >= 60: idx = 'C'
        elif score >= 40: idx = 'D'
        else : idx = 'E'
        return idx

    # print every single data line
    for line in data:
        nim = line[0]
        name = line[1]
        uts = line[2]
        uas = line[3]
        score = countingscore(uts, uas)
        index = getscoreindex(score)
        print('%s\t%s\t%0.2f\t%s'% (nim, name, score, index))


data = [
    ['101', 'Andi', 50, 30],
    ['102', 'Rizki', 90, 85],
    ['103', 'Anis', 100, 90],
    ['104', 'Abimanyu', 95, 90],
    ['105', 'Yudistira', 85, 79],
    ['106', 'Santika', 85, 79]
]

# call the function
printoutscore(data)


'''
countingscore() and getscoreindex() is the local function
'''
