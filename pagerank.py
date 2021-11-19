from built_graph import build
import networkx as nx
import matplotlib.pyplot as plt
import pylab

G, (source, target, relation) = build()

ppr1 = nx.pagerank(G)
tuples = sorted([(key, val) for key, val in ppr1.items()], key=lambda x: -x[1])


G = nx.DiGraph()
rel = list(zip(source, target))
G.add_edges_from( rel )

node_list = list(G)
node_sizes = [ ppr1[x] * 200000 for x in node_list ]
pos = nx.kamada_kawai_layout(G)
plt.figure(num=None, figsize=(40, 40), dpi=80)
plt.axis('off')
fig = plt.figure(1)
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='#eb5c3f')
nx.draw_networkx_edges(G, pos, edge_color=(0.9,0.9,0.9))
nx.draw_networkx_labels(G, pos, font_size=18, font_weight='bold')

plt.savefig("graph.pdf", bbox_inches="tight")
pylab.close()
del fig