def check_luckiness(N):
    return "lucky" if N % 7 == 0 else "unlucky"


N = int(input())
result = check_luckiness(N)
print(result)
