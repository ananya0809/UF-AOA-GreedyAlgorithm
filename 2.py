import heapq

def max_no_of_house_painted(n, m, house):
    result = []
    priorityQueue = []
    j = 0

    for i in range(1, n+1):
        while house and house[0][0] <= i:
            startDay, endDay = house.pop(0)
            startDay = startDay * (-1)
            heapq.heappush(priorityQueue, ((-startDay,endDay),j+1))
            j = j + 1

        while priorityQueue:
            (startDay, endDay), index = heapq.heappop(priorityQueue)
            if endDay >= i:
                result.append(index)
                break

    return result


n, m = map(int, input().split())
house = [tuple(map(int, input().split())) for _ in range(m)]
house.sort(key=lambda h: (h[0],h[1]))
finalResult = max_no_of_house_painted(n, m, house)
print(' '.join(map(str, finalResult)))

