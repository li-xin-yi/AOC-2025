from typing import List
from functools import reduce

def read_input(path: str) -> List[List[str]]:
    mat = []
    with open(path, 'r') as f:
        for line in f.readlines():
            mat.append(line.strip().split())
    return mat

def read_matarix(path: str) -> List[str]:
    with open(path, 'r') as f:
        return [line.strip('\n') for line in f.readlines()]

func = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}

def solve1(matrix: List[str]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    res = 0
    for j in range(m):
        col = [matrix[i][j] for i in range(n)]
        res += reduce(func[col[-1]], map(int, col[:-1]))
    return res

def solve2(matrix: List[str]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    res = 0
    op_pos = [i for i in range(m) if matrix[-1][i]!=' '] + [m+1]
    for s, e in zip(op_pos, op_pos[1:]):
        nums = []
        for j in range(s, e-1):
            nums.append(int(''.join(matrix[i][j] for i in range(n-1))))
        res += reduce(func[matrix[-1][s]], nums)
    return res


if __name__ == "__main__":
    input_path = '../input/day06.txt'
    lines = read_input(input_path)
    res1 = solve1(lines)
    print(res1)

    lines = read_matarix(input_path)
    res2 = solve2(lines)
    print(res2)
    