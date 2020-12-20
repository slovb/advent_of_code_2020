class Tile:
    def __init__(self, id, size = 10):
        self.id = id
        self.size = size
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
        for i in range(self.size):
            if (i, 0) in self.map:
                edges[0]['edge'].append(i)
            if (self.size - 1, i) in self.map:
                edges[1]['edge'].append(i)
            if (self.size - 1 - i, self.size - 1) in self.map:
                edges[2]['edge'].append(i)
            if (0, self.size - 1 - i) in self.map:
                edges[3]['edge'].append(i)
        for s in range(4):
            for i in edges[s]['edge'][::-1]:
                edges[s]['flip'].append(self.size - 1 - i)
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
    
    def verticalFlip(self):
        self.edges[0], self.edges[2] = self.edges[2], self.edges[0]
        for i in range(4):
            self.edges[i]['edge'], self.edges[i]['flip'] = self.edges[i]['flip'], self.edges[i]['edge']
        mup = set()
        for p in self.map:
            x, y = p
            mup.add((x, self.size - 1 - y))
        self.map = mup
        return self

    def horizontalFlip(self):
        self.clockwiseRotate().verticalFlip().clockwiseRotate().clockwiseRotate().clockwiseRotate()
        return self
    
    def clockwiseRotate(self):
        self.edges[0], self.edges[1], self.edges[2], self.edges[3] = self.edges[3], self.edges[0], self.edges[1], self.edges[2]
        mup = set()
        for p in self.map:
            x, y = p
            mup.add((self.size - 1 - y, x)) # (2, 1) => (8, 2)
        self.map = mup
        return self
    
    def __repr__(self):
        return str(self.id)
    
    def count_monsters(self):
        # assumption monsters don't overlap
        monster = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]
        total = 0
        for x in range(self.size - 19):
            for y in range(self.size - 2):
                has_monster = True
                for dx, dy in monster:
                    if (x + dx, y + dy) not in self.map:
                        has_monster = False
                        break
                if has_monster:
                    total += 1
        return total


def tile_to_array(tile):
    out = []
    for i in range(tile.size):
        out.append(['.']*tile.size)
    for p in tile.map:
        x, y = p
        out[y][x] = '#'
    return out


def paint(map):
    data = {}
    xmax = 0
    ymax = 0
    dy = 0
    for maprow in map:
        dx = 0
        for tile in maprow:
            painted_tile = tile_to_array(tile)
            for y, row in enumerate(painted_tile):
                for x, c in enumerate(row):
                    p = (x + dx, y + dy)
                    data[p] = c
                p = (x + dx + 1, y + dy)
                data[p] = ' '
            for x in range(10):
                p = (x + dx, y + dy + 1)
                data[p] = ' '
            data[(x + dx + 1, y + dy + 1)] = ' '
            xmax = max(xmax, x + dx + 1)
            ymax = max(ymax, y + dy + 1)
            dx += 11
        dy += 11
    rows = []
    for y in range(ymax): # skip the final empty
        row = []
        for x in range(xmax): # skip the final empty
            row.append(data[(x, y)])
        rows.append(''.join(row))
    return '\n'.join(rows)


def paint_internal(map):
    data = {}
    xmax = 0
    ymax = 0
    dy = 0
    for maprow in map:
        dx = 0
        for tile in maprow:
            painted_tile = tile_to_array(tile)
            for y, row in enumerate(painted_tile[1:9]):
                for x, c in enumerate(row[1:9]):
                    p = (x + dx, y + dy)
                    data[p] = c
            xmax = max(xmax, x + dx)
            ymax = max(ymax, y + dy)
            dx += 8
        dy += 8
    rows = []
    for y in range(ymax + 1):
        row = []
        for x in range(xmax + 1):
            row.append(data[(x, y)])
        rows.append(''.join(row))
    return '\n'.join(rows)


def paint_tile(tile):
    return '\n'.join([''.join(row) for row in tile_to_array(tile)]) + '\n'


def link(tiles):
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


def find_corners(tiles):
    corners = []
    for tid in tiles:
        if tiles[tid].count() == 2:
            corners.append(tid)
    return corners


def assemble(tiles):
    map = []
    start = tiles[find_corners(tiles)[0]]
    while start.edges[0]['adjacent'] is not None or start.edges[3]['adjacent'] is not None:
        start.clockwiseRotate()
    row = [start]
    left = start
    total = 1
    while total < len(tiles):
        right = left.edges[1]['adjacent']
        row.append(right)
        while right.edges[3]['adjacent'] != left:
            right.clockwiseRotate()
        if left.edges[1]['edge'] != right.edges[3]['flip']:
            right.verticalFlip()
        left = right
        total += 1
        if left.count() == start.count() and total < len(tiles):
            map.append(row)
            left = start.edges[2]['adjacent']
            while left.edges[0]['adjacent'] != start:
                left.clockwiseRotate()             
            if start.edges[2]['edge'] != left.edges[0]['flip']:
                left.horizontalFlip()
            start = left
            row = [start]
            total += 1
    map.append(row)
    return map 


def make_master_tile(map):
    internal = paint_internal(map)
    tile = Tile(0, 8 * len(map))
    for y, row in enumerate(internal.split('\n')):
        for x, c in enumerate(row):
            if c == '#':
                tile.add_pos((x, y))
    tile.build_edges()
    return tile


def solve(tiles):
    link(tiles)
    map = assemble(tiles)
    tile = make_master_tile(map)
    rotations = 0
    while tile.count_monsters() == 0:
        tile.clockwiseRotate()
        rotations += 1
        if rotations == 4:
            tile.verticalFlip()
    return len(tile.map) - 15 * tile.count_monsters()


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
