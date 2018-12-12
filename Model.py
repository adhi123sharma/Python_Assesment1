# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:01:16 2018

@author: gy18as
"""

import agentframework5
import random
import operator
import matplotlib.pyplot
import csv
import matplotlib.animation


#agents.append(agentframework5.Agent(environment))
'''
def distance_between(agents_row_a, agents_row_b):
  return (((agents_row_a[0] - agents_row_b[0])**2) + 
      ((agents_row_a[1] - agents_row_b[1])**2))**0.5
'''
environment=[]
f=open ('in.txt', newline='')
reader= csv.reader(f,quoting=csv. QUOTE_NONNUMERIC)
for row in reader:
    rowlist=[]
    environment.append(rowlist)
    for value in row:
        #]print(value)
        rowlist.append(value)
    #environment.append(rowlist)
    #this enironment.append above should have been under rowlist=[] as it is a part of rowlist code not here under rowlist.append 
f.close()

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()    
     

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 200

# Make the empty graph
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# make agents
agents = []
for i in range(num_of_agents):
    #random_seed += 1 
    agents.append(agentframework5.Agent(environment,agents))
      
carry_on = True	

if random.random() < 0.1:
   carry_on = False
   print("stopping condition")	     
        
def update(frame_number):
    
    #print (agents[i])
    fig.clear()   

   
    '''   
    # Move the agents.
    for j in range(num_of_iterations):
    for i in range(num_of_agents):
    '''
    
    
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(299,0)
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        

        
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
    
    #matplotlib.pyplot.show()

#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b)

    
        #agents[i].share_with_neighbours(neighbourhood)
          
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 20) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()















