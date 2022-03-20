import tkinter as tk
import frames


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Machine Simulator")
        self.resizable(False, False)

        self.gpr_and_ixr = frames.GPR_AND_IXR(self)
        self.gpr_and_ixr.grid(column=0, row=0, padx="10", pady="10")

        self.other_machine_registers = frames.OTHER_MACHINE_REGISTERS(self)
        self.other_machine_registers.grid(column=1, row=0, padx="10", pady="10")

        self.switch = frames.SWITCH(self)
        self.switch.grid(column=0, row=1, padx="10", pady="10")

        self.function_buttons = frames.FUNCTION_BUTTONS(self)
        self.function_buttons.grid(column=1, row=1, padx="10", pady="10")


if __name__ == "__main__":
    app = App()
    app.mainloop()
    