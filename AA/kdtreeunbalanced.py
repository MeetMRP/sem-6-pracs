class Node:
    def __init__(self, point, axis):
        self.point = point
        self.left = None
        self.right = None
        self.axis = axis

class KDTree:
    def __init__(self, dimensions):
        self.root = None
        self.dimensions = dimensions
        
    def insert(self, point, node=None, depth=0):
        if node is None:
            node = self.root
        
        if node is None:
            axis = depth % self.dimensions
            self.root = Node(point, axis)
            return
        
        axis = depth % self.dimensions
        if point[axis] < node.point[axis]:
            if node.left is None:
                node.left = Node(point, (depth + 1) % self.dimensions)
            else:
                self.insert(point, node.left, depth + 1)
        else:
            if node.right is None:
                node.right = Node(point, (depth + 1) % self.dimensions)
            else:
                self.insert(point, node.right, depth + 1)
                
def print_kd_tree(node, depth=0):
    if not node:
        return
    print("    " * depth + f"({node.point})")
    print_kd_tree(node.left, depth + 1)
    print_kd_tree(node.right, depth + 1)

# Example usage
kd_tree = KDTree(2)
points = [(3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)]
for point in points:
    kd_tree.insert(point)
print('Pre-order Traversal')
print_kd_tree(kd_tree.root)
