import random
#import numpy 
from collections import defaultdict
import fileinput
from random import seed
import copy
import csv,operator
import itertools
#import pandas as pd
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)



#r_mut = list(float_range(0, 1 , 0.1))

r_mut = 0.0
r_mut2 = 1
class Design:

    nodes = []
    Edges = []
    sum_security = []
    sum_availability = []
    FitnessValues = []

    #numberOfNodes = int(input("enter"))

    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes  # = 5

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
        reqLines = 0
        counter = 1

        filne = "/home/ahmad/Documents/GitHub/Code/req.txt"
        f2 = open(filne, 'r+')

        req = f2.readlines()

        for edge in range(self.numberOfEdges):
            c = int(lines[linesCounter])
            self.Edges[edge][0] = counter
            self.Edges[edge][1] = c
            linesCounter = linesCounter + 1
            c = int(lines[linesCounter])
            linesCounter = linesCounter + 1
            self.Edges[edge][2] = c
            self.Edges[edge][3] = int(req[reqLines])  # Distance
            reqLines = reqLines+1
            self.Edges[edge][4] = int(req[reqLines])  # Bandwidth
            reqLines = reqLines+1
            counter = counter + 1
            self.Edges[edge][5] = random.randrange(1, 6)  # Availability
            self.Edges[edge][6] = random.randrange(1, 6)  # Security
        f.close()
        f2.close()

        # for x in self.Edges:
        #   print(x)
    
    def fitness_Design(self):

        ##########################AVAILABILITY###########################

        SumOfAvailability = 0
        for edge in range(self.numberOfEdges):
            self.sum_availability.append(self.Edges[edge][5])

        for i in self.sum_availability:
            SumOfAvailability += i
        # print(self.sum_availability)

        #print("SumOfAvailability = ", SumOfAvailability)

        ##########################SECURITY###############################
        SumOfSecurity = 0
        for edge in range(self.numberOfEdges):
            self.sum_security.append(self.Edges[edge][6])

        for i in self.sum_security:
            SumOfSecurity += i
        #print("SumOfSecurity = ", SumOfSecurity)

        
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

        

        ##########################FITNESS_VAlues###########################

        filne = "/home/ahmad/Documents/GitHub/Code/AV_SE.txt"
        f3 = open(filne, 'r+')

        AV_SE = f3.readlines()

        Weight = float(AV_SE[2])
        Weightt = float(AV_SE[3])
        FitnessValue_Design = SumOfdistances + SumOfbandwidth + (Weight * SumOfAvailability) + (Weightt * SumOfSecurity)

        #FitnessValue_Design =    ( Weight * SumOfAvailability ) + ( Weightt * SumOfSecurity )
        #print("FitnessValue_Design = ", abs(FitnessValue_Design - 36.0 ))
        self.sum_availability.clear()
        self.sum_security.clear()
        return abs(FitnessValue_Design - 36.0)
        #print(  abs(FitnessValue_Design - 36.0) )

        f3.close()

        # print([requirement])

    def print(self):

        print(self.Edges)
                
    def __repr__(self):
        
        return f"Book:, {self.Edges}, {self.FitnessValue_Design}"
  
