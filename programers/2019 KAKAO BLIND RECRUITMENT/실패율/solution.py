def solution(N, stages):
    reached = [0] * (N + 2)
    for i in stages:
        reached[i] += 1
    blocked = reached[:]
    for i in range(N+1, 1, -1):
        reached[i-1] = blocked[i-1] + reached[i]
    rate = [0] * (N + 1)
    rate[0] = -1
    for i in range(1, N+1):
        if reached[i]:
            rate[i] = blocked[i] / reached[i]

    answer = []
    while len(answer) < N:
        i = rate.index(max(rate))
        answer.append(i)
        rate[i] = -1

    return answer
