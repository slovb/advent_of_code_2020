def solve(data):
    acc = 0
    i = 0
    mem = set()
    while i not in mem:
        mem.add(i)
        ins, val = data[i]
        if ins == 'acc':
            acc += val
            i += 1
        elif ins == 'nop':
            i += 1
        elif ins == 'jmp':
            i += val
    return acc


def read(filename):
    with open(filename, 'r') as f:
        def process(line):
            cmd = line.split(' ')[0]
            val = int(line.split(' ')[1])
            return (cmd, val)
        return [process(line.rstrip()) for line in f.readlines()]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
