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

def point_in_polygon_int(px: int, py: int, points: List[Tuple[int, int]]) -> bool:
    inside = False
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        if y1 == y2:
            if py == y1 and min(x1, x2) <= px <= max(x1, x2):
                return True
        else:
            if px == x1 and min(y1, y2) <= py <= max(y1, y2):
                return True

            y_low = min(y1, y2)
            y_high = max(y1, y2)
            if y_low <= py < y_high:
                if px < x1:
                    inside = not inside

    return inside


def solve2(points: List[Tuple[int, int]]) -> int:
    if points and points[0] == points[-1]:
        points = points[:-1]

    xs = set()
    ys = set()
    for x, y in points:
        xs.add(x)
        ys.add(y)
        xs.add(x + 1)
        ys.add(y + 1)

    x_min = min(x for x, y in points)
    y_min = min(y for x, y in points)
    x_max = max(x for x, y in points)
    y_max = max(y for x, y in points)

    xs.add(x_min - 1)
    ys.add(y_min - 1)
    xs.add(x_max + 2)
    ys.add(y_max + 2)

    xs = sorted(xs)
    ys = sorted(ys)

    x_id = {x: i for i, x in enumerate(xs)}
    y_id = {y: i for i, y in enumerate(ys)}

    W = len(xs) - 1
    H = len(ys) - 1

    good = [[False] * W for _ in range(H)]
    for i in range(H):
        py = ys[i]
        for j in range(W):
            px = xs[j]
            good[i][j] = point_in_polygon_int(px, py, points)

    red_cells = []
    for x, y in points:
        red_cells.append((x_id[x], y_id[y]))

    good_weight = [[0] * W for _ in range(H)]
    for i in range(H):
        dy = ys[i + 1] - ys[i]
        for j in range(W):
            if good[i][j]:
                dx = xs[j + 1] - xs[j]
                good_weight[i][j] = dx * dy

    presum = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        row_sum = 0
        for j in range(W):
            row_sum += good_weight[i][j]
            presum[i + 1][j + 1] = presum[i][j + 1] + row_sum

    def rect_sum(top, left, bottom, right):
        return presum[bottom + 1][right + 1] - presum[top][right + 1] - presum[bottom + 1][left] + presum[top][left]

    res = 0
    R = len(red_cells)
    for i in range(R):
        x0, y0 = red_cells[i]
        for j in range(i + 1, R):
            x1, y1 = red_cells[j]

            if x0 == x1 or y0 == y1:
                continue

            top = min(y0, y1)
            bottom = max(y0, y1)
            left = min(x0, x1)
            right = max(x0, x1)

            rect_area = (xs[right + 1] - xs[left]) * (ys[bottom + 1] - ys[top])
            good_area = rect_sum(top, left, bottom, right)

            if good_area == rect_area:
                res = max(res, rect_area)

    return res


if __name__ == "__main__":
    input_path = '../input/day09.txt'
    points = read_input(input_path)
    res1 = solve1(points)
    print(res1)

    res2 = solve2(points)
    print(res2)