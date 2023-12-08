class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)

    def My_BFS(self, s, t, parent):
        visited = [False] * (self.row)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for index, val in enumerate(self.graph[u]):
                if visited[index] == False and val > 0:
                    queue.append(index)
                    visited[index] = True
                    parent[index] = u
                    if index == t:
                        return True
        return False


# Helping functions
def convert_to_incident_matrix(g):
    num_vertices = max(max(edge.keys(), default=0) for edge in g.values()) + 1
    incident_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, edges in g.items():
        for v, capacity in edges.items():
            incident_matrix[u][v] = capacity
    return incident_matrix


def convert_to_dict_matrix(g):
    dict_matrix = {}
    for u in range(len(g)):
        dict_matrix[u] = {}
        for v, capacity in enumerate(g[u]):
            if capacity > 0:
                dict_matrix[u][v] = capacity
    return dict_matrix


def FordFulkerson(graph, source, sink):
    parent = [-1] * (graph.row)

    max_flow = 0

    while graph.My_BFS(source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph.graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph.graph[u][v] -= path_flow
            graph.graph[v][u] += path_flow
            v = parent[v]

        temp_graph = convert_to_dict_matrix(graph.graph)

    DiGraph(temp_graph).show(edge_labels=True)

    return max_flow


# This means just my main function
if __name__ == "__main__":
    g1 = {
        0: {1: 10, 2: 7},
        1: {3: 3, 2: 9},
        2: {1: 6, 4: 11},
        3: {2: 9, 5: 18},
        4: {3: 6, 5: 4},
        5: {4: 2, 1: 3},
    }

    source = 0
    sink = 5

    g = Graph(convert_to_incident_matrix(g1))
    max_flow = FordFulkerson(g, source, sink)
    print(f"The maximum possible flow is {max_flow}")
