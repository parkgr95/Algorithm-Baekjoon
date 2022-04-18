for _ in range(int(input())):
    w, h = map(int, input().split())
    prison, prisoner, door, escape = [], [], [], []
    for i in range(w):
        arr = list(input())
        prison.append(arr)
        for j in range(h):
            if prison[i][j] == '#':
                if i == 0 or i == w - 1 or j == 0 or j == h - 1:
                    escape.append((i, j))
                else:
                    door.append((i, j))
            elif prison[i][j] == '$':
                prisoner.append((i, j))
            elif prison[i][j] == '.':
                if i == 0 or i == w - 1 or j == 0 or j == h - 1:
                    escape.append((i, j))
    print(prisoner, door, escape)
    print()