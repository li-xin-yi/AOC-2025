import sys
input = sys.stdin.readline

def read_input(path: str) -> list[str]:
    with open(path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def reduce_max(digits: str, k: int = 2) -> int:
    n = len(digits)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]*10  + int(digits[i-1]))
    return dp[-1][-1]
    

def solve1(lst: list[str]) -> int:
    res = 0
    for digits in lst:
        res += reduce_max(digits)
    return res

def solve2(lst: list[str]) -> int:
    res = 0
    for digits in lst:
        res += reduce_max(digits, k=12)
    return res
    
if __name__ == "__main__":
    input_path = '../input/day03.txt'
    lines = read_input(input_path)
    res1 = solve1(lines)
    print(res1)
    res2 = solve2(lines)
    print(res2)