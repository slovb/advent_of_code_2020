def solve(data):
    counted = {}
    def count(color):
        if color in counted:
            return counted[color]
        x = 1
        for m, c in data[color]:
            x += m * count(c)
        counted[color] = x
        return x
    return count('shiny gold') - 1


def read(filename):
    with open(filename, 'r') as f:
        data = {}
        for line in f.readlines():
            line = line.rstrip()
            parts = line.rstrip('.').split(" contain ")
            contents = []
            if parts[1] != 'no other bags':
                for content in parts[1].split(', '):
                    count = 1
                    content = content.rstrip(' bags').rstrip(' bag')
                    if content[0].isnumeric():
                        count = int(content[0])
                        content = content[2:]
                    contents.append((count, content))
            data[parts[0].rstrip(' bags')] = contents
        return data


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\n{}".format(main(f)))
