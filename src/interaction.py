from control_unit import CU
from frames import *


class Interaction:
    def __init__(self, control_unit, gpr_and_ixr, other_machine_registers, switch, function_buttons):
        self.control_unit = control_unit
        self.gpr_and_ixr = gpr_and_ixr
        self.other_machine_registers = other_machine_registers
        self.switch = switch
        self.function_buttons = function_buttons