def tournament_selection(arrayOfdesigns , arr2):
    """
    new_fitnesses = []
    for i in range(499):
        if arrayOffitneses[i] < arrayOffitneses[i+1]:
        
            fitness_selection = random.choices(arrayOffitneses, k = 2 )
            if fitness_selection[0]  <  fitness_selection[1]  :
                
       
            

                print(fitness_selection)

    """ 
    #print("newBEF", new)
    cou = 1
    new = []    
    xarray = []      
    print("FIT-ONE = ", arrayOfdesigns[0]) 
    print("FIT-TWO = ", arrayOfdesigns[1])
    #Designs_selection = random.choices(arr2, k = 2 )
    #print("111",Fit(Designs_selection[0]))
    #print("222",Fit(Designs_selection[1]))
            

    for i in range(10000000):


        """
        if Fit(Designs_selection[0]) < arrayOfdesigns[0] and  Fit(Designs_selection[1]) < arrayOfdesigns[1]: 
                new  = Designs_selection[0]
                print("Fit(Designs_selection[0])",Fit(new))

        if  Fit(arr2[0]) < arrayOfdesigns[0] and  Fit(arr2[0]) < arrayOfdesigns[1]: 
                new  = Designs_selection[0]
                print("Fit(Designs_selection[0])",Fit(new))
                """
        Designs = random.choices(arr2, k = 4 )
        
        Designs_selection = random.choices(Designs, k = 2 )

        if Fit(Designs[0]) < Fit(Designs[1]):
            Designs_selection[0] = Designs[0]

        else: 
             Designs_selection[0] = Designs[1]

        if Fit(Designs[2]) < Fit(Designs[3]):
            Designs_selection[1] = Designs[2]

        else: 
            Designs_selection[1] = Designs[3]


        p1 = Designs_selection[0]
        #print("p1",p1)
        p2 = Designs_selection[1]
        #print("p2",p2)
        z = corssover_selection( p1 , p2  )
        #print("z",z)
        #print("-1]" , arrayOfdesigns[-1])
        if z < arrayOfdesigns[-1]: 
            arrayOfdesigns[-1]  = z
    print("Fitness_After_Xover = ",arrayOfdesigns[-1])

    
        
        
      
        

"""
    for i in range(100000):
        Designs_selection = random.choices(arrayOfdesigns, k = 2 )

            #print("bef",arrayOfdesigns[i][1])   
            #print( "--------------------------------------------------------" )
            #if  Designs_selection[0][1]  <  Designs_selection[1][1] and Designs_selection[0][1]  !=  Designs_selection[1][1]:
                #new.append(Designs_selection[0][1])
        
        if  Designs_selection[0] < arrayOfdesigns[0]   :
                 arrayOfdesigns[0] = Designs_selection[0]
                 print( "fAf0", arrayOfdesigns[0])
        if  Designs_selection[1] <  arrayOfdesigns[1]  :
             arrayOfdesigns[1] =  Designs_selection[1]
             print( "fAf1", arrayOfdesigns[1] )        
                



        

   
        #else:  Designs_selection = random.choices(arrayOfdesigns, k = 2 )
        
        if  Designs_selection[1][1]  < Designs_selection[0][1]:
            arrayOfdesigns[i][1] = Designs_selection[1][1]
            if arrayOfdesigns[i][1] < Designs_selection[1][1]:
                 print("less")
            else: arrayOfdesigns[i][1] = Designs_selection[1][1]
       # else:     Designs_selection = random.choices(arrayOfdesigns, k = 2 )
        
        #print("after",arrayOfdesigns[i][1])   
        #dict = {}
        
       
       # dict[0] = Designs_selection[0] 
        #dict[1] = Designs_selection[1]
        #p1 = Designs_selection[0]
        #p2 = Designs_selection[1]
        
        dict[2] = Fit(dict[0])
        dict[3] = Fit(dict[1])
        if dict[2] < dict[3] :
            Designs_selection.append(dict[2])
        if dict[3] < dict[2] :
            Designs_selection.append(dict[3])
            

    #print( dict)
    #print (sorted(new))  
   
"""
             
    
    #print( "____________" )
    
    


def corssover_selection(  arr1  , arr2):
    Fitness_Xover = 0
    arr3 = []
    arr4 = []
    length = len(arr1)
    length = len(arr2)
    middle_index = length // 2
    middle_index2 = length //2
    

    first_half = arr1[:middle_index]
    second_half = arr1[middle_index2:]

    third_half = arr2[:middle_index2]
    fourd_half = arr2[middle_index2:]
    

    #print("first_half",first_half)
    #print("second_half",second_half)

    #print("=============")

    #print(third_half)
    #print(fourd_half)
    arr3.append(first_half + fourd_half)

    for i in arr3:
     Fitness_Xover = Fit(i)
    #print(arr3)
    dict1 = {}
    dict1[0] = arr3
    dict1[1] = Fitness_Xover
    mutation(arr3, Fitness_Xover )

    return Fitness_Xover 
    
