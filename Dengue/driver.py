'''from taonanwangplot import taonanwangplot
from zhaoqiyangplot import zhaoqiyangplot
from zhaoqiyangplot import zhaoqiyangdiffcalc
from jiliplot import jiliplot
from lifeizhaoyuplot import lifeizhaoyuplot
from randic2dplot import randic2dplot'''
from randic3dplot_v2 import randic3dplot
# from randic3dplot import randic3dplot
from nandyplot import nandyplot
import threading
import datetime
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool


#from songtangplot import songtangplot

#from wangzhangplot import wangzhangplot

#from jiliplot import jiliplot

#import oct2py

#taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/10_base.txt')
#taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chimp_taonanwangplot.txt')

#zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/10_base.txt')
#zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chimp_taonanwangplot.txt')

#zhaoqiyangdiffcalc('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chimp_taonanwangplot.txt', 'C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/human_taonanwangplot.txt')
#zhaoqiyangdiffcalc('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/zhangqi_goat.txt', 'C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/zhangqi_human.txt')
#zhaoqiyangdiffcalc('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/zhangqi_goat_2.txt', 'C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/zhangqi_human.txt')


#jiliplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/10_base.txt')
#jiliplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/jili_10_base.txt')
#jiliplot('C:/Users/Dwaipayan Sen/Dropbox/JBNSTS_project/DNA_Methods_Comparison/Methods/Randic3D-plot/Human globin genes-CDS(new)/human-alpha1-globin/human-alpha1-globin.txt')

#lifeizhaoyuplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/10_base.txt')
#lifeizhaoyuplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chunli_test.txt')

'''taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/AB745326.1_seq.txt')
zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/AB745326.1_seq.txt')
jiliplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/AB745326.1_seq.txt')
lifeizhaoyuplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/AB745326.1_seq.txt')'''


'''taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-alpha1-globin/human-alpha1-globin.txt')
taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-beta-globin-HBB-mRNA/Human-beta-globin-HBB-mRNA.txt')
taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-delta-globin-HBD/Human-delta-globin-HBD.txt')
taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-hbg1-mrna/Human-HBG1-mRNA.txt')'''

'''jiliplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-alpha1-globin/human-alpha1-globin.txt')
jiliplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-beta-globin-HBB-mRNA/Human-beta-globin-HBB-mRNA.txt')
jiliplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-delta-globin-HBD/Human-delta-globin-HBD.txt')
jiliplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-hbg1-mrna/Human-HBG1-mRNA.txt')'''


'''zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-alpha1-globin/human-alpha1-globin.txt')
zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-beta-globin-HBB-mRNA/Human-beta-globin-HBB-mRNA.txt')
zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-delta-globin-HBD/Human-delta-globin-HBD.txt')
zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-hbg1-mrna/Human-HBG1-mRNA.txt')'''

'''lifeizhaoyuplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-alpha1-globin/human-alpha1-globin.txt')
lifeizhaoyuplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-beta-globin-HBB-mRNA/Human-beta-globin-HBB-mRNA.txt')
lifeizhaoyuplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-delta-globin-HBD/Human-delta-globin-HBD.txt')
lifeizhaoyuplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-hbg1-mrna/Human-HBG1-mRNA.txt')'''

'''taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/JX669476_envelope.txt')
taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/KC601756_envelope.txt')
taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/JN620362_envelope.txt')
taonanwangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/KX197192_envelope.txt')'''

'''jiliplot('data/virus_envelopes/JX669476_envelope.txt')
jiliplot('data/virus_envelopes/KC601756_envelope.txt')
jiliplot('data/virus_envelopes/JN620362_envelope.txt')
jiliplot('data/virus_envelopes/KX197192_envelope.txt')'''

'''zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/JX669476_envelope.txt')
zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/KC601756_envelope.txt')
zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/JN620362_envelope.txt')
zhaoqiyangplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/KX197192_envelope.txt')'''

'''randic2dplot('data/chapter_data/human-alpha1-globin/human-alpha1-globin.txt')
randic2dplot('data/chapter_data/Human-beta-globin-HBB-mRNA/Human-beta-globin-HBB-mRNA.txt')
randic2dplot('data/chapter_data/Human-delta-globin-HBD/Human-delta-globin-HBD.txt')
randic2dplot('data/chapter_data/human-hbg1-mrna/Human-HBG1-mRNA.txt')'''

