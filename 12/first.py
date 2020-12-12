def solve(data):
    faces = ['N', 'E', 'S', 'W']
    directions = {
        'N': (0, 1), 
        'E': (1, 0), 
        'S': (0, -1), 
        'W': (-1, 0)
    }
    facing = 1
    x = 0
    y = 0
    for d, val in data:
        if d == 'L':
            facing = (facing - (val // 90)) % 4
        if d == 'R':
            facing = (facing + (val // 90)) % 4
        if d == 'F':
            d = faces[facing]
        if d in faces:
            x += val * directions[d][0]
            y += val * directions[d][1]
        print((x, y))
    return abs(x) + abs(y)


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
