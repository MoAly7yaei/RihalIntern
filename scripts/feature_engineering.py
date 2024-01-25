

def extract_integers(array): # To extract numbers in strings

    temp = []
    value = 0

    for string in array:
        for char in string:

            if char.isdigit():
                temp.append(int(char))
    
    for i in range(len(temp)):

        try:
            value = value + temp[-(i+1)] * (10**i)
        except:
            break #For Indexing boundries Eror
    
    return value





        