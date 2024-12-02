# Advent of Code, Day 02, Riddle 2

# Task: if you remove 1 level from the reportlist, will it be safe then?
# Thoughts: make riddle 1 solution into method, make 2nd method and use 1st solution for each possibility

def readLines(fileName):
    with open(fileName,"r") as f:
        return f.read().splitlines()
    
def checkIfLineIsSafe(lineToCheck):
    safe = True
    levels = [int(x) for x in lineToCheck.split(" ")]
    increaseMode = 0 # 1 = increase; 2 = decrease
    prevLevel = 0 # memory of last iterated level
    levelAmount = len(levels)
    # print(f"Line with {levelAmount} Levels.") # debug
    for i, level in enumerate(levels):
        if i == 1: # first level
            if level > prevLevel:
                increaseMode = 1
                if ((level - prevLevel) <= 0 or (level - prevLevel)>3): safe = False
            elif level < prevLevel:
                increaseMode = 2
                if ((prevLevel - level) <= 0 or (prevLevel - level)>3): safe = False
            else:
                safe = False
        if i > 1: # next levels
            if increaseMode == 1 and ((level - prevLevel) <= 0 or (level - prevLevel)>3):
                safe = False
            if increaseMode == 2 and ((prevLevel - level) <= 0 or (prevLevel - level)>3):
                safe = False
        # print(f"Index {i}\t{level}\tPrev: {prevLevel}\tIncrease Mode: {increaseMode}\tSafe: {safe}") # debug
        prevLevel = level # Keep level until next iteration
    return safe

def checkRiddle2(lineToCheck):
    safeAfterRemoving = False
    levels = [x for x in lineToCheck.split(" ")]
    print(f"Base levels: {levels}")
    for i in range(0, len(levels)):
        tempLevels = list()
        for j in range(0, len(levels)):
            if j != i: tempLevels.append(levels[j])
        tempLine = ""
        for k, level in enumerate(tempLevels):
            if k == 0: tempLine = level
            if k > 0: tempLine += " " + level
        print(f"Check tempLevels: {tempLine}")
        if checkIfLineIsSafe(tempLine):
            safeAfterRemoving = True
            break
    print(f"Is it safe? {safeAfterRemoving}")
    return safeAfterRemoving


def main():
    lines = readLines("day_02_input.txt")
    safeCounter = 0
    for line in lines:
        if checkIfLineIsSafe(line): safeCounter+=1
        else:
            if checkRiddle2(line): safeCounter+=1
    
    print(safeCounter)

main()
