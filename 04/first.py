def validate(obj):
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in keys:
        if key not in obj:
            return False
    return True


def solve(data):
    return sum([1 if validate(obj) else 0 for obj in data])


def read(filename):
    with open(filename, 'r') as f:
        data = []
        obj = {}
        for line in f.readlines():
            l = line.rstrip()
            if l == '':
                data.append(obj)
                obj = {}
                continue
            for kvp in l.split(' '):
                obj[kvp.split(':')[0]] = kvp.split(':')[1]
        data.append(obj)
        return data


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\nAnswer {}".format(main(f)))
