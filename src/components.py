from memory import Memory
from cache import Cache
from register import Register


class Components:
    # init objects for CPU and Memory
    def __init__(self) -> None:
        # Memory
        self.memory = Memory()

        # Cache
        self.cache = Cache()

        # CPU
        # general purpose register
        self._gpr = []
        for _ in range(4):
            self._gpr.append(Register(16))
        # index register
        self._ixr = []
        for _ in range(3):
            self._ixr.append(Register(16))
        # program counter
        self._pc = Register(12)
        # memory address register
        self._mar = Register(12)
        # memory buffer register
        self._mbr = Register(16)
        # memory fault register
        self._mfr = Register(4)
        # instruction register
        self._ir = Register(16)

    # getter and setter for gpr
    def gpr_getter(self, r):
        if r == "00":
            return self._gpr[0].value
        elif r == "01":
            return self._gpr[1].value
        elif r == "10":
            return self._gpr[2].value
        elif r == "11":
            return self._gpr[3].value

    def gpr_setter(self, r, value):
        value = value.zfill(16)
        if r == "00":
            self._gpr[0].value = value
        elif r == "01":
            self._gpr[1].value = value
        elif r == "10":
            self._gpr[2].value = value
        elif r == "11":
            self._gpr[3].value = value

    # getter and setter for ixr
    def ixr_getter(self, ix):
        if ix == "01":
            return self._ixr[0].value
        elif ix == "10":
            return self._ixr[1].value
        elif ix == "11":
            return self._ixr[2].value

    def ixr_setter(self, ix, value):
        value = value.zfill(16)
        if ix == "01":
            self._ixr[0].value = value
        elif ix == "10":
            self._ixr[1].value = value
        elif ix == "11":
            self._ixr[2].value = value

    # getter and setter for pc
    @property
    def pc(self):
        return self._pc.value

    @pc.setter
    def pc(self, pc):
        if pc is not None:
            pc = pc.zfill(12)
        self._pc.value = pc

    # getter and setter for mar
    @property
    def mar(self):
        return self._mar.value

    @mar.setter
    def mar(self, mar):
        if mar is not None:
            mar = mar.zfill(12)
        self._mar.value = mar

    # getter and setter for mbr
    @property
    def mbr(self):
        return self._mbr.value

    @mbr.setter
    def mbr(self, mbr):
        if mbr is not None:
            mbr = mbr.zfill(16)
        self._mbr.value = mbr

    # getter and setter for mfr
    @property
    def mfr(self):
        return self._mfr.value

    @mfr.setter
    def mfr(self, mfr):
        if mfr is not None:
            mfr = mfr.zfill(4)
        self._mfr.value = mfr

    # getter and setter for ir
    @property
    def ir(self):
        return self._ir.value

    @ir.setter
    def ir(self, ir):
        if ir is not None:
            ir = ir.zfill(16)
        self._ir.value = ir

    def reset(self):
        for gpr in self._gpr:
            gpr.value = None
        for ixr in self._ixr:
            ixr.value = None
        self.pc = None
        self.mar = None
        self.mbr = None
        self.ir = None
        self.mfr = None
        self.cache.clear_cache()
        self.memory.reset_memory()

    def test(self):
        print(self._mfr.size)
        for gpr in self.gpr:
            print(gpr)
        print("****************")
        for ixr in self.ixr:
            print(ixr)
