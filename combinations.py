def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter total number of elements n: "))
k = int(input("Enter number of elements to choose k: "))

result = fact(n) // (fact(k) * fact(n - k))
print(f"Number of ways to choose {k} from {n} is: {result}")