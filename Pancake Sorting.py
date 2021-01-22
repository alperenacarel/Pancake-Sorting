from simpleai.search import SearchProblem, astar
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

def takeInput():
    goal = ()
    actions = ()
    initial_console = ()

    for i in range(0, num_pancake):
        goal += (i,)
        actions += (i,)

    ordering = input("Do you want to enter ordering: ")
    if ordering == "yes":
        initial_console = tuple(int(x.strip()) for x in input(
            "Enter top to bottom ordering between [0 - {}], seperated by spaces: ".format(num_pancake-1)).split(' '))
        return goal, actions, initial_console

    elif ordering == "no":
        perm = tuple(permutations(goal))
        initial_console = random.choice(perm)
        return goal, actions, initial_console

    else:
        print("Please enter 'yes' or 'no'")
        return takeInput()

GOAL, action_list, initial = takeInput()

print("initial state : ",initial)
problem = PancakeSorting(initial_state=initial)
result = astar(problem, viewer=myViewer, graph_search=True)

res = str(result)
res = res.replace("Node", "")
res = res.replace("<", "")
res = res.replace(">", "")

print("{} result : {}".format("A*", result.path()))
print("cost :", result.cost)
print("final state : {}".format(res) )
print(myViewer.stats)

input("Press a button for quit...")
