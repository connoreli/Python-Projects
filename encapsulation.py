

class Protected:
    def __init__(self):
        self._varProtected = 50

    def __init__(self):
        self.__privateVAR = 51

    def getPrivate(self):
        print(self.__privateVAR)

    def setPrivate(self, private):
        self.__privateVAR = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(53)
obj.getPrivate()
