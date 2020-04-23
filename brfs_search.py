import util
import search_strategies

from search_strategies import breadth_first_search
import frontiers

from frontiers import Queue

def solve(problem) :
    # Initial the variables
    start_state = problem.get_initial_state()
    frontier_q = Queue()
    visited = set()
    parents = dict()
    parents[start_state] = None
    tree = {}

    visited.add(start_state)
    frontier_q.push(start_state)

    t1 = {start_state: None}
    t2 = {start_state: t1}
    tree.update(t2)
    # Search the loop until the frontier is empty

    while frontier_q.is_empty() is not True:

            current_state = frontier_q.pop()
            if problem.goal_test(current_state):
                    path = [current_state]
                    actions = [tree[current_state][1]]
                    parent = tree[current_state][0]
                    action = tree[current_state][1]
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
            # Test is the state is the goal state
            if problem.goal_test(current_state):
                path = [current_state]
                actions = [tree[current_state][1]]
                parent = tree[current_state][0]
                action = tree[current_state][1]

                # Find the parents from the target
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

            for successor, action, cost in problem.get_successors(current_state):
                if successor not in parents.keys():
                    parents[successor] = current_state
                    temp1 = [current_state, action]
                    temp = {successor: temp1}
                    tree.update(temp)

                # Add state into frontier and visited
                if successor not in visited:

                    frontier_q.push(successor)
                    visited.add(successor)






