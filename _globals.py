"""Vars and modules shared by all notebooks.
"""

import pandas as pd
import numpy as np
import matplotlib as plt
from pathlib import Path


__files__ = [
    "data.csv",
    "data_concelhos.csv",
    "data_concelhos_14dias.csv",
    "data_concelhos_incidencia.csv",
    "data_concelhos_new.csv",
    "rt.csv",
    "vacinas.csv",
    "vacinas_detalhe.csv",
]

class PATH:
    ROOT = Path(".")
    DATA = ROOT/'covid19pt-data'
    data = DATA/"data.csv"
    
