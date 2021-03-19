baseset = set(['A', 'C', 'G', 'T'])

def getseqlen(fname):
	f = open(fname, 'r')
	seqlen=0
	'''print(f.name)'''
	c = f.read(1)
	while c!="":
		if(c.upper() in baseset):
			#print("string is: ", c)
			seqlen+=1
		c = f.read(1)
	#print(seqlen)
	f.close()
	return seqlen