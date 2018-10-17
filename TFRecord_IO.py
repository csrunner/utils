# -*- coding:utf-8 -*-
__author__ = 'shichao'

import os
import tensorflow as tf
from PIL import Image
import cv2

cwd = os.getcwd()
classes = ['cctv1','cctv2']
def encode_TFRecord(cwd,filename,classes):
    '''
    encode images and their labels into the TF Record
    :param cwd:
    :param filename:
    :param classes:
    :return:
    '''
    writer = tf.python_io.TFRecordWriter(filename)
    for index,name in enumerate(classes):
        imgs_path = os.path.join(cwd,name)
        for img_name in os.listdir(imgs_path):
            img_path = os.path.join(imgs_path,img_name)
            # img = cv2.imread(img_path)
            # cv2.resize(img,[224,224],img)
            # img_b = cv2.
            img = Image.open(img_path)
            img = img.resize((224,224))
            img_raw = img.tobytes()
            TFrecord = tf.train.Example(features=tf.train.Feature(feature={
                'label':tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
                'img_raw':tf.train.Feature(bytes_list=tf.train.BytesList(value=[img_raw]))
            }))
            writer.write(TFrecord.SerializeToString())
    writer.close()


def decode_TFRecord_single(filename):
    '''
    decode the TF Record one by one
    :param filename:
    :return:
    '''
    for serialized_example in tf.python_io.tf_record_iterator(filename):
        example = tf.train.Example()
        example.ParseFromString(serialized_example)
        image = example.features.feature['image'].bytes_list.value
        label = example.features.feature['label'].int64_list.value
        print(image,label)


def decode_TFRecord_queue(filename):
    '''
    decode the TF Record in a queue
    :param filename:
    :return:
    '''
    filename_queue = tf.train.string_input_producer([filename])
    reader = tf.TFRecordReader()
    _,serialized_record = reader.read(filename_queue)
    features = tf.parse_single_example(serialized_record,
                                       features={
                                           'label':tf.FixedLenFeature([],tf.int64),
                                           'img_raw':tf.FixedLenFeature([],tf.string),
                                       })
    img = tf.decode_raw(features['img_raw'],tf.uint8)
    img = tf.reshape(img,[224,224,3])
    img = tf.cast(img,tf.float32)*(1./255)-0.5
    label = tf.cast(features['label'],tf.int32)

    return img,label


def main():
    img,label = decode_TFRecord_queue('train.tfrecords')
    img_batch,label_batch = tf.train.shuffle_batch([img,label],
                                                   batch_size=30,capacity=2000,
                                                   min_after_dequeue=1000)
    init = tf.initialize_all_variables()
    with tf.Session() as sess:
        sess.run(init)
        threads = tf.train.start_queue_runners(sess=sess)
        for i in range(3):
            val,l = sess.run([img_batch,label_batch])
            print(val.shape,l)

if __name__ == '__main__':
    main()