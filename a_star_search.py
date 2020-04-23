import util
from frontiers import PriorityQueue
from search_strategies import a_star_search
def solve(problem, heuristic) :
    # Initial the variables
    start_state=problem.get_initial_state()
    frontier = PriorityQueue()
    frontier.push(start_state, 0)
    came_from = {}
    path_cost = {}
    came_from[start_state] = None
    path_cost[start_state] = 0
    tree = {}
    t1 = {start_state: None}
    t2 = {start_state: t1}
    tree.update(t2)

    # Start the loop until find the goal
    while frontier.is_empty() is not True:
        current_state = frontier.pop()
        # Test if the state is the goal state
        if problem.goal_test(current_state):
            path = [current_state]
            actions = [tree[current_state][1]]
            parent = tree[current_state][0]
            action = tree[current_state][1]

            #  Find the parents from the target
            while parent is not None:
                if parent not in path:
                    if tree[parent][0] != start_state:
                        path.append(parent)
                        actions.append(action)
                        parent = tree[parent][0]
                        action = tree[parent][1]
                    else:
                        action = tree[parent][1]
                        actions.append(action)

                        actions = actions[::-1]
                        break

            return actions

        # Obtain the information about the sub-states
        for successor, action, cost in problem.get_successors(current_state) :
            new_cost = path_cost[current_state] + cost

            # Check the cost of child
            if successor in path_cost and new_cost < path_cost[successor]:
                   continue
            # Put the successor in to the frontier and the tree which record the action
            if successor not in path_cost:
                path_cost[successor] = new_cost
                priority = new_cost+heuristic(successor,problem)
                frontier.push(successor, priority)
                came_from[successor] = current_state
                temp1 = [current_state,action]
                temp = {successor:temp1}
                tree.update(temp)
