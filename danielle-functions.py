# Define your function below.

nums = [5, 12, 6, 7, 4, 9, 10]
not_all_nums = [4, 5, 6, 8, 'w', 'o', 'w']

def even_or_odd(lst, string='even'):
    """
    Take two arguments, a list and a string indicating whether the user wants a 
    new list containing only the odd or even numbers. Return the user its new list.
    """
#set the parameter for an odd or even number by using modulo
#set default to even if not specified
#if asked for an odd list, only return a number from the input list that num % 2 would be 1
#play around with isinstance to check if list includes all integers, per python
#docs and stack overflow https://stackoverflow.com/questions/6009589/how-to-test-if-every-item-in-a-list-of-type-int
#per python docs on handling exceptions and also watched: https://www.youtube.com/watch?v=hrR0WrQMhSs
    
    # if all(isinstance(item, int) for item in lst):
    try:
     
        even_lst = [x for x in lst if x % 2 == 0]

        odd_lst = [x for x in lst if x % 2 == 1]

        if string == 'odd':
            #print odd_lst
            return odd_lst

        if string == 'even':
            #print even_lst
            return even_lst

    except: 
        raise ValueError("Shoot, this function can only take a list of integers!")



# Call your function here (details on specifically how to call the function
# are in the assessment instructions.)


list_1  = even_or_odd(nums,)
print list_1

list_2 = even_or_odd(nums, 'odd')
print list_2

list_3 = even_or_odd(nums)
print list_3

print (list_1 == list_2)

print (list_1 == list_3)

#even_or_odd(not_all_nums,)


