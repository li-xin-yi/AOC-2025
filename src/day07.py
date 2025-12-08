from typing import List
def read_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.strip('\n') for line in f.readlines()]

def solve1(lines: List[str]) -> int:
    ys = set([lines[0].index('S')])
    n, m = len(lines), len(lines[0])
    res = 0
    for i in range(1, n):
        next_ys = set()
        for y in ys:
            if lines[i][y] == '.':
                next_ys.add(y)
            elif lines[i][y] == '^':
                res += 1
                for dy in [-1, 1]:
                    ny = y + dy
                    if 0 <= ny < m:
                        next_ys.add(ny)
        ys = next_ys

    return res

def solve2(lines: List[str]) -> int:
    n, m = len(lines), len(lines[0])
    ys = [1] * m
    for i in range(n-1, 0, -1):
        ys = list(ys)
        for j in range(m):
            if lines[i][j] == '^':
                ys[j] = ys[j-1] + ys[j+1]
    y0 = lines[0].index('S')
    return ys[y0]


if __name__ == "__main__":
    input_path = '../input/day07.txt'
    lines = read_input(input_path)
    res1 = solve1(lines)
    print(res1)

    res2 = solve2(lines)
    print(res2)