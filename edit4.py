
import  numpy as np

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.flow import preflow_push
import osmnx as ox
import geopandas as gpd
import pandas as pd
import numpy as np
import time
import sys
from networkx.drawing.nx_pydot import read_dot
from networkx.drawing.nx_pydot import write_dot
from networkx.algorithms.community.label_propagation import label_propagation_communities
import csv


   
def plot_weighted_graph():
 
    
    G = nx.Graph() 
    num_of_node_list = int(input("What is num of design you needs ? "))
    node_list = []
    for i in range(num_of_node_list): 
        node_list.append(i)  
    #num_of_node_list = input("What is num of design you needs ? ")
  
   
    for node in node_list:
        G.add_node(node)

    pos=nx.circular_layout(G) 
    nx.draw_networkx_nodes(G,pos,node_color='blue',node_size=900)

    labels = {}
    for node_name in node_list:
        labels[int(node_name)] = int(node_name)
    nx.draw_networkx_labels(G,pos,labels,font_size=20)
 
    values=[1,2,3,4,5]
    dis = []
    all_weights = []
    all_bandwidth = []
    all_security = []
    all_delay = []
    all_speed = []
    all_throughput = []
    
    counter=0
    co = 0
    arr = []
    #num_of_nods = int(input("What is num of nood you needs ? "))
    #for i in range(num_of_nods): 
     #   arr.append(i) 
     
    a = len(node_list) 
    b = len(node_list) - 1
        
   # c = a * b
    #for i in range(c): 
     #   arr.append(c)
        
   
    for av in values:
        for se in values:
            for de in values:
                for sp in values:
                    for ba in values:
                        for th in values:
                            counter+=1
                            for n1 in range(b):
                                for n2 in range(b):
                                    G.add_edge(node_list[n1],node_list[n2],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                                    
                                    for (node1,node2,data) in G.edges(data=True):
                                        all_bandwidth.append(data['bandwidth'] )
                                        all_security.append(data['security'])
                                        all_weights.append(data['weight']) 
                                        all_delay.append(data['delay']) 
                                        all_speed.append(data['speed'])
                                        all_throughput.append(data['throughput'])
                            ####
                         
                            spl = dict(nx.all_pairs_shortest_path_length(G))
                            for node1 in spl:
                               for node2 in spl[node1]:
                                           x = spl.values()
                                           s = dis.append(x)
                                           l = len(dis)
                            trans = l / sum(all_bandwidth) 
                            Fiinal_speed = (sum(all_speed) +(l/sum(all_bandwidth)))+sum(all_speed)
                            pro_delay = Fiinal_speed / 2 
                            Fiinal_delay = trans + pro_delay
                            Fiinal_bandwidth = ( sum(all_weights) * Fiinal_delay ) / 2
                            Fiinal_avai = 2 * Fiinal_bandwidth * Fiinal_delay
                            Fiinal_thro = (sum(all_throughput) * Fiinal_bandwidth ) / 60
                            print("Fiinal_speed = ",Fiinal_speed)
                             #print("Fiinal_delay = ",Fiinal_delay)
                             #print("Fiinal_bandwidth = ",Fiinal_bandwidth)
                             #print("Fiinal_avai = ",Fiinal_avai)
                             #print("Fiinal_thro = ",Fiinal_thro)
                        """    
                        sec_arr = []
                        for i in range(100):
                                i = i + 1 
                                sec_arr.append(i)
                           
                        for x in sec_arr:
                                 s3 = sum(all_security)
                                 s4 = sum(sec_arr)
                                 Finsal_security = s3 * s4 
                                 
                             #print("Fiinal_security = ",Finsal_security) 
                            
                        BW = []
                            #if not all_bandwidth :
                    for i in all_bandwidth:
                          
                         spl = dict(nx.all_pairs_shortest_path_length(G))
                         for node1 in spl:
                            for node2 in spl[node1]:
                                        x = spl.values()
                                        s = dis.append(x)
                                        l = len(dis)
                         trans = l / sum(all_bandwidth) 
                         Fiinal_speed = (sum(all_speed) +(l/sum(all_bandwidth)))+sum(all_speed)
                         pro_delay = Fiinal_speed / 2 
                         Fiinal_delay = trans + pro_delay
                         Fiinal_bandwidth = ( sum(all_weights) * Fiinal_delay ) / 2
                         Fiinal_avai = 2 * Fiinal_bandwidth * Fiinal_delay
                         Fiinal_thro = (sum(all_throughput) * Fiinal_bandwidth ) / 60                       
                                
     
                       # print("Fiinal_bandwidth = ",Fiinal_bandwidth)
                       #  BW.append(Fiinal_bandwidth)
                         #BW.append(Fiinal_speed)
                         #BW.append(Fiinal_delay)
                         #BW.append(Fiinal_avai)
                         #BW.append(Fiinal_thro)
                         #BW.append(Finsal_security)
                    
                    #array = np.array([BW])
                    #newfile = np.savetxt("header.csv", np.dstack((np.arange(1, array.size+1),array))[0],"%d,%d",header=",ID,Values")
                    #print(newfile)     
                         
                                                                            
                    #persons=[('Lata',22,45),('Anil',21,56),('John',20,60)]
                    csvfile=open('BW.csv','w')
                    obj=csv.writer(csvfile)
                    #for i in all_bandwidth:
                          #obj.writerow(i)
                    obj.writerows(map(lambda x: [x], BW))
                    csvfile.close()
                    """
            
                                                   # print(counter)
                                    
                            #print(" The sum of all the weights =  ",sum(all_weights))
                                                                                        
                                                                                        
                         #   print(" The sum of all the bandwidth =  ",sum(all_bandwidth))
                                                                                
                          #  print(" The sum of all the security =  ",sum(all_security))
                           # print(" The sum of all the delay =  ",sum(all_delay))
                            #print(" The sum of all the speed =  ",sum(all_speed))
                            #print(" The sum of all the throughput =  ",sum(all_throughput))          
                            #print(counter)
       
            
            
        """    
        print("Fiinal_speed = ",Fiinal_speed)
        print("Fiinal_delay = ",Fiinal_delay)
        print("Fiinal_bandwidth = ",Fiinal_bandwidth)
        print("Fiinal_avai = ",Fiinal_avai)
        print("Fiinal_thro = ",Fiinal_thro)
        """
        
       
                                     
        unique_weights = list(set(all_weights))
        unique_bandwidth = list(set(all_bandwidth))
        unique_security = list(set(all_security))
        unique_delay = list(set(all_delay))
        unique_speed = list(set(all_speed))
        unique_throughput = list(set(all_throughput))
        
       
        
                                            
                                           
                                           # Create an 6 x 15625 matrix of 0's:
                                           #w, h = 6, counter;
                                           #MyMatrix = [ [0 for x in range( w )] for y in range( h ) ]  
                                           
                                           # Create an array of objects:
                                           #MyList = [ {} for x in range( 5) ]
                                           #print("lll=",len(MyMatrix))
                                           
                        #   unique_weights = list(set(all_weights))
                         #  unique_bandwidth = list(set(all_bandwidth))
                          # unique_security = list(set(all_security))
                           #unique_delay = list(set(all_delay))
                          # unique_speed = list(set(all_speed))
                          # unique_throughput = list(set(all_throughput))
                                        
                                 
                                                            
                          
                                          
                        #  print(counter)
  
                     #   for i in range(0, len(unique_weights)):

                      #      print(unique_weights[i])
              #          print("UU = ", list.__contains__(unique_))       
                              #  print("ccccc", c)
                        #spl = dict(nx.all_pairs_shortest_path_length(G))
                        #for node1 in spl:
                         #   for node2 in spl[node1]:
                          #             x = spl.values()
                           #            s = dis.append(x)
                            #           l = len(dis)
                           # print("sgt",l)
                            #lat = 2 * 1
                           # Fiinal_speed = (sum(all_speed) +(l/sum(all_bandwidth)))+sum(all_speed)
                            #trans = l / sum(all_bandwidth) 
                            #pro_delay = Fiinal_speed / 2 
                            #Fiinal_delay = trans + pro_delay
                            #Fiinal_bandwidth = ( sum(all_weights) * Fiinal_delay ) / 2
                            #Fiinal_avai = 2 * Fiinal_bandwidth * Fiinal_delay
                            #Fiinal_thro = (sum(all_throughput) * Fiinal_bandwidth ) / 60
                            #print("Fiinal_speed = ",Fiinal_speed)
                            #print("Fiinal_delay = ",Fiinal_delay)
                            #print("Fiinal_bandwidth = ",Fiinal_bandwidth)
                            #print("Fiinal_avai = ",Fiinal_avai)
                            #print("Fiinal_thro = ",Fiinal_thro)
                            #sec_arr = []
                            #for i in range(100):
                            #    i = i + 1 
                            #    sec_arr.append(i)
                          
                            #for x in sec_arr:
                             #   s3 = sum(all_security)
                              #  s4 = sum(sec_arr)
                               # Finsal_security = s3 * s4 
                                
                            #print("Fiinal_security = ",Finsal_security) 
                                
                              
   
        
        
            
            
            #end
            
            #------------throughput--------------------
          #  bandwidth = ( Avai * delay ) / 2
           # Avai = 2 * bandwidth * total_delay
            #lat = 2 * 1
          # rtt = (lat+(size/bandwidth))+lat
            #rtt = (lat+(l/bandwidth))+lat
             #  pro_delay = rtt / 2 # 
        
            
            
            #------------end---------------------------
        
        
        
                                            #plt.show() 
                    
                             
        
if __name__=='__main__':
      plot_weighted_graph()
       
    
    
