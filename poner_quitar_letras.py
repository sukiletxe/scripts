#!/usr/bin/env python
from __future__ import print_function
import os, shutil, sys
programa = os.path.realpath(__file__) if getattr(sys, 'frozen', False) == False else sys.executable
os.chdir(os.pardir)
print("Analizando carpeta...")
lista = [x for x in sorted(os.listdir(os.curdir), key = lambda k: len(k)) if os.path.isdir(x)]
lista.remove(os.path.relpath(os.path.dirname(programa), os.curdir))
if len(lista[-1]) >1:
    print('Ordenando letra por letra...')
    for elem in sorted(lista, key = lambda k: k.lower()):
        if len(elem) > 1:
            primera=elem[0].upper()
            if not os.path.isdir(primera):
                os.mkdir(primera)
            shutil.move(elem, primera)
            print(os.path.join(primera, elem))
else:
    print('Quitando orden por letras...')
    for elem in sorted(lista, key = lambda k: k.lower()):
        for x in sorted(os.listdir(elem), key = lambda k: k.lower()):
            shutil.move(os.path.join(elem, x), x)
        os.rmdir(elem)
        print(elem)
