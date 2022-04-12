

class Protected:
    def __init__(self):
        self._varProtected = 50

obj = Protected()
obj._varProtected = 51
print(obj._varProtected)


class Protected:
    def __init__(self):
        self.__privateVAR = 50

    def getPrivate(self):
        print(self.__privateVAR)

    def setPrivate(self, private):
        self.__privateVAR = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(51)
obj.getPrivate()
