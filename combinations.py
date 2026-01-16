def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def comb(n, k):
    return fact(n) // (fact(k) * fact(n - k))

n = int(input("Enter total number of elements n: "))
k = int(input("Enter number of elements to choose k: "))

print("Number of ways to choose", k, "from", n, "is:", comb(n, k))