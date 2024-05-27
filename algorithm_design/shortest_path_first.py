my_graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('D', 5)],
    'D': [('A', 4), ('C', 5)]
}

def shortest_path(graph, start):
  # unvisited = []
  unvisited = list(graph)
  distances = {node: 0 if node == start else float('inf') for node in graph}
  paths = {node: [] for node in graph}
  paths[start].append(start)

  # for vertex in graph:
  #   unvisited.append(vertex)

  #   if vertex == start:
  #     distance[vertex] = 0
  #   else:
  #     distance[vertex] = float('inf')

  while unvisited:
    current = min(unvisited, key = distance.get)
    for node, distance in graph[current]:
      if distances[current] + distance < distances[node]:
        distance[node] = distance[current] + distance
        if paths[node][-1] == node:
          paths[node] = paths[current]
        else:
          paths[node].extend(paths[current])
      paths[node].append(node)
    unvisited.remove(current)

  print(f'Unvisited: {unvisited}\nDistance: {distances}\nPaths: {paths}')

shortest_path(my_graph, 'A')