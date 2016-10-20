#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__, unittest
from multiprocessing.pool import ThreadPool


class testFrequenciaTermos(unittest.TestCase):
    threads = 10
    pool = ThreadPool(threads)


    def emParalelo(self, func, args):
        "Executa paralelamente a função func com os argumentos em args."
        resultados = self.pool.map_async(func, args)
        self.pool.close()
        self.pool.join()
        return resultados


    def test_frequencia(self):
        texto = 'lorem ' * 2 + 'lorem ipsum ' * 2
        frequencias = __init__.frequencias(texto, 2)
        self.assertEqual(
            frequencias,
            { 'lorem': 4, 'ipsum': 2, 'lorem ipsum': 2},
            'Valor obtido: %s' % frequencias)


if __name__ == '__main__':
    unittest.main()
