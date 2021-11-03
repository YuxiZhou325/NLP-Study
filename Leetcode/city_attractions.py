"""
City Attractions | CITRIX OA 2020
https://leetcode.com/discuss/interview-question/823105/city-attractions-citrix-oa-2020
"""

G = []
ans = 0
beauties = []


def dfs(cur_node, time_taken, beauty_collected, max_t, nodes_passed):
    if time_taken > max_t:
        return
    global ans
    if (cur_node == 0):
        ans = max(ans, beauty_collected)
    for (v, weight) in G[cur_node]:
        add = beauties[v]
        if v in nodes_passed:
            add = 0
        nodes_passed[v] = nodes_passed.get(v, 0) + 1
        time_taken += weight
        beauty_collected += add
        dfs(v, time_taken, beauty_collected, max_t, nodes_passed)
        time_taken -= weight
        beauty_collected -= add
        nodes_passed[v] = nodes_passed.get(v, 0) - 1
        if nodes_passed[v] == 0:
            del nodes_passed[v]


def findBestPath(n, m, max_t, beauty, u, v, t):
    global G
    G = [[] for _ in range(n)]
    global beauties
    beauties = beauty
    for i in range(m):
        a = u[i]
        b = v[i]
        weight = t[i]
        G[a].append((b, weight))
        G[b].append((a, weight))
    dfs(0, 0, beauties[0], max_t, {0: 1})
    return ans
