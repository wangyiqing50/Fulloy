#!/usr/bin/python
import sys
import getopt


def usage():
    print("""
    fusion_detector.py:  A pipline for detecting gene 
    fusions using full length transcripts
    
    Usage: fusion_detector [options] <filename>
    Options:
     -h                    Brief decription and help message
     -M                    Min read number to support a 
                           fusion event
     -l                    Min range width for a breakpoint
     -R                    Min distant of breakpoints if on 
                           the same chromosome
     Alignment:
     -A                    Start from alignment
     -B                    Choose aligner, default is minimap2
     -G                    used in minimap2, max intron length
     Input/Output:
     -c                    Input in fasta format
     -b                    Input in bam format
     -O                    Output folder
     Annotations:
     -D                    Annotation file in GTF format
     -L                    Store annotation table locally for 
                           for reuse
    """)


o, a = getopt.getopt(sys.argv[1:], 'l:h')
opts = {}
#seqlen = 0

for k, v in o:
    opts[k] = v
if '-h' in opts.keys():
    usage()
    sys.exit()
if len(a) < 1:
    usage()
    sys.exit('input fasta file is missing')


