class Node:
    def __init__(self, point, axis):
        self.point = point
        self.left = None
        self.right = None
        self.axis = axis

class KDTree:
    def __init__(self, points, dimensions=2):
        self.root = self.build_tree(points, 0, dimensions)
        
    def build_tree(self, points, depth, dimensions):
        if not points:
            return None
        
        axis = depth % dimensions
        points.sort(key=lambda x: x[axis])
        median = len(points) // 2
        
        node = Node(points[median], axis)
        node.left = self.build_tree(points[:median], depth + 1, dimensions)
        node.right = self.build_tree(points[median+1:], depth + 1, dimensions)
        
        return node
                
def print_kd_tree(node, depth=0):
    if not node:
        return
    print("    " * depth + f"({node.point})")
    print_kd_tree(node.left, depth + 1)
    print_kd_tree(node.right, depth + 1)

# Example usage
points = [(3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)]
kd_tree = KDTree(points)
print('Pre-order Traversal')
print_kd_tree(kd_tree.root)
