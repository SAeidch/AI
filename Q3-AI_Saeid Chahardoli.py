import heapq

# Define a function to find the least expensive path.
# This function not only returns the lowest cost but also the path taken to achieve this cost.
def uniform_cost_search(start, goals, graph, cost):
   # Initialize a priority queue with the starting point, cost set to 0, and an empty path.
   pq = [(0, start, [])]
   # Keep track of the nodes that have already been checked.
   visited = set()

   # Continue searching until there are no more nodes to check.
   while pq:
       # Get the node with the lowest cost so far.
       current_cost, current_node, current_path = heapq.heappop(pq)

       # Skip this node if it has been visited already.
       if current_node in visited:
           continue

       # Mark this node as visited.
       visited.add(current_node)
       # If it's a goal node, return the cost and path to reach this node.
       if current_node in goals:
           return {current_node: {'cost': current_cost, 'path': current_path}}

       # Explore the neighbors of the current node.
       for neighbor in graph[current_node]:
           if neighbor not in visited:
               new_cost = current_cost + cost[(current_node, neighbor)]
               heapq.heappush(pq, (new_cost, neighbor, current_path + [neighbor]))

   # If none of the goals are reachable, return infinity as the cost for all goals and an empty path.
   return {goal: {'cost': float('inf'), 'path': []} for goal in goals}

# Execute the main code if the script is run directly.
if __name__ == '__main__':
   # Construct a graph that has up to 30 nodes.
   graph, cost = [[] for _ in range(30)], {}

   # Define connections between nodes in the graph.
   graph[0].extend([4, 5, 16])
   graph[2].append(1)
   graph[3].append(1)
   graph[4].extend([2, 3, 5])
   graph[5].extend([8, 18])
   graph[6].extend([3, 7])
   graph[8].extend([16, 17])
   graph[16].append(17)
   graph[18].append(6)

   # Assign a travel cost for each direct connection between nodes.
   cost.update({
       (0, 4): 3, (0, 5): 9, (0, 16): 1,
       (2, 1): 2, (3, 1): 2,
       (4, 2): 1, (4, 3): 8, (4, 5): 2,
       (5, 8): 3, (5, 18): 2,
       (6, 3): 3, (6, 7): 2,
       (8, 16): 4, (8, 17): 4,
       (16, 17): 15,
       (18, 6): 1
   })

   # Specify the starting point of the search.
   start = 0

   # Indicate the target nodes to reach.
   goals = [7]

   # Perform the search to find the cheapest path to the goal and store the result.
   min_cost_info = uniform_cost_search(start, goals, graph, cost)

   # Display the results: the lowest cost and the path for each goal.
   for node, info in min_cost_info.items():
       print(f'Lowest cost to get from {start} to {node}: {info["cost"]}')
       print(f'Route taken: {info["path"]}')
