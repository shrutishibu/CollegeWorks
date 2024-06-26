#dfs
def takeInput():
    for i in range(n):
        graph[i] = list(map(int, input().split()))
def dfs(start):
    print(start, end=" ")
    visited[start] = 1
    for i in range(n):
        if graph[start][i] == 1 and not visited[i]:
            dfs(i)
n = int(input("No. of nodes: "))
graph = [[0]*n for _ in range(n)]
takeInput()
visited = [0]*n
start = int(input("Start: "))
dfs(start)