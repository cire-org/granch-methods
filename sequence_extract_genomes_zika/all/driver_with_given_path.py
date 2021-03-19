from jiliplot import jiliplot
from randic2dplot import randic2dplot
from randic3dplot import randic3dplot
from wangzhangplot import wangzhangplot
from songtangplot import songtangplot
from nandyplot import nandyplot
from yauplot import yauplot
import os, sys, contextlib

def log_output(method, file_path, log_path):
	with open(log_path + '/' + str(method.__name__) + '.out','a') as log:
		with contextlib.redirect_stdout(log):
			print(file_path)
			method(file_path)

path = 'sequences'
count = 0
sequences = []
# methods = [randic2dplot , wangzhangplot, songtangplot]
methods = [nandyplot, yauplot]
for i in os.listdir(path):
	sequences.append(i)
for method in methods:
	for sequence in sequences:
		print(sequence)
		log_output(method, path + '/' + sequence, 'logs')
