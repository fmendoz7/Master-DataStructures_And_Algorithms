"""
    Heaps are tree-based data structures (COMPLETE binary tree- all nodes except *not strict* last gen have children)

    TYPES OF HEAPS
        1. Max-Heap
            > Root must be the MAXIMUM (local & global)

        2. Min-Heap
            > Root must be the minimum (local & global)
            > Ex:

                 10                                 10
                /  \                              /    \
              20   100                          15      30
             /                                  /\      /\
            30                                 40 50   100 40

    COMMON HEAP OPERATIONS
        1. getMini()
            > Returns root element of the min heap
            > Time Complexity: O(1)

        2. extractMin()/extractMax()
            > Removes minimum or maximum element from MinHeap
            > Time Complexity: O(log(n))
                i. Needs to use heapify with each iteration of removing root

        3. decreaseKey()
            > Decreases value of key
            > Time Complexity: O(log(n))

        4. insert()
            > Inserting new key to fix violated min or max heap property
            > Time Complexity: O(log(n))

        5. delete()
            > extractMin or extractMax called to  eliminate specified node with assigned key
            > "To be deleted with minimum infinite"
            > Time Complexity: O(log(n))
"""

class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)/2

    def insertKey(self, k):
        heappush(self.heap, k)

    