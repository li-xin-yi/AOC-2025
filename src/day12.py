from typing import List, Tuple

def read_input(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()
    shapes = []
    for i in range(6):
        shape = []
        for line in lines[i*5+1:i*5+4]:
            shape.append(line.strip())
        shapes.append(shape)
    queries = []
    for line in lines[30:]:
        if not line.strip():
            continue
        left, right = line.strip().split(': ')
        n, m = map(int, left.split('x'))
        lst = list(map(int, right.split()))
        queries.append((n, m, lst))
    return shapes, queries

def area(shape: List[str]) -> int:
    return sum(row.count('#') for row in shape)

def solve(shapes: List[List[str]], queries: List[Tuple[int, int, List[int]]]) -> int:
    areas = [area(shape) for shape in shapes]
    res = 0
    for n, m, lst in queries:
        total = sum(c*a for c, a in zip(lst, areas))
        if total > n * m:
            continue
        res += 1
    return res
    

if __name__ == "__main__":
    input_path = "../input/day12.txt"
    shapes, queries = read_input(input_path)
    print(solve(shapes, queries))
