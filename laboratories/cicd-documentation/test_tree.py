import unittest
from tree import Tree


class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(0)
        self.tree.add(8)
        self.tree.add(2)

    def test_find_existing_value(self):
        node = self.tree._find(4, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 4)

    def test_find_missing_value(self):
        node = self.tree._find(10, self.tree.getRoot())
        self.assertIsNone(node)

    def test_find_root_value(self):
        node = self.tree._find(3, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 3)


if __name__ == "__main__":
    unittest.main()