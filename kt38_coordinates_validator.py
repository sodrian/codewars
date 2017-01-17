"""Title: Coordinates Validator
URL: https://www.codewars.com/kata/coordinates-validator
Description:

You need to create a function that will validate if given parameters are valid geographical coordinates.

Valid coordinates look like the following: __"23.32353342, -32.543534534"__.
The return value should be either __true__ or __false__.

Latitude (which is first float) can be between 0 and 90, positive or negative.
Longitude (which is second float) can be between 0 and 180, positive or negative.

Coordinates can only contain digits, or one of the following symbols (including space after comma) __ -, . __

There should be no space between the minus "-" sign and the digit after it.

Here are some valid coordinates:

* -23, 25
* 24.53525235, 23.45235
* 04, -23.234235
* 43.91343345, 143
* 4, -3

And some invalid ones:

* 23.234, - 23.4234
* 2342.43536, 34.324236
* N23.43345, E32.6457
* 99.234, 12.324
* 6.325624, 43.34345.345
* 0, 1,2
* 0.342q0832, 1.2324
"""

import re
DIGIT_PTRN = r'^[-]?[\d]+[\.]?[\d]*$'


def is_valid_coordinates(coordinates):
    cs = list(map(float, [c if re.match(DIGIT_PTRN, c.strip()) else 1000 for c in coordinates.split(',')]))
    print(coordinates, cs)
    return len(cs) == 2 and -90 <= cs[0] <= 90 and -180 <= cs[1] <= 180