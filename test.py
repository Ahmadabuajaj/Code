
import networkx as nx


#G_symmetric = nx.Graph()
G_weighted = nx.Graph()



G_weighted.add_edge('Node A','Node D', weight=3)
G_weighted.add_edge('Node A','Node E', weight=2)
G_weighted.add_edge('Node B','Node C', weight=5)
G_weighted.add_edge('Node B','Node D', weight=2)
G_weighted.add_edge('Node B','Node E', weight=3)
G_weighted.add_edge('Node E','Node C',weight=4)


print(G_weighted.edges.items())
edges = list(G_weighted.edges.__iter__())
for i in edges:
    print(i)

data = G_weighted.get_edge_data('Node A','Node D')

nx.draw_networkx(G_weighted)
G_weighted.size()
#print(G_weighted.size())
#print(G_weighted.degree())
#print(G_weighted.degree('Node A'))
#x =  G_weighted.degree('Node A')
#print("x = " , x)


print(G_weighted.degree())
#print(G_weighted.number_of_edges())
#print(G_weighted.size())

#for weight  in number(G_weighted):
 #   print(  weight)
    
x = nx.adjacency_matrix(G_weighted)
print(x)
#sum(x)
#print("x = " ,sum(x))