"""
def mutation(bitstring, FITNEE ,r_mut):
    
    for i in range(len(bitstring)):
    # check for a mutation

        if  FITNEE < r_mut:
        # flip the bit
             print("before",bitstring[i])  
             bitstring[i] =  1 - bitstring[i][i]
             print("after",bitstring[i])  

"""
def convert_2D_1D(array1):
    new_list = []
    new2 = []
    for i in array1:
        for j in i:
            new_list.append(j)
    for i in new_list:
            for j in i:
                new2.append(j)
    return new2



def mutation(array2 , Fitness_Xover):
    new_array = convert_2D_1D(array2)
   
  # Get index of individual to modify
    index = random.randint(0,42)

    # Convert individual to list so that can be modified
    individual_mod = list(new_array)

    if Fitness_Xover <= r_mut or x <= r_mut2:      
        individual_mod[index] = 1 - individual_mod[index]
        print("2nms",new_array)


    
    # Convert indivudal to tuple
    #individual = tuple(individual_mod)

    #print( individual )
        



def Fit(arr):

    sum_dis = []

    SumOfdistances = 0
    for edge in range(numberOfEdges):
        sum_dis.append(arr[edge][3])

    for i in sum_dis:
        SumOfdistances += i
    #print("SumOfdistances = ", SumOfdistances)

    sum_band = []
    SumOfbandwidth = 0
    for edge in range(numberOfEdges):
        sum_band.append(arr[edge][4])

    for i in sum_band:
        SumOfbandwidth += i
    #print("SumOfbandwidth = ", SumOfbandwidth)
    
    
    SumOfAvailability = 0
    sum_availability = []
    for edge in range(numberOfEdges):
        sum_availability.append(arr[edge][5])

    for i in sum_availability:
         SumOfAvailability += i

    SumOfSecurity = 0
    sum_security = []
    for edge in range(numberOfEdges):
            sum_security.append(arr[edge][6])

    for i in sum_security:
            SumOfSecurity += i


    FitnessValue_Design = SumOfdistances + SumOfbandwidth + (Weight * SumOfAvailability) + (Weightt * SumOfSecurity)
    return abs(FitnessValue_Design - 36.0) 
    sum_availability.clear()
    sum_security.clear()
    sum_band.clear()
    sum_dis.clear()


def pso(swarm, max_iter, n):
    
        for i in range(max_iter):
            best_swarm_fitnessVal = swarm[0] # swarm best

            for i in range(n): 
                if swarm[i] < best_swarm_fitnessVal:
                    best_swarm_fitnessVal = swarm[i]
                    #best_swarm_pos = best_swarm_fitnessVal

            
            return  print(" best fitness = %.3f" % best_swarm_fitnessVal)
        


filne = "/home/ahmad/Documents/GitHub/Code/nodes.txt"
f = open(filne, 'r+')

lines = f.readlines()
# f.close()
numberOfNodes = int(lines[0])
numberOfEdges = int(lines[1])


filne = "/home/ahmad/Documents/GitHub/Code/req.txt"
f2 = open(filne, 'r+')

req = f2.readlines()


NodesEdges = [[0 for x in range(numberOfNodes)] for y in range(numberOfEdges)]

Edges = [[0 for x in range(numberOfNodes)] for y in range(numberOfEdges)]

linesCounter = 2
reqLines = 0
counter = 1

for x in range(numberOfEdges):
    c = int(lines[linesCounter])
    NodesEdges[x][0] = counter
    NodesEdges[x][1] = c
    linesCounter = linesCounter + 1
    c = int(lines[linesCounter])
    linesCounter = linesCounter + 1
    NodesEdges[x][2] = c
    NodesEdges[x][3] = int(req[reqLines])
    reqLines = reqLines+1
    NodesEdges[x][4] = int(req[reqLines])
    reqLines = reqLines+1
    counter = counter + 1

for x in NodesEdges:
    print(x)


sum_dis = []

SumOfdistances = 0
for edge in range(numberOfEdges):
    sum_dis.append(NodesEdges[edge][3])

for i in sum_dis:
    SumOfdistances += i
