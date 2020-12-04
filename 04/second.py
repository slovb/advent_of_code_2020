def validate_year(year, lower, upper):
    if not year.isdigit():
        return False
    y = int(year)
    if lower <= y and y <= upper:
        return True
    return False


def validate_height(height):
    h = height[:-2]
    if not h.isdigit():
        return False
    h = int(h)
    if height[-2:] == 'cm':
        return 150 <= h and h <= 193
    elif height[-2:] == 'in':
        return 59 <= h and h <= 76
    return False


def validate_hair_color(hair):
    if not hair[0] == '#' or not len(hair) == 7:
        return False
    for c in hair[1:]:
        if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
            return False
    return True


def validate_eye_color(eye):
    return eye in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(pid):
    if not pid.isdigit():
        return False
    return len(pid) == 9


def validate(obj):
    if 'byr' not in obj or not validate_year(obj['byr'], 1920, 2002):
        return False
    if 'iyr' not in obj or not validate_year(obj['iyr'], 2010, 2020):
        return False
    if 'eyr' not in obj or not validate_year(obj['eyr'], 2020, 2030):
        return False
    if 'hgt' not in obj or not validate_height(obj['hgt']):
        return False
    if 'hcl' not in obj or not validate_hair_color(obj['hcl']):
        return False
    if 'ecl' not in obj or not validate_eye_color(obj['ecl']):
        return False
    if 'pid' not in obj or not validate_pid(obj['pid']):
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
