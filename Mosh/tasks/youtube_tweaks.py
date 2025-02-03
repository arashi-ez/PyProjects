"""Lambda expression"""
def lambda_simple(n, k):
    return(lambda x,y : x + y)(n,k) #just one line addition 

"""One Liner!"""
def name_input():
    user_input = input('Name: ')
    name = user_input or "N/A"
    print(name) 
"""reversing order -> for lists, tuples, strings etc (sequence type)"""
def reverse_string(string):
    words = string.split()
    reversed = words[::-1]
    return ' '.join(reversed)

'''same but better'''
def reverse(st):
    # Your Code Here
    return " ".join(st.split()[::-1])
