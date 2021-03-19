from math import *
from seqlencalc import getseqlen
import datetime

def taonanwangplot(fname):
	'''f = open(fname, 'r')
	seqlen=0
	c = f.read(1)
	while c!="":
		if(c.upper() in baseset):
			#print("string is: ", c)
			seqlen+=1
		c = f.read(1)
	#print(seqlen)
	f.close()'''
	seqlen = getseqlen(fname)
	
	start_time = datetime.datetime.now()
	
	print("wsrocalc: ", wsrocalc(fname, seqlen))
	print("mkrocalc: ", mkrocalc(fname, seqlen))
	print("ryrocalc: ", ryrocalc(fname, seqlen))
	
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time
	
	print('time taken = ' + str(time_taken.microseconds))
	print('time taken = ' + str(time_taken.seconds))
	
def wsrocalc(fname, seqlen):
	xset = {'C', 'G'}
	yset = {'A', 'T'}
	#ro = get_3d_vector(fname, seqlen, xset, yset)[2]
	#return ro
	return get_3d_vector(fname, seqlen, xset, yset)
	
def mkrocalc(fname, seqlen):
	xset = {'G', 'T'}
	yset = {'A', 'C'}
	#ro = get_3d_vector(fname, seqlen, xset, yset)[2]
	#return ro
	return get_3d_vector(fname, seqlen, xset, yset)
	
def ryrocalc(fname, seqlen):
	xset = {'C', 'T'}
	yset = {'A', 'G'}
	#ro = get_3d_vector(fname, seqlen, xset, yset)[2]
	#return ro
	return get_3d_vector(fname, seqlen, xset, yset)
	
def get_3d_vector(fname, seqlen, xset, yset):
	f = open(fname, 'r')
	currx = 0
	curry = 0
	count = 0
	sumdiff = 0
	sumx = 0
	sumy = 0
	list = [[0]*3 for i in range(seqlen)]
	
	#print(seqlen)
	f = open(fname, 'r')
	c = f.read(1).upper()
	while c!="":
		if(c in xset):
			currx += 1
			list[count][0] = c
			list[count][1] = currx
			list[count][2] = curry
			#print(list[count][0], list[count][1], list[count][2])
			sumdiff += fabs(currx - curry)
			sumx += currx
			count += 1
			#print(sumx)
		elif(c in yset):
			curry += 1
			list[count][0] = c
			list[count][1] = currx
			list[count][2] = curry
			#print(list[count][0], list[count][1], list[count][2])
			sumdiff += fabs(currx - curry)
			sumy += curry
			count += 1
		c = f.read(1).upper()
	f.close()
	#print(sumx, sumy)
	mewx = sumx / seqlen
	mewy = sumy / seqlen
	#theta = 0
	theta = mewy / mewx
	gr = sqrt(pow(mewx, 2) + pow(mewy, 2))
	#sumdiff = fabs(sumx - sumy)
	ro = (1 / (sqrt(2) * seqlen)) * (sumdiff)
	return [theta, gr, ro]
