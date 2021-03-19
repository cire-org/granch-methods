from multi_key_dict import multi_key_dict
from math import *
from seqlencalc import getseqlen
import datetime

tripletdict = multi_key_dict()
tripletdict['TAA', 'TAG', 'TGA'] = 0
tripletdict['ATG'] = 1
tripletdict['GCT', 'GCC', 'GCA', 'GCG'] = 2
tripletdict['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'] = 3
tripletdict['AAT', 'AAC'] = 4
tripletdict['GAT', 'GAC'] = 5
tripletdict['TGT', 'TGC'] = 6
tripletdict['CAA', 'CAG'] = 7
tripletdict['GAA', 'GAG'] = 8
tripletdict['GGT', 'GGC', 'GGA', 'GGG'] = 9
tripletdict['ATT', 'ATC', 'ATA'] = 10
tripletdict['CAT', 'CAC'] = 11
tripletdict['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'] = 12
tripletdict['AAA', 'AAG'] = 13
tripletdict['TTT', 'TTC'] = 14
tripletdict['CCT', 'CCC', 'CCA', 'CCG'] = 15
tripletdict['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'] = 16
tripletdict['ACT', 'ACC', 'ACA', 'ACG'] = 17
tripletdict['TGG'] = 18
tripletdict['TAT', 'TAC'] = 19
tripletdict['GTT', 'GTC', 'GTA', 'GTG'] = 20

#print(tripletdict['TAG'])

def zhaoqiyangplot(fname):
	codonvector = [0]*21
	#seqlen = getseqlen(fname)
	
	start_time = datetime.datetime.now()
	
	f = open(fname, 'r')
	triplet = f.read(3).upper()
	while len(triplet) == 3:
		#print(triplet)
		try:
			index = tripletdict[triplet]
			codonvector[index] += index
		except:
			print("Not a valid sequence")
		f.seek(f.tell() - 2)
		#print(f.tell())
		triplet = f.read(3).upper()
	f.close()
	
	print(codonvector)
	
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time
	
	print('time taken = ' + str(time_taken.microseconds))
	print('time taken = ' + str(time_taken.seconds))
	
	return codonvector
	
def zhaoqiyangdiffcalc(fname1, fname2):
	cv1 = zhaoqiyangplot(fname1)
	cv2 = zhaoqiyangplot(fname2)
	print(cv1, cv2)
	multresult = 0
	squaredsumcv1 = 0
	squaredsumcv2 = 0
	for i in range(0, 21):
		multresult += cv1[i]*cv2[i]
		squaredsumcv1 += pow(cv1[i], 2)
		squaredsumcv2 += pow(cv2[i], 2)
	diff = ((1-(multresult/(sqrt(squaredsumcv1*squaredsumcv2))))/2)
	print(diff)
	return diff