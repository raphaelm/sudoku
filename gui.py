#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       gui.py
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
import time
import thread

import gtk

import sudoku

def err(text, sectext = None):
	if sectext is None:
		error_dlg = gtk.MessageDialog(type=gtk.MESSAGE_ERROR
					, message_format=text
					, buttons=gtk.BUTTONS_OK)
	else:
		error_dlg = gtk.MessageDialog(type=gtk.MESSAGE_ERROR
					, message_format=text
					, buttons=gtk.BUTTONS_OK)
		error_dlg.format_secondary_text(sectext)
	error_dlg.run()
	error_dlg.destroy()
	
class MainWindow(gtk.Window):
	
	def ev_leave(self, this):
		self.destroy()
	
	def __init__(self):
		gtk.Window.__init__(self)
		
		self.tbl = gtk.Table(12,12)
		self.tbl.show()
		
		self.fields = []
		
		for i in range(0,81):
			new = gtk.Entry()
			new.set_width_chars(2)
			new.set_max_length(1)
			self.fields.append(new)
		
		self.shb1 = gtk.HBox()
		self.shb1.show()
		self.tbl13 = gtk.Table()
		self.tbl13.attach(self.fields[6], 0, 1, 0, 1)
		self.tbl13.attach(self.fields[7], 1, 2, 0, 1)
		self.tbl13.attach(self.fields[8], 2, 3, 0, 1)
		self.tbl13.attach(self.fields[15], 0, 1, 1, 2)
		self.tbl13.attach(self.fields[16], 1, 2, 1, 2)
		self.tbl13.attach(self.fields[17], 2, 3, 1, 2)
		self.tbl13.attach(self.fields[24], 0, 1, 2, 3)
		self.tbl13.attach(self.fields[25], 1, 2, 2, 3)
		self.tbl13.attach(self.fields[26], 2, 3, 2, 3)
		self.tbl13.show()
		
		self.tbl12 = gtk.Table()
		self.tbl12.attach(self.fields[3], 0, 1, 0, 1)
		self.tbl12.attach(self.fields[4], 1, 2, 0, 1)
		self.tbl12.attach(self.fields[5], 2, 3, 0, 1)
		self.tbl12.attach(self.fields[12], 0, 1, 1, 2)
		self.tbl12.attach(self.fields[13], 1, 2, 1, 2)
		self.tbl12.attach(self.fields[14], 2, 3, 1, 2)
		self.tbl12.attach(self.fields[21], 0, 1, 2, 3)
		self.tbl12.attach(self.fields[22], 1, 2, 2, 3)
		self.tbl12.attach(self.fields[23], 2, 3, 2, 3)
		self.tbl12.show()
		
		self.tbl11 = gtk.Table()
		self.tbl11.attach(self.fields[0], 0, 1, 0, 1)
		self.tbl11.attach(self.fields[1], 1, 2, 0, 1)
		self.tbl11.attach(self.fields[2], 2, 3, 0, 1)
		self.tbl11.attach(self.fields[9], 0, 1, 1, 2)
		self.tbl11.attach(self.fields[10], 1, 2, 1, 2)
		self.tbl11.attach(self.fields[11], 2, 3, 1, 2)
		self.tbl11.attach(self.fields[18], 0, 1, 2, 3)
		self.tbl11.attach(self.fields[19], 1, 2, 2, 3)
		self.tbl11.attach(self.fields[20], 2, 3, 2, 3)
		self.tbl11.show()
		self.shb1.pack_end(self.tbl13, True, False, 10)
		self.shb1.pack_end(self.tbl12, True, False, 10)
		self.shb1.pack_end(self.tbl11, True, False, 10)
		
		self.shb2 = gtk.HBox()
		self.shb2.show()
		self.tbl23 = gtk.Table()
		self.tbl23.attach(self.fields[33], 0, 1, 0, 1)
		self.tbl23.attach(self.fields[34], 1, 2, 0, 1)
		self.tbl23.attach(self.fields[35], 2, 3, 0, 1)
		self.tbl23.attach(self.fields[42], 0, 1, 1, 2)
		self.tbl23.attach(self.fields[43], 1, 2, 1, 2)
		self.tbl23.attach(self.fields[44], 2, 3, 1, 2)
		self.tbl23.attach(self.fields[51], 0, 1, 2, 3)
		self.tbl23.attach(self.fields[52], 1, 2, 2, 3)
		self.tbl23.attach(self.fields[53], 2, 3, 2, 3)
		self.tbl23.show()
		
		self.tbl22 = gtk.Table()
		self.tbl22.attach(self.fields[30], 0, 1, 0, 1)
		self.tbl22.attach(self.fields[31], 1, 2, 0, 1)
		self.tbl22.attach(self.fields[32], 2, 3, 0, 1)
		self.tbl22.attach(self.fields[39], 0, 1, 1, 2)
		self.tbl22.attach(self.fields[40], 1, 2, 1, 2)
		self.tbl22.attach(self.fields[41], 2, 3, 1, 2)
		self.tbl22.attach(self.fields[48], 0, 1, 2, 3)
		self.tbl22.attach(self.fields[49], 1, 2, 2, 3)
		self.tbl22.attach(self.fields[50], 2, 3, 2, 3)
		self.tbl22.show()
		
		self.tbl21 = gtk.Table()
		self.tbl21.attach(self.fields[27], 0, 1, 0, 1)
		self.tbl21.attach(self.fields[28], 1, 2, 0, 1)
		self.tbl21.attach(self.fields[29], 2, 3, 0, 1)
		self.tbl21.attach(self.fields[36], 0, 1, 1, 2)
		self.tbl21.attach(self.fields[37], 1, 2, 1, 2)
		self.tbl21.attach(self.fields[38], 2, 3, 1, 2)
		self.tbl21.attach(self.fields[45], 0, 1, 2, 3)
		self.tbl21.attach(self.fields[46], 1, 2, 2, 3)
		self.tbl21.attach(self.fields[47], 2, 3, 2, 3)
		self.tbl21.show()
		self.shb2.pack_end(self.tbl23, True, False, 10)
		self.shb2.pack_end(self.tbl22, True, False, 10)
		self.shb2.pack_end(self.tbl21, True, False, 10)
	
		self.shb3 = gtk.HBox()
		self.shb3.show()
		self.tbl33 = gtk.Table()
		self.tbl33.attach(self.fields[60], 0, 1, 0, 1)
		self.tbl33.attach(self.fields[61], 1, 2, 0, 1)
		self.tbl33.attach(self.fields[62], 2, 3, 0, 1)
		self.tbl33.attach(self.fields[69], 0, 1, 1, 2)
		self.tbl33.attach(self.fields[70], 1, 2, 1, 2)
		self.tbl33.attach(self.fields[71], 2, 3, 1, 2)
		self.tbl33.attach(self.fields[78], 0, 1, 2, 3)
		self.tbl33.attach(self.fields[79], 1, 2, 2, 3)
		self.tbl33.attach(self.fields[80], 2, 3, 2, 3)
		self.tbl33.show()
		
		self.tbl32 = gtk.Table()
		self.tbl32.attach(self.fields[57], 0, 1, 0, 1)
		self.tbl32.attach(self.fields[58], 1, 2, 0, 1)
		self.tbl32.attach(self.fields[59], 2, 3, 0, 1)
		self.tbl32.attach(self.fields[66], 0, 1, 1, 2)
		self.tbl32.attach(self.fields[67], 1, 2, 1, 2)
		self.tbl32.attach(self.fields[68], 2, 3, 1, 2)
		self.tbl32.attach(self.fields[75], 0, 1, 2, 3)
		self.tbl32.attach(self.fields[76], 1, 2, 2, 3)
		self.tbl32.attach(self.fields[77], 2, 3, 2, 3)
		self.tbl32.show()
		
		self.tbl31 = gtk.Table()
		self.tbl31.attach(self.fields[54], 0, 1, 0, 1)
		self.tbl31.attach(self.fields[55], 1, 2, 0, 1)
		self.tbl31.attach(self.fields[56], 2, 3, 0, 1)
		self.tbl31.attach(self.fields[63], 0, 1, 1, 2)
		self.tbl31.attach(self.fields[64], 1, 2, 1, 2)
		self.tbl31.attach(self.fields[65], 2, 3, 1, 2)
		self.tbl31.attach(self.fields[72], 0, 1, 2, 3)
		self.tbl31.attach(self.fields[73], 1, 2, 2, 3)
		self.tbl31.attach(self.fields[74], 2, 3, 2, 3)
		self.tbl31.show()
		self.shb3.pack_end(self.tbl33, True, False, 10)
		self.shb3.pack_end(self.tbl32, True, False, 10)
		self.shb3.pack_end(self.tbl31, True, False, 10)
		
		self.buttonbox = gtk.HBox()
		
		self.solvebutton = gtk.Button('Lösen')
		
		self.buttonbox.pack_end(self.solvebutton)
		
		self.svb = gtk.VBox()		
		self.svb.pack_end(self.buttonbox, True, True, 10)
		self.svb.pack_end(self.shb3, True, True, 10)
		self.svb.pack_end(self.shb2, True, True, 10)
		self.svb.pack_end(self.shb1, True, True, 10)
		self.svb.show()
		
		# statusbar
		self.statusbar = gtk.Statusbar()
		self.statusbar.push(0, 'Hallo!')
		
		# vbox to combine menubar and notebook
		main_vbox = gtk.VBox()
		main_vbox.pack_end(self.statusbar, False, False)
		main_vbox.pack_end(self.svb)
		main_vbox.show()
		
		self.add(main_vbox)
		
