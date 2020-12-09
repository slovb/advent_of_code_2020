def is_valid(data, n, i):
    v = data[i]
    a = data[i-n:i]
    for k, x in enumerate(a[:-1]):
        for y in a[k+1:]:
            if x+y == v:
                return True
    return False


def find(data):
    n = 25
    for i, d in enumerate(data[n:]):
        if not is_valid(data, n, i+n):
            return d

def solve(data):
    inval = find(data)
    acc, i, j = 0, 0, 0
    while acc != inval:
        if acc > inval:
            acc -= data[i]
            i += 1
        else:
            acc += data[j]
            j += 1
    print((i, j))
    return min(data[i:j]) + max(data[i:j])

def read(filename):
    with open(filename, 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
