'''
This file implements the Heap data structure as a subclass of the BinaryTree.
The book implements Heaps using an *implicit* tree with an *explicit* vector
implementation,
so the code in the book is likely
to be less helpful than the code for the other data structures.
The book's implementation is the traditional
implementation because it has a faster constant factor
(but the same asymptotics).
This homework is using an explicit tree implementation to
help you get more practice with OOP-style programming and classes.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class
    declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        self.root = None
        self.num_nodes = 0
        if xs is not None:
            for x in xs:
                self.insert(x)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string
        that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap
        will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically
        test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        ret = True
        if node.left:
            ret &= node.value <= node.left.value
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= node.value <= node.right.value
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        '''
        Inserts value into the heap.

        FIXME:
        Implement this function.

        HINT:
        The pseudo code is
        1. Find the next position in the tree using the
        binary representation of
        the total number of nodes
            1. You will have to explicitly store the size
            of your heap in a variable
            (rather than compute it) to maintain the
            O(log n) runtime
            1. See https://stackoverflow.com/
            questions/18241192/implement-heap-using-
            a-binary-tree for hints
        1. Add `value` into the next position
        1. Recursively swap value with its parent
        until the heap property is satisfied

        HINT:
        Create a @staticmethod helper function,
        following the same pattern used in the
        BST and AVLTree insert functions.
        '''
        self.num_nodes += 1
        binary_str = bin(self.num_nodes)[3:]
        if self.root is None:
            self.root = Node(value)
        else:
            Heap._insert(self.root, value, binary_str)

    @staticmethod
    def _insert(node, value, binary_str):
        if binary_str[0] == '0':
            if len(binary_str) == 1:
                node.left = Node(value)
            else:
                Heap._insert(node.left, value, binary_str[1:])
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
        if binary_str[0] == '1':
            if len(binary_str) == 1:
                node.right = Node(value)
            else:
                Heap._insert(node.right, value, binary_str[1:])
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return Heap._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None and node.right is None:
            return node.value
        elif node.left is None:
            return min(node.value, Heap._find_smallest(node.right))
        elif node.right is None:
            return min(node.value, Heap._find_smallest(node.left))
        else:
            return min(node.value, Heap._find_smallest(node.left), Heap._find_smallest(node.right))

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.
        FIXME:
        Implement this function.
        HINT:
        The pseudocode is
        1. remove the bottom right node from the tree
        2. replace the root node with what was formerly the bottom right
        3. "trickle down" the root node: recursively swap it with its largest
        child until the heap property is satisfied
        HINT:
        I created two @staticmethod helper functions:
        _remove_bottom_right and _trickle.
        It's possible to do it with only a single helper
        (or no helper at all),
        but I personally found dividing up the code into
        two made the most sense.
        '''
        remove = list('{0:b}'.format(self.num_nodes))
        self.num_nodes = self.num_nodes - 1
        remove.pop(0)

        if len(remove) < 1:
            self.root = None
        else:
            self.root.value = Heap._remove_bottom_right(self.root, remove)
            Heap._trickle_down(self.root)
    
    @staticmethod
    def _remove_bottom_right(node, remove):
        '''
        Removes and returns the bottom right node in the
        subtree rooted at `node`.
        HINT:
        Recursively traverse the tree to the right until we hit a leaf node.
        '''
        if len(remove) == 1:
            if remove[0] == '1':
                number = node.right.value
                node.right = None
                return number
            else:
                number = node.left.value
                node.left = None
                return number
        elif remove[0] == '1':
            remove.pop(0)
            return Heap._remove_bottom_right(node.right, remove)
        else:
            remove.pop(0)
            return Heap._remove_bottom_right(node.left, remove)

    @staticmethod
    def _trickle_down(node):
        '''
        Recursively swap root with its smallest
        child until there is no child smaller.
        HINT:
        First find the index of the smallest child (if any)
        , then check if we need to swap.
        '''
        value = node.value
        if node.left is None:
            return None
        if node.right is None or node.right.value > node.left.value:
            child = node.left
        else:
            child = node.right
        if child.value < node.value:
            node.value = child.value
            child.value = value
            Heap._trickle_down(child)
