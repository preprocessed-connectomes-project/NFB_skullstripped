#DICE coefficient

#Ben Puccio
#2016-06-02
#
#use after running dice.sh
#calculate dice coefficients for each test image and gold standard image pair 
#save in numpy array


import numpy as np
import nibabel as nib
import glob


#get filenames
path='/home/bpuccio/3dSkullStrip/LPBA40_anat/dice_step/'
test_filenames=glob.glob(path+'*_test.nii.gz')
gold_filenames=glob.glob(path+'*_gold.nii.gz')

dice=[]

#iterate over each line in the text file
for i in test_filenames:
    
    g=str.rstrip(i,'_test.nii.gz')
    gname=g+'_gold.nii.gz'
	
    #load test image
    test = nib.load(i)
    test_img = test.get_data()

    #load gold standard image
    gold = nib.load(gname)
    gold_img = gold.get_data()

    #calculate the intersection of the two
    intersect = np.multiply(test_img, gold_img) 
    num_in = np.transpose(intersect.nonzero())
    in_size = num_in.shape[0]

    #calculate num of voxels in mask for test & gold
    t_mask = np.transpose(test_img.nonzero())
    t_mask_size = t_mask.shape[0]
    g_mask = np.transpose(gold_img.nonzero())
    g_mask_size = g_mask.shape[0]	

	
    #dice equation
    x=((in_size)*2.0)/((t_mask_size)+(g_mask_size))
    dice.append(x)
    #jaccard or other calculations?
    

#write dice coefficients to csv file
import csv
outcv = open(path+'dice.csv',"wb+")
writer = csv.writer(outcv, quoting=csv.QUOTE_NONNUMERIC)
writer.writerow(('Number', 'Dice coeffient'))
for i in range((len(dice))):
    writer.writerow((i+1, round(dice[i], 3)))

#average dice
dicenp = np.array(dice)
d_mean = np.mean(dicenp)
d_std = np.std(dicenp)
d_mean_r = round(d_mean, 3)
d_std_r = round(d_std, 3)
writer.writerow(('AVERAGE_DICE', d_mean_r, d_std_r))
print(d_mean_r, d_std_r)

#save dice numpy array to file
np.save('/home/bpuccio/dice/LPBA40_dice_3dSkullStrip', dicenp)

#close csv
outcv.close()






