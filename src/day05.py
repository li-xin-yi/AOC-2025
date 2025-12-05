from typing import List, Tuple
import bisect

def read_input(path: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    with open(path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    intervals = []
    queries = []
    for line in lines:
        if '-' in line:
            low, high = map(int, line.split('-'))
            intervals.append((low, high))
        else:
            queries.append(int(line))
    return intervals, queries

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

def solve1(intervals: List[Tuple[int, int]], queries: List[int]) -> int:
    res = 0
    intervals = merge_intervals(intervals)
    for q in queries:
        idx = bisect.bisect_right(intervals, (q, float('inf'))) - 1
        if idx >= 0 and intervals[idx][0] <= q <= intervals[idx][1]:
            res += 1
    return res


def solve2(intervals: List[Tuple[int, int]]) -> int:
    intervals = merge_intervals(intervals)
    total_covered = sum(high - low + 1 for low, high in intervals)
    return total_covered


if __name__ == "__main__":
    input_path = '../input/day05.txt'
    intervals, queries = read_input(input_path)
    res1 = solve1(intervals, queries)
    print(res1)

    res2 = solve2(intervals)
    print(res2)
