class ALU:
    def __init__(self) -> None:
        # init condition code:
        # bit -> condition -> binary
        # 0 -> OVERFLOW -> 1000
        # 1 -> UNDERFLOW -> 0100
        # 2 -> DIVZERO -> 0010
        # 3 -> EQUALORNOT -> 0001
        self._condition_code = [0,0,0,0]


    def get_cc(self):
        return self._condition_code


    def set_cc(self, condition):
        if condition == "OVERFLOW":
            self._condition_code[0] = 1
        elif condition == "UNDERFLOW":
            self._condition_code[1] = 1
        elif condition == "DIVZERO":
            self._condition_code[2] = 1
        elif condition == "EQUALORNOT":
            self._condition_code[3] = 1

    
    def reset_cc(self, *argv):
        for condition in argv:
            if condition == "OVERFLOW":
                self._condition_code[0] = 0
            elif condition == "UNDERFLOW":
                self._condition_code[1] = 0
            elif condition == "DIVZERO":
                self._condition_code[2] = 0
            elif condition == "EQUALORNOT":
                self._condition_code[3] = 0


    # x and y are binary value
    # addition method:
    def add(self, x, y):
        # upper boundary 65535
        # lower boundary 0
        z = int(x, 2) + int(y, 2)
        if z > 65535:
            self.set_cc("OVERFLOW")
            return
        else:
            z = bin(z)[2:].zfill(16)
            return z
            


    # subtraction method:
    def sub(self, x, y):
        # upper boundary 65535
        # lower boundary 0
        z = int(x, 2) - int(y, 2)
        if z < 0:
            self.set_cc("UNDERFLOW")
            return
        else:
            z = bin(z)[2:].zfill(16)
            return z


    # multiplication method:
    def mlt(self, x, y):
        # upper boundary 4294967295
        # lower boundary 0
        z = int(x, 2) * int(y, 2)
        if z > 4294967295:
            self.set_cc("OVERFLOW")
            return
        else:
            z = bin(z)[2:].zfill(32)
            zh = z[0:16]
            zl = z[16:32]
            return zh, zl


    # division method:
    def div(self, x, y):
        # // -> Floor division, / -> division
        try:
            z_quotient = bin(int(x, 2) // int(y, 2))[2:].zfill(16)
            z_remainder = bin(int(x, 2) % int(y, 2))[2:].zfill(16)
            return z_quotient, z_remainder
        except ZeroDivisionError:
            # will return None
            self.set_cc("DIVZERO")
            

    # If two value is equal
    def is_equal(self, x, y):
        return True if x == y else False

    
    # logical and method:
    def logical_and(self, x, y):
        # ask for, or and not operator
        z = ''.join(str(int(i) & int(j))for i,j in zip(x, y)).zfill(16)
        # z = bin(int(x, 2) & int(y, 2))[2:].zfill(16)
        # lazy evaluation
        # d = bin(int(x,2) and int(y,2))
        return z

    
    # logical or method:
    def logical_or(self, x, y):
        z = ''.join(str(int(i) | int(j))for i,j in zip(x, y)).zfill(16)
        # z = bin(int(x,2) | int(y,2))[2:].zfill(16)
        # lazy evaluation
        # d = bin(int(x,2) or int(y,2))
        return z


    # logical not method:
    def logical_not(self, x):
        # z = bin(~int(x))
        res_int = []
        for i in x:
            res_int.append(not int(i))
        z = ''.join(str(int(i)) for i in res_int).zfill(16)
        return z

    
    # shift method:
    def shift(self, value, count, l_r, a_l):
        # Arithmetic Shift (a_l = 0)
        count = int(count, 2)
        if a_l == "0":
            # left (l_r =1)
            if l_r == "1":
                value = bin(int(value, 2) << count)[2:].zfill(16)
            # TODO
            # right (l_r = 0)
            elif l_r == "0":
                value = bin(int(value, 2) >> count)

        # Logical Shift (a_l = 1) 
        elif a_l == "1":
            # left (l_r =1)
            if l_r == "1":
                value = bin(int(value, 2) << count)[2:].zfill(16)
            # right (l_r = 0)
            elif l_r == "0":
                value = bin(int(value, 2) >> count)[2:].zfill(16)

            if int(value, 2) > 65535:
                self.set_cc("OVERFLOW")
                return
            else:
                return value


    # rotate method:
    def rotate(self, value, count, l_r):
        count = int(count, 2)
        value_list = list(value)
        # r = 10111010 count = 2
        # r_left = 10 r_right = 111010
        # left (l_r = 1) 
        if l_r == "1":
            value_list_left = value_list[0:count] 
            value_list_right = value_list[count:]
        # right (l_r = 0)
        elif l_r == "0":
            value_list_left = value_list[0:len(value_list)-count] 
            value_list_right = value_list[len(value_list)-count:]

        res = ''.join(value_list_right) + ''.join(value_list_left)
        res = res.zfill(16)
        return res
        