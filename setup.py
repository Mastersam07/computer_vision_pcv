#!/usr/bin/env python

from distutils.core import setup

setup(name='pcv',
        version='1.1',
        author='Jan Erik Solem',
        mod='Abada Samuel',
        url='https://github.com/jesolem/PCV',
        url2='https://github.com/mastersam07/pcv',
        packages=['pcv', 'pcv.classifiers', 'pcv.clustering', 'pcv.geometry',
                'pcv.imagesearch', 'pcv.localdescriptors', 'pcv.tools'],
        requires=['NumPy', 'Matplotlib', 'SciPy'],
        )
