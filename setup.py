#!/usr/bin/env python
'''
Installs pymodbus using distutils

Run:
    python setup.py install
to install the package from the source archive.

For information about setuptools
http://peak.telecommunity.com/DevCenter/setuptools#new-and-changed-setup-keywords
'''
#---------------------------------------------------------------------------#
# initialization
#---------------------------------------------------------------------------#
try: # if not installed, install and proceed
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

try:
    from setup_commands import command_classes
except ImportError:
    command_classes = {}
from pymodbus import __version__, __author__

#---------------------------------------------------------------------------#
# configuration
#---------------------------------------------------------------------------#
setup(
    name  = 'pymodbus',
    setup_requires=['vcversioner'],
    vcversioner={
        'version_module_paths': ['pymodbus/_version.py'],
    },
    description = 'A fully featured modbus protocol stack in python',
    long_description='''
    Pymodbus aims to be a fully implemented modbus protocol stack.
    Its orignal goal was to allow simulation of thousands of
    modbus devices on a single machine for monitoring software testing.
    ''',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: X11 Applications :: GTK',
        'Framework :: None',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: System :: Networking',
        'Topic :: Utilities'
    ],
    keywords = 'modbus, scada',
    author = __author__,
    author_email = 'bashwork@gmail.com',
    maintainer = "Bryan Bates",
    maintainer_email = 'bryan.bates@synapse-wireless.com',
    url='https://github.com/synapse-wireless/pymodbus',
    license = 'BSD',
    packages = find_packages(exclude=['examples', 'test']),
    exclude_package_data = {'' : ['examples', 'test', 'tools', 'doc']},
    py_modules = ['ez_setup'],
    platforms = ['Linux', 'Mac OS X', 'Win'],
    include_package_data = True,
    zip_safe = True,
    install_requires = [
        'pyserial >= 2.6'
    ],
    extras_require = {
        'quality'   : [ 'coverage >= 3.5.3', 'nose >= 1.2.1', 'mock >= 1.0.0', 'pep8 >= 1.3.3' ],
        'documents' : [ 'sphinx >= 1.1.3' ],
    },
    test_suite = 'nose.collector',
    cmdclass = command_classes,
)
