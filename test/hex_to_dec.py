dataframe = {}
with open('/Users/ygao1/machine_simulator/test/test.txt', 'r') as f:
    for line in f.readlines():
        address, value = line.split(" ")
        address = int(address, 16)
        value = int(value, 16)
        dataframe[address] = value

with open('/Users/ygao1/machine_simulator/test/test_dec.txt', 'a') as writer:
    for location, value in dataframe.items():
        # print(location + " " + value)
        writer.write(str(location) + " " + str(value) + "\n")
