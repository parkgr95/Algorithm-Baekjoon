import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    distance = [int(1e9)] * (n + 1)
    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
    start, end = map(int, input().split())

    dijkstra(start)

    print(distance[end])

# 회고: 다익스트라 알고리즘