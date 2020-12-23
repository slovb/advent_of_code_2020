# Double linked looping list
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pop(self, i = 1):
        n = self.right
        m = n
        for _ in range(i - 1):
            m = m.right
        self.right = m.right
        m.right.left = self
        n.left = None
        m.right = None
        return n

    def push(self, node):
        node.left = self
        m = node
        while m.right is not None and m.right != node:
            m = m.right
        m.right = self.right
        self.right.left = m
        self.right = node
        return self

    def __contains__(self, item):
        if self.value == item:
            return True
        n = self.right
        while n != self and n != None:
            if n.value == item:
                return True
            n = n.right
        return False
    
    def get(self, item):
        if self.value == item:
            return self
        n = self.right
        while n != self:
            if n.value == item:
                return n
            n = n.right
        return None
    
    def __repr__(self):
        out = [str(self.value)]
        n = self.right
        while n != self and n != None:
            out.append(str(n.value))
            n = n.right
        return ' '.join(out)


def simulate(cup, references, max_value):
    removed = cup.pop(3)
    d_val = cup.value - 1
    if d_val not in references:
        d_val = max_value
    while d_val in removed:
        d_val -= 1
        if d_val not in references:
            d_val = max_value
    destination = references[d_val]
    destination.push(removed)
    cup = cup.right
    return cup


def solve(data):
    max_value = max(data)
    node = Node(data.pop(0))
    references = {node.value: node}
    selected = node
    for d in data:
        n = Node(d)
        references[n.value] = n
        node.right = n
        n.left = node
        node = n
    node.right = selected
    selected.left = node

    for i in range(10, 1000000 + 1):
        n = Node(i)
        references[i] = n
        selected.left.push(n)
    max_value = 1000000
    for i in range(10000000):
        if i % 10**5 == 0:
            print(i)
        selected = simulate(selected, references, max_value)
    cup = selected.get(1)
    return cup.right.value * cup.right.right.value


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        data = []
        for c in lines[0]:
            data.append(int(c))
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
