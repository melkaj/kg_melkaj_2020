
# Meldin Kajoshaj
# Coding assessment for Kargo

import sys
from definitions import is_one_to_one

# Getting strings from the command line
if len(sys.argv) == 3:
    str1 = sys.argv[1]
    str2 = sys.argv[2]

    # Getting final answer and printing it out to the console
    final_answer = is_one_to_one(str1, str2)
    print(f'\n{final_answer}')

else:
    print("\nRetry with the correct number of arguments please")



