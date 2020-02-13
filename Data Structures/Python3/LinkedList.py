"""
    LinkedLists traditionally linked nodes with pointers in lower-level languages

    VARIATIONS
        1. Singly-Linked List (points towards end)
        2. Doubly-Linked List (points towards end and head)
        3. Nested Linked List (Hierarchal LL. Can be Singly or Doubly linked but have "subnodes")

    EMPIRIC CHARACTERISTICS
        1. Node
            > Data Payload
        2. Pointing Mechanism
        3. Iterating Mechanism
"""

class LLNode:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SinglyLinkedList:
    def __init__(self):
        self.headval = None

exampleLL = SinglyLinkedList()
exampleLL = LLNode("Francis")
    #Is linkedlist technically declared as the pointer node?
    #REM: THere is no such thing as pointers in python

n2 = LLNode("Evelyn")
n3 = LLNode("Meghan")

#Link nodes together
exampleLL.headval.nextval = n2
n2.nextval = n3

