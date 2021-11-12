"""

"""
l = [0, 0, 1, 0, 0, 1, 1, 1, 2, 2, 3, 2, 3]


def counter(list):
    # parse the list and find occurance
    count = dict()
    for item in list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count


print(counter(l))

# an alternative way just for fun
result = {
    0: l.count(0),
    1: l.count(1),
    2: l.count(2),
    3: l.count(3)
}
print(result)
