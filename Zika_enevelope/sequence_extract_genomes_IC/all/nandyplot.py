import csv
from math import *
from seqlencalc import getseqlen
from seqlencalc import baseset
import numpy as np
import datetime

class Node:
	def __init__(self, base):
		self.base = base
		self.visited = False
		self.x = 0
		self.y = 0
		self.z = 0

def nandyplot(fname):
	seqlen = getseqlen(fname)
	print(seqlen)
	seqarr = []
	f = open(fname, 'r')
	
	c = f.read(1)
	while c!="":
		c = c.upper()
		if(c in baseset):
			seqarr.append(Node(c))
		c = f.read(1)
	f.close()
	
	curr_x = 0
	curr_y = 0
	count_a = 0
	count_c = 0
	count_g = 0
	count_t = 0
	sum_x = 0
	sum_y = 0
	total_count = 0
	start_time = datetime.datetime.now()
			
	for i in range(0, seqlen):
		curr_base = seqarr[i].base
		if(curr_base == 'G'):
			total_count += 1
			count_g +=  1
			curr_x = curr_x + 1
			sum_x = sum_x + curr_x
			sum_y = sum_y + curr_y
		elif(curr_base == 'C'):
			total_count += 1
			count_c +=  1
			curr_y = curr_y + 1
			sum_x = sum_x + curr_x
			sum_y = sum_y + curr_y
		elif(curr_base == 'A'):
			total_count += 1
			count_a +=  1
			curr_x = curr_x - 1
			sum_x = sum_x + curr_x
			sum_y = sum_y + curr_y
		elif(curr_base == 'T'):
			total_count += 1
			count_t +=  1
			curr_y = curr_y - 1
			sum_x = sum_x + curr_x
			sum_y = sum_y + curr_y
		seqarr[i].x = curr_x
		seqarr[i].y = curr_y
			
	mew_x = sum_x / total_count;
	mew_y = sum_y / total_count;
	
	gr_value = pow((pow(mew_x, 2.0) + pow(mew_y, 2.0)), 0.5)
	
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time
	
	print('gr_value = ' + str(gr_value))
	print('time taken = ' + str(time_taken.microseconds))
	print('time taken = ' + str(time_taken.seconds))
