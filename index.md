---
layout: page
title: NFBS Skull-Stripped Repository
---

Brain extraction, also known as skull stripping, is one of the first steps used in the preprocessing of neuroimaging data. The purpose is to remove non-brain tissue from structural magnetic resonance imaging (MRI) data in order to increase the quality of subsequent analyses. Many algorithms have been developed in order to solve the problem, though none have been able to overcome all of the challenges. In order to facilitate the development of automatic brain extraction methods, 125 T1-weighted anatomical MRI scans from The Enhanced Rockland Sample Neurofeedback Study were used to create a repository of manually skull stripped T1-weighted MR images.

The BEaST method (brain extraction based on nonlocal segmentation technique) was used to create the initial masks, followed by bootstrapping some of the manually edited masks into its reference library. Maual editing was performed using the Freeview visualization software from Freeview. In total, 72 of the masks were hand edited and 43 were deemed good enough to be released. In order to compare the quality of the repository, a few skull stripping algorithms were used on the anatomical scans. The results were quantified using our repository as gold truth data and were compared to those using other datasets.

The Neurofeedback Skull-stripped (NFBS) repository is available for download on the NFB\_skullstripped Github page, which can be found on the Preprocessed Connectomes Project website. It will allow researchers and data scientists to test brain extraction methods, as well as for training data in machine learning based algorithms.

For more information, please see ...

**Table of Contents**

* [Contents of the Repository](#contents-of-the-repository)
* [Downloading the Repository](#downloading-the-repository)
* [Contributors](##contributor)


## Contents of the Repository

The repository contains data from 125 participants, ranging from 21 to 45 years old. For each participant, the repository contains:

* Structural T1-weighted image in NiFTI format (.nii.gz)
* Skull-stripped image in NiFTI format (.nii.gz)
* Brain mask in NiFTI format (.nii.gz)



## Downloading the Repository

Please go to our github page, http://www.github.com/preprocessed-connectomes-project/NFB_skullstripped

The images are available in NiFTI format (.nii.gz).

The total amount of free hard disk space required is ?

## Contributors

Benjamin Puccio

Cameron Craddock

Carol Froehlich

Amalia McDonald

John Pellman

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
