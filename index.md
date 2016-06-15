---
layout: page
title: Skull Stripped Repository
---

Brain extraction, also known as skull stripping, is one of the first steps used in the preprocessing of neuroimaging data. The purpose is to remove non-brain regions from structural magnetic resonance imaging (MRI) data,in order to increase the quality of subsequent analyses. Many algorithms have been developed in order to solve the problem, though none have been able to overcome all of the challenges. In order to further the development of automatic brain extraction methods, 125 T1-weighted anatomical MRI scans from The Enhanced Rockland Sample Neurofeedback Study were used to create a repository of manually skull stripped T1-weighted MR images. The BEaST method (Brain extraction based on nonlocal segmentation technique) was used to create the initial masks, followed by bootstrapping and manual editing. In order to compare the quality of the repository, a few skull stripping packages were used on the anatomical scans. The results were quantified using our repository as gold truth data and can be compared to those using other datasets.

For more information, please see ...

**Table of Contents**

* [Downloading the Repository](#downloading-the-repository)
  * [Downloading Data from Your S3 Bucket](#downloading-data-from-your-S3-buckey)
* [Contributors](#contributor)


## Downloading the Repository

### File Requirements

* Original anonymized images, skull stripped brain images, and corresponding masks are in nifti (.nii) format.  
* The total amount of free hard disk space required is ?


### Downloading Data from Your S3 Bucket

If you ran QAP in the cloud, you will need to download the outputs from S3 before you can merge them.  To do this, run the following command:

    qap_download_output_from_S3.py {path to the S3 directory containing subject outputs} {path to AWS key file} {s3 bucket name} {type of measure to download} {directory to download to}

For example, if you wanted to obtain functional spatial measures from an S3 bucket named `the_big_run` with subject outputs in `subjects/outputs` you would use the following command.

    qap_download_output_from_S3.py subjects/outputs /home/wintermute/Documents/aws-keys.csv the_big_run func_spatial /home/wintermute/qap_outputs

With the above commands, the outputs will be stored in a directory named `qap_outputs` in the user *wintermute*'s home folder.  As with the pipeline commands from earlier, more information on this command's usage can be obtained by running it with the *-h* flag.  

## Contributors

Benjamin Puccio

Cameron Craddock

Elise Taverna


## References

[^1]:

[^2]:

[^3]:

[^4]:

[^5]:

[^6]:

[^7]:

[^8]:

[^9]:

[^10]:
