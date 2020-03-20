
# Meldin Kajoshaj
# Coding assessment for Kargo

import sys
from definitions import is_one_to_one

# Getting strings from the command line
str1 = sys.argv[1]
str2 = sys.argv[2]

# myDict = {}
# myDict['r'] = 3
# print(myDict['r'])
# myDict['r'] = myDict['r'] + 1
# print(myDict['r'])

# myDict = {'4': 4, '5': 5, '6': 6}
# print(len(myDict))


# Getting final answer and printing it out to the console
final_answer = is_one_to_one(str1, str2)
print(f'\n{final_answer}')



