#from multi_key_dict import multi_key_dict
import csv
from math import *
from seqlencalc import getseqlen
from seqlencalc import baseset
import numpy as np
import datetime

rset = {'A', 'G'}
yset = {'C', 'T'}

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

def jiliplot(fname):
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
	rcount = 0; ycount = 0;
	start_time = datetime.datetime.now()
	'''Computing the Euclidean-distance-distance matrix'''
	edmat = np.zeros((seqlen, seqlen))
	for i in range(seqstart, seqstart+seqlen):
		#seqarr[i].x = 0; seqarr[i].y = 0;
		if(seqarr[i].base in baseset):
			if(seqarr[i].visited == False):
				if(seqarr[i].base in rset):
					seqarr[i].x = 1
					rcount += 1
					seqarr[i].y = rcount
				else:
					seqarr[i].x = 0
					ycount += 1
					seqarr[i].y = ycount
				seqarr[i].visited = True
		for j in range(i, seqstart+seqlen):
			#seqarr[j].x = 0; seqarr[j].y = 0;
			if(j!=i):
				if(seqarr[j].base in baseset):
					if(seqarr[j].visited == False):
						if(seqarr[j].base in rset):
							seqarr[j].x = 1
							rcount += 1
							seqarr[j].y = rcount
						else:
							seqarr[j].x = 0
							ycount += 1
							seqarr[j].y = ycount
						seqarr[j].visited = True
			else:
				seqarr[j].x = seqarr[i].x
				seqarr[j].y = seqarr[i].y;
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
	# mbym_mat = np.zeros((seqlen, seqlen))
	# for i in range(0, seqlen):
	# 	for j in range(i, seqlen):
	# 		if(i==j):
	# 			mbym_mat[i][j] = 0;
	# 		else:
	# 			mbym_mat[i][j] = edmat[i][j] / abs(i-j)
	# 			mbym_mat[j][i] = mbym_mat[i][j]
				
	'''Computing the L/L matrix'''
	lbyl_mat = np.zeros((seqlen, seqlen))
	for i in range(0, seqlen):
		for j in range(i, seqlen):
			if(i==j):
				lbyl_mat[i][j] = 0;
			else:
				lbyl_mat[i][j] = edmat[i][j] / pdmat[i][j]
				lbyl_mat[j][i] = lbyl_mat[i][j]
				
	#print(pdmat)
	
	#print('time taken = ' + str(time_taken.microseconds))
	#print('time taken = ' + str(time_taken.seconds))
	
	'''print(np.linalg.eigvals(edmat).max())
	print(np.linalg.eigvals(pdmat).max())
	print(np.linalg.eigvals(mbym_mat).max())
	print(np.linalg.eigvals(lbyl_mat).max())'''
	
	''' open('jili_ed.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerows(edmat)
	with open('jili_mm.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerows(mbym_mat)
	with open('jili_ll.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerows(lbyl_mat)
	with open('jili_pd.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerows(pdmat)'''
	
	'''print('**************************************************')
	print(edmat)
	print('**************************************************')
	print('**************************************************')
	print(mbym_mat)
	print('**************************************************')
	print('**************************************************')
	print(lbyl_mat)
	print('**************************************************')'''
	
	
	# print(np.linalg.eigvals(lbyl_mat).max())
	# window_list.append(round(np.linalg.eigvals(lbyl_mat).max(), 4))
	window_list.append(round(np.real(np.linalg.eigvals(lbyl_mat).max()), 4))
	
	# end_time = datetime.datetime.now()
	# time_taken = end_time - start_time
	
	# print('time taken = ' + str(time_taken.microseconds))
	# print('time taken = ' + str(time_taken.seconds))
			