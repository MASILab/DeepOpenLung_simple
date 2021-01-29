#!/bin/bash

IN_ROOT=$(readlink -f ${1-/INPUTS}) #/INPUTS
OUT_ROOT=$(readlink -f ${2-/OUTPUTS}) # /OUTPUTS
CONFIG_PATH=$(readlink -f ${3-/config.yaml}) # /config.yaml


PREP_ROOT=${OUT_ROOT}/temp/prep

mkdir -p ${OUT_ROOT}/temp
mkdir -p ${PREP_ROOT}


ORI_ROOT=${IN_ROOT}/NIfTI
SPLIT_CSV=${IN_ROOT}/SUBINFO/test_dcm.csv

echo "Convert DICOM to NIFTI ..."

python3 ./Tools/DCM2NII.py --sess_root ${IN_ROOT}/DICOM --nifti_root ${ORI_ROOT} --sess_csv ${SPLIT_CSV}

echo " step 1 data preprocess"

python3 ./1_preprocess/step1_main.py --sess_csv ${SPLIT_CSV} --prep_root ${PREP_ROOT} --ori_root ${ORI_ROOT} 

echo " step 1 data preprocess finished !"


