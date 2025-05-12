# class Node:
#     def __init__(self, key, prev=None, next_=None):
#         self.key = key
#         self.prev = prev
#         self.next_ = next_
#
#
# class List:
#     def __init__(self):
#         self.nil = Node("NIL")
#         self.nil.next_ = self.nil
#         self.nil.prev = self.nil
#         # Two guards link together.
#
#     def ListInsert(self, x):
#         x.next_ = self.nil.next_
#         self.nil.next_.prev = x
#         self.nil.next_ = x
#         x.prev = self.nil
#
#     def ListSearch(self, k):
#         x = self.nil.next_
#         while x.key != k and x != self.nil:
#             x = x.next_
#         return x
#
#     def ListDelete(self, x):
#         x.prev.next_ = x.next_
#         x.next_.prev = x.prev
#
#
# L = List()
# for i in range(0, 5):
#     L.ListInsert(Node(i))
# A = []
# for i in range(0, 5):
#     A.append(L.ListSearch(i))
#     print A[i].key
# for i in A:
#     L.ListDelete(i)
# print "DEBUG"

class Node:
    def __init__(self, key, prev=None, next_=None):
        self.key = key
        self.prev = prev
        self.next_ = next_

class DoublyCircularLinkedList:
    def __init__(self):
        self.nil = Node("NIL")  # Sentinel node (guard)
        self.nil.next_ = self.nil
        self.nil.prev = self.nil

    def list_insert(self, node):
        """在头部插入节点"""
        node.next_ = self.nil.next_
        self.nil.next_.prev = node
        self.nil.next_ = node
        node.prev = self.nil

    def list_search(self, key):
        """搜索并返回 key 对应的节点；若未找到，返回 NIL 哨兵节点"""
        x = self.nil.next_
        while x != self.nil and x.key != key:
            x = x.next_
        return x

    def list_delete(self, node):
        """删除指定节点（不能删除 NIL 节点）"""
        if node == self.nil:
            print("Attempted to delete NIL node; skipping.")
            return
        node.prev.next_ = node.next_
        node.next_.prev = node.prev

    def display(self):
        """打印链表中的所有元素"""
        result = []
        x = self.nil.next_
        while x != self.nil:
            result.append(x.key)
            x = x.next_
        return result

# ===== 测试部分 =====
dll = DoublyCircularLinkedList()

# 插入 0~4
for i in range(5):
    dll.list_insert(Node(i))

# 搜索并打印每个元素
nodes = []
for i in range(5):
    node = dll.list_search(i)
    nodes.append(node)
    print(f"Found node with key: {node.key}")

# 打印当前链表
print("Current list:", dll.display())

# 删除所有节点
for node in nodes:
    dll.list_delete(node)

# 验证删除后链表是否为空
# print("After deletion:", dll.display())
# print("DEBUG")
#
# 命名混乱	ListInsert → list_insert，遵循 Python 命名规范
# print 非 Python 3	全部改为 print() 函数
# 删除 NIL 节点风险	增加判断并输出提示，防止非法删除
# 没有遍历方法	添加 display() 用于完整链表内容调试与验证
# 调试输出混乱	结构化、格式化输出便于阅读和验证
