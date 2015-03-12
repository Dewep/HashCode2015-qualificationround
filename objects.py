__author__ = 'Steven'


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