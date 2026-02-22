# 1
n = int(input())
for i in range(1, n + 1):
    print(i * i)

# 2
n = int(input())
for i in range(1, n + 1):
    print(i * i * i)

# 3
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i * i
print(s)

# 4
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i * i * i
print(s)

# 5
n = int(input())
for i in range(1, n + 1):
    if i * i > n:
        break
    print(i * i)
