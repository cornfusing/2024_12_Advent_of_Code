# Advent of Code, Day 03, Riddle 1

# Regex, I guess
import re

with open('day_03_input.txt','r') as f:
    input = f.read()
    # Pattern: mul(x,y)
    # x and y are 1-3 digits long
    # => escaping () => \(\)
    # \d+ for 1 or more digits
    # ,
    # \d+ for 1 or more digits
    matches = re.findall('mul\(\d+,\d+\)',input)
    sum = 0
    print (matches)
    for match in matches:
        matchList = match.split(',')
        #leftEntry = re.search('\d',matchList[0])
        leftEntry = int(re.sub('\D','',matchList[0]))
        rightEntry = int(re.sub('\D','',matchList[1]))
        #print(leftEntry)
        #print(rightEntry)
        sum+=(leftEntry*rightEntry)
        #print(f"{leftEntry} * {rightEntry}")
        #print(matchList)
        #print(re.sub('((mul)\()|,|\)','',match))
    #print(matches)
    print(sum)

# PART 2
# in the text there is also do() and don't() statements, default is do().
# only mul(x,y)s after do() instructions are to be allowed.

with open('day_03_input.txt','r') as f:
    input = f.read()
    matches = re.findall('(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))',input)
    sum = 0
    doOrDontDo = True # default True for do(); False is don't()
    for match in matches:
        if match[0]:
            #print(match[0]) #debug
            doOrDontDo = True
        elif match[1]:
            #print(match[1]) #debug
            doOrDontDo = False
        else: 
            #print(match[2]) #debug
            print(f"DO or DONT: {doOrDontDo}")
            if doOrDontDo:
                matchList = match[2].split(',')
                leftEntry = int(re.sub('\D','',matchList[0]))
                rightEntry = int(re.sub('\D','',matchList[1]))
                print(f"New Sum = {sum} + {leftEntry} * {rightEntry}")
                sum+=(leftEntry*rightEntry)
        #print(match)
    
    print(sum)

