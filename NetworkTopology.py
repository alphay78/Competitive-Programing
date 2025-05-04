n, m = map(int, input().split())
deg = [0] * (n + 1)  # 1-based indexing

for _ in range(m):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1

# remove the unused 0th index
deg = deg[1:]

if m == n - 1:
    # Possible star or bus
    if deg.count(1) == n - 1 and deg.count(n - 1) == 1:
        print("star topology")
    elif deg.count(1) == 2 and deg.count(2) == n - 2:
        print("bus topology")
    else:
        print("unknown topology")
elif m == n:
    # Possible ring
    if deg.count(2) == n:
        print("ring topology")
    else:
        print("unknown topology")
else:
    print("unknown topology")
