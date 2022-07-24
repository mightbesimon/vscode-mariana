'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from decimal import Decimal
from unittest import TestCase, main
from .colour import Colour, hsla, rgba


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


class TestHSLA(AssertColour, TestCase):

	def test_init(self) -> None:
		c1 = hsla(10, 10, 10)
		self.assertIsInstance(c1, Colour)
		self.assertIsInstance(c1, hsla)
		self.assert_hsla(c1, 10, 0.1, 0.1, None)

		c2 = hsla(s=1, a=50)
		self.assert_hsla(c2, None, 1, None, 0.5)

	def test_clone(self) -> None:
		...

	def test_to_hsla(self) -> None:
		...

	def test_to_rgba(self) -> None:
		mint = hsla(114, 31, 68)
		self.assert_rgba(mint.to_rgba(), 153, 199, 148, None)

		orange = hsla(32, 85, 55)
		self.assert_rgba(orange.to_rgba(), 238, 147, 43, None)

	def test_to_hex(self) -> None:
		...


class TestRGBA(AssertColour, TestCase):

	def test_init(self) -> None:
		c = rgba(10, 10, 10)
		self.assertIsInstance(c, Colour)
		self.assertIsInstance(c, rgba)
		self.assert_rgba(c, 10, 10, 10, None)

		c = rgba(g=50, a=0.5)
		self.assert_rgba(c, None, 50, None, 0.5)

	def test_clone(self) -> None:
		...

	def test_to_hsla(self) -> None:
		...

	def test_to_rgba(self) -> None:
		...

	def test_to_hex(self) -> None:
		...


if __name__ == '__main__':
	main()
