# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class fuzzy():
	Xmin=2100 #permintaan minimal
	Xmax=3500 #permintaan maxsimal
	Ymin=100  #persediaan minimal
	Ymax=250
	Zmin=1000
	Zmax=5000
	permNaik=0
	premTurun=0
	psdSedikit=0
	psdBanyak=0
	x=0 #permintaan
	y=0 #persediaan
	alpa=[0]*4
	z=[0]*4

def __init__(self,permintaan,persediaan):
	self.x=permintaan
	self.y=persediaan
	self.fpermTurun()
	self.fpermNaik()
	self.psdSedikit()
	self.psdBanyak()
	self.rule()
#self.defuzifikasi()

def fpermTurun(self):
	if self.x < self.Xmin:
		self.permTurun=1
	elif self.x>=self.Xmin and self.x<=self.Xmax:
		self.permTurun=(self.Xmax-self.x)/(self.Xmax-self.Xmin)
	else:
		self.permTurun=0

def fpermNaik(self):
	if self.x < self.Xmin:
		self.permNaik=0
	elif self.x>=self.Xmin and self.x<=self.Xmax:
		self.permNaik=(self.x-self.Xmin)/(self.Xmax-self.Xmin)
	else:
		self.permNaik=1

def fpsdSedikit(self):
	if self.y<self.Ymin:
		self.psdSedikit=1
	elif self.y>=self.Ymin and self.y<=self.Ymax:
		self.psdSedikit=(self.Ymax-self.y)/(self.Ymax-self.Ymin)
	else:
		self.psdSedikit=0

def fpsdBanyak(self):
	if self.y<self.Ymin:
		self.psdBanyak=0
	elif self.y>=self.Ymin and self.y<=self.Ymax:
		self.psdBanyak=(self.y-self.Ymin)/(self.Ymax-self.Ymin)
	else:
		self.psdBanyak=1

def rule(self):
	#rule 1: jika perm turun dan psd banyak maka produksi berkurang
	self.alpa[0]=min(self.permTurun,self.psdBanyak)
	self.z[0]=self.Zmax-self.alpa[0]*(self.Zmax-self.Zmin)

	#rule 2: Jika perm turun dan pesediaan sedikit maka produksi berkurang
	self.alpa[1]=min(self.permTurun,self.psdSedikit)
	self.z[1]=self.Zmax-self.alpa[1]*(self.Zmax-self.Zmin)

	#rule 3: Jika perm Naik, Persediaan Banyak maka Produksi bertambah
	self.alpa[2]=min(self.permNaik,self.psdBanyak)
	self.z[2]=self.alpa[2]*(self.Zmax-self.Zmin)+self.Zmin

	#rule 4: Jika perm Naik, Persediaan Sedikit,Maka produksi bertambah
	self.alpa[3]=min(self.permNaik,self.psdSedikit)
	self.z[3]=self.alpa[3]*(self.Zmax-self.Zmin)+self.Zmin

def defuzifikasi(self):
	output=(self.alpa[0]*self.z[0])+(
		self.alpa[1]*self.z[1])+(self.alpa[2]*self.z[2])+(self.alpa[3]*self.z[3])
	output1=self.alpa[0]+self.alpa[1]+self.alpa[2]+self.alpa[3]
	return output/output1

#main program
fz= fuzzy(3200,140)
print("permintaan turun =".fz.permTurun)
print("permintaan naik =".fz.permNaik)
print("persediaan sedikit =".fz.psdSedikit)
print("persediaan banyak =".fz.psdBanyak)
print("nilai seluruh perdiket =".fz.alpa)
print("nilai seluruh z =".fz.z)
print("produksi adalah =".fz.defuzifikasi())