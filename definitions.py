
# Helper function
def sum_of_lists(list1):
    total = 0
    for elem in list1:
        total += elem
    return total


# boolean function to find out if two strings can be 
# mapped one to one
def is_one_to_one(str1, str2):
    # Initializing empty dictionaries
    dict_str1 = {}
    dict_str2 = {}

    # Iterate through the first string to get count of unique characters
    for char in str1:
        if dict_str1.get(char) == None:
            dict_str1[char] = 1
        else:
            dict_str1[char] = dict_str1[char] + 1    
        
    # Iterate through the second string to get count of unique characters
    for char in str2:
        if dict_str2.get(char) == None:
            dict_str2[char] = 1
        else:
            dict_str2[char] = dict_str2[char] + 1

    # Getting amount of unique characters in each string
    amount_of_unique_char_str1 = len(dict_str1)
    amount_of_unique_char_str2 = len(dict_str2)

    # If amount of unique characters in each string match,
    # then it can be mapped one to one
    if (amount_of_unique_char_str1 == amount_of_unique_char_str2):
        return True
    else: 
        list_str2 = list(dict_str2.values())
        # for the when the amount of unique characters in string1 is greater than string 2
        # Then we have to check if the amount of unique characters in string 1 is less than 
        # the total characters in string 2
        # (ex: hel - php)
        if (amount_of_unique_char_str1 >= amount_of_unique_char_str2
             and amount_of_unique_char_str1 <= sum_of_lists(list_str2)):
            return True
        else:
            return False


