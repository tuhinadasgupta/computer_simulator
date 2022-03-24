from frames import *
from control_unit import ControlUnit
from interaction import Interaction


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Machine Simulator")
        self.resizable(False, False)

        gpr_and_ixr = GprAndIxr(self)
        gpr_and_ixr.grid(column=0, row=0, padx="10", pady="10")

        other_machine_registers = OtherMachineRegisters(self)
        other_machine_registers.grid(column=1, row=0, padx="10", pady="10")

        switch = SWITCH(self)
        switch.grid(column=0, row=1, padx="10", pady="10")

        function_buttons = FunctionButtons(self)
        function_buttons.grid(column=1, row=1, padx="10", pady="10")

        printer_and_keyboard = PrinterAndKeyboard(self)
        printer_and_keyboard.grid(column=0, row=2, padx="10", pady="10", columnspan=2)

        field_engineering_console = FieldEngineeringConsole(self)
        field_engineering_console.grid(column=2, row=0, ipadx=10, rowspan=3)

        control_unit = ControlUnit()
        interaction = Interaction(
            control_unit, gpr_and_ixr, other_machine_registers, switch, function_buttons, printer_and_keyboard,
            field_engineering_console)

        gpr_and_ixr.set_controller(interaction)
        other_machine_registers.set_controller(interaction)
        switch.set_controller(interaction)
        function_buttons.set_controller(interaction)
        printer_and_keyboard.set_controller(interaction)
        field_engineering_console.set_controller(interaction)


if __name__ == "__main__":
    app = App()
    app.mainloop()
