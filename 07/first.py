def generateRules(data):
    rules = {}
    for container, contents in data:
        contentList = [c[1] for c in contents]
        if container not in rules:
            rules[container] = set(contentList)
        else:
            for c in contentList:
                rules[container].add(c)
    return rules


def getContainers(rules, type):
    containers = set()
    for container in rules:
        contents = rules[container]
        if type in contents:
            print(type)
            containers.add(container)
            containers |= getContainers(rules, container)
    return containers


def solve(data):
    rules = generateRules(data)
    return len(getContainers(rules, 'shiny gold'))


def read(filename):
    with open(filename, 'r') as f:
        def process(line):
            parts = line.rstrip('.').split(" contain ")
            contents = []
            for content in parts[1].split(', '):
                count = 1
                content = content.rstrip(' bags').rstrip(' bag')
                if content[0].isnumeric():
                    count = int(content[0])
                    content = content[2:]
                contents.append((count, content))
            return (parts[0].rstrip(' bags'), contents)
        return [process(line.rstrip()) for line in f.readlines()]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\n{}".format(main(f)))
