#!/usr/bin/env python3
from datetime import datetime

from objects import Datacenter, Server, guaranteedCapacity

R, S, U, P, M = map(int, input().split())

servers = []
datacenter = Datacenter(R, S)

for i in range(0, U):
    y, x = map(int, input().split())
    datacenter.setAvailability(x, y)

datacenter.showMap()

for i in range(0, M):
    x, y = map(int, input().split())
    servers.append(Server(i, x, y))


sort = sorted(servers, reverse=True)

for s in sort:
    print(str(s))

#_round = 1000
_round = 1
while datacenter.isEmpty() > 0 and _round >= 0:

    for i in range(0, datacenter._rows):
        j = 0
        print(P)
        #import sys
        #sys.exit(1)
        if datacenter.storeInLine(i, sort[0], servers, P):
            del sort[j]
        else:
            j += 1
        if j == len(sort):
            print("try exhausted in this line")
            continue
        #print("store in %s: %s" % (i, ))
    _round -= 1

datacenter.showMap()
#sorted(servers, key=lambda o: o._line)

for s in servers:
    print(str(s))
datacenter.showMap()
print(guaranteedCapacity(datacenter, servers))


with open("output.txt", "w") as text_file:
    for s in servers:
        if s._x == -1:
            print("x", file=text_file)
        else:
            print("%d %d %d" % (s._y, s._x, s._group), file=text_file)
