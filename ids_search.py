import itertools
import util
from frontiers import Stack

from search_strategies import SearchNode

import frontiers

cutoff = "cutoff"

def recursive_dfs(node,problem,path, depth,touched):
    # Set the notification of cutoff
    cutoff_occurred = False
    touched.add(node.state)
    # Test whether find the goal
    if problem.goal_test(node.state):
        path.append([node.state,node.action])
        actions = []
        while node.action is not None:
            actions.append(node.action)
            node = node.parent
        actions.reverse()
        return actions

    # Return cutoff if depth achieve limit
    if depth == 0:
        touched.remove(node.state)
        return cutoff
    else:
        # Put the state and action into path and recursive dfs to find the goal
        path.append([node.state,node.action])
        for successor, action, cost in problem.get_successors(node.state):
            if successor not in touched:
                # Create the child node
                tem = SearchNode(successor, action, node.path_cost + cost, node,depth)
                result = recursive_dfs(tem,problem,path,depth-1,touched)
                if result == cutoff:
                  cutoff_occurred is True
                elif result is not None:
                    return result
        path.pop(-1)
        touched.remove(node.state)
        # Return cutoff if cutoff show up
        if cutoff_occurred is not True:
            return cutoff
        else:
            return

def dls(problem,depth):
    # Initial the variables
    path = list()
    touched = set()
    root = SearchNode(problem.get_initial_state(), None, 0, None,depth)
    # Put the variables into recursive function
    return recursive_dfs(root,problem, path,depth,touched)

def solve( problem ) :
    for depth in itertools.count():
        print(depth)
        result = dls(problem, depth)
        # Check whether the result equal to cutoff
        if result != cutoff:
            return result
