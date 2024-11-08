from collections import Counter
def solution(array):
    count = Counter(array)
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]
    return modes[0] if len(modes) == 1 else -1