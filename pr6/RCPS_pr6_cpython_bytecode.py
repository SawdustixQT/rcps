stack = [0] * 16
sp = 0 # Stack pointer

def push(value):
    global sp
    stack[sp] = value
    sp += 1

def pop():
    global sp
    sp -= 1
    return  stack[sp]

def peek():
    global sp
    print(stack[sp - 1])


def bor():
    rhl = pop()
    lhl = pop()
    result = lhl | rhl
    push(result)

def rshift():
    rhl = pop()
    lhl = pop()
    res = lhl >> rhl
    push(res)

def lshift():
    rhl = pop()
    lhl = pop()
    res = lhl << rhl
    push(res)

def add():
    rhl = pop()
    lhl = pop()
    res = lhl + rhl
    push(res)

def sub():
    rhl = pop()
    lhl = pop()
    res = lhl + rhl
    push(res)

def bmod():
    rhl = pop()
    lhl = pop()
    res = lhl % rhl
    push(res)



def execute (prog):
    for line in prog:
        op, *args = line
        op(*args)

x = 1
y = 2
# 4
# program = [
#     (push, x),
#     (push, 3),
#     ("bor", )
#     # Команды из дисасебмлера python
# ]

# 5
program = [
    (push, x),
    (push, 1),
    (bmod, ),
    (push, y),
    (add, ),
    (push, y),
    (push, 5),
    (lshift, ),
    (add, )
]

# 6
x = 2
y = 3


execute(program)
peek()
