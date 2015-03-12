__author__ = 'Steven'


# 0 dispo
# 1 indispo
# 2 serveur

class Datacenter(object):
    def __init__(self, rows, cols):
        self._map = []
        self._rows = rows
        self._cols = cols
        for i in range(0, rows):
            self._map.append([0 for i in range(0, cols)])

        print("Rows: %s" % len(self._map))


    def setAvailability(self, x, y):
        self._map[y][x] = 1

    def showMap(self):
        print("lines: %s" % (len(self._map)))
        for line in self._map:
            print("%s: %s" % (len(line), "".join([str(o) for o in line])))

    def isEmpty(self):
        ret = 0
        for line in self._map:
            ret += line.count(0)
        return ret

    def storeInLine(self, line, server):
        s = "%0*d" % (server._size, 0)
        print(s)
        line_str = "".join([str(o) for o in self._map[line]])
        pos = line_str.find(s)
        if pos >= 0:
            for i in range(0, server._size):
                if self._map[line][pos + i] != 0:
                    raise Exception("Euh !!! line(%s), pos(%s): " % (line, pos + i))
                self._map[line][pos + i] = 2
            server._x = pos
            server._y = line
            return True
        return False




class Server(object):
    def __init__(self, line, size, power):
        self._x = -1
        self._y = -1
        self._group = -1
        self._size = int(size)
        self._power = int(power)
        self._line = int(line)

    def __str__(self):
        return "%s: x(%s), y(%s), group(%s), ratio(%s), power(%s), size(%s)" % (self._line, self._x, self._y, self._group, self.getPerf(), self._power, self._size)

    def setPosXY(self, x, y):
        self._x = x
        self._y = y


    def getPerf(self):
        return self._power / self._size



def guaranteedCapacity(datacenter, servers):
    rows = []
    for i in range(0, datacenter._rows):
        rows.append(999)
    for s in servers:
        if s._x != -1:
            rows[s._y] = min(rows[s._y], s._power)
    return min(*rows)
