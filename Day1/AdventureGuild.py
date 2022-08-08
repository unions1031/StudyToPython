'''input은 N명 // 공포도 X 모험가 -> X명 이상 그룹에 참여'''\

N = int(input())
X = list(map(int, input().split()))
X.sort()

count = 0
result = 0

for i in X:
  count += 1
  if count >= i:
    result += 1
    count = 0


print(count)