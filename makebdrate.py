#!/usr/bin/python
# coding: utf-8

# テスト実行用のバッチファイルを作成する。
#
# 使用例：
# mkdir test
# ./makebat.py > test/bat.sh
# cp ~/h265/bin/TAppEncoderStatic test/
# cd test/
# sh bat.sh
# エンコーダー

# Q値
Q = (22,27,32,37)
# 設定ファイル
sequencelist = ('class720p',)# "classHD")
config = 'encoder_lowdelay_P_main'

#set two group
result_dir = './'
testname_anchor = 'anchor_result.txt'
testname_test   = 'fixQP_result.txt'

import os
import sys
import numpy
from bdrate import bdrate 
# リストの読み込み
try:
    anchor = open(os.path.join(result_dir, testname_anchor),"r")
except IOError:
    print('There was an error opening the file!')
    sys.exit()    
try:
    test = open(os.path.join(result_dir, testname_test),"r")
except IOError:
    print('There was an error opening the file!')
    sys.exit()
    
sequence = [] 

for seqset in sequencelist:
    seqset += ".txt"
    for line in open(seqset):
        sequence = line.split() 
        name = os.path.splitext(sequence[0])[0]
        result = []
        for q in Q:
            if 'anchor' in locals():
                a = anchor.readline().split()
                result.append(a[2])
                result.append(a[3])
            if 'test' in locals():
                t = test.readline().split()
                result.append(t[2])
                result.append(t[3])
        #re_anchor_bits = numpy.vstack([re_anchor_bits, re_anchor_psnr])
        #re_test_bits = numpy.vstack([re_test_bits, re_test_psnr])
        re = bdrate(result)
        print " ".join((
                "%s    "       % name,
                "%s"           % re
            ))
            
