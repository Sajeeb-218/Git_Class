def get_divisors(N):
    divisors = []
    for i in range(1, N+1):
        if N % i == 0:
            divisors.append(i)
    return divisors
N = int(input("Enter an integer: "))
divisors = get_divisors(N)
print(f"The divisors of {N} are: {divisors}")
