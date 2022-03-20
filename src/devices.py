############################################################
# class for simple IO
# keyboard is a console that can get the input from user
# printer is a console that can print the output
# card reader is not required for this project
# other devices are something like console registers, switches, etc
############################################################


class Devices:
    def __init__(self) -> None:
        self.keyboard = None
        self.printer = None
        self.card_reader = None
        self.other_devices = [None]*29


    @property
    def keyboard(self):
        return self.keyboard
    

    @keyboard.setter
    def keyboard(self, keyboard):
        self.keyboard = keyboard


    @property
    def printer(self):
        return self.printer
    

    @printer.setter
    def printer(self, printer):
        self.printer = printer


    @property
    def card_reader(self):
        return self.card_reader
    

    @card_reader.setter
    def card_reader(self, card_reader):
        self.card_reader = card_reader

    
    def get_other_device(self, index):
        return self.other_devices[index]


    def set_other_device(self, index, value):
        self.other_devices[index] = value


    def test(self):
        print("keyboard: " + str(self.keyboard))
        print("printer: " + str(self.printer))
        print("card reader: " + str(self.card_reader))
        i = 3
        for device in self.other_devices:
            print(str(i) + " " + "device: " + str(device))
            i+=1

    