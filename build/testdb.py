import sys
import sqlite3
import time
import os


def get_title(db,tb_name):
    cu=db.cursor();
    sql="PRAGMA table_info(%s);" %(tb_name)
    print sql
    l=[]
    d=cu.execute(sql);
    d=cu.fetchall()
    for item in d:
        l.append(item[1])
    return l;
def dump(title, data,fname):
    f=open(fname,"w")
    for item in title:
        print >>f,item,"\t",
    print>>f
    for items in data:
        for item in items:
            print >>f,item,"\t",
	print >>f

sys.path.append('./');
db = sqlite3.connect('datadir/tdata.sdb');
cu=db.cursor();

title=get_title(db, "tdata_IF1404");
titlemap={}
idx=0;
for item in title:
    titlemap[item]=idx;
    idx=idx+1

print title;
#1397466840

start_time=time.strptime("9:00:00 20140416",'%H:%M:%S %Y%m%d')
end_time=time.strptime("15:15:00 20140416",'%H:%M:%S %Y%m%d')

print start_time
start= time.mktime(start_time)
end= time.mktime(end_time)

cu.execute("select * from  tdata_IF1404 where sec > %d and sec < %d order by sec asc,msec asc" % (start,end));
d=cu.fetchall();
print start,"---",end;
print len(d);
print d[0];
print d[1];
print d[2];
#localtime = time.localtime(time.time())


dump(title,d,"1.txt");
real_start=d[0][titlemap['sec']]
real_end=d[-1][titlemap['sec']]
print time.ctime(real_start),"---",time.ctime(real_end)





