def solution(book_time):
    answer = []
    book_time.sort()
    
    def time_append(h,m):
        if m + 10 >= 60:
            h += 1
            m = m + 10 - 60
        else:
            m = m + 10
        if h == 23 and m+10 > 59:
            h, m = 23, 59
        return h,m
        
    for time1,time2 in book_time:
        h1, m1 = map(int, time1.split(":"))
        h, m = map(int, time2.split(":"))
        h, m = time_append(h,m)
        if not answer:
            answer.append([h,m])
        else:
            flag = 0
            for k in range(len(answer)):
                h2,m2 = answer[k][0], answer[k][1]
                if h1 > h2 or (h1 == h2 and m1 >= m2):
                    answer[k][0], answer[k][1] = h, m
                    break
            else:
                answer.append([h,m])
    return len(answer)