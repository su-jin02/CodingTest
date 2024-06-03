def solution(n, q):
    answer = 0
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    print(rev_base[::-1])
    x = rev_base[::-1].split('0')
    for i in x:
        if i != '1' and i != '':
            if isPrime(float(i)) == True:
                answer += 1
    return answer


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True