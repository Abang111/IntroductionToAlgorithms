# import random
#
#
# class Node:
#     def __init__(self, key, next_=None, prev=None, down=None):
#         self.key = key
#         self.next_ = next_
#         self.prev = prev
#         self.down = down
#
#
# class List:
#     def __init__(self):
#         minNum, maxNum = -1, 10000
#         self.L = Node(minNum)
#         E = Node(maxNum)
#         self.L.next_, E.prev = E, self.L
#
#
# class JList:
#     def __init__(self):
#         self.JL = []
#         self.JL.append(List())
#
#     def AddLevel(self):
#         self.JL.append(List())
#         self.JL[len(self.JL) - 1].L.down = self.JL[len(self.JL) - 2].L
#
#     def Add(self, key):
#         e = Node(key)
#         i = 0
#         while random.randint(0, 9) % 2 == 0:
#             i += 1
#         while len(self.JL) < i + 1:
#             self.AddLevel()
#         it = self.JL[i].L
#         while it.key < e.key:
#             it = it.next_
#         e.next_ = it
#         e.prev = it.prev
#         it.prev.next_ = e
#         it.prev = e
#         self.RecursiveAdd(e.prev.down, e, key)
#         return True
#
#     def RecursiveAdd(self, itt, e, key):
#         if itt == None:
#             return
#         e.down = en = Node(key)
#         while itt.key < en.key:
#             itt = itt.next_
#         en.next_ = itt
#         en.prev = itt.prev
#         itt.prev.next_ = en
#         itt.prev = en
#         itt = en.prev.down
#         self.RecursiveAdd(itt, en, key)
#
#     def Search(self, key, Level=None):
#         i = self.JL[len(self.JL) - 1].L if Level is None else Level
#         while i.key < key:
#             i = i.next_
#         if i.prev.down != None:
#             return self.Search(key, i.prev.down)
#         elif i.key == key:
#             return i
#         else:
#             return False
#
#     def Delete(self, key, Level=None):
#         i = self.JL[len(self.JL) - 1].L if Level is None else Level
#         while i.key < key:
#             i = i.next_
#         if i.key == key:
#             i.prev.next_ = i.next_
#             i.next_.prev = i.prev
#             while i.down is not None:
#                 i = i.down
#                 i.prev.next_ = i.next_
#                 i.next_.prev = i.prev
#         elif i.prev.down != None:
#             return self.Delete(key, i.prev.down)
#         else:
#             return False
#
# test = JList()
# for i in range(0, 10):
#     test.Add(i)
# n = test.Search(6)
# for i in range(0, 1024):
#     test.Delete(i)

import random

class Node:
    def __init__(self, key, next_=None, prev=None, down=None):
        self.key = key
        self.next_ = next_
        self.prev = prev
        self.down = down

class LevelList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(10000)
        self.head.next_ = self.tail
        self.tail.prev = self.head

class SkipList:
    def __init__(self):
        self.levels = []
        self.levels.append(LevelList())  # Level 0

    def add_level(self):
        """新增一层并连接上一层"""
        new_level = LevelList()
        new_level.head.down = self.levels[-1].head
        self.levels.append(new_level)

    def insert(self, key):
        level = 0
        # 随机决定插入的层数
        while random.randint(0, 1) == 0:
            level += 1
        while len(self.levels) <= level:
            self.add_level()

        new_node = Node(key)
        current = self.levels[level].head

        # 寻找插入位置
        while current.key < key:
            current = current.next_
        # 插入节点
        new_node.next_ = current
        new_node.prev = current.prev
        current.prev.next_ = new_node
        current.prev = new_node

        # 向下递归插入
        self._insert_down(new_node, new_node.prev.down, key)

    def _insert_down(self, upper_node, down_node, key):
        if down_node is None:
            return
        # 向下插入
        new_node = Node(key)
        upper_node.down = new_node

        current = down_node
        while current.key < key:
            current = current.next_
        new_node.next_ = current
        new_node.prev = current.prev
        current.prev.next_ = new_node
        current.prev = new_node

        self._insert_down(new_node, new_node.prev.down, key)

    def search(self, key):
        current = self.levels[-1].head
        while current:
            while current.next_ and current.next_.key <= key:
                current = current.next_
            if current.key == key:
                return current
            current = current.down
        return None

    def delete(self, key):
        current = self.levels[-1].head
        found = False
        while current:
            while current.next_ and current.next_.key < key:
                current = current.next_
            if current.next_ and current.next_.key == key:
                target = current.next_
                current.next_ = target.next_
                target.next_.prev = current
                found = True
                current = current.down
            else:
                current = current.down
        return found

# ==== 测试 ====
if __name__ == "__main__":
    skiplist = SkipList()
    for i in range(10):
        skiplist.insert(i)

    node = skiplist.search(6)
    print("Found 6" if node else "6 Not Found")

    for i in range(1024):
        skiplist.delete(i)
    print("Deletion done.")

# 项目	优化前	优化后
# 命名规范	List 与 Python 保留字冲突	改为 LevelList，避免冲突
# 层间链接	手动链接复杂	结构清晰，head.down 链接上下层
# 插入流程	多层嵌套	_insert_down 封装递归逻辑
# 删除流程	缺乏状态返回	返回布尔值说明是否成功删除
# 结构健壮性	无断链保护，逻辑易错	添加空值判断与边界保护
