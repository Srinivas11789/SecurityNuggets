record = {}

"""
def recurse_all_nodes(node, stack):

    if node not in stack:
        stack.append(node)
        if node in record:
            stack.append(node)
            for child in record[node]:
                recurse_all_nodes(child, stack)

"""
def recurse_all_nodes(node, stack, leaf):

    if node in record and node not in stack:
        stack.append(node)
        for child in record[node]:
            recurse_all_nodes(child, stack, leaf)
    else:
        leaf.append(node)


def topo_graph_create(data):

    root = None
    
    # Format data and make the relation (Dictionary with before)
    for line in data:
        line = line.split(" ")
        
        if not root:
            root = line[1]

        if line[1] not in record:
            record[line[1]] = []
        record[line[1]].append(line[7])
        record[line[1]] = sorted(record[line[1]])

        """
        # Build a dictionary with before and after 
        if line[1] not in record:
            record[line[1]] = {}
            record[line[1]]["Before"] = [] 
            record[line[1]]["After"] = []
        record[line[1]]["After"].append(line[7])
        if line[7] not in record:
            record[line[7]] = {}
            record[line[7]]["Before"] = [] 
            record[line[7]]["After"] = []
        record[line[7]]["Before"].append(line[1])
        """
    # Construct a tree and perform inorder traversal except for the last leaf node
    # As of now lets apply this in dictionary!

    #print record
    stack = []
    leaf = []
    recurse_all_nodes(root, stack, leaf)
    stack.extend(sorted(set(leaf)))
    print "".join(stack)
    #return data


def main():
    # Fetch input from url
    import requests, sys
    # Sent the cookie set through the environment variable to get this
    #input = requests.get("https://adventofcode.com/2018/day/8/input")

    # Hard Coded inputs
    input = open("71.example","r").read()
    input = input.split("\n")
    topo_graph_create(input[:-1])
    #print "Day 3: Part 1 answer is --> " + str(count)
    #print "Day 3: Part 2 answer is --> " + id

main()
