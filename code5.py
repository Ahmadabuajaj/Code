import random
from random import seed
import matplotlib.pyplot as plt
import networkx as nx
 
class Design:
    #numberOfEdges=5
    #definition of graph
    G = nx.Graph() 
    num_of_node_list = int(input("What is num of nodes you needs ? "))
    numberOfEdges = int(input("What is num of edges you needs ? "))

    node_list = []
    for i in range(num_of_node_list): 
        node_list.append(i)  
  
   
    for node in node_list:
        G.add_node(node)
        
     

      
  
    
    Edges = [[0 for x in range(6)] for y in range(numberOfEdges)] 
    FitnessValues = [6]
    # Speed
    # Delay
    # BW
    # Ava
    # Thro
    # Security
    
    #for requirement in range(5):
     #   for edge in range(numberOfEdges-1):
            
               #Edges[requirement][edge] = random.randint(1, 5)
               
               
               
               
    
 
    def __init__(self):
        self.numberOfEdges
        
    def fitnessValu(self):
        for requirement in range(5):
            self.FitnessValues[self.requirement] = 5 # eqation of speed 
    def print(self):
        for requirement in range(5):
            
            for edge in range(self.numberOfEdges-1):
                self.Edges[requirement][edge] = random.randint(1, 5)
                print(self.Edges[requirement][edge])
                        
            
#main program, how many nodes, edges

Designs = []

for d in range(10000):
    design = Design()
    Designs.append(design)

 
       


Designs[1].print()

print("----------------")
 
Designs[100].print()