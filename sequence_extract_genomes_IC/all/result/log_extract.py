import csv
import datetime

# class Result:
# 	def __init__(self):
# 		self.seq_name = seq_name
# 		self.total_count

def result_extract(log_name):
	with open(log_name, 'rb') as log:
		for i in (0, 3):
			
		
	seq_name = get_seq_name()
	path = 
	seq_name = get_seq_name()

def get_seq_name(path):
	return path.split('/')

def log_extract(path):
	files = []
	for i in os.listdir(path):
    	if i.endswith('.out'):files.append(i)
	for file in files:
		result_extract(file)