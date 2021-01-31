import yaml
import numpy as np
import matplotlib.pyplot as plt
from skimage import io 
import fitz
from PyPDF2 import PdfFileWriter
import argparse
import pandas as pd
import os
import nibabel as nib
import pdb

parser = argparse.ArgumentParser()

parser.add_argument('--ori_root', type=str, default='/nfs/masi/gaor2/tmp/justtest',
                        help='the root of original data')

parser.add_argument('--prep_root', type=str, default='/nfs/masi/gaor2/tmp/justtest/prep',
                    help='the root for save result data')

parser.add_argument('--save_pdf_root', type=str, default='/nfs/masi/gaor2/tmp/justtest/prep',
                    help='the root for save result data')

# parser.add_argument('--file_name', type=str, default='/input',
#                         help='sessions want to be tested')

args = parser.parse_args()

pdf_writer = PdfFileWriter()
pdf_writer.addBlankPage(width=220, height=350)
from pathlib import Path
with Path("./blank.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

file_names = os.listdir(args.ori_root)
file_names = [i for i in file_names if '.nii' in i]
for file_name in file_names:
    tmp_id = file_name.replace('.nii.gz', '')
    #img = np.load(args.prep_root + '/' + file_name)
    img = nib.load(args.prep_root + '/' + file_name.replace('.nii.gz', '_clean.nii.gz'))
    
    img_npy = img.get_fdata()
    io.imsave('./temp_img.png', img_npy[int(img.shape[0] / 2)])

    image_rectangle = fitz.Rect(10,10,110,110)

    # retrieve the first page of the PDF
    file_handle = fitz.open('./blank.pdf')
    first_page = file_handle[0]
    pix = fitz.Pixmap('./temp_img.png') 
    # add the image 
    first_page.insertImage(image_rectangle, pixmap=pix) 

    
    io.imsave('./temp_img.png', img_npy[:, int(img.shape[1] / 2)][::-1])

    image_rectangle = fitz.Rect(10,110,110,210)

    # retrieve the first page of the PDF
    #file_handle = fitz.open('./blank.pdf')
    first_page = file_handle[0]
    pix = fitz.Pixmap('./temp_img.png') 
    # add the image 
    first_page.insertImage(image_rectangle, pixmap=pix) 
    
    
    io.imsave('./temp_img.png', img_npy[:, :, int(img.shape[2] / 3)][::-1])

    image_rectangle = fitz.Rect(10,210,110,310)

    # retrieve the first page of the PDF
    #file_handle = fitz.open('./blank.pdf')
    first_page = file_handle[0]
    pix = fitz.Pixmap('./temp_img.png') 
    first_page.insertImage(image_rectangle, pixmap=pix) 
    file_handle.save(args.save_pdf_root + '/' + tmp_id + '.pdf')

