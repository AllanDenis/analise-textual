#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from pprint import pprint
import re

def frequencias(texto, minOcorrencias=1):
    palavras = re.split(r'\W?\s+\W?', texto)
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
    tamFrase = 1
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
            reverse=True)[:int(len(distFrequencia) * .2)]])
    return distFrequencia

if __name__ == '__main__':
    texto = ''''''
    frequencias(texto, 2)
