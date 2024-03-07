def solution(s):
    from collections import deque
    answer = 0
    s = deque(s)
    match = {")":"(", "]":"[", "}":"{"}
    
    for _ in range(len(s)):        
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if stack:
                    if stack.pop() != match[i]:
                        break
                else:
                    break
        else:
            if not stack:
                answer += 1
        s.append(s.popleft())
    return answer
