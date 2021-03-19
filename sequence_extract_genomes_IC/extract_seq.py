import csv
import os, sys, pathlib

with open('IC (n=1 to 6).csv') as csvfile:
	path = "sequences"
	# try:
    # 	os.makedirs(path)
	# except OSError as exc:  # Python >2.5
    # 	if exc.errno == errno.EEXIST and os.path.isdir(path):
    # 		pass
    # 	else:
    # 		raise
	pathlib.Path(path).mkdir(parents=True, exist_ok=True)
	reader = csv.DictReader(csvfile)
	count = 0
	for row in reader:
		locus_id = row['File Name']
		if locus_id:
			file_name = open(path + "/" + locus_id,"w+")
			file_name.write(row['Sequence'])
			count += 1
	print(count)
