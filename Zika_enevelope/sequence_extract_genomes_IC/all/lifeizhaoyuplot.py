from multi_key_dict import multi_key_dict
from math import *
from seqlencalc import getseqlen
from seqlencalc import baseset
from jiliplot import Node
import datetime

class ThreeDVector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		
	def __repr__(self):
		#print('[' + self.x + ', ' + self.y + ', ' + self.z + ']')
		#return('[' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ']')
		#return('[' + str(round(self.x, 4)) + ', ' + str(round(self.y, 4)) + ', ' + str(round(self.z, 4)) + ']')
		return('[' + str(round(self.x, 3)) + ', ' + str(round(self.y, 3)) + ', ' + str(round(self.z, 3)) + ']')
		
	def modulus(self):
		return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
		
	def unit(self):
		mod = self.modulus()
		if(mod > 0):
			unit_x = self.x / mod
			unit_y = self.y / mod
			unit_z = self.z / mod
			return ThreeDVector(unit_x, unit_y, unit_z)
		else:
			return ThreeDVector(0, 0, 0)
			
	def add(self, point_from):
		if(isinstance(point_from, ThreeDVector)):
			return ThreeDVector((self.x + point_from.x), (self.y + point_from.y), (self.z + point_from.z))
		else:
			return None
		
	def unit_couplet_value(self, to):
		if(isinstance(to, ThreeDVector)):
			midpoint = ThreeDVector(((self.x + to.x)/2), ((self.y + to.y)/2), ((self.z + to.z)/2))
			return midpoint.unit()
		else:
			#print("Unable to compute the distance")
			return None
			#return ThreeDVector(0, 0, 0)
		'''if(isinstance(to, ThreeDVector)):
			midpoint = ThreeDVector(((self.x + 0)/2), ((self.y + 0)/2), ((self.z + 0)/2))
			return midpoint.unit()'''

class BasePosition:
	def __init__(self):
		self.O = ThreeDVector(0, 0, 0)		
		self.A = ThreeDVector(1, 1, 1)
		self.C = ThreeDVector(-1, -1, 1)
		self.G = ThreeDVector(1, -1, -1)
		self.T = ThreeDVector(-1, 1, -1)

basepos = BasePosition()		

'''doubledict = multi_key_dict()
doubledict['AA'] = A.unit_couplet_value(A)
doubledict['AC', 'CA'] = A.unit_couplet_value(C)
doubledict['AG', 'GA'] = A.unit_couplet_value(G)
doubledict['AT', 'TA'] = A.unit_couplet_value(T)
doubledict['CC'] = C.unit_couplet_value(C)
doubledict['CG', 'GC'] = C.unit_couplet_value(G)
doubledict['CT', 'TC'] = C.unit_couplet_value(T)
doubledict['GG'] = G.unit_couplet_value(G)
doubledict['GT', 'TG'] = G.unit_couplet_value(T)
doubledict['TT'] = T.unit_couplet_value(T)'''

doubledict = multi_key_dict()
doubledict['AA'] = basepos.A.unit_couplet_value(basepos.A)
doubledict['AC', 'CA'] = basepos.A.unit_couplet_value(basepos.C)
doubledict['AG', 'GA'] = basepos.A.unit_couplet_value(basepos.G)
doubledict['AT', 'TA'] = basepos.A.unit_couplet_value(basepos.T)
doubledict['CC'] = basepos.C.unit_couplet_value(basepos.C)
doubledict['CG', 'GC'] = basepos.C.unit_couplet_value(basepos.G)
doubledict['CT', 'TC'] = basepos.C.unit_couplet_value(basepos.T)
doubledict['GG'] = basepos.G.unit_couplet_value(basepos.G)
doubledict['GT', 'TG'] = basepos.G.unit_couplet_value(basepos.T)
doubledict['TT'] = basepos.T.unit_couplet_value(basepos.T)


def lifeizhaoyuplot(fname):
	seqlen = getseqlen(fname)
	#print(seqlen)
	seqarr = []
	f = open(fname, 'r')
	c = f.read(1)
	while c!="":
		c = c.upper()
		if(c in baseset):
			#x = Node(c)
			seqarr.append(Node(c))
		c = f.read(1)
	f.close()
	
	start_time = datetime.datetime.now()
	
	point = basepos.O
	count = 0
	while(count < seqlen-1):
		word = seqarr[count].base + seqarr[count+1].base
		#print(count)
		#print(word)
		#(doubledict[word])
		#point = point.unit_couplet_value(doubledict[word])
		#point = doubledict[word].unit_couplet_value(point)
		point = doubledict[word].add(point)
		#print(point)
		count += 1
	#print(count)
	print(point)
	
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time
	
	print('time taken = ' + str(time_taken.microseconds))
	print('time taken = ' + str(time_taken.seconds))
