"""Title: Extract the domain name from a URL
URL: https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1
Description:

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
```ruby
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```
```python
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```
```javascript
domainName("http://github.com/carbonfive/raygun") == "github" 
domainName("http://www.zombie-bites.com") == "zombie-bites"
domainName("https://www.cnet.com") == "cnet"
```
"""

import re
PTRN = r'^(https?://)?(www\.)?([a-z-]*)\..+$'

def domain_name(url):
    print(url)
    return re.match(PTRN, url).groups()[2]