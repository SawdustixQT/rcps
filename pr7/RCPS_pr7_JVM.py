class JVM:
    def __init__(self):
        self.stack = []
        self.locals = []

    def run(self, programs, *args):
        self.stack = []
        self.locals = list(args)
        for i in programs:
            self._exec(i)
        print(self.stack.pop())

    def _sanitize(self, arg: str):
        if arg.startswith("m"):
            return -int(arg[1:])
        return int(arg)

    def _exec(self, prog):
        if "_" in prog:
            op, arg = prog.split("_")
            arg = self._sanitize(arg)
            match op:
                case "iconst": self.stack.append(arg)
                case "iload": self.stack.append(self.locals[arg])
        else:
            r = self.stack.pop()
            l = self.stack.pop()
            match prog:
                case "isub": self.stack.append(l - r)
                case "iadd": self.stack.append(l + r)
                case "ior": self.stack.append(l | r)
                # case "ireturn": return self.stack

prog = [
    "iconst_2",
    "iload_0",
    "isub",
    "iload_0",
    "iadd",
    "iload_1",
    "iconst_2",
    "ior",
    "iadd"
]
j = JVM()
j.run(prog, 1, 5)



