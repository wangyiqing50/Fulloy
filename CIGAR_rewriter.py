import re


def rewrite(cigar):
    # Input a cigar string
    # Output a rewritten cigar string
    pattern = re.compile('([MIDNSHPX=])')
    values = pattern.split(cigar)[:-1]
    pairs = (values[n:n + 2] for n in range(0, len(values), 2))

    rewritten = ''  # Final
    merge_len = 0  # D and N are ignored
    operation = {"S": 1, "H": 1, "D": 2, "M": 2, "N": 1, "I": 3}
    for pair in pairs:
        op = pair[1]

        if operation[op] == 1:
            rewritten += str(merge_len) + "M" + pair[0] + pair[1]
            merge_len = 0

        if operation[op] == 2:
            merge_len += int(pair[0])

        if operation[op] == 3:
            pass
    if values[1] in ['S', 'H']:
        return rewritten[2:]
    elif values[-1] in ['S', 'H']:
        return rewritten[:-2]
    else:
        return rewritten
