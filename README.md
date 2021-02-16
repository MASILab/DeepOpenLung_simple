# DeepOpenLung Simple Overview

This is the first step of DeepOpenLung repository https://github.com/MASILab/DeepOpenLung. This repository is just for testing if the docker image can work well. Please visit the complete DeepOpenLung respository for more background. 


## image pre-process

> python3 ./1_preprocess/step1_main.py --sess_csv ${SPLIT_CSV} --prep_root ${PREP_ROOT} --ori_root ${ORI_ROOT}

```${SPLIT_CSV}``` is the csv file stores the scan list (and meta data) you want to test. 
```${PREP_ROOT}``` is the data folder saves the pre-processed result.
```${ORI_ROOT}``` is the data folder stores the scans you want to test.

## create pdf report

>python3 create_pdf.py --ori_root ${ORI_ROOT} --prep_root ${OUT_ROOT} --save_pdf_root ${OUT_ROOT}



# Docker

Docker image can be downloaded from docker hub: rg15/deeplungsimple:0.2

We can also use the DeepOpenLung example. INPUTS / OUTPUTS / config.yaml example can be downloaded from: 
https://vanderbilt.box.com/s/6h6388kw6h4jbjogd8yk1xqp9eotd3tv

Please run the following command if you use docker. 


(1)NIfTI: 
> sudo docker run -u root -v {LOCAL INPUTS PATH}:/INPUTS/ -v {LOCAL OUTPUTS PATH}:/OUTPUTS/ rg15/deeplungsimple:0.2 sh run_all.sh 


(2) For DICOM-cpu: 
> sudo docker run -u root -v {LOCAL INPUTS PATH}:/INPUTS/ -v {LOCAL OUTPUTS PATH}:/OUTPUTS/ rg15/deeplungsimple:0.2 sh run_all_DICOM.sh

## Requirements of running the docker

### Minimum Memory
CPU: 4 GB  

### Data Input
Modality: CT

Anatomy: Lungs

Projection: axial

Contrast: non

Slice thickness: 2.5

KVP: 120

X-Ray Tube Current (mAs): 120

Recon kernel/filter: 'STANDARD'

Windows Center: "40"

Window Width: "400"

Note this is the information for the example image. Other reasonable settings of a CT should also be working. 

### Data Output

Images: .nii.gz

PDF: .pdf

Text: None (for this simple demo)

CSV: None (for this simple demo)

