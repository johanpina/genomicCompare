#!/usr/bin/python

"""
Este Script contiene una forma más compleja y pro de hacer el trimming(corte de calidad) de secuencias
y va a limpiar las secuencias por el valor phred de calidad y un threshold

"""

## Ojo actividad reescribir este codigo sin usar biopython


__author__ = "Juan Jovel"
__license__ = "GPL"
__email__ = "jovel@ualberta.ca"
__status__ = "Development"
__message__ = "Feel free to use and modify this script at your own risk"

import os
import sys
import re
from Bio import SeqIO


def main ():
    infile    = sys.argv[1]

    fastqFile = open(infile)
    outFile_name   = infile.replace('.fq', '_trimmer.fq')
    outFile = open(outFile_name, 'w')
    threshold  = 20
    min_length = 70

    for record in SeqIO.parse(fastqFile, "fastq"):
        id1          = record.id
        id1 = f'@{id1}'
        id1 = id1.replace('_', ' ')
        seq          = str(record.seq)
        qual_scores  = record.letter_annotations["phred_quality"]
        print(qual_scores)
        qual_symbols = ''.join([chr(score+33) for score in qual_scores])

        if(len([*filter(lambda x: x < threshold, qual_scores)]) > 0):
            index=next(x[0] for x in enumerate(qual_scores) if x[1] < threshold)
            seq = seq[0:index]
            qual_symbols = qual_symbols[0:index]

        if len(seq) >= min_length:
            to_print = f'{id1}\n{seq}\n+\n{qual_symbols}\n'
            outFile.write(to_print)

    fastqFile.close()
    outFile.close()


if __name__ == '__main__':
    main() 
