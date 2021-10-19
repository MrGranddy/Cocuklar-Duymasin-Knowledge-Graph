import json
import networkx as nx
import matplotlib.pyplot as plt
import pylab

import numpy as np

def build():
    with open("graph.json", "r") as f:
        g = json.load(f)

    source = g["source"]
    target = g["target"]
    relation = g["relation"]

    G = nx.DiGraph()
    G.add_edges_from( zip(source, target) )

    return G, (source, target, relation)