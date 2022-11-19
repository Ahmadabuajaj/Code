import random
from random import seed
import csv
class Design:
    #definition of graph
    
    nodes = []
    
    Edges = []
    FitnessValues = []
    for i in range(6):
        FitnessValues.append(i)
    #numberOfNodes = int(input("enter"))
    
    def __init__(self,numberOfNodes):
        self.numberOfNodes = numberOfNodes # = 5
       # print("mm",self.numberOfNodes)
        self.numberOfEdges = (int)(self.numberOfNodes*(self.numberOfNodes-1)/2) # = 10
        #print(self.numberOfEdges)
        #nodes = [[0 for x in range(self.numberOfNodes)] for y in range(2)]
       # lines = self.numberOfEdges
        self.Edges = [[0 for x in range(self.numberOfEdges)] for y in range(6)] # 10 col 6 rows
        
        for edge in range(self.numberOfEdges-1):
              #  self.Edges[requirement][edge] = random.randint(1, 5)
            self.Edges[0][edge] = random.randrange(1, 6)
            self.Edges[1][edge] = random.randrange(1, 6)
            self.Edges[2][edge] = random.randrange(1, 6)
            self.Edges[3][edge] = random.randrange(1, 6)
            self.Edges[4][edge] = random.randrange(1, 6)
            self.Edges[5][edge] = random.randrange(1, 6)
       
        #print([requirement])

            
    def print(self):
        #print( (self.numberOfEdges) )
        
        for requirement in range(5):
         for edge in range(self.numberOfEdges-1):
#                print( "d;,;",(requirement) )
                 print(self.Edges[requirement][edge])
                 
    # def fitnessValues():
        
        
       
            
#main program, how many nodes, edges
#for requirement in range(6):
    #  self.FitnessValues[requirement] = 5 # eqation of speed

numberOfNodes = int(input("Enter Number of Nodes:"))
numberOfEdges = (int)(numberOfNodes*(numberOfNodes-1)/2)


Edges = [[0 for x in range(4) ] for y in range(numberOfEdges)]

for x in range(numberOfEdges):
    Edges[x][0] =  int(input("Enter node 0: "))
    Edges[x][1] =  int(input("Enter node 1: "))
    Edges[x][2] =  int(input("Enter distance: "))
    Edges[x][3] =  int(input("Enter Bandwidth: "))
    #Edges[x][4] =  int(input("Enter Availability :"))
    #Edges[x][5] =  int(input("Enter Security:"))
    

av_sec = []
for i in range(1):
    avai = int(input("Enter Number of Availability :"))
    Sec = int(input("Enter Number of Security: "))
    av_sec.append(avai)
    av_sec.append(Sec)



    
print("The Ava = ",av_sec[0]  )
print("The Sec = ",av_sec[1]  )      
""" 
DY = int(input("Enter Delay:"))
SP = int(input("Enter Speed:"))
       
FitnessValues = []
for i in range(6):
    FitnessValues.append(i)
FitnessValues[0] =  DY # eqation of Delay 
FitnessValues[1] = 5
FitnessValues[2] = SY
FitnessValues[3] =  ((numberOfNodes * BW)/60) # th
FitnessValues[4] = BW * numberOfNodes # speed
FitnessValues[5] =   BW / (BW + DY)# eqation of ava 

#for i in Edges:
 #   FitnessValues = 5
""" 
    
csvfile=open('arr.csv','w')
obj=csv.writer(csvfile)
for i in range(1):
      obj.writerow(Edges)
#obj.writerows(map(lambda x: [x], FitnessValues))
csvfile.close()
with open('arr.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

        
        


   
Designs = []

for d in range(1000):
    design = Design(5)
    Designs.append(design)
    


print("--------------")
#Designs[100].print()

#Designs[3].fitnessValues()
  

#Designs[3].print()