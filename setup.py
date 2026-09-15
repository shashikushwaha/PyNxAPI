from setuptools import setup
from Cython.Build import cythonize

setup(
    name="NAL",
    ext_modules=cythonize("NAL/*.py", compiler_directives={'language_level' : "3"}),
    zip_safe=False,
)