# -*- coding:utf-8 -*-
__author__ = 'shichao'

import os
import tarfile

def targz_demo(output_filename, source_dir):
    '''
    This function compress directories into tar file
    :param output_filename: '/Users/shichao/Downloads/transport/dataset.tar'
    :param source_dir: '/Users/shichao/Downloads/transport/dataset'
    :return:
    '''
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

def targz(out_dir,in_rootdir):
    dirs = os.listdir(in_rootdir)
    for dir in dirs:
        out_filename = os.path.join(out_dir,dir)
        with tarfile.open(out_filename, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(in_rootdir))

def untar(in_dir,out_dir):
    for parent, dirs, files in os.walk(in_dir):
        for file in files:
            filename = os.path.join(parent,file)
            t = tarfile.open(filename)
            t.extract(path=out_dir)


if __name__ == '__main__':

    output_filename = '/Users/shichao/Downloads/transport/dataset.tar'
    source_dir = '/Users/shichao/Downloads/transport/dataset'
    targz(output_filename,source_dir)