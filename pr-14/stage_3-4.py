import sys
import csv

def mask(n):
    return (2 ** n) - 1

CMD_SIZES = {0: 5, 1: 3, 4: 3, 7: 8}

def execute(bytecode, memory_size=1024):
    memory = [0] * memory_size
    registers = [0] * 32
   
    # Загружаем программу в память
    for i, b in enumerate(bytecode):
        memory[i] = b
   
    pc = 0
    program_end = len(bytecode)
   
    while pc < program_end:
        # Fetch: определяем опкод и размер команды
        opcode = memory[pc] & mask(3)
        size = CMD_SIZES[opcode]
       
        # Decode: читаем байты и собираем в число
        cmd = int.from_bytes(memory[pc:pc+size], 'little')
       
        # Execute
        if opcode == 1:  # LOAD_CONST
            B = (cmd >> 3) & mask(5)
            C = (cmd >> 8) & mask(10)
            registers[B] = C
       
        elif opcode == 0:  # READ_MEM
            B = (cmd >> 3) & mask(25)
            C = (cmd >> 28) & mask(5)
            registers[C] = memory[B]
       
        elif opcode == 4:  # WRITE_MEM
            B = (cmd >> 3) & mask(5)
            C = (cmd >> 8) & mask(11)
            D = (cmd >> 19) & mask(5)
            addr = registers[D] + C
            memory[addr] = registers[B]

        elif opcode == 7:  # SHIFT_LEFT
            B = (cmd >> 3) & mask(5)
            C = (cmd >> 8) & mask(25)
            D = (cmd >> 33) & mask(25)
            memory[D] = memory[C] << registers[B]
       
        pc += size
   
    return memory, registers

def dump_memory(memory, path, start, end):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['address', 'value'])
        for addr in range(start, end + 1):
            writer.writerow([addr, memory[addr]])

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    mem_range = sys.argv[3]  # формат: "start-end"
   
    start, end = map(int, mem_range.split('-'))
   
    with open(input_file, 'rb') as f:
        bytecode = f.read()
   
    memory, registers = execute(bytecode)
    dump_memory(memory, output_file, start, end)
   
    print(f"Выполнено. Дамп памяти [{start}-{end}] сохранён в {output_file}")

if __name__ == '__main__':
    main()

