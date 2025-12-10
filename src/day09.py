from typing import List, Tuple

def read_input(path: str) -> List[Tuple[int, int]]:
    points = []
    with open(path, 'r') as f:
        for line in f:
            x, y = map(int, line.strip().split(','))
            points.append((x, y))
    return points

def solve1(points: List[Tuple[int, int]]) -> int:
    res = 0
    n = len(points)
    for i in range(n):
        x0, y0 = points[i]
        for j in range(i+1, n):
            x1, y1 = points[j]
            res = max(res, (abs(x0 - x1) + 1) * (abs(y0 - y1) + 1))
    return res


if __name__ == "__main__":
    input_path = '../input/day09.txt'
    points = read_input(input_path)
    res1 = solve1(points)
    print(res1)