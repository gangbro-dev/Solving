import sys
sys.stdin = open('sample_input.txt')

def heappush(heap, n):
    heap.append(n)
    node = len(heap) - 1
    while node > 1:
        if heap[node] < heap[node//2]:
            heap[node], heap[node//2] = heap[node//2], heap[node]
            node //= 2
        else:
            break
T = int(input())

for Tc in range(1, T+1):
    N = int(input())
    binary_heap = [0]
    data = tuple(map(int, input().split()))
    for i in data:
        heappush(binary_heap, i)

    node = len(binary_heap) - 1
    ans = 0

    while node > 1:
        ans += binary_heap[node//2]
        node //= 2

    print(f'#{Tc} {ans}')
