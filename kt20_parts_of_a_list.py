def partlist(arr):
    ret = []
    for i in range(len(arr) - 1):
        ret.append((' '.join(arr[:i+1]), ' '.join(arr[i+1:])))
    return ret