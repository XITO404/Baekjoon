a, b = map(int, input().split())
large = max(a, b)
small = min(a, b)

s = (large+small)/2 * (large+1-small)
print(int(s))
