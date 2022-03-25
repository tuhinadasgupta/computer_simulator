import tkinter as tk
from tkinter import ttk


class GprAndIxr(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        # gpr0
        tk.Label(self, text="GPR 0").grid(column=0, row=0, sticky="w")
        self.gpr0 = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.gpr0.configure(state='disabled')
        self.gpr0.grid(column=1, row=0, padx="10")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("GPR0")).grid(column=2, row=0)

        # gpr1
        tk.Label(self, text="GPR 1").grid(column=0, row=1, sticky="w")
        self.gpr1 = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.gpr1.configure(state='disabled')
        self.gpr1.grid(column=1, row=1, padx="10")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("GPR1")).grid(column=2, row=1)

        # gpr2
        tk.Label(self, text="GPR 2").grid(column=0, row=2, sticky="w")
        self.gpr2 = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.gpr2.configure(state='disabled')
        self.gpr2.grid(column=1, row=2, padx="10")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("GPR2")).grid(column=2, row=2)

        # gpr3
        tk.Label(self, text="GPR 3").grid(column=0, row=3, sticky="w")
        self.gpr3 = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.gpr3.configure(state='disabled')
        self.gpr3.grid(column=1, row=3, padx="10")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("GPR3")).grid(column=2, row=3)

        # ixr1
        tk.Label(self, text="IXR 1").grid(column=0, row=4, sticky="w")
        self.ixr1 = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.ixr1.configure(state='disabled')
        self.ixr1.grid(column=1, row=4, padx="10")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("IXR1")).grid(column=2, row=4)

        # ixr2
        tk.Label(self, text="IXR 2").grid(column=0, row=5, sticky="w")
        self.ixr2 = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.ixr2.configure(state='disabled')
        self.ixr2.grid(column=1, row=5, padx="10")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("IXR2")).grid(column=2, row=5)

        # ixr3
        tk.Label(self, text="IXR 3").grid(column=0, row=6, sticky="w")
        self.ixr3 = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.ixr3.configure(state='disabled')
        self.ixr3.grid(column=1, row=6, padx="10")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("IXR3")).grid(column=2, row=6)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def load_to_register(self, register_name):
        if self.controller:
            self.controller.load_to_register(register_name)

    def on_change(self, on_change_dict):
        register_dict = {
            "GPR0": self.gpr0,
            "GPR1": self.gpr1,
            "GPR2": self.gpr2,
            "GPR3": self.gpr3,
            "IXR1": self.ixr1,
            "IXR2": self.ixr2,
            "IXR3": self.ixr3
        }
        for register_name, value in on_change_dict.items():
            if value is not None:
                value = " ".join(str(value))
                for register_str, register in register_dict.items():
                    if register_str == register_name:
                        register["state"] = "normal"
                        register.delete("1.0", "end")
                        register.insert("1.0", value)
                        register["state"] = "disabled"
            else:
                for register_str, register in register_dict.items():
                    if register_str == register_name:
                        register["state"] = "normal"
                        register.delete("1.0", "end")
                        register.insert("1.0", '')
                        register["state"] = "disabled"


