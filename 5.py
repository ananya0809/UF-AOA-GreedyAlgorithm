import heapq as hq #python built-in library for priority queue implementation using heap
  
class House: # define a class house for storing the index, startDate and endDate
    index: int
    start: int
    end: int
    
    def __init__(self, index: int, start: int, end: int) -> None:
        self.index = index
        self.start = start
        self.end = end
    
    def deadline(self) -> int: # this function finds the deadline with respect to the end date for all houses
        return self.end
    
    def __lt__(self, other): #method to compare between consecutive deadlines and find earliest deadline
        return self.deadline() < other.deadline()
          
    def can_be_painted(self, day) -> bool: # a house will be painted if it is available on the day that lies between its start and end date
        return day >= self.start and day <= self.end

# input
dataset = []
nm = input()
n = int(nm.split(" ")[0])
m = int(nm.split(" ")[1])
for i in range(1, m+1):
    temp = input()
    startDate = int(temp.split(" ")[0])
    endDate = int(temp.split(" ")[1])
    dataset.append(House(i, startDate, endDate))

list_house = []

for house in dataset:
    list_house.append((house.deadline(), house)) #m

hq.heapify(list_house)

day = 1

# output answer
output = []
# condition to check if the house should be popped from the queue of unpainted houses if it satisfies the criteria:
# house with shortest duration must be available between the start and end date if the current day lies within its availability - that can be painted
# if house is not available, it is anyhow popped and appended back into the queue after the next house is found that satisfies the criteria
# if the end date for the previously unavailable house is lesser than the current day, then it remains in the queue as an unpainted house
while day <= n and len(list_house) > 0: # m
    item = hq.heappop(list_house) # log m
    item_house = item[1]
    if item_house.can_be_painted(day):
        output.append(item_house.index)
        day += 1
    else:
        if (item_house.deadline() < day):
            day += 1
        list_house.append(item) # log m
print (' '.join(map(str,output)))

# Time Complexity: Theta(m + mlogm) = Theta(mlogm)