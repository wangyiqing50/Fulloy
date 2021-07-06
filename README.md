# Fulloy
An efficient tool for discovery of gene fusion from isoseq data
## About
Gene fusions, which hybrid two or more independent genes, always play a driving role in tumorigenesis and progression. Therefore, they become important diagnostic and prognostic biomarkers and are potential therapeutic targets. It is critical to comprehensively characterize gene fusions Despite its dominating status in “omics” studies, Next generation sequencing (NGS) still has inevitable limitations to accurately identify gene fusions caused by the short-read length. For example, it is extremely challenging to discover fusion genes in repetitive regions such as tandem repeats, tandem duplications, long interspersed nuclear elements (LINEs), segmental duplications, etc., where short read alignments tend to be ambiguous.   In recent years, long read sequencing technologies have demonstrated great potential in detecting gene fusions thanks to their ultra-long read lengths. For instance, Pacific Bioscience (PacBio) has proposed the iso-seq platform, which can be used to sequence the whole set of mRNA molecules at their full lengths. It can generate sequences with an average read length of over 10,000 bp and up to 60,000 bp. This offers a great opportunity for accurate and comprehensive identification of gene fusions. However, the methods for gene fusion detection using long reads are insufficient and the existing tools are far from optimal. Here, we present Fulloy, an efficient tool for comprehensive gene fusion detection from long-read sequencing data. First, it aligns long sequencing reads to the reference genome. In our pipeline, minimap2 is chosen as the default aligner. Then it collects the all supplementary alignments and infer structural variations (SVs) based on the primary and supplementary alignments. Next, the SVs will be annotated and only the events involving in more than two genes will be selected as candidates. To confidently report a gene fusion event, evidence such as the number of supporting reads, genomic evidence, annotation information of where the breakpoints occur (whether involving in lnc RNA, in exons, or in high repetitive region), splicing patterns (GT-AG), strands, etc. will be collected and evaluated. After applying a filter, it will output a final call set in VCF format. To evaluate the performance of Fulloy, we benchmarked it on a public iso-seq dataset from SK-BR-3 cancer cell line. We have successfully detected 15 previously reported fusions. In addition, we also found 7 novel fusion candidates with robust evidence. If starting from bam file, it took less than 2 minutes to run Fulloy on this dataset with a peak memory of roughly 700MB. These results suggest that Fulloy can accurately and efficiently detect gene fusion events. In the future, we will extensively test and improve Fulloy on more dataset. Written in Python, the alpha version of Fulloy is freely available at https://github.com/wangyiqing50/Fulloy under MIT license. 
## Prerequisite
Python (version 3) <br>
Samtools <br>
Minimap2 <br>
## Download
```sh
git clone https://github.com/wangyiqing50/Fulloy.git
```
## Install
```
pip install -r requisites.txt
```
## Quick start
### Start from CCS read
```sh
python fusion_detector.py -a -f path_to_the_CCS_read -r path_to_the_GTF_file -o output_folder
```
### Start from alignment file
```sh
python fusion_detector.py -f path_to_the_bam_file -r path_to_the_GTF_file -o output_folder 
```
