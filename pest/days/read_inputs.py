dir = "pest/inputs/"
fileName = "inputs.txt"
fileName = "real_inputs.txt"

def readFromFile(name):
    with open(dir + name, "r") as file:
        data = file.readlines()
        data = [x.strip() for x in data]
        # print(data)
        return data
