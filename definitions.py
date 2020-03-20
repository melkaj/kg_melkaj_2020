
# boolean function to find out if two strings can be 
# mapped one to one
def is_one_to_one(str1, str2):
    # Initializing empty dictionaries
    list_str1 = []
    list_str2 = []

    # Iterate through the first string to find all unique characters
    for char in str1:
        if char not in list_str1:
            list_str1.append(char)    
        
    # Iterate through the second string to find all unique characters
    for char in str2:
        if char not in list_str2:
            list_str2.append(char)
        
    # Getting amount of unique characters in each string
    amount_of_unique_char_str1 = len(list_str1)
    amount_of_unique_char_str2 = len(list_str2)

    # If amount of unique characters in string one is more or equal,
    # to the amount in string two, then return True
    if (amount_of_unique_char_str1 >= amount_of_unique_char_str2):
        return True
    else: 
        return False
