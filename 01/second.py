def solve(data):
    data.sort()
    for i, a in enumerate(data):
        for j, b in enumerate(data[i+1::-1]):
            for c in data[i+1:len(data) - i - j - 2]:
                if a + b + c == 2020:
                    return a * b * c
                elif a + b + c > 2020:
                    continue


def read(filename):
    with open(filename, 'r') as f:
        return [int(l) for l in f.readlines()]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\nAnswer {}".format(main(f)))
