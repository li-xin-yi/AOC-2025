
def read_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def solve1(lst):
    cur = 50
    res = 0
    for line in lst:
        direction = line[0]
        value = int(line[1:])
        if direction == 'L':
            cur -= value
        elif direction == 'R':
            cur += value
        cur %= 100
        if cur == 0:
            res += 1
    return res

def solve2(lst):
    cur = 50
    res = 0
    for line in lst:
        direction = line[0]
        value = int(line[1:])
        new_cur = cur
        if direction == 'L':
            new_cur -= value
        elif direction == 'R':
            new_cur += value
        l, r = sorted([cur, new_cur])
        # count how many multiples of 100 are in [l, r]
        res += (r // 100) - ((l - 1) // 100)
        if cur % 100 == 0:
            res -= 1
        cur = new_cur % 100
    return res

if __name__ == "__main__":
    input_path = '../input/day01.txt'
    lines = read_input(input_path)
    res1 = solve1(lines)
    print(res1)
    res2 = solve2(lines)
    print(res2)

