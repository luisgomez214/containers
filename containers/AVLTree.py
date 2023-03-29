'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()
       # if xs is not None:
       #     for x in xs:
       #         self.insert(x)
    
    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        if self.root is None:
            return True 
        else:
            return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        elif not node:
            return True
        else:
            left_satisfied = AVLTree._is_avl_satisfied(node.left)
            right_satisfied = AVLTree._is_avl_satisfied(node.right)
            return left_satisfied and right_satisfied
       # stack = [node]
       # while stack:
        #    node = stack.pop()
        #    balance_factor = AVLTree._balance_factor(node)
        #    if balance_factor not in [-1,0,1]:
        #        return False
        #    if node.left is not None:
        #        stack.append(node.left)
        #    if node.right is not None:
        #        stack.append(node.right)
        #return True
       # ret = True
       # if node is None:
       #     return True
       # if AVLTree._balance_factor(node) not in [-1, 0, 1]:
       #     return False
       # else:
       #     if node.left:
       #        ret&= AVLTree._is_avl_satisfied(node.left)
       #     if node.right:
       #        ret&= AVLTree._is_avl_satisfied(node.right)
       # return ret


    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        original = node
        if original.right: 
            newRoot = Node(original.right.value)
            newRoot.left = Node(original.value)
            newRoot.right = original.right.right
            newRoot.left.left = original.left
            newRoot.left.right = original.right.left
            return newRoot
        else:
            return original 

    
    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        original = node
        if original.left: 
            newRoot = Node(original.left.value)
            newRoot.right = Node(original.value)
            newRoot.left = original.left.left
            newRoot.right.right = original.right
            newRoot.right.left = original.left.right
            return newRoot
        else:
            return original
    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        '''
        Inserts value into the BST rooted at node.
        '''
        #if not node:
        #    return Node(value)
        #if value< node.value:
        #    node.left = AVLTree._insert(node.left, value)
        #else:
        #    node.right = AVLTree._insert(node.right, value)
        #node.height = 1 + max(AVLTree._height(node.left), AVLTree._height(node.right))
        #node = AVLTree._rebalance(node)
        #return node
        if not node:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return  AVLTree._left_rotate(node)
        return node


    def insert_list(self, xs):
        for i in xs:
            return self.insert(i)  


    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        #if node:
         #   balance_factor = AVLTree._balance_factor(node)
        #if balance_factor > 1:
         #   if AVLTree._balance_factor(node.left) < 0:
          #      node.left = AVLTree._right_rotate(node.right)
           # node = AVLTree._left_rotate(node)
        #elif balance_factor < -1:
         #   if AVLTree._balance_factor(node.right) > 0:
          #      node.right = AVLTree._right_rotate(node.right)
           # node = AVLTree._left_rotate(node)
        balance = AVLTree._balance(node)
        if balance > 1:
            if AVLTree._balance(node.left)>=0:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVL._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if balance < -1:
            if AVLTree._balance(node.right)<=0:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.left)
                return AVLTree._left_rotate(node)
        return node
        #return node