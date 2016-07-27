#!/usr/bin/env bash
# 
# BEaSTSkullStrip.sh
# Using BEaST to do SkullStriping
# [see here](https://github.com/FCP-INDI/C-PAC/wiki/Concise-Installation-Guide-for-BEaST) for instructions for BEaST.
# 
# 
# Benjamin Puccio, shell script for implemenatation of BEaST
# Based off of (minor changes to):
#
# Qingyang Li
# 2013-07-29
#  
# The script requires AFNI, BEaST, MINC toolkit.

do_anyway=1

# set the timing
SECONDS=0

MincPATH='/opt/minc'
source $MincPATH/minc-toolkit-config.sh

MincLibPATH='/home/bpuccio/library_NFBS'
NumLibImgs=20

MNItemplatePATH='/opt/minc/share/atlas'

cwd=`pwd`

if [ $# -lt 1  ]
then 
  echo " USAGE ::  "
  echo "  beastskullstrip.sh <input> [output prefix] " 
  echo "   input: anatomical image with skull, in nifti format " 
  echo "   output: The program will output: " 
  echo "      1) a skull stripped brain image in scanner space; "  
  echo "      2) skull stripped brain masks in mni spcae and scanner space. "
  echo "      3) anatomical image transformed to mni space "
  echo "      4) minc files of brain mask and anatomical, both in mni space (for beast library)"
  echo "   Option: output prefix: the filename of the output files without extention"
  echo " Example: beastskullstrip.sh ~/data/head.nii.gz ~/brain "
  exit
fi

if [ $# -ge 1 ]
then
    inputDir=$(dirname $1)
    if [ $inputDir == "." ]
    then
        inputDir=$cwd
    fi

    filename=$(basename $1)
    inputFile=$inputDir/$filename

    extension="${filename##*.}"
    if [ $extension == "gz" ]
    then
        filename="${filename%.*}"
    fi

    filename="${filename%.*}"
    out=$inputDir/$filename
fi

if [ $# -ge 2 ]
then
    outputDir=$(dirname $2)
    if [ $outputDir == "." ]
    then
        outputDir=$cwd
        out=$outputDir/$2
    else
        mkdir -p $outputDir
        out=$2
    fi
fi

workingDir=`mktemp -d`
#workingDir=`pwd`
echo " ++ working directory is $workingDir"
cd $workingDir

if [ ! -f head.nii ]
then 
    3dcopy $inputFile head.nii
fi

if [ ! -f head.mnc ]
then
    nii2mnc head.nii head.mnc
fi

flist=head.mnc
# Normalize the input
if [ ! -f head_mni.mnc ] && [ ! -f anat2mni.xfm ] || [ $do_anyway -eq 1 ]
then
    beast_normalize head.mnc head_mni.mnc anat2mni.xfm -modeldir $MNItemplatePATH
fi
flist="$flist head_mni.mnc"

# Run BEaST to do SkullStripping
# configuration file can be replaced by $MincLibPATH/default.2mm.conf or $MincLibPATH/default.4mm.conf

if [ ! -f brain_mask_mni.mnc ] || [ $do_anyway -eq 1 ]
then
    mincbeast -selection_num $NumLibImgs -verbose -same_res -median -fill -conf $MincLibPATH/default.1mm.conf $MincLibPATH head_mni.mnc brain_mask_mni.mnc
fi
flist="$flist brain_mask_mni.mnc"

# Trasform brain mask to it's original space
if [ ! -f brain_mask.mnc ] || [ $do_anyway -eq 1 ]
then
    mincresample -invert_transformation -like head.mnc -transformation anat2mni.xfm brain_mask_mni.mnc brain_mask.mnc
fi
flist="$flist brain_mask.mnc"

# Convert image from MNC to NII format.

if [ ! -f brain_mask_tmp.nii ] || [ $do_anyway -eq 1 ]
then
    mnc2nii brain_mask.mnc brain_mask_tmp.nii
fi

if [ ! -f brain_mask_orig.nii ] || [ $do_anyway -eq 1 ]
then
    3dresample -master head.nii -inset brain_mask_tmp.nii -prefix brain_mask_orig.nii
fi
flist="$flist brain_mask_tmp.nii brain_mask_orig.nii"

if [ ! -f brain_mask_mni.nii ] || [ $do_anyway -eq 1 ]
then
    mnc2nii brain_mask_mni.mnc brain_mask_mni.nii
fi
flist="$flist brain_mask_mni.nii"

if [ ! -f head_mni.nii ] || [ $do_anyway -eq 1 ]
then
    mnc2nii head_mni.mnc head_mni.nii
fi
flist="$flist head_mni.nii"


# Generate and output brain image and brain mask
if [ ! -f head_brain.nii.gz ] || [ $do_anyway -eq 1 ]
then
    3dcalc -a brain_mask_orig.nii -b head.nii -expr "step(a)*b" -prefix head_brain.nii.gz
fi
flist="$flist head_brain.nii"

# output files

# fix the AFNI won't overwrite problem.
rm -rf ${out}_brainmask.nii.gz ${out}_brain.nii.gz ${out}_head_mni.nii.gz ${out}_brain_mask_mni.nii.gz ${out}_head_mni.mnc ${out}_brain_mask_mni.mnc

3dcopy brain_mask_orig.nii ${out}_brainmask.nii.gz
3dcopy head_brain.nii.gz ${out}_brain.nii.gz
3dcopy brain_mask_mni.nii ${out}_brain_mask_mni.nii.gz
3dcopy head_mni.nii ${out}_head_mni.nii.gz
mv head_mni.mnc ${out}_head_mni.mnc
mv brain_mask_mni.mnc ${out}_brain_mask_mni.mnc
mv anat2mni.xfm ${out}_anat2mni.xfm

# delete all intermediate files
rm -rf $flist
echo "  ++ working directory is $workingDir"
cd $cwd

duration=$SECONDS
echo "Time elapsed $(( $duration / 3600 )) hours, $(( $duration / 60 )) minutes, $(( $duration % 60 )) seconds"
 
