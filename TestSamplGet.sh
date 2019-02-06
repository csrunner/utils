#! /bin/bash

###############################################
# File:         TestSampleGet
# Description:  随机抽取视频
#
# Usage:        sh TestSampleGet \
#               -t type of sample library \
#               -n numbers of videos  \
#               -0 destination directory \
#
# author:       chaoshi.lk@gmail.com
# date:         3/8/2018
###############################################
#
#
# 检查入参
#
#---------------------------------------------
if [ $# -lt 3 ]
then
    echo "Error! Not Enough Params."
    echo "Usage : ./TestSampleGet.sh -t 1 -n 120 -o /run/media/root/Test "
    exit 1;
fi
#---------------------------------------------

#
# 定义变量
#
#---------------------------------------------
video_type=0;        # type of video
video_amount=0;            # amount of videos
des_dir=0;           # destination directory
#---------------------------------------------

#---------------------------------------------
#
# 解析入参
#
#---------------------------------------------

# optstring是"t:n:o:"，字符串optstring没有以冒号开头，
# 说明不进入slient error模式，如果getopts执行时有报错，
# (譬如非法选项，错误参数等)，会向错误输出打印错误信息。
#
# 另外t,n,0都是选项，每个选项后面都有冒号，
# 说明这四个选项都需要接收参数。
#
# OPTARG记录当前选项的参数值。
#
while getopts "t:n:o:" opt
do 
    case $opt in
        t) #set option "t"
            video_type=$OPTARG
            ;;
        n) #set option "n"
            video_amount=$OPTARG
            ;;
        o) #set option "o"
            des_dir=$OPTARG
            ;;
        *)
            echo "-$opt not recognized"
            ;;
    esac
done
if [ -d "$des_dir" ]; then
yes | rm -r "$des_dir"
fi
mkdir "$des_dir"
sudo python get_video_samples.py $video_type $video_amount $des_dir
#echo "video_type : $video_type"
#echo "number of videos : $video_amount"
#echo "destination directory : $des_dir"

