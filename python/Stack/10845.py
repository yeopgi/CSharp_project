import sys
N = int(sys.stdin.readline())
queue = list()


for _ in range(N):
    t = list(map(str,sys.stdin.readline().split()))
    if t[0] == 'push':
        queue.append(t[1])
    elif t[0] == 'pop':
        if len(queue) != 0:
            print(queue[0])
            queue.pop(0)
        else:
            print(-1)
    elif t[0] == 'size':
        print(len(queue))
    elif t[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif t[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue) != 0:
            print(queue[len(queue)-1])
        else:
            print(-1)

