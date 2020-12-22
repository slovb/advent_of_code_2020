def solve(data):
    p1, p2 = data
    while len(p1) > 0 and len(p2) > 0:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    total = 0
    p = p1 if len(p1) > 0 else p2
    for i, c in enumerate(p[::-1]):
        total += (i + 1) * c
    return total


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        data = []
        player = []
        for line in lines:
            if line == '':
                data.append(player)
                player = []
            elif line[0] == 'P':
                continue
            else:
                player.append(int(line))
        data.append(player)
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
