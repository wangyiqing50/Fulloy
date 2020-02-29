import re

pattern = re.compile('([MIDNSHPX=])')
values = pattern.split('20S71M2901N345M606H')[:-1]
pairs = (values[n:n + 2] for n in range(0, len(values), 2))

rewritten = ''  # Final
merge_len = 0  # D is ignored
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

print(rewritten[2:])

i = 0
for key, value in pri_sup_pairs.items():
    if len(value) == 2:
        i += 1