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

Docker image can be downloaded from docker hub: rg15/deeplungsimple:0.1 

We can also use the DeepOpenLung example. INPUTS / OUTPUTS / config.yaml example can be downloaded from: 
https://vanderbilt.box.com/s/6h6388kw6h4jbjogd8yk1xqp9eotd3tv


(1)NIfTI: 
> sudo docker run -u root -v {LOCAL INPUTS PATH}:/INPUTS/ -v {LOCAL OUTPUTS PATH}:/OUTPUTS/ deeplungsimple:0.1 sh run_all.sh 


(2) For DICOM-cpu: 
> sudo docker run -u root -v {LOCAL INPUTS PATH}:/INPUTS/ -v {LOCAL OUTPUTS PATH}:/OUTPUTS/ deeplungsimple:0.1 sh run_all_DICOM.sh




