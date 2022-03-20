############################################################
# memory implementation
# use dictionary to hold the data.
# the key represent the location and the value represent the 
# data in that memory location.
# provide the basic methods like get and set...
############################################################


class Memory:
    # init the memory. the default flag for expend is false.
    def __init__(self):
        self.memory = {}
        self.is_expended = False


    # get method
    def get_memory(self, memory_address):
        return self.memory[memory_address]


    # set method
    def set_memory(self, memory_address, memory_value):
        memory_value = memory_value.zfill(16)
        self.memory[memory_address] = memory_value


    # check if the memory is expended.
    @property
    def expend_memory(self):
        return self.is_expended


    # expending the memory and set the flag to true. 
    @expend_memory.setter
    def expend_memory(self):
        self.is_expended = True

    
    def reset_memory(self):
        self.memory.clear()
        