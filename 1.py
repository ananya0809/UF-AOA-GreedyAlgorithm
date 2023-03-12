def max_no_of_house_painted(n, m, house):
  count = 0
  marker = 0
  result = []
  for i in range(1, n+1):
    while marker < m and house[marker][0]<=i:
      if house[marker][1]>=i:
        # print(marker+1, house[marker])
        result.append(marker+1)
        count+=1
        marker+=1
        break
      marker+=1
  return result

n, m = map(int, input().split())
house = [tuple(map(int, input().split())) for _ in range(m)]
house.sort(key=lambda h: (h[0],h[1]))
result = max_no_of_house_painted(n, m, house)
print(' '.join(map(str, result)))