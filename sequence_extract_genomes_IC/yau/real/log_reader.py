out_file = open('log.out', 'w+')

with open('yau_result.out') as file:
    while True:
        line = file.readline()
        if line is None:
            break
        if "sequences" in line:
            out_file.write(line + ", ")
        if "gr: " in line:
            out_file.write(line + "\n")

out_file.close()
