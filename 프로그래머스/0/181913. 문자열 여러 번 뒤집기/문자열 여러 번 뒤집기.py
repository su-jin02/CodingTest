def solution(my_string, queries):
    my_string = list(my_string)  # 문자열을 리스트로 변환
    for s, e in queries:
        my_string[s:e+1] = my_string[s:e+1][::-1]  # 슬라이싱을 통해 부분 뒤집기
    return ''.join(my_string)  # 리스트를 다시 문자열로 변환하여 반환
