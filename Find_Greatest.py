# Find the greates number from the list without using max() and sorted()

def find_greatest(t):
    max_value = t[0]

    for i in t:
        if i>max_value:
            max_value = i
    
    return(max_value)


print(find_greatest([3, 7, 1, 9, 4]))

'''
One line approach:
print(sorted(t)[-1])
'''