class SolveDialog(gtk.Dialog):
	def __init__(self, title = None, parent = None, flags = 0, buttons = None):
		gtk.Dialog.__init__(self, title, parent, flags, buttons)
		self.pg = gtk.ProgressBar()
		self.pg.show()
		self.pg.set_pulse_step(0.2)
		carea = self.get_content_area()
		vbox = gtk.VBox()
		vbox.pack_end(self.pg)
		lb = gtk.Label('Lösung wird berechnet...')
		lb.show()
		vbox.pack_end(lb)
		vbox.show()
		carea.add(vbox)
		self.show_all()
		
# Main class
class SudokuGUI:
	
	def ev_leave(self, this):
		gtk.main_quit()
		
	def solve(self, this):
		self.sud = sudoku.Sudoku()
		i = 0
		for f in self.main_win.fields:
			try:
				v = int(f.get_text())
			except:
				v = None
			else:
				if v < 1 or v > 9:
					v = None
			self.sud.field[i] = v
			i += 1
		if not self.sud.check_field(self.sud.field):
			err('Dies ist kein regelkonformes Sudoku! :)')
			return False
		self.sud.found = False
		self.dg = SolveDialog("Berechnung", self.main_win, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT)
		self.dg.show()
		self.thr1 = thread.start_new_thread(self.sud.solve_quiet, (None,))
		self.thr2 = thread.start_new_thread(self.while_solving, (None,))
		
	def while_solving(self, nothing=None):
		while not self.sud.found:
			self.dg.pg.pulse()
			time.sleep(0.5)
		try:
			self.dg.hide()
			del self.dg
			
			i = 0
			for f in self.sud.field:
				self.main_win.fields[i].set_text(str(f))
				i += 1
			
		except Exception, e:
			print e
			
	def __init__(self):
		self.main_win = MainWindow()
		self.main_win.show_all()
		#self.main_win.set_icon_from_file("logo_klein.png")
		self.main_win.set_title("Sudoku GUI")
		self.main_win.connect('destroy', self.ev_leave)
		self.main_win.solvebutton.connect('activate', self.solve)
		self.main_win.solvebutton.connect('clicked', self.solve)

# parameters, initialization
if __name__ == '__main__':
	
	gui = SudokuGUI()
	try:
		gtk.gdk.threads_init()
		gtk.main()
	except KeyboardInterrupt:
		try:
			gui.exit()
		finally:
			sys.exit(0)
