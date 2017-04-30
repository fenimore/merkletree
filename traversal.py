from collections import deque

# Tree traversal algorithms returning
# all children from a given root node.
### Functions for traversing a MerkelTree in which
### you input a root or head Node and it returns
### a list of a Node and all its children.
### Nodes have these values:
###    v = value producing the hash digest
###    c = list of children Nodes
###    h = hash value calculated recursively with _hash()

# Breadth First
def bf_search(node):
    """Visit all nodes in breadth first order"""
    result = []
    q = deque()
    q.append(node)
    while len(q) != 0:
        n = q.pop()
        q.extend(n.c)
        result.append(n)
    return result

# Depth First
def df_search(node):
    """Visit all nodes in depth first order"""
    return descend(node, [])

def descend(root, tree):
    """Recursively descend tree until all nodes are visited"""
    tree.append(root)
    if len(root.c) < 1:
        return tree # leaf node
    for c in root.c:
        tree = descend(c, tree)
    return tree
