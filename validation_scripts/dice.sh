#!/usr/bin/env bash
# 
# 
# Ben Puccio
# 2016-06-02
#  
# 
# Run in test path
# Copy test image and gold standard pair into test path sub-directory for python script (nibabel)
# Use 3dcalc step to take away 0 voxels from mask (reduce impact of amount of CSF on dice calculation)


TestPath='/home/bpuccio/FS_Skullstrip/NFB3_Data_masks_r9_full'
GoldPath='/home/bpuccio/NFB3_Data_brain_mask_r9'

#make sub-directory
mkdir dice_step

#run in test path
for i in $(ls A*/*_brain.nii.gz) ; do
	name=${i#*/} ;
	fold=${i%%/*} ;	 
	3dcalc -a $i -expr "step(a)" -prefix dice_step/${fold}_test.nii.gz ;	
	3dcalc -a $GoldPath/${fold}/sub-${fold}_ses-NFB3_T1w_brain.nii.gz -expr "step(a)" -prefix dice_step/${fold}_gold.nii.gz ;
	echo ${fold} >> dice_step/filenames.txt ;
done

