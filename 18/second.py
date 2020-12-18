def simplify_add(expr):
    left = None
    simpler = []
    for part in expr:
        if isinstance(part, list):
            if left is not None:
                simpler.append(left)
                simpler.append('+')
                left = None
            simpler.append(simplify_add(part))
        elif part == '+':
            if left is None:
                simpler.append('+')
        elif part == '*':
            if left is not None:
                simpler.append(left)
                left = None
            simpler.append('*')
        else:
            if left is not None:
                left += part
            else:
                left = part
    if left is not None:
        simpler.append(left)
    return simpler
            

def simplify_mul(expr):
    canEval = True
    for part in expr:
        if part == '+':
            canEval = False
    left = None
    simpler = []
    for part in expr:
        if isinstance(part, list):
            if left is not None:
                simpler.append(left)
                simpler.append('*')
                left = None
            simpler.append(simplify_mul(part))
        elif part == '*':
            if left is None:
                simpler.append('*')
        elif part == '+':
            if left is not None:
                simpler.append(left)
                left = None
            simpler.append('+')
        else:
            if left is not None:
                if canEval:
                    left *= part
                else:
                    simpler.append(left)
                    simpler.append('*')
                    left = part
            else:
                left = part
    if left is not None:
        simpler.append(left)
    return simpler


def simplify_group(expr):
    if len(expr) == 1:
        return expr[0]
    simpler = []
    for part in expr:
        if isinstance(part, list):
            simpler.append(simplify_group(part))
        else:
            simpler.append(part)
    return simpler


def simplify(expr):
    expr = simplify_add(expr)
    #print(expr)
    expr = simplify_mul(expr)
    #print(expr)
    expr = simplify_group(expr)
    return expr


def calc(expr):
    while isinstance(expr, list):
        #print(expr)
        expr = simplify(expr)
    return expr


def solve(data):
    total = 0
    for expr in data:
        value = calc(expr)
        total += value
        print('{} = {}'.format(expr, value))
    return total


def read(filename):
    def process(line):
        data = []
        level = 0
        groupStart = None
        for i in range(len(line)):
            c = line[i]
            if c == ' ':
                pass
            elif c == '(':
                if level == 0:
                    groupStart = i
                level += 1
            elif c == ')':
                level -= 1
                if level == 0:
                    data.append(process(line[groupStart+1:i]))
            elif level == 0:
                if c in ['+', '*']:
                    data.append(c)
                else:
                    data.append(int(c))
        return data
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
