import re
def solution(myStr):
    split_values = re.split('[abc]', myStr)
    result = [value for value in split_values if value]
    return result if result else ["EMPTY"]