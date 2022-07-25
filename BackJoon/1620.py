#pypy
N, M = map(int, input().split())
pokemon_book = []
problem = []

for i in range(N):
    pokemon_book.append(input())
for i in range(M):
    problem.append(input())

for i in range(M):
    if ord(problem[i][0]) < 58:
        print(pokemon_book[int(problem[i])-1])
    else:
        print(pokemon_book.index(problem[i])+1)
