import sys
input = sys.stdin.readline

def read_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def solve1(grid: list[str]) -> int:
    n, m = len(grid), len(grid[0])
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue
            cnt = 0
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] == '@':
                    cnt += 1
            if cnt < 4:
                res += 1
    return res


def solve2(grid: list[str]) -> int:
    n, m = len(grid), len(grid[0])
    res = 0
    q = []
    degrees = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue
            cnt = 0
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] == '@':
                    cnt += 1
            degrees[i][j] = cnt
            if cnt < 4:
                q.append((i, j))
    
    seen = set(q)
    for i, j in q:
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m and grid[x][y] == '@':
                degrees[x][y] -= 1
                if degrees[x][y] < 4 and (x, y) not in seen:
                    seen.add((x, y))
                    q.append((x, y))
    return len(seen)



if __name__ == "__main__":
    input_path = '../input/day04.txt'
    lines = read_input(input_path)
    res1 = solve1(lines)
    print(res1)
    res2 = solve2(lines)
    print(res2)