def solve(data):
    directions = {
        'N': (0, 1), 
        'E': (1, 0), 
        'S': (0, -1), 
        'W': (-1, 0)
    }
    p = (0, 0)
    wp = (10, 1)
    for d, val in data:
        if d == 'R':
            if val == 90:
                wp = (wp[1], -wp[0])
            elif val == 180:
                wp = (-wp[0], -wp[1])
            elif val == 270:
                wp = (-wp[1], wp[0])
        elif d == 'L':
            if val == 90:
                wp = (-wp[1], wp[0])
            elif val == 180:
                wp = (-wp[0], -wp[1])
            elif val == 270:
                wp = (wp[1], -wp[0])
        elif d == 'F':
            p = (p[0] + val * wp[0], p[1] + val * wp[1])
        elif d in directions:
            wp = (wp[0] + val * directions[d][0], wp[1] + val * directions[d][1])
        print((p, wp))
    return abs(p[0]) + abs(p[1])


def read(filename):
    with open(filename, 'r') as f:
        def process(line):
            return (line[0], int(line[1:]))
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
