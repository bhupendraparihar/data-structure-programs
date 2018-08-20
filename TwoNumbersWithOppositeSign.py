#XOR operation of two opposite sign nubmer is always negative
def isOppositeSign1(a,b):
  return a ^ b < 0

def isOppositeSign2(a,b):
  return (a > 0 and b < 0) if (a > b) else (a < 0 and b > 0)

print(isOppositeSign2(2,3))
print(isOppositeSign2(2,-3))
print(isOppositeSign2(-2,3))
print(isOppositeSign2(-2,-33))
