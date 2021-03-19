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
		self.z = 0
		
	def reset(self):
		self.visited = False
		self.x = 0
		self.y = 0
		self.z = 0
		


def songtangplot(fname):
	window_list = list()
	seqlen = getseqlen(fname)
	print(seqlen, end=",")
	seqarr = []
	f = open(fname, 'r')
	
	c = f.read(1)
	while c!="":
		c = c.upper()
		if(c in baseset):
			seqarr.append(Node(c))
		c = f.read(1)
	f.close()

	for i in range (0, seqlen - 36, 3):
		for j in range (i, i+36):
			seqarr[j].reset()
		# print("slide_count: " + str(i))
		sliding_window(i, 36, seqarr, window_list)
	
	# for window in window_list:
	# 	print(str(window), end=",")
	print(','.join(map(str, window_list)))
	# print(len(window_list))

def sliding_window(seqstart, seqlen, seqarr, window_list):
	curr_x = 0
	curr_y = 0
	start_time = datetime.datetime.now()
	
	edmat = np.zeros((seqlen, seqlen))
	
	for i in range(seqstart, seqstart+seqlen):
		'''if(seqarr[i].visited == False):
			seqarr[i].x = i+1'''
		for j in range(i, seqstart+seqlen):
			if(seqarr[j].visited == False):
				curr_x += 1
				seqarr[j].x = curr_x
				seqarr[j].y = base_to_y_val_map[seqarr[j].base]
				seqarr[j].visited = True
			edmat[i - seqstart][j - seqstart] = sqrt(pow((seqarr[i].x-seqarr[j].x), 2) + pow((seqarr[i].y-seqarr[j].y),2))
			edmat[j - seqstart][i - seqstart] = edmat[i - seqstart][j - seqstart]
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
				
	'''Computing the L/L matrix'''
	# lbyl_mat = np.zeros((seqlen, seqlen))
	# for i in range(0, seqlen):
	# 	for j in range(i, seqlen):
	# 		if(i==j):
	# 			lbyl_mat[i][j] = 0;
	# 		else:
	# 			lbyl_mat[i][j] = edmat[i][j] / pdmat[i][j]
	# 			lbyl_mat[j][i] = lbyl_mat[i][j]
				
	# print(np.linalg.eigvals(mbym_mat).max())
	window_list.append(round(np.real(np.linalg.eigvals(mbym_mat).max()), 4))
	
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time
	
	# print('time taken = ' + str(time_taken.microseconds))
	# print('time taken = ' + str(time_taken.seconds))
