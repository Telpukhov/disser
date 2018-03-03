import json
from pprint import pprint

def tanimoto(s1, s2):
    a, b, c = len(s1), len(s2), 0.0
    for sym in s1:
        if sym in s2:
            c += 1
    return c / (a + b - c)


def clean_array(FA):
    for i in range(len(FA)):
        max = 0
        for j in range(i):
            cmp = tanimoto(FA[i], FA[j])
            if max < cmp:
                max = cmp
        print(str(i)+' - ', str(max))


with open('comments.txt', 'r') as file:
    FA = file.readlines()

FAA = json.load(open('array.txt'))
pprint(FAA)