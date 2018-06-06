
class SetError(Exception):
    def __init__(self, w1, w2):
        self.__message = w1 + " nie może być tam gdzie " + w2 + "!"

    def Message_Get(self):
        return self.__message

class DistanceError(Exception):
    def __init__(self):
        self.__message = "Start i Koniec zdecydowanie za blisko!"

    def Message_Get(self):
        return self.__message