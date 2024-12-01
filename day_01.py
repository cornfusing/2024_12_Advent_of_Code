'''
Advent of Code, Day 01, Riddle 1
Thoughts:
* List 1
* List 2
* sort both
* sum
'''

leftList = list()
rightList = list()
sumOfDifs = 0

with open("day_01_1_input.txt","r") as f:
    lines = f.read().splitlines()
    for line in lines:
        splittedLine = line.split("   ")
        rightList.append(splittedLine.pop())
        leftList.append(splittedLine.pop())

leftList.sort()
rightList.sort()

for i, entry in enumerate(leftList):
    dif = int(leftList[i]) - int(rightList[i])
    if dif < 0: dif*=-1
    sumOfDifs += dif
    #print(f"Dif: {dif}")
    
print(f"Final: {sumOfDifs}")

'''
Riddle 2:
Similarity score:
how often does every number on the left occure on the right
sum up for every number

thoughts:
* make lists again
* iterate left
** iterate right for every left
done
'''

similarityScore = 0

for leftEntry in leftList:
    similarities = 0
    for rightEntry in rightList:
        if leftEntry==rightEntry: similarities+=1
    
    similarityScore += (int(leftEntry)*similarities)

print(f"Similarity Score: {similarityScore}")