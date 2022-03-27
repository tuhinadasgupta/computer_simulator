from tkinter import filedialog as fd


class Interaction:
    def __init__(self, control_unit, gpr_and_ixr, other_machine_registers, switch, function_buttons,
                 printer_and_keyboard, field_engineering_console):
        self.control_unit = control_unit
        self.gpr_and_ixr = gpr_and_ixr
        self.other_machine_registers = other_machine_registers
        self.switch = switch
        self.function_buttons = function_buttons
        self.printer_and_keyboard = printer_and_keyboard
        self.field_engineering_console = field_engineering_console

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
                    on_change_dict = {
                        register_str: self.control_unit.components.gpr_getter(register)
                    }
                    self.gpr_and_ixr.on_change(on_change_dict)
        elif register_name in ixr_dict.keys():
            for register_str, register in ixr_dict.items():
                if register_str == register_name:
                    self.control_unit.components.ixr_setter(register, instruction)
                    on_change_dict = {
                        register_str: self.control_unit.components.ixr_getter(register)
                    }
                    self.gpr_and_ixr.on_change(on_change_dict)
        elif register_name == "PC":
            instruction = instruction[-12:]
            self.control_unit.components.pc = instruction
            on_change_dict = {
                "PC": self.control_unit.components.pc
            }
            self.other_machine_registers.on_change(on_change_dict)
            self.field_engineering_console.load_to_pc(self.control_unit.components.pc)
        elif register_name == "MAR":
            instruction = instruction[-12:]
            self.control_unit.components.mar = instruction
            on_change_dict = {
                "MAR": self.control_unit.components.mar
            }
            self.other_machine_registers.on_change(on_change_dict)
        elif register_name == "MBR":
            self.control_unit.components.mbr = instruction
            on_change_dict = {
                "MBR": self.control_unit.components.mbr
            }
            self.other_machine_registers.on_change(on_change_dict)

    def store_and_store_plus(self, option_str):
        if self.control_unit.components.mar and self.control_unit.components.mbr:
            location = self.control_unit.components.mar.zfill(16)
            value = self.control_unit.components.mbr
            self.control_unit.components.memory.set_memory(location, value)
            if option_str == "S+":
                location = bin(int(self.control_unit.components.mar, 2) + 1)[2:].zfill(12)
                self.control_unit.components.mar = location
                on_change_dict = {
                    "MAR": self.control_unit.components.mar
                }
                self.other_machine_registers.on_change(on_change_dict)
        # TODO: either mar or mbr is None, halt.
        else:
            print("none")
            pass

    def load(self):
        if self.control_unit.components.mar is not None:
            location = self.control_unit.components.mar.zfill(16)
            value = self.control_unit.components.memory.get_memory(location)
            self.control_unit.components.mbr = value
            on_change_dict = {
                "MBR": self.control_unit.components.mbr
            }
            self.other_machine_registers.on_change(on_change_dict)
        # TODO: mar is None, halt.
        else:
            print("none")
            pass

    def single_step(self):
        self.function_buttons.run_canvas.configure(bg="yellow")
        self.function_buttons.halt_canvas.configure(bg="black")
        instruction_location = self.control_unit.components.pc.zfill(16)
        self.control_unit.components.ir = self.control_unit.components.memory.get_memory(instruction_location)
        instruction = self.control_unit.components.ir
        opcode = int(oct(int(instruction[:6], 2))[2:])

        if opcode == 61:
            input_value = self.printer_and_keyboard.keyboard_on_change()
            self.control_unit.components.devices.keyboard = input_value
        func_name = self.control_unit.instruction_decoder(instruction)

        on_change_dict_gpr_and_ixr = {
            "GPR0": self.control_unit.components.gpr_getter("00"),
            "GPR1": self.control_unit.components.gpr_getter("01"),
            "GPR2": self.control_unit.components.gpr_getter("10"),
            "GPR3": self.control_unit.components.gpr_getter("11"),
            "IXR1": self.control_unit.components.ixr_getter("01"),
            "IXR2": self.control_unit.components.ixr_getter("10"),
            "IXR3": self.control_unit.components.ixr_getter("11")
        }
        on_change_dict_other_machine_registers = {
            "PC": self.control_unit.components.pc,
            "MAR": self.control_unit.components.mar,
            "MBR": self.control_unit.components.mbr,
            "IR": self.control_unit.components.ir,
            "MFR": self.control_unit.components.mfr,
            # "CC": self.control_unit.alu.get_cc(),
        }
        on_change_dict_field_engineering_console = {
            "GPR0": self.control_unit.components.gpr_getter("00"),
            "GPR1": self.control_unit.components.gpr_getter("01"),
            "GPR2": self.control_unit.components.gpr_getter("10"),
            "GPR3": self.control_unit.components.gpr_getter("11"),
            "IXR1": self.control_unit.components.ixr_getter("01"),
            "IXR2": self.control_unit.components.ixr_getter("10"),
            "IXR3": self.control_unit.components.ixr_getter("11"),
            "MAR": self.control_unit.components.mar,
            "MBR": self.control_unit.components.mbr,
            "MFR": self.control_unit.components.mfr,
            # "CC": self.control_unit.alu.get_cc(),
        }

        self.gpr_and_ixr.on_change(on_change_dict_gpr_and_ixr)
        self.other_machine_registers.on_change(on_change_dict_other_machine_registers)
        self.field_engineering_console.ss_on_change(self.control_unit.components.pc,
                                                    on_change_dict_field_engineering_console, func_name)

        if func_name == "OUT":
            self.printer_and_keyboard.printer_on_change(self.control_unit.components.devices.printer)

    def run(self):
        while True:
            self.single_step()

    def init(self):
        self.control_unit.reset()
        on_change_dict = {
            "GPR0": self.control_unit.components.gpr_getter("00"),
            "GPR1": self.control_unit.components.gpr_getter("01"),
            "GPR2": self.control_unit.components.gpr_getter("10"),
            "GPR3": self.control_unit.components.gpr_getter("11"),
            "IXR1": self.control_unit.components.ixr_getter("01"),
            "IXR2": self.control_unit.components.ixr_getter("10"),
            "IXR3": self.control_unit.components.ixr_getter("11"),
            "PC": self.control_unit.components.pc,
            "MAR": self.control_unit.components.mar,
            "MBR": self.control_unit.components.mbr,
            "IR": self.control_unit.components.ir,
            "MFR": self.control_unit.components.mfr,
            "CC": self.control_unit.alu.get_cc(),
        }
        self.gpr_and_ixr.on_change(on_change_dict)
        self.other_machine_registers.on_change(on_change_dict)

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

        self.field_engineering_console.init_on_change()
