#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

for a in range(20):
    print(a + 1)

mil = list(range(1000000) + 1)

coils = list(range(300))

print("{} and the max is {}".format(min(mil), max(mil)))

for a in range(1, 20, 3):
    print(a)

theThrees = list(range(3, 30, 3))
for a in theThrees:
    print("the threes are\n")
    print(a)

cubesAre = [a**3 for a in range(10)]
for i in cubesAre:
    print("the cubes 1 to 10 : {}".format(i))
