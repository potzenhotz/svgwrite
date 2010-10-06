#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: test text module
# Created: 25.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import unittest

from svgwrite import TSpan, TRef, TextPath, parameter

class TestTSpan(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_constructor(self):
        txt = TSpan('testtext')
        self.assertEqual(txt.tostring(), '<tspan>testtext</tspan>')

    def test_insert(self):
        txt = TSpan('testtext', insert=(1,1))
        self.assertEqual(txt.tostring(), '<tspan x="1" y="1">testtext</tspan>')

    def test_subelement(self):
        txt = TSpan('testtext')
        txt.add(TSpan('subtext1'))
        txt.add(TSpan('subtext2'))
        self.assertEqual(txt.tostring(), '<tspan>testtext<tspan>subtext1</tspan><tspan>subtext2</tspan></tspan>')

    def test_x_values(self):
        txt = TSpan('text', x=[1,2,3,4])
        self.assertEqual(txt.tostring(), '<tspan x="1 2 3 4">text</tspan>')

    def test_y_values(self):
        txt = TSpan('text', y=[1,2,3,4])
        self.assertEqual(txt.tostring(), '<tspan y="1 2 3 4">text</tspan>')

    def test_dx_values(self):
        txt = TSpan('text', dx=[1,2,3,4])
        self.assertEqual(txt.tostring(), '<tspan dx="1 2 3 4">text</tspan>')

    def test_dy_values(self):
        txt = TSpan('text', dy=[1,2,3,4])
        self.assertEqual(txt.tostring(), '<tspan dy="1 2 3 4">text</tspan>')

    def test_rotate_values(self):
        txt = TSpan('text', rotate=[1,2,3,4])
        self.assertEqual(txt.tostring(), '<tspan rotate="1 2 3 4">text</tspan>')

    def test_subelement_tspan(self):
        txt = TSpan('text')
        txt.tspan('subtext')
        self.assertEqual(txt.tostring(), '<tspan>text<tspan>subtext</tspan></tspan>')


    def test_errors(self):
        # None for x, y, dx, dy, rotate is valid - willl be ignored
        self.assertRaises(TypeError, TSpan,"txt", x=1)
        self.assertRaises(TypeError, TSpan,"txt", y=1)
        self.assertRaises(TypeError, TSpan,"txt", dx=1)
        self.assertRaises(TypeError, TSpan,"txt", dy=1)
        self.assertRaises(TypeError, TSpan,"txt", rotate=1)

    def test_insert_errors(self):
        self.assertRaises(TypeError, TSpan, "txt", insert=1)
        self.assertRaises(TypeError, TSpan, "txt", insert='1')
        # do not use 'insert' and 'x' or 'y' at the same time
        self.assertRaises(ValueError, TSpan, "txt", insert=(1,1), x=[1])
        self.assertRaises(ValueError, TSpan, "txt", insert=(1,1), y=[1])

class TestTRef(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_constructor(self):
        tref = TRef('test')
        self.assertEqual(tref.tostring(), '<tref xlink:href="#test" />')

class TestTextPath(unittest.TestCase):
    def setUp(self):
        parameter.set_debug(True)

    def test_constructor(self):
        tref = TextPath('test', 'The Text', startOffset=10, spacing='auto', method='stretch')
        self.assertEqual(tref.tostring(), '<textPath method="stretch" spacing="auto"' \
                         ' startOffset="10" xlink:href="#test">The Text</textPath>')

    def test_subelement_tspan(self):
        txt = TextPath('test', 'text')
        txt.tspan('subtext')
        self.assertEqual(txt.tostring(), '<textPath xlink:href="#test">text<tspan>subtext</tspan></textPath>')

if __name__=='__main__':
    unittest.main()