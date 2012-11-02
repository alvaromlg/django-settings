# -*- coding: utf-8 -*-
import os

from distutils.core import setup
import django_settings


setup(
    name='django-settings',
    version=django_settings.__version__,
    description='Simple django reusable application for storing project settings in database.',
    author='Alvaro Pelegrina',
    author_email='alvaro@designhouseilo.fi',
    url='http://github.com/alvaromlg/django-settings',
    packages=['django_settings'],
    package_dir={
        'django_settings': 'django_settings'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
