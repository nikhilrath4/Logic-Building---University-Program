#Problem 13: Alphabet Pattern (Single Letter)

N = 5
for row in range(1, N+1):
    for col in range(0, row):
        print("A", end=" ")
    print()