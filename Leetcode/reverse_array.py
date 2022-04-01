"""
author: Yuxi Zhou
2022-04-01 17:48:58
"""


# the function is expected to return an reversed array of the input one

def reverse_array(a):
    return a[::-1]


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = reverse_array(arr)
    print(result)