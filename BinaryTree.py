
class BT_Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def populate_tree_helper(self, parent_string, left_right_string, level):
        print("level: " + str(level))
        data = input("enter the " + left_right_string + "data for " + parent_string + ": ")
        if data == "":
            return None
        node = BT_Node(data)
        node.left = self.populate_tree_helper(node.data, 'left ', level + 1)
        node.right = self.populate_tree_helper(node.data, 'right ', level + 1)
        return node

    def populate_tree(self):
        self.root = self.populate_tree_helper("root", "", 0)

    def print_tree_recur(self, node):
        if node == None:
            return

        #preorder
        print(node.data)
        self.print_tree_recur(node.left)
        #inorder
        self.print_tree_recur(node.right)
        #postorder

    def print_tree(self):
        self.print_tree_recur(self.root)


tree = BinaryTree()
tree.populate_tree()
tree.print_tree()