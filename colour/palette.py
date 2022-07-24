'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from enum import Enum
from . import hsla, rgba

################################################################
#######                   base palette                   #######
################################################################
class Palette(Enum):
	...

################################################################
#######                     palettes                     #######
################################################################
class Mariana(Palette):
	MARIANA_0 = hsla(210, 15, 22)
	MARIANA_1 = hsla(210, 13, 40, 75)
	MARIANA_2 = hsla(210, 13, 45)
	MARIANA_3 = hsla(221, 12, 69)
	MARIANA_4 = hsla(219, 28, 88)
	RED_0     = hsla(357, 79, 65)
	RED_1     = hsla( 13, 93, 66)
	ORANGE    = hsla( 32, 93, 66)
	YELLOW    = hsla( 40, 94, 68)
	MINT      = hsla(114, 31, 68)
	TEAL      = hsla(180, 36, 54)
	BLUE      = hsla(210, 50, 60)
	PURPLE    = hsla(300, 30, 68)

class Dark(Palette):
	DARK_0 = rgba(10, 10, 10)
	DARK_1 = rgba(25, 25, 25)
	DARK_2 = rgba(50, 50, 50)
