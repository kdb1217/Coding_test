import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Bst:
    def __init__(self, head):
        self.head = head

    def insert_Node(self, value):
        base_Node = self.head
        while True:
            if base_Node.value > value:
                if base_Node.left is not None:
                    base_Node = base_Node.left
                else:
                    base_Node.left = Node(value)
                    break
            else:
                if base_Node.right is not None:
                    base_Node = base_Node.right
                else:
                    base_Node.right = Node(value)
                    break


def inorder_Serach(node):
    if node.left is not None:
        inorder_Serach(node.left)

    if node.right is not None:
        inorder_Serach(node.right)

    print(node.value)


cnt = 0
while True:
    try:
        a = int(input())
        if cnt == 0:
            binaryTree = Bst(Node(a))
        else:
            binaryTree.insert_Node(a)
        cnt += 1
    except EOFError:
        if cnt >= 1:
            inorder_Serach(binaryTree.head)
        else:
            print(binaryTree.head.value)
        break

