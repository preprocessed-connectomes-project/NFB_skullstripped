#DICE coefficient plot

#Ben Puccio
#2016-06-08
#
#
#Load numpy arrays of IBSR & LPBA40 dice coefficients from dice.py
#Make boxplot using Matplotlib and Seaborn

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#read each dice numpy array
ss = np.load('/home/bpuccio/dice/IBSR_dice_3dSkullStrip.npy')
fs = np.load('/home/bpuccio/dice/IBSR_dice_FS.npy')
bet = np.load('/home/bpuccio/dice/IBSR_dice_BET.npy')
beast = np.load('/home/bpuccio/dice/IBSR_dice_BEaSTlib.npy')
beastN = np.load('/home/bpuccio/dice/IBSR_dice_BEaSTNFBS.npy')

#read each dice numpy array
ss2 = np.load('/home/bpuccio/dice/LPBA40_dice_3dSkullStrip.npy')
fs2 = np.load('/home/bpuccio/dice/LPBA40_dice_FS.npy')
bet2 = np.load('/home/bpuccio/dice/LPBA40_dice_BET.npy')
beast2 = np.load('/home/bpuccio/dice/LPBA40_dice_BEaSTlib.npy')
beastN2 = np.load('/home/bpuccio/dice/LPBA40_dice_BEaSTNFBS.npy')

#print avg dice
print('IBSR')
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
beastd_mean = np.mean(beast)
beastd_std = np.std(beast)
beastd_mean_r = round(beastd_mean, 3)
beastd_std_r = round(beastd_std, 3)
print('BEaST',beastd_mean_r,beastd_std_r)
beastNd_mean = np.mean(beastN)
beastNd_std = np.std(beastN)
beastNd_mean_r = round(beastNd_mean, 3)
beastNd_std_r = round(beastNd_std, 3)
print('BEaST w/ NFBS',beastNd_mean_r,beastNd_std_r)

print('LPBA40')
sd2_mean = np.mean(ss2)
sd2_std = np.std(ss2)
sd2_mean_r = round(sd2_mean, 3)
sd2_std_r = round(sd2_std, 3)
print('3dSkullStrip',sd2_mean_r,sd2_std_r)
fsd2_mean = np.mean(fs2)
fsd2_std = np.std(fs2)
fsd2_mean_r = round(fsd2_mean, 3)
fsd2_std_r = round(fsd2_std, 3)
print('FreeSurfer',fsd2_mean_r,fsd2_std_r)
betd2_mean = np.mean(bet2)
betd2_std = np.std(bet2)
betd2_mean_r = round(betd2_mean, 3)
betd2_std_r = round(betd2_std, 3)
print('BET',betd2_mean_r,betd2_std_r)
beastd2_mean = np.mean(beast2)
beastd2_std = np.std(beast2)
beastd2_mean_r = round(beastd2_mean, 3)
beastd2_std_r = round(beastd2_std, 3)
print('BEaST',beastd_mean_r,beastd_std_r)
beastNd2_mean = np.mean(beastN2)
beastNd2_std = np.std(beastN2)
beastNd2_mean_r = round(beastNd2_mean, 3)
beastNd2_std_r = round(beastNd2_std, 3)
print('BEaST w/ NFBS',beastNd2_mean_r,beastNd2_std_r)

#make data nice for IBSR
data1 = np.concatenate((bet, ss, fs, beast, beastN))
name1 = np.array(['BET']*len(bet))
name2 = np.array(['3dSkullStrip']*len(ss))
name3 = np.array(['FreeSurfer']*len(fs))
name4 = np.array(['BEaST']*len(beast))
name5 = np.array(['BEaST w/ NFBS']*len(beastN))
names1 = np.concatenate((name1, name2, name3, name4, name5))

#make data nice for LPBA40
data2 = np.concatenate((bet2, ss2, fs2, beast2, beastN2))
Lname1 = np.array(['BET']*len(bet2))
Lname2 = np.array(['3dSkullStrip']*len(ss2))
Lname3 = np.array(['FreeSurfer']*len(fs2))
Lname4 = np.array(['BEaST']*len(beast2))
Lname5 = np.array(['BEaST w/ NFBS']*len(beastN2))
names2 = np.concatenate((Lname1, Lname2, Lname3, Lname4, Lname5))

#make 1 big array
datanamesA = np.array(['IBSR']*len(names1))
datanamesB = np.array(['LPBA40']*len(names2))
dataname = np.concatenate((datanamesA, datanamesB))
name= np.concatenate((names1, names2))
data = np.concatenate((data1, data2))
dictionary={'Dice':data,'Algorithm':name,'Dataset':dataname}
df=pd.DataFrame(data=dictionary)

#make boxplot
sns.set_style("whitegrid")
box_plot=sns.boxplot(y='Dice', x='Algorithm', hue='Dataset', data=df, palette="Set3")
#plt.xticks(np.arange(5),names)
plt.xlabel('Skull-Stripping Methods')
plt.ylabel('Dice Similarity Coefficients')
plt.ylim((0.7,1.0))
plt.title('IBSR & LPBA40')
plt.legend(frameon=True, title='Dataset', loc=7)
plt.savefig('boxplot_I&L.png')

