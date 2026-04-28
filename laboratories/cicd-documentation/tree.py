from node import Node


class Tree:
    """Tree class for binary tree."""

    def __init__(self):
        """Constructor for Tree class."""
        self.root = None

    def getRoot(self):
        """Get the root of the tree.

        Returns:
            Node: root node of the tree, or None if the tree is empty.
        """
        return self.root

    def add(self, data):
        """Add data to the tree.

        Args:
            data (int): data to add.

        Returns:
            None
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Add data to the tree starting from a given node.

        Args:
            data (int): data to add.
            node (Node): current node.

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Find data in the tree.

        Args:
            data (int): data to find.

        Returns:
            Node: node with the searched data, or None if not found.
        """
        if self.root is not None:
            return self._find(data, self.root)

        return None

    def _find(self, data, node):
        """Find data starting from a given node.

        Args:
            data (int): data to find.
            node (Node): current node.

        Returns:
            Node: node with the searched data, or None if not found.
        """
        if data == node.data:
            return node
        elif data < node.data and node.left is not None:
            return self._find(data, node.left)
        elif data > node.data and node.right is not None:
            return self._find(data, node.right)

        return None

    def deleteTree(self):
        """Delete all nodes from the tree.

        Returns:
            None
        """
        self.root = None

    def printTree(self):
        """Print the tree using inorder traversal.

        Returns:
            None
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def printPreorderTree(self):
        """Print the tree using preorder traversal.

        Returns:
            None
        """
        if self.root is not None:
            self._printPreorderTree(self.root)

    def printPostorderTree(self):
        """Print the tree using postorder traversal.

        Returns:
            None
        """
        if self.root is not None:
            self._printPostorderTree(self.root)

    def _printInorderTree(self, node):
        """Print tree nodes in inorder traversal.

        Inorder traversal means:
        left subtree, current node, right subtree.

        Args:
            node (Node): current node.

        Returns:
            None
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """Print tree nodes in preorder traversal.

        Preorder traversal means:
        current node, left subtree, right subtree.

        Args:
            node (Node): current node.

        Returns:
            None
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """Print tree nodes in postorder traversal.

        Postorder traversal means:
        left subtree, right subtree, current node.

        Args:
            node (Node): current node.

        Returns:
            None
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')