
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return 
        root = self.root
        while (root != None):
            if root.value > value:
                if root.left == None:
                    root.left = Node(value)
                    return 
                root = root.left
            else:
                if root.right == None:
                    root.right = Node(value)
                    return
                root = root.right
        
    def lookup(self, value):
        root = self.root
        while (root != None):
            if root.value > value:
                root = root.left
            elif root.value < value:
                root = root.right
            else:
                return True
        return False
    
    # def remove(self, root, value):
    #     if not root:
    #         return False
        
    #     if value < root.value:
    #         root = self.remove(root.left, value)
    #     elif value > root.value:
    #         root = self.remove(root.right, value)
    #     else:
    #         if not root.left:
    #             return root.right
    #         elif not root.right:
    #             return root.left
    #         else:
    #             next = root.right
    #             while next.left:
    #                 next = next.left
    #             root.value = next.value
    #             self.remove(root.right, next.value)
    #     return root
    
    def remove(self, value):
        def remove_node(node, value):
            if not node:
                return None
            if node.value == value:
                if not node.left and not node.right:
                    return None
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.value = temp.value
                node.right = remove_node(node.right, temp.value)
            elif node.value > value:
                node.left = remove_node(node.left, value)
            else:
                node.right = remove_node(node.right, value)
            return node

        self.root = remove_node(self.root, value)
            
    def print_tree(self):
        if self.root == None:
            print("Empty binary search tree")
            return
        self.print_node(self.root, "", True)

    def print_node(self, node, prefix, is_left):
        if node == None:
            return
        print(f"{prefix}{'|-- ' if is_left else '`-- '}{node.value}")
        self.print_node(node.left, prefix + ("|   " if is_left else "    "), True)
        self.print_node(node.right, prefix + ("|   " if not is_left else "    "), False)



if __name__ == "__main__":
    Tree = BinaryTree()
    Tree.insert(8)
    Tree.insert(5)
    Tree.insert(2)
    Tree.insert(6)
    Tree.insert(10)
    Tree.insert(9)
    Tree.print_tree()
    Tree.remove(8)
    Tree.print_tree()
