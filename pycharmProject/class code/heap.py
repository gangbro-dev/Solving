# 최대힙
# 힙에서 팝을 하면 최대힙은 최대값 또는 최소힙은 최솟값을 구할 수 있다.
# 힙에서는 루트 노드의 원소만을 삭제 할 수 있다.

def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가

    c = last
    p = c // 2      # 완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]: # 부모가 있고(root가 아니고, 부모 < 자식 인 경우
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def deq():
    global last
    temp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
        else:
            break
    return temp



heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

while last:
    print(deq())
