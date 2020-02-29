# -*- coding: utf-8 -*-

import os
import sys
from align_class import *

bam_file = sys.argv[1]
aln = open(bam_file)

# Extract supplementary alignments
os.system('samtools view -f 2048 ' + bam_file + ' > supp.sam')


def read_bam():
    seenset = set()
    pri_sup_pairs = {}

    alns = open('supp.sam')
    for aln in alns:
        QNAME = aln.split()[0]  # sequence name
        if QNAME not in seenset:
            seenset.add(QNAME)
            pri_sup_pairs[QNAME] = []
            sup1 = alignment(QNAME, aln.split()[2], aln.split()[3], aln.split()[15][5:], aln.split()[5], aln.split()[4],
                             aln.split()[11][5:])
            pri_sup_pairs[QNAME].append(sup1)
            SAtag = aln.split()[21].split(";")  # SA tag are seprated by ";"
            for i in range(len(SAtag) - 1):
                sups = alignment(QNAME,
                                 SAtag[i].split(',')[0][5:],
                                 SAtag[i].split(',')[1],
                                 SAtag[i].split(',')[2],
                                 SAtag[i].split(',')[3],
                                 SAtag[i].split(',')[4],
                                 SAtag[i].split(',')[5])
                pri_sup_pairs[QNAME].append(sups)
    return pri_sup_pairs
