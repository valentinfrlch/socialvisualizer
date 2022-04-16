# draw a network graph from data from a json file

import json
from pyvis.network import Network

path = "connections.json"

#import the json and store as a dictionary
with open(path) as f:
    connections = json.load(f)


def visualize(connections):
    # create a network object
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    # loop through the dictionary and add nodes
    for node in connections:
        net.add_node(node, label=node)
    
    # show the network
    net.show("network.html")



visualize(connections)
