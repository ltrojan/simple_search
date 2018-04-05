#!/usr/bin/env python

import os
from setuptools import setup


version = '0.0.1'
local_dir = os.path.dirname(__file__)
if len(local_dir) == 0:
    local_dir = '.'
try:
    with open(os.sep.join([local_dir, 'VERSION']), 'r') as fid:
        version = fid.read().strip()
except:
    pass


setup(
    name='simple_search',
    version=version,
    description='Simple Search',
    packages=[
        "simple_search",
    ],
    scripts=["scripts/csv_search.py"]
)
