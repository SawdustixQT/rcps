# LUA
# Регистровая машина

x = 3
y = 3

registers = [0] * 32 # положительные 
consts = [x, 3, 5, y] # отрицательные

def rk(value):
    if value < 0:
        return consts[abs(value) - 1]
    return registers[value]


def gettabup(a, b, c):
    registers[a] = rk(c)


def idiv(a, b, c):
    registers[a] = rk(b) // rk(c)


def shr(a, b, c):
    registers[a] = rk(b) >> rk(c)

def sub(a, b, c):
    registers[a] = rk(b) - rk(c)

def bor(a, b, c):
    registers[a] = rk(b) | rk(c)

def add(a, b, c):
    registers[a] = rk(b) + rk(c)

def band(a, b, c):
    registers[a] = rk(b) & rk(c)

def retur(a, b):
    print(registers[b])

def execute (prog):
    for line in prog:
        op, *args = line
        op(*args)

# 1
prog = [
    (gettabup, 0, 0, -1),
    (band, 0, 0, -2),
    (band, 1, 0, -3),
    (add, 0, 0, 1),
    (gettabup, 1, 0, -3),
    (add, 0, 0, 1),
    (retur, 0, 2)
]

# 2
# prog = [
#     (gettabup, 0, 0, -1),
#     (band, 0, 0, -2),
#     (sub, 0, -3, 1),
#     (gettabup, 1, 0, -4),
#     (shr, 1, 0, -4),
#     (add, 0, 0, 1),
#     (retur, 0, 2),
#     (retur, 0, 1)
# ]

# prog = [
# #     (gettabup, 0, 0, -1)
# # ]
execute(prog)
print(registers)
    