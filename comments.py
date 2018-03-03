#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import copy
from fuzzywuzzy import fuzz
from pprint import pprint
import codecs

def is_kirill(comment):
    kirill = (u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    find_kirill = [x for x in kirill if x in comment.lower()]
    if find_kirill == []:
        return False
    else:
        return True


def tanimoto(s1, s2):
    a, b, c = len(s1), len(s2), 0.0
    for sym in s1:
        if sym in s2:
            c += 1
    print(a, b, c)
    if is_kirill(s1) == is_kirill(s2):
        return c / (a + b - c)
    else:
        return 0


def clean_array(FA, FAA):
    reject = [[16, 15], [203, 202], [187, 101], [200, 199], [48,47], [119,116], [122,116], [152,147], [157, 147], [187, 184], [191, 101]]
    CA = copy.copy(FA)
    accord = [i for i in range(len(CA))]
    accord2 = []
    i = 0
    j = 0
    while 1:
        i+=1
        if i > len(CA)-1:
            break
        for j in range(i):
            cmp = fuzz.ratio(CA[i], CA[j])
            if cmp > 60:
                if [accord[i]+1, accord[j]+1] not in reject:
                    print(CA[i])
                    print(CA[j])
                    CA.pop(i)
                    print('deleted ' + str(accord[i]+1) + ' matches with ' + str(accord[j]+1))
                    print('CMP!!!! = ', cmp)
                    print('---------------------------------')
                    accord2.append([accord[i], j])
                    accord.pop(i)
                    i-=1
                    break
    for i in range(len(accord)):
        accord2.append([accord[i], i])
    accord2.sort()
    accord = {}
    for lst in accord2:
        accord[lst[0]] = lst[1]
    CAA = copy.deepcopy(FAA)
    for ref in CAA:
        for i in range(len(CAA[ref])):
            CAA[ref][i] = accord[CAA[ref][i]]+1
    return CA, CAA


# загрузка данных
import io
with io.open('comments.txt', encoding='utf-8') as file:
    FA = file.readlines()
FAA = json.load(open('array.txt'))

pprint(FAA)


#for comment in FA:
#    print(comment)
#    print(is_kirill(comment))

#очистка
CA, CAA = clean_array(FA, FAA)
pprint(CAA)


#вывод
i = 0
for comment in CA:
    i+=1
    print('['+str(i)+'] '+comment)

x = [i for i in range(len(CAA))]
for i in x:
    print(str(i+1)+'--'+str(CAA[str(i+1)]))