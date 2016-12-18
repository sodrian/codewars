def find_it(seq):
    print(seq)
    d = dict()
    for num in seq:
        d[num] = d.get(num, 0) + 1 

    l = []
    for k, v in d.items():
        if not l:
            l.append([k, v])
        elif l and v > l[0][1]:
            l.insert(0, [k, v])
        else:
            l.append([k, v])
    
    for el in l:
        if el[1] % 2:
            return el[0]