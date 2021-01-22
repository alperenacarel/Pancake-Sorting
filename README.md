# Pancake-Sorting
Pancake Sorting Problem with simple.ai Library

Pancake sorting is the order of pancakes from smallest to largest in the order entered by the user or in a random order.

**Downloading**

simple.ai:

    pip install simpleai

**For more informations about simple.ai**

  https://github.com/simpleai-team/simpleai
  
**Working sample of the code**


    Enter number of pancakes: 5
    Do you want to enter ordering: yes
    Enter top to bottom ordering between [0 - 4], seperated by spaces: 2 0 1 4 3
    initial state :  (2, 0, 1, 4, 3)
    A* result : [(None, (2, 0, 1, 4, 3)), (3, (4, 1, 0, 2, 3)), (4, (3, 2, 0, 1, 4)), (3, (1, 0, 2, 3, 4)), (1, (0, 1, 2, 3, 4))]
    cost : 4
    final state :  (0, 1, 2, 3, 4)
    {'max_fringe_size': 24, 'visited_nodes': 14, 'iterations': 14}
    
    Enter number of pancakes: 4
    Do you want to enter ordering: no
    initial state :  (3, 0, 1, 2)
    A* result : [(None, (3, 0, 1, 2)), (3, (2, 1, 0, 3)), (2, (0, 1, 2, 3))]
    cost : 2
    final state :  (0, 1, 2, 3)
    {'max_fringe_size': 7, 'visited_nodes': 6, 'iterations': 6}
