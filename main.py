#!/usr/bin/env python3

from objects import Datacenter, Server

R, S, U, P, M = map(int, input().split())

servers = []
datacenter = Datacenter(R, S)

for i in range(0, U):
    y, x = map(int, input().split())
    datacenter.setAvailability(x, y)

datacenter.showMap()

for i in range(0, M):
    y, x = map(int, input().split())
    servers.append(Server(i, x, y))



sum1 = 0
sum2 = 0
for s in servers:
    sum1 += int(s._size)
    sum2 += int(s._power)

print(sum1)
print(sum2)


#for s in servers:
#    if s.
#    print()
