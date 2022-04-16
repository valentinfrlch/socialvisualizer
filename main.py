# draw a network graph from data from a json file
import json
from pyvis.network import Network

path = "connections.json"

#import the json and store as a dictionary
with open(path) as f:
    connections = json.load(f)


def visualize(connections):
    # create a network object
    net = Network(height="100%", width="100%",
                  bgcolor="#222222", font_color="white")

    # loop through the dictionary and add nodes
    for node in connections:
        net.add_node(node, label=node)
    
    # loop through the dictionary and add edges
    for node, connections in connections.items():
        for connection in connections:
            # only add if score is greater than 0.5
            if connections[connection]["score"] > 0.5:
                net.add_edge(node, connection)

    # show the network
    net.show_buttons()


    net.show("index.html")



visualize(connections)
