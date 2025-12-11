from collections import defaultdict, Counter

def read_input(path: str) -> (defaultdict(list), defaultdict(list)):
    adj = defaultdict(list)
    rev = defaultdict(list)
    with open(path, 'r') as f:
        for line in f:
            u, adj_list = line.strip('\n').split(': ')
            for v in adj_list.split():
                adj[u].append(v)
                rev[v].append(u)
    return adj, rev

def solve1(adj: defaultdict(list), rev: defaultdict(list), src: str, dst: str) -> int:
    cnt = Counter()
    cnt[src] = 1
    degree = {u: len(vs) for u, vs in rev.items()}
    q = [u for u in adj if degree.get(u, 0) == 0]
    for u in q:
        for v in adj[u]:
            cnt[v] += cnt[u]
            degree[v] -= 1
            if degree[v] == 0:
                q.append(v)
    return cnt[dst]

def solve2(adj: defaultdict(list), rev: defaultdict(list), src: str, dst: str, mid1: str, mid2: str) -> int:
    if (mid:= solve1(adj, rev, mid1, mid2)) == 0:
        mid1, mid2 = mid2, mid1
        mid = solve1(adj, rev, mid1, mid2)
    
    left = solve1(adj, rev, src, mid1)
    right = solve1(adj, rev, mid2, dst)
    return left * mid * right

    # Placeholder for part 2 solution
    


if __name__ == "__main__":
    input_path = '../input/day11.txt'
    adj, rev = read_input(input_path)
    res1 = solve1(adj, rev, 'you', 'out')
    print(res1)

    res2 = solve2(adj, rev, 'svr', 'out', 'dac', 'fft')
    print(res2)

