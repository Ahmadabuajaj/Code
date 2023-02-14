import random
#import numpy as np

import fileinput
from random import seed
import csv
class Design:
    
    nodes = []
    Edges = []
    sum_security = []
    sum_availability = []
    FitnessValues = []
    


    #numberOfNodes = int(input("enter"))
    
    def __init__(self,numberOfNodes):
        self.numberOfNodes = numberOfNodes # = 5
     
        filne = "/home/ahmad/Documents/GitHub/Code/nodes.txt"
        f = open(filne, 'r+')

        lines = f.readlines() 
        self.numberOfEdges = int(lines[1])

     
        self.Edges = [[0 for x in range(7)] for y in range(self.numberOfEdges)] 
        """
        for edge in range(self.numberOfEdges):
            self.Edges[0][edge] = random.randrange(1, 6)
            self.Edges[1][edge] = random.randrange(1, 6)
            self.Edges[2][edge] = random.randrange(1, 6)
            self.Edges[3][edge] = random.randrange(1, 6)
            self.Edges[4][edge] = random.randrange(1, 6) #ava
            self.Edges[5][edge] = random.randrange(1, 6) # sec
             """

        linesCounter = 2
        reqLines=0
        counter = 1

        


        filne = "/home/ahmad/Documents/GitHub/Code/req.txt"
        f2 = open(filne, 'r+')

        req = f2.readlines() 
        
        for edge in range(self.numberOfEdges):
            c= int(lines[linesCounter])
            self.Edges[edge][0] =  counter
            self.Edges[edge][1] = c  
            linesCounter = linesCounter + 1
            c= int(lines[linesCounter])
            linesCounter = linesCounter + 1
            self.Edges[edge][2] = c
            self.Edges[edge][3] = int(req[reqLines]) # Distance
            reqLines=reqLines+1
            self.Edges[edge][4] = int(req[reqLines]   ) # Bandwidth
            reqLines=reqLines+1
            counter = counter + 1
            self.Edges[edge][5] = random.randrange(1,6) # Availability
            self.Edges[edge][6] = random.randrange(1,6) # Security

        f.close()
        f2.close()



        #for x in self.Edges:
         #   print(x) 
    

    def fitness_Design(self):
                
        ##########################AVAILABILITY###########################

        SumOfAvailability = 0
        for edge in range(self.numberOfEdges):
            self.sum_availability.append ( self.Edges[edge][5] )

        for i in  self.sum_availability:
            SumOfAvailability += i
        #print(self.sum_availability)
        
        
            
        #print("SumOfAvailability = ", SumOfAvailability)
        
        ##########################SECURITY###############################
        SumOfSecurity = 0 
        for edge in range(self.numberOfEdges):
            self.sum_security.append ( self.Edges[edge][6] )

        for i in  self.sum_security:
            SumOfSecurity += i
        #print("SumOfSecurity = ", SumOfSecurity)



        """
        sum_dis = []

        SumOfdistances = 0
        for edge in range(numberOfEdges):
            sum_dis.append ( NodesEdges[edge][3] )

        for i in  sum_dis:
            SumOfdistances += i
        #print("SumOfdistances = ", SumOfdistances)

        sum_band = []
        SumOfbandwidth = 0
        for edge in range(numberOfEdges):
            sum_band.append ( NodesEdges[edge][4] )

        for i in  sum_band:
            SumOfbandwidth += i
        #print("SumOfbandwidth = ", SumOfbandwidth)

        """
    


        ##########################FITNESS_VAlues###########################


        filne = "/home/ahmad/Documents/GitHub/Code/AV_SE.txt"
        f3 = open(filne, 'r+')

        AV_SE = f3.readlines() 
        
         
        Weight = float(AV_SE[2])
        Weightt = float(AV_SE[3])
        #FitnessValue_Design =  SumOfdistances + SumOfbandwidth +  ( Weight * SumOfAvailability ) + ( Weightt * SumOfSecurity )

        FitnessValue_Design =    ( Weight * SumOfAvailability ) + ( Weightt * SumOfSecurity )
        print("FitnessValue_Design = ", abs(FitnessValue_Design - 36.0 )) 
        self.sum_availability.clear()
        self.sum_security.clear()
        f3.close()


       
        #print([requirement])

            
    def print(self):        
        for requirement in range(7):
         for edge in range(self.numberOfEdges):
                 print(self.Edges[edge][requirement])
                 
                 
    
        
        
       
            

filne = "/home/ahmad/Documents/GitHub/Code/nodes.txt"
f = open(filne, 'r+')

lines = f.readlines() 
#f.close()
numberOfNodes = int(lines[0])
numberOfEdges = int(lines[1])


filne = "/home/ahmad/Documents/GitHub/Code/req.txt"
f2 = open(filne, 'r+')

req = f2.readlines() 


NodesEdges = [[0 for x in range(numberOfNodes)] for y in range(numberOfEdges)]

Edges = [[0 for x in range(numberOfNodes) ] for y in range(numberOfEdges)]

linesCounter = 2
reqLines=0
counter = 1

for x in range(numberOfEdges):
    c= int(lines[linesCounter])
    NodesEdges[x][0] =  counter
    NodesEdges[x][1] = c  
    linesCounter = linesCounter + 1
    c= int(lines[linesCounter])
    linesCounter = linesCounter + 1
    NodesEdges[x][2] = c
    NodesEdges[x][3] = int(req[reqLines])
    reqLines=reqLines+1
    NodesEdges[x][4] = int(req[reqLines]   ) 
    reqLines=reqLines+1
    counter = counter + 1

for x in NodesEdges:
        print(x)


sum_dis = []

SumOfdistances = 0
for edge in range(numberOfEdges):
    sum_dis.append ( NodesEdges[edge][3] )

for i in  sum_dis:
    SumOfdistances += i
#print("SumOfdistances = ", SumOfdistances)

sum_band = []
SumOfbandwidth = 0
for edge in range(numberOfEdges):
    sum_band.append ( NodesEdges[edge][4] )

for i in  sum_band:
    SumOfbandwidth += i
#print("SumOfbandwidth = ", SumOfbandwidth)


    
filne = "/home/ahmad/Documents/GitHub/Code/AV_SE.txt"
f3 = open(filne, 'r+')

AV_SE = f3.readlines() 

Availability = int(AV_SE[0])
Security = int(AV_SE[1])
Weight = float(AV_SE[2])
Weightt = float(AV_SE[3])
FitnessValue_Network = SumOfdistances + SumOfbandwidth +  ( Weight * Availability ) + ( Weightt * Security )
#print("Distance ", Distance) 
#print("Bandwidth ", Bandwidth) 
#print("Availability ", Availability )
#print("Security ", Security )
#print("Weight = ", Weight )
print("FitnessValue_Network = ", FitnessValue_Network) 
f.close()
f2.close()
f3.close()


   
Designs = []

for d in range(1000):
    design = Design(numberOfNodes)
    Designs.append(design)
    


Designs[10].print()


print("--------------")

Designs[10].fitness_Design() 
#Designs[10].fitness_Design() 
#Designs[100].fitness_Design() 
#Designs[200].fitness_Design()
 

ArrayOfDesignsOf_fitness = []
ArrayOfDesignsOf_fitness = [[0 for x in range(2)] for y in range(10)]


"""
for i in range(10):
    ArrayOfDesignsOf_fitness.append(i)

for i in ArrayOfDesignsOf_fitness:
    ArrayOfDesignsOf_fitness.append(  Designs[i].fitness_Design()  )

for x  in ArrayOfDesignsOf_fitness:
    print(x)
"""