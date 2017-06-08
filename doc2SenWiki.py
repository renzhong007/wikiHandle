# -*- coding:utf8 -*-

import codecs
import segtok.segmenter as segter

# wikipedia 提取出文档text后 会以<doc></doc> 标记 
docStartFlagStr = '<doc id'
docEndFlagStr = '</doc>'

def doc2Sen(sour, dest):
    '''
    sour中的段落转换为句子，写入到dest中
    '''
    with codecs.open(sour, 'r', 'utf8') as fin:
        with codecs.open(dest, 'w', 'utf8') as fout:
            line = fin.readline()
            while(line):
                while((line.startswith(docStartFlagStr) or line.startswith(docEndFlagStr)) and line):
                    line = fin.readline()
                lineArr = list(segter.split_single(line))
                for i in range(len(lineArr)):
                    unit = lineArr[i]
                    if(len(unit.split(' ')) > 3):
                        fout.write(lineArr[i])
                        fout.write('\n')
                line = fin.readline()

def fileMerge(fileList, dest):
    '''
    将fileList中文件合并写入到dest中
    '''
    with codecs.open(dest, 'a+', 'utf8') as fout:
        for i in range(len(fileList)):
            fileName = fileList[i]
            print('fileName',fileName)
            with codecs.open(fileList[i], 'r', 'utf8') as fin:
                line = fin.readline()
                while(line):
                    fout.write(line)
                    line = fin.readline()
    
def clean(sour, dest):
    '''
    删除句子长度过短的句子，将保留的句子写入到dest中
    '''
    with codecs.open(sour, 'r', 'utf8') as fin:
        with codecs.open(dest, 'w', 'utf8') as fout:
            line = fin.readline()
            while(line):
                while((line.startswith(docStartFlagStr) or line.startswith(docEndFlagStr)) and line):
                    line = fin.readline()
                if(len(line.split(' ')) > 3):
                    fout.write(line)
                line = fin.readline()

def cleanEn():
    dir = 'result/enExtract/AA/wiki_'
    frange = 26
    for i in range(frange):
        fileName = ''
        if(i < 10):
            fileName = dir + '0' + str(i)
        else:
            fileName = dir + str(i)
        clean(fileName, fileName+'.clean')

def enDoc2Sen():
    dir = 'result/enExtract/AA/wiki_'
    frange = 26
    for i in range(frange):
        fileName = ''
        if(i < 10):
            fileName = dir + '0' + str(i)
        else:
            fileName = dir + str(i)
        doc2Sen(fileName, fileName+'.sen')
        
def cleanDe():
    dir = 'result/deExtract/AA/wiki_'
    frange = 26
    for i in range(frange):
        fileName = ''
        if(i < 10):
            fileName = dir + '0' + str(i)
        else:
            fileName = dir + str(i)
        clean(fileName, fileName+'.clean')

def deDoc2Sen():
    dir = 'result/deExtract/AA/wiki_'
    frange = 26
    for i in range(frange):
        fileName = ''
        if(i < 10):
            fileName = dir + '0' + str(i)
        else:
            fileName = dir + str(i)
        doc2Sen(fileName, fileName+'.sen')
def mergeDe():
    fileNL = []
    dir = 'result/deExtract/AA/wiki_'
    frange = 26
    for i in range(frange):
        fileName = ''
        if(i < 10):
            fileName = dir + '0' + str(i)
        else:
            fileName = dir + str(i)
        fileName += '.clean'
        fileNL.append(fileName)
    fileMerge(fileNL, dir + 'merge')
    
def mergeEn():
    fileNL = []
    dir = 'result/enExtract/AA/wiki_'
    frange = 11
    for i in range(10,frange):
        fileName = ''
        if(i < 10):
            fileName = dir + '0' + str(i)
        else:
            fileName = dir + str(i)
        fileName += '.clean'
        fileNL.append(fileName)
    fileMerge(fileNL, dir + 'merge')

def mergeTe():
    fileNL = []
    dir = 'result/teExtract/AA/wiki_'
    frange = 3
    for i in range(frange):
        fileName = ''
        if(i < 10):
            fileName = dir + '0' + str(i)
        else:
            fileName = dir + str(i)
        fileName += '.clean'
        fileNL.append(fileName)
    fileMerge(fileNL, dir + 'merge')    
        
if __name__=='__main__':
    #cleanEn()
    #enDoc2Sen()
    
    #cleanDe()
    #deDoc2Sen()
    mergeEn()
