from distutils.core import setup
from Cython.Build import  cythonize

build_dir = 'bulid'
build_tmp_dir = 'bulid/temp'
setup(
    name='2006119220王晓安',
    ext_modules=cythonize(['login.py']),
    script_args=["install"]
)