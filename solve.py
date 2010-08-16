#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       solve.py
#       
#       Copyright 2010 Raphael Michel <webmaster@raphaelmichel.de>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
import sys

import sudoku

def help():
	print "SUDOKU solve.py von Raphael Michel"
	print "./solve.py sudoku-datei"
	
def main():
	
	if len(sys.argv) < 2:
		help()
		return 0
	
	try:
		f = open(sys.argv[1])
		s = f.read()
		f.close()
	except IOError:
		print "Die Datei konnte nicht gelesen werden."
		return 0
	
	sud = sudoku.Sudoku()
	if not sud.load(s):
		print "Ungültiges Sudoku!"
		return 0
		
	sud.print_field(sud.field)
	sud.solve()
	
if __name__ == '__main__':
	main()
