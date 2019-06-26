
from distutils.core import setup, Extension

leap_module = Extension(
    '_leap',
    sources=['Leap_wrap.cxx', 'LeapPython.cpp'],
)

setup(name='Leap',version='3.3.0',author='SWIG Docs',
    description="""LeapMotion Wrapper for Python 3.3""",
     ext_modules=[leap_module]
    # py_modules=["leap_module"],
    )
