#!/usr/bin/env python

import os

LABELS_1 = './coco/labels/train2014'
LABELS_2 = './coco/labels/val2014'

for file in os.listdir(LABELS_1):
    f = open(os.path.join(LABELS_1, file), 'r')
    lines = f.readlines()
    f.close()
    target = open(os.path.join(LABELS_1, file), 'w')
    for l in lines:
        a = l.split(' ')
        target.write(('1' if int(a[0]) > 0 else '0') + ' ' + a[1] + ' ' + a[2] + ' ' + a[3] + ' ' + a[4] + '\n')
    target.close()
    
for file in os.listdir(LABELS_2):
    f = open(os.path.join(LABELS_2, file), 'r')
    lines = f.readlines()
    f.close()
    target = open(os.path.join(LABELS_2, file), 'w')
    for l in lines:
        a = l.split(' ')
        target.write(('1' if int(a[0]) > 0 else '0') + ' ' + a[1] + ' ' + a[2] + ' ' + a[3] + ' ' + a[4] + '\n')
    target.close()
    
    
