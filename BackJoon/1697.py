import sys

def BFS(start, destination):
    visit = [False for i in range(200000)]
    cnt = 0

    if start > destination:
        return start - destination

    if start == destination:
        return cnt
    
    if not start:
        start = 1
        cnt += 1
        if start == destination:
            return cnt

    visit[start] = -1
    now = [start]
    next = []

    while True:
        cnt += 1

        for i in now:
            if not visit[i+1]:
                visit[i+1] = cnt
                next.append(i+1)
            
            if not i:
                pass
            elif not visit[i-1]:    
                visit[i-1] = cnt
                next.append(i-1)

            if i*2 > 100000:
                pass
            elif not visit[i*2]:    
                visit[i*2] = cnt
                next.append(i*2)
        
        now = next[:]
        next.clear()
        
        if visit[destination]:
            break
    
    return cnt

N, K = map(int, sys.stdin.readline().split())

print(BFS(N, K))
