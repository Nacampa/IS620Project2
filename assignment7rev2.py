# IS620 - Assignment 7
# Program: assignment7.py
# Student: Neil Acampa
# Date:    10/12/16
# Function: To use a bipartite network (a network with 2 distinct node sets)
#           and to perform the island method to identify significant subgraphs

#           Read in movie data from IMDB and test on a small sample. Create nodes and graph
#           Headings: Title,year,length,budget,rating (Using Movie info and average rating)
#           Headings: votes,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,mpaa	(Not using)
#           Headings: Action,Animation,Comedy,Drama,Documentary,Romance,Short (Using Movie Genra)

				          
#           10/9/16:  Get the Island method to work for the retweet graph
#	    10/16/16: Get the Island method to work for the movie database 



from __future__ import absolute_import 
from __future__ import division
import re
import os 
import math
import decimal
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import networkx as nx
import random
#from prettytable import prettytable


# Movie nodes
movietitle =[]
movieyear  =[]
movielength=[]

# Posible Edge Value
rating=[]

# Genra Nodes
actiongenra=[]
animationgenra=[]
comedygenra=[]
dramagenra=[]
docgenra=[]
romancegenra=[]
shortgenra=[]

linelst=[]
lines  = ""

def trim_edges(e, weight=1):
   """Method from Social Network Analysis for Startups"""
   
   g2=nx.Graph()
   for f, to , edata in e.edges(data=True):
     if edata['weight'] > weight:
       g2.add_edge(f, to, edata)
     
   return g2


def island_method(e, iterations = 5):
   """Method from Social Network Analysis for Startups"""

   weights = [edata['weight'] for f,to,edata in e.edges(data=True) if 'weight' in edata] 
   #weights = [(u,v,edata['weight']) for u,v,edata in g.edges(data=True) if 'weight' in edata ]

   mx = int(max(weights))
   mn = int(min(weights))
 
   #compute the size of the step, so we get a resonable step in iterations
   
   step = int((mx-mn)/iterations)
 

   return [[threshold, trim_edges(e, threshold)] for threshold in range(mn, mx, step)]




if __name__ == "__main__":
 linecnt    = 0
 print
 print
 e = nx.read_pajek("egypt_retweets.net")
  
 cc = nx.connected_component_subgraphs(e)
 x = [len(c) for c in nx.connected_component_subgraphs(e) if len(c) > 10]
 print(x)
 island = island_method(e)
 for i in island:
   print ("%d connections for each pair of nodes  %d Nodes at that Level") % (i[0], len(i[1]))
 

 
 


 