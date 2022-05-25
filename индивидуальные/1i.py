#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    minimum = min(A)
    print("Наименьший элемент", minimum)

    for x in range(len(A)):
        if A[x] == minimum:
            A[-1], A[x] = A[x], A[-1]
    print("Преобразованный элемент", A)