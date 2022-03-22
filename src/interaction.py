from tkinter import filedialog as fd


class Interaction:
    def __init__(self, control_unit, gpr_and_ixr, other_machine_registers, switch, function_buttons):
        self.control_unit = control_unit
        self.gpr_and_ixr = gpr_and_ixr
        self.other_machine_registers = other_machine_registers
        self.switch = switch
        self.function_buttons = function_buttons

    def load_to_register(self, register_name):
        instruction = self.switch.get_switch()
        gpr_dict = {
            "GPR0": "00",
            "GPR1": "01",
            "GPR2": "10",
            "GPR3": "11"
        }
        ixr_dict = {
            "IXR1": "01",
            "IXR2": "10",
            "IXR3": "11"
        }
        if register_name in gpr_dict.keys():
            for register_str, register in gpr_dict.items():
                if register_str == register_name:
                    self.control_unit.components.gpr_setter(register, instruction)
                    self.gpr_and_ixr.on_change(register_str, self.control_unit.components.gpr_getter(register))
        elif register_name in ixr_dict.keys():
            for register_str, register in ixr_dict.items():
                if register_str == register_name:
                    self.control_unit.components.ixr_setter(register, instruction)
                    self.gpr_and_ixr.on_change(register_str, self.control_unit.components.ixr_getter(register))
        elif register_name == "PC":
            instruction = instruction[-5:]
            self.control_unit.components.pc = instruction
            self.other_machine_registers.on_change("PC", self.control_unit.components.pc)
        elif register_name == "MAR":
            instruction = instruction[-5:]
            self.control_unit.components.mar = instruction
            self.other_machine_registers.on_change("MAR", self.control_unit.components.mar)
        elif register_name == "MBR":
            self.control_unit.components.mbr = instruction
            self.other_machine_registers.on_change("MBR", self.control_unit.components.mbr)

    def init(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/Users/ygao1/machine_simulator/test',
            filetypes=filetypes)

        dataframe = {}

        with open(filename, 'r') as f:
            for line in f.readlines():
                address, value = line.split(" ")
                address = bin(int(address, 16))[2:].zfill(16)
                value = bin(int(value, 16))[2:].zfill(16)
                dataframe[address] = value

        for location, value in dataframe.items():
            self.control_unit.components.memory.set_memory(location, value)
