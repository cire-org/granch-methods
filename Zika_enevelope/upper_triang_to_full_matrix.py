import csv
import re
import numpy as np

def upper_to_full_mat(fname):
	with open(fname, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|', skipinitialspace=True)
		l = list()
		r = re.compile(r'\s')
		for row in reader:
			'''if(count <= 10):
				print(', '.join(row))
			else:
				break
			count += 1'''
			row_str = ''
			row_str.join(row)
			if(row_str == ' '):
				row_str = r.sub('0', row_str)
			#l.append(np.fromstring(row_str, np.float))
			print(np.fromstring(row_str, np.float))
		#print(l)

upper_to_full_mat('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/wang_zhang_ex.txt')