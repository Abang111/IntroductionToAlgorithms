# import random
#
#
# def HashDelete(e, T, s):
#     i1, i2 = HashSearch(e, T, s)
#     T[i1].pop(i2)
#
#
# def HashSearch(e, T, s):
#     for i in range(0, len(T[e % s])):
#         if T[e % s][i] == e:
#             return e % s, i
#     return None
#
#
# def HashInsert(e, T, s):
#     T[e % s].append(e)
#
#
# print "Now displaying Chaining Hash"
# s = 13
# A = []
# T = [[] for i in range(0, s)]
# t = random.randint(5, 100)
# for i in range(0, t):
#     A.append(random.randint(0, 1000))
# for e in A:
#     HashInsert(e, T, s)
# print T
# e = random.choice(A)
#
# i1, i2 = HashSearch(e, T, s)
# print "The selected elem ", e, " is in Slot:", i1, " Position: ", i2
# HashDelete(e, T, s)
# print "After Deletion:"
# print T

import random

def hash_insert(key, table, slot_size):
    """将元素插入到哈希表中（使用链式哈希）"""
    index = key % slot_size
    table[index].append(key)

def hash_search(key, table, slot_size):
    """在哈希表中查找元素，返回其所在槽位及在链表中的位置"""
    index = key % slot_size
    for i, val in enumerate(table[index]):
        if val == key:
            return index, i
    return None

def hash_delete(key, table, slot_size):
    """从哈希表中删除指定元素"""
    result = hash_search(key, table, slot_size)
    if result is not None:
        index, position = result
        table[index].pop(position)

# ==== 测试代码 ====
print("Now displaying Chaining Hash")

slot_size = 13
data = [random.randint(0, 1000) for _ in range(random.randint(5, 100))]
hash_table = [[] for _ in range(slot_size)]

# 插入数据
for key in data:
    hash_insert(key, hash_table, slot_size)

# 显示哈希表
print("Hash Table:")
for i, chain in enumerate(hash_table):
    print(f"Slot {i}: {chain}")

# 随机选取一个要查找并删除的元素
target = random.choice(data)
search_result = hash_search(target, hash_table, slot_size)

if search_result:
    slot, pos = search_result
    print(f"The selected element {target} is in Slot {slot}, Position {pos}")
else:
    print(f"The selected element {target} was not found in the table.")

# 删除元素
hash_delete(target, hash_table, slot_size)

# 显示删除后的哈希表
print("After Deletion:")
for i, chain in enumerate(hash_table):
    print(f"Slot {i}: {chain}")

# ✅ 核心优化总结：
#
# 原始问题	优化方式
# print 为 Python 2 语法	全部改为 Python 3 兼容语法
# 函数命名简单，缺乏注释	增加文档注释与命名如 hash_insert 等
# 查找失败后无处理	hash_delete 添加查找结果判空处理
# A, T, s 命名不明确	更换为 data, hash_table, slot_size
# 输出格式混乱	使用 enumerate 和格式化字符串统一输出格式