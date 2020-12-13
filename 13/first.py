def wait_time(timestamp, id):
    return id - (timestamp % id)


def solve(data):
    timestamp, ids, unknown = data
    best_wait = wait_time(timestamp, ids[0][1])
    best_id = ids[0][1]
    for i, id in ids:
        wait = wait_time(timestamp, id)
        if wait < best_wait:
            best_wait = wait
            best_id = id
    return best_id * best_wait


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        timestamp = int(lines[0])
        ids = []
        unknown = []
        for i, id in enumerate(lines[1].split(',')):
            if id == 'x':
                unknown.append((i, id))
            else:
                ids.append((i, int(id)))
        return (timestamp, ids, unknown)


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
