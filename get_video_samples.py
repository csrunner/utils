# chao shi
import os
import random
import shutil
import sys
'''
def eachFile(file_path):
    list_file = []
    for parent,dirnames,filenames in os.walk(file_path):
        for filename in filenames:
            list_file.append(os.path.join(di))
    selected_file_list = [random.randint(0,len(list_file)) for _ in range(n)]
    for i in range(len(selected_file_list)):
'''
if __name__ == '__main__':
    t = sys.argv[1]
    n = sys.argv[2]
    o = sys.argv[3]
    file_path = '/home/mayue/github/ROLO2/' if t == 1 else '/home/mayue/github/unet3/'
    if (not os.path.exists(file_path)):
        print("video path does not exist, modify the path in the source code")
        sys.exit(0)
    targetDir = o
    #targetDir = '/home/mayue/Documents/test'
    '''
    pathDir = os.listdir(file_path)
    for allDir in pathDir:
        child = os.path.join('%s%s'%(file_path,allDir))
        print(child)
    '''
    list_all = []
    for parent,dirnames,filenames in os.walk(file_path):
        for file in filenames:
            list_all.append(os.path.join(parent,file))
    list_selected = random.sample(list_all,int(n))
    #list_selected_number = [random.randint(0,n) for _ in range()]
    for i,val in enumerate(list_selected):
        shutil.copy(val,targetDir)
#main(sys.argv[1],sys.argv[2],sys.argv[3])
