# -*- coding: utf-8 -*-
"""aulacurso.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O9QElQc0gjV22DB93o4ToHwFjHHkJZzX
"""

import pandas as pd
import json
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'nome' : ['Vinicius', 'Gustavo', 'Chrisley', 'João'],
    'idade' : [19, 19, 22, 50],
    'genero': ['M', 'M', 'M', 'M'],
    'estado': ['MG', 'MG', 'MG', 'MG'],
    'num_filhos': [1, 2, 3, 0],
    'num_pets': [4, 2, 3, 1]
})

df

df.plot(kind="line", x="nome", y="idade", color="green")
plt.show()