#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from pprint import pprint
from sys import argv
from os.path import isfile
import re

def frequencias(texto, minOcorrencias=1):
    palavras = re.findall(r'\S+', texto)
    palavras = [p.lower().strip() for p in palavras]
    if len(palavras) == 0: return {}
    termosComuns = set('abcdefghijklmnopqrstuvwxyz0123456789')
    termosComuns.update({''})
    termosComuns.update(
        set((' em na são que dos uma para como se um é das de no os nos à as ' +
            'sob foi com esse ser sobre esses essas pois eles não mais tem ao por ' +
            'do da sem seu sua quais ou').split()))
    distFrequencia = ocorrencias = {}
    numPalavras = len(palavras)
    tamFrase = 3
    while set(ocorrencias.values()) != {1}:
        ocorrencias = defaultdict(int)
        print('Contando frases com %d palavras...' % tamFrase)
        for i in range(numPalavras)[: numPalavras - tamFrase : tamFrase]:
            frase = ' '.join(palavras[i:i + tamFrase]).strip()
            if frase in termosComuns:
                continue
            else:
                ocorrencias[frase] += 1
        if not ocorrencias: return {}
        distFrequencia.update(
            {frase:freq for frase,freq in ocorrencias.items()
                if freq >= minOcorrencias}
        )
        tamFrase += 1
    pprint([frase[::-1] for frase in
        sorted(distFrequencia.items(),
            key=lambda x: x[1],
            reverse=True)])
    return distFrequencia

if __name__ == '__main__':
    texto = ''
    try:
        if isfile(argv[1]):
            with open(argv[1]) as arquivo:
                frequencias(arquivo.read(), 2)
    except IndexError as e:
        frequencias(texto, 2)
