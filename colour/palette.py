'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from enum import Enum
from . import hsla

################################################################
#######                   base palette                   #######
################################################################
class Palette(Enum):
	...

################################################################
#######                     palettes                     #######
################################################################
class Mariana(Palette):
	BLACK     = hsla(  0,  0,  0, 25)
	GREY      = hsla(  0,  0, 20)
	MARIANA_0 = hsla(210, 15, 22)
	MARIANA_1 = hsla(210, 13, 40, 70)
	MARIANA_2 = hsla(210, 13, 45)
	MARIANA_3 = hsla(221, 12, 69)
	MARIANA_4 = hsla(219, 28, 88)
	RED_0     = hsla(357, 79, 65)
	RED_1     = hsla( 13, 93, 66)
	ORANGE    = hsla( 32, 93, 66)
	YELLOW    = hsla( 40, 94, 68, 25)
	MINT      = hsla(114, 31, 68)
	TEAL      = hsla(180, 36, 54)
	BLUE_0    = hsla(210, 50, 60)
	BLUE_1    = hsla(210, 60, 60)
	PURPLE    = hsla(300, 30, 68)
