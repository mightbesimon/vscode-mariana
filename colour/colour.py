'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from abc import ABC
from dataclasses import dataclass
from decimal import Decimal
from typing import Tuple


class Colour(ABC):
	'''	abstract base `Colour` class
	'''

	def to_hsla(self) -> 'hsla':
		raise NotImplemented

	def to_rgba(self) -> 'rgba':
		raise NotImplemented

	def to_hex(self) -> str:
		c = self.to_rgba()
		alpha = f'{c.a:02x}' if c.a and c.a!=1 else ''
		return f'#{c.r:02x}{c.g:02x}{c.b:02x}{alpha}'


@dataclass
class hsla(Colour):
	h: int     = None	# hue        [0  , 359]
	s: Decimal = None	# saturation [0.0, 1.0]
	l: Decimal = None	# lightness  [0.0, 1.0]
	a: Decimal = None	# alpha      [0.0, 1.0]

	def __init__(self,
		h:int=None,
		s:Decimal=None,
		l:Decimal=None,
		a:Decimal=None,
	) -> None:
		'''	`h`: hue `[0, 359]`
			`s`: saturation `[0, 100]` or `[0.0, 1.0]`
			`l`: lightness `[0, 100]` or `[0.0, 1.0]`
			`a`: alpha `[0, 100]` or `[0.0, 1.0]`
		'''
		if h and not 0<=h<=359: raise ValueError(f'hue {h} not in range [0, 359]')
		if s and not 0<=s<=100: raise ValueError(f'saturation {s} not in range [0, 100] or [0.0, 1.0]')
		if l and not 0<=l<=100: raise ValueError(f'lightness {l} not in range [0, 100] or [0.0, 1.0]')
		if a and not 0<=a<=100: raise ValueError(f'alpha {a} not in range [0, 100] or [0.0, 1.0]')

		if h: self.h = h
		if s: self.s = s/100 if s>1 else s
		if l: self.l = l/100 if l>1 else l
		if a: self.a = a/100 if a>1 else a

	def clone(self,
		h:int=None,
		s:Decimal=None,
		l:Decimal=None,
		a:Decimal=None,
	) -> 'hsla':
		'''	create a new instance of `hsla`,
			optionally modify value fields
		'''
		return self.__class__(
			h=h if h else self.h,
			s=s if s else self.s,
			l=l if l else self.l,
			a=a if a else self.a,
		)

	def to_hsla(self) -> 'hsla':
		return self

	def to_rgba(self) -> 'rgba':
		'''	[formula](https://www.rapidtables.com/convert/color/hsl-to-rgb.html)
		'''
		C = (1 - abs(2*self.l - 1)) * self.s
		X = C * (1 - abs(self.h/60%2 - 1))
		m = self.l - C/2

		table = {
			(0, 60): (C, X, 0),
			(60, 120): (X, C, 0),
			(120, 180): (0, C, X),
			(180, 240): (0, X, C),
			(240, 300): (X, 0, C),
			(300, 360): (C, 0, X),
		}

		for key, value in table.items():
			if not key[0]<=self.h<key[1]: continue
			r_, g_, b_ = value

			return rgba(
				r=round((r_+m) * 255),
				g=round((g_+m) * 255),
				b=round((b_+m) * 255),
				a=self.a,
			)


@dataclass
class rgba(Colour):
	r: int     = None	# red   [0  , 255]
	g: int     = None	# green [0  , 255]
	b: int     = None	# blue  [0  , 255]
	a: Decimal = None	# alpha [0.0, 1.0]

	def __init__(self,
		r:int=None,
		g:int=None,
		b:int=None,
		a:Decimal=None,
	) -> None:
		'''	`r`: red `[0, 255]`
			`g`: green `[0, 255]`
			`b`: blue `[0, 255]`
			`a`: alpha `[0, 100]` or `[0.0, 1.0]`
		'''
		if r and not 0<=r<=255: raise ValueError(f'red {r} not in range [0, 255]')
		if g and not 0<=g<=255: raise ValueError(f'green {g} not in range [0, 255]')
		if b and not 0<=b<=255: raise ValueError(f'blue {b} not in range [0, 255]')
		if a and not 0<=a<=100: raise ValueError(f'alpha {a} not in range [0, 100] or [0.0, 1.0]')

		if r: self.r = r
		if g: self.g = g
		if b: self.b = b
		if a: self.a = a/100 if a>1 else a

	def clone(self,
		r:int=None,
		g:int=None,
		b:int=None,
		a:Decimal=None,
	) -> 'rgba':
		'''	create a new instance of `rgba`,
			optionally modify value fields
		'''
		return self.__class__(
			r=r if r else self.r,
			g=g if g else self.g,
			b=b if b else self.b,
			a=a if a else self.a,
		)

	def normalise(self) -> Tuple[int, int, int]:
		return (self.r/255, self.g/255, self.b/255)

	def to_hsla(self) -> 'hsla':
		'''	[formula](https://www.rapidtables.com/convert/color/rgb-to-hsl.html)
		'''
		r_, g_, b_ = self.normalise()
		C_max = max(r_, g_, b_)
		C_min = min(r_, g_, b_)
		delta = C_max - C_min

		H = round(
			0 if delta==0 else
			60 * ((g_-b_)/delta % 6) if C_max==r_ else
			60 * ((b_-r_)/delta + 2) if C_max==g_ else
			60 * ((r_-g_)/delta + 4) if C_max==b_ else
			None
		)
		L = round((C_max+C_min) / 2, 2)
		S = round(delta / (1 - abs(2*L - 1)), 2)

		return hsla(H, S, L, self.a)

	def to_rgba(self) -> 'rgba':
		return self
