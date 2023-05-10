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
    for i in range(1,1001):
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

    print(Tree[source].adjacent)
    print(dfs(source,Tree))

def dfs(source,Tree):
    s = []
    closest_leafs = []
    s.append(source + 1)
    depth = 0
    while s:
        v = s.pop()
        #print(v, " about to check this pls no out of bounds")
        if Tree[v-1].explored == 'W':
            print("New node discovered: ", v)
            Tree[v-1].explored = 'G'
            depth += 1
            print("we are going deeper: ", depth)
            for edge in Tree[v-1].adjacent:
                print(edge)
                s.append(edge[0])
                
            if(len(Tree[v-1].adjacent) == 1 and [edge[0], depth] not in closest_leafs):
                closest_leafs.append([edge[0], depth])
        else:
            print("skipping node ", v, " already explored.")
            depth -= 1
            print("arising from the ashes: ", depth)
    print("Closest leafs in order: ", closest_leafs)



def bestfs(source,Tree):
    Tree[source - 1].explored = 'G'
    queue = []
    queue.append(Tree[source-1])
    while queue:
        min = 2
        min_node = 0
        for node in queue:
            if(node.adjacent[1] < min):
                min = node.adjacent[1]
                min_node = node.adjacent[0]
        curr = min_node
        curr = queue.remove(curr)
        for node in Tree[curr[min_node].adjacent[0] - 1]:
            if node.explored != 'G':
                if node.adjacent[1] < min:
                    min = node.adjacent[1]
                else:
                    node.explored = 'G'
                    queue.append(node)

            





if __name__ == '__main__':
    main()