import re
PTRN = r'^(https?://)?(www\.)?([a-z-]*)\..+$'

def domain_name(url):
    print(url)
    return re.match(PTRN, url).groups()[2]