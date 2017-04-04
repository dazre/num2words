# -*- encoding: utf-8 -*-
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from unittest import TestCase

from num2words import num2words

class Num2WordsRUTest(TestCase):

    def test_cardinal(self):
        self.assertEqual(num2words(5, lang='ru'), u"пять")
        self.assertEqual(num2words(15, lang='ru'), u"пятнадцать")
        self.assertEqual(num2words(154, lang='ru'), u"сто пятьдесят четыре")
        self.assertEqual(num2words(1135, lang='ru'), u"одна тысяча сто тридцать пять")
        self.assertEqual(num2words(418531, lang='ru'), u"четыреста восемнадцать тысяч пятьсот тридцать один")
        self.assertEqual(num2words(1000139, lang='ru'), u"один миллион сто тридцать девять")

    def test_floating_point(self):
        self.assertEqual(num2words(5.2, lang='ru'), u"пять запятая два")
        self.assertEqual(num2words(561.42, lang='ru'), u"пятьсот шестьдесят один запятая сорок два")
