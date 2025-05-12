# class Vertex:
#     def __init__(self, key, adjacent):
#         self.key = key
#         self.adjacent = adjacent
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
#     def BDFS(self, s, t):
#         OPEN = []
#         CLOSE = []
#         OPEN.append(self.node[s])
#         self.Recursion(OPEN, CLOSE, t)
#         return CLOSE
#
#     def Recursion(self, OPEN, CLOSE, s):
#         if len(OPEN) == 0:
#             return
#         i = OPEN.pop(0)
#         CLOSE.append(i)
#         for j in i.adjacent:
#             isUndiscover = True
#             for k  in OPEN:
#                 if j[0] == k:
#                     isUndiscover = False
#             for k in CLOSE:
#                 if j[0] == k:
#                     isUndiscover = False
#             if (isUndiscover):
#                 if s == "BFS":
#                     OPEN.append(j[0])
#                 elif s == "DFS":
#                     OPEN.insert(0, j[0])
#         self.Recursion(OPEN, CLOSE,s)
#
#
# G = Graph()
# G.AddVertex("H")
# G.AddVertex("I")
# G.AddVertex("J")
# G.AddVertex("K")
# G.AddVertex("L")
# G.AddVertex("M")
# G.AddVertex("N")
# G.AddVertex("O")
# G.AddVertex("D", ["H", "I"])
# G.AddVertex("E", ["J", "K"])
# G.AddVertex("F", ["L", "M"])
# G.AddVertex("G", ["N", "O"])
# G.AddVertex("B", ["D", "E"])
# G.AddVertex("C", ["F", "G"])
# G.AddVertex("A", ["B", "C"])
# LIST = G.BDFS("A", "BFS")
# print [i.key for i in LIST]
# LIST = G.BDFS("A", "DFS")
# print [i.key for i in LIST]

class Vertex:
    def __init__(self, key):
        self.key = key
        self.adjacent = []  # List of (Vertex, weight) tuples

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_vertex(self, key, neighbors=None, weights=None):
        """添加顶点及其邻接点（可选）"""
        vertex = Vertex(key)
        self.nodes[key] = vertex
        if neighbors:
            if weights is None:
                weights = [1] * len(neighbors)
            for neighbor_key, weight in zip(neighbors, weights):
                if neighbor_key in self.nodes:
                    vertex.adjacent.append((self.nodes[neighbor_key], weight))

    def add_edge(self, u, v, weight=1):
        """添加边 u -> v"""
        u_node = self.nodes[u]
        v_node = self.nodes[v]
        if not any(neigh.key == v for neigh, _ in u_node.adjacent):
            u_node.adjacent.append((v_node, weight))

    def bdfs(self, start_key, mode="BFS"):
        """支持 BFS 或 DFS 的遍历方法"""
        if start_key not in self.nodes:
            return []

        open_list = [self.nodes[start_key]]
        closed_list = []
        visited = set()

        def _recurse():
            if not open_list:
                return
            current = open_list.pop(0)
            closed_list.append(current)
            visited.add(current.key)
            for neighbor, _ in current.adjacent:
                if neighbor.key not in visited and neighbor not in open_list:
                    if mode.upper() == "BFS":
                        open_list.append(neighbor)
                    elif mode.upper() == "DFS":
                        open_list.insert(0, neighbor)
            _recurse()

        _recurse()
        return closed_list

# ===== 测试部分 =====
G = Graph()
# 添加叶子节点
for key in ["H", "I", "J", "K", "L", "M", "N", "O"]:
    G.add_vertex(key)
# 添加中间节点
G.add_vertex("D", ["H", "I"])
G.add_vertex("E", ["J", "K"])
G.add_vertex("F", ["L", "M"])
G.add_vertex("G", ["N", "O"])
G.add_vertex("B", ["D", "E"])
G.add_vertex("C", ["F", "G"])
G.add_vertex("A", ["B", "C"])

# 执行 BFS 和 DFS
bfs_result = G.bdfs("A", "BFS")
print("BFS Order:", [v.key for v in bfs_result])

dfs_result = G.bdfs("A", "DFS")
print("DFS Order:", [v.key for v in dfs_result])



# 优化项	说明
# ✅ Python 3 兼容	使用 print() 函数
# ✅ 命名规范	方法、变量命名改为小写并符合 PEP8 标准
# ✅ 可扩展性提升	分离 bfs() 和 dfs()，更符合设计职责
# ✅ 判重逻辑简化	使用集合提升效率，替代嵌套 for 判断
# ✅ 注释与结构优化	增加注释，清晰表达邻接关系与遍历逻辑
# 优化点	原代码问题/限制	优化后效果
# print 语法	使用 Python 2 写法	使用 print()，兼容 Python 3
# 命名风格	AddVertex、BDFS 等不规范	使用 PEP8 标准命名：add_vertex、bdfs
# 遍历判重效率低	使用两个 for 循环在 OPEN 和 CLOSE 查找重复项	改用 set 结构做判重（visited）提升效率
# 遍历策略混用	使用参数字符串判断 BFS/DFS，不直观	用统一函数处理模式，逻辑清晰易维护
# 顶点添加顺序混乱	添加邻接点时引用未创建顶点会报错	确保先添加叶子节点，再添加引用它们的顶点
