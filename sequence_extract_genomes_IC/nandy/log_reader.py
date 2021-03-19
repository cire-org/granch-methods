# out_file = open('log.out', 'w+')

with open('nandy_results') as file:
    with open('log.out', 'w+') as out_file:
        for line in file:
            # line = file.readline()
            # if line is None:
            #     break
            if "fasta" in line:
                out_file.write(line + ", ")
            if "gr_value" in line:
                out_file.write(line + "\n")

out_file.close()
