def most_frequent(List):
    return max(set(List), key = List.count)
n=int(input()) 
List = list(map(int,input().split()))
print(most_frequent(List))