print("Bon courage pour la suite ")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import normalize

from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import recall_score, f1_score
carac = pd.read_csv("step1/carac.csv",sep=';')
lieux = pd.read_csv("step1/lieux.csv",sep=';',low_memory=False)
veh = pd.read_csv("step1/veh.csv",sep=';')
vict = pd.read_csv("step1/vict.csv",sep=';')
victime = vict.merge(veh,on=['Num_Acc','num_veh'])
accident = carac.merge(lieux,on = 'Num_Acc')
victime = victime.merge(accident,on='Num_Acc')
nan_values = victime.isna().sum()

nan_values = nan_values.sort_values(ascending=True)*100/127951

ax = nan_values.plot(kind='barh', 
                     figsize=(8, 10), 
                     color='#AF7AC5',
                     zorder=2,
                     width=0.85)

ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.tick_params(axis="both", 
               which="both", 
               bottom="off", 
               top="off", 
               labelbottom="on", 
               left="off", 
               right="off", 
               labelleft="on")

vals = ax.get_xticks()

for tick in vals:
  ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

nans = ['v1','v2','lartpc',
       'larrout','locp','etatp',
       'actp','voie','pr1',
       'pr','place']

victime = victime.drop(columns = nans)
victime = victime.dropna()
victime.to_csv('step2/missing_values_deleted.csv', index=False)