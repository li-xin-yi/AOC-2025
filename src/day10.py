from typing import List, Tuple
import pulp

def read_input(path: str) -> List[List]:
    with open(path, 'r') as f:
        return [line.strip('\n').split() for line in f.readlines()]

def calc_min_op(input: List) -> int:
    init_state = input[0][1:-1]
    target = int(''.join([str(int(c=='#')) for c in init_state[::-1]]), 2)
    seen = {0: 0}
    for button in input[1:-1]:
        digits = tuple(map(int, button[1:-1].split(',')))
        state = 0
        for d in digits:
            state |= (1 << d)
        for s, step in list(seen.items()):
            nstate = s ^ state
            if nstate not in seen or seen[nstate] > step + 1:
                seen[nstate] = step + 1
    return seen.get(target, -1)

def solve1(input: List[Tuple]) -> int:
    res = 0
    for line in input:
        res += calc_min_op(line)
    return res

def solve_ilp(input: List) -> int:
    target = tuple(map(int, input[-1][1:-1].split(',')))
    buttons = [tuple(map(int, line[1:-1].split(','))) for line in input[1:-1]]
    m = len(target)
    n = len(buttons)

    prob = pulp.LpProblem("MinButtonPress", pulp.LpMinimize)
    x = [pulp.LpVariable(f'x_{i}', cat='Integer', lowBound=0) for i in range(n)]

    prob += pulp.lpSum(x)

    for i in range(m):
        prob += (pulp.lpSum(x[j] for j in range(n) if i in buttons[j]) == target[i])
        
    result_status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if result_status != pulp.LpStatusOptimal:
        return -1

    presses = [int(pulp.value(var)) for var in x]
    return sum(presses)
    
def solve2(input: List[List]) -> int:
    res = 0
    for line in input:
        res += solve_ilp(line)
    return res


if __name__ == "__main__":
    input_path = '../input/day10.txt'
    input_data = read_input(input_path)
    res1 = solve1(input_data)
    print(res1)

    res2 = solve2(input_data)
    print(res2)

        
    
