# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:01:27 2019

@author: markus@volantis.io
"""

import sys
import pandas as pd
import numpy as np
from datetime import date



arg = sys.argv[1]

def stockConverter(filenameInput : str):

    """
    This function is used for converting
    datetime to timestamp dataType column
    :params:
    :fileName -> string
    :return value -> None
    """
    df = pd.read_csv(filenameInput)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['timestamp'] = df.timestamp.values.astype(np.int64) // 10 ** 6
    df = df[:8]
    filename = filenameInput + str(date.today()) + ".csv"
    df.to_csv(filename)


if __name__ == '__main__':
    #test Function
    stockConverter(arg)

    #> python conv.py "<inputFilename>"
