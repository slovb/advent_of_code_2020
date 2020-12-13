def good(timestamp, i, id):
    return ((timestamp + i) % id) == 0


def fix(timestamp, i, id):
    #print(timestamp, i, id, id - ((timestamp + i) % id))
    return id - ((timestamp + i) % id)


def determine_step(ids):
    return ids[0][0]


def solve(data):
    timestamp, ids = data
    timestamp += fix(timestamp, ids[0][1], ids[0][0])
    step = determine_step(ids)
    bad = True
    while bad:
        bad = False
        for id, i in ids:
            while not good(timestamp, i, id):
                bad = True
                timestamp += step
            if bad: # update step
                n = 1
                while not good(timestamp + n * step, i, id):
                    n += 1
                step = n*step
                break
    return timestamp


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        timestamp = int(lines[0])
        ids = []
        for i, id in enumerate(lines[1].split(',')):
            if id != 'x':
                ids.append((int(id), i))
        ids = sorted(ids)[::-1]
        return (timestamp, ids)


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
