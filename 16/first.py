def valid_tid(tid, rule):
    return (rule[0][0] <= tid and tid <= rule[0][1]) or (rule[1][0] <= tid and tid <= rule[1][1])

def solve(data):
    total = 0
    for ticket in data['nearby tickets']:
        for tid in ticket:
            valid = False
            for rule in data['rules']:
                #print(tid, data['rules'][rule], valid_tid(tid, data['rules'][rule]))
                if valid_tid(tid, data['rules'][rule]):
                    valid = True                    
                    break
            if not valid:
                total += tid
                print(tid)
    return total


def read(filename):
    def process(line):
        key = line.split(':')[0]
        v0 = [int(v) for v in line.split(': ')[1].split(' or ')[0].split('-')]
        v1 = [int(v) for v in line.split(' or ')[1].split('-')]
        return key, (v0, v1)
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        data = {}
        rules = {}
        l = 0
        while lines[l] != '':
            key, val = process(lines[l])
            rules[key] = val
            l += 1
        data['rules'] = rules
        l += 2
        data['your ticket'] = [int(v) for v in lines[l].split(',')]
        nearby = []
        l += 3
        for line in lines[l:]:
            ticket = []
            for v in line.split(','):
                ticket.append(int(v))
            nearby.append(ticket)
        data['nearby tickets'] = nearby
        return data


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
