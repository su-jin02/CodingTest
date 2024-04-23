from collections import Counter

def solution(X, Y):
    answer = ''
    x_cnt = Counter(map(int, X))
    y_cnt = Counter(map(int, Y))
    common_keys = sorted(set(x_cnt.keys()) & set(y_cnt.keys()), reverse=True)

    if not common_keys:
        return "-1"
    elif len(common_keys) == 1:
        return str(common_keys[-1])
    answer = "".join(str(key) * min(x_cnt[key], y_cnt[key]) for key in common_keys)
    return answer


# def solution(x,y):
#     y = list(y)
#     answer = []
#     for i in x:
#         if i in y:
#             y.remove(i)
#             answer.append(i)
#     if not answer:
#         answer = "-1"
#     else:
#         answer.sort(reverse=True)
#         answer = int("".join(map(str, answer)))
#     return str(answer)