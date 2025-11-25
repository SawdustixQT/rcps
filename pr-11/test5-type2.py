stack = [0] * 16

sp = 0

env = {"x": 4, "y": 3}

def push(arg):
    global sp
    stack[sp] = arg
    sp += 1


def pop():
    global sp
    sp -= 1
    return stack[sp]


def get(name):
    push(env[name])

def set_(name):
    env[name] = pop()

def add():
    push(pop() + pop())

def div():
    a = pop()
    b = pop()
    push(b / a)

def nearest():
    push(pop().round())

def min_():
    push(min(pop(), pop()))

def mul():
    push(pop() * pop())

def ret():
    print(pop())


def exec(code):
    for op, *args in code:
        op(args)
        print(stack)

code = [
    (get, "y"),
    (push, 2),
    (div, ),
    (nearest, ),
    (set_, "a"),
    (get, "x"),
    (get, "y"),
    (min_, ),
    (set_, "b")
    ()
]