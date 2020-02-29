from CIGAR_rewriter import *


class alignment:
    def __init__(self, seqname, chromo, pos, strand, CIGAR, MAPQ, NM):
        self.seqname = seqname
        self.chromo = chromo
        self.pos = pos
        self.strand = strand
        self.CIGAR = CIGAR
        self.MAPQ = MAPQ
        self.NM = NM

    def rewrite_cigar(self):
        return rewrite(self.CIGAR)

    def mapped_cigar_length(self):
        pattern = re.compile('([MIDNSH])')
        values = pattern.split(self.CIGAR)[:-1]
        pairs = (values[n:n + 2] for n in range(0, len(values), 2))
        operation = {"S": 1, "H": 1, "D": 1, "M": 2, "N": 1, "I": 2}
        length = 0
        for pair in pairs:
            op = pair[1]

            if operation[op] == 2:
                length += int(pair[0])

        return length

    def break_coord(self):
        start = int(self.pos)
        rewritten = rewrite(self.CIGAR)
        pattern = re.compile('([SHMN])')
        values = pattern.split(rewritten)[:-1]
        left = True
        if int(values[0]) > int(values[-2]):
            pass
        else:
            left = False
        if left:
            return [str(self.chromo), start - 1, start]
        else:
            values = values[2:-2]
            pairs = (values[n:n + 2] for n in range(0, len(values), 2))
            inner_length = 0
            for pair in pairs:
                inner_length += int(pair[0])
            return [str(self.chromo), start + inner_length, start + inner_length + 1]
