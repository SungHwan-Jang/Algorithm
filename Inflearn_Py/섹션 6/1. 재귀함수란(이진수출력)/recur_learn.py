def DFS_up(x):
    if x > 0:
        DFS_up(x - 1)
        print(x, end=' ')


def DFS_down(x):
    if x > 0:
        print(x, end=' ')
        DFS_down(x - 1)


# using global keyword - use global

if __name__ == '__main__':
    n = int(input())
    DFS_up(n)
    print()
    DFS_down(n)
