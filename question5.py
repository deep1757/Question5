T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    minus1 = a.count(-1)
    zero = a.count(0)
    one = a.count(1)
    mz = a.count(-1) + a.count(0)
    other = n - (a.count(-1) + a.count(0) + a.count(1))
    if zero == n or one == n or zero == n - one:
        print("yes")
    elif other <= 1 and (n - other) == one:
        print("yes")
    elif one >= 1 and mz == n - one:
        print("yes")
    else:
        print("no")