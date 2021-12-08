dir = "pest/inputs/"

def read_file(name):
    with open(dir + name, "r") as file:
        data = file.readlines()
        data = [x.strip() for x in data]
        # print(data)
        return data
