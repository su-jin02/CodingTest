def solution(routes):
    answer = 1
    routes.sort(key=lambda x:(x[1]))
    camera =  routes[0][1]

    for x,y in routes:
        if x > camera:
            answer += 1
            camera = y

    return answer