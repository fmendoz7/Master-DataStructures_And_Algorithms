"""
    Dynamic Array in Python is literally just a list...

    The nice thing about Python lists (arrays) is that they are dynamic by nature

    If you are looking for a WHOLLY IMMUTABLE version after declaration, use tuples

    If you are looking for an ITERABLE, MUTABLE list with NO DUPLICATES, use a set
"""
"""----------------------------------------------------------------------"""
#--LISTS-- []
exampleList = []

#If you want to add something to a set, encapsulate it with []
exampleList += [1]

#You can also use .append() to add something to list
exampleList.append(2)
"""----------------------------------------------------------------------"""
#--TUPLES-- ()

#CANNOT add anything to tuple NOR change it once declared
exampleTuple = ('z', 'y') 
"""----------------------------------------------------------------------"""
#--SETS--
exampleSet = set()

#If you want to add something to a set, use .add()
exampleSet.add('a')
"""----------------------------------------------------------------------"""
"""
    RESOURCES
        1. 
        2.
        3. SETS: https://www.geeksforgeeks.org/sets-in-python/
"""