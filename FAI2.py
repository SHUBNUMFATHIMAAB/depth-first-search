#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[ ]:




