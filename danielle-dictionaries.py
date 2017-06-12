



def create_state_capital_dictionary():
    """Create a dictionary that maps a state name to its capital. 

    This dictionary should contain at least the following three states and capitals:
        The capital of California is Sacramento.
        The capital of Washington is Olympia.
        The capital of Oregon is Salem.

        >>> capitals = create_state_capital_dictionary()

        >>> capitals['California']
        'Sacramento'

        >>> capitals['Washington']
        'Olympia'

        >>> capitals['Oregon']
        'Salem'
    """

    cap_dict = {'California': 'Sacramento',
                'Washington': 'Olympia',
                'Oregon': 'Salem',
                }

    for state in cap_dict:
        capital = cap_dict[state]
    
    return cap_dict

    #capitals = create_state_capital_dictionary()
    #per lecture notes on dictionaries, using the items method to unpack tuple
    #in the for statement is very common. Didn't use, just notes to self:
    # for state, capital in state_capitals.items():
    #     print "The capital of {} is {}.".format(capitals[state], capitals[capital])

inv = {'apples': 5, 'berries': 0, 'cherries': 3}

def get_inventory(inventory, item):
    """Takes in an inventory of items (dictionary) and an item. Prints the
    number of that item in the inventory.

    If the item is not in the inventory, function should print
    "Cannot find __item__"

        >>> inv = {'apples': 5, 'berries': 0, 'cherries': 3}
        
        >>> get_inventory(inv, 'apples')
        5 apples
        
        >>> get_inventory(inv, 'berries')
        0 berries

        >>> get_inventory(inv, 'durian')
        Cannot find durian

    """

    
    if item not in inventory:
        print 'Cannot find {}'.format(item)

    if item in inventory:
        quantity = inventory[item]
        print quantity, item


items = ['a', 'b', 'a', 'c', 'd', 'e', 'a', 'e']

def count_items(items):
    """Take in a list of items and return a dictionary with each item and
    the number of times it appears in the list.

        >>> items = ['a', 'b', 'a', 'c', 'd', 'e', 'a', 'e']

        >>> item_counts = count_items(items)
        
        >>> sorted(item_counts.items())
        [('a', 3), ('b', 1), ('c', 1), ('d', 1), ('e', 2)]
    """
    #look at a list, the first time a letter appears add it as a key to the dict
    #and set its value to 1. if the letter is already in the dict, modify its value +1
    #per lecture notes, counting with dictionaries section 

    item_counts = {}

    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1

    #return the dict
    #print item_counts
    return item_counts


# Optional
import itertools
def find_word_lengths(words):
    """Take in a list of words and return a dictionary where the key is the
    length of a word and the value is a list of words of that length.

        >>> words = ['blue', 'green', 'pink', 'yellow', 'lavender']

        >>> word_lengths = find_word_lengths(words)
        
        >>> sorted(word_lengths.items())
        [(4, ['blue', 'pink']), (5, ['green']), (6, ['yellow']), (8, ['lavender'])]
    """
    #example key = 4, and value is any word from the list with four letters
    #I need to put them in piles bassed on their letter count
    #research brought up itertools.groupby but not sure how to use it properly.
    #per https://community.modeanalytics.com/python/tutorial/pandas-groupby-and-python-lambda-functions/
    #https://docs.python.org/2/library/itertools.html
    #found a crazy comprehension that does everything in one step 
    #I totally do not follow, but was still able to mess around with it
    #and make it print a pretty dictionary in my terminal

        # word_lengths = {}

        # for word in words:
        #     word_lengths[word] = len(word)

        # return word_lengths

    return {x:list(y) for x,y in itertools.groupby(sorted(words,key=len), key=lambda x:len(x))}

# You can ignore everything below here
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")