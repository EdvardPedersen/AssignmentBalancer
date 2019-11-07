def read_groups(filename):
    groups = {}
    with open(filename, 'r') as f:
        for line in f:
            group, ta = line.strip().split(',')
            groups[int(group)] = ta
    return groups
