def valid_tid(tid, rule):
    return (rule[0][0] <= tid and tid <= rule[0][1]) or (rule[1][0] <= tid and tid <= rule[1][1])


def find_valid(data):
    good = []
    for ticket in data['nearby tickets']:
        invalid = False
        for tid in ticket:
            valid = False
            for rule in data['rules']:
                #print(tid, data['rules'][rule], valid_tid(tid, data['rules'][rule]))
                if valid_tid(tid, data['rules'][rule]):
                    valid = True                    
                    break
            if not valid:
                invalid = True
                break
        if not invalid:
            good.append(ticket) 
    return good


def find_fields(tickets, rules):
    fields = {}
    for rule_name in rules:
        rule = rules[rule_name]
        field = []
        for i in range(len(tickets[0])):
            valid = True
            for ticket in tickets:
                if not valid_tid(ticket[i], rule):
                    valid = False
                    break
            if valid:
                field.append(i)
        fields[rule_name] = field
    return fields


def solve(data):
    tickets = find_valid(data)
    my, rules = data['your ticket'], data['rules']
    fields = find_fields(tickets, rules)
    print(fields)
    solved = {}
    while len(fields) > 0:
        for field_name in fields:
            field = fields[field_name]
            if len(field) == 1:
                solved[field_name] = field[0]
                del(fields[field_name])
                for fn in fields:
                    if field[0] in fields[fn]:
                        fields[fn].remove(field[0])
                break
    prod = 1
    print(solved)
    for rule_name in solved:
        if rule_name[:9] == 'departure':
            prod *= my[solved[rule_name]]
    return prod


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
