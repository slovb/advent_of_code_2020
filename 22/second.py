def score(deck):
    total = 0
    for i, c in enumerate(deck[::-1]):
        total += (i + 1) * c
    return total


def simulate(p1, p2, depth = 0):
    import copy
    mem = set()
    i = 1
    while True:
        #print('Round {}:{}\n{}\n{}'.format(depth, i, p1, p2))
        i += 1
        s = (score(p1), score(p2)) # lets assume this is a hash for now
        if s in mem:
            #print('P1 wins game on mem\n')
            return True, p1 # p1 wins
        mem.add(s)
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        p1Wins = None
        if c1 > len(p1) or c2 > len(p2):
            p1Wins = c1 > c2
        else:
            #print('<recurse>')
            p1Wins = simulate(copy.deepcopy(p1[:c1]), copy.deepcopy(p2[:c2]), depth + 1)[0]
            #print('</recurse>')
        if p1Wins:
            #print('P1 wins round\n')
            p1.append(c1)
            p1.append(c2)
        else:
            #print('P2 wins round\n')
            p2.append(c2)
            p2.append(c1)
        if len(p1) == 0:
            #print('P2 wins game\n')
            return False, p2
        elif len(p2) == 0:
            #print('P1 wins game\n')
            return True, p1


def solve(data):
    p1, p2 = data
    return score(simulate(p1, p2)[1])


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        data = []
        player = []
        for line in lines:
            if line == '':
                data.append(player)
                player = []
            elif line[0] == 'P':
                continue
            else:
                player.append(int(line))
        data.append(player)
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
