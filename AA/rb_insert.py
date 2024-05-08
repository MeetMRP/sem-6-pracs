class Node:
    def __init__(self, item, color=1):
        self.item = item
        self.color = color
        self.parent = self.left = self.right = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, 0)
        self.root = self.TNULL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent and k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def insert(self, key):
        node = Node(key)
        node.left = node.right = self.TNULL
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            x = x.left if node.item < x.item else x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node
        if node.parent is None or node.parent.parent is None:
            return
        self.fix_insert(node)

    def print_helper(self, node, indent, last):
        if node != self.TNULL:
            print(indent + ("R---> " if last else "L---> ") + str(node.item) + 
                  ("(RED)" if node.color == 1 else "(BLACK)"))
            self.print_helper(node.left, indent + ("     " if last else "|    "), False)
            self.print_helper(node.right, indent + ("     " if last else "|    "), True)

    def print_tree(self):
        self.print_helper(self.root, "", True)

if __name__ == "__main__":
    bst = RedBlackTree()
    nodes = [int(input(f"\nEnter value of Node {i+1} : ")) for i in range(int(input("Enter Number of nodes: ")))]
    for value in nodes:
        bst.insert(value)
    bst.print_tree()
    while True:
        option = int(input("Menu:\n1.Add new Node\n2.Exit:\nEnter Option: "))
        if option == 1:
            bst.insert(int(input("Enter new Node: ")))
            bst.print_tree()
        elif option == 2:
            print("Exit")
            break
