import pafy 
import re
import csv
with open('watch-history.txt','r') as myfile:
    data=myfile.read()
pattern=re.compile(r"""https?:\/\/(?:[0-9A-Z-]+\.)?(?:youtu\.be\/|youtube(?:-nocookie)?\.com\S*[^\w\s-])([\w-]{11})(?=[^\w-]|$)(?:[?=&+%\w.-]*(?:['"][^<>]*>|<\/a>))[?=&+%\w.-]*""", re.IGNORECASE) #https://www.youtube.com/watch?v=f-aDUXPmNWc
result = re.findall(pattern,data)
length=len(result)
print length
f1 = open("videorithik.txt", "w")
for i in range(0, len(result)):
   f1.write('http://www.youtube.com/watch?v=' + result[i] + '\n')
f1.close()
f = open('videorithik.txt', "r")
fi=open('datasetrithik.txt',"w")
attributes='@videoid,'+'@category,'+ '@channel name,'+'@viewcount,'+'@Timestamp,' +'@likes,'+'@dislikes,'+ '\n'
fi.write(attributes)

for line in f:
    try :
	v = pafy.new(line)
    	ids=v.videoid 
        cat= v.category
        channel= v.author
    	viewcount= v.viewcount
    	Timestamp= v.duration
    	likes= v.likes
    	dislikes=v.dislikes
    	if str(likes) == 'None':
    		likes=0
    	if str(dislikes) == 'None':
		dislikes=0
    	fi.write( ids+','+cat+','+channel+','+str(viewcount)+','+str(Timestamp)+','+str(likes)+','+str(dislikes)+'\n')
    except IOError as e:
    	print "I/O error({0}): {1}".format(e.errno, e.strerror)
f.close()
fi.close()
txt_file = "datasetrithik.txt"
csv_file = "datasetrithik.csv"
in_txt = csv.reader(open(txt_file, "rb"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'wb'))
out_csv.writerows(in_txt)
