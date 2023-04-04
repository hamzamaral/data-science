# -*- coding: utf-8 -*-
"""
Created on Wed Jun 1 00:18:36 2022

@author: HAMZA
"""


# This Python 3 environment comes with many helpful analytics libraries installedfcfc
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-pythonfcfc
# For example, here's several helpful packages to load in fcddexqdecfcfcfc

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

#dechvgdhbcdofbhhbdkxlömnjcefd2dc2decıuhdecıudeıcdecıunfıuencufencıufecfffffffffffffffffffff
# For examplecefcfc, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

import os
for dirname, _, filenames in os.walk("/kaggle/input"):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# Any results you write to the current directory are saved as output.
