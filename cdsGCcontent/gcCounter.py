import argparse

function='Calculates GC content for the coding parts of a given fasta genome, as well as for the non-coding parts and for the whole genome'

parser=argparse.ArgumentParser(description=function)
parser.add_argument('-v','--version',action='version',version='%(prog)s 1.0')
parser.add_argument('-i',metavar='FASTA_GENOME',help='input genome sequence file, fasta sequence may be interleaved',dest='fastaGenome',required=True)
parser.add_argument('-g',metavar='GFF_ANNOTATION',help='input gff annotation file containing positions for CDs',dest='gffAnnot',required=True)
args=parser.parse_args()

CDSpositions={}

with open(args.gffAnnot,'r') as fin:
    for line in fin:
        if not line.startswith('#') and line.split('\t')[2]=='CDS' and line.split('\t')[6]=='+':
            start=int(line.split('\t')[3])+1; end=int(line.split('\t')[4])+2
            CDSpositions[start]=end
with open(args.fastaGenome,'r') as fin:
    lines=[]
    for line in fin:
        if not line.startswith('>'):
            lines.append(line.strip('\n'))
    oneLineGenome=''.join(lines)
for i in CDSpositions:
    CDSseqs=[]
    CDSseqs.append(oneLineGenome[i:CDSpositions[i]])
    oneLineCDS=''.join(CDSseqs)
CDSa=oneLineCDS.count('A')+oneLineCDS.count('a')
CDSc=oneLineCDS.count('C')+oneLineCDS.count('c')
CDSg=oneLineCDS.count('G')+oneLineCDS.count('g')
CDSt=oneLineCDS.count('T')+oneLineCDS.count('t')
CDSgcCont=(CDSg+CDSc)/(CDSa+CDSc+CDSg+CDSt)
print(CDSgcCont)
