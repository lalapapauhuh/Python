import sys
from cx_Freeze import setup, Executable

base = None 
if sys.platform == 'win32':
    base == 'win32GUI'

execubatles = [
    Executable('calculadora1.1.py', base=base)
]

setup(name='Calculadora App',
    version = '1.1',
    description='Calculadora em Python',
    execubatles=execubatles
)
