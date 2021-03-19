import csv
from math import *
from seqlencalc import getseqlen
from seqlencalc import baseset
import numpy as np
import datetime
from multiprocessing import Pool
import pandas as pd
import threading
import gc

base_to_y_val_map = {
	'A': 4,
	'T': 3,
	'G': 2,
	'C': 1
}

class Node:
	def __init__(self, base):
		self.base = base
		self.visited = False
		self.x = 0
		self.y = 0
		self.z = 0

curr_x = 0
curr_y = 0
curr_z = 0		

def visit_node(node):
	#global curr_x, curr_y, curr_z
	global curr_x
	global curr_y
	global curr_z
	if(node.visited == False):
		curr_base = node.base
		if(curr_base == 'G'):
			curr_x = curr_x - 1
			curr_y = curr_y + 1
			curr_z = curr_z - 1
		elif(curr_base == 'C'):
			curr_x = curr_x - 1
			curr_y = curr_y - 1
			curr_z = curr_z + 1
		elif(curr_base == 'A'):
			curr_x = curr_x + 1
			curr_y = curr_y - 1
			curr_z = curr_z - 1
		elif(curr_base == 'T'):
			curr_x = curr_x + 1
			curr_y = curr_y + 1
			curr_z = curr_z + 1
		node.x = curr_x
		node.y = curr_y
		node.z = curr_z
		node.visited = True
		
def dist_calc(node1, node2):
	return sqrt(pow((node1.x - node2.x), 2) + pow((node1.y - node2.y),2) + pow((node1.z - node2.z),2)) / pow(3, 0.5)
	
def memoize_ed(seqarr, edmat, index1, index2):
	visit_node(seqarr[index1])
	visit_node(seqarr[index2])
	edmat[index1][index2] = dist_calc(seqarr[index1], seqarr[index2])
	edmat[index1][index1] = edmat[index1][index2]		

def randic3dplot(fname):
	seqlen = getseqlen(fname)
	print("Current thread: " + str(threading.get_ident()) + "; sequence length: " + str(seqlen))
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
	
	# edmat = np.zeros((seqlen, seqlen))
	edmat = np.zeros((seqlen, seqlen), dtype=float)
	# edmat = pd.DataFrame(np.zeros((seqlen, seqlen)))
	
	
	
	for i in range(0, seqlen):
		visit_node(seqarr[i])
		for j in range(i, seqlen):
			visit_node(seqarr[j])
			edmat[i][j] = sqrt(pow((seqarr[i].x - seqarr[j].x), 2) + pow((seqarr[i].y - seqarr[j].y),2) + pow((seqarr[i].z - seqarr[j].z),2)) / pow(3, 0.5)
			edmat[j][i] = edmat[i][j]
	
	# pool = Pool(processes=2)
			
	# for i in range(0, seqlen):
	# 	for j in range(i, seqlen):
	# 		#pool.map(memoize_ed(seqarr, edmat, i, j))
	# 		pool.map(memoize_ed, seqarr)
	
	# '''Computing the path-distance matrix'''
	# pdmat = np.zeros((seqlen, seqlen))
	# for i in range(0, seqlen):
	# 	for j in range(i, seqlen):
	# 		if(j==i):
	# 			pdmat[i][j] = 0
	# 		elif(i<j):
	# 			pdmat[i][j] = pdmat[i][j-1] + edmat[j-1][j]
	# 			pdmat[j][i]= pdmat[i][j]
	
	# '''Computing the M/M matrix'''
	# mbym_mat = np.zeros((seqlen, seqlen))
	# print(current.name, current._identity + " Size of edmat:" + str(edmat.nbytes))
	# print("Current thread: " + str(threading.current_thread().getName) + "; Size of edmat(MB):" + str(edmat.nbytes/(1024*1024)))
	# print("Current thread: " + str(threading.Thread.getName) + "; Size of edmat(MB):" + str(edmat.nbytes/(1024*1024)))
	print("Current thread: " + str(threading.get_ident()) + "; Size of edmat(MB):" + str(edmat.nbytes/(1024*1024)))

	# mbym_mat = pd.DataFrame(np.zeros((seqlen, seqlen)))
	# mbym_mat = np.zeros((seqlen, seqlen))
	mbym_mat = np.zeros((seqlen, seqlen), dtype=float)
	for i in range(0, seqlen):
		for j in range(i, seqlen):
			if(i==j):
				mbym_mat[i][j] = 0
			else:
				mbym_mat[i][j] = edmat[i][j] / abs(i-j)
				mbym_mat[j][i] = mbym_mat[i][j]
	
	# print(current.name, current._identity + " Size of mbym_mat:" + str(mbym_mat.nbytes))
	print("Current thread: " + str(threading.get_ident()) + "; Size of mbym_mat(MB):" + str(mbym_mat.nbytes/(1024*1024)))
				
	# '''Computing the L/L matrix'''
	# lbyl_mat = np.zeros((seqlen, seqlen))
	# for i in range(0, seqlen):
	# 	for j in range(i, seqlen):
	# 		if(i==j):
	# 			lbyl_mat[i][j] = 0;
	# 		else:
	# 			lbyl_mat[i][j] = edmat[i][j] / pdmat[i][j]
	# 			lbyl_mat[j][i] = lbyl_mat[i][j]
				
	# print(current.name, current._identity + " Max eigvalue: " + np.linalg.eigvals(mbym_mat).max())
	# print("Max eigvalue: " + np.linalg.eigvals(mbym_mat).max())
	before_eigvals = datetime.datetime.now()
	# print("Max eigvalue(eig): " + str(np.linalg.eigvals(mbym_mat).max()) + ": time_taken: " + str(datetime.datetime.now() - before_eigvals))
	before_eigvalsh = datetime.datetime.now()
	print("Current thread: " + str(threading.get_ident()) + "; Max eigvalue(eigh): " + str(np.linalg.eigvalsh(mbym_mat).max()) + ": time_taken: " + str(datetime.datetime.now() - before_eigvalsh))
	
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time
	
	# print('time taken = ' + str(time_taken.microseconds))
	# print("Current thread: " + str(threading.get_ident()) + "; time taken = " + str(time_taken.seconds))
	print("Current thread: " + str(threading.get_ident()) + "; time taken = " + str(time_taken))
	gc.collect()
