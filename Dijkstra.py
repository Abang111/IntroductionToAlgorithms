# class Vertex:
#     def __init__(self, key, adjacent):
#         self.key = key
#         self.adjacent = adjacent
#         self.prev = None
#
#
# class Graph:
#     def __init__(self):
#         self.node = {}
#
#     def AddVertex(self, key, adjance=[], rank=[]):
#         A = []
#         if rank == []:
#             rank = [1 for i in range(0, len(adjance))]
#         for i in range(0, len(adjance)):
#             A.append((self.node[adjance[i]], rank[i]))
#
#         self.node[key] = Vertex(key, A)
#
#     def AddEdge(self, u, v, r):
#         for i in self.node[u].adjacent:
#             if i[0].key == v:
#                 return False
#         self.node[u].adjacent.append((self.node[v], r))
#
#     def Dijkstra(self, s, e):
#         OPEN = []
#         CLOSE = []
#         OPEN.append((self.node[s], 0))
#         self.Recursion(OPEN, CLOSE, e)
#         RET = []
#         i = self.node[e]
#         while i != None:
#             RET.append(i)
#             i = i.prev
#         RET.reverse()
#         return RET
#
#     def Contains(self, list, e):
#         for i in list:
#             if i[0] == e:
#                 return i
#         return False
#
#     def Recursion(self, OPEN, CLOSE, e):
#         if self.Contains(CLOSE, e):
#             return
#         if len(OPEN) == 0:
#             return
#         i = OPEN.pop(0)
#         CLOSE.append(i)
#         for j in i[0].adjacent:
#             if self.Contains(CLOSE, j[0]):
#                 continue
#             con = self.Contains(OPEN, j[0])
#             if con:
#                 if con[1] > i[1] + j[1]:
#                     OPEN.remove(con)
#                 else:
#                     continue
#             j[0].prev = i[0]
#             rank = i[1] + j[1]
#             OPEN.append((j[0], rank))
#         OPEN.sort(lambda x, y: cmp(x[1], y[1]))
#         self.Recursion(OPEN, CLOSE, e)
#
#
# G = Graph()
# G.AddVertex("s")
# G.AddVertex("t")
# G.AddVertex("x")
# G.AddVertex("y")
# G.AddVertex("z")
# G.AddEdge("s", "t", 10)
# G.AddEdge("s", "y", 5)
# G.AddEdge("t", "x", 1)
# G.AddEdge("t", "y", 2)
# G.AddEdge("x", "z", 4)
# G.AddEdge("y", "t", 3)
# G.AddEdge("y", "x", 9)
# G.AddEdge("y", "z", 2)
# G.AddEdge("z", "s", 7)
# G.AddEdge("z", "x", 6)
# path = G.Dijkstra("s", "x")
# print [i.key for i in path]
# print "DEBUG"

class Vertex:
    def __init__(self, key):
        self.key = key
        self.adjacent = []  # List of tuples: (neighbor Vertex, weight)
        self.prev = None

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_vertex(self, key):
        if key not in self.nodes:
            self.nodes[key] = Vertex(key)

    def add_edge(self, u, v, weight):
        if v not in self.nodes or u not in self.nodes:
            raise ValueError("Both vertices must exist.")
        for neighbor, _ in self.nodes[u].adjacent:
            if neighbor.key == v:
                return False  # Edge already exists
        self.nodes[u].adjacent.append((self.nodes[v], weight))

    def contains(self, lst, vertex):
        for v, dist in lst:
            if v == vertex:
                return v, dist
        return None

    def dijkstra(self, start_key, end_key):
        open_list = [(self.nodes[start_key], 0)]
        closed_list = []

        self._recursion(open_list, closed_list, self.nodes[end_key])

        path = []
        node = self.nodes[end_key]
        while node:
            path.append(node)
            node = node.prev
        path.reverse()
        return path

    def _recursion(self, open_list, closed_list, end_node):
        if self.contains(closed_list, end_node):
            return
        if not open_list:
            return

        current, current_dist = open_list.pop(0)
        closed_list.append((current, current_dist))

        for neighbor, weight in current.adjacent:
            if self.contains(closed_list, neighbor):
                continue
            existing = self.contains(open_list, neighbor)
            new_dist = current_dist + weight
            if existing:
                _, existing_dist = existing
                if new_dist < existing_dist:
                    open_list.remove(existing)
                else:
                    continue
            neighbor.prev = current
            open_list.append((neighbor, new_dist))

        open_list.sort(key=lambda x: x[1])
        self._recursion(open_list, closed_list, end_node)

# ===== 测试部分 =====
G = Graph()
for key in ["s", "t", "x", "y", "z"]:
    G.add_vertex(key)

edges = [
    ("s", "t", 10),
    ("s", "y", 5),
    ("t", "x", 1),
    ("t", "y", 2),
    ("x", "z", 4),
    ("y", "t", 3),
    ("y", "x", 9),
    ("y", "z", 2),
    ("z", "s", 7),
    ("z", "x", 6),
]

for u, v, w in edges:
    G.add_edge(u, v, w)

path = G.dijkstra("s", "x")
print([v.key for v in path])
print("DEBUG")

# Python 3兼容	使用cmp()已被移除	使用 key=lambda x: x[1]
# 命名标准	AddVertex, AddEdge 不符合规范	改为 add_vertex, add_edge 符合PEP 8
# 排序方式	lambda x, y: cmp(x[1], y[1]) 非法	改为 sort(key=lambda x: x[1])
# 结构清晰	顶点和图结构混乱	顶点/边关系分离，代码职责更明确
# 函数职责清晰	Dijkstra逻辑复杂，递归混用	拆分为 dijkstra() 和 _recursion() 更清晰
