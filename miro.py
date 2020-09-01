#4875 미로
howmany = int(input())
for i in range(1,howmany+1):
    howbig = int(input())
    map = [list(map(int,list(input()))) for _ in range(howbig)]
    print(map)