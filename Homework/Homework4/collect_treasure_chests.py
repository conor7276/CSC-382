import random
import heapq
  
# iPair ==> Integer Pair
iPair = tuple
  
# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V: int): # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]
  
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
  
    # Prints shortest paths from src to all other vertices
    def shortestPath(self, src: int, chest_nodes : list):
        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))
        total_coins = 0
        chests_found = 0
        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0
  
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)
  
            # 'i' is used to get all adjacent vertices of a
            # vertex
            for chest, coins in chest_nodes:
                
                if u == chest:
                    print("Chest: ",u, " found")
                    total_coins += coins
                    chest_nodes.remove([u,coins])
                    chests_found += 1

            if(total_coins >= 200):
                break
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
  
        # Print shortest distances stored in dist[]
        for i in range(self.V):
            pass
            #print(f"{i} \t\t {dist[i]}") 

        print("Total number of coins found: ", total_coins)
        print("Total number of chests found: ", chests_found)
  
# Driver's code
if __name__ == "__main__":
    # create the graph given in above figure
    V = 1000
    g = Graph(V)
    chest_nodes = [] # there can only be 10
    for node in range(V):
        chosen_node = node
        while(chosen_node == node): # choose first node
            chosen_node = random.randint(0,V-1)
        weight = random.randint(1,10)
        if ( len(chest_nodes) < 10):
            if(random.randint(0,1)):
                chest_nodes.append([node,random.randint(20,80)])
        g.addEdge(node,chosen_node,weight)
        #print("Adding: ", node, " ", chosen_node, " ", weight)
        while (1): # for connecting a random amount of nodes to each node
            if(random.randint(0,1)):
                chosen_node = node
                while(chosen_node == node):
                    chosen_node = random.randint(0,V-1)
                weight = random.randint(1,10)
                g.addEdge(node,chosen_node, weight)
                #print("Adding: ", node, " ", chosen_node, " ", weight)
            else:
                break

            

    # making above shown graph
    # g.addEdge(0, 1, 4, False, 20)
    # g.addEdge(0, 7, 8, False, 20)
    # g.addEdge(1, 2, 8, False, 20)
    # g.addEdge(1, 7, 11, False, 20)
    # g.addEdge(2, 3, 7, False, 20)
    # g.addEdge(2, 8, 2, False, 20)
    # g.addEdge(2, 5, 4, False, 20)
    # g.addEdge(3, 4, 9, False, 20)
    # g.addEdge(3, 5, 14, False, 20)
    # g.addEdge(4, 5, 10, False, 20)
    # g.addEdge(5, 6, 2, False, 20)
    # g.addEdge(6, 7, 1, False, 20)
    # g.addEdge(6, 8, 6, False, 20)
    # g.addEdge(7, 8, 7, False, 20)
    print("Chests to find: ", chest_nodes)

    src = random.randint(0,1000)
    print("Our source is: ", src)
    g.shortestPath(src, chest_nodes)

    print(chest_nodes)


























# import random
# class GraphNode:
#     def __init__(self, name : int, adjacent : list, explored : str, has_chest : bool, coins : int):
#         self.name = name
#         self.adjacent = adjacent # List[Tuple] Format: [[name, weight],[name, weight]]
#         self.explored = explored
#         self.has_chest = has_chest
#         self.coins = coins
#     def printNode(self):
#         print("Node: ", self.name, " ", self.adjacent, " ", self.explored, " ", self.has_chest, " ", self.coins)


# def random_coins(): # choose random number of coins if there is a chest
#     return random.randint(20,80)

# def random_chest(): # choose whether or not a node will have a chest
#     return random.randint(0,1)

# def random_weight(): # choose a random weight to connect two nodes
#     return random.uniform(0.01,1)

# def make_connection(): # choose whether or not to connect node with another node again after the first time
#     return random.randint(0,1)
    


# def main():
#     graph = [] # list of graph nodes
#     chest_count = 0
#     for i in range(0, 1000): #create a graph of 1000 nodes
#         node = GraphNode(i + 1 , [] ,'W', False , 0)
#         node.append(graph)
#         if len(graph) == 1: # can't append nodes if it's root
#             if(chest_count < 10):
#                 node[i].has_chest = random_chest()
#                 if(node[i].has_chest):
#                     node[i].coins = random_coins()
#         else:
#             if(chest_count < 10):
#                 node[i].has_chest = random_chest()
#                 if(node[i].has_chest):
#                     node[i].coins = random_coins()
            
                    


# if __name__ == '__main__':
#     main()