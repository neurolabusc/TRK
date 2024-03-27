#!/usr/bin/env python

#https://github.com/brainlife/app-convert-tck-to-trk/blob/master/convert_tck_to_trk.py
# MIT License Copyright (c) 2018 BrainLife
import json
import nibabel as nib
import sys
from nibabel.streamlines import Field
from nibabel.orientations import aff2axcodes


def main():
    if len(sys.argv) < 4:
        print('No filename or threshold provided:')
        print(' '+sys.argv[0]+ ' track.tck MNI152_T1_2mm_brain_mask.nii.gz track.trk')
        sys.exit()
    tck_file = sys.argv[1]
    anatomy_file = sys.argv[2]
    trk_file = sys.argv[3]
    nii = nib.load(anatomy_file)
    header = {}
    header[Field.VOXEL_TO_RASMM] = nii.affine.copy()
    header[Field.VOXEL_SIZES] = nii.header.get_zooms()[:3]
    header[Field.DIMENSIONS] = nii.shape[:3]
    header[Field.VOXEL_ORDER] = "".join(aff2axcodes(nii.affine))
    tck = nib.streamlines.load(tck_file)
    nib.streamlines.save(tck.tractogram, trk_file, header=header)

        
if __name__ == '__main__':
        main()