class OtherMachineRegisters(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        # pc
        tk.Label(self, text="PC").grid(column=0, row=0, sticky="w")
        self.pc = tk.Text(self, width="24", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.pc.configure(state='disabled')
        self.pc.grid(column=1, row=0, padx="10", sticky="w")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("PC")).grid(column=2, row=0)

        # mar
        tk.Label(self, text="MAR").grid(column=0, row=1, sticky="w")
        self.mar = tk.Text(self, width="24", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.mar.configure(state='disabled')
        self.mar.grid(column=1, row=1, padx="10", sticky="w")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("MAR")).grid(column=2, row=1)

        # mbr
        tk.Label(self, text="MBR").grid(column=0, row=2, sticky="w")
        self.mbr = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.mbr.configure(state='disabled')
        self.mbr.grid(column=1, row=2, padx="10", sticky="w")
        tk.Button(self, text="LD", command=lambda: self.load_to_register("MBR")).grid(column=2, row=2)

        # ir
        tk.Label(self, text="IR").grid(column=0, row=3, sticky="w")
        self.ir = tk.Text(self, width="32", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.ir.configure(state='disabled')
        self.ir.grid(column=1, row=3, padx="10", sticky="w")

        # mfr
        tk.Label(self, text="MFR").grid(column=0, row=4, sticky="w")
        self.mfr = tk.Text(self, width="8", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.mfr.configure(state='disabled')
        self.mfr.grid(column=1, row=4, padx="10", sticky="w")

        # cc
        tk.Label(self, text="CC").grid(column=0, row=5, sticky="w")
        self.cc = tk.Text(self, width="4", height="1", padx=2, borderwidth=2, relief=tk.SUNKEN)
        self.cc.configure(state='disabled')
        self.cc.grid(column=1, row=5, padx="10", sticky="w")

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def load_to_register(self, register_name):
        if self.controller:
            self.controller.load_to_register(register_name)

    def on_change(self, on_change_dict):
        register_dict = {
            "PC": self.pc,
            "MAR": self.mar,
            "MBR": self.mbr,
            "IR": self.ir
        }
        for register_name, value in on_change_dict.items():
            if value is not None:
                value = " ".join(str(value))
                for register_str, register in register_dict.items():
                    if register_str == register_name:
                        register["state"] = "normal"
                        register.delete("1.0", "end")
                        register.insert("1.0", value)
                        register["state"] = "disabled"
            else:
                for register_str, register in register_dict.items():
                    if register_str == register_name:
                        register["state"] = "normal"
                        register.delete("1.0", "end")
                        register.insert("1.0", '')
                        register["state"] = "disabled"


class SWITCH(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        # opcode
        tk.Label(self, text="Operation").grid(column=0, row=0, sticky="S")
        self.opcode = ttk.Entry(self, width=10)
        self.opcode.grid(column=0, row=1, sticky="N")

        # r
        tk.Label(self, text="GPR").grid(column=1, row=0, sticky="S")
        self.r = ttk.Entry(self, width=6)
        self.r.grid(column=1, row=1, sticky="N")
        # gpr.bind("<FocusOut>", self.on_focus_out)

        # ixr
        tk.Label(self, text="IXR").grid(column=2, row=0, sticky="S")
        self.ixr = ttk.Entry(self, width=6)
        self.ixr.grid(column=2, row=1, sticky="N")
        # ixr.bind("<FocusOut>", self.on_focus_out)

        # i
        tk.Label(self, text="I").grid(column=3, row=0, sticky="S")
        self.i = ttk.Entry(self, width=4)
        self.i.grid(column=3, row=1, sticky="N")
        # i.bind("<FocusOut>", self.on_focus_out)

        # address
        ttk.Label(self, text="Address").grid(column=4, row=0, sticky="S")
        self.address = tk.Entry(self, width=8)
        self.address.grid(column=4, row=1, sticky="N")
        # address.bind("<FocusOut>", self.on_focus_out)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def get_switch(self):
        instruction = self.opcode.get() + \
                      self.r.get() + \
                      self.ixr.get() + \
                      self.i.get() + \
                      self.address.get()
        # TODO: add validation for invalid input.
        if self.controller:
            return instruction


class FunctionButtons(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        tk.Button(self, text="Store", width=5, command=self.store_and_store_plus).grid(column=0, row=0)
        tk.Button(self, text="S+", width=5, command=lambda: self.store_and_store_plus("S+")).grid(column=1, row=0)
        tk.Button(self, text="Load", width=5, command=self.load).grid(column=2, row=0)
        tk.Button(self, text="Init", width=5, command=self.init).grid(column=3, row=0)
        tk.Button(self, text="SS", width=5, command=self.single_step).grid(column=0, row=1)
        tk.Button(self, text="Run", width=5, command=self.run).grid(column=1, row=1)

        halt_frame = ttk.Frame(self, padding=5)
        tk.Label(halt_frame, text="Halt").grid(column=0, row=0)
        tk.Canvas(halt_frame, bg="black", height="20",
                  width="20").grid(column=1, row=0)

        run_frame = ttk.Frame(self, padding=5)
        tk.Label(run_frame, text="Run").grid(column=0, row=0)
        tk.Canvas(run_frame, bg="black", height="20",
                  width="20").grid(column=1, row=0)

        halt_frame.grid(column=2, row=1)
        run_frame.grid(column=3, row=1)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def init(self):
        if self.controller:
            self.controller.init()

    def single_step(self):
        if self.controller:
            self.controller.single_step()

    def store_and_store_plus(self, option_str="Store"):
        if self.controller:
            self.controller.store_and_store_plus(option_str)

    def load(self):
        if self.controller:
            self.controller.load()

    def run(self):
        if self.controller:
            self.controller.run()


class PrinterAndKeyboard(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None
        self.button_pressed = tk.StringVar()
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=0)
        tk.Label(self, text="Keyboard").grid(column=0, row=0, columnspan=2, sticky="N")
        self.keyboard = tk.Text(self, height=5, width=50)
        self.keyboard.grid(column=0, row=1, columnspan=2)
        self.ok = tk.Button(self, text="OK", width=5, command=lambda: self.button_pressed.set("button pressed"))
        self.ok.grid(column=1, row=2, sticky="E")
        tk.Button(self, text="Cancel").grid(column=0, row=2, sticky="E")

        tk.Label(self, text="Printer").grid(column=2, row=0, sticky="N")
        self.printer = tk.Text(self, height=7.5, width=50)
        self.printer.configure(state='disabled')
        self.printer.grid(column=2, row=1, rowspan="2")

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def keyboard_on_change(self):
        self.ok.wait_variable(self.button_pressed)
        self.keyboard.delete("1.0", "end")
        input_value = self.keyboard.get('1.0','end')
        self.keyboard.see(tk.END)
        return input_value

    def printer_on_change(self, value):
        value = int(value, 2)
        if not 48 <= value <= 57:
            value = chr(value)
        self.printer['state'] = 'normal'
        # if self.printer.index('end-1c') != '1.0':
        #     self.printer.insert('end', '\n')
        self.printer.insert('end', value)
        self.printer['state'] = 'disabled'
        self.printer.see(tk.END)


class FieldEngineeringConsole(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        tk.Label(self, text="Console").grid(column=0, row=0, sticky="N")
        self.console = tk.Text(self, height=28, width=50, state="disabled", borderwidth=2, relief=tk.SUNKEN)
        self.console.grid(column=0, row=1)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def write_to_log(self, msg):
        # num_lines = int(self.console.index('end - 1 line').split('.')[0])
        # if num_lines % 24 == 0:
        #     self.console.delete(1.0, 2.0)
        self.console['state'] = 'normal'
        if self.console.index('end-1c') != '1.0':
            self.console.insert('end', '\n')
        self.console.insert('end', msg)
        self.console['state'] = 'disabled'
        self.console.see(tk.END)

    def ss_on_change(self, pc, register_dict, func_name):
        msg = "Executing {} instruction.\n".format(func_name)
        for key, value in register_dict.items():
            if value is None:
                msg += "{}: None\n".format(key)
            else:
                msg += "{}: {}\n".format(key, str(int(value, 2)))
        msg += "PC jump to memory location: {}.\n".format(str(int(pc, 2)))
        self.write_to_log(msg)

    def init_on_change(self):
        msg = "Program has been stored into memory.\n"
        self.write_to_log(msg)

    def load_to_pc(self, pc):
        msg = "Set PC at memory location: {}.\n".format(str(int(pc, 2)))
        self.write_to_log(msg)
