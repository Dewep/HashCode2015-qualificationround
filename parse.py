#!/usr/bin/env python3

R, S, U, P, M = input().split()
R = int(R)
S = int(S)
U = int(U)
P = int(P)
M = int(M)

indispo = []
servers = []
map = list()

for i in range(0, U):
    indispo.append(input().split())

for i in range(0, M):
    servers.append(input().split())

print(R)
print(S)
print(U)
print(P)
print(M)

print(indispo)
print(servers)
