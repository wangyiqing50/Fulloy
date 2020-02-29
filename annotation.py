
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 01:49:32 2020

@author: 81943
"""

import sqlite3
import os
import pandas as pd

print(os.listdir())

annotation = pd.read_csv('gencode.v33lift37.annotation.gtf', sep='\t', header=None, skiprows=range(0, 5))
annotation.columns = ['seqid', 'source', 'featuretype', 'start', 'end', "score", "strand", "frame", "attributes"]
annotation = annotation[annotation.iloc[:, 2] == 'gene']
conn = sqlite3.connect('annotation_hg19.db')

annotation.to_sql(name='features3', con=conn)

conn.execute(
    "CREATE INDEX seqidstartend ON features3 (seqid,start,end)"
)

query = conn.execute(
    "SELECT * FROM features3 "
    "WHERE seqid = 'chr8' AND start < 119434616 AND end > 119434616;"
)
result = query.fetchall()
gene_type = result[0][-1].split(';')[1].split(' ')[2]
gene_name = result[0][-1].split(';')[2].split(' ')[2]

data = pd.read_table(, header = 0)
for index, row in data.iterrows():
    print(row['chrom1'], row['pri'], row['sup'])
    # print("WHERE seqid = " + str(row['chrom']) +" AND start < "+ str(row['pri'])+ " AND end > " + str(row['pri']) +  ";")
    # break
    pri_query = conn.execute(
        "SELECT * FROM features "
        "WHERE seqid = '" + str(row['chrom1']) + "' AND start < " + str(row['pri']) + " AND end > " + str(
            row['pri']) + ";"
    )
    pri_result = pri_query.fetchone()
    gene_type = result[0][-1].split(';')[1].split(' ')[2]
    gene_name = result[0][-1].split(';')[2].split(' ')[2]
    sup_query = conn.execute(
        "SELECT * FROM features "
        "WHERE seqid = '" + str(row['chrom1']) + "' AND start < " + str(row['sup']) + " AND end > " + str(
            row['sup']) + ";"
    )
    sup_result = sup_query.fetchone()
    gene_type = result[0][-1].split(';')[1].split(' ')[2]
    gene_name = result[0][-1].split(';')[2].split(' ')[2]


def range_overlap(range1, range2):
    A1, A2 = range1[0], range1[-1]
    B1, B2 = range2[0], range2[-1]
    begin = lambda A1, B1: list(range(A1, B1 + 1)) if A1 <= B1 else list(range(B1, A1 + 1))
    end = lambda A2, B2: list(range(A2, B2 + 1)) if A1 <= B1 else list(range(B1, A1 + 1))
    return len(max(begin(A1, B1)) - min(end(A2, B2))) >= 0