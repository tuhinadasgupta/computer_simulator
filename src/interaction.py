from tkinter import filedialog as fd


class Interaction:
    def __init__(self, control_unit, gpr_and_ixr, other_machine_registers, switch, function_buttons):
        self.control_unit = control_unit
        self.gpr_and_ixr = gpr_and_ixr
        self.other_machine_registers = other_machine_registers
        self.switch = switch
        self.function_buttons = function_buttons

    def init(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
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
