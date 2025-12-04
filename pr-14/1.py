import yaml
import sys

def parse(program_file):
    with open(program_file, "r") as f:
        return yaml.safe_load(f)['program']


def toIR(instructions):
    ir = []
    for inst in instructions:
        cmd = inst["cmd"]
        if cmd == "LOAD_CONST":
            ir.append({"op": cmd, "a": 1, "b": inst['reg'], "c": inst['value']})
        elif cmd == "READ_MEM":
            ir.append({"op": cmd, "a": 0, "b": inst['addr'], "c": inst['dest_reg']})
        elif cmd == "WRITE_MEM": 
            ir.append({"op": cmd, "a": 4})
        elif cmd == "RSHIFT":
            ir.append({"op": cmd})
        
    return ir

def field(value, start, end):
    mask = 2 ** (end - start + 1) - 1
    return (value & mask) << start

def encode(entry):
    op = entry['op']
    if op == "LOAD_CONST":
        cmd = 0
        cmd |= field(entry['a'], 0, 2)
        cmd |= field(entry['b'], 8, 18)
        return cmd.to_bytes(length=3, byteorder = 'little')


def assembler(ir):
    binar = bytearray()
    for i in ir:
        binar.extend(encode(i))
    return binar

def main():
    src = sys.argv[1]
    output = sys.argv[2]
    test_mode = sys.argv[3]

    ir = toIR(parse(src))
    print(ir)

    byni = assembler(ir)
    print(len(byni))
    with open(output, 'w') as file:
        file.write(byni)

# 3 этап

cmd_sizes = {
    0: 5,

}


def mask(m):
    return 2 * m - 1

def execute(bytecode, memSize = 1024):
    memory = [0] * memSize
    reg = [0] * 32
    for i, elem in enumerate(bytecode):
        memory[i] = elem

    pc = 0
    program_end = len(bytecode)

    while pc < program_end:
        op = memory[pc] & mask(3)
        size = cmd_sizes[op]

        cmd = int.from_bytes(memory[pc: pc + size], byteorder='little')

        if op == 1:
            b = (cmd >> 3) & mask(5)
            c = (cmd >> 8) & mask(10)
            reg[b] = c
        elif op == 7:
            b = (cmd >> 3) & mask(5)
            c = (cmd >> 8) & mask(25)
            d = (cmd >> 33) & mask(25)
            memory[d] = memory[c] << reg[b]




main()

