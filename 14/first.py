def solve(data):
    def mask(value, bitmask):
        for i, c in enumerate(bitmask[::-1]):
            if c == '1':
                value = value | (1<<i)
            elif c == '0':
                value = value & ~(1<<i)
        return value

    mem = {}
    for bitmask, writes in data:
        for addr, value in writes:
            mem[addr] = mask(value, bitmask)
    return sum([mem[k] for k in mem])


def read(filename):
    def parse_mask(line):
        return line.split(' ')[2]
    def parse_mem(line):
        addr = int(line.split('[')[1].split(']')[0])
        val = int(line.split(' ')[2])
        return (addr, val)
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        data = []
        mask = parse_mask(lines[0])
        group = []
        for line in lines[1:]:
            if line[0:4] == 'mask':
                data.append((mask, group))
                mask = parse_mask(line)
                group = []
            else:
                group.append(parse_mem(line))
        data.append((mask, group))
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
