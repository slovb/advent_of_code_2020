class Tile:
    def __init__(self, id):
        self.id = id
        self.edges = {}
        self.map = set()
        self.total = 0

    def add_pos(self, pos):
        self.map.add(pos)
    
    def build_edges(self):
        edges = {}
        for s in range(4):
            edges[s] = {
                'edge': [],
                'flip': [],
                'adjacent': None
            }
        for i in range(10):
            if (i, 0) in self.map:
                edges[0]['edge'].append(i)
            if (9, i) in self.map:
                edges[1]['edge'].append(i)
            if (9 - i, 9) in self.map:
                edges[2]['edge'].append(i)
            if (0, 9 - i) in self.map:
                edges[3]['edge'].append(i)
        for s in range(4):
            for i in edges[s]['edge'][::-1]:
                edges[s]['flip'].append(9 - i)
        self.edges = edges

    def match(self, tile):
        for seid in self.edges:
            se = self.edges[seid]
            if se['adjacent'] == tile:
                return True
        for seid in self.edges:
            se = self.edges[seid]
            if se['adjacent'] is not None:
                continue
            for teid in tile.edges:
                te = tile.edges[teid]
                if te['adjacent'] is not None:
                    continue
                if se['edge'] == te['flip'] or se['edge'] == te['edge']:
                    se['adjacent'] = tile
                    te['adjacent'] = self
                    self.total += 1
                    tile.total += 1
                    return True
        return False
    
    def count(self):
        return self.total
    
    def __repr__(self):
        return str(self.edges)


def solve(tiles):
    for tid0 in tiles:
        for tid1 in tiles:
            if tid0 == tid1:
                continue
            tile0 = tiles[tid0]
            tile1 = tiles[tid1]
            if tile1.count() == 4:
                continue
            if tile0.match(tile1):
                if tile0.count() == 4:
                    break
    product = 1
    for tid in tiles:
        if tiles[tid].count() == 2:
            print(tid)
            product *= tid
    return product


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        tiles = {}
        i = 0
        while i < len(lines):
            line = lines[i]
            id = int(line[5:9])
            tile = Tile(id)
            i += 1
            for y, line in enumerate(lines[i:i+10]):
                for x, c in enumerate(line):
                    if c == '#':
                        tile.add_pos((x, y))
            i += y + 2
            tile.build_edges()
            tiles[id] = tile
        return tiles

def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
