import sys
import sqlite3
import time
import os
import copy

#t=float(sys.argv[1]);
#print t;
#print time.ctime(t)

def candle_load(candle_file):
    kdata=[]
    idx=0
    for line in file(candle_file):
        temp={}
        l=line.strip().split(" ")
        open_sp=l[11]
        close_sp=l[12]
        high_sp=l[13]
        low_sp=l[14]
        sec_sp=l[15]
        msec_sp=l[16]
        close_sp=close_sp.split(":")
        open_sp=open_sp.split(":")
        high_sp=high_sp.split(":")
        low_sp=low_sp.split(":")
        sec_sp=sec_sp.split(":")
        msec_sp=msec_sp.split(":")

        temp[close_sp[0]]=float(close_sp[1]);
        temp[open_sp[0]]=float(open_sp[1]);
        temp[high_sp[0]]=float(high_sp[1]);
        temp[low_sp[0]]=float(low_sp[1]);
        temp[sec_sp[0]]=int(sec_sp[1]);
        temp[msec_sp[0]]=int(msec_sp[1]);

        candle=copy.deepcopy(temp);
        kdata.append(candle)
        
        idx=idx+1;
        if(idx>3):
            pass
            #break;
    return kdata
def candle_get_timediff(kdata):
    last_candle={}
    time_diff=[]
    for candle in kdata:
        if len(last_candle)==0:
            last_candle=candle;
            continue;
        else:
            time_diff.append(candle["sec"]-last_candle["sec"]);
            last_candle=candle;
            pass
    pass
    return time_diff

def candle_get_timeslot(kdata):
    last_candle={}
    time_slot=[]
    for candle in kdata:
        time_slot.append(candle["sec"]/60);
    pass
    return time_slot


candle_file=sys.argv[1];
kdata=candle_load(candle_file);
time_diff=candle_get_timediff(kdata);
time_slot=candle_get_timeslot(kdata);
print time_slot;
