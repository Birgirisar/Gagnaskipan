
class GT_Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []


class GeneralTree:
    def __init__(self):
        self.root = None
    

    def populate_tree_helper(self):
        data = input()
        if data == "":
            return None

        node = GT_Node(data)
        while True:
            child_node = self.populate_tree_helper()
            if child_node == None:
                break
            node.children.append(child_node)

        return node

    def populate_tree(self):
        self.root = self.populate_tree_helper()

    def print_tree_recur(self, node):
        if node == None:
            return
        print(str(node.data), end=" ")
        for child_node in node.children:
            self.print_tree_recur(child_node)
  
    def print_tree(self):
        self.print_tree_recur(self.root)


tree = GeneralTree()
tree.populate_tree()
tree.print_tree()