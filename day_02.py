# Advent of Code, Day 02, Riddle 1

# Safe: levels are either all increasing all decreasing
# Safe: Any two adjacent levels differ by at least one at most three

'''
Count the safe level-lines.
Safe conditions:
* Line is all increasing or all decreasing
* Levels next to each other within a line differ 1-3 (0 is also unsafe)

Thoughts:
Make lists
check increase/decrease
check differences
count
'''



with open("day_02_input.txt","r") as f:
    lines = f.read().splitlines()
    safeCounter = 0
    for line in lines:
        safe = True # safe as long as not unsafe :)
        levels = [int(x) for x in line.split(" ")]
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
            
        if safe is True:
            safeCounter+=1
            # print(f"New safe counter: {safeCounter}") # debug
    print(safeCounter)