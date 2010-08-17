#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sudoku.py
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
import thread
import time
import os

class Sudoku:
	def __init__(self):
		self.field   = [None, None, None, None, None, None, None, None, None,
						None, None, None, None, None, None, None, None, None,
						None, None, None, None, None, None, None, None, None,
						None, None, None, None, None, None, None, None, None,
						None, None, None, None, None, None, None, None, None,
						None, None, None, None, None, None, None, None, None,
						None, None, None, None, None, None, None, None, None,
						None, None, None, None, None, None, None, None, None,
						None, None, None, None, None, None, None, None, None]
	
	def load(self, stri):
		i = 0
		for chr in stri:
			if 48 < ord(chr) < 58:
				self.field[i] = int(chr)
				i += 1
			elif chr == 'x' or chr == '0' or chr == 'X' or chr == '?':
				i += 1
		return self.check_field(self.field)
		
	def print_field(self, field): 
		i = 0
		l = 0
		sys.stdout.write("+---------+---------+---------+\n")
		for f in field:
			if i % 9 == 0:
				sys.stdout.write("| ")
			if f is None:
				sys.stdout.write("? ")
			else:
				sys.stdout.write(str(f)+" ")
			
			if i % 3 == 2 and i != 0:
				sys.stdout.write("| ")
			else:
				sys.stdout.write(" ")
			if i % 9 == 8 and i != 0:
				l += 1
				sys.stdout.write("\n")
				if l % 3 == 0 and i != 0:
					sys.stdout.write("+---------+---------+---------+\n")
			i += 1
			
	def check_field(self, f):
		# Reihen
		for i in range(0,9):
			row = f[i*9:i*9+9]
			for j in range(1,10):
				if row.count(j) > 1:
					return False
			
		# Spalten
		for i in range(0,9):
			column = [f[i], f[9+i], f[18+i],
					  f[27+i], f[36+i], f[45+i],
					  f[54+i], f[63+i], f[72+i]]
			for j in range(1,10):
				if column.count(j) > 1:
					return False
			
		# Blöcke
		b1 = [f[0], f[1], f[2], f[9], f[10], f[11], f[18], f[19], f[20]]
		b2 = [f[3], f[4], f[5], f[12], f[13], f[14], f[21], f[22], f[23]]
		b3 = [f[6], f[7], f[8], f[15], f[16], f[17], f[24], f[25], f[26]]
		b4 = [f[27], f[28], f[29], f[36], f[37], f[38], f[45], f[46], f[47]]
		b5 = [f[30], f[31], f[32], f[39], f[40], f[41], f[48], f[49], f[50]]
		b6 = [f[33], f[34], f[35], f[42], f[43], f[44], f[51], f[52], f[53]]
		b7 = [f[54], f[55], f[56], f[63], f[64], f[65], f[72], f[73], f[74]]
		b8 = [f[57], f[58], f[59], f[66], f[67], f[68], f[75], f[76], f[77]]
		b9 = [f[60], f[61], f[62], f[69], f[70], f[71], f[78], f[79], f[80]]	
		for j in range(1,10):
			if b1.count(j) > 1 or b2.count(j) > 1 or b3.count(j) > 1 or b4.count(j) > 1 or b5.count(j) > 1 or b6.count(j) > 1 or b7.count(j) > 1 or b8.count(j) > 1 or b9.count(j) > 1:
				return False
		return True
	
	def solve(self):
		self.found = False
		self.cancel = False
		self.solve_clear_fields()
		thr = thread.start_new_thread(self.recsolve, (0, self.field))
		while not self.found:
			os.system("clear")
			self.print_field(self.field)
			time.sleep(1)
	
	def solve_quiet(self, nothing=None):
		self.found = False
		self.solve_clear_fields()
		self.cancel = False
		try:
			self.recsolve(0, self.field, True)
		except:
			pass
			
	def check_with(self, field, f, v):
		before = field[f]
		field[f] = v
		result = self.check_field(field)
		field[f] = before
	
	def solve_clear_fields(self):
		i = 0
		for f in self.field:
			if f is None:
				c = 0
				found = None
				for n in range(1,10):
					if self.check_with(self.field, i, n):
						found = n
						c += 1
				if c == 1:
					self.field[i] = found
			i += 1
		
	def recsolve(self, start, field, q = False):	
		if q and self.cancel:
			thread.exit()
		f = field
		if f[start] is None:
			some = False
			for n in range(1,10):
				f[start] = n
				
				if self.check_field(f):
					self.field = f
					some = True
					if f.count(None) == 0:
						if not q:
							print "GOT IT"
							self.found = True
							self.print_field(f)
							sys.exit(0)
						else:
							self.found = True
							self.field = f
							thread.exit()
					else:
						sub = self.recsolve(start+1, f, q)
						#if not sub:
						#	continue
				f[start] = None
			#if not some:
			#	pass
		else:
			self.recsolve(start+1, field, q)
