def solve(data):
    jolts = sorted(data)
    jolts.append(max(jolts) + 3)
    jolt = 0
    diff = [0, 0, 0, 0]
    for j in jolts:
        diff[j-jolt] += 1
        jolt = j
    return diff[1] * diff[3]

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
