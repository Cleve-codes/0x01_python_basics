
class TreeNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root =None

  def _insert(self, node, key):
    if node is None:
      return TreeNode(key)

    if key < node.key:
      node.left = self._inser(node.left, key)
    elif key > node.key:
      node.right = self._inser(node.right, key)
    return node

  def insert(self, key):
    self.root = self._insert(self.root, key)

  def _search(self, node, key):
    if node is None or node.key == key:
      return node

    if key < node.key:
      return self._search(node.left, key)

    return self._search(node.right, key)

  def search(self, key):
    return self._search(self.root, key)
