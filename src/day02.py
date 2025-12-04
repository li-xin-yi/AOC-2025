from typing import Tuple, List

primes = [2, 3, 5, 7, 11]

def read_input(path: str) -> List[Tuple[int, int]]:
    with open(path, 'r') as f:
        input = f.read().strip()
    lines = input.split(',')
    return [tuple(map(int, line.split('-'))) for line in lines]

def find_upper(num: int, k: int = 2) -> int:
    if num < 10 ** (k-1):
        return 1
    num_str = str(num)
    n = len(num_str)
    if n % k != 0:
        prefix = '1' + '0' * (n // k)
    else:
        prefix = num_str[:n // k]
    if int(str(prefix) * k) >= num:
        return int(prefix)
    return int(prefix) + 1

def find_lower(num: int, k: int = 2) -> int:
    num_str = str(num)
    n = len(num_str)
    if n % k != 0:
        prefix = '9' * (n // k)
    else:
        prefix = num_str[:n // k]
    if int(str(prefix) * k) <= num:
        return int(prefix)
    return int(prefix) - 1




def solve1(lst: List[Tuple[int, int]]) -> int:
    res = 0
    for low, high in lst:
        l, r = find_upper(low), find_lower(high)
        for num in range(l, r + 1):
            res += int(str(num) * 2)
    return res

def solve2(lst: List[Tuple[int, int]]) -> int:
    res = 0
    for low, high in lst:
        seen = set()
        for k in primes:
            if k > len(str(high)):
                break
            l, r = find_upper(low, k), find_lower(high, k)
            for num in range(l, r + 1):
                if ((cur:=int(str(num) * k))) not in seen:
                    seen.add(cur)
                    res += cur
    return res


if __name__ == "__main__":
    input_path = '../input/day02.txt'
    lines = read_input(input_path)
    res1 = solve1(lines)
    print(res1)

    res2 = solve2(lines)
    print(res2)