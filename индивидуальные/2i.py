#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a = list(map(int, input().split()))

    C = int(input("Введите число"))
    t = 0
    for i in a:
        if i > C:
            t += 1
    print(t)

    answ = 1
    i_max = 0
    a_max = a[0]
    for i, item in enumerate(a):
        if abs(item) > abs(a_max):
            i_max, a_max = i, item

    for item in a[i_max+1:]:
        answ *= item
    print(answ)

    a.sort(key=lambda x: x >= 0)
    print(a)
