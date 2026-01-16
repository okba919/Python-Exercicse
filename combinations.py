import math

n = int(input("Enter total number of elements n: "))
k = int(input("Enter number of elements to choose k: "))

result = math.comb(n, k)
print(f"Number of ways to choose {k} from {n} is: {result}")