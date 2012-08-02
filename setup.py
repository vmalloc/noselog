import os
import itertools
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "noselog", "__version__.py")) as version_file:
    exec(version_file.read())

setup(name="noselog",
      classifiers = [
          "Programming Language :: Python :: 2.6",
          ],
      description="Nose plugin for controlling test logs output",
      license="BSD",
      author="Rotem Yaari",
      author_email="vmalloc@gmail.com",
      version=__version__,
      packages=find_packages(exclude=["tests"]),
      install_requires=[],
      scripts=[],
      namespace_packages=[],
      entry_points = {
          'nose.plugins.0.10' : [
              'noselog = noselog.nose_plugin:NosePlugin',
              ]
          }

      )
