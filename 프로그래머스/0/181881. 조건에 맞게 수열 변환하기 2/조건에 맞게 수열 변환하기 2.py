def solution(arr):
    return dup(arr)  # 결과를 반환하도록 수정
        
def dup(arr):
    count = 0  # 로컬 카운트 변수 초기화
    while True:
        original_arr = arr.copy()  # 현재 상태의 리스트 복사
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] /= 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
        
        count += 1  # 카운트 증가
        
        if original_arr == arr:  # 리스트가 동일하면 반복 종료
            return count - 1
        

