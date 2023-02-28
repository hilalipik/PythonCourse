def highest_even(li):
    '''
    Function finds the highest number in list that is divisible by 2.
    Input: list.
    Output: the highest number in list that is divisible by 2.
    '''
    max = li[0]
    for i in li:
        if i > max and i %2==0:
            max = i
    return max

print(highest_even([101,3,4,5,99,200,1]))