# -*- coding:utf-8 -*-
__author__ = 'shichao'
import os
import glob
import shutil

def create_smallset(root_in,root_out,rate):
    counter = 0
    dirs = os.listdir(root_in)
    for dir in dirs:
        if os.path.isfile(os.path.join(root_in,dir)):
            continue
        file_dir = os.path.join(root_in,dir)
        os.mkdir(os.path.join(root_out,dir))
        filelists = [n for n in glob.glob(os.path.join(file_dir,'*.pdf')) if os.path.isfile(n)]


        # test the number and basename of files in the directory
        # print('the number of files in directory {} is {}'.format(dir,len(filelist)))
        # for filelist in filelists:
        #     print(os.path.basename(filelist))
        for filelist in filelists:
            if os.path.isfile(filelist):
                filename = os.path.basename(filelist)
                while counter < int(len(filelists)*rate):
                    shutil.copy(filelist,os.path.join(os.path.join(root_out,dir),filename))




def main():
    root_in = '/Users/shichao/workding_dir/paper/'
    root_out = '/Users/shichao/workding_dir/paper/'
    rate = 0.3
    create_smallset(root_in,root_out,rate)


if __name__ == '__main__':
    main()
