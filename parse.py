#!/usr/bin/env python3

R, S, U, P, M = map(int, input().split())

indispo = []
servers = []

for i in range(0, U):
    x, y = map(int, input().split())
    indispo.append((x, y))

for i in range(0, M):
    x, y = map(int, input().split())
    servers.append((x, y))

print(R)
print(S)
print(U)
print(P)
print(M)

print(indispo)
print(servers)

sum1 = 0
sum2 = 0
for s in servers:
    sum1 += int(s[0])
    sum2 += int(s[1])

print(sum1)
print(sum2)
