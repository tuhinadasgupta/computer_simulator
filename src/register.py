############################################################
# class for registers like gpr, ixr, mar, and mbr...
# have two initial values ---- size and value
# size: size of the register
# value: value that register holds currently.
# provide the basic methods like get and set...
############################################################


class Register:
    def __init__(self, size, value=None) -> None:
        self._size = size
        self._value = value


    @property
    def value(self):
        return self._value
    

    @value.setter
    def value(self, value):
        self._value = value

    
    @property
    def size(self):
        return self._size
    

    @size.setter
    def size(self, size):
        self._size = size
 