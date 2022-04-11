import pandas as pd
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# données
df_data = pd.read_csv("churner_train_data_set.csv")
list_binary = df_data.columns[df_data.isin([0, 1, float('nan')]).all()]
nom_column = df_data.columns.tolist()



#variable booléenne 
def is_binary(list_binary, nom_column):
    if nom_column in list_binary:
        return True
    else:
        return False



#Création des classes pour chaque variables
def creation_Collonnes(element, nbClasses):
    for i in range(0, nbClasses):
        df_data[element + "-" + str(i)] = 0


#retourne les indexes des 2 classes pour les booléens
def Index_2_Classes(collonne):
    # False
    classe1 = df_data.index[(df_data[collonne] == 0)]
    # True
    classe2 = df_data.index[(df_data[collonne] == 1)]

    return classe1, classe2

#retourne les indexes des 3 classes
def Index_3_Classes(collonne):
    max = df_data[collonne].max()
    min = df_data[collonne].min()
    #std = df_data[collonne].std()
    #moy = df_data[collonne].mean()

    borne1 = (max - min) / 3 + min
    borne2 = (2 / 3) * (max - min) + min

    #borne1 = moy - std
    #borne2 = moy + std

    classe1 = df_data.index[(df_data[collonne] < borne1)]
    classe3 = df_data.index[(df_data[collonne] > borne2)]
    classe2 = ((df_data.index ^ classe1)^ classe3)

    return classe1,classe2, classe3

#parcour chaque collone de notre dataframe (excepté la dernière)
for element in nom_column[:-1]:



    # Si la variable est non binaire
    if not is_binary(list_binary, element):

        #creation_Collonnes(element, 3)
        (x,y,z) = Index_3_Classes(element)
        for i in x:
            df_data.at[i,element] = element + "-1"
        for i in y:
            df_data.at[i,element] = element + "-2"
        for i in z:
            df_data.at[i,element] = element + "-3"


    # Si la variable est binaire ==> 2 classes
    else:
        #creation_Collonnes(element, 2)
        (x,y) = Index_2_Classes(element)
        for i in x:
            df_data.at[i, element] = element + "-1"
        for i in y:
            df_data.at[i, element] = element + "-2"

    #df_data.drop(element, inplace=True, axis=1)
    print("Collonne Traité")

df_data = pd.get_dummies(df_data)

df_data['Var_a_expliquee'] = df_data['churner']
df_data.drop('churner', inplace=True, axis=1)

#Export en Csv
df_data.to_csv('Symbolique.csv', index=False, sep=';')
