class NET:
    def __init__(self):
        self.stack = []
        self.locals = []
        self.args = []
        self.isinstance = False

    def run(self, progs, *args, inst: bool, loc):
        self.stack = []
        self.locals = [0] * loc
        if inst:
            self.args = [None] + list(args)
        else:
            self.args = list(args)
        for i in progs:
            self._exec(i)
        print(self.stack.pop())

    def _exec(self, prog):
        if "." in prog:
            op, *args = prog.split(".")
            arg = int(args[-1])
            match op:
                case "ldc": self.stack.append(arg)
                case "ldarg": self.stack.append(self.args[arg])
                case "stloc": self.locals[arg] = self.stack.pop()
                case "ldloc": self.stack.append(self.locals[arg])
        else:
            r = self.stack.pop()
            l = self.stack.pop()
            match prog:
                case "add": self.stack.append(l + r)
                case "or": self.stack.append(l | r)

prog2 = [
    ""
]

n = NET()
n.run(prog2, 5, 1, loc=1, inst=False)



