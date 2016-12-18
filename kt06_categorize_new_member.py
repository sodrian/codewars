def openOrSenior(data):
    r = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            r.append('Senior')
        else:
            r.append('Open')
    return r