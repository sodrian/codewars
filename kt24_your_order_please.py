import re
PTRN = r'[a-zA-Z]*(\d+)[a-zA-Z]*'


def order(sentence):
    print(sentence)
    ret = list()
    for el in sentence.split(' '):
        if el:
            d = re.findall(PTRN, el)[0]
            ret.append([d, el])
    print(ret)
    ret = sorted(ret, key=lambda el: el[0])
    return ' '.join([el[1] for el in ret])