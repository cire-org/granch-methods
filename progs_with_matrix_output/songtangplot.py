import csv
from math import *
from seqlencalc import getseqlen
from seqlencalc import baseset
import numpy as np
import datetime

base_to_y_val_map = {
	'A': 1,
	'T': 0,
	'G': -1,
	'C': 0
}

class Node:
	def __init__(self, base):
		self.base = base
		self.visited = False
		self.x = 0
		self.y = 0
		


def songtangplot(fname):
	seqlen = getseqlen(fname)
	print(seqlen)
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
	
	curr_x = 0
	curr_y = 0
	start_time = datetime.datetime.now()
	
	edmat = np.zeros((seqlen, seqlen))
	
	for i in range(0, seqlen):
		'''if(seqarr[i].visited == False):
			seqarr[i].x = i+1'''
		for j in range(i, seqlen):
			if(seqarr[j].visited == False):
				curr_x += 1
				seqarr[j].x = curr_x
				seqarr[j].y = base_to_y_val_map[seqarr[j].base]
				seqarr[j].visited = True
			edmat[i][j] = sqrt(pow((seqarr[i].x-seqarr[j].x), 2) + pow((seqarr[i].y-seqarr[j].y),2))
			edmat[j][i] = edmat[i][j]
	'''Computing the path-distance matrix'''
	pdmat = np.zeros((seqlen, seqlen))
	for i in range(0, seqlen):
		for j in range(i, seqlen):
			if(j==i):
				pdmat[i][j] = 0
			elif(i<j):
				pdmat[i][j] = pdmat[i][j-1] + edmat[j-1][j]
				pdmat[j][i]= pdmat[i][j]
	
	'''Computing the M/M matrix'''
	mbym_mat = np.zeros((seqlen, seqlen))
	for i in range(0, seqlen):
		for j in range(i, seqlen):
			if(i==j):
				mbym_mat[i][j] = 0;
			else:
				mbym_mat[i][j] = edmat[i][j] / abs(i-j)
				mbym_mat[j][i] = mbym_mat[i][j]
	np.savetxt("songtang-mm.csv", mbym_mat, delimiter=",")
				
	'''Computing the L/L matrix'''
	lbyl_mat = np.zeros((seqlen, seqlen))
	for i in range(0, seqlen):
		for j in range(i, seqlen):
			if(i==j):
				lbyl_mat[i][j] = 0;
			else:
				lbyl_mat[i][j] = edmat[i][j] / pdmat[i][j]
				lbyl_mat[j][i] = lbyl_mat[i][j]
	np.savetxt("songtang-ll.csv", lbyl_mat, delimiter=",")
				
	print(np.linalg.eigvals(mbym_mat).max())
	
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time
	
	print('time taken = ' + str(time_taken.microseconds))
	print('time taken = ' + str(time_taken.seconds))
