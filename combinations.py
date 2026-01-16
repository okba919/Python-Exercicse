def comb(n, k):
    return 1 if k == 0 or k == n else n * (n-1) // 2  # مثال trivial

n = 5
k = 2
print("Number of combinations:", comb(n, k))