from setuptools import setup, find_packages
from os import path


here = path.join(path.abspath(path.dirname(__file__)), 'garpix_utils')

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='garpix_utils',
    version='1.10.0-rc26',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/garpixcms/garpix_utils',
    author='Garpix LTD',
    author_email='info@garpix.com',
    license='MIT',
    packages=find_packages(exclude=['testproject', 'testproject.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django >= 1.11, < 5',
        'django-uuslug >= 1.2.0',
        'django-polymorphic-tree-for-garpix-page >= 2.2.2',
        'djangorestframework >= 3.13.0'
    ],
)
