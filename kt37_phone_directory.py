"""Title: Phone Directory
URL: https://www.codewars.com/kata/phone-directory
Description:

John keeps a backup of his old personal phone book as a text file. On each line of the file
he can find the phone number (formated as `+X-abc-def-ghij` where X stands for one or two digits), the corresponding name
between `<` and `>` and the address. 

Unfortunately everything is mixed, things are not
always in the same order, lines are cluttered with non-alpha-numeric characters.

Examples of John's phone book lines:

`"/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"`

`" 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"`

`"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"`

Could you help John with a program that, given the lines of his phone book and a phone number
returns a string for this number : `"Phone => num, Name => name, Address => adress"`

Examples:

```
s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."

```
It can happen that, for a few phone numbers, there are many people for a phone number -say `nb`- , then 

return : `"Error => Too many people: nb"` 

or it can happen that the number `nb` is not
in the phone book, in that case 

return: `"Error => Not found: nb"`

You can see other examples in the test cases.

JavaScript random tests completed by @matt c
"""

import re
MANY_PEOPLE_ERR = 'Error => Too many people: {0}'
NOT_FOUND_ERR = 'Error => Not found: {0}'
PHONE_PTRN = r'.?\+(\d{1,2}-\d{3}-\d{3}-\d{4}).?'
NAME_PTRN = r'<([a-zA-Z \']+)>'
TRASH_PTRN = r'[//;,]+'
SPACES_PTRN = r'[\s_]+'
PTRNS = [PHONE_PTRN, NAME_PTRN, TRASH_PTRN]


def format_line(line):
    phone = re.search(PHONE_PTRN, line)
    phone = phone and phone.groups()[0]
    name = re.search(NAME_PTRN, line)
    name = name and name.groups()[0]
    
    for ptrn in PTRNS:
        line = re.sub(ptrn, '', line)
    
    line = re.sub(SPACES_PTRN, ' ', line).strip()
    
    return 'Phone => {0}, Name => {1}, Address => {2}'.format(phone, name, line)


def phone(strng, num):
    ret = ''
    for line in strng.splitlines():
        if num in line:
            if not ret:
                ret = line
            else:
                return MANY_PEOPLE_ERR.format(num)
    return ret and format_line(ret) or NOT_FOUND_ERR.format(num)