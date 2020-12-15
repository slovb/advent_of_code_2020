def solve(data):
    mem = {}
    turn = 0
    c = 0
    for n in data:
        if n not in mem:
            c = 0
        else:
            c = turn - mem[n]
        mem[n] = turn
        turn += 1
        recent = n
    while turn < 30000000:
        n = c
        if n not in mem:
            c = 0
        else:
            c = turn - mem[n]
        mem[n] = turn
        turn += 1
    return n


def read(filename):
    def process(line):
        return int(line)
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        data = [process(line) for line in lines]
        return data


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
