'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from abc import ABC
from dataclasses import dataclass
from decimal import Decimal


class Colour(ABC):
	'''	abstract base `Colour` class
	'''

	def to_hsla(self) -> 'hsla':
		raise NotImplemented

	def to_rgba(self) -> 'rgba':
		raise NotImplemented

	def to_hex(self) -> str:
		c = self.to_rgba()
		return ''


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
		if h and not 0<=h<360: raise ValueError('hue not in range [0, 359]')
		if s and not 0<=s<=100: raise ValueError('saturation not in range [0, 100] or [0.0, 1.0]')
		if l and not 0<=l<=100: raise ValueError('lightness not in range [0, 100] or [0.0, 1.0]')
		if a and not 0<=a<=100: raise ValueError('alpha not in range [0, 100] or [0.0, 1.0]')

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
		raise NotImplemented


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
		if r and not 0<=r<=255: raise ValueError('red not in range [0, 255]')
		if g and not 0<=g<=255: raise ValueError('green not in range [0, 255]')
		if b and not 0<=b<=255: raise ValueError('blue not in range [0, 255]')
		if a and not 0<=a<=100: raise ValueError('alpha not in range [0, 100] or [0.0, 1.0]')

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

	def to_hsla(self) -> 'hsla':
		raise NotImplemented

	def to_rgba(self) -> 'rgba':
		return self
