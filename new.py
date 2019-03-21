import csv
txt_file = r"datasetsai.txt"
csv_file = r"datasetsais.csv"
in_txt = csv.reader(open(txt_file, "rb"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'wb'))
out_csv.writerows(in_txt)
