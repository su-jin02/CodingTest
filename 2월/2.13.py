# ict 코테 2번 문제 - 리스트 사이 개수 세기
def countBetween(arr, low, high):
    res = [0] * len(low)
    dic = {}
    #딕셔너리로 횟수 세기
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    #누적합 만들기
    pre = 0
    sort_dic = sorted(dic.keys())
    for key in sort_dic:
        dic[key] += pre
        pre = dic[key]
    print(sort_dic)
    print(dic)

    def binary(target):
        left, right = 0, len(sort_dic) - 1
        while left <= right:
            mid = (left+right) // 2
            if sort_dic[mid] == target:
                return sort_dic[mid]
            elif sort_dic[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return sort_dic[left]

    for i in range(len(low)):
        num = 0
        if low[i] == high[i]:
            if low[i] in dic:
                num = dic[low[i]]
        else:
            start_index = binary(low[i])
            print('start', start_index)
            end_index = binary(high[i])
            print('end' ,end_index)
            num = dic[end_index] - dic[start_index]
        res[i] = num

    return res

print(countBetween([1,1,1,3,3,3,3],[2],[3]))