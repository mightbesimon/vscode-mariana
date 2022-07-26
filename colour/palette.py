'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from itertools import chain
from typing import List, Tuple
from . import Colour, hsla, rgba

################################################################
#######                    metaclass                     #######
################################################################
class MetaPalette(type):

	def __iter__(self) -> List[Tuple[str, Colour]]:
		iter_self = ( (name, attr)
			for name, attr in self.__dict__.items()
			if isinstance(attr, Colour)
		)
		try:
			return chain(iter_self, ( (name, attr)
				for name, attr in self.__base__
				if isinstance(attr, Colour)
			))
		except TypeError:
			return iter_self

	def __contains__(self, obj:Colour) -> bool:
		in_self = obj in [ attr
			for name, attr in self.__dict__.items()
			if isinstance(attr, Colour)
		]
		try:
			return in_self or obj in self.__base__
		except TypeError:
			return in_self

################################################################
#######                   base palette                   #######
################################################################
class Palette(metaclass=MetaPalette):
	BLACK  = rgba(  0,   0,   0)
	WHITE  = rgba(255, 255, 255)
	SHADOW = BLACK.clone(a=50)
	TRANSPARENT = BLACK.clone(a=0)

################################################################
#######                     palettes                     #######
################################################################
class Mariana(Palette):
	MARIANA  = hsla(210, 15, 22)
	DARK_0   = MARIANA.clone(l=11)
	DARK_1   = MARIANA.clone(l=13)
	DARK_2   = MARIANA.clone(l=19)
	MEDIUM_0 = MARIANA.clone()
	MEDIUM_1 = MARIANA.clone(l=40, a=75)
	MEDIUM_2 = MARIANA.clone(l=45)
	LIGHT_0  = hsla(220, 12, 69)
	LIGHT_1  = hsla(220, 28, 88)
	RED_0    = hsla(357, 79, 65)
	RED_1    = hsla( 13, 93, 66)
	ORANGE   = hsla( 32, 93, 66)
	YELLOW   = hsla( 40, 94, 68)
	MINT     = hsla(114, 31, 68)
	TEAL     = hsla(180, 36, 54)
	BLUE     = hsla(210, 50, 60)
	PURPLE   = hsla(300, 30, 68)
