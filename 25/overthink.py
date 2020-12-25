def simulate(subject, loop, value = 1):
    for i in range(loop):
        value = (value * subject) % 20201227
    return value


def solve(data):
    public0, public1 = data
    prime = 20201227
    loop = 1
    values = []
    candidates0 = {}
    candidates1 = {}
    starting_subject = 2
    next_subject = starting_subject
    while True:
        for i, v in enumerate(values):
            subject = i + starting_subject
            values[i] = (v * subject) % prime
            if values[i] == public0:
                print('{}: {} x {}'.format(0, subject, loop))
                if subject in candidates1:
                    return simulate(public0, candidates1[subject])
                candidates0[subject] = loop
            if values[i] == public1:
                print('{}: {} x {}'.format(1, subject, loop))
                if subject in candidates0:
                    return simulate(public1, candidates0[subject])
                candidates1[subject] = loop
        v = 1
        subject = next_subject
        for i in range(loop):
            v = (v * subject) % prime
            if v == public0:
                print('{}: {} x {}'.format(0, subject, i + 1))
                if subject in candidates1:
                    return simulate(public0, candidates1[subject])
                candidates0[subject] = i + 1
            if v == public1:
                print('{}: {} x {}'.format(1, subject, i + 1))
                if subject in candidates0:
                    return simulate(public1, candidates0[subject])
                candidates1[subject] = i + 1
        values.append(v)
        next_subject += 1
        loop += 1


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
