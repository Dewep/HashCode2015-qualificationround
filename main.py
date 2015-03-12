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



with open("output.txt", "w") as text_file:
    for s in servers:
        if s._x == -1:
            print("x", file=text_file)
        else:
            print("%d %d %d" % (s._y, s._x, s._group), file=text_file)
