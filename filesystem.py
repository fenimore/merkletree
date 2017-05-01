from merkel import MerkelTree

import os, sys, hashlib

def traverse_dir(filename):
    """get a list of children

    Returns empty list for leaf node
    """
    if os.path.isdir(filename):
        return [os.path.join(filename, x) for x in os.listdir(filename)]
    else:
        return []

def read_file(filename):
    """concatnate filename with file content for hash"""
    if os.path.isdir(filename):
        return filename.encode("utf-8")

    f = open(filename, "r+")
    content = filename + f.read()
    f.close()
    return content.encode("utf-8")

if __name__ == "__main__":
    print("Merkel Tree File System")
    assert len(sys.argv) != 1, "No dir argument"
    directory = sys.argv[1]
    mt = MerkelTree(directory, read_file, traverse_dir) # md5 default
    # mt.tree -> sorted breadth first by default
    merkel_tree = mt.bfs() #-> string repr of dfs tree

    # Using different traversals
    if len(mt.diff(merkel_tree)) != 0:
        print("This shouldn't show a difference")

    # Different hashes of same map
    md5_tree = MerkelTree(directory, read_file, traverse_dir, "md5")
    sha_tree = MerkelTree(directory, read_file, traverse_dir, "sha1")
    if len(md5_tree.diff(sha_tree)) == 0:
        print("These should not overlap")

    # print tree
    for n in merkel_tree:
        print(n)
