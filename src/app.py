import tkinter as tk
from frames import *
from control_unit import ControlUnit
from interaction import Interaction


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Machine Simulator")
        self.resizable(False, False)

        gpr_and_ixr = GPR_AND_IXR(self)
        gpr_and_ixr.grid(column=0, row=0, padx="10", pady="10")

        other_machine_registers = OTHER_MACHINE_REGISTERS(self)
        other_machine_registers.grid(column=1, row=0, padx="10", pady="10")

        switch = SWITCH(self)
        switch.grid(column=0, row=1, padx="10", pady="10")

        function_buttons = FUNCTION_BUTTONS(self)
        function_buttons.grid(column=1, row=1, padx="10", pady="10")

        control_unit = ControlUnit()
        interaction = Interaction(
            control_unit, gpr_and_ixr, other_machine_registers, switch, function_buttons)

        gpr_and_ixr.set_controller(interaction)
        other_machine_registers.set_controller(interaction)
        switch.set_controller(interaction)
        function_buttons.set_controller(interaction)


if __name__ == "__main__":
    app = App()
    app.mainloop()
