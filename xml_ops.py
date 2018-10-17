# -*- coding:utf-8 -*-
__author__ = 'shichao'

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob


def get_xml_coordinate():
    xmls_path = glob.glob('/Users/shichao/workding_dir/others/*.xml')
    for xml_path in xmls_path:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for obj in root.iter('object'):
            xmlbox = obj.find('bndbox')
            b_xmin = float(xmlbox.find('xmin').text)
            b_xmax = float(xmlbox.find('xmax').text)
            b_ymin = float(xmlbox.find('ymin').text)
            b_ymax = float(xmlbox.find('ymax').text)

            return((b_xmin,b_xmax,b_ymin,b_ymax))

def main():
    print(get_xml_coordinate())

if __name__ == '__main__':
    main()