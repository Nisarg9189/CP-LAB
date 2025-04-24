import random
from collections import deque
queue = deque()
for ele in range(4):
    a = random.randint(1,10)
    queue.append(a)
print(queue)
queue.popleft()
print(queue)
