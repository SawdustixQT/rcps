import yaml
import sys

def parse(source):
    with open(source, 'r') as f:
        return yaml.safe_load(f)['program']

def to_ir(instructions):
    ir = []
    for instr in instructions:
        cmd = instr['cmd']
        if cmd == 'LOAD_CONST':
            ir.append({'op': cmd, 'A': 1, 'B': instr['reg'], 'C': instr['value']})
        elif cmd == 'READ_MEM':
            ir.append({'op': cmd, 'A': 0, 'B': instr['addr'], 'C': instr['dest_reg']})
        elif cmd == 'WRITE_MEM':
            ir.append({'op': cmd, 'A': 4, 'B': instr['src_reg'],
                       'C': instr['offset'], 'D': instr['base_reg']})
        elif cmd == 'SHIFT_LEFT':
            ir.append({'op': cmd, 'A': 7, 'B': instr['shift_reg'],
                       'C': instr['src_addr'], 'D': instr['dest_addr']})
    return ir


def field(value, start, end):
    mask = 2**(end - start + 1) - 1
    return (value & mask) << start


def encode(val):
    op = val['op']
    if op == 'LOAD_CONST':
        cmd = 0
        cmd |= field(val['A'], 0, 2)
        cmd |= field(val['B'], 3, 7)
        cmd |= field(val['C'], 8, 17)
        return cmd.to_bytes(3, "little")
    elif op == 'READ_MEM':
        cmd = 0
        cmd |= field(val['A'], 0, 2)
        cmd |= field(val['B'], 3, 27)
        cmd |= field(val['C'], 28, 32)
        return cmd.to_bytes(5, "little")
    elif op == 'WRITE_MEM':
        cmd = 0
        cmd |= field(val['A'], 0, 2)
        cmd |= field(val['B'], 3, 7)
        cmd |= field(val['C'], 8, 18)
        cmd |= field(val['D'], 19, 23)
        return cmd.to_bytes(3, "little")
    elif op == 'SHIFT_LEFT':
        cmd = 0
        cmd |= field(val['A'], 0, 2)
        cmd |= field(val['B'], 3, 7)
        cmd |= field(val['C'], 8, 32)
        cmd |= field(val['D'], 33, 57)
        return cmd.to_bytes(8, "little")


def aseemble(ir):
    val = bytearray()
    for en in ir:
        val.extend(encode(en))
    return val


def main():
    source = sys.argv[1]
    output = sys.argv[2]
    test_mode = '--test' in sys.argv
   
    ir = to_ir(parse(source))
   

    per = aseemble(ir)
    with open(output, 'wb') as file:
        file.write(per)

    print(len(per))

    if test_mode:
        for i, e in enumerate(ir):
            fields = f"A={e['A']}, B={e['B']}, C={e['C']}"
            if 'D' in e:
                fields += f", D={e['D']}"
            print(f"{e['op']}: {fields}")

if __name__ == '__main__':
    main()
