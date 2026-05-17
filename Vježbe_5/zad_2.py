def iteracije(N):
    broj = 5.0
    for _ in range(N):
        broj += 1 / 3
    for _ in range(N):
        broj -= 1 / 3
    return broj


for n in [200, 2000, 20000]:
    print(f" N = {n:5d}: {iteracije(n)}")
