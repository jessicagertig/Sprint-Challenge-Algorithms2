#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)


b)
O(nlogn)

c)
O(n)

## Exercise II

We can assume that the floors will be in order, as that is normal.
1. middle floor = n//2
2. Check if egg is broken if dropped off middle floor.
3. If yes to broken off middle floor, next go through the floors below/less than middle floor from highest to lowest, until finding safe_floor = floor where egg is not broken:
return as f: safe_floor + 1
4. if not broken off middle floor, go through floor above/greater than middle floor, from lowest to highest, until finding unsafe_floor = floor where egg is broken (stop):
return as f: unsafe_floor 

def find_floor(n):
  mid = n//2
  if mid is egg broken true:
    for x in range(mid-1, 0):
      if x is egg broken false:
        return x + 1
  elif mid is egg broken false:
    for y in range(mid + 1, n+1):
      if y is egg broken true:
        return y

