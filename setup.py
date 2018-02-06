from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
import numpy

setup(
    maintainer='Sun jiadong',
    name='fm_py',
    packages=find_packages(),
    url='https://github.com/sunjiadong/fm_for_myown',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("pyfm_fast", ["pyfm_fast.pyx"],
        libraries=["m"],include_dirs=[numpy.get_include()])]
)
