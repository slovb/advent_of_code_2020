def solve(data):
    solved = {}
    def count(jolts, jolt, i, mem):
        if (jolt, i) in solved:
            return solved[(jolt, i)]
        if i >= len(jolts):
            return 0
        if jolts[i] - jolt > 3:
            return 0
        if i == len(jolts) - 1:
            #if (jolts[1] == 3):
            #print(mem + [jolts[i]])
            return 1
        s = 0
        for j in range(3):
            s += count(jolts, jolts[i], i + j + 1, mem + [jolts[i]])
        solved[(jolt, i)] = s
        return s
    data.append(0)
    data.append(max(data) + 3)
    jolts = sorted(data)
    return count(jolts, 0, 0, [])

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
