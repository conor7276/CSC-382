#Viterbi algorithm
import random
class Node:
    top_to_top = 0
    top_to_bottom = 0
    bottom_to_top = 0
    bottom_to_bottom = 0
    def __init__(self, ttt, ttb, btt, btb) -> None:
        self.top_to_top = ttt
        self.top_to_bottom = ttb
        self.bottom_to_top = btt
        self.bottom_to_bottom = btb

    
class Viterbi:
    points = [] # List[Node]
    def __init__(self,size):
        self.points = Viterbi.generate_random_array(self,size)

    def generate_random_array(self,arr_size):
        arr = [] # generate array size of 100 with distances being from 1-10
        for _ in range(arr_size):
            arr.append(Node(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)))
        return arr
    def print_points(self,points):
        for node in points:
            print("*---", node.top_to_top,"---*")
            # print(" \\        /")
            print(" \\      /")
            print("  \\    /")
            print("   \\ ",node.bottom_to_top)
            print("    \\/")
            print("    /\\  ")
            print("   / ",node.top_to_bottom)
            print("  /    \\")
            print(" /      \\")
            #print(" /        \\")
            print("*---", node.bottom_to_bottom,"---*")

    def shortest_path(self, points):
        directions = [] # keep track of directions
        total_distance = 0
        location = "" 
        # location is needed so we know which nodes to compare
        
        for node in points:
            if(location == 'top'):
                if(node.top_to_top < node.top_to_bottom):
                    directions.append(node.top_to_top)
                    total_distance += node.top_to_top
                else:
                    directions.append(node.top_to_bottom)
                    total_distance == node.top_to_bottom
                    location = 'bottom'
            elif(location == 'bottom'):
                if(node.bottom_to_bottom < node.bottom_to_top):
                    directions.append(node.bottom_to_bottom)
                    total_distance += node.bottom_to_bottom
                else:
                    directions.append(node.bottom_to_top)
                    total_distance == node.bottom_to_top
                    location = 'top'
            else:
                if(node.top_to_top == min(node.top_to_top,node.top_to_bottom, node.bottom_to_top, node.bottom_to_bottom)):
                    location = 'top'
                    directions.append(node.top_to_top)
                    total_distance += node.top_to_top
                elif(node.top_to_bottom == min(node.top_to_top,node.top_to_bottom, node.bottom_to_top, node.bottom_to_bottom)):
                    location = 'top'
                    directions.append(node.top_to_bottom)
                    total_distance += node.top_to_bottom
                if(node.bottom_to_top == min(node.top_to_top,node.top_to_bottom, node.bottom_to_top, node.bottom_to_bottom)):
                    location = 'bottom'
                    directions.append(node.bottom_to_top)
                    total_distance += node.bottom_to_top
                if(node.bottom_to_bottom == min(node.top_to_top,node.top_to_bottom, node.bottom_to_top, node.bottom_to_bottom)):
                    location = 'bottom'
                    directions.append(node.bottom_to_bottom)
                    total_distance += node.bottom_to_bottom   

        print(directions)
        print(total_distance)

graph = Viterbi(100)
#graph.print_points(graph.points)
graph.shortest_path(graph.points)
#graph.print_points_cool(graph.points)
