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

    def storeInLine(self, line, server, servers, nb_groups):
        s = "%0*d" % (server._size, 0)
        #print(s)
        line_str = "".join([str(o) for o in self._map[line]])
        pos = line_str.find(s)
        if pos >= 0:
            for i in range(0, server._size):
                if self._map[line][pos + i] != 0:
                    raise Exception("Euh !!! line(%s), pos(%s): " % (line, pos + i))
                self._map[line][pos + i] = 2
            server._x = pos
            server._y = line
            server._group = getLowestGroup(servers, nb_groups)
            # attribuer groupe
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

    def csv(self):
        return "%d;%d;%d;%d;%d;%d;%d" % (self._line, self._x, self._y, self._group, self.getPerf(), self._power, self._size)

    def setPosXY(self, x, y):
        self._x = x
        self._y = y

    def getPerf(self):
        return self._power / self._size

    def __cmp__(self, o):
        if self.getPerf() < o.getPerf():
            return -1
        if self.getPerf() > o.getPerf():
            return 1
        if self._size > o._size:
            return -1
        if self._size < o._size:
            return 1
        return 0
    def __lt__(self, other):
        return self.__cmp__(other) < 0
    def __gt__(self, other):
        return self.__cmp__(other) > 0
    def __eq__(self, other):
        return self.__cmp__(other) == 0
    def __le__(self, other):
        return self.__cmp__(other) <= 0
    def __ge__(self, other):
        return self.__cmp__(other) >= 0
    def __ne__(self, other):
        return self.__cmp__(other) != 0


def guaranteedCapacity(datacenter, servers):
    rows = []
    for i in range(0, datacenter._rows):
        rows.append(999)
    for s in servers:
        if s._x != -1:
            rows[s._y] = min(rows[s._y], s._power)
    return min(*rows)


def groupByGroup(servers, nb_groups):
    groups = []
    for i in range(0, nb_groups):
        groups.append([])
    for s in servers:
        if s._group != -1:
            groups[s._group].append(s)
    return groups


#def PowerByGroups(servers):
#    groups = {}
#    for
#    for s in servers:
#        if s._group != -1:
#            while len(groups) < s._group + 1:
#                groups.append([])
#            groups[s._group].append(s)
#    return groups

def getLowestGroup(servers, nb_groups):
    groups = groupByGroup(servers, nb_groups)
    lowest_group = 0
    lowest_value = 999999
    for i in range(0, nb_groups):
        value = 0
        for s in groups[i]:
            value += s._power
        if value < lowest_value:
            lowest_group = i
            lowest_value = value
    return lowest_group
