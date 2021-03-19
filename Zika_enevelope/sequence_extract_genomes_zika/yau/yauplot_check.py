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

def yauplot(fname):
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
	
	curr_x = 0.0
	curr_y = 0.0
	count_a = 0
	count_c = 0
	count_g = 0
	count_t = 0
	sum_x = 0.0
	sum_y = 0.0
	total_count = 0
	start_time = datetime.datetime.now()

	# sqrt_three = pow(3, 0.5)
	# half = 1.0 / 2.0
	# print(sqrt_three * half)

	for i in range(0, seqlen):
		curr_base = seqarr[i].base
		if(curr_base == 'G'):
			total_count += 1
			count_g +=  1
			curr_x = curr_x + 0.8660254
			sum_x = sum_x + curr_x
			curr_y = curr_y - 0.5
			sum_y = sum_y + curr_y
		elif(curr_base == 'C'):
			total_count += 1
			count_c +=  1
			curr_x = curr_x + 0.8660254
			sum_x = sum_x + curr_x
			curr_y = curr_y + 0.5
			sum_y = sum_y + curr_y
		elif(curr_base == 'A'):
			total_count += 1
			count_a +=  1
			curr_x = curr_x + 0.5
			sum_x = sum_x + curr_x
			curr_y = curr_y - 0.8660254
			sum_y = sum_y + curr_y
		elif(curr_base == 'T'):
			total_count += 1
			count_t +=  1
			curr_x = curr_x + 0.5
			sum_x = sum_x + curr_x
			curr_y = curr_y + 0.8660254
			sum_y = sum_y + curr_y
		seqarr[i].x = curr_x
		seqarr[i].y = curr_y
			
	mew_x = float(sum_x) / float(total_count)
	mew_y = float(sum_y) / float(total_count)
	
	sqr_gr_value = pow(mew_x, 2.0) + pow(mew_y, 2.0)
	gr_value = pow(sqr_gr_value, 0.5)
	# gr_value = pow((pow(mew_x, 2.0) + pow(mew_y, 2.0)), 0.5)
	
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time

	print('count of a:' + str(count_a))
	print('count of c:' + str(count_c))
	print('count of g:' + str(count_g))
	print('count of t:' + str(count_t))
	
	print('mew_x = ' + str(mew_x))
	print('mew_y = ' + str(mew_y))
	print('sqr_gr_value = ' + str(sqr_gr_value))

	print('gr_value = ' + str(gr_value))
	print('time taken = ' + str(time_taken.microseconds))
	print('time taken = ' + str(time_taken.seconds))
