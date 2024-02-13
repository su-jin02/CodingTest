# ict 코테 2번 문제 - 리스트 사이 개수 세기
def countBetween(arr, low, high):
    res = [0] * len(low)
    dic = {0:0} # 주어진 리스트 최솟값보다 더 작으면 0개
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

    def left_binary(target):
        left, right = 0, len(sort_dic) - 1
        while right-left > 1:
            mid = (left+right) // 2
            if sort_dic[mid] == target:
                if target == 0:
                    return 0
                return mid - 1 #자기자신 이전 값을 뺴야 원하는 값을 얻을 수 있음
            elif sort_dic[mid] < target:
                left = mid
            else:
                right = mid - 1
        return left

    def right_binary(target):
        left, right = 0, len(sort_dic) - 1
        while left <= right:
            mid = (left+right) // 2
            if sort_dic[mid] == target:
                return mid
            elif sort_dic[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    for i in range(len(low)):
        num = 0
        if low[i] == high[i]:
            if low[i] in dic:
                num = dic[low[i]]
        else:
            start_index = left_binary(low[i])
            print('start', start_index)
            end_index = right_binary(high[i])
            print('end' ,end_index)
            num = dic[sort_dic[end_index]] - dic[sort_dic[start_index]]
        res[i] = num

    return res

print(countBetween([1,1,1,5,5,5,5],[1],[4]))
# print(countBetween([1,2,2,3,4],[0,2],[2,4]))