ExpNo 2 : Implement Depth First Search Traversal of a Graph

Name:SHUBNUM FATHIMA AB
Register Number: 212225240147

Aim:
To Implement Depth First Search Traversal of a Graph using Python 3.

Theory:
Depth First Traversal (or DFS) for a graph is like Depth First Traversal of a tree. The only catch here is that, unlike trees, graphs may contain cycles (a node may be visited twice). Use a Boolean visited array to avoid processing a node more than once. A graph can have more than one DFS traversal. Depth-first search is an algorithm for traversing or searching trees or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. Step 1: Initially, stack and visited arrays are empty.
image

Queue and visited arrays are empty initially. Stack and visited arrays are empty initially. Step 2: Visit 0 and put its adjacent nodes which are not visited yet into the stack. image

Visit node 0 and put its adjacent nodes (1, 2, 3) into the stack Visit node 0 and put its adjacent nodes (1, 2, 3) into the stack

Step 3: Now, Node 1 at the top of the stack, so visit node 1 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack. image

Visit node 1 Visit node 1

Step 4: Now, Node 2 at the top of the stack, so visit node 2 and pop it from the stack and put all of its adjacent nodes which are not visited (i.e, 3, 4) in the stack. image

Visit node 2 and put its unvisited adjacent nodes (3, 4) into the stack Visit node 2 and put its unvisited adjacent nodes (3, 4) into the stack

Step 5: Now, Node 4 at the top of the stack, so visit node 4 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack. image

Visit node 4 Visit node 4

Step 6: Now, Node 3 at the top of the stack, so visit node 3 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack. image

Visit node 3 Visit node 3

Now, the Stack becomes empty, which means we have visited all the nodes, and our DFS traversal ends.

Algorithm:
Construct a Graph with Nodes and Edges
Depth First Search Uses Stack and Recursion
Insert a START node to the STACK
Find its Successors Or neighbors and Check whether the node is visited or not
If Not Visited, add it to the STACK. Else Call The Function Again Until No more nodes needs to be visited.

Program:
```
from collections import defaultdict

def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True

    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited, path)

    return path


graph = defaultdict(list)

n, e = map(int, input("Enter the number of nodes and edges: ").split())

for i in range(e):
    u, v = input(f"Enter edge {i+1} (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)

if '0' in graph:
    start = '0'
else:
    start = 'A'

visited = defaultdict(bool)
path = []

traversed_path = dfs(graph, start, visited, path)

print("DFS Traversal Path:", traversed_path)
```
Output:
<img width="612" height="246" alt="image" src="https://github.com/user-attachments/assets/3665dc10-efcb-487a-96fa-ad6e4df3b125" />

Result:
Thus,a Graph was constructed and implementation of Depth First Search for the same graph was done successfully.
