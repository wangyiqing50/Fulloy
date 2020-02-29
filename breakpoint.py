def type_classification(pri_sup_pairs, distance=100000):
    deletion = {}
    inversion = {}
    translocation = {}
    for key, value in pri_sup_pairs.items():
        if value[0].chromo == value[1].chromo:
            if abs(int(value[0].pos) - int(value[1].pos)) > distance:
                if value[0].strand == value[1].strand:
                    deletion[key] = value
                else:
                    inversion[key] = value

        else:
            translocation[key] = value
    return deletion, inversion, translocation

