import random
class TreeNode:
   def __init__(self,name : int, adjacent : list):
       self.name = name
       self.adjacent = adjacent
   def printNode(self):
       print("Node: ", self.name, " ", self.adjacent)

def main():
    Tree = []
    for i in range(1,11):
        node = TreeNode(i,[])
        Tree.append(node)
        if len(Tree) == 1:
            pass
        else:
            rand_node = random.randint(0,len(Tree)-2)
            weight = round(random.uniform(0,1),2)
            Tree[rand_node].adjacent.append([i,weight])
            Tree[i-1].adjacent.append([rand_node + 1,weight])

    for node in range(len(Tree)):
        Tree[node].printNode()

    source = random.randint(0,len(Tree) - 1)
    target1 = source
    target2 = source
    target3 = source
    while(target1 == source):
        target1 = random.randint(0,len(Tree) - 1)
    
    while(target2 == source and target2 != target1):
        target2 = random.randint(0,len(Tree) - 1)

    while(target3 == source and target3 != target1 and target3 != target2):
        target3 = random.randint(0,len(Tree) - 1)

    source = Tree[source]
    target1 = Tree[target1]
    target2 = Tree[target2]
    target3 = Tree[target3]
    print("Printing randomly selected nodes: ")
    source.printNode()
    target1.printNode()
    target2.printNode()
    target3.printNode()

    
    

def dfs():
    pass

def bestfs():
    pass
        














if __name__ == "__main__":
    main()