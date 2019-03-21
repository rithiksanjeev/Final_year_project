import csv
import re
data = {}
with open("Adds.csv","wb+") as resultfile:
	with open("Advertisement.csv") as inf2:
       		for row in csv.reader(inf2):
			data[row[1]] = row
			data[row[0][1]]="video_ads"
		with open("Advertisement_users.csv","rb+") as inf1:
			for row in csv.reader(inf1):
				if row[1] in data:
		        		print (data[row[1]])
					wr = csv.writer(resultfile)
					wr.writerow(data[row[1]])
with open("Adds.csv", 'r') as f:
    my_csv_text = f.read()
find_str = 'videoid'
replace_str = 'videoid_ads'
new_csv_str = re.sub(find_str, replace_str, my_csv_text)
new_csv_path = 'Adds.csv'
with open(new_csv_path, 'w') as f:
    f.write(new_csv_str)
