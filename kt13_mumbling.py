def accum(s):
    return '-'.join([(ch * i).capitalize() for i, ch in enumerate(s, 1)])