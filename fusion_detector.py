from bam_reader import *
from align_class import *
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from breakpoint import *
import os
import sys
import usage
bam_file = sys.argv[1]
aln = open(bam_file)

# Extract supplementary alignments
os.system('samtools view -f 2048 ' + bam_file + ' > supp.sam')

pri_sup_pairs = read_bam()
popkey = []
for key, align in pri_sup_pairs.items():
    if len(align) == 1:
        popkey.append(key)

for key in popkey:
    pri_sup_pairs.pop(key)

deletion, inversion, translocation = type_classification(pri_sup_pairs, distance=100000)

# Deletion
del_frame = []
for m in range(1, 23):
    breakpoints_left = []
    sups = []
    for key, align in deletion.items():
        if align[1].chromo == 'chr' + str(m):
            breakpoints_left.append(align[1].break_coord()[1])
            sups.append([align[0].chromo, align[0].break_coord()[1]])
    sups = pd.DataFrame(sups)
    breakpoints_left = np.array(breakpoints_left).reshape(-1, 1)
    clustering = DBSCAN(eps=10, min_samples=4).fit(breakpoints_left)
    labels = clustering.labels_

    for j in range(max(labels)):
        group = []
        for i in range(labels.shape[0]):
            if labels[i] == j:
                group.append(i)
        # breakpoints_left[group]
        if abs(max(sups.iloc[group, 1]) - min(sups.iloc[group, 1])) < 20:
            del_frame.append(['chr' + str(m), int(breakpoints_left[group].mean()), int(sups.iloc[group, 1].mean()), len(breakpoints_left[group])])
del_frame = pd.DataFrame(del_frame, columns=('chromosome', 'pri', 'sup', 'number'))

# Translocation
tra_frame = []
for m in range(1, 23):
    breakpoints_left = []
    sups = []
    for key, align in translocation.items():
        if align[1].chromo == 'chr' + str(m):
            breakpoints_left.append(align[1].break_coord()[1])
            sups.append([align[0].chromo, align[0].break_coord()[1]])
    sups = pd.DataFrame(sups)
    breakpoints_left = np.array(breakpoints_left).reshape(-1, 1)
    clustering = DBSCAN(eps=10, min_samples=3).fit(breakpoints_left)
    labels = clustering.labels_

    for j in range(max(labels)):
        group = []
        for i in range(labels.shape[0]):
            if labels[i] == j:
                group.append(i)
        # breakpoints_left[group]
        if abs(max(sups.iloc[group, 1]) - min(sups.iloc[group, 1])) < 100:
            tra_frame.append(['chr' + str(m), int(breakpoints_left[group].mean()), int(sups.iloc[group, 1].mean()), len(breakpoints_left[group])])
tra_frame = pd.DataFrame(tra_frame, columns=('chromosome', 'pri', 'sup', 'number'))

# Inversion
inv_frame = []
for m in range(1, 23):
    breakpoints_left = []
    sups = []
    for key, align in inversion.items():
        if align[1].chromo == "chr" + str(m):
            breakpoints_left.append(align[1].break_coord()[1])
            sups.append([align[0].chromo, align[0].break_coord()[1]])
    sups = pd.DataFrame(sups)
    breakpoints_left = np.array(breakpoints_left).reshape(-1, 1)
    clustering = DBSCAN(eps=10, min_samples=4).fit(breakpoints_left)
    labels = clustering.labels_

    for j in range(max(labels)):
        group = []
        for i in range(labels.shape[0]):
            if labels[i] == j:
                group.append(i)
        # breakpoints_left[group]
        if abs(max(sups.iloc[group, 1]) - min(sups.iloc[group, 1])) < 20:
            inv_frame.append(['chr' + str(m), int(breakpoints_left[group].mean()), int(sups.iloc[group, 1].mean()), len(breakpoints_left[group])])
inv_frame = pd.DataFrame(inv_frame, columns=('chromosome', 'pri', 'sup', 'number'))

if __name__ == '__main__':
    pass
