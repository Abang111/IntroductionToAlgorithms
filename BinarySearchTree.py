# import random
#
#
# class Tree:
#     def __init__(self):
#         self.l = None
#         self.r = None
#         self.k = None
#         self.p = None
#
#     def Transplant(self, u, v):
#         if u.p is None:
#             u.k = v.k
#
#         elif u is u.p.l:
#             u.p.l = v
#         else:
#             u.p.r = v
#         if v.k is not None:
#             v.p = u.p
#
#     def TreeDelete(self, z):
#
#         if z.l.k is None:
#             self.Transplant(z, z.r)
#         elif z.r.k is None:
#             self.Transplant(z, z.l)
#         else:
#             y = z.r.TreeMinimum()
#             if y.p is not z:
#                 self.Transplant(y, y.r)
#                 y.r = z.r
#                 y.r.p = y
#             self.Transplant(z, y)
#             y.l = z.l
#             y.l.p = y
#
#     def Insert(self, T, i, P):
#         if T.k == None:
#             T.k = i
#             T.p = P
#             T.l = Tree()
#             T.r = Tree()
#         elif T.k > i:
#             self.Insert(T.l, i, T)
#         elif T.k < i:
#             self.Insert(T.r, i, T)
#
#     def Sort(self, A):
#         # random.shuffle(A) # This is use to get randomized Tree.
#         for i in range(0, len(A)):
#             self.Insert(self, A[i], None)
#
#     def InOrderTreeWalk(self, A):
#         if self.k is not None:
#             self.l.InOrderTreeWalk(A)
#             A.append(self)
#             self.r.InOrderTreeWalk(A)
#
#     def TreeSearch(self, k):
#         if self.k == k or self.k is None:
#             return self
#         elif k < self.k:
#             return self.l.TreeSearch(k)
#         else:
#             return self.r.TreeSearch(k)
#
#     def IterativeTreeSearch(self, k):
#         while self.k is not None and self.k != k:
#             if k < self.k:
#                 self = self.l
#             else:
#                 self = self.r
#         return self
#
#     def TreeMinimum(self):
#         while self.l.k is not None:
#             self = self.l
#         return self
#
#     def TreeMaxinum(self):
#         while self.r.k is not None:
#             self = self.r
#         return self
#
#
# A = []
# s = random.randint(5, 100)
# for i in range(0, s):
#     A.append(random.randint(0, 1000))
# k = random.choice(A)
# t = Tree()
# t.Sort(A)
# A = []
# t.InOrderTreeWalk(A)
# print "Using InOrderWalk:", [A[i].k for i in range(0, len(A))]
# print "Using Recursion method to find ", k, " :", t.TreeSearch(k).k
# print "Using Interval method to find ", k, " :", t.IterativeTreeSearch(k).k
# print "Finding the Minimum elem :", t.TreeMinimum().k
# print "Finding the Maximum elem :", t.TreeMaxinum().k
# d = random.choice([A[i].k for i in range(len(A))])
# print "we are going to delete:",d
# t.TreeDelete(t.TreeSearch(d))
# B = []
# t.InOrderTreeWalk(B)
# print "After deletion:",[B[i].k for i in range(0, len(B))]
import random

class TreeNode:
    def __init__(self, key=None):
        self.k = key
        self.l = None
        self.r = None
        self.p = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = TreeNode(key)
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.k < x.k:
                x = x.l
            else:
                x = x.r

        node.p = y
        if y is None:
            self.root = node  # Tree was empty
        elif node.k < y.k:
            y.l = node
        else:
            y.r = node

    def inorder_walk(self, node, result):
        if node is not None:
            self.inorder_walk(node.l, result)
            result.append(node)
            self.inorder_walk(node.r, result)

    def search(self, node, key):
        if node is None or key == node.k:
            return node
        if key < node.k:
            return self.search(node.l, key)
        else:
            return self.search(node.r, key)

    def iterative_search(self, node, key):
        while node is not None and key != node.k:
            if key < node.k:
                node = node.l
            else:
                node = node.r
        return node

    def minimum(self, node):
        while node.l is not None:
            node = node.l
        return node

    def maximum(self, node):
        while node.r is not None:
            node = node.r
        return node

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.l:
            u.p.l = v
        else:
            u.p.r = v
        if v is not None:
            v.p = u.p

    def delete(self, z):
        if z.l is None:
            self.transplant(z, z.r)
        elif z.r is None:
            self.transplant(z, z.l)
        else:
            y = self.minimum(z.r)
            if y.p != z:
                self.transplant(y, y.r)
                y.r = z.r
                y.r.p = y
            self.transplant(z, y)
            y.l = z.l
            y.l.p = y

# ==== 测试部分 ====

# 生成随机数据
A = [random.randint(0, 1000) for _ in range(random.randint(5, 100))]
k = random.choice(A)

bst = BinarySearchTree()
for value in A:
    bst.insert(value)

# 中序遍历（排序）
inorder_result = []
bst.inorder_walk(bst.root, inorder_result)
print("Using InOrderWalk:", [node.k for node in inorder_result])

# 搜索
print("Using Recursion method to find", k, ":", bst.search(bst.root, k).k)
print("Using Iterative method to find", k, ":", bst.iterative_search(bst.root, k).k)

# 最小最大值
print("Finding the Minimum elem:", bst.minimum(bst.root).k)
print("Finding the Maximum elem:", bst.maximum(bst.root).k)

# 删除元素
delete_key = random.choice([node.k for node in inorder_result])
print("We are going to delete:", delete_key)
node_to_delete = bst.search(bst.root, delete_key)
bst.delete(node_to_delete)

# 中序遍历再检查
after_delete_result = []
bst.inorder_walk(bst.root, after_delete_result)
print("After deletion:", [node.k for node in after_delete_result])

# ✅ 改进点汇总
# 使用 TreeNode 表示节点，职责更单一。
#
# 用 BinarySearchTree 封装操作逻辑，符合 OOP 原则。
#
# 修复了根节点替换的 bug。
#
# 打印输出更明确。
#
# 删除前后结果对比方便验证。
#
# 再加上图形可视化或递归平衡功能（如 AVL 树）
