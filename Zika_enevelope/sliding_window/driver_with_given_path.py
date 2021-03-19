from jiliplot import jiliplot
from randic2dplot import randic2dplot
from randic3dplot import randic3dplot
# from wangzhangplot import wangzhangplot
from songtangplot import songtangplot
from nandyplot import nandyplot
# from yauplot import yauplot
import os, sys, contextlib
import datetime

def add_header(method, log_path):
	header = "FileName,SeqLen," + ",".join(map(str, list(range(1, 1801))))
	with open(log_path + '/' + str(method.__name__) + '.csv','w') as log:
		with contextlib.redirect_stdout(log):
			print(header)

def log_output(method, file_path, log_path):
	with open(log_path + '/' + str(method.__name__) + '.csv','a') as log:
		with contextlib.redirect_stdout(log):
			print(file_path, end=",")
			method(file_path)

path = 'sequences'
# path = 'sequences (copy)'
count = 0
sequences = []
# methods = [randic2dplot , wangzhangplot, songtangplot]
# methods = [nandyplot, yauplot]
# methods = [randic3dplot]
# methods = [nandyplot]
methods = [nandyplot, randic3dplot, randic2dplot, songtangplot, jiliplot]
# methods = [randic2dplot, songtangplot, jiliplot]
for i in os.listdir(path):
	sequences.append(i)
for method in methods:
	start_time = datetime.datetime.now()
	add_header(method, 'logs')
	for sequence in sequences:
		print(sequence)
		log_output(method, path + '/' + sequence, 'logs')
	end_time = datetime.datetime.now()
	time_taken = end_time - start_time
	print('time taken (in microseconds) = ' + str(time_taken.microseconds))
	print('time taken (in seconds) = ' + str(time_taken.seconds))

