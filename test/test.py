import sys
import sqlite3
import time
sys.path.append('./');
db = sqlite3.connect('datadir/tdata.sdb');
cu=db.cursor();
cu.execute("select * from  tdata_IF1404");
print len(cu.fetchall());
