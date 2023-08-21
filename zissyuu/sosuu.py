num = int(input("自然数を入力してください: "))
if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
    print(f"{num} は素数です。")
else:
    print(f"{num} は素数ではありません。")
