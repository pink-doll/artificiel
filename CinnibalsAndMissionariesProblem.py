from assets.Node import *
from assets.Problem import *

class CinnibalsAndMissionariesProblem(Problem):
    def __init__(self, initial):
        self.initial = initial
        self.goal = [0, 0]

    def actions(self, a):
        """
            First number represent the canniballs, the other number represents the missionaries.
        """
        all_states = []

        if a[0]==0 and a[1]==0:
            return a

        # Subtract one
        if a[0] > 0:
            p = [a[0]-1, a[1]]
            if not (p[0] > p[1]):
                all_states.append(p)
        
        if a[1] > 0:
            p = [a[0], a[1]-1]
            if not (p[0] > p[1]):
                all_states.append(p)

        if a[1] > 0 and a[0] > 0:
            p = [a[0]-1, a[1]-1]
            if not (p[0] > p[1]):
                all_states.append(p)
        # Subtract two

        if a[0] > 1:
            p = [a[0]-2, a[1]]
            if not (p[0] > p[1]):
                all_states.append(p)

        if a[1] > 1:
            p = [a[0], a[1]-2]
            if not (p[0] > p[1]):
                all_states.append(p)
                
        return all_states
    
    def result(self, state, action):
        return action

    def goal_test(self, state):
        """
            This one needs to be redefined cause the state in a list.
            See the super.goal_test() to understand.
        """
        return state==self.goal

def depth_first_graph_search(problem):
    frontier = [(Node(problem.initial))]  # Stack
    explored = []
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.append(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and
                        child not in frontier)
    return None


pro = CinnibalsAndMissionariesProblem([3,3])
c = depth_first_graph_search(pro)

while c != None:
    print(c)
    c = c.parent
