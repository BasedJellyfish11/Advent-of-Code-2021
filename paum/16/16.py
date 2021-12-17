import numpy as np

with open("./input.txt") as f:
    hex_bits = f.readlines()[0].strip()

bits = np.array([])
binary = bin(int(hex_bits, 16))
bits = np.array([int(c) for c in binary[2:]])

while len(bits) < len(hex_bits) * 4:
    bits = np.insert(bits, 0, 0)

def decode(binary_arr):
    num = ""
    for bit in binary_arr:
        num += str(int(bit))

    #print("Decoding: " + str(binary_arr) + " : " + str(int(num, 2)))
    return int(num, 2)

def process_literal(packet):

    counter = 0
    should_process = True
    bin_rep = np.array([])

    #print(bin_rep)
    #print(packet[1:5])

    while should_process:
        if packet[counter] == 0:
            should_process = False
        bin_rep = np.concatenate((bin_rep, packet[counter + 1: counter + 5]))
        counter += 5

    res = decode(bin_rep)

    #print("Processed literal " + str(packet[0:counter]) + " as " + str(res))
    return (counter, res)

def operate_literals(type_id, literals):
    if type_id == 0:
        ret = np.sum(literals)
    elif type_id == 1:
        ret = np.prod(literals)
    elif type_id == 2:
        ret = np.min(literals)
    elif type_id == 3:
        ret = np.max(literals)
    elif type_id == 5:
        ret = 1 if literals[0] > literals[1] else 0
    elif type_id == 6:
        ret = 1 if literals[0] < literals[1] else 0
    elif type_id == 7:
        ret = 1 if literals[0] == literals[1] else 0
    else:
        print("WARNING")
        return "Hi Jon"
    
    #print(ret)
    return ret


def process_operator(packet, type_id):

    operator_type = packet[0] 
    version_total = 0
    literals = np.array([])
    tot_bits_processed = 1

    if operator_type == 0:

        len_to_process = decode(packet[1:16])
        tot_bits_processed = 16
        #print("Operating by length: " + str(len_to_process))

        while (len_to_process > tot_bits_processed - 16):
            bits_processed, version_sum, literal = process_packet(packet[tot_bits_processed:])
            tot_bits_processed += bits_processed
            version_total += version_sum
            literals = np.append(literals, literal)
        
        if (len_to_process != tot_bits_processed - 16):
            print("WARNING!")

    else:
        num_to_process = decode(packet[1:12])
        tot_bits_processed = 12
        #print("Operating by number: " + str(num_to_process))
        
        for i in range(num_to_process):
            bits_processed, version_sum, literal = process_packet(packet[tot_bits_processed:])
            tot_bits_processed += bits_processed
            version_total += version_sum
            literals = np.append(literals, literal)
    
    res = operate_literals(type_id, literals)

    #print("Operands: " + str(literals))
    #print("Finished operation of " + str(type_id) + " - result = " + str(res))

    return tot_bits_processed, version_total, res


def process_packet(packet):

    version = decode(packet[0:3])
    type_id = decode(packet[3:6])

    version_total = version

    #print("Version: " + str(version))
    #print("Type: " + str(type_id))

    #print("Processing packet with type_id: " + str(type_id))

    if (type_id == 4):
        bits_processed, literal = process_literal(packet[6:])
    else:
        bits_processed, version_sum, literal = process_operator(packet[6:], type_id)
        version_total += version_sum


    return (bits_processed + 6, version_total, literal)

bits_processed, version_sum, literal = process_packet(bits)
print(version_sum)
print(literal)
print(str(bits[:200]))
print(np.prod([]))