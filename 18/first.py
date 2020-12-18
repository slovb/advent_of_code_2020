def calc(line):
    value = None
    currentOp = None
    level = 0
    groupStart = None
    def eval_op(value, currentOp, val):
        if currentOp == None:
            return val, currentOp
        elif currentOp == '+':
            return value + val, None
        elif currentOp == '*':
            return value * val, None
    for i in range(len(line)):
        c = line[i]
        if c == '(':
            if level == 0:
                groupStart = i
            level += 1
        elif c == ')':
            level -= 1
            if level == 0:
                value, currentOp = eval_op(value, currentOp, calc(line[groupStart + 1:i]))
        elif level == 0:
            if c == ' ':
                pass
            elif c == '+' or c == '*':
                currentOp = c
            else:
                value, currentOp = eval_op(value, currentOp, int(c))

    return value


def solve(data):
    total = 0
    for line in data:
        value = calc(line)
        total += value
        print('{} = {}'.format(line, value))
    return total


def read(filename):
    def process(line):
        return line
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        return [process(line) for line in lines]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