'''randic2dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/JX669476_envelope.txt')
randic2dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/KC601756_envelope.txt')
randic2dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/JN620362_envelope.txt')
randic2dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/KX197192_envelope.txt')'''

'''randic3dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-alpha1-globin/human-alpha1-globin.txt')
randic3dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-beta-globin-HBB-mRNA/Human-beta-globin-HBB-mRNA.txt')
randic3dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/Human-delta-globin-HBD/Human-delta-globin-HBD.txt')
randic3dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/chapter_data/human-hbg1-mrna/Human-HBG1-mRNA.txt')'''

'''randic3dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/JX669476_envelope.txt')
randic3dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/KC601756_envelope.txt')
randic3dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/JN620362_envelope.txt')
randic3dplot('C:/Users/Dwaipayan Sen/Dropbox/GRANCH Review/Progs_and_Results/data/virus_envelopes/KX197192_envelope.txt')'''

'''songtangplot('data/chapter_data/human-alpha1-globin/human-alpha1-globin.txt')
songtangplot('data/chapter_data/Human-beta-globin-HBB-mRNA/Human-beta-globin-HBB-mRNA.txt')
songtangplot('data/chapter_data/Human-delta-globin-HBD/Human-delta-globin-HBD.txt')
songtangplot('data/chapter_data/human-hbg1-mrna/Human-HBG1-mRNA.txt')'''

'''songtangplot('data/virus_envelopes/JX669476_envelope.txt')
songtangplot('data/virus_envelopes/KC601756_envelope.txt')
songtangplot('data/virus_envelopes/JN620362_envelope.txt')
songtangplot('data/virus_envelopes/KX197192_envelope.txt')'''

#wangzhangplot('C:/Users/Dwaipayan Sen/Dropbox/JBNSTS_project/DNA_Methods_Comparison/Methods/WangZhang-plot/first-exon-beta-globin-WangZhang/bovine/bovine.txt')

'''wangzhangplot('data/chapter_data/human-alpha1-globin/human-alpha1-globin.txt')
wangzhangplot('data/chapter_data/Human-beta-globin-HBB-mRNA/Human-beta-globin-HBB-mRNA.txt')
wangzhangplot('data/chapter_data/Human-delta-globin-HBD/Human-delta-globin-HBD.txt')
wangzhangplot('data/chapter_data/human-hbg1-mrna/Human-HBG1-mRNA.txt')'''

'''wangzhangplot('data/virus_envelopes/JX669476_envelope.txt')
wangzhangplot('data/virus_envelopes/KC601756_envelope.txt')
wangzhangplot('data/virus_envelopes/JN620362_envelope.txt')
wangzhangplot('data/virus_envelopes/KX197192_envelope.txt')'''

import os
#import errno
path = '/home/dwaipayan/Downloads/Required/Output'

start_time = datetime.datetime.now()

#files = glob.glob(path)
files = []
'''for i in os.listdir(path):
	if i.endswith('.txt'):
		files.append(i)'''
'''for name in files:
#jiliplot(path + "/" + name)
#nandyplot(path + "/" + name)
	print(name)
	randic3dplot(path + "/" + name)
	print('--------------------------------------------------------------------\n\n')
	#randic3dplot('AB122020_sample_5562')
	#randic3dplot('AB122020_sample_2780')
	#randic3dplot(name)'''
	
# randic3dplot('AB122020_sample_2780')
# randic3dplot('AB122020_sample_5562')
# randic3dplot('AB122020.txt')

# t1 = threading.Thread(target=randic3dplot, args=('AB122020_sample_2780',))
# t2 = threading.Thread(target=randic3dplot, args=('AB122020_sample_5562',))
# t3 = threading.Thread(target=randic3dplot, args=('AB122020.txt',))

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

list = ['AB122020_sample_2780', 'AB122020_sample_5562', 'AB122020.txt']
# list = ['AB122020_sample_2780']
# list = ['AB122020.txt', 'AB122020.txt', 'AB122020.txt']
# list = ['AB122020.txt', 'AB122021.txt', 'AB122022.txt', 'AB189122.txt']
# list = ['AB122020.txt']

# pool = multiprocessing.
# pool.map(randic3dplot, list)

pool = ThreadPool(2)
pool.map(randic3dplot, list)
pool.close()
pool.join()

end_time = datetime.datetime.now()
time_taken = end_time - start_time

print('total_time_taken = {0}'.format(str(time_taken.seconds)))
