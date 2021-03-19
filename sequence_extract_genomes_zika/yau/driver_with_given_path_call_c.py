import ctypes 
NUM = 16      
# libfun loaded to the python file 
# using fun.myFunction(), 
# C function can be accessed 
# but type of argument is the problem. 
                         
yau = ctypes.CDLL(yau.so)   
# Now whenever argument  
# will be passed to the function                                                         
# ctypes will check it. 
            
yau.main.argtypes(ctypes.c_int, cty) 
  
# now we can call this  
# function using instant (fun) 
# returnValue is the value  
# return by function written in C  
# code 
returnVale = fun.myFunction(NUM) 
import os
#import errno
# path = '/home/dwaipayan/Dropbox/GRANCH Review/Progs_and_Results/sequence_extract_genomes_zika/sequences'
# path = 'virus_envelopes'
path = 'sequences'
#files = glob.glob(path)
count = 0
files = []
# for i in os.listdir(path):
#     if i.endswith('.txt'):files.append(i)
        #files.append(open(i))
	# 	fil
	# es.append(i)
	# files.append(i)
for i in os.listdir(path):
	files.append(i)
for name in files:
	#jiliplot(path + "/" + name)
	# if count == 4:
	# 	break
	print(name)
	# yauplot(path + "/" + name)
	count += 1
# print(nandyplot('test.txt'))
