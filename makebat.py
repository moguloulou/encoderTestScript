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
encoder = "./TAppEncoderStatic"

# Q値
#Q = range(22, 40, 5)
Q = (22,27,32,37,42,47)
# 設定ファイル
config = ('encoder_lowdelay_P_main','encoder_randomaccess_main')
sequencelist = ('classCif',)# "classHD")
testname = ('anchor',)

import os
outdir = "./RESULT/"
if not os.path.exists(outdir):
    os.makedirs(outdir)

#settings
intraperiod = -1
recfile = "rec"
# リストの読み込み
sequence = []
for tst in testname:
    refile = "%s_result.txt" % tst
    if os.path.exists(refile):
        os.remove(refile)
    for cfg in config:
        outdir = "./RESULT/% s/" % cfg
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        for seqset in sequencelist:
            outdir = "./RESULT/% s/" % cfg
            outdir += "% s/" % seqset
            if not os.path.exists(outdir):
                os.makedirs(outdir)
            if seqset is 'class720p':
                width = 1280
                height = 720
                framerate = 60
                framenum = 150
                yuvdir = "/share/Video/1280_720p_420/"
            elif seqset is 'classHD':       
                width = 1920
                height = 1080
                framerate = 60
                framenum = 150
                yuvdir = "/share/Video/1920_1080p_420/"
            else:
                width = 352
                height = 288
                framerate = 24
                framenum = 150
                yuvdir = "/share/Video/cif/"
            seqset += ".txt"
            for line in open(seqset):
                sequence = line.split() 
                for q in Q:
                    # ファイル名
                    name = os.path.splitext(sequence[0])[0]
                    name += "_%s" % tst
                    name += "_Q%02d" % q
                    #print " ".join((
                    #        encoder,
                    #        "-c %s.cfg"     % cfg,
                    #        "-i %s"         % os.path.join(yuvdir, sequence[0]),
                    #        "-b %s.bin"     % os.path.join(outdir, name),
                    #        "-wdt %s"       % width,
                    #        "-hgt %s"       % height,
                    #        "-fr %s"        % framerate,
                    #        "-f %s"         % framenum,
                    #        "-q %s"         % q,
                    #        "-ip %s"        % intraperiod,
                    #        "> %s.log"      % os.path.join(outdir, name)
                    #        #"-o %s.yuv"     % recfile,
                    #        #"--TargetBitrate=%s" %q,
                    #    ))
                    print " ".join((
                            "grep '    a' %s.log"       % os.path.join(outdir, name),
                            " >> %s"                    % refile
                        ))
            
