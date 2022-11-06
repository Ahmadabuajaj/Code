import random
from random import seed

class Design:
    #definition of graph
    
    nodes = []
    
    Edges = []
    FitnessValues =[6]
    #numberOfNodes = int(input("enter"))
    
    def __init__(self,numberOfNodes):
        self.numberOfNodes = numberOfNodes # = 5
       # print("mm",self.numberOfNodes)
        self.numberOfEdges = (int)(self.numberOfNodes*(self.numberOfNodes-1)/2) # = 10
        #print(self.numberOfEdges)
        #nodes = [[0 for x in range(self.numberOfNodes)] for y in range(2)]
       # lines = self.numberOfEdges
        self.Edges = [[0 for x in range(self.numberOfEdges)] for y in range(6)] # 10 col 6 rows
        for requirement in range(5):
            for edge in range(self.numberOfEdges-1):
              #  self.Edges[requirement][edge] = random.randint(1, 5)
                self.Edges[0][edge] = random.randrange(1, 6)
                self.Edges[1][edge] = random.randrange(1, 6)
                self.Edges[2][edge] = random.randrange(1, 6)
                self.Edges[3][edge] = random.randrange(1, 6)
                self.Edges[4][edge] = random.randrange(1, 6)
                self.Edges[5][edge] = random.randrange(1, 5)
       
        #print([requirement])
    
    
    
    
    def fitnessValu(self):
        for requirement in range(5):
            self.FitnessValues[requirement] = 5 # eqation of speed 
    def print(self):
        #print( (self.numberOfEdges) )
        
        for requirement in range(5):
         for edge in range(self.numberOfEdges-1):
#                print( "d;,;",(requirement) )
               
                 print(self.Edges[requirement][edge])
                
        """
             def print(self):
                 for requirement in range(5):
                     
                     for edge in range(self.numberOfEdges-1):
                         self.Edges[requirement][edge] = random.randint(1, 5)
                         
                         print(self.Edges[requirement][edge])
                         #print("e",self.Edges)
                        """
            
#main program, how many nodes, edges

Designs = []

for d in range(1000):
    design = Design(5)
    Designs.append(design)
  

Designs[3].print()
print("--------------")
#Designs[100].print()