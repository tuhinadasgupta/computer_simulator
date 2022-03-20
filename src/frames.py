import tkinter as tk
from tkinter import ttk


class GPR_AND_IXR(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        # gpr0
        tk.Label(self, text="GPR 0").grid(column=0, row=0, sticky="w")
        gpr0 = tk.Text(self, width="32", height="1", padx=2,
                       borderwidth=2, relief=tk.SUNKEN)
        gpr0.configure(state='disabled')
        gpr0.grid(column=1, row=0, padx="10")
        tk.Button(self, text="LD").grid(column=2, row=0)

        # gpr1
        tk.Label(self, text="GPR 1").grid(column=0, row=1, sticky="w")
        gpr1 = tk.Text(self, width="32", height="1", padx=2,
                       borderwidth=2, relief=tk.SUNKEN)
        gpr1.configure(state='disabled')
        gpr1.grid(column=1, row=1, padx="10")
        tk.Button(self, text="LD").grid(column=2, row=1)

        # gpr2
        tk.Label(self, text="GPR 2").grid(column=0, row=2, sticky="w")
        gpr2 = tk.Text(self, width="32", height="1", padx=2,
                       borderwidth=2, relief=tk.SUNKEN)
        gpr2.configure(state='disabled')
        gpr2.grid(column=1, row=2, padx="10")
        tk.Button(self, text="LD").grid(column=2, row=2)

        # gpr3
        tk.Label(self, text="GPR 3").grid(column=0, row=3, sticky="w")
        gpr3 = tk.Text(self, width="32", height="1", padx=2,
                       borderwidth=2, relief=tk.SUNKEN)
        gpr3.configure(state='disabled')
        gpr3.grid(column=1, row=3, padx="10")
        tk.Button(self, text="LD").grid(column=2, row=3)

        # ixr1
        tk.Label(self, text="IXR 1").grid(column=0, row=4, sticky="w")
        ixr1 = tk.Text(self, width="32", height="1", padx=2,
                       borderwidth=2, relief=tk.SUNKEN)
        ixr1.configure(state='disabled')
        ixr1.grid(column=1, row=4, padx="10")
        tk.Button(self, text="LD").grid(column=2, row=4)

        # ixr2
        tk.Label(self, text="IXR 2").grid(column=0, row=5, sticky="w")
        ixr2 = tk.Text(self, width="32", height="1", padx=2,
                       borderwidth=2, relief=tk.SUNKEN)
        ixr2.configure(state='disabled')
        ixr2.grid(column=1, row=5, padx="10")
        tk.Button(self, text="LD").grid(column=2, row=5)

        # ixr3
        tk.Label(self, text="IXR 3").grid(column=0, row=6, sticky="w")
        ixr3 = tk.Text(self, width="32", height="1", padx=2,
                       borderwidth=2, relief=tk.SUNKEN)
        ixr3.configure(state='disabled')
        ixr3.grid(column=1, row=6, padx="10")
        tk.Button(self, text="LD").grid(column=2, row=6)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


class OTHER_MACHINE_REGISTERS(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        # pc
        tk.Label(self, text="PC").grid(column=0, row=0, sticky="w")
        pc = tk.Text(self, width="24", height="1", padx=2,
                     borderwidth=2, relief=tk.SUNKEN)
        pc.configure(state='disabled')
        pc.grid(column=1, row=0, padx="10", sticky="w")
        tk.Button(self, text="LD").grid(column=2, row=0)

        # mar
        tk.Label(self, text="MAR").grid(column=0, row=1, sticky="w")
        mar = tk.Text(self, width="24", height="1", padx=2,
                      borderwidth=2, relief=tk.SUNKEN)
        mar.configure(state='disabled')
        mar.grid(column=1, row=1, padx="10", sticky="w")
        tk.Button(self, text="LD").grid(column=2, row=1)

        # mbr
        tk.Label(self, text="MBR").grid(column=0, row=2, sticky="w")
        mbr = tk.Text(self, width="32", height="1", padx=2,
                      borderwidth=2, relief=tk.SUNKEN)
        mbr.configure(state='disabled')
        mbr.grid(column=1, row=2, padx="10", sticky="w")
        tk.Button(self, text="LD").grid(column=2, row=2)

        # ir
        tk.Label(self, text="IR").grid(column=0, row=3, sticky="w")
        ir = tk.Text(self, width="32", height="1", padx=2,
                     borderwidth=2, relief=tk.SUNKEN)
        ir.configure(state='disabled')
        ir.grid(column=1, row=3, padx="10", sticky="w")
        tk.Button(self, text="LD").grid(column=2, row=3)

        # mfr
        tk.Label(self, text="MFR").grid(column=0, row=4, sticky="w")
        mfr = tk.Text(self, width="8", height="1", padx=2,
                      borderwidth=2, relief=tk.SUNKEN)
        mfr.configure(state='disabled')
        mfr.grid(column=1, row=4, padx="10", sticky="w")

        # cc
        tk.Label(self, text="CC").grid(column=0, row=5, sticky="w")
        cc = tk.Text(self, width="4", height="1", padx=2,
                     borderwidth=2, relief=tk.SUNKEN)
        cc.configure(state='disabled')
        cc.grid(column=1, row=5, padx="10", sticky="w")

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


class SWITCH(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        # opcode
        tk.Label(self, text="Operation").grid(column=0, row=0, sticky="S")
        opcode = ttk.Entry(self, width=10)
        opcode.grid(column=0, row=1, sticky="N")
        # opcode.bind("<FocusOut>", self.on_focus_out)

        # gpr
        tk.Label(self, text="GPR").grid(column=1, row=0, sticky="S")
        gpr = ttk.Entry(self, width=6)
        gpr.grid(column=1, row=1, sticky="N")
        # gpr.bind("<FocusOut>", self.on_focus_out)

        # ixr
        tk.Label(self, text="IXR").grid(column=2, row=0, sticky="S")
        ixr = ttk.Entry(self, width=6)
        ixr.grid(column=2, row=1, sticky="N")
        # ixr.bind("<FocusOut>", self.on_focus_out)

        # i
        tk.Label(self, text="I").grid(column=3, row=0, sticky="S")
        i = ttk.Entry(self, width=4)
        i.grid(column=3, row=1, sticky="N")
        # i.bind("<FocusOut>", self.on_focus_out)

        # address
        ttk.Label(self, text="Address").grid(column=4, row=0, sticky="S")
        address = tk.Entry(self, width=8)
        address.grid(column=4, row=1, sticky="N")
        # address.bind("<FocusOut>", self.on_focus_out)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller


class FUNCTION_BUTTONS(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = None

        tk.Button(self, text="Store", width=5).grid(column=0, row=0)
        tk.Button(self, text="S+", width=5).grid(column=1, row=0)
        tk.Button(self, text="Load", width=5).grid(column=2, row=0)
        tk.Button(self, text="Init", width=5, command=self.init).grid(column=3, row=0)
        tk.Button(self, text="SS", width=5).grid(column=0, row=1)
        tk.Button(self, text="Run", width=5).grid(column=1, row=1)

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

    def init(self):
        if self.controller:
            self.controller.init()

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
