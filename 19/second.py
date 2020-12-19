class Value:
    def __init__(self, value):
        self.value = value
    
    def valid(self, m):
        return self.value == m


class Reference:
    def __init__(self, reference, ruleset):
        self.reference = reference
        self.ruleset = ruleset
    
    def valid(self, m):
        if not isinstance(self.ruleset[self.reference], Rule):
            self.ruleset[self.reference] = Rule(self.ruleset[self.reference], self.ruleset)
        return self.ruleset[self.reference].valid(m)


class Sequence:
    def __init__(self, sequence, ruleset):
        self.sequence = sequence
        self.ruleset = ruleset
    
    def valid(self, m):
        if len(self.sequence) == 1:
            if Rule(self.sequence[0], self.ruleset).valid(m):
                #print('{} {}'.format(m, self.sequence[0]))
                return True
        elif len(self.sequence) == 2:
            for i in range(1, len(m)):
                if Rule(self.sequence[0], self.ruleset).valid(m[:i]) and Rule(self.sequence[1], self.ruleset).valid(m[i:]):
                    #print('{} {}\t{} {}'.format(m[:i], self.sequence[0], m[i:], self.sequence[1]))
                    return True
        elif len(self.sequence) == 3:
            for i in range(1, len(m) - 1):
                for j in range(i + 1, len(m)):
                    if Rule(self.sequence[0], self.ruleset).valid(m[:i]) and Rule(self.sequence[1], self.ruleset).valid(m[i:j]) and Rule(self.sequence[2], self.ruleset).valid(m[j:]):
                        #print('{} {}\t{} {}\t{} {}'.format(m[:i], self.sequence[0], m[i:j], self.sequence[1], m[j:], self.sequence[2]))
                        return True
        else:
            raise Exception("I don't want to do the general case now please")
        return False


class Alternatives:
    def __init__(self, alternatives, ruleset):
        self.alternatives = alternatives
        self.ruleset = ruleset

    def valid(self, m):
        for alternative in self.alternatives:
            if Rule(alternative, self.ruleset).valid(m):
                return True
        return False


class Rule:
    def __init__(self, rule, ruleset):
        self.ruleset = ruleset
        self.rule = rule
        self.mem = {}

    def valid(self, m):
        if m not in self.mem:
            if isinstance(self.rule, list):
                self.mem[m] = Alternatives(self.rule, self.ruleset).valid(m)
            elif isinstance(self.rule, tuple):
                self.mem[m] = Sequence(self.rule, self.ruleset).valid(m)
            elif self.rule in ['a', 'b']:
                self.mem[m] = Value(self.rule).valid(m)
            else:
                self.mem[m] = Reference(self.rule, self.ruleset).valid(m)
        return self.mem[m]


def solve(data):
    ruleset, messages = data
    ruleset[8] = [(42), (42, 8)]
    ruleset[11] = [(42, 31), (42, 11, 31)]
    total = 0
    rule = Rule(ruleset[0], ruleset)
    for message in messages:
        if rule.valid(message):
            total += 1
            print('{} is valid'.format(message))
        else:
            print('{} is invalid'.format(message))
    return total


def read(filename):
    def process(sequence):
        s = []
        for item in sequence.split(' '):
            if item in ['"a"', '"b"']:
                s.append(item[1])
            else:
                s.append(int(item))
        return tuple(s)
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        ruleset = {}
        messages = []
        i = 0
        while lines[i] != '':
            line = lines[i]
            id = int(line.split(':')[0])
            rule = []
            part = line.split(': ')[1]
            if '|' in part:
                ruleset[id] = [process(p) for p in part.split(' | ')]
            else:
                ruleset[id] = process(part)
            i += 1
        messages = lines[i+1:]
        return (ruleset, messages)


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
