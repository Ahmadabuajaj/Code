
import matplotlib.pyplot as plt
import networkx as nx
 
 
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
    counter=0
 
    for av in values:
        for se in values:
            for de in values:
                for sp in values:
                    for ba in values:
                        for th in values:
                            G.add_edge(node_list[0],node_list[0],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[0],node_list[1],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[0],node_list[2],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[0],node_list[3],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[1],node_list[0],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[1],node_list[1],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[1],node_list[2],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[1],node_list[3],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[2],node_list[0],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[2],node_list[1],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[2],node_list[2],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[2],node_list[3],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[3],node_list[0],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[3],node_list[1],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[3],node_list[2],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 
                            G.add_edge(node_list[3],node_list[3],weight=av,bandwidth=ba,security=se,delay=de,speed=sp,throughput=th) 

                            counter+=1
                            print(counter)

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
         
              #    unique_bandwidth.append(all_bandwidth)
               #   unique_bandwidth.append(all_security)
                #  unique_bandwidth.append(all_weights)
                 # ubue_bandwidth.append(all_speed)
                  #unique_bandwidth.append(all_delay)
                                         
                                       
                                        for (node1,node2) in G.edges():
                                            set_w.append(all_bandwidth)
                                            #set_w.append(all_security)
                                            #set_w.append(all_weights)
                                            #set_w.append(all_speed)
                                            #set_w.append(all_delay)
                                           
                                        
                                            

                                        

                               
                            for weight in unique_weights:
                                    weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in G.edges(data=True) if edge_attr['weight']==weight]
                                    width = weight*len(node_list)*3.0/sum(all_weights)
                                    nx.draw_networkx_edges(G,pos,edgelist=weighted_edges,width=width)
                        
                        
                            
                        
                            print("all_weights : ",all_weights)
                            
                            print("all_bandwidth : ",all_bandwidth)
                           
                            print("all_security : ",all_security)
                            print("all_delay : ",all_delay)
                            print("all_speed : ",all_speed)
                            print("all_throughput : ",all_throughput)
                            x = len(all_bandwidth)
                            z = len(set_w)

                            
                            print("sss = ", x)
                            print("sss = ",z )

                            
                            print("--------")
                        
                        
                        
                            
                                
                        
                        
                            print(" The sum of all the weights =  ",sum(all_weights))
                        
                        
                            print(" The sum of all the bandwidth =  ",sum(all_bandwidth))
                        
                            print(" The sum of all the security =  ",sum(all_security))
                            print(" The sum of all the delay =  ",sum(all_delay))
                            print(" The sum of all the speed =  ",sum(all_speed))
                            print(" The sum of all the throughput =  ",sum(all_throughput))
                        
                        
                          
                        
                          
                            #plt.show() 




if __name__=='__main__':
    plot_weighted_graph()


