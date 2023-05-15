import random
import heapq
  
# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V: int): # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]
  
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
  
    def shortestPath(self, src: int, chest_nodes : list):
        pq = []
        heapq.heappush(pq, (0, src))
        total_coins = 0
        chests_found = 0
        
        dist = [float('inf')] * self.V
        dist[src] = 0

        passes = 0
        while pq:
            d, u = heapq.heappop(pq)
  
            for chest, coins in chest_nodes:             
                if u == chest:
                    if chests_found == 0:
                        first_chest.append(passes)
                    print("Chest: ",u, " found")
                    total_coins += coins
                    chest_nodes.remove([u,coins])
                    chests_found += 1                 

            if(total_coins >= 200):
                break

            for v, weight in self.adj[u]:         
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
                passes += 1
  
        # for i in range(self.V): # for printing distances between source for all nodes
        #     pass
        #     #print(f"{i} \t\t {dist[i]}") 

        print("Total number of coins found: ", total_coins)
        print("Total number of chests found: ", chests_found)
        collected_chests_avg.append(chests_found)
        whole_tour.append(passes)
        avg_coins.append(total_coins)
  
def collect_treasure_chests():
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

    print("Chests to find: ", chest_nodes)

    src = random.randint(0,1000)
    print("Our source is: ", src)
    g.shortestPath(src, chest_nodes)

    print(chest_nodes)

if __name__ == "__main__":
    first_chest = [] # store how many passes it took to get to the first chest
    collected_chests_avg = [] # store the number of chests collected each time
    whole_tour = [] # store the total number of passes 
    avg_coins = []
    for graph in range(50):
        collect_treasure_chests()
    print("\n\n\n\n")
    print("First chest was found on average at the ", round(sum(first_chest) / len(first_chest),0)," pass")
    print("Number of chests collected on average is: ", round(sum(collected_chests_avg) / len(collected_chests_avg),0), " chests per graph")
    print("Average of the whole tour on average is: ", round(sum(whole_tour) / len(whole_tour),0), " passes")
    print("Average amount of coins found each graph: ", round(sum(avg_coins) / len(avg_coins),0), " coins")
