def int_reverser(test):
    if test >= 0:
        answer = int(str(test)[::-1])
    else:
        answer = -int(str(-test)[::-1])
    return answer
test=int(input())
print(int_reverser(test))