'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from decimal import Decimal
from unittest import TestCase, main
from . import Colour, hsla, rgba


################################################################
#######                   base classes                   #######
################################################################
class AssertColour:

	def assert_hsla(self,
		colour:hsla,
		h:int,
		s:Decimal,
		l:Decimal,
		a:Decimal
	) -> None:
		self.assertEqual(colour.h, h)
		self.assertEqual(colour.s, s)
		self.assertEqual(colour.l, l)
		self.assertEqual(colour.a, a)

	def assert_rgba(self,
		colour:rgba,
		r:int,
		g:Decimal,
		b:Decimal,
		a:Decimal
	) -> None:
		self.assertEqual(colour.r, r)
		self.assertEqual(colour.g, g)
		self.assertEqual(colour.b, b)
		self.assertEqual(colour.a, a)


################################################################
#######                      tests                       #######
################################################################
class TestHSLA(AssertColour, TestCase):

	def test_init(self) -> None:
		c1 = hsla(10, 10, 10)
		self.assertIsInstance(c1, Colour)
		self.assertIsInstance(c1, hsla)
		self.assert_hsla(c1, 10, 0.1, 0.1, None)

		c2 = hsla(s=1, a=50)
		self.assert_hsla(c2, None, 1, None, 0.5)

	def test_clone(self) -> None:
		c1 = hsla(10, 10, 10)
		c2 = c1.clone()
		c3 = c1.clone(h=30)
		c4 = c3.clone(a=0.5)

		self.assert_hsla(c2, 10, 0.1, 0.1, None)
		self.assert_hsla(c3, 30, 0.1, 0.1, None)
		self.assert_hsla(c4, 30, 0.1, 0.1, 0.5)

	def test_to_hsla(self) -> None:
		...

	def test_to_rgba(self) -> None:
		mint = hsla(114, 31, 68)
		self.assert_rgba(mint.to_rgba(), 153, 199, 148, None)

		orange = hsla(32, 85, 55)
		self.assert_rgba(orange.to_rgba(), 238, 147, 43, None)

	def test_to_hex(self) -> None:
		mint = hsla(114, 31, 68)
		self.assertEqual(mint.to_hex(), '#99c794')

		orange = hsla(32, 85, 55, 100)
		self.assertEqual(orange.to_hex(), '#ee932b')


class TestRGBA(AssertColour, TestCase):

	def test_init(self) -> None:
		c = rgba(10, 10, 10)
		self.assertIsInstance(c, Colour)
		self.assertIsInstance(c, rgba)
		self.assert_rgba(c, 10, 10, 10, None)

		c = rgba(g=50, a=0.5)
		self.assert_rgba(c, None, 50, None, 0.5)

	def test_clone(self) -> None:
		c1 = rgba(10, 10, 10)
		c2 = c1.clone()
		c3 = c1.clone(r=30)
		c4 = c3.clone(a=0.5)

		self.assert_rgba(c2, 10, 10, 10, None)
		self.assert_rgba(c3, 30, 10, 10, None)
		self.assert_rgba(c4, 30, 10, 10, 0.5)

	def test_to_hsla(self) -> None:
		mint = rgba(153, 199, 148)
		self.assert_hsla(mint.to_hsla(), 114, 0.31, 0.68, None)

		orange = rgba(238, 147, 43)
		self.assert_hsla(orange.to_hsla(), 32, 0.85, 0.55, None)

	def test_to_rgba(self) -> None:
		...

	def test_to_hex(self) -> None:
		mint = rgba(153, 199, 148, 100)
		self.assertEqual(mint.to_hex(), '#99c794')

		orange = rgba(238, 147, 43, 100)
		self.assertEqual(orange.to_hex(), '#ee932b')


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':
	main()
