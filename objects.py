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



class Server(object):
    def __init__(self, line, size, power):
        self._x = -1
        self._y = -1
        self._group = -1
        self._size = int(size)
        self._power = int(power)
        self._line = int(line)


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
