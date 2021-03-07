# -*- coding: utf-8 -*-
"""
#Becky Matthews-Pease
IST 659: Scripting for Data Analysis
Week 10
"""

##Undirected Graphs

conda install networkx

from sympy import Matrix
import sympy
import numpy
import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_edge(1,2)
g.add_node("spam")
g.nodes()

g.edges()

g.add_edge(1,"spam")
g.edges()

g.add_nodes_from([3,4])
g.add_edges_from([(1, 3), (3,4)])
g.nodes()

g.edges()

g.add_node(5, color = "blue")
g.nodes[1]["color"] = "red"
#g.node[1] is the dictionary of existing node 1
g.nodes(data = True)
#lists each node with its data dictionary
[(1, {"color":"red"}), (2,{}), (3,{}), (4,{}), (5,{"color":"blue"}), ("spam", {})]

g.add_edge(2,5, weight = 4.7)
g.edges[1][2]["weight"] = 1.2 #g.edge[1][2] is dictionary of edge from 1 to 2
g.edges(data = True)
[(1,2,{"weight":1.2}), (1,3, {}), (1, "spam", {}), (2,5,{"weight":4.7}), (3,4,{})]

g.neighbors(1)
[2, 3, "spam"]

adj_matrix = nx.adjacency_matrix(g)
type(adj_matrix)
amatrix = adj_matrix.todense()
type(amatrix)
amatrix
matrix([[0,1,1],
        [1,0,0],
        [1,0,0]], dtype = int64)  #this result for a small graph with three nodes

deg = nx.degree(g)
type(deg)

deg

min(deg.values())
max(deg.values())

sorteddeg = sorted(deg.items(), key = lambda x:x[1])
for node in sorteddeg:
    print(node)


#Directed Graphs

dg = nx.DiGraph()
dg.add_weighted_edges_from([(1,2,.5),(3,1,.75)])

dg.nodes()

dg.edges(data = True)

dg.out_degree(1)

dg.out_degree(1, weight = "weight")

nx.connected_components(g)

comp_list = list(nx.connected_components(g))
comp_list

g.add_node(6)
comp_list = list(nx.connected_components(g))
comp_list

nx.draw(g)  #draw_random, draw_sphere, etc.
plot.show(g)

def trim_degrees(g, degree = 1):
    g2 = g.copy()
    d = nx.degree(g2)
    for n in g2.nodes():
        if d[n] <= degree: g2.remove_node(n)
    return g2

core = trim_degrees(g)
len(core)
core.nodes()
core.edges()


pip install geopy

##10.3.3





import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim()
geopy.geocoders.options.default_user_agent = "bmatth01@syr.edu"
geo = geocode(data['addr'], provider='nominatim')
location = geolocator.geocode("Hinds Hall, Syracuse, NY")
print(location.address)
##Output = Hinds Hall, 110, Smith Drive, University Hill, Syracuse, Onondaga County, New York, 13244, United States of America


location = geolocator.reverse("43.0382155,-76.1333455471294")
print(location.address)
##Output = Hinds Hall, 110, Smith Drive, University Hill, Syracuse, Onondaga County, New York, 13244, United States of America

location = geolocator.reverse("42.773760,-78.786973")
print(location.address)
##Output = Bills Stadium, Bills Drive, Windom, Orchard Park, Erie County, New York, 14127, United States of America

location = geolocator.reverse("44.854865,-93.242215")
print(location.address)
##Output = Mall of America, 60, Lindau Lane, Bloomington, Hennepin County, Minnesota, 55425, United States of America

location = geolocator.reverse("42.999775,-78.787046")
print(location.address)
##Output = Alfiero Center, Mary Talbert Way, Governors Residence Halls, North Bailey, Amherst, Erie County, New York, 14261, United States of America

location = geolocator.reverse("43.183994,-76.236695")
print(location.address)
##Output = Outback Steakhouse, 3946, State Route 31, Euclid, Town of Clay, Onondaga County, New York, 13090, United States of America

location = geolocator.reverse("40.689249,-74.044500")
print(location.address)
##Output = Statue of Liberty, Flagpole Plaza, Manhattan Community Board 1, Manhattan, New York County, New York, 10004, United States of America


###10.4.1
import json
import re
import pymongo
import facebook
import requests
from bson.json_util import dumps

client = pymongo.MongoClient()
collection = client.fbusers.chuckschumer

docs_bson = list(collection.find())
docs_json_str = [dumps(doc) for doc in docs_bson]
doclist = [json.loads(doc) for doc in docs_json_str]

doc = doclist[0]
type(doc)
doc.keys() 

dict_keys(['actions', 'message', 'status_type', 'type', 'to', 'shares', 'source', 'properties', 'link', 'from', 'picture', 'message_tags', 'created_time', 'is_expired', 'id', 'is_hidden
           , '_id', 'icon', 'updated_time', 'privacy', 'comments', 'object_id', 'likes'])

doc['from']
{'name': 'Senator Chuck Schumer', 'category': 'Government Official', 'id': '15771239406'}
doc('message')


doc('id')

FB_id = doc['id'
            ]