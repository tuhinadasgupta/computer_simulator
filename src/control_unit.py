################################################################################
# Instruction Type:
#
# 1. Halt instruction:                          000000 -- -- - 00000
#
# 2. Trap instruction:                          011000 -- -- - 00000
#
# 3. Load/Store instruction:                     xxxxxx xx xx x xxxxx
#                                               Opcode R  IX I Address
#
# 3. Transfer instruction:                       xxxxxx xx [xx] [x] xxxxx
#                                               Opcode R   IX   I  Address
#
# 4. Immediate instruction:                      xxxxxx xx -- - xxxxx
#                                               Opcode R  -- - immed
#
# 5. Arithmetic and Logical instruction:         xxxxxx xx xx - -----
#                                               Opcode Rx Ry - -----
#
# 5. Shift and Rotate instruction:              xxxxxx xx x    x   -- xxxx
#                                               Opcode R  A/L  L/R -- Count
#
# 6. IO operation instruction:                   xxxxxx xx -- - xxxxx
#                                               Opcode R  -- - DevID
################################################################################


from alu import ALU
from components import Components


class ControlUnit:
    def __init__(self) -> None:
        self.alu = ALU()
        self.components = Components()
        self.instructions = {
            0: self.HLT,
            1: self.LDR,
            2: self.STR,
            3: self.LDA,
            4: self.AMR,
            5: self.SMR,
            6: self.AIR,
            7: self.SIR,
            10: self.JZ,
            11: self.JNE,
            12: self.JCC,
            13: self.JMA,
            14: self.JSR,
            15: self.RFS,
            16: self.SOB,
            17: self.JGE,
            20: self.MLT,
            21: self.DVD,
            22: self.TRR,
            23: self.AND,
            24: self.ORR,
            25: self.NOT,
            31: self.SRC,
            32: self.RRC,
            41: self.LDX,
            42: self.STX,
            61: self.IN,
            62: self.OUT,
            63: self.CHK,
        }

    # calculate effective address
    def _calculate_ea(self, instruction):
        if instruction[8:10] == "00":
            ea = instruction[11:16]
        else:
            if self.components.ixr_getter(instruction[8:10]) is not None:
                ea = bin(int(instruction[11:16], 2) +
                         int(self.components.ixr_getter(instruction[8:10]), 2))[2:].zfill(5)
            else:
                ea = instruction[11:16]
        ea = ea.zfill(16)
        if instruction[10] == "1" and ea in self.components.memory.get_memory_location():
            ea = self.components.memory.get_memory(ea)
        return ea

    def get_location(self, instruction):
        return self._calculate_ea(instruction)

    def HLT(self, instruction):
        print("halt")

    def LDR(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        value = self.components.memory.get_memory(ea)
        self.components.gpr_setter(r, value)

    def STR(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        value = self.components.gpr_getter(r)
        print(ea + " " + value)
        self.components.memory.set_memory(ea, value)

    def LDA(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        self.components.gpr_setter(r, ea)

    def AMR(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        x = self.components.gpr_getter(r)
        y = self.components.memory.get_memory(ea)
        value = self.alu.add(x, y)
        if value is not None:
            self.components.gpr_setter(r, value)
        else:
            # TODO Halt the program
            pass

    def SMR(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        x = self.components.gpr_getter(r)
        y = self.components.memory.get_memory(ea)
        value = self.alu.sub(x, y)
        if value is not None:
            self.components.gpr_setter(r, value)
        else:
            # TODO Halt the program
            pass

    def AIR(self, instruction):
        immed = instruction[11:16]
        r = instruction[6:8]
        x = self.components.gpr_getter(r)
        value = self.alu.add(x, immed)
        if value is not None:
            self.components.gpr_setter(r, value)
        else:
            # TODO Halt the program
            pass

    def SIR(self, instruction):
        immed = instruction[11:16]
        r = instruction[6:8]
        x = self.components.gpr_getter(r)
        value = self.alu.sub(x, immed)
        if value is not None:
            self.components.gpr_setter(r, value)
        else:
            # TODO Halt the program
            pass

    def JZ(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        value = int(self.components.gpr_getter(r))
        if value == 0:
            self.components.pc = ea
        else:
            pc = bin(int(self.components.pc, 2) + 1)[2:].zfill(12)
            self.components.pc = pc

    def JNE(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        value = int(self.components.gpr_getter(r))
        if value != 0:
            self.components.pc = ea
        else:
            pc = bin(int(self.components.pc, 2) + 1)[2:].zfill(12)
            self.components.pc = pc

    def JCC(self, instruction):
        ea = self._calculate_ea(instruction)
        ix = int(instruction[6:8], 2)
        value = self.alu.get_cc()[ix]
        if value == 1:
            self.components.pc = ea
        else:
            pc = bin(int(self.components.pc, 2) + 1)[2:].zfill(12)
            self.components.pc = pc

    def JMA(self, instruction):
        ea = self._calculate_ea(instruction)
        self.components.pc = ea

    def JSR(self, instruction):
        ea = self._calculate_ea(instruction)
        r = "11"
        value = bin(int(self.components.pc, 2) + 1)[2:].zfill(16)
        self.components.gpr_setter(r, value)
        self.components.pc = ea

    def RFS(self, instruction):
        immed = instruction[11:16]
        r0 = "00"
        r3 = "11"
        value = self.components.gpr_getter(r3)
        self.components.gpr_setter(r0, immed)
        self.components.pc = value

    def SOB(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        value = int(self.components.gpr_getter(r)) - 1
        value_bin = bin(value)[2:].zfill(16)
        self.components.gpr_setter(r, value_bin)
        if value > 0:
            self.components.pc = ea
        else:
            pc = bin(int(self.components.pc, 2) + 1)[2:].zfill(12)
            self.components.pc = pc

    def JGE(self, instruction):
        ea = self._calculate_ea(instruction)
        r = instruction[6:8]
        value = self.components.gpr_getter(r)
        if value >= 0:
            self.components.pc = ea
        else:
            pc = bin(int(self.components.pc, 2) + 1)[2:].zfill(12)
            self.components.pc = pc

    def MLT(self, instruction):
        rx = instruction[6:8]
        ry = instruction[8:10]
        valid_gpr = ["00", "01", "10"]
        if rx in valid_gpr and ry in valid_gpr:
            rx_plus_one = bin(int(rx, 2)+1)[2:].zfill(2)
            x = self.components.gpr_getter(rx)
            y = self.components.gpr_getter(ry)
            if self.alu.mlt(x, y) is not None:
                value_h, value_l = self.alu.mlt(x, y)
                self.components.gpr_setter(rx, value_h)
                self.components.gpr_setter(rx_plus_one, value_l)
            else:
                # TODO: Halt the program
                pass
        else:
            # TODO: set the trap code
            pass

    def DVD(self, instruction):
        rx = instruction[6:8]
        ry = instruction[8:10]
        valid_gpr = ["00", "01", "10"]
        if rx in valid_gpr and ry in valid_gpr:
            rx_plus_one = bin(int(rx, 2)+1)[2:].zfill(2)
            x = self.components.gpr_getter(rx)
            y = self.components.gpr_getter(ry)
            if self.alu.div(x, y) is not None:
                value_quotient, value_remainder = self.alu.div(x, y)
                self.components.gpr_setter(rx, value_quotient)
                self.components.gpr_setter(rx_plus_one, value_remainder)
            else:
                # TODO: Halt the program
                pass
        else:
            # TODO: set the trap code
            pass

    def TRR(self, instruction):
        rx = instruction[6:8]
        ry = instruction[8:10]
        x = self.components.gpr_getter(rx)
        y = self.components.gpr_getter(ry)
        if self.alu.is_equal(x, y):
            self.alu.set_cc("EQUALORNOT")
        else:
            self.alu.reset_cc("EQUALORNOT")

    def AND(self, instruction):
        rx = instruction[6:8]
        ry = instruction[8:10]
        x = self.components.gpr_getter(rx)
        y = self.components.gpr_getter(ry)
        value = self.alu.logical_and(x, y)
        self.components.gpr_setter(rx, value)

    def ORR(self, instruction):
        rx = instruction[6:8]
        ry = instruction[8:10]
        x = self.components.gpr_getter(rx)
        y = self.components.gpr_getter(ry)
        value = self.alu.logical_or(x, y)
        self.components.gpr_setter(rx, value)

    def NOT(self, instruction):
        rx = instruction[6:8]
        x = self.components.gpr_getter(rx)
        value = self.alu.logical_not(x)
        self.components.gpr_setter(rx, value)

    def SRC(self, instruction):
        r = instruction[6:8]
        l_r = instruction[9]
        a_l = instruction[8]
        count = instruction[12:16]
        value = self.components.gpr_getter(r)
        value_shifted = self.alu.shift(value, count, l_r, a_l)
        self.components.gpr_setter(r, value_shifted)

    def RRC(self, instruction):
        r = instruction[6:8]
        l_r = instruction[9]
        count = instruction[12:16]
        value = self.components.gpr_getter(r)
        value_rotated = self.alu.rotate(value, count, l_r)
        self.components.gpr_setter(r, value_rotated)

    def LDX(self, instruction):
        ea = self._calculate_ea(instruction)
        ixr = instruction[8:10]
        value = self.components.memory.get_memory(ea)
        self.components.ixr_setter(ixr, value)

    def STX(self, instruction):
        ea = self._calculate_ea(instruction)
        ixr = instruction[8:10]
        value = self.components.ixr_getter(ixr)
        self.components.memory.set_memory(ea, value)

    # TODO: all about devices.
    def IN(self, instruction):
        r = instruction[6:8]
        device_id = int(instruction[11:16], 2)
        if device_id == 0:
            value = self.components.devices.keyboard.zfill(16)
            self.components.gpr_setter(r, value)
        elif device_id == 2:
            value = self.components.devices.card_reader.zfill(16)
            self.components.gpr_setter(r, value)
        else:
            value = self.components.devices.get_other_device(device_id)
            self.components.gpr_setter(r, value)

    def OUT(self, instruction):
        r = instruction[6:8]
        value = self.components.gpr_getter(r)
        device_id = int(instruction[11:16], 2)
        if device_id == 1:
            self.components.devices.printer = value
        else:
            self.components.devices.set_other_device(device_id, value)

    def CHK(self, instruction):
        r = instruction[6:8]
        device_id = int(instruction[11:16], 2)
        if 0 <= device_id <= 31:
            self.components.gpr_setter(r, "1")
        else:
            self.components.gpr_setter(r, "0")

    def instruction_decoder(self, instruction):
        # ea = self._calculate_ea(instruction)
        opcode = int(oct(int(instruction[:6], 2))[2:])
        self.instructions.get(opcode)(instruction)

    def reset(self):
        self.components.reset()
        self.alu.reset_cc("OVERFLOW", "UNDERFLOW", "DIVZERO", "EQUALORNOT")

    def test(self):
        self.instruction_decoder("1000010010101000")
        print("done")