def solution(picture, k):
    result = []
    for row in picture:
        transformations = ''
        for i in row:
            for _ in range(k):
                transformations += i
        for _ in range(k):
            result.append(transformations)
    return result