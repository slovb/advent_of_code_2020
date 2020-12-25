def solve(data):
    subject = 7
    prime = 20201227
    public0, public1 = data
    v = 1
    loop = 0
    while True:
        v = (v * subject) % prime
        loop += 1
        if v == public0:
            return (public1 ** loop) % prime
        elif v == public1:
            return (public0 ** loop) % prime


def read(filename):
    def process(line):
        return int(line)
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
