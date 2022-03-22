dataframe = {}
with open('/Users/ygao1/machine_simulator/test/test.txt', 'r') as f:
    for line in f.readlines():
        address, value = line.split(" ")
        address = bin(int(address, 16))[2:].zfill(16)
        value = bin(int(value, 16))[2:].zfill(16)
        print(address + " " + value)
        dataframe[address] = value

with open('/Users/ygao1/machine_simulator/test/test_bin.txt', 'a') as writer:
    for location, value in dataframe.items():
        # print(location + " " + value)
        writer.write(location + " " + value + "\n")