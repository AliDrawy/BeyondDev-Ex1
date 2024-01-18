class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_path(root, node, path):
    # check if there is no path
    if root is None:
        return False

    # Add the current node to the path
    path.append(root.value)

    # If the current node is the target node, return True
    if root.value == node:
        return True

    # Check in the left and right subtrees
    if (root.left and find_path(root.left, node, path)) or (root.right and find_path(root.right, node, path)):
        return True

    # If the current node is not part of the path to the target node, remove it
    path.pop()
    return False

def find_lowest_common_ancestor(root, node1, node2):
    # Initialize paths for node1 and node2
    path1, path2 = [], []

    # Find paths from the root to node1 and node2
    if not find_path(root, node1, path1) or not find_path(root, node2, path2):
        return None  # One or both nodes not present in the tree

    # Compare paths to find the lowest common ancestor
    print(path1,path2)
    lca = None
    min_len= len(path1)
    if len(path1)> len(path2):
        min_len=len(path2)
    for i in range(min_len):
        if path1[i] == path2[i]:
            lca = path1[i]
        else:
            break

    return lca
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Initialize an empty graph using defaultdict to store edges
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an undirected edge between nodes u and v
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start, end):
        # Check if start and end nodes are present in the graph
        if start not in self.graph or end not in self.graph:
            return None  # Nodes are not present in the graph

        visited = set()  # Set to keep track of visited nodes during traversal
        q = deque([(start, [])])  # Queue to store nodes and their paths

        while q:
            node, path = q.popleft()

            # Check if the current node is the destination
            if node == end:
                return path + [end]  # Return the shortest path

            # Explore neighbors if the current node hasn't been visited
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        # Enqueue the neighbor with the updated path
                        q.append((neighbor, path + [node]))

        return None  # No path found

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return TreeNode(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)

        return root

    def delete(self, value):
        # Call the private _delete method to perform deletion
        self.root = self._delete(self.root, value)

    def _delete(self, root, value):
        # Base case: If the root is None, the value is not present
        if root is None:
            return root

        # Recursive cases based on the comparison of values
        if value < root.value:
            # If the value is smaller, recursively delete in the left subtree
            root.left = self._delete(root.left, value)
        elif value > root.value:
            # If the value is larger, recursively delete in the right subtree
            root.right = self._delete(root.right, value)
        else:
            # Node with one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.value = self._min_value_node(root.right).value

            # Delete the inorder successor
            root.right = self._delete(root.right, root.value)

        # Return the modified root after deletion
        return root

    def _min_value_node(self, node):
        # Helper function to find the node with the minimum value in a subtree
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        # Call the private _search method to perform the search
        return self._search(self.root, value)

    def _search(self, root, value):
        # Base cases: If the root is None or the value is found
        if root is None or root.value == value:
            return root

        # Recursive cases based on the comparison of keys
        if value < root.value:
            # If the value is smaller, recursively search in the left subtree
            return self._search(root.left, value)
        return self._search(root.right, value)


if __name__ == '__main__':
# ---------------Q4--------------------
# Q4-1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)
    root.left.left.left = TreeNode(10)
    root.left.left.right = TreeNode(11)
    node1_value = 5
    node2_value = 11
    # Find the lowest common ancestor
    lca_value = find_lowest_common_ancestor(root, node1_value, node2_value)
    if lca_value is not None:
        print(f"The lowest common ancestor of nodes {node1_value} and {node2_value} is {lca_value}.")
    else:
        print(f"At least one of the nodes {node1_value} and {node2_value} is not present in the tree.")
#Q4-2
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.add_edge(4, 8)
    graph.add_edge(5, 8)
    graph.add_edge(6, 9)
    graph.add_edge(7, 9)
    # Find the shortest path between nodes 1 and 9
    start = 1
    end = 9
    result = graph.shortest_path(start, end)
    if result:
        print(f"The shortest path from node {start} to {end} is: {result}")
    else:
        print(f"There is no path from node {start} to {end}.")
# Q4-3
    bst = BinarySearchTree()
    # Insert elements
    elements_to_insert = [50, 45, 10, 40, 90, 70, 30]
    for element in elements_to_insert:
        bst.insert(element)
    # Search for an element
    search_key = 40
    search_result = bst.search(search_key)
    if search_result:
        print(f"{search_key} found in the tree.")
    else:
        print(f"{search_key} not found in the tree.")
    # Delete an element
    delete_key = 30
    bst.delete(delete_key)
    print(f"Deleted {delete_key} from the tree.")
    # Search for the deleted element
    deleted_search_result = bst.search(delete_key)
    if deleted_search_result:
        print(f"{delete_key} found in the tree.")
    else:
        print(f"{delete_key} not found in the tree.")

