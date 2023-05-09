import random
class TreeNode:
   def __init__(self,name : int, adjacent : list):
       self.name = name
       self.adjacent = adjacent
       self.explored = 'W' # use this to traverse
   def printNode(self):
       print("Node: ", self.name, " ", self.adjacent, " ", self.explored)

def main():
    Tree = []
    for i in range(1,16):
        node = TreeNode(i,[])
        Tree.append(node)
        if len(Tree) == 1:
            pass
        else:
            rand_node = random.randint(0,len(Tree)-2)
            weight = round(random.uniform(0.01,1),2)
            Tree[rand_node].adjacent.append([i,weight])
            Tree[i-1].adjacent.append([rand_node + 1,weight])

    for node in range(len(Tree)):
        Tree[node].printNode()

    # targets = set({})
    # while len(targets) < 11:
    #     targets.add(random.randint(1,15))
    # targets = list(targets)
    # print(targets)
    while(1):
        source = random.randint(1,len(Tree)-1)
        if(len(Tree[source].adjacent) == 1):
            break
    #targets.remove(source)
    print(source + 1, " is a leaf node")
    #print(targets)
    # source = random.randint(0,len(Tree) - 1)
    # target1 = source
    # target2 = source
    # target3 = source
    # while(target1 == source):
    #     target1 = random.randint(0,len(Tree) - 1)
    
    # while(target2 == source and target2 != target1):
    #     target2 = random.randint(0,len(Tree) - 1)

    # while(target3 == source and target3 != target1 and target3 != target2):
    #     target3 = random.randint(0,len(Tree) - 1)

    # source = Tree[source]
    # target1 = Tree[target1]
    # target2 = Tree[target2]
    # target3 = Tree[target3]
    # print("Printing randomly selected nodes: ")
    # source.printNode()
    # target1.printNode()
    # target2.printNode()
    # target3.printNode()

    print(Tree[source].adjacent)
    #print(dfs(source,Tree))

def dfs(source,Tree):
    leaf_nodes = []
    depth = 0
    curr = source
    prev = 0
    def dfsHelper(curr,Tree,depth,leaf_nodes, prev, source):
        depth += 1
        # if(len(Tree[curr].adjacent) == 1 and Tree[curr].adjacent[0] == source):
        #     return
        for node in Tree[curr].adjacent:
            for point in range(len(Tree)):
                Tree[point].printNode()
            Tree[node[0]].printNode()
            #print("curr: ", curr + 1, " prev: ", prev + 1)
            #print(node[0])
            #print(type(node), " ", node)
            if Tree[node[0]].explored == 'W':
                Tree[node[0]].explored = 'G'
                leaf_nodes.append([node[0],node[1],depth])
                #print([node[0], node[1],depth])
                prev = curr
                
                dfsHelper(node[0] - 1,Tree,depth,leaf_nodes, prev,source)
        return
    
    dfsHelper(curr,Tree,depth,leaf_nodes, prev, source)
    return leaf_nodes
    


def bestfs():
    pass
        














if __name__ == "__main__":
    main()