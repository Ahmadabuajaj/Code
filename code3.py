
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


def ban_cal():
   # c = 2 * b * d
 #  b = ( c * d ) / 2
 print("bb")
 

def ava_cal():
    
   #  pro_delay = rtt / 2
    # ava = 2 * bandwidth * pro_delay
 
     print("av")

def sec_cal():
    for i in range[0:4]:
    #  s = sum(w*s)

        print("ss")

def thr_cal():

    lat = 2 * 1
   # rtt = (lat+(size/bandwidth))+lat
 #  rtt = (lat+(len()/bandwidth))+lat
   
    
    print("th")




   
def plot_weighted_graph():
 
    
    G = nx.Graph() 
    node_list = ['A','B','C','D']
    for node in node_list:
        G.add_node(node)

    pos=nx.circular_layout(G) 
    nx.draw_networkx_nodes(G,pos,node_color='blue',node_size=900)

    labels = {}
    for node_name in node_list:
        labels[str(node_name)] =str(node_name)
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
    
    for av in values:
        for se in values:
            for de in values:
                for sp in values:
                    for ba in values:
                        for th in values:
                            
                            G.add_edge(node_list[0],node_list[1],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[0],node_list[2],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[0],node_list[3],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[1],node_list[2],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[1],node_list[3],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[2],node_list[3],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[3],node_list[3],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            counter+=1
                            for (node1,node2,data) in G.edges(data=True):
                                        all_bandwidth.append(data['bandwidth'] )
                                        all_security.append(data['security'])
                                        all_weights.append(data['weight']) 
                                        all_delay.append(data['delay']) 
                                        all_speed.append(data['speed'])
                                        all_throughput.append(data['throughput'])
                 
                                
                        unique_weights = list(set(all_weights))
                        unique_bandwidth = list(set(all_bandwidth))
                        unique_security = list(set(all_security))
                        unique_delay = list(set(all_delay))
                        unique_speed = list(set(all_speed))
                        unique_throughput = list(set(all_throughput))
                      
                   
                     
                      
                             #  print("Length between", node1, "and", node2, "is", spl[node1][node2])
                    
                   
                        """
      
                                       
                                counter+=1
                                print(counter)
                                  #  print(len(G.degree))
                                     
                                  
        
                                    all_weights = []
                                    all_bandwidth = []
                                    all_security = []
                                    all_delay = []
                                    all_speed = []
                                    all_throughput = []
                                
                                    set_w = []
                                    
                                   
                                    for (node1,node2,data) in G.edges(data=True):
                                                all_bandwidth.append(data['bandwidth'] )
                                                all_security.append(data['security'])
                                                all_weights.append(data['weight']) 
                                                all_delay.append(data['delay']) 
                                                all_speed.append(data['speed'])
                                                all_throughput.append(data['throughput'])
                                        
                                
                                                unique_weights = list(set(all_weights))
                                                unique_bandwidth = list(set(all_bandwidth))
                                                unique_security = list(set(all_security))
                                                unique_delay = list(set(all_delay))
                                                unique_speed = list(set(all_speed))
                                                unique_throughput = list(set(all_throughput))
                                                spl = dict(nx.all_pairs_shortest_path_length(G))
                                            
                                                """
                                           
        
                      #    unique_bandwidth.append(all_bandwidth)
                       #   unique_bandwidth.append(all_security)
                        #  unique_bandwidth.append(all_weights)
                         # ubue_bandwidth.append(all_speed)
                          #unique_bandwidth.append(all_delay)
                                                 
                                               
                                            #    for (node1,node2) in values:
                                             #      set_w.append(all_bandwidth)
                                                    #set_w.append(all_security)
                                                    #set_w.append(all_weights)
                                                    #set_w.append(all_speed)
                                                    #set_w.append(all_delay)
                                                   
                                                    
            
                       
                
                                 
                        """      
                        print("all_weights : ",all_weights)
                                
                        print("all_bandwidth : ",all_bandwidth)
                                   
                        print("all_security : ",all_security)
                        print("all_delay : ",all_delay)
                        print("all_speed : ",all_speed)
                        print("all_throughput : ",all_throughput)
                        x = len(all_bandwidth)
                        # z = len(set_w)
                          """          
                                    
                  #                  print("sss = ", x)
                   #                 print("sss = ",z )
        
                                    
                        print("--------")
        
                                   # print("nn" ,nx.maximum_flow_value(G,node_list[0],node_list[1]))
                                   
                                  
                                
                        print(" The sum of all the weights =  ",sum(all_weights))
                                
                                
                        print(" The sum of all the bandwidth =  ",sum(all_bandwidth))
                        
                        print(" The sum of all the security =  ",sum(all_security))
                        print(" The sum of all the delay =  ",sum(all_delay))
                        print(" The sum of all the speed =  ",sum(all_speed))
                        print(" The sum of all the throughput =  ",sum(all_throughput))
                                   
                        print(counter)
                      
    spl = dict(nx.all_pairs_shortest_path_length(G))
    for node1 in spl:
           for node2 in spl[node1]:
               x = spl.values()
               s = dis.append(x)
               l = len(dis)
   # print("sgt",l)
    #lat = 2 * 1
    Fiinal_speed = (sum(all_speed) +(l/sum(all_bandwidth)))+sum(all_speed)
    trans = l / sum(all_bandwidth) 
    pro_delay = Fiinal_speed / 2 
    Fiinal_delay = trans + pro_delay
    Fiinal_bandwidth = ( sum(all_weights) * Fiinal_delay ) / 2
    Fiinal_avai = 2 * Fiinal_bandwidth * Fiinal_delay
    Fiinal_thro = (sum(all_throughput) * Fiinal_bandwidth ) / 60
    print("Fiinal_speed = ",Fiinal_speed)
    print("Fiinal_delay = ",Fiinal_delay)
    print("Fiinal_bandwidth = ",Fiinal_bandwidth)
    print("Fiinal_avai = ",Fiinal_avai)
    print("Fiinal_thro = ",Fiinal_thro)
    sec_arr = []
    for i in range(100):
        i = i + 1 
        sec_arr.append(i)
  
    for x in sec_arr:
        s3 = sum(all_security)
        s4 = sum(sec_arr)
        Finsal_security = s3 * s4 
        
    print("Fiinal_security = ",Finsal_security)




    
    
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
   


