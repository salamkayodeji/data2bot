#function that gets all the keys and values in the dictionary
def get_v_k(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from get_v_k(value)
        elif type(value) is list:
            yield (key, value)
            for i in value:
                if type(i) is dict:
                    yield from get_v_k(i)
        else:
            yield (key, value)
           
#function that checks all the values data types  
def check_type(value):
        if value == True or value == False : return None
        if isinstance(value, str) : return "string" 
        if isinstance(value, int) : return "integer" 
        if all(isinstance(x, str) for x in value) and value != [] and not isinstance(value, dict) : return "enum" 
        if isinstance(value, dict) : return "array" 


""" 
# Global Array storing word for each digit
arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
 
def number_2_word(n):
 
    # If all the digits are encountered return blank string
    if(n==0):
        return ""
     
    else:
        # compute spelling for the last digit
        small_ans = arr[n%10]
 
        # keep computing for the previous digits and add the spelling for the last digit
        ans = number_2_word(int(n/10)) + small_ans + " "
     
    # Return the final answer
    return ans
"""
