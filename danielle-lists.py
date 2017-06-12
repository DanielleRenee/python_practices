def all_vowel_words(lst):
    """Return a list containing every word that starts with a vowel.

    This function takes in a list of words. It should return a list
    containing only the words from the input list that start with vowels.

    Assume that 'y' always counts as a vowel.

        >>> all_vowel_words(['apple', 'berry', 'cherry'])
        ['apple']

        >>> all_vowel_words(['bear', 'duck'])
        []

        >>> all_vowel_words(['yellow', 'green', 'eggplant'])
        ['yellow', 'eggplant']
    """

    #make and empty list to store the words that have a vowel as the first letter
    vowely_lst = [] 
    #check the first letter of the first word to see if the string of vowels
    #from lecture, could try if word.startwith, but string seems easier
    for word in lst:
            if word[0][0] in 'aeiouy':
                vowely_lst.append(word)

    return vowely_lst


def is_item_in_list(lst, item):
    """Return True if item is in the list, False if not.
    
        >>> is_item_in_list(['apple', 'berry', 'cherry'], 'durian')
        False

        >>> is_item_in_list(['apple', 'berry', 'cherry'], 'berry')
        True
    """
    if item in lst:
        return True
    else: 
        return False


def print_index_of_item(lst, item):
    """Print the index of an item in a list, followed by the item.

    If the item appears multiple times in the list, return the index and
    the item for each time it appears in the list.

    If the item does not appear, print '_item_ not found' (substitute the
    name of the item.)

        >>> print_index_of_item(['a', 'b', 'c', 'b', 'c'], 'b')
        1 b
        3 b

        >>> print_index_of_item([1, 2, 3], 4)
        4 not found

        >>> print_index_of_item(['apple', 'berry', 'cherry', 'durian'], 'apple')
        0 apple
    """

# look to see if item exists in the list
# iterate over the list and only print if word is equal to item
# per lecture notes, use enumerate() function
# Notes to self per python docs: Return an enumerate object. sequence must be a sequence, 
# an iterator, or some other object which supports iteration. 
# The next() method of the iterator returned by enumerate() returns a 
# tuple containing a count (from start which defaults to 0) and the values 
# obtained from iterating over sequence:

    if item not in lst:
        print '{} not found'.format(item)

    if item in lst:
        for index, word in enumerate(lst):
            if word == item:
                print index, word


# You can ignore everything below here
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")