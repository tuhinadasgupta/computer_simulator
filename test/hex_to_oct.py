dataframe = {}
with open('/Users/ygao1/machine_simulator/test/test_bin.txt', 'r') as f:
    for line in f.readlines():
        address, value = line.split(" ")
        address = oct(int(address, 2))[2:]
        value = oct(int(value, 2))[2:]
        dataframe[address] = value

with open('/Users/ygao1/machine_simulator/test/test_oct.txt', 'a') as writer:
    for location, value in dataframe.items():
        # print(location + " " + value)
        writer.write(str(location) + " " + str(value) + "\n")
