import re
def ConvertListToStr(input):
    res = ""
    if len(input) == 0:
        return res
    for item in input:
        res += item
    pattern = re.compile(r'\s+')
    res = re.sub(pattern, '', res)
    return res

# 处理text() 合并因为\r\n导致的分割错误
def HandleTextList(input):
    i = 1
    while i < len(input):
        if input[i].startswith(('\r\n', '\n')):
            input[i-1] += input[i]
            del input[i]
        else:
            i = i+1
    return input