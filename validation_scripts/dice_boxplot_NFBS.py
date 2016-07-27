#DICE coefficient plot

#Ben Puccio
#2016-06-08
#
#
#Load numpy arrays of NFBS dice coefficients from dice.py
#Make boxplot using Matplotlib and Seaborn

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#read each dice numpy array
ss = np.load('/home/bpuccio/dice/dice_3dSkullStrip.npy')
fs = np.load('/home/bpuccio/dice/dice_FS.npy')
bet = np.load('/home/bpuccio/dice/dice_BET.npy')

#print avg dice
sd_mean = np.mean(ss)
sd_std = np.std(ss)
sd_mean_r = round(sd_mean, 3)
sd_std_r = round(sd_std, 3)
print('3dSkullStrip',sd_mean_r,sd_std_r)
fsd_mean = np.mean(fs)
fsd_std = np.std(fs)
fsd_mean_r = round(fsd_mean, 3)
fsd_std_r = round(fsd_std, 3)
print('FreeSurfer',fsd_mean_r,fsd_std_r)
betd_mean = np.mean(bet)
betd_std = np.std(bet)
betd_mean_r = round(betd_mean, 3)
betd_std_r = round(betd_std, 3)
print('BET',betd_mean_r,betd_std_r)

#make data nice
data = np.concatenate((bet, ss, fs))
name1 = np.array(['BET']*len(bet))
name2 = np.array(['3dSkullStrip']*len(ss))
name3 = np.array(['FreeSurfer']*len(fs))
name = np.concatenate((name1, name2, name3))
dataname = np.array(['NFBS']*len(name))
dictionary={'Dice':data,'Algorithm':name,'Dataset':dataname}
df=pd.DataFrame(data=dictionary)

#make boxplot
sns.set_style("whitegrid")
b=sns.color_palette(["#866080"])
box_plot=sns.boxplot(y='Dice', x='Algorithm', data=df, palette=b)
plt.xlabel('Skull-Stripping Methods')
plt.ylabel('Dice Similarity Coefficients')
plt.ylim((0.7,1.0))
plt.title('NFBS')
plt.savefig('boxplot_NFBS2.png')

