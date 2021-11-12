"""
Latest Recently Used Algorithm
2021-11-12 18:28:32
"""
"""LRU淘汰算法：
    1。如果此数据已经被缓存到链表中，遍历得到数据节点，将其从原位置删除，然后再插入链表头部
    2。如果数据没有再缓存链表中：缓存未满， 则直接加入头部
                            缓存已满， 则先删除尾节点，再将新的节点插入到链表

"""
# 这边进行相应列表的生成
data_list = []
while True:
    try:
        list_num = int(input("请输入列表数字:"))
        data_list.append(list_num)
    except:
        break

# 进行算法实现
while True:
    try:
        num = int(input("请输入数字:"))
        if num in data_list:
            data_list.remove(num)
            data_list.insert(0, num)
        else:
            if len(data_list) < 5:
                data_list.insert(0, num)
            else:
                data_list.pop(-1)
                data_list.insert(0, num)
        print(data_list)
    except:
        break

