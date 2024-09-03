def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    result = "".join(numbers)
    return result if result[0] != '0' else '0'