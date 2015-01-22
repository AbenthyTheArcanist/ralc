#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2014 Tyler Dinsmoor <d@D-LM>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
testlist=('name','name2','name3','name4','name5','name6')

import Tkinter as tk
import ttk, mapGen, ImageTk, Image
import cPickle as pickle


class AppData(object):
	def __init__(self):
		self.newData()


	def newData(self):
		self.im,self.cityName = mapGen.main('tk')
		print "AppData.newData.Retrieved Data"

	def saveAll(self):
		def saveImg():
			self.im.save('save/img','PNG')

		def saveNames():
			savef = open('save/name', 'w')
			pickle.dump((self.cityName),savef)
			savef.close

		saveImg()
		print 'AppData.saveAll.Image Saved'
		saveNames()
		print 'AppData.saveAll.Names Saved'


	def loadAll(self):
		def loadImg():
			self.im = Image.open('save/img')


		def loadNames():
			savef = open('save/name', 'r')
			self.cityName = pickle.load(savef)
			savef.close

		loadImg()
		print 'AppData.loadAll.Loaded Image From Disk'
		loadNames()
		print 'AppData.loadAll.Loaded Names From Disk'
		ui.createWidgets()
		print 'AppData.loadAll.Refreshed Widgets'

	def loadPhoto(self):
		return ImageTk.PhotoImage(self.im)



class UI(tk.Frame,AppData):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.makeMenuBar()
		self.createWidgets()
		self.grid()
		self.getPhoto()
		print "UI.__init__.Done"

	def makeMenuBar(self):
		self.menubar = tk.Menu(self)
		self.menubar.add_command(label="Quit!", command=self.quit)
		self.menubar.add_cascade(label="File", menu=self.menubar)
		print 'UI.makeMenuBar.Done'

	def createWidgets(self):
		def makeQuitButton():
			self.quitButton = tk.Button(self, text="Quit",
			command=self.quit)
			self.quitButton.grid(sticky='n', column=2, row=0, padx=10)

		def makeSaveButton():
			self.showButton = tk.Button(self, text="Save",
			command=dat.saveAll)
			self.showButton.grid(sticky='n', column=2, row=0, padx=10,pady=40)

		def makeLoadButton():
			self.showButton = tk.Button(self, text="Load",
			command=self.loadState)
			self.showButton.grid(sticky='n', column=2, row=0, padx=10,pady=80)

		def makeNewButton():
			self.showButton = tk.Button(self, text="New",
			command=self.newState)
			self.showButton.grid(sticky='n', column=2, row=0, padx=10,pady=120)

		def makeTreeView():
			self.tree = ttk.Treeview(self, height=28,
				selectmode='browse')
			ysb = ttk.Scrollbar(self, orient='vertical',
				command=self.tree.yview)
			xsb = ttk.Scrollbar(self, orient='horizontal',
				command=self.tree.xview)
			ysb.grid(row=0, column=1, sticky='ns')
			xsb.grid(row=1, column=0, sticky='ew')
			self.tree.heading('#0', text='Name', anchor='w')
			self.tree.grid(row=0, column=0)

			self.tree.insert('', 'end', text=dat.cityName, open=True)


		makeTreeView()
		print 'UI.createWidgets.makeTreeView.Done'
		makeQuitButton()
		makeSaveButton()
		makeLoadButton()
		makeNewButton()
		print 'UI.createWidgets.make*Button.Done'



	def loadState(self):
		dat.loadAll()
		self.createWidgets()
		self.getPhoto()
		print 'UI.loadState.Done'

	def newState(self):
		dat.newData()
		self.createWidgets()
		self.getPhoto()
		print 'UI.newState.Done'

	def getPhoto(self):
		self.img = dat.loadPhoto()
		self.label = tk.Label(image = self.img)
		self.label.grid(sticky='E', column=3, row=0)
		print 'UI.getPhoto.Done'

	def addDataToTree(self, parent):
		for itm in testdata:
			self.tree.insert(parent, 'end', text=itm)


dat = AppData()
ui = UI()

ui.master.title('RALC v0.1')
ui.mainloop()

