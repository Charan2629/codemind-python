def int_reverser(test):
    if test >= 0:
        answer = int(str(test)[::-1])
    else:
        answer = -int(str(-test)[::-1])
    if -2**31 <= answer <= 2**31 - 1:
        return answer
    else:
        return 0
test=int(input())
print(int_reverser(test))