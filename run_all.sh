#!/bin/bash

IN_ROOT=$(readlink -f ${1-/INPUTS}) #/INPUTS
OUT_ROOT=$(readlink -f ${2-/OUTPUTS}) # /OUTPUTS
CONFIG_PATH=$(readlink -f ${3-/config.yaml}) # /config.yaml
LOG_PATH=$(readlink -f ${4-/LOG}) # log file

exec > ${LOG_PATH}

PREP_ROOT=${OUT_ROOT}/Synthesis/NIFTI
PDF_ROOT=${OUT_ROOT}/PDF

mkdir -p ${OUT_ROOT}/Synthesis
mkdir -p ${PREP_ROOT}
mkdir -p ${PDF_ROOT}


ORI_ROOT=${IN_ROOT}/NIFTI
#SPLIT_CSV=${IN_ROOT}/SUBINFO/test_nifti.csv

echo "Run step 1 data preprocessing ..."

python3 ./1_preprocess/step1_main.py --prep_root ${PREP_ROOT} --ori_root ${ORI_ROOT} 

echo " step 1 data preprocess finished !"

echo "Run  creating PDF ..."

python3 create_pdf.py --ori_root ${ORI_ROOT} --prep_root ${PREP_ROOT} --save_pdf_root ${PDF_ROOT}


echo " PDF created !"