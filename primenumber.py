#printing all prime upto n
import math
n=int(input())
print([i for i in range(2,n+1) if i not in [i  for i in range(2,n+1) for j in range(2,int(math.sqrt(i))+1) if i%j==0]])
