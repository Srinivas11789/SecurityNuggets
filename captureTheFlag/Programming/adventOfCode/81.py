# Arrangement:
# * We provide our own naming
# * Each node: 1st num of children
# *            2nd metadata size

# Part 1 --> sum of all the metadata

# Logic 1: Construct a dictionary
def traverse(data):
    stack = {}
    n = len(data)
    i = 0
    while i < n:
        element = stack[]
        if element.children == 0:
                element.metadata += data[i+1:i+1+n]
        stack.append(element)


# Logic 2: Stack Method
# * The metadata of A is after all the children metadata are filled. When there is heavy nesting a tree  mthod would require a depth first traversal either way to add the children and fill in the metadata values.
# Backward traversal is a little tough for tree. Going with stack logic
"""
class node:
    def __init__(children, metadata_size):
        self.children = children
        self.metadata = metadata_size
        self.metadata = ""

def traverse(data):
    stack = []
    n = len(data)
    i = 0
    while i < n:
        element = node(data[i], data[i+1])
        if element.children == 0:
                element.metadata += data[i+1:i+1+n]
        stack.append(element)
"""        

"""
# Logic 3: Construct a tree
class node:
    def __init__(children, metadata_size):
        # Integer num of children
        self.children = children
        # Integer size of metadata
        self.metadata = metadata_size
        # Metadata string
        self.metadata = ""

# Possible recursion function to iterate through the tree
def traverse(data):
    n = len(data)
    i = 0
    while i < n:
        current_node = node(data[i], data[i+1])
"""        
        
def main():
    # Fetch input from url
    import requests, sys
    # Sent the cookie set through the environment variable to get this
    #input = requests.get("https://adventofcode.com/2018/day/8/input")

    # Hard Coded inputs
    input = open("81.example","r").read()
    input = input.split("\n")[0].split(" ")
    print input

main()
