from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cython.pyx'))

## ========= ( python build_cython.py build_ext --inplace ) ===================== ##
