# Ben Puccio
# 2016-06-02
#  

# parse log file for last entry that says time elapsed

import numpy as np
import glob
import time
import datetime


path='/home/bpuccio/BET/IBSR_nifti_stripped/log'
log_names=glob.glob(path+'*.log')

time=[]
splitter=[]
sec=[]

for i in log_names:
    with open(i,'r') as f:
        f=f.readlines()
    line = f[-1]
    if 'Time elapsed' in line:
        splitter=line.split(' ')
        hours=int(splitter[2])
        minutes=int(splitter[4])
        seconds=int(splitter[6])
        time.append([hours, minutes, seconds])
        x=(minutes*60)+seconds
        sec.append(x)

np_time=np.array(time)
np_sec=np.array(sec)

meantime=np.mean(np_sec)
stdtime=round(np.std(np_sec),0)

meanmin=int(meantime/60)
meansec=int(meantime-(meanmin*60))

print(meanmin, meansec, stdtime)







    
