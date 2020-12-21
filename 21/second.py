def solve(data):
    processed = {}
    solved = set()
    for ingredients, allergens in data:
        for allergen in allergens:
            if allergen not in processed:
                processed[allergen] = []
                for ingredient in ingredients:
                    if ingredient not in solved:
                        processed[allergen].append(ingredient)
            else:
                # remove ingredients that don't appear twice
                to_remove = []
                for ingredient in processed[allergen]:
                    if ingredient not in ingredients:
                        to_remove.append(ingredient)
                for ingredient in to_remove:
                    processed[allergen].remove(ingredient)
                if len(processed[allergen]) == 1:
                    ingredient = processed[allergen][0]
                    solved.add(ingredient)
                    for a in processed:
                        if a != allergen and ingredient in processed[a]:
                            processed[a].remove(ingredient)
                            if len(processed[a]) == 1:
                                solved.add(processed[a][0])
    while len(solved) < len(processed):
        for allergen in processed:
            if len(processed[allergen]) == 1:
                ingredient = processed[allergen][0]
                solved.add(ingredient)
                for a in processed:
                    if a != allergen and ingredient in processed[a]:
                        processed[a].remove(ingredient)
    keys = sorted([a for a in processed])
    allergens = [processed[key][0] for key in keys]
    return ','.join(allergens)


def read(filename):
    def process(line):
        ingredients = line.split(' (contains')[0].split(' ')
        allergens = line.split(' (contains ')[1].rstrip(')').split(', ')
        return (ingredients, allergens)
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        return [process(line) for line in lines]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
