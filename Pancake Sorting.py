from simpleai.search import SearchProblem, breadth_first, astar, greedy, uniform_cost, iterative_limited_depth_first, depth_first, limited_depth_first
from itertools import permutations
import random
import functools 
from simpleai.search.viewers import BaseViewer

myViewer = BaseViewer()

GOAL = ()
action_list = ()
initial = ()

class PancakeSorting(SearchProblem):
    def actions(self, state):
        
        return action_list
    
    def result(self, state, action):
        
        return state[action::-1] + state[action+1:len(state)]

    def is_goal(self, state):
        
        return state == GOAL

    def heuristic(self, state):
        
        return (len(initial)-2 - state[len(initial)-2])**2 + (len(initial)-1 - state[len(initial)-1])**2

    def cost(self, state1, action, state2):
       
        return 1

num_pancake = int(input("Enter number of pancakes: "))

for i in range(0, num_pancake):
    GOAL += (i,)
    action_list += (i,)

ordering = input("Do you want to enter ordering: ")
if ordering == "yes":
    initial = tuple(int(x.strip()) for x in input(
        "Enter top to bottom ordering between [0 - {}], seperated by spaces: ".format(num_pancake-1)).split(' '))
    
elif ordering == "no":
    perm = tuple(permutations(GOAL))
    initial = random.choice(perm)
    
print("initial state : ",initial)
problem = PancakeSorting(initial_state=initial)

result = astar(problem, viewer=myViewer, graph_search=True)
print("{} result : {}".format("A*", result.path()))
print("cost: ", result.cost)
print(myViewer.stats)
