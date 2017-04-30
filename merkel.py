import hashlib

from traversal import bf_search, df_search

class MerkelTree(object):
    """
    Create a Merkel Tree from root Node.

    Functions which derive value from an input and
    a possible list of children from that same value
    allows any kind of "Node", as long as it can be
    represented by bytes.

    The filesystem.py file gives an example of a
    filesystem (duh) Merkel Tree, which includes
    :func: `read_file` returns file contents from a path
    :func: `traverse_dir` returns sub directories of path

    :Parameters
    root: the value of root node
    get_val func: Node -> the value of a Node (ex. read_file)
    get_child func: Node -> enumerate Node's children
    hasher: string selector for a hashlib function def md5
    """

    def __init__(self, root, get_val, get_child,
                 hasher="md5"):
        self.root = root
        self.head = Node(root, get_val, get_child, hasher)
        self.tree = self.bfs() # list of nodes in bfs order

    def __str__(self):
        return "HEAD %s: %s" % (self.h, self.head.root)

    def print_tree(self):
        result = ""
        for child in self.tree:
            result += "%s: %s" % (child.h, child.v)
            result += "\n"
        result += "\n\n"
        return result

    # TODO: search

    def traverse(self, traversal):
        """Pass in func for traversing graph from root"""
        return traversal(self.head)

    def dfs(self):
        return df_search(self.head)

    def bfs(self):
        return bf_search(self.head)

    def diff(self, other):
        a = set(self.tree)
        if not isinstance(other, list):
            b = set(other.tree)
        else:
            b = set(other)
        # Uncomment to get diff of /both/ trees
        # return list(a.symmetric_difference(b))
        return a - b


class Node(object):
    """
    Merkel tree, the value of a node is used to both
    get the children and the hash value of a node.

    Parameters:
    value: root value to be stored in MerkelTree.
    get_hash func: value -> digest from leaf node.
    get_child func: value -> list of node children.
    hash_func: string selecting hash function. TODO

    Attributes:
    v = value producing the hash digest
    c = list of children Nodes
    h = hash value calculated recursively with _hash()
    """

    def __init__(self, value, get_val, get_child,
                 hash_func, verbose=False):
        self.v = value
        self.c = []
        self.hash_func = hash_func
        self.h = self._hash(value, get_val, get_child)
        if verbose:
            print(self.__str__())


    def __repr__(self):
        return "%s | %s" % (self.h, self.v)

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
                getattr(other, 'h') == self.h)

    def __hash__(self):
        return hash(self.h)

    def _hash(self, value, get_val, get_child):
        """Return the hash of a node and its children.

        get_hash -> returns a hash of the value,
                    only called on leaf nodes
        get_child -> return list of children Nodes
                     derived from the value
        """
        hasher = getattr(hashlib, self.hash_func)
        children = get_child(value)

        # If leaf node
        if len(children) < 1:
            return hasher(get_val(value)).hexdigest()

        h = hasher()
        for child in children:
            # Tree is created recursively
            n = Node(child, get_val, get_child,
                     self.hash_func)
            self.c.append(n)
            h.update(n.h.encode("utf-8"))
        return h.hexdigest()
