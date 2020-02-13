#Depth-First Search Algorithm

"""
BACKGROUND
    1. Uses stack to store fringe
    2. Expands the successors ONE AT A TIME
        > Checks to see if successor has children
        > If successor has children, will go DEEPER down that path
        > Else, will exit, POP successor off the stack and go to sibling successor

LIMITATIONS
    1. Problem of looping- if given infinite tree, DFS will never escape
        > COUNTER: Use Iterative Deepening Depth-First Search

"""