#print("SumOfdistances = ", SumOfdistances)

sum_band = []
SumOfbandwidth = 0
for edge in range(numberOfEdges):
    sum_band.append(NodesEdges[edge][4])

for i in sum_band:
    SumOfbandwidth += i
#print("SumOfbandwidth = ", SumOfbandwidth)

filne = "/home/ahmad/Documents/GitHub/Code/AV_SE.txt"
f3 = open(filne, 'r+')

AV_SE = f3.readlines()

Availability = int(AV_SE[0])
Security = int(AV_SE[1])
Weight = float(AV_SE[2])
Weightt = float(AV_SE[3])
FitnessValue_Network = SumOfdistances + SumOfbandwidth +  (Weight * Availability) + (Weightt * Security)
print("FitnessValue_Network = ", FitnessValue_Network)
f.close()
f2.close()
f3.close()


Designs = []

for d in range(100000):
    design = Design(numberOfNodes)
    Designs.append(design)


# Designs[10].print()
#Designs[10].fitness_Design()
# print("--------------")
# Designs[100].fitness_Design()
# Designs[100].fitness_Design()
# print("--------------")


ArrayOfDesignsOf_fitness = []
#ArrayOf_fitness= [10][2]
#ArrayOf_fitness = [[0 for x in range(10)] for y in range(5)]

arrfit = [[0 for x in range(2)] for y in range(1000)]
ArrayOf_fitness =[]
newar = []

co = 1
armin = []

for f in range(1000):
    #print("Design:", x)
    x = random.randrange(0, 10000)

    
    
    ArrayOfDesignsOf_fitness.append(Designs[x].Edges)

    #ArrayOfDesignsOf_fitness.append(Fit(Designs[x].Edges))
    #print("Design:", x)
    arrfit[f][0]= Designs[x].Edges
    arrfit[f][1]= Designs[x].fitness_Design()
    ArrayOf_fitness.append( arrfit[f][1])
#sorted(ArrayOfDesignsOf_fitness)
    newar.append(Designs[x].fitness_Design())


    #print("Design:", x)
with open('arrfitdes.csv', mode='w') as csv_file:
    fieldnames = ['Design' , 'fitness_value', 'sorted_fitness' ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    ArrayOf_fitness.sort()

    
    writer.writeheader()
    for i in range(1000):


        writer.writerow({'Design':arrfit[i][0] , 'fitness_value':arrfit[i][1] , 'sorted_fitness': ArrayOf_fitness[i] })




"""with open('/home/ahmad/Documents/GitHub/GPC/arrfitdes.csv', "r") as csvfile:
    data = csv.reader(csvfile)
    minVal, maxVal = [], []
    
    for i in data:
        minVal.append([i][1])

print( min(minVal) )
"""
    #print(arrfit[f][1].sort())

#print(arrfit)
#print("beeeeee",ArrayOf_fitness)

    

"""
coun = 0
coun2 = 1
soarr = []
for s in range(500):
   
    a1 = arrfit[coun][1] #     
    a2 = arrfit[coun2][1] #        
    coun = coun2 + 1  #   
    coun2 = coun +1    # 

    if a1 < a2:
        
    
        print("a1 ",a1 )
        print("a2 ",a2 )
 """



    #if a1 < a2 and a1 != a2:
       
print("--------------")


#print(ArrayOfDesignsOf_fitness)
#ArrayOf_fitness.sort()


tournament_selection(ArrayOf_fitness , ArrayOfDesignsOf_fitness)

print("------ttt--------")


Des = newar
#fitness = ArrayOf_fitness


num_particles = 1000
max_iter = 10000000

print("Setting num_particles = " + str(num_particles))
print("Setting max_iter = " + str(max_iter))
print("\nStarting PSO algorithm\n")



best_position = pso(Des, max_iter, num_particles)

print("\nPSO completed\n")
print("\nBest solution found:")
#print(["%.6f"%best_position[k] for k in range(Des)])
#print("fitness of best solution = %.6f" % fitnessVal)

print("\nEnd particle swarm for sphere function\n")






