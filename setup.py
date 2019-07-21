#!/usr/bin/python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='CategorizerAI',
     version='0.4.2',
     author="Arpad Magosanyi",
     author_email="mag@kodekonveyor.com",
     description="An AI to categorize finantial transactions",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/kode-konveyor/categorizerai",
     scripts = ['CategorizerAI'],
     package_dir = {'':'src'},
     packages= setuptools.find_packages('src'),
     install_requires=[
          'tensorflow',
          'keras',
          'pandas',
          'psycopg2-binary',
          'winterboot>=0.3'
      ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
         "Operating System :: OS Independent",
     ],

 )
