#!/usr/bin/env python3
import sys

# Program to join exons 1 and 2 from different files with different orders
# Run like: python3 programName exons1File exons2File joinedExonsFileNAme
exons1=sys.argv[1]
exons2=sys.argv[2]
uniSeqs=sys.argv[3]

uniDic={}

def makeDic(fastaFile):
    ids=[];seqs=[];seqDic={}
    with open(fastaFile) as infile:
        for line in infile:
            if line.startswith('>'):
                ids.append(line.rstrip('\n'))
            else:
                seqs.append(line.rstrip('\n'))
        for i in range(len(ids)):
            seqDic[i]=ids[i],seqs[i]
    return seqDic

seqDic1=makeDic(exons1)
seqDic2=makeDic(exons2)

for i in range(len(seqDic1)):
    for j in range(len(seqDic2)):
        if seqDic1[i][0]==seqDic2[j][0]:
            uniDic[seqDic1[i][0]]=seqDic1[i][1]+seqDic2[j][1]

with open(uniSeqs,'w') as outfile:
    for i in sorted(uniDic):
        print(i,uniDic[i],sep='\n',file=outfile)
