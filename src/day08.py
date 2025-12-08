from typing import List, Tuple
import heapq
def read_input(path: str) -> List[Tuple[int, int, int]]:
    with open(path, 'r') as f:
        return [tuple(map(int, line.strip('\n').split(','))) for line in f.readlines()]

def calc_dist(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


def solve1(points: List[Tuple[int, int, int]], k=10) -> int:
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            dist = calc_dist(points[i], points[j])
            edges.append((dist, i, j))
    heapq.heapify(edges)

    parent = list(range(n))
    size = [1] * n
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int) -> None:
        rx, ry = find(x), find(y)
        if rx != ry:
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            return True
        return False
    
    while k:
        _, u, v = heapq.heappop(edges)
        union(u, v)
        k -= 1

    roots = set()
    for i in range(n):
        roots.add(find(i))
    groups = sorted([size[r] for r in roots], reverse=True)[:3]
    res = 1
    for g in groups:
        res *= g
    
    return res


def solve2(points: List[Tuple[int, int, int]]) -> int:
    n = len(points)
    edges = []
    g = n
    for i in range(n):
        for j in range(i+1, n):
            dist = calc_dist(points[i], points[j])
            edges.append((dist, i, j))
    heapq.heapify(edges)

    parent = list(range(n))
    size = [1] * n
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int) -> None:
        rx, ry = find(x), find(y)
        if rx != ry:
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            return True
        return False
    
    while True:
        _, u, v = heapq.heappop(edges)
        if union(u, v):
            g -= 1
            if g == 1:
                return points[u][0] * points[v][0]

    return 0
    


if __name__ == "__main__":
    input_path = '../input/day08.txt'
    points = read_input(input_path)
    res1 = solve1(points, k=1000)
    print(res1)
    
    res2 = solve2(points)
    print(res2)
