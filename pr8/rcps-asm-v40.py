import argparse
from fontTools.varLib.instancer import parseArgs


def mask(n: int):
    m = (1 << n) - 1
    return m

def asm_load_const(const: int):
    cmd = 0
    cmd |= 8
    cmd |= (const & mask(19)) << 4
    return cmd.to_bytes(length=3, byteorder="little")

def asm_read_mem():
    cmd = 0
    cmd |= 10
    return cmd.to_bytes(length=1, byteorder="little")

def asm_write_mem(const: int):
    cmd = 0
    cmd |= 9
    cmd |= (const & mask(29)) << 4
    return cmd.to_bytes(length=5, byteorder="little")

def asm_not():
    cmd = 0
    cmd |= 14
    return cmd.to_bytes(length=1, byteorder="little")

def validate_args(args):
    if args.i is None:
        print("Необходим входной файл программы")
        return args, False
    if args.o == "program.bin":
        return args, True
    if args.t is None:
        args.t = False
        return args, True
    return args, True

def asm_read_file(input_file):
    with open(input_file) as file:
        for line in file.readlines():
            if "asm_load_const" in line:
                arg = int(line.split("(")[-1].strip().rstrip(")"))
                yield asm_load_const, arg
            elif "asm_read_mem" in line:
                yield (asm_read_mem, )
            elif "asm_write_mem" in line:
                arg = int(line.split("(")[-1].strip().rstrip(")"))
                yield asm_write_mem, arg
            elif "asm_not" in line:
                yield (asm_not, )
            file.close()

def asm(cmd: tuple):
    if len(cmd) == 1:
        return cmd[0]()
    else:
        return cmd[0](cmd[1])

def write_bin(program):
    program_bin = b""
    for cmd in program:
        program_bin += asm(cmd)
    return program_bin


def main():
    parser = argparse.ArgumentParser(description="АСМ ИКБО-21-22 вариант 40")
    parser.add_argument("-i", help='Путь к входному файлу', type=str)
    parser.add_argument("-o", help="Путь выходного файла", type=str)
    parser.add_argument("-t", help="Режим работы", type=bool)
    args = parser.parse_args()
    args, ok = validate_args(args)
    program = list(asm_read_file("program.txt"))
    wrote_bin = write_bin(program)
    with open(args.o, "wb") as file:
        file.write(wrote_bin)
        file.close()
    print(program)
    print(wrote_bin)

main()

#
assert asm_load_const(285) == bytes([0xD8, 0x11, 0x00])
assert asm_read_mem() == bytes([0x0A])
assert asm_write_mem(150) == bytes([0x69, 0x09, 0x00, 0x00, 0x00])
assert asm_not() == bytes([0x0E])
