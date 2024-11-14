class Tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


n = int(input())
tree = {}
firstData = ""


def pre_order(node):
    print(node.data, end="")

    if node.left is not None:
        pre_order(tree[node.left])

    if node.right is not None:
        pre_order(tree[node.right])


def in_order(node):
    if node.left is not None:
        in_order(tree[node.left])

    print(node.data, end="")

    if node.right is not None:
        in_order(tree[node.right])


def post_order(node):
    if node.left is not None:
        post_order(tree[node.left])

    if node.right is not None:
        post_order(tree[node.right])

    print(node.data, end="")
    return


for i in range(n):
    data, left, right = input().split()
    if i == 0:
        firstData = data

    if left == ".":
        left = None

    if right == ".":
        right = None

    tree[data] = Tree(data, left, right)

pre_order(tree[firstData])
print()
in_order(tree[firstData])
print()
post_order(tree[firstData])
