t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if '>' not in s or '<' not in s:
        print(n)
    else:
        count = 0
        for i in range(n):
            if s[i] == '-' or s[(i - 1 + n) % n] == '-':
                count += 1
        print(count)
