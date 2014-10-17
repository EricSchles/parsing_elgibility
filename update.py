#started college in 2010
#born in 1991 or later

data = []
with open("sheet.csv","r") as f:
    for line in f:
        line = line.replace("\n","")
        line = line.split(",")
        data.append(line)

#fields we care about: 2,3
final_data = []
for datum in data[1:]:
    final_datum = []
    print datum[2]
    if datum[2] != '':
        birth_year = int(datum[2])
    else:
        continue
    if datum[3] != '':
        college_start = int(datum[3])
    else:
        continue
    final_datum = datum[:] #create a copy of the data
    if birth_year > 1991 and college_start > 2010:
        final_datum.append("elligible")
    else:
        final_datum.append("letter required")
    final_data.append(final_datum)

with open("result.csv","w") as f:
    header = ",".join(data[0])
    header += "\n"
    f.write(header)
    for line in final_data:
        line = ",".join(line) 
        line += "\n"
        f.write(line)
