from collections import Counter
def solution(s):
    counter = Counter()
    for i in s.replace("{{", "").replace("}}", "").split("},{"):
        counter.update(map(int, i.split(',')))
    sorted_elements = sorted(counter.items(), key=lambda x: (-x[1]))
    answer = [element for element, _ in sorted_elements]

    